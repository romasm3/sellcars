#!/usr/bin/env python
"""Add all major world car brands and their models"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Brand, CarModel

# All major world car brands and their models
all_brands_models = {
    # Luxury/Premium Brands
    "Lamborghini": [
        "Aventador",
        "Huracán",
        "Urus",
        "Countach",
        "Diablo",
        "Murciélago",
        "Gallardo",
        "Reventón",
        "Veneno",
        "Centenario",
        "Sián",
    ],
    "Ferrari": [
        "F8 Tributo",
        "SF90 Stradale",
        "296 GTB",
        "Roma",
        "Portofino",
        "812 Superfast",
        "488 GTB",
        "458 Italia",
        "California",
        "F12berlinetta",
        "LaFerrari",
        "Enzo",
        "F40",
        "F50",
        "Testarossa",
        "599 GTB",
    ],
    "Bugatti": [
        "Chiron",
        "Veyron",
        "Divo",
        "Centodieci",
        "La Voiture Noire",
        "EB110",
        "Bolide",
        "Mistral",
    ],
    "Rolls-Royce": [
        "Phantom",
        "Ghost",
        "Wraith",
        "Dawn",
        "Cullinan",
        "Spectre",
        "Silver Shadow",
        "Silver Spirit",
        "Corniche",
    ],
    "Bentley": [
        "Continental GT",
        "Continental Flying Spur",
        "Bentayga",
        "Mulsanne",
        "Azure",
        "Arnage",
        "Brooklands",
        "Turbo R",
    ],
    "Aston Martin": [
        "DB11",
        "DB12",
        "DBS Superleggera",
        "Vantage",
        "DBX",
        "Rapide",
        "Vanquish",
        "One-77",
        "Valkyrie",
        "Vulcan",
        "DB9",
        "V8 Vantage",
    ],
    "McLaren": [
        "720S",
        "765LT",
        "Artura",
        "GT",
        "600LT",
        "570S",
        "P1",
        "Senna",
        "Speedtail",
        "Elva",
        "MP4-12C",
        "650S",
    ],
    "Maserati": [
        "Ghibli",
        "Quattroporte",
        "Levante",
        "MC20",
        "GranTurismo",
        "GranCabrio",
        "Alfieri",
        "3200 GT",
        "Coupe",
        "Spyder",
    ],
    "Lotus": ["Evora", "Elise", "Exige", "Emira", "Evija", "Elan", "Esprit"],
    "Pagani": ["Huayra", "Zonda", "Imola", "Utopia", "Huayra BC", "Zonda R"],
    "Koenigsegg": ["Jesko", "Gemera", "Regera", "Agera", "CCX", "One:1", "CCXR"],
    # American Brands
    "Chevrolet": [
        "Camaro",
        "Corvette",
        "Silverado",
        "Colorado",
        "Tahoe",
        "Suburban",
        "Equinox",
        "Traverse",
        "Blazer",
        "Trax",
        "Malibu",
        "Impala",
        "Cruze",
        "Bolt EV",
        "Volt",
        "Spark",
        "Sonic",
        "Aveo",
    ],
    "Cadillac": [
        "Escalade",
        "XT4",
        "XT5",
        "XT6",
        "CT4",
        "CT5",
        "CT6",
        "Lyriq",
        "CTS",
        "ATS",
        "SRX",
        "XTS",
        "DTS",
        "STS",
        "Eldorado",
    ],
    "Dodge": [
        "Challenger",
        "Charger",
        "Durango",
        "Journey",
        "Grand Caravan",
        "Viper",
        "Demon",
        "Hellcat",
        "Ram 1500",
        "Ram 2500",
    ],
    "Jeep": [
        "Wrangler",
        "Grand Cherokee",
        "Cherokee",
        "Compass",
        "Renegade",
        "Gladiator",
        "Wagoneer",
        "Grand Wagoneer",
        "Commander",
        "Patriot",
    ],
    "Lincoln": [
        "Navigator",
        "Aviator",
        "Nautilus",
        "Corsair",
        "Continental",
        "MKZ",
        "MKX",
        "MKC",
        "Town Car",
    ],
    "GMC": ["Sierra", "Canyon", "Yukon", "Acadia", "Terrain", "Savana", "Hummer EV"],
    "Ram": ["1500", "2500", "3500", "Rebel", "TRX", "Promaster"],
    "Chrysler": ["Pacifica", "300", "Voyager", "Aspen", "Sebring", "PT Cruiser"],
    # Japanese Brands
    "Lexus": [
        "ES",
        "IS",
        "GS",
        "LS",
        "LC",
        "RC",
        "NX",
        "RX",
        "GX",
        "LX",
        "UX",
        "LFA",
        "CT",
        "HS",
        "RZ",
        "TX",
    ],
    "Infiniti": [
        "Q50",
        "Q60",
        "Q70",
        "QX30",
        "QX50",
        "QX55",
        "QX60",
        "QX80",
        "G35",
        "G37",
        "M35",
        "M45",
        "FX35",
        "FX45",
    ],
    "Acura": [
        "TLX",
        "ILX",
        "MDX",
        "RDX",
        "NSX",
        "Integra",
        "ZDX",
        "TSX",
        "RSX",
        "Legend",
        "RL",
        "RLX",
    ],
    "Mitsubishi": [
        "Outlander",
        "Eclipse Cross",
        "ASX",
        "Pajero",
        "L200",
        "Lancer",
        "Mirage",
        "Colt",
        "Galant",
        "3000GT",
        "Evolution",
    ],
    "Subaru": [
        "Outback",
        "Forester",
        "XV",
        "Impreza",
        "Legacy",
        "WRX",
        "BRZ",
        "Crosstrek",
        "Ascent",
        "Tribeca",
        "SVX",
        "Levorg",
    ],
    "Suzuki": [
        "Swift",
        "Vitara",
        "S-Cross",
        "Jimny",
        "Baleno",
        "Ignis",
        "SX4",
        "Grand Vitara",
        "Kizashi",
        "Alto",
        "Celerio",
    ],
    "Daihatsu": ["Terios", "Sirion", "Copen", "Move", "Tanto", "Mira", "Rocky"],
    # Korean Brands
    "Genesis": ["G70", "G80", "G90", "GV60", "GV70", "GV80", "Electrified G80"],
    "SsangYong": ["Tivoli", "Korando", "Rexton", "Musso", "XLV", "Rodius"],
    # Chinese Brands
    "BYD": ["Han", "Tang", "Song", "Qin", "Dolphin", "Seal", "Atto 3", "e6"],
    "NIO": ["ES6", "ES7", "ES8", "ET5", "ET7", "EC6", "EC7"],
    "Geely": ["Coolray", "Azkarra", "Okavango", "Emgrand", "Tugella", "Icon"],
    "MG": ["ZS", "HS", "5", "MG4", "Marvel R", "Cyberster", "ZS EV", "MG3"],
    "Lynk & Co": ["01", "02", "03", "05", "06", "09"],
    "Polestar": ["1", "2", "3", "4", "5"],
    "Xpeng": ["P5", "P7", "G3", "G9"],
    "Li Auto": ["Li L7", "Li L8", "Li L9", "Li ONE"],
    # British Brands
    "Jaguar": [
        "XE",
        "XF",
        "XJ",
        "F-Type",
        "E-Pace",
        "F-Pace",
        "I-Pace",
        "X-Type",
        "S-Type",
        "XK",
        "XKR",
    ],
    "Land Rover": [
        "Range Rover",
        "Range Rover Sport",
        "Range Rover Velar",
        "Range Rover Evoque",
        "Discovery",
        "Discovery Sport",
        "Defender",
    ],
    "MINI": [
        "Cooper",
        "Cooper S",
        "John Cooper Works",
        "Clubman",
        "Countryman",
        "Paceman",
        "Roadster",
        "Coupe",
        "Electric",
    ],
    "Caterham": ["Seven", "620", "420", "360", "270"],
    # Italian Brands
    "Alfa Romeo": [
        "Giulia",
        "Stelvio",
        "Giulietta",
        "Tonale",
        "4C",
        "159",
        "Brera",
        "Spider",
        "MiTo",
        "GT",
        "147",
        "156",
        "166",
    ],
    "Fiat": [
        "500",
        "500X",
        "500L",
        "Panda",
        "Tipo",
        "Punto",
        "Uno",
        "Doblo",
        "Ducato",
        "500e",
        "600",
        "Bravo",
        "Stilo",
        "Multipla",
    ],
    "Lancia": ["Ypsilon", "Delta", "Thema", "Musa", "Voyager"],
    # French Brands
    "Citroën": [
        "C1",
        "C3",
        "C4",
        "C5",
        "C3 Aircross",
        "C5 Aircross",
        "Berlingo",
        "SpaceTourer",
        "ë-C4",
        "ë-Berlingo",
        "DS3",
        "DS4",
        "DS5",
    ],
    "DS Automobiles": [
        "DS 3",
        "DS 4",
        "DS 7",
        "DS 9",
        "DS 3 Crossback",
        "DS 4 Crossback",
    ],
    "Alpine": ["A110", "A310", "GTA"],
    "Dacia": ["Sandero", "Duster", "Logan", "Spring", "Jogger", "Lodgy"],
    # German Brands
    "Smart": ["ForTwo", "ForFour", "Roadster", "EQ ForTwo", "EQ ForFour", "#1", "#3"],
    # Swedish Brands
    "Saab": ["9-3", "9-5", "9-4X", "9-7X", "900", "9000"],
    # Spanish Brands
    "Cupra": ["Formentor", "Leon", "Ateca", "Born", "Tavascan"],
    # Romanian Brands
    "Dacia": ["Sandero", "Duster", "Logan", "Spring", "Jogger", "Lodgy", "Dokker"],
    # Indian Brands
    "Tata": ["Nexon", "Harrier", "Safari", "Tigor", "Altroz", "Punch", "Nano"],
    "Mahindra": ["XUV700", "XUV500", "Scorpio", "Thar", "Bolero", "XUV300"],
    # Malaysian Brands
    "Proton": ["X50", "X70", "Saga", "Persona", "Exora", "Iriz"],
    # Electric/New Energy Brands
    "Rivian": ["R1T", "R1S", "EDV"],
    "Lucid": ["Air", "Gravity"],
    "Fisker": ["Ocean", "Pear", "Karma"],
    "Faraday Future": ["FF 91"],
    "Canoo": ["Lifestyle Vehicle", "Pickup", "MPDV"],
}


def add_all_world_brands():
    """Add all world car brands and models"""

    brands_created = 0
    models_created = 0

    for brand_name, model_names in sorted(all_brands_models.items()):
        # Get or create brand
        brand, created = Brand.objects.get_or_create(name=brand_name)
        if created:
            brands_created += 1
            print(f"\n✨ {brand_name}")
        else:
            print(f"\n📦 {brand_name}")

        # Add models for this brand
        for model_name in model_names:
            car_model, created = CarModel.objects.get_or_create(
                brand=brand, name=model_name
            )
            if created:
                models_created += 1
                print(f"   + {model_name}")

    print(f"\n" + "=" * 60)
    print(f"✅ SUMMARY:")
    print(f"   New brands created: {brands_created}")
    print(f"   New models created: {models_created}")
    print(f"   Total brands in DB: {Brand.objects.count()}")
    print(f"   Total models in DB: {CarModel.objects.count()}")
    print("=" * 60)


if __name__ == "__main__":
    add_all_world_brands()
