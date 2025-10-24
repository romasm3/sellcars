# apps/core/forms.py
from django import forms
from .models import Car, CarImage, Brand


class CarForm(forms.ModelForm):
    """Form for creating/editing car advertisements"""

    class Meta:
        model = Car
        fields = [
            "title",
            "brand",
            "model",
            "year",
            "body_type",
            "condition",
            "mileage",
            "fuel_type",
            "transmission",
            "engine_size",
            "power_hp",
            "power_kw",
            "co2_emission",
            "consumption",
            "first_registration",
            "previous_owners",
            "vin",
            "description",
            "color",
            "doors",
            "seats",
            "features",
            "emission_class",
            "emission_sticker",
            "price",
            "price_per_day",
            "price_per_week",
            "is_for_sale",
            "is_for_rent",
            "location",
            "latitude",
            "longitude",
            "phone",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "e.g., BMW 430i Cabrio M Sport",
                }
            ),
            "brand": forms.Select(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "e.g., 430i",
                }
            ),
            "year": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "2020",
                    "min": "1900",
                    "max": "2025",
                }
            ),
            "body_type": forms.Select(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                }
            ),
            "condition": forms.Select(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                }
            ),
            "mileage": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "50000",
                }
            ),
            "fuel_type": forms.Select(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                }
            ),
            "transmission": forms.Select(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                }
            ),
            "engine_size": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "2000",
                }
            ),
            "power_hp": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "252",
                }
            ),
            "power_kw": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "185",
                }
            ),
            "co2_emission": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "169",
                }
            ),
            "consumption": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "7.3",
                    "step": "0.1",
                }
            ),
            "first_registration": forms.DateInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "type": "date",
                }
            ),
            "previous_owners": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "1",
                    "min": "0",
                }
            ),
            "vin": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "WBA1234567890",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "Describe your car in detail...",
                    "rows": 6,
                }
            ),
            "color": forms.Select(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                }
            ),
            "doors": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "4",
                    "min": "2",
                    "max": "5",
                }
            ),
            "seats": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "5",
                    "min": "2",
                    "max": "9",
                }
            ),
            "features": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "e.g., Leather seats, Navigation, Sunroof, Parking sensors",
                    "rows": 3,
                }
            ),
            "emission_class": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "Euro 6",
                }
            ),
            "emission_sticker": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "Green",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "32900",
                    "step": "100",
                }
            ),
            "price_per_day": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "150",
                    "step": "10",
                }
            ),
            "price_per_week": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "900",
                    "step": "50",
                }
            ),
            "is_for_sale": forms.CheckboxInput(
                attrs={
                    "class": "w-4 h-4 text-orange-500 bg-slate-700 border-slate-600 rounded focus:ring-orange-500"
                }
            ),
            "is_for_rent": forms.CheckboxInput(
                attrs={
                    "class": "w-4 h-4 text-orange-500 bg-slate-700 border-slate-600 rounded focus:ring-orange-500"
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "Berlin, Germany",
                }
            ),
            "latitude": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "52.520008",
                    "step": "0.000001",
                }
            ),
            "longitude": forms.NumberInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "13.404954",
                    "step": "0.000001",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500",
                    "placeholder": "+49 30 12345678",
                }
            ),
        }


class CarImageForm(forms.ModelForm):
    """Form for uploading car images"""

    class Meta:
        model = CarImage
        fields = ["image", "is_main"]
        widgets = {
            "image": forms.FileInput(attrs={"class": "hidden", "accept": "image/*"}),
            "is_main": forms.CheckboxInput(
                attrs={
                    "class": "w-4 h-4 text-orange-500 bg-slate-700 border-slate-600 rounded focus:ring-orange-500"
                }
            ),
        }


# Formset for multiple images
CarImageFormSet = forms.inlineformset_factory(
    Car, CarImage, form=CarImageForm, extra=5, max_num=10, can_delete=True
)
