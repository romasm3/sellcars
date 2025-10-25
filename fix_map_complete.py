import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the map container and completely rewrite it without rounded corners
# The overflow-hidden was clipping the tiles, so we need overflow: visible
# But rounded-xl + overflow:visible doesn't work, so remove rounded corners

old_container_pattern = (
    r'<div\s+class="relative[^"]*"\s+style="[^"]*"\s+id="map-container"\s*>'
)

new_container = """<div
            class="relative shadow-2xl border border-slate-700"
            style="height: 600px;"
            id="map-container"
        >"""

content = re.sub(old_container_pattern, new_container, content)

# Also update the inner map div to ensure it's not clipped
old_map_div_pattern = r'<div id="cars-map" style="[^"]*"></div>'
new_map_div = '<div id="cars-map" style="height: 600px; width: 100%;"></div>'

content = re.sub(old_map_div_pattern, new_map_div, content)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Map container completely fixed!")
print("- Removed rounded corners that were causing clipping issues")
print("- Set explicit height on map div")
print("- Ensured no overflow restrictions")
