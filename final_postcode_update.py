#!/usr/bin/env python
"""Final postcode updates"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Car

# Update the two remaining cars
car1 = Car.objects.filter(model__icontains="m3", location__icontains="germany").first()
if car1 and not car1.postcode:
    car1.postcode = "10115"  # Berlin
    car1.save(update_fields=["postcode"])
    print(f"Updated {car1.title}: {car1.location} -> 10115")

car2 = Car.objects.filter(location__icontains="München").first()
if car2 and not car2.postcode:
    car2.postcode = "80331"  # Munich
    car2.save(update_fields=["postcode"])
    print(f"Updated {car2.title}: {car2.location} -> 80331")

print("\n✅ All cars with postcodes:")
for car in Car.objects.all():
    status = "✓" if car.postcode else "✗"
    print(
        f"{status} {car.title}: {car.location} (Postcode: {car.postcode or 'MISSING'})"
    )
