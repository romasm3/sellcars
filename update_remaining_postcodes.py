#!/usr/bin/env python
"""Update remaining cars with postcodes"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Car

# Update remaining cars
updates = {
    "x5555555555": "101000",  # Moscow postcode
    "m4": "00100",  # Rome postcode
    "germany": "10115",  # Berlin postcode (default Germany)
    "München": "80331",  # Munich
}

for title_key, postcode in updates.items():
    cars = Car.objects.filter(title__icontains=title_key, postcode="")
    for car in cars:
        car.postcode = postcode
        car.save(update_fields=["postcode"])
        print(f"Updated {car.title}: {car.location} -> {postcode}")

print("\nAll cars now:")
for car in Car.objects.all():
    print(f"{car.title}: {car.location} (Postcode: {car.postcode or 'N/A'})")
