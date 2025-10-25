#!/usr/bin/env python
"""Update existing cars with postcodes based on their location"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Car

# Common German postcodes for major cities
location_postcodes = {
    "Berlin, Germany": "10115",
    "Berlin": "10115",
    "Munich, Germany": "80331",
    "Munich": "80331",
    "Hamburg, Germany": "20095",
    "Hamburg": "20095",
    "Frankfurt, Germany": "60311",
    "Frankfurt": "60311",
    "Cologne, Germany": "50667",
    "Cologne": "50667",
    "Stuttgart, Germany": "70173",
    "Stuttgart": "70173",
    "Düsseldorf, Germany": "40213",
    "Düsseldorf": "40213",
}

cars = Car.objects.all()

updated_count = 0
for car in cars:
    if not car.postcode and car.location:
        # Try to find a matching postcode
        for location_key, postcode in location_postcodes.items():
            if location_key.lower() in car.location.lower():
                car.postcode = postcode
                car.save(update_fields=["postcode"])
                print(f"Updated {car.title}: {car.location} -> {postcode}")
                updated_count += 1
                break

print(f"\nTotal cars updated: {updated_count}")
print(f"Total cars: {cars.count()}")

# Show all cars with their postcodes
print("\nAll cars:")
for car in cars:
    print(f"  {car.title}: {car.location} (Postcode: {car.postcode or 'N/A'})")
