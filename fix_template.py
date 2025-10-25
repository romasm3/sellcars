#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fix the home.html template file"""

file_path = "apps/core/templates/core/home.html"

# Read all lines
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Original line 1: {lines[0]}")
print(f"Original line 2: {lines[1]}")

# Fix first 3 lines
lines[0] = '{% extends "base.html" %}\n'
lines[1] = "{% block title %}SellCars - Buy & Sell Cars Online{% endblock %}\n"
lines[2] = "{% block content %}\n"

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\nFile fixed successfully!")
print("First 3 lines now:")
with open(file_path, "r", encoding="utf-8") as f:
    for i in range(3):
        line = f.readline()
        print(f"{i + 1}: {line}", end="")
