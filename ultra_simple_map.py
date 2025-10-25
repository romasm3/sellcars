import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace ENTIRE map section with ultra-simple version that will work
map_section_pattern = r"<!-- Interactive Map Section -->.*?</script>\s*{% endblock %}"

ultra_simple_map = """<!-- Interactive Map Section -->
<div class="bg-slate-900 py-16">
    <div class="container mx-auto px-4">
        <div class="text-center mb-8">
            <h2 class="text-4xl font-bold text-white mb-4">
                Explore Cars <span class="gradient-text">on Map</span>
            </h2>
            <p class="text-xl text-slate-300">
                Browse available cars by location
            </p>
        </div>

        <!-- Map -->
        <div id="map" style="height: 600px; width: 100%;"></div>
    </div>
</div>

<!-- Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
    // Simple working map
    var map = L.map('map').setView([52.0, 10.0], 5);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // Add markers for cars
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

    cars.forEach(function(car) {
        L.marker([car.lat, car.lng])
            .addTo(map)
            .bindPopup('<b>' + car.brand + ' ' + car.model + '</b><br>' + car.price);
    });

    // Fit to show all cars
    if (cars.length > 0) {
        var group = new L.featureGroup(cars.map(c => L.marker([c.lat, c.lng])));
        map.fitBounds(group.getBounds().pad(0.1));
    }
</script>
{% endblock %}"""

content = re.sub(map_section_pattern, ultra_simple_map, content, flags=re.DOTALL)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Ultra paprastas žemėlapis")
print("✓ Be jokių zoom, transform ar kitų komplikacijų")
print("✓ Turėtų veikti su body zoom: 0.6")
