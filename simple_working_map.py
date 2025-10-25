import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the entire map section with a simple working version
# Find from "<!-- Interactive Map Section -->" to the end of the script
map_section_pattern = r"<!-- Interactive Map Section -->.*?</script>\s*{% endblock %}"

simple_map_section = """<!-- Interactive Map Section -->
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

        <!-- Map Container - SIMPLE VERSION -->
        <div id="map-container" style="height: 600px; width: 100%; position: relative;">
            <div id="map" style="height: 100%; width: 100%;"></div>
        </div>
    </div>
</div>

<!-- Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
    // Wait for DOM to be ready
    document.addEventListener('DOMContentLoaded', function() {
        // Initialize map
        var map = L.map('map').setView([52.0, 10.0], 5);

        // Add tile layer
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Fix map size after a short delay
        setTimeout(function() {
            map.invalidateSize();
        }, 100);

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

        // Add markers
        cars.forEach(function(car) {
            var marker = L.marker([car.lat, car.lng]).addTo(map);
            marker.bindPopup('<b>' + car.brand + ' ' + car.model + '</b><br>' +
                           car.price + '<br>' +
                           '<a href="/cars/' + car.slug + '/">View Details</a>');
        });

        // Fit bounds if we have cars
        if (cars.length > 0) {
            var bounds = L.latLngBounds(cars.map(function(car) {
                return [car.lat, car.lng];
            }));
            map.fitBounds(bounds, {padding: [50, 50]});
        }
    });
</script>
{% endblock %}"""

content = re.sub(map_section_pattern, simple_map_section, content, flags=re.DOTALL)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("✓ Žemėlapis pakeistas į paprastą, veikiančią versiją")
print("✓ Pašalinti visi sudėtingi elementai")
print("✓ Naudojami paprasti Leaflet markeriai")
print("✓ DOMContentLoaded užtikrina kad viskas užsikrauna")
