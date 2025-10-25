import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Car

# Check the first car
car = Car.objects.first()
if car:
    print(f"Car: {car}")
    print(f"Latitude: {car.latitude}")
    print(f"Longitude: {car.longitude}")
    print(f"Location: {car.location}")
else:
    print("No cars in database")
