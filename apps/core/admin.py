from django.contrib import admin
from .models import Brand, Car, CarImage


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 3
    fields = ("image", "is_main")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "brand",
        "model",
        "year",
        "price",
        "mileage",
        "power_display",
        "seller",
        "is_active",
        "created_at",
    )
    list_filter = (
        "brand",
        "fuel_type",
        "transmission",
        "condition",
        "body_type",
        "is_active",
        "created_at",
    )
    search_fields = ("title", "brand__name", "model", "description")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("views", "created_at", "updated_at")

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "brand",
                    "model",
                    "year",
                    "body_type",
                    "condition",
                )
            },
        ),
        (
            "Technical Specifications",
            {
                "fields": (
                    "mileage",
                    "fuel_type",
                    "transmission",
                    "engine_size",
                    "power_hp",
                    "power_kw",
                    "co2_emission",
                    "consumption",
                )
            },
        ),
        (
            "Registration Details",
            {"fields": ("first_registration", "previous_owners", "vin")},
        ),
        (
            "Additional Information",
            {"fields": ("description", "color", "doors", "seats", "features")},
        ),
        (
            "Environmental",
            {
                "fields": ("emission_class", "emission_sticker"),
                "classes": ("collapse",),
            },
        ),
        ("Price & Location", {"fields": ("price", "location")}),
        ("Seller Information", {"fields": ("seller", "phone")}),
        (
            "Metadata",
            {
                "fields": ("views", "is_active", "created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    inlines = [CarImageInline]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.seller = request.user
        super().save_model(request, obj, form, change)


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ("car", "is_main", "uploaded_at")
    list_filter = ("is_main", "uploaded_at")
    search_fields = ("car__title",)
