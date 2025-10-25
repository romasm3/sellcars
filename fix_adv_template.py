#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fix broken template tags in advertisement_create.html"""

with open("templates/core/advertisement_create.html", "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken template tags at the start
old_start = (
    r"{% extends 'base.html' %} {% block title %}Add New Advertisement - SellCars{%"
    + "\n"
    + r"endblock %} {% block content %}"
)
new_start = """{% extends 'base.html' %}
{% block title %}Add New Advertisement - SellCars{% endblock %}

{% block content %}"""

content = content.replace(old_start, new_start)

with open("templates/core/advertisement_create.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Template tags fixed successfully!")
