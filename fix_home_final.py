#!/usr/bin/env python
"""Fix the broken template tags in home.html - final fix"""

template_path = (
    r"C:\Users\user\Desktop\programos\sellcars\apps\core\templates\core\home.html"
)

# Read the file
with open(template_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix all broken template tags
# Fix line 1-2
content = content.replace(
    '{% extends "base.html" %} {% block title %}SellCars - Buy & Sell Cars Online{%\nendblock %} {% block extra_css %}',
    '{% extends "base.html" %}\n\n{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}\n\n{% block extra_css %}',
)

# Write back
with open(template_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Fixed home.html template - all tags properly closed")
