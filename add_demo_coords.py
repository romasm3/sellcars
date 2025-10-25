#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Add demo coordinates if geocoding fails"""

file_path = "apps/core/views.py"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the geocoding section and add fallback coordinates
old_code = """        if car_data["lat"] and car_data["lng"]:
            cars_with_coords.append(car_data)"""

new_code = """        # Add demo coordinates if geocoding failed
        if not car_data["lat"] or not car_data["lng"]:
            # Demo coordinates for various European cities
            demo_coords = [
                (52.52, 13.405),  # Berlin
                (48.8566, 2.3522),  # Paris
                (51.5074, -0.1278),  # London
                (50.0755, 14.4378),  # Prague
                (52.3676, 4.9041),  # Amsterdam
                (48.2082, 16.3738),  # Vienna
            ]
            import random
            lat, lng = random.choice(demo_coords)
            car_data["lat"] = lat
            car_data["lng"] = lng

        cars_with_coords.append(car_data)"""

content = content.replace(old_code, new_code)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully added demo coordinates fallback!")
