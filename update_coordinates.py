#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Car

# Update existing cars with coordinates
cars = Car.objects.all()

for car in cars:
    if car.location == "Berlin" and not car.latitude:
        car.latitude = 52.520008
        car.longitude = 13.404954
        car.save()
        print(f"✅ Updated {car.title} with Berlin coordinates")
    elif car.location == "München" and not car.latitude:
        car.latitude = 48.137154
        car.longitude = 11.576124
        car.save()
        print(f"✅ Updated {car.title} with München coordinates")

print("\n" + "=" * 60)
print("✅ Coordinates updated successfully!")
print("=" * 60)
