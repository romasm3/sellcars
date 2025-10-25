import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Brand, CarModel
from django.utils.text import slugify

# Brands from user's list
user_brands = [
    "Abarth",
    "AC",
    "Acura",
    "Aiways",
    "Aixam",
    "Alfa Romeo",
    "Alpina",
    "Ariel",
    "ARO",
    "Asia",
    "Austin Rover",
    "Austin-Healey",
    "Bontu",
    "Brilliance",
    "Buick",
    "Casalini",
    "Cemitro",
    "Chatenet",
    "Chery",
    "Cobra",
    "Datsun",
    "De Tomaso",
    "DeLorean",
    "DFSK",
    "Donkervoort",
    "Foton",
    "GAZ",
    "Geo",
    "Gonow",
    "GWM",
    "Hongqi",
    "Hudson",
    "IFA",
    "Ineos",
    "Isuzu",
    "Iveco",
    "KTM",
    "Lada",
    "Landwind",
    "Lifan",
    "Luxgen",
    "Maybach",
    "Mercury",
    "Microcar",
    "Morgan",
    "Moskvich",
    "MPM",
    "Norster",
    "Nysa",
    "Oldsmobile",
    "Ozeta",
    "Plymouth",
    "ROX",
    "RUNHORSE",
    "SAIC",
    "Santana",
    "Saturn",
    "Scion",
    "Seeme",
    "Seres",
    "Shuanghuan",
    "Silence",
    "Skywell",
    "Spartan",
    "Sportequipe",
    "Spyker",
    "Tazzari",
    "Think",
    "Trabant",
    "Triumph",
    "UAZ",
    "Vauxhall",
    "Venturi",
    "Voyah",
    "Wanderer",
    "Wartburg",
    "XEV",
    "Xiaomi",
    "Zastava",
    "ZAZ",
    "Zeekr",
    "Zotye",
    "ЗИЛ",
    "УАЗ",
]

# Brand models dictionary
brand_models = {
    "Abarth": ["500", "595", "695", "124 Spider", "Grande Punto"],
    "AC": ["Cobra", "Ace", "Aceca", "Greyhound", "428"],
    "Acura": ["Integra", "TLX", "MDX", "RDX", "NSX", "ILX", "RLX", "TSX"],
    "Aiways": ["U5", "U6", "U7"],
    "Aixam": ["City", "Crossline", "Coupe", "e-City", "e-Crossline"],
    "Alfa Romeo": [
        "Giulia",
        "Stelvio",
        "Tonale",
        "Giulietta",
        "MiTo",
        "4C",
        "159",
        "156",
        "147",
        "GT",
    ],
    "Alpina": ["B3", "B4", "B5", "B7", "B8", "XB7", "XD3", "XD4"],
    "Ariel": ["Atom", "Nomad", "Hipercar"],
    "ARO": ["10", "24", "240", "244", "320"],
    "Asia": ["Rocsta", "Retona", "Topic", "Combi", "Towner"],
    "Austin Rover": ["Mini", "Maestro", "Montego", "Metro"],
    "Austin-Healey": ["Sprite", "100", "3000", "100-6"],
    "Bontu": ["E1", "E2", "E3"],
    "Brilliance": ["V5", "V6", "V7", "BC3", "BS6"],
    "Buick": ["Enclave", "Encore", "Envision", "Regal", "LaCrosse", "Verano"],
    "Casalini": ["M10", "M12", "M14", "M20"],
    "Cemitro": ["C1", "C2"],
    "Chatenet": ["CH26", "CH30", "CH32", "CH40", "CH46", "Barooder"],
    "Chery": ["Tiggo", "Tiggo 7", "Tiggo 8", "Tiggo 4", "Arrizo", "QQ"],
    "Cobra": ["427", "289", "Daytona"],
    "Datsun": ["280Z", "240Z", "510", "620", "720", "1200"],
    "De Tomaso": ["Pantera", "Mangusta", "Deauville", "Longchamp"],
    "DeLorean": ["DMC-12"],
    "DFSK": ["Glory 580", "Glory 560", "Fengon 5", "Fengon 7"],
    "Donkervoort": ["D8", "D8 GTO", "F22"],
    "Foton": ["Tunland", "Toano", "View", "Aumark"],
    "GAZ": ["Volga", "21", "24", "31", "3110", "Sobol"],
    "Geo": ["Metro", "Prizm", "Tracker", "Storm"],
    "Gonow": ["Troy", "GX6", "GA200"],
    "GWM": ["Wingle", "Poer", "Cannon", "Tank 300", "Tank 500"],
    "Hongqi": ["H5", "H7", "H9", "E-HS9", "HS5", "HS7"],
    "Hudson": ["Hornet", "Commodore", "Super Six", "Terraplane"],
    "IFA": ["F9", "W50", "L60", "Barkas"],
    "Ineos": ["Grenadier"],
    "Isuzu": ["D-Max", "MU-X", "Trooper", "Rodeo", "Ascender", "VehiCross"],
    "Iveco": ["Daily", "Eurocargo", "Stralis", "S-Way"],
    "KTM": ["X-Bow", "X-Bow GT", "X-Bow GTX"],
    "Lada": ["Niva", "Vesta", "Granta", "Largus", "XRAY", "2107", "2106", "2105"],
    "Landwind": ["X7", "X5", "X6", "X2", "CV9"],
    "Lifan": ["X60", "X70", "X50", "Solano", "Breez", "320", "520"],
    "Luxgen": ["U5", "U6", "U7", "S5", "M7"],
    "Maybach": ["S-Class", "S 560", "S 650", "GLS 600", "57", "62"],
    "Mercury": ["Grand Marquis", "Sable", "Milan", "Mountaineer", "Mariner"],
    "Microcar": ["M.Go", "M8", "Dué", "M.Cross"],
    "Morgan": ["Plus Four", "Plus Six", "3 Wheeler", "Aero 8"],
    "Moskvich": ["408", "412", "2141", "2140", "3"],
    "MPM": ["Motors Pulse"],
    "Norster": ["N1"],
    "Nysa": ["522", "501", "521"],
    "Oldsmobile": ["Cutlass", "88", "98", "Aurora", "Intrigue", "Alero"],
    "Ozeta": ["City"],
    "Plymouth": ["Barracuda", "Fury", "Valiant", "Road Runner", "GTX"],
    "ROX": ["R1"],
    "RUNHORSE": ["Celer", "Manso"],
    "SAIC": ["Maxus", "Roewe", "MG"],
    "Santana": ["PS-10"],
    "Saturn": ["S-Series", "L-Series", "Vue", "Ion", "Sky", "Aura"],
    "Scion": ["tC", "xB", "xD", "FR-S", "iQ"],
    "Seeme": ["E10"],
    "Seres": ["SF5", "SF7"],
    "Shuanghuan": ["SCEO", "CEO"],
    "Silence": ["S01", "S02", "S04"],
    "Skywell": ["ET5"],
    "Spartan": ["300"],
    "Sportequipe": ["SE1"],
    "Spyker": ["C8", "C12"],
    "Tazzari": ["Zero", "EM1"],
    "Think": ["City"],
    "Trabant": ["601", "P50", "P60", "1.1"],
    "Triumph": ["TR6", "TR7", "Spitfire", "Stag", "GT6"],
    "UAZ": ["Hunter", "Patriot", "452", "469", "3303"],
    "Vauxhall": ["Corsa", "Astra", "Insignia", "Mokka", "Grandland", "Crossland"],
    "Venturi": ["Fetish", "America", "Atlantique"],
    "Voyah": ["Free", "Dreamer", "Passion"],
    "Wanderer": ["W24", "W25"],
    "Wartburg": ["353", "311", "312"],
    "XEV": ["Yoyo"],
    "Xiaomi": ["SU7"],
    "Zastava": ["Yugo", "101", "128", "750", "850"],
    "ZAZ": ["965", "966", "968", "1102", "Lanos", "Chance", "Forza"],
    "Zeekr": ["001", "009", "X", "007"],
    "Zotye": ["T600", "SR9", "Z100", "Z300", "T700"],
    "ЗИЛ": ["130", "131", "157", "164"],
    "УАЗ": ["Hunter", "Patriot", "452", "469", "3303"],
}

# Get existing brands
existing_brands = set(Brand.objects.values_list("name", flat=True))

# Find missing brands
missing_brands = [brand for brand in user_brands if brand not in existing_brands]

print(f"Total brands in user's list: {len(user_brands)}")
print(f"Existing brands: {len(existing_brands)}")
print(f"Missing brands to add: {len(missing_brands)}")
print(f"\nMissing brands: {', '.join(missing_brands)}")

# Add missing brands and their models
brands_added = 0
models_added = 0

for brand_name in missing_brands:
    # Create brand with proper slug handling for Cyrillic and special characters
    slug = slugify(brand_name)
    # If slug is empty (e.g., for Cyrillic), use transliteration or name
    if not slug:
        # For Cyrillic brands, use their Latin equivalent or just the name
        cyrillic_map = {"ЗИЛ": "zil", "УАЗ": "uaz-cyrillic"}
        slug = cyrillic_map.get(brand_name, brand_name.lower().replace(" ", "-"))

    brand, created = Brand.objects.get_or_create(
        name=brand_name, defaults={"slug": slug}
    )

    if created:
        brands_added += 1
        print(f"\n✓ Added brand: {brand_name}")

        # Add models for this brand
        models = brand_models.get(brand_name, [])
        for model_name in models:
            model, model_created = CarModel.objects.get_or_create(
                brand=brand, name=model_name, defaults={"slug": slugify(model_name)}
            )
            if model_created:
                models_added += 1

        print(f"  Added {len(models)} models")

print(f"\n{'=' * 60}")
print(f"SUMMARY:")
print(f"Brands added: {brands_added}")
print(f"Models added: {models_added}")
print(f"Total brands in database: {Brand.objects.count()}")
print(f"Total models in database: {CarModel.objects.count()}")
print(f"{'=' * 60}")
