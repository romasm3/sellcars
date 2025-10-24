# apps/core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Car, Brand, CarImage


def home(request):
    """Home page with featured cars"""
    from django.contrib.auth.models import User

    featured_cars = (
        Car.objects.filter(is_active=True)
        .select_related("brand")
        .prefetch_related("images")[:6]
    )
    brands = Brand.objects.all()

    # Stats
    total_cars = Car.objects.filter(is_active=True).count()
    total_brands = Brand.objects.count()
    total_users = User.objects.count()

    context = {
        "featured_cars": featured_cars,
        "brands": brands,
        "total_cars": total_cars,
        "total_brands": total_brands,
        "total_users": total_users,
    }
    return render(request, "core/home.html", context)


def car_list(request):
    """All cars listing page"""
    cars = (
        Car.objects.filter(is_active=True)
        .select_related("brand")
        .prefetch_related("images")
    )

    # Filters
    brand_id = request.GET.get("brand")
    fuel_type = request.GET.get("fuel_type")
    transmission = request.GET.get("transmission")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    if brand_id:
        cars = cars.filter(brand_id=brand_id)
    if fuel_type:
        cars = cars.filter(fuel_type=fuel_type)
    if transmission:
        cars = cars.filter(transmission=transmission)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)

    brands = Brand.objects.all()

    context = {
        "cars": cars,
        "brands": brands,
    }
    return render(request, "core/car_list.html", context)


def car_detail(request, slug):
    """Car detail page"""
    car = get_object_or_404(
        Car.objects.select_related("brand", "seller").prefetch_related("images"),
        slug=slug,
    )

    # Increment views
    car.views += 1
    car.save(update_fields=["views"])

    # Get similar cars
    similar_cars = (
        Car.objects.filter(brand=car.brand, is_active=True)
        .exclude(id=car.id)
        .select_related("brand")
        .prefetch_related("images")[:3]
    )

    context = {
        "car": car,
        "similar_cars": similar_cars,
    }
    return render(request, "core/car_detail.html", context)


@login_required
def my_advertisements(request):
    """User's car listings"""
    cars = (
        Car.objects.filter(seller=request.user)
        .select_related("brand")
        .prefetch_related("images")
        .order_by("-created_at")
    )

    context = {
        "cars": cars,
        "active_menu": "advertisements",
    }
    return render(request, "core/my_advertisements.html", context)


@login_required
def my_vehicles(request):
    """User's vehicles page"""
    cars = (
        Car.objects.filter(seller=request.user)
        .select_related("brand")
        .prefetch_related("images")
    )

    context = {
        "cars": cars,
        "active_menu": "vehicles",
    }
    return render(request, "core/my_vehicles.html", context)


@login_required
def advertisement_create(request):
    """Create new car advertisement"""
    from .forms import CarForm

    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)

        if form.is_valid():
            car = form.save(commit=False)
            car.seller = request.user

            # Ensure at least one availability option is selected
            if not car.is_for_sale and not car.is_for_rent:
                car.is_for_sale = True  # Default to for sale

            car.save()

            # Handle image uploads
            images = request.FILES.getlist("images")
            if images:
                for i, image in enumerate(images):
                    CarImage.objects.create(
                        car=car,
                        image=image,
                        is_main=(i == 0),  # First image is main
                    )

            messages.success(
                request,
                f"Advertisement for {car.brand} {car.model} created successfully!",
            )
            return redirect("core:my_advertisements")
        else:
            # Add error message if form is invalid
            print("Form validation errors:", form.errors)
            messages.error(
                request,
                "Please correct the errors below and try again.",
            )
    else:
        # Initialize form with default values
        initial_data = {
            "is_for_sale": True,  # Default to for sale
            "is_for_rent": False,
            "doors": 4,
            "seats": 5,
            "previous_owners": 0,
        }
        form = CarForm(initial=initial_data)

    context = {
        "form": form,
        "active_menu": "advertisements",
    }
    return render(request, "core/advertisement_create.html", context)


@login_required
def advertisement_edit(request, slug):
    """Edit car advertisement"""
    car = get_object_or_404(Car, slug=slug, seller=request.user)

    context = {
        "car": car,
        "active_menu": "advertisements",
    }
    return render(request, "core/advertisement_edit.html", context)


@login_required
def advertisement_delete(request, slug):
    """Delete car advertisement"""
    car = get_object_or_404(Car, slug=slug, seller=request.user)

    if request.method == "POST":
        car.delete()
        messages.success(request, "Advertisement deleted successfully!")
        return redirect("core:my_advertisements")

    context = {
        "car": car,
        "active_menu": "advertisements",
    }
    return render(request, "core/advertisement_delete.html", context)
