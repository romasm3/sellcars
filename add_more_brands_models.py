#!/usr/bin/env python
"""Add more brands and models to the database"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Brand, CarModel

# Define brands and their models
brands_models = {
    "BMW": [
        "X1",
        "X2",
        "X3",
        "X4",
        "X5",
        "X6",
        "X7",
        "1 Series",
        "2 Series",
        "3 Series",
        "4 Series",
        "5 Series",
        "6 Series",
        "7 Series",
        "8 Series",
        "M2",
        "M3",
        "M4",
        "M5",
        "M8",
        "i3",
        "i4",
        "i8",
        "iX",
        "Z4",
    ],
    "Mercedes-Benz": [
        "A-Class",
        "B-Class",
        "C-Class",
        "E-Class",
        "S-Class",
        "GLA",
        "GLB",
        "GLC",
        "GLE",
        "GLS",
        "G-Class",
        "CLA",
        "CLS",
        "AMG GT",
        "EQC",
        "EQS",
        "EQE",
        "V-Class",
    ],
    "Audi": [
        "A1",
        "A3",
        "A4",
        "A5",
        "A6",
        "A7",
        "A8",
        "Q2",
        "Q3",
        "Q4 e-tron",
        "Q5",
        "Q7",
        "Q8",
        "TT",
        "R8",
        "e-tron GT",
        "RS3",
        "RS4",
        "RS5",
        "RS6",
        "RS7",
    ],
    "Volkswagen": [
        "Polo",
        "Golf",
        "Golf GTI",
        "Golf R",
        "Passat",
        "Arteon",
        "Tiguan",
        "Touareg",
        "T-Roc",
        "T-Cross",
        "ID.3",
        "ID.4",
        "ID.5",
        "Up!",
        "Caddy",
    ],
    "Toyota": [
        "Corolla",
        "Camry",
        "RAV4",
        "Highlander",
        "Land Cruiser",
        "Prius",
        "Yaris",
        "Aygo",
        "C-HR",
        "bZ4X",
        "GR Supra",
        "GR Yaris",
        "Hilux",
        "Proace",
    ],
    "Ford": [
        "Fiesta",
        "Focus",
        "Mondeo",
        "Mustang",
        "Kuga",
        "Puma",
        "EcoSport",
        "Explorer",
        "Edge",
        "Ranger",
        "F-150",
        "Mustang Mach-E",
        "Bronco",
    ],
    "Honda": ["Civic", "Accord", "CR-V", "HR-V", "Jazz", "e:Ny1", "NSX", "Type R"],
    "Porsche": [
        "911",
        "Cayenne",
        "Macan",
        "Panamera",
        "Taycan",
        "718 Boxster",
        "718 Cayman",
    ],
    "Tesla": ["Model 3", "Model S", "Model X", "Model Y"],
    "Volvo": ["XC40", "XC60", "XC90", "S60", "S90", "V60", "V90", "C40 Recharge"],
    "Mazda": ["Mazda2", "Mazda3", "Mazda6", "CX-3", "CX-30", "CX-5", "CX-60", "MX-5"],
    "Nissan": ["Micra", "Juke", "Qashqai", "X-Trail", "Leaf", "Ariya", "GT-R", "370Z"],
    "Hyundai": [
        "i10",
        "i20",
        "i30",
        "Tucson",
        "Santa Fe",
        "Kona",
        "IONIQ 5",
        "IONIQ 6",
    ],
    "Kia": ["Picanto", "Rio", "Ceed", "Sportage", "Sorento", "Niro", "EV6", "Stinger"],
    "Peugeot": ["208", "308", "508", "2008", "3008", "5008", "e-208", "e-2008"],
    "Renault": ["Clio", "Megane", "Captur", "Kadjar", "Koleos", "Zoe", "Megane E-Tech"],
    "Škoda": ["Fabia", "Octavia", "Superb", "Kamiq", "Karoq", "Kodiaq", "Enyaq iV"],
    "SEAT": [
        "Ibiza",
        "Leon",
        "Arona",
        "Ateca",
        "Tarraco",
        "Cupra Formentor",
        "Cupra Leon",
    ],
    "Opel": [
        "Corsa",
        "Astra",
        "Insignia",
        "Crossland",
        "Grandland",
        "Mokka",
        "Corsa-e",
    ],
    "Fiat": ["500", "Panda", "Tipo", "500X", "500L", "Ducato", "500e"],
}


def add_brands_and_models():
    """Add brands and their models to database"""

    brands_created = 0
    models_created = 0

    for brand_name, model_names in brands_models.items():
        # Get or create brand
        brand, created = Brand.objects.get_or_create(name=brand_name)
        if created:
            brands_created += 1
            print(f"Created brand: {brand_name}")

        # Add models for this brand
        for model_name in model_names:
            car_model, created = CarModel.objects.get_or_create(
                brand=brand, name=model_name
            )
            if created:
                models_created += 1
                print(f"  + {model_name}")

    print(f"\n✅ Summary:")
    print(f"   Brands created: {brands_created}")
    print(f"   Models created: {models_created}")
    print(f"   Total brands: {Brand.objects.count()}")
    print(f"   Total models: {CarModel.objects.count()}")


if __name__ == "__main__":
    add_brands_and_models()
