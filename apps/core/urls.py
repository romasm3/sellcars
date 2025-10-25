# apps/core/urls.py
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    # Public pages
    path("", views.home, name="home"),
    path("cars/", views.car_list, name="car_list"),
    path("cars/<slug:slug>/", views.car_detail, name="car_detail"),
    # User advertisements
    path("my-advertisements/", views.my_advertisements, name="my_advertisements"),
    path(
        "my-advertisements/create/",
        views.advertisement_create,
        name="advertisement_create",
    ),
    path(
        "my-advertisements/<slug:slug>/edit/",
        views.advertisement_edit,
        name="advertisement_edit",
    ),
    path(
        "my-advertisements/<slug:slug>/delete/",
        views.advertisement_delete,
        name="advertisement_delete",
    ),
    # User vehicles
    path("my-vehicles/", views.my_vehicles, name="my_vehicles"),
    # API endpoints
    path(
        "api/models/<int:brand_id>/",
        views.get_models_by_brand,
        name="get_models_by_brand",
    ),
]
