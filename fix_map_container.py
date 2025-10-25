import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove overflow-hidden from map container as it can cause tile loading issues
old_container = r'<div\s+class="relative rounded-xl overflow-hidden shadow-2xl border border-slate-700"\s+style="height: 600px"\s+id="map-container"\s*>'

new_container = """<div
            class="relative rounded-xl shadow-2xl border border-slate-700"
            style="height: 600px; overflow: visible;"
            id="map-container"
        >"""

content = re.sub(old_container, new_container, content)

# Also ensure the inner map div is properly styled
old_map_div = r'<div id="cars-map" style="height: 100%; width: 100%"></div>'
new_map_div = '<div id="cars-map" style="height: 100%; width: 100%; position: relative; z-index: 1;"></div>'

content = re.sub(old_map_div, new_map_div, content)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Map container CSS fixed!")
print("- Removed overflow-hidden that was clipping tiles")
print("- Added explicit positioning to map div")
