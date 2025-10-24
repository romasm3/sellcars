# apps/core/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Brand(models.Model):
    """Car brand/manufacturer"""

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    logo = models.ImageField(upload_to="brands/", blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Car(models.Model):
    """Car listing/Advertisement"""

    FUEL_CHOICES = [
        ("petrol", "Benzin"),
        ("diesel", "Diesel"),
        ("electric", "Elektro"),
        ("hybrid", "Hybrid"),
        ("lpg", "Autogas (LPG)"),
        ("cng", "Erdgas (CNG)"),
    ]

    TRANSMISSION_CHOICES = [
        ("manual", "Schaltgetriebe"),
        ("automatic", "Automatik"),
        ("semi_automatic", "Halbautomatik"),
    ]

    CONDITION_CHOICES = [
        ("new", "Neu"),
        ("used", "Gebraucht"),
        ("damaged", "Unfallfahrzeug"),
        ("vintage", "Oldtimer"),
    ]

    BODY_TYPE_CHOICES = [
        ("sedan", "Limousine"),
        ("suv", "SUV/Geländewagen"),
        ("coupe", "Coupé"),
        ("cabrio", "Cabrio/Roadster"),
        ("wagon", "Kombi"),
        ("van", "Van/Kleinbus"),
        ("pickup", "Pick-up"),
        ("hatchback", "Kleinwagen"),
    ]

    COLOR_CHOICES = [
        ("black", "Schwarz"),
        ("white", "Weiß"),
        ("silver", "Silber"),
        ("gray", "Grau"),
        ("blue", "Blau"),
        ("red", "Rot"),
        ("green", "Grün"),
        ("yellow", "Gelb"),
        ("orange", "Orange"),
        ("brown", "Braun"),
        ("beige", "Beige"),
        ("gold", "Gold"),
    ]

    # Basic info
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="cars")
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    # Technical details
    mileage = models.IntegerField(help_text="Kilometerstand")
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    engine_size = models.IntegerField(
        help_text="Hubraum in cm³",
        null=True,
        blank=True,
    )
    power_hp = models.IntegerField(help_text="Leistung in PS", default=100)
    power_kw = models.IntegerField(help_text="Leistung in kW", null=True, blank=True)
    condition = models.CharField(
        max_length=20, choices=CONDITION_CHOICES, default="used"
    )
    body_type = models.CharField(
        max_length=20, choices=BODY_TYPE_CHOICES, default="sedan"
    )

    # Registration details
    first_registration = models.DateField(
        help_text="Erstzulassung", null=True, blank=True
    )
    previous_owners = models.IntegerField(default=0, help_text="Vorbesitzer")
    vin = models.CharField(
        max_length=17, blank=True, help_text="Fahrzeugidentifikationsnummer"
    )

    # Additional specs
    description = models.TextField()
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    doors = models.IntegerField(default=4)
    seats = models.IntegerField(default=5)
    co2_emission = models.IntegerField(
        null=True, blank=True, help_text="CO2-Emission in g/km"
    )
    consumption = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="Kraftstoffverbrauch l/100km",
    )

    # Features
    features = models.TextField(blank=True, help_text="Ausstattung (comma separated)")

    # Environmental badge
    emission_class = models.CharField(
        max_length=20, blank=True, help_text="Schadstoffklasse"
    )
    emission_sticker = models.CharField(
        max_length=20, blank=True, help_text="Umweltplakette"
    )

    # Price and location
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_day = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Daily rental price",
    )
    price_per_week = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Weekly rental price",
    )
    is_for_sale = models.BooleanField(default=True, help_text="Car is for sale")
    is_for_rent = models.BooleanField(
        default=False, help_text="Car is available for rent"
    )
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text="Latitude coordinate",
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        help_text="Longitude coordinate",
    )

    # Seller info
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cars")
    phone = models.CharField(max_length=20)

    # Metadata
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.brand}-{self.model}-{self.year}")
            self.slug = base_slug
        # Auto calculate kW from HP if not provided
        if self.power_hp and not self.power_kw:
            self.power_kw = int(self.power_hp * 0.735)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:car_detail", kwargs={"slug": self.slug})

    def get_main_image(self):
        """Get main image or first image"""
        main_img = self.images.filter(is_main=True).first()
        if main_img:
            return main_img
        return self.images.first()

    @property
    def power_display(self):
        """Display power in both HP and kW"""
        if self.power_kw:
            return f"{self.power_hp} PS/{self.power_kw} kW"
        return f"{self.power_hp} PS"


class CarImage(models.Model):
    """Car images"""

    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="cars/")
    is_main = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_main", "uploaded_at"]

    def __str__(self):
        return f"Image for {self.car}"
