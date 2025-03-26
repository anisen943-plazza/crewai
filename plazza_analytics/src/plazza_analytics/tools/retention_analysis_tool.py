# src/plazza_analytics/tools/retention_analysis_tool.py

import os
import psycopg2
import psycopg2.extras
from langchain.tools import BaseTool
from plazza_analytics.tools.config import DB_CONNECTION_VARS

class RetentionAnalysisTool(BaseTool):
    name = "RetentionAnalysisTool"
    description = """Perform comprehensive customer retention analysis across the Plazza ecosystem.
    Calculates repeat rates, time between purchases, top products, and discount impact."""

    _retention_cache = None  # Cached results for reuse
    
    def run(self, generate_visuals: bool = True):
        """Run comprehensive retention analysis on the user_transactions database.
        
        Args:
            generate_visuals: Whether to generate visualizations (default: True)
        """
        return self._run(generate_visuals=generate_visuals)
    
    def _run(self, generate_visuals: bool = True) -> str:
        try:
            results = []
            conn_str = os.getenv(DB_CONNECTION_VARS["user_transactions"])
            if not conn_str:
                return "❌ DATABASE_URL_USER_TRANSACTIONS not set"

            conn = psycopg2.connect(conn_str)

            # QUERY 1: Repeat customer %
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                SELECT 
                    COUNT(DISTINCT contact_id) as total_customers,
                    COUNT(DISTINCT CASE WHEN order_count > 1 THEN contact_id END) as repeat_customers
                FROM (
                    SELECT contact_id, COUNT(*) as order_count
                    FROM orders
                    WHERE status = 'paid'
                    AND order_id NOT LIKE '%TEST%'
                    AND order_id NOT LIKE 'POD-WEBHOOK%'
                    GROUP BY contact_id
                ) sub
                """)
                row = cursor.fetchone()
                if row:
                    total = row["total_customers"]
                    repeat = row["repeat_customers"]
                    results.append("## Retention Summary")
                    results.append(f"- Total customers: {total}")
                    results.append(f"- Repeat customers: {repeat}")
                    results.append(f"- One-time customers: {total - repeat}")
                    results.append(f"- Repeat rate: {round((repeat / total) * 100, 1) if total else 0}%\n")

            # QUERY 2: Avg time between purchases
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                WITH ranked_orders AS (
                    SELECT contact_id, created_at,
                           ROW_NUMBER() OVER (PARTITION BY contact_id ORDER BY created_at) AS rn
                    FROM orders
                    WHERE status = 'paid'
                      AND order_id NOT LIKE '%TEST%'
                )
                SELECT 
                    AVG(EXTRACT(DAY FROM r2.created_at - r1.created_at)) as avg_days
                FROM ranked_orders r1
                JOIN ranked_orders r2 
                  ON r1.contact_id = r2.contact_id AND r1.rn = 1 AND r2.rn = 2
                """)
                row = cursor.fetchone()
                if row and row["avg_days"]:
                    results.append("## Time Between Purchases")
                    results.append(f"- Average days between 1st and 2nd order: {round(row['avg_days'], 1)} days\n")

            # QUERY 3: Discount impact (optional)
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
                cursor.execute("""
                SELECT 
                    ROUND(discount_pct, -1) as bracket,
                    COUNT(DISTINCT contact_id) as customers
                FROM (
                    SELECT contact_id,
                           (1 - bill_total_amount / NULLIF(item_total, 0)) * 100 as discount_pct
                    FROM orders
                    WHERE status = 'paid'
                      AND item_total > 0
                      AND order_id NOT LIKE '%TEST%'
                ) sub
                GROUP BY ROUND(discount_pct, -1)
                ORDER BY bracket
                """)
                rows = cursor.fetchall()
                if rows:
                    results.append("## Discount Impact")
                    for row in rows:
                        results.append(f"- {int(row['bracket'])}% bracket: {row['customers']} customers")

            self._retention_cache = "\n".join(results)
            return self._retention_cache

        except Exception as e:
            return f"❌ Retention analysis failed: {str(e)}"
        finally:
            if 'conn' in locals() and conn:
                conn.close()