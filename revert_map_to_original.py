import re

# Read the file
with open("apps/core/templates/core/home.html", "r", encoding="utf-8") as f:
    content = f.read()

# The working original map JavaScript (without navigation buttons)
original_map_js = """<!-- Leaflet JS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
    // Initialize map centered on Europe (Germany)
    const map = L.map('cars-map').setView([52.0, 10.0], 6);

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 19
    }).addTo(map);

    // Car data from Django
    const cars = [
        {% for car in featured_cars %}
        {% if car.latitude and car.longitude %}
        {
            id: {{ car.id }},
            lat: {{ car.latitude }},
            lng: {{ car.longitude }},
            brand: "{{ car.brand.name }}",
            model: "{{ car.model }}",
            year: {{ car.year }},
            price: {% if car.is_for_rent and car.price_per_day %}"€{{ car.price_per_day|floatformat:0 }}/day"{% else %}"€{{ car.price|floatformat:0 }}"{% endif %},
            slug: "{{ car.slug }}",
            image: "{% if car.get_main_image %}{{ car.get_main_image.image.url }}{% endif %}",
            isForRent: {{ car.is_for_rent|yesno:"true,false" }}
        },
        {% endif %}
        {% endfor %}
    ];

    // Add markers for each car
    cars.forEach((car, index) => {
        // Create custom marker with price
        const icon = L.divIcon({
            className: 'car-marker',
            html: car.price,
            iconSize: null
        });

        const marker = L.marker([car.lat, car.lng], { icon: icon }).addTo(map);

        // Popup with car details
        const popupContent = `
            <div style="min-width: 200px;">
                ${car.image ? `<img src="${car.image}" style="width: 100%; height: 120px; object-fit: cover; border-radius: 8px; margin-bottom: 8px;">` : ''}
                <h3 style="font-weight: bold; font-size: 16px; margin-bottom: 4px; color: #1e293b;">
                    ${car.brand} ${car.model}
                </h3>
                <p style="color: #64748b; font-size: 14px; margin-bottom: 8px;">
                    ${car.year} ${car.isForRent ? '• Available for rent' : ''}
                </p>
                <p style="font-weight: bold; color: #ea580c; font-size: 18px; margin-bottom: 8px;">
                    ${car.price}
                </p>
                <a href="/cars/${car.slug}/"
                   style="display: block; background: #ea580c; color: white; text-align: center; padding: 8px; border-radius: 6px; text-decoration: none; font-weight: 600;">
                    View Details
                </a>
            </div>
        `;

        marker.bindPopup(popupContent);

        // Click marker to open popup
        marker.on('click', function() {
            marker.openPopup();
        });
    });

    // Fit map to show all markers
    if (cars.length > 0) {
        const bounds = L.latLngBounds(cars.map(car => [car.lat, car.lng]));
        map.fitBounds(bounds, { padding: [50, 50] });
    }

    // Fullscreen functionality
    function toggleFullscreen() {
        const mapContainer = document.getElementById('map-container');

        if (!document.fullscreenElement) {
            mapContainer.requestFullscreen().then(() => {
                // Resize map when entering fullscreen
                setTimeout(() => map.invalidateSize(), 100);
            });
        } else {
            document.exitFullscreen().then(() => {
                // Resize map when exiting fullscreen
                setTimeout(() => map.invalidateSize(), 100);
            });
        }
    }

    // Handle fullscreen changes
    document.addEventListener('fullscreenchange', () => {
        map.invalidateSize();
    });
</script>
{% endblock %}"""

# Remove the navigation buttons HTML
# Find and remove the navigation buttons section
nav_buttons_pattern = r'<!-- Navigation Buttons -->.*?</div>\s*<div id="cars-map"'
content = re.sub(nav_buttons_pattern, '<div id="cars-map"', content, flags=re.DOTALL)

# Replace the entire script section (from <!-- Leaflet JS --> to {% endblock %})
script_pattern = r"<!-- Leaflet JS -->.*?{% endblock %}\s*$"
content = re.sub(script_pattern, original_map_js, content, flags=re.DOTALL)

# Write back
with open("apps/core/templates/core/home.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Map reverted to original working version!")
print("- Removed navigation buttons")
print("- Cleaned up duplicate JavaScript code")
print("- Restored simple, working map implementation")
