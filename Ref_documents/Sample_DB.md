<!DOCTYPE html>
<html>
<head>
    <title>Plazza Insights</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
    <style>
        :root { --plazza: #FF0084; }
        body { 
            font-family: system-ui, sans-serif;
            margin: 0;
            padding: 20px;
            background: #fafafa;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .card {
            background: white;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 24px;
        }
        .kpi {
            text-align: center;
            padding: 16px;
        }
        .kpi-value {
            font-size: 32px;
            font-weight: bold;
            color: var(--plazza);
        }
        .kpi-label {
            font-size: 14px;
            color: #666;
        }
        h1, h2 { color: var(--plazza); }
        .chart { height: 300px; }
        .tooltip {
            position: absolute;
            padding: 8px;
            background: rgba(0,0,0,0.8);
            color: white;
            border-radius: 4px;
            font-size: 12px;
            pointer-events: none;
        }
        .insight-card {
            background: #f8f9fa;
            padding: 16px;
            border-radius: 8px;
            margin-bottom: 16px;
        }
        .insight-title {
            font-weight: bold;
            color: var(--plazza);
            margin-bottom: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Plazza Performance Insights</h1>
        
        <!-- KPIs -->
        <div class="card">
            <h2>Key Metrics</h2>
            <div class="grid" id="kpi-grid">
                <div class="kpi">
                    <div class="kpi-value">47%</div>
                    <div class="kpi-label">Customer Retention Rate</div>
                </div>
                <div class="kpi">
                    <div class="kpi-value">51</div>
                    <div class="kpi-label">Power Users</div>
                </div>
                <div class="kpi">
                    <div class="kpi-value">₹715</div>
                    <div class="kpi-label">Peak Weekly AOV</div>
                </div>
                <div class="kpi">
                    <div class="kpi-value">22%</div>
                    <div class="kpi-label">Late Night Orders</div>
                </div>
            </div>
        </div>

        <!-- Weekly Performance -->
        <div class="grid">
            <div class="card">
                <h2>Weekly Order Volume</h2>
                <div id="weekly-chart" class="chart"></div>
            </div>
            <div class="card">
                <h2>Time Distribution</h2>
                <div id="hourly-chart" class="chart"></div>
            </div>
        </div>

        <!-- Customer Analysis -->
        <div class="card">
            <h2>Notable Insights</h2>
            <div class="grid">
                <div class="insight-card">
                    <div class="insight-title">Prescription Patterns</div>
                    <p>504 unique prescription medicines ordered with average value of ₹186, showing strong medical compliance.</p>
                </div>
                <div class="insight-card">
                    <div class="insight-title">Fast Delivery Impact</div>
                    <p>76 orders delivered under 30 minutes, with average value of ₹535, indicating premium for speed.</p>
                </div>
                <div class="insight-card">
                    <div class="insight-title">High Value Categories</div>
                    <p>OTC segment shows highest average order value at ₹284, demonstrating strong commercial performance.</p>
                </div>
            </div>
        </div>
    </div>

<script>
// Weekly trends visualization
const renderWeeklyTrends = () => {
    const data = [
        {week: 1, orders: 53, aov: 666.89},
        {week: 2, orders: 69, aov: 715.69},
        {week: 3, orders: 60, aov: 539.95},
        {week: 4, orders: 11, aov: 507.12}
    ];

    const margin = {top: 20, right: 30, bottom: 40, left: 60};
    const width = document.getElementById('weekly-chart').offsetWidth - margin.left - margin.right;
    const height = 250;

    const svg = d3.select("#weekly-chart")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const x = d3.scaleBand()
        .range([0, width])
        .padding(0.1);

    const y = d3.scaleLinear()
        .range([height, 0]);

    x.domain(data.map(d => d.week));
    y.domain([0, d3.max(data, d => d.orders)]);

    svg.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", d => x(d.week))
        .attr("y", d => y(d.orders))
        .attr("width", x.bandwidth())
        .attr("height", d => height - y(d.orders))
        .attr("fill", "#FF0084");

    svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x).tickFormat(d => `Week ${d}`));

    svg.append("g")
        .call(d3.axisLeft(y));
};

// Time distribution visualization
const renderTimeDistribution = () => {
    const data = [
        {hour: 0, orders: 2}, {hour: 1, orders: 5}, {hour: 2, orders: 7},
        {hour: 3, orders: 14}, {hour: 4, orders: 13}, {hour: 5, orders: 25}
    ];

    const margin = {top: 20, right: 30, bottom: 40, left: 60};
    const width = document.getElementById('hourly-chart').offsetWidth - margin.left - margin.right;
    const height = 250;

    const svg = d3.select("#hourly-chart")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    const x = d3.scaleBand()
        .range([0, width])
        .padding(0.1);

    const y = d3.scaleLinear()
        .range([height, 0]);

    x.domain(data.map(d => d.hour));
    y.domain([0, d3.max(data, d => d.orders)]);

    svg.selectAll(".bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", d => x(d.hour))
        .attr("y", d => y(d.orders))
        .attr("width", x.bandwidth())
        .attr("height", d => height - y(d.orders))
        .attr("fill", "#FF0084");

    svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x).tickFormat(d => `${d}:00`));

    svg.append("g")
        .call(d3.axisLeft(y));
};

document.addEventListener('DOMContentLoaded', () => {
    renderWeeklyTrends();
    renderTimeDistribution();
});
</script>
</body>
</html>