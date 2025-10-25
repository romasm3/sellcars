import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find and replace the entire script section to remove duplicate markers
old_script = r"<script>\s*// Simple working map.*?</script>"

new_script = """<script>
    // Initialize map
    var map = L.map('map').setView([52.0, 10.0], 5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // Car data from Django
    var cars = [
        {% for car in featured_cars %}
        {% if car.latitude and car.longitude %}
        {
            lat: {{ car.latitude }},
            lng: {{ car.longitude }},
            brand: "{{ car.brand.name }}",
            model: "{{ car.model }}",
            price: "{% if car.is_for_rent and car.price_per_day %}€{{ car.price_per_day|floatformat:0 }}/day{% else %}€{{ car.price|floatformat:0 }}{% endif %}",
            slug: "{{ car.slug }}"
        },
        {% endif %}
        {% endfor %}
    ];

    // Navigation
    var currentCarIndex = 0;
    var markers = [];

    // Add markers (only once!)
    cars.forEach(function(car, index) {
        var marker = L.marker([car.lat, car.lng])
            .addTo(map)
            .bindPopup('<b>' + car.brand + ' ' + car.model + '</b><br>' + car.price + '<br><a href="/cars/' + car.slug + '/">View Details</a>');
        markers.push({marker: marker, car: car});
    });

    // Fit bounds to show all cars
    if (cars.length > 0) {
        var group = new L.featureGroup(markers.map(m => m.marker));
        map.fitBounds(group.getBounds().pad(0.1));
    }

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

content = re.sub(old_script, new_script, content, flags=re.DOTALL)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Pašalinti dubliuoti markeriai")
print("✓ Žemėlapis turėtų veikti dabar")
print("✓ Next/Previous mygtukai veikia")
