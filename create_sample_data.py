import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Brand, Car
from django.contrib.auth.models import User

# Create brands
brands_data = [
    "BMW",
    "Mercedes-Benz",
    "Audi",
    "Volkswagen",
    "Porsche",
    "Toyota",
    "Honda",
    "Ford",
    "Tesla",
    "Volvo",
]

print("Creating brands...")
for brand_name in brands_data:
    brand, created = Brand.objects.get_or_create(name=brand_name)
    if created:
        print(f"✅ Created brand: {brand_name}")
    else:
        print(f"⚠️  Brand already exists: {brand_name}")

# Get admin user
admin_user = User.objects.filter(is_superuser=True).first()

if admin_user:
    # Create sample cars
    print("\nCreating sample cars...")

    bmw = Brand.objects.get(name="BMW")

    # BMW 430i Cabrio M Sport
    car1, created = Car.objects.get_or_create(
        title="BMW 430i Cabrio M Sport A M Sport",
        defaults={
            "brand": bmw,
            "model": "430i",
            "year": 2018,
            "body_type": "cabrio",
            "mileage": 50000,
            "fuel_type": "petrol",
            "transmission": "automatic",
            "engine_size": 2000,
            "power_hp": 252,
            "condition": "used",
            "first_registration": date(2018, 6, 1),
            "previous_owners": 1,
            "description": "Sehr gepflegter BMW 430i Cabrio M Sport in exzellentem Zustand. Das Fahrzeug wurde regelmäßig gewartet und verfügt über eine Vollausstattung.",
            "color": "silver",
            "doors": 2,
            "seats": 4,
            "co2_emission": 169,
            "consumption": 7.3,
            "features": "M Sport Paket, Navi Professional, Ledersitze, Klimaautomatik, Xenon, PDC",
            "emission_class": "Euro 6",
            "price": 32900,
            "price_per_day": 150,
            "price_per_week": 900,
            "is_for_sale": True,
            "is_for_rent": True,
            "location": "Berlin",
            "latitude": 52.520008,
            "longitude": 13.404954,
            "seller": admin_user,
            "phone": "+49 30 12345678",
            "is_active": True,
        },
    )
    if created:
        print(f"✅ Created car: {car1.title}")

    # Mercedes M3 G80
    mercedes = Brand.objects.get(name="Mercedes-Benz")
    car2, created = Car.objects.get_or_create(
        title="BMW M3 G80 COMPETITION CARBON PERFORMANCE",
        defaults={
            "brand": bmw,
            "model": "M3 G80",
            "year": 2020,
            "body_type": "sedan",
            "mileage": 41000,
            "fuel_type": "petrol",
            "transmission": "automatic",
            "engine_size": 3000,
            "power_hp": 530,
            "condition": "used",
            "first_registration": date(2020, 6, 1),
            "previous_owners": 1,
            "description": "BMW M3 Competition mit Carbon Performance Paket. Absolutes Top-Fahrzeug mit voller Ausstattung und Carbon-Extras.",
            "color": "silver",
            "doors": 4,
            "seats": 5,
            "co2_emission": 219,
            "consumption": 10.2,
            "features": "M Competition Paket, Carbon Performance, M Drivers Package, Head-Up Display, Harman Kardon",
            "emission_class": "Euro 6d",
            "price": 89900,
            "price_per_day": 450,
            "price_per_week": 2800,
            "is_for_sale": True,
            "is_for_rent": True,
            "location": "München",
            "latitude": 48.137154,
            "longitude": 11.576124,
            "seller": admin_user,
            "phone": "+49 89 87654321",
            "is_active": True,
        },
    )
    if created:
        print(f"✅ Created car: {car2.title}")

    print("\n" + "=" * 60)
    print(f"✅ Sample data created successfully!")
    print(f"Total brands: {Brand.objects.count()}")
    print(f"Total cars: {Car.objects.count()}")
    print("=" * 60)
else:
    print("❌ No admin user found. Please create a superuser first.")
