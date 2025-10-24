#!/usr/bin/env python
# -*- coding: utf-8 -*-

file_path = "templates/core/car_list.html"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find where to cut (before "<!-- Right Side: Map -->")
new_lines = []
skip = False

for i, line in enumerate(lines):
    if "<!-- Right Side: Map -->" in line:
        # Add closing tags
        new_lines.append("        </div>\n")
        new_lines.append("    </div>\n")
        new_lines.append("</div>\n")
        new_lines.append("{% endblock %}\n")
        skip = True
        break

    # Skip extra closing divs before map
    if not skip and "endif" in line and i > 260:
        new_lines.append(line)
        continue

    if not skip:
        new_lines.append(line)

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("✅ Fixed car_list.html - removed map section")
