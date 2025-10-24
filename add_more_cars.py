#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Brand, Car
from django.contrib.auth.models import User

# Get admin user
admin_user = User.objects.filter(is_superuser=True).first()

if admin_user:
    print("Adding more cars with Berlin location...\n")

    # Get brands
    audi = Brand.objects.get(name="Audi")
    mercedes = Brand.objects.get(name="Mercedes-Benz")
    volkswagen = Brand.objects.get(name="Volkswagen")

    # Audi A4 - Berlin
    car1, created = Car.objects.get_or_create(
        title="Audi A4 Avant 2.0 TDI S line",
        defaults={
            "brand": audi,
            "model": "A4 Avant",
            "year": 2020,
            "body_type": "wagon",
            "mileage": 35000,
            "fuel_type": "diesel",
            "transmission": "automatic",
            "engine_size": 2000,
            "power_hp": 190,
            "condition": "used",
            "first_registration": date(2020, 3, 15),
            "previous_owners": 1,
            "description": "Gepflegter Audi A4 Avant mit S line Paket und voller Ausstattung.",
            "color": "blue",
            "doors": 5,
            "seats": 5,
            "co2_emission": 138,
            "consumption": 5.2,
            "features": "S line, LED Scheinwerfer, Virtual Cockpit, Navi Plus, Parkassistent",
            "emission_class": "Euro 6d",
            "price": 28900,
            "price_per_day": 85,
            "price_per_week": 550,
            "is_for_sale": True,
            "is_for_rent": True,
            "location": "Berlin",
            "latitude": 52.516275,
            "longitude": 13.377704,
            "seller": admin_user,
            "phone": "+49 30 11111111",
            "is_active": True,
        },
    )
    if created:
        print(f"✅ Created: {car1.title}")

    # Mercedes C-Class - Berlin
    car2, created = Car.objects.get_or_create(
        title="Mercedes-Benz C 200 AMG Line",
        defaults={
            "brand": mercedes,
            "model": "C 200",
            "year": 2019,
            "body_type": "sedan",
            "mileage": 42000,
            "fuel_type": "petrol",
            "transmission": "automatic",
            "engine_size": 2000,
            "power_hp": 184,
            "condition": "used",
            "first_registration": date(2019, 7, 10),
            "previous_owners": 1,
            "description": "Elegante Mercedes C-Klasse mit AMG Line Paket.",
            "color": "black",
            "doors": 4,
            "seats": 5,
            "co2_emission": 155,
            "consumption": 6.8,
            "features": "AMG Line, MBUX, LED High Performance, Burmester Sound, 360° Kamera",
            "emission_class": "Euro 6d-TEMP",
            "price": 31500,
            "price_per_day": 95,
            "price_per_week": 620,
            "is_for_sale": True,
            "is_for_rent": True,
            "location": "Berlin",
            "latitude": 52.524877,
            "longitude": 13.369548,
            "seller": admin_user,
            "phone": "+49 30 22222222",
            "is_active": True,
        },
    )
    if created:
        print(f"✅ Created: {car2.title}")

    # VW Golf GTI - Berlin
    car3, created = Car.objects.get_or_create(
        title="Volkswagen Golf 8 GTI",
        defaults={
            "brand": volkswagen,
            "model": "Golf GTI",
            "year": 2021,
            "body_type": "hatchback",
            "mileage": 18000,
            "fuel_type": "petrol",
            "transmission": "automatic",
            "engine_size": 2000,
            "power_hp": 245,
            "condition": "used",
            "first_registration": date(2021, 4, 20),
            "previous_owners": 1,
            "description": "Sportlicher Golf GTI der 8. Generation.",
            "color": "red",
            "doors": 5,
            "seats": 5,
            "co2_emission": 172,
            "consumption": 7.5,
            "features": "DCC, Digital Cockpit Pro, IQ.LIGHT LED Matrix, Soundsystem",
            "emission_class": "Euro 6d",
            "price": 35900,
            "price_per_day": 110,
            "price_per_week": 700,
            "is_for_sale": True,
            "is_for_rent": True,
            "location": "Berlin",
            "latitude": 52.519444,
            "longitude": 13.406667,
            "seller": admin_user,
            "phone": "+49 30 33333333",
            "is_active": True,
        },
    )
    if created:
        print(f"✅ Created: {car3.title}")

    print("\n" + "=" * 60)
    print("✅ Cars added successfully!")
    print(f"Total cars: {Car.objects.count()}")
    print("=" * 60)
else:
    print("❌ No admin user found. Please create a superuser first.")
