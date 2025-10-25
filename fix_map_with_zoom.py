import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the map container to compensate for body zoom: 0.6
# We need to apply inverse zoom (1/0.6 = 1.667) to the map container
old_container = (
    r'<div id="map-container" style="height: 600px; width: 100%; position: relative;">'
)

new_container = """<div id="map-container" style="height: 1000px; width: 166.67%; position: relative; transform: scale(0.6); transform-origin: top left;">"""

content = re.sub(old_container, new_container, content)

# Also update the inner map div
old_map = r'<div id="map" style="height: 100%; width: 100%;"></div>'
new_map = '<div id="map" style="height: 1000px; width: 100%;"></div>'

content = re.sub(old_map, new_map, content)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Žemėlapis pritaikytas veikti su zoom: 0.6")
print("✓ Pridėtas inverse scale transform")
