#!/usr/bin/env python
"""Populate CarModel table from existing Car data"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Car, Brand, CarModel


def populate_car_models():
    """Create CarModel entries from existing Car data"""

    # Get all unique brand-model combinations
    cars = Car.objects.select_related("brand").all()

    created_count = 0

    for car in cars:
        if car.brand and car.model:
            # Try to get or create the CarModel
            car_model, created = CarModel.objects.get_or_create(
                brand=car.brand, name=car.model, defaults={"name": car.model}
            )

            if created:
                created_count += 1
                print(f"Created: {car_model}")

    print(f"\nTotal CarModels created: {created_count}")
    print(f"Total CarModels in database: {CarModel.objects.count()}")


if __name__ == "__main__":
    populate_car_models()
