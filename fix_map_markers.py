#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fix map markers to use cars_with_coords from view"""

file_path = "apps/core/templates/core/home.html"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the cars array to use cars_with_coords from view
old_cars_array = """    var cars = [
        {% for car in featured_cars %}
        {% if car.latitude and car.longitude %}
        {
            lat: {{ car.latitude }},
            lng: {{ car.longitude }},
            brand: "{{ car.brand.name }}",
            model: "{{ car.model }}",
            price: "{% if car.is_for_rent and car.price_per_day %}€{{ car.price_per_day|floatformat:0 }}/day{% else %}€{{ car.price|floatformat:0 }}{% endif %}",
            slug: "{{ car.slug }}",
            location: "Berlin, Germany"
        },
        {% endif %}
        {% endfor %}
    ];"""

new_cars_array = """    var cars = [
        {% for car_data in cars_with_coords %}
        {
            lat: {{ car_data.lat }},
            lng: {{ car_data.lng }},
            brand: "{{ car_data.car.brand.name }}",
            model: "{{ car_data.car.model }}",
            price: "{% if car_data.car.is_for_rent and car_data.car.price_per_day %}€{{ car_data.car.price_per_day|floatformat:0 }}/day{% else %}€{{ car_data.car.price|floatformat:0 }}{% endif %}",
            slug: "{{ car_data.car.slug }}",
            location: "{{ car_data.car.location }}"
        }{% if not forloop.last %},{% endif %}
        {% endfor %}
    ];"""

content = content.replace(old_cars_array, new_cars_array)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully fixed map markers to use cars_with_coords!")
