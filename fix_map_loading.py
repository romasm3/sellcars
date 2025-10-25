import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the map initialization script and add invalidateSize after map creation
# This ensures the map properly calculates its size

# Replace the map initialization to add a delay and invalidateSize call
old_init = r"const map = L\.map\('cars-map'\)\.setView\(\[52\.0, 10\.0\], 6\);"

new_init = """const map = L.map('cars-map', {
        scrollWheelZoom: true,
        zoomControl: true
    }).setView([52.0, 10.0], 6);

    // Force map to recalculate size after initialization
    setTimeout(() => {
        map.invalidateSize();
    }, 100);"""

content = re.sub(old_init, new_init, content)

# Also add invalidateSize after tile layer is added
old_tiles = r"L\.tileLayer\('https://\{s\}\.tile\.openstreetmap\.org/\{z\}/\{x\}/\{y\}\.png', \{\s*attribution: '© OpenStreetMap contributors',\s*maxZoom: 19\s*\}\)\.addTo\(map\);"

new_tiles = """L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 19,
        minZoom: 2
    }).addTo(map);

    // Ensure tiles load properly
    map.whenReady(() => {
        setTimeout(() => {
            map.invalidateSize();
        }, 200);
    });"""

content = re.sub(old_tiles, new_tiles, content, flags=re.DOTALL)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Map loading fixed!")
print("- Added proper map initialization with size recalculation")
print("- Added whenReady handler to ensure tiles load")
print("- Added minZoom to prevent over-zooming out")
