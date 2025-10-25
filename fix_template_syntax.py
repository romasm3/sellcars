import re

# Read the file
with open("templates/core/advertisement_create.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken template tags at the beginning
# Replace the broken first lines
old_pattern = r"{% extends 'base\.html' %} {% block title %}Add New Advertisement - SellCars{%\s*\nendblock %} {% block content %}"
new_start = """{% extends 'base.html' %}
{% block title %}Add New Advertisement - SellCars{% endblock %}

{% block content %}"""

content = re.sub(old_pattern, new_start, content)

# Write back
with open("templates/core/advertisement_create.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Template fixed!")
