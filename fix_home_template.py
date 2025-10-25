#!/usr/bin/env python
"""Fix home.html template syntax"""

# Read the file
with open("templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix the first lines
if content.startswith('{% extends "base.html" %} {% block title %}'):
    # Replace the problematic first two lines
    old_start = '{% extends "base.html" %} {% block title %}SellCars - Buy & Sell Cars Online{%\nendblock %} {% block content %}'
    new_start = '{% extends "base.html" %}\n\n{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}\n\n{% block content %}'

    content = content.replace(old_start, new_start, 1)

    # Write back
    with open("templates/core/home.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("✓ Fixed home.html template syntax")
    print("\nFirst 5 lines now:")
    with open("templates/core/home.html", "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if i <= 5:
                print(f"{i}: {line}", end="")
            else:
                break
else:
    print("Template already fixed or different format")
    print("Current start:")
    print(content[:200])
