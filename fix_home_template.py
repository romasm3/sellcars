#!/usr/bin/env python
# -*- coding: utf-8 -*-

file_path = "apps/core/templates/core/home.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the broken first lines
content = content.replace(
    '{% extends "base.html" %} {% block title %}SellCars - Buy & Sell Cars Online{%\nendblock %} {% block content %}',
    '{% extends "base.html" %}\n\n{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}\n\n{% block content %}',
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Template fixed successfully!")
print("First 5 lines:")
with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i < 5:
            print(f"{i + 1}: {line}", end="")
        else:
            break
