#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Remove How It Works section"""

file_path = "apps/core/templates/core/home.html"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find and remove the How It Works section
new_lines = []
skip = False
skip_count = 0

for i, line in enumerate(lines):
    # Start skipping at "<!-- How It Works -->"
    if "<!-- How It Works -->" in line:
        skip = True
        continue

    # Keep skipping until we find the closing div and next section comment
    if skip:
        skip_count += 1
        # Look for the end of this section (before Interactive Map or CTA)
        if "<!-- Interactive Map Section -->" in line or "<!-- CTA Section -->" in line:
            skip = False
            new_lines.append(line)
        continue

    new_lines.append(line)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Successfully removed How It Works section! Removed {skip_count} lines.")
