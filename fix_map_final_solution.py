import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the map container with a simpler approach
# Remove the transform and just use normal sizing with a wrapper
old_container = r'<div id="map-container" style="height: 1000px; width: 166\.67%; position: relative; transform: scale\(0\.6\); transform-origin: top left;">\s*<div id="map" style="height: 1000px; width: 100%;"></div>'

new_container = """<div style="width: 100%; height: 600px; position: relative;">
            <div id="map" style="width: 100%; height: 100%; zoom: 1.667;"></div>"""

content = re.sub(old_container, new_container, content)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Žemėlapis pakeistas - naudoja zoom: 1.667 ant map div")
print("✓ Tai kompensuos body zoom: 0.6")
