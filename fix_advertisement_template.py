#!/usr/bin/env python
"""Fix the broken template tags in advertisement_create.html"""

template_path = (
    r"C:\Users\user\Desktop\programos\sellcars\templates\core\advertisement_create.html"
)

# Read the file
with open(template_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken template tags at the start
# Replace the broken line breaks in template tags
content = content.replace(
    "{% extends 'base.html' %} {% block title %}Add New Advertisement - SellCars{%\nendblock %} {% block content %}",
    "{% extends 'base.html' %}\n\n{% block title %}Add New Advertisement - SellCars{% endblock %}\n\n{% block content %}",
)

# Write back
with open(template_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Fixed advertisement_create.html template tags")
