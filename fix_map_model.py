#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fix map model filter to dropdown"""

file_path = "apps/core/templates/core/home.html"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace map model text input with dropdown
old_map_model = """                        <input
                            type="text"
                            id="mapModelFilter"
                            placeholder="Enter model..."
                            class="w-full px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                            oninput="filterMapCars()"
                        />"""

new_map_model = """                        <select
                            id="mapModelFilter"
                            class="w-full px-4 py-2 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                            onchange="filterMapCars()"
                        >
                            <option value="">All Models</option>
                        </select>"""

content = content.replace(old_map_model, new_map_model)

# Update the filterMapCars function to work with select dropdown
old_filter = """        var modelFilter = document.getElementById('mapModelFilter').value.toLowerCase();"""
new_filter = (
    """        var modelFilter = document.getElementById('mapModelFilter').value;"""
)

content = content.replace(old_filter, new_filter)

# Update the model match check
old_match = """            var modelMatch = !modelFilter || car.model.toLowerCase().includes(modelFilter);"""
new_match = (
    """            var modelMatch = !modelFilter || car.model === modelFilter;"""
)

content = content.replace(old_match, new_match)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully changed map Model filter to dropdown!")
