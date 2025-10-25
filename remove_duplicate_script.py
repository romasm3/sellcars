#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Remove duplicate Brand/Model Dynamic Filter Script"""

file_path = "apps/core/templates/core/home.html"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find and remove the first occurrence (at the top, before extends)
new_lines = []
skip_until = -1
found_first = False

for i, line in enumerate(lines):
    # Skip the first Brand/Model Dynamic Filter Script block
    if "<!-- Brand/Model Dynamic Filter Script -->" in line and not found_first:
        found_first = True
        # Find the end of this script block
        for j in range(i, min(i + 100, len(lines))):
            if "</script>" in lines[j]:
                skip_until = j + 1
                break
        continue

    if i < skip_until:
        continue

    new_lines.append(line)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(
    f"Removed duplicate script. Total lines before: {len(lines)}, after: {len(new_lines)}"
)
