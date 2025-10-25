#!/usr/bin/env python
"""Fix broken template tags in home.html - version 2"""

template_path = (
    r"C:\Users\user\Desktop\programos\sellcars\apps\core\templates\core\home.html"
)

# Read the file
with open(template_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Check first few lines
print("First 3 lines before fix:")
for i, line in enumerate(lines[:3]):
    print(f"{i + 1}: {repr(line)}")

# Fix line 1-2 if broken
if len(lines) >= 2:
    line1 = lines[0].strip()
    line2 = lines[1].strip()

    # Check if tags are broken across lines
    if "{%" in line1 and "endblock" in line2 and "%}" in line2:
        print("\n✓ Found broken template tags!")
        # Replace first two lines with properly formatted ones
        lines[0] = '{% extends "base.html" %}\n'
        lines[1] = "\n"
        lines.insert(
            2, "{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}\n"
        )
        lines.insert(3, "\n")

        # Remove old broken lines
        if "endblock" in lines[4]:
            lines[4] = "{% block extra_css %}\n"

        print("✓ Fixed template tags")

# Write back
with open(template_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✓ File saved")
print("\nFirst 5 lines after fix:")
with open(template_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f.readlines()[:5]):
        print(f"{i + 1}: {line.rstrip()}")
