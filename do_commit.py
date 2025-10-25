#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Commit changes"""

import subprocess
import sys

try:
    # Commit
    result = subprocess.run(
        ["git", "commit", "-m", "Add Model dropdown and remove How It Works section"],
        capture_output=True,
        text=True,
        cwd=r"C:\Users\user\Desktop\programos\sellcars",
    )

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return code:", result.returncode)

    # Show last commit
    result2 = subprocess.run(
        ["git", "log", "-1", "--oneline"],
        capture_output=True,
        text=True,
        cwd=r"C:\Users\user\Desktop\programos\sellcars",
    )
    print("\nLast commit:", result2.stdout)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
