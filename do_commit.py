import subprocess
import sys

message = "Add rental features, Airbnb-style UI, map integration, advertisement form, and zoom-out layout"

try:
    result = subprocess.run(
        ["git", "commit", "-m", message], capture_output=True, text=True, check=True
    )
    print(result.stdout)
    print(result.stderr)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
    print(f"stdout: {e.stdout}")
    print(f"stderr: {e.stderr}")
    sys.exit(1)
