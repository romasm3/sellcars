import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.core.models import Brand, CarModel

print(f"Total brands in database: {Brand.objects.count()}")
print(f"Total models in database: {CarModel.objects.count()}")

print(f"\nRecently added brands (last 15):")
for brand in Brand.objects.order_by("-id")[:15]:
    model_count = brand.models.count()
    print(f"  - {brand.name} ({model_count} models)")
