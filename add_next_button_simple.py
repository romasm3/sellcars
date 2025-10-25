import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Add Next/Previous buttons ABOVE the map (not overlaying it)
# Find the map div and add buttons before it
old_map_div = r'<!-- Map -->\s*<div id="map" style="height: 600px; width: 100%;"></div>'

new_map_with_buttons = """<!-- Map Controls -->
        <div class="flex justify-center gap-4 mb-4">
            <button onclick="previousCar()"
                    class="bg-orange-500 hover:bg-orange-600 text-white px-6 py-3 rounded-lg font-semibold flex items-center gap-2">
                <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
                </svg>
                Previous Car
            </button>
            <button onclick="nextCar()"
                    class="bg-orange-500 hover:bg-orange-600 text-white px-6 py-3 rounded-lg font-semibold flex items-center gap-2">
                Next Car
                <svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                </svg>
            </button>
        </div>

        <!-- Map -->
        <div id="map" style="height: 600px; width: 100%;"></div>"""

content = re.sub(old_map_div, new_map_with_buttons, content)

# Now add the navigation functions to the JavaScript
# Find the end of the script (before </script>) and add navigation functions
old_script_end = r"(if \(cars\.length > 0\) \{.*?\})\s*</script>"

new_script_end = r"""\1

    // Navigation through cars
    var currentCarIndex = 0;
    var markers = [];

    // Store markers as we create them
    cars.forEach(function(car, index) {
        var marker = L.marker([car.lat, car.lng])
            .addTo(map)
            .bindPopup('<b>' + car.brand + ' ' + car.model + '</b><br>' + car.price);
        markers.push({marker: marker, car: car});
    });

    // Next car function
    function nextCar() {
        if (markers.length === 0) return;
        currentCarIndex = (currentCarIndex + 1) % markers.length;
        var current = markers[currentCarIndex];
        map.setView([current.car.lat, current.car.lng], 13);
        current.marker.openPopup();
    }

    // Previous car function
    function previousCar() {
        if (markers.length === 0) return;
        currentCarIndex = (currentCarIndex - 1 + markers.length) % markers.length;
        var current = markers[currentCarIndex];
        map.setView([current.car.lat, current.car.lng], 13);
        current.marker.openPopup();
    }
</script>"""

content = re.sub(old_script_end, new_script_end, content, flags=re.DOTALL)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Pridėti Next/Previous mygtukai")
print("✓ Funkcionalumas: paspaudus Next - nuveda į kitą mašiną žemėlapyje")
print("✓ Funkcionalumas: paspaudus Previous - nuveda į ankstesnę mašiną")
print("✓ Auto-zoom į mašiną ir atidaro popup")
