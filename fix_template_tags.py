import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken template tags at the beginning
# Replace the broken multiline tags with proper single-line tags
old_start = r"{% extends \"base\.html\" %} {% block title %}SellCars - Buy & Sell Cars Online{%\s*endblock %} {% block content %}"

new_start = """{% extends "base.html" %}
{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}

{% block content %}"""

content = re.sub(old_start, new_start, content)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Template tags pataisyti!")
print("✓ Visi {% block %} ir {% endblock %} tagai dabar atskirose eilutėse")
