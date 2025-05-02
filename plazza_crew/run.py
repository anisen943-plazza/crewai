#!/usr/bin/env python
# Run script to properly execute the plazza_crew main.py

import os
import sys
import subprocess
from pathlib import Path

# Get the absolute path to the project root
project_root = Path(__file__).resolve().parent
src_dir = project_root / "src"

# Add the project root to Python path
sys.path.append(str(project_root))

# Ensure required environment variables are set
from dotenv import load_dotenv
load_dotenv()

# Check for required environment variables
required_env_vars = [
    "DATABASE_URL", 
    "DATABASE_URL_ERP", 
    "DATABASE_URL_USER_TRANSACTIONS",
    "OPENAI_API_KEY"
]

missing_vars = []
for var in required_env_vars:
    if not os.getenv(var):
        missing_vars.append(var)

if missing_vars:
    print("❌ ERROR: Missing required environment variables:")
    for var in missing_vars:
        print(f"  - {var}")
    print("\nPlease set these variables in your .env file at the project root.")
    sys.exit(1)

print("✅ Environment variables verified")

# Verify the schema file exists
schema_path = project_root / "schema_summary.md"
if not schema_path.exists():
    print(f"❌ ERROR: Schema file {schema_path} not found")
    sys.exit(1)

print(f"✅ Schema file found at {schema_path}")

# Run the main.py script with the proper Python path
main_script = src_dir / "plazza_crew" / "main.py"
if not main_script.exists():
    print(f"❌ ERROR: Main script {main_script} not found")
    sys.exit(1)

print(f"✅ Main script found at {main_script}")
print("\n🚀 Running plazza_crew...\n")

# Execute the main script
try:
    # Use the current Python executable
    python_executable = sys.executable
    result = subprocess.run([python_executable, str(main_script)], check=True)
    sys.exit(result.returncode)
except subprocess.CalledProcessError as e:
    print(f"❌ ERROR: Process failed with exit code {e.returncode}")
    sys.exit(e.returncode)
except Exception as e:
    print(f"❌ ERROR: {str(e)}")
    sys.exit(1)