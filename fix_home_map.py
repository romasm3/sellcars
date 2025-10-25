#!/usr/bin/env python
"""Fix the broken template tags in home.html"""

template_path = (
    r"C:\Users\user\Desktop\programos\sellcars\apps\core\templates\core\home.html"
)

# Read the file
with open(template_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the first line - ensure proper spacing
content = content.replace(
    '{% extends "base.html" %} \n\n{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}',
    '{% extends "base.html" %}\n\n{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}',
)

# Write back
with open(template_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Fixed home.html template tags")
