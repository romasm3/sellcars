#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Populate map model dropdown from cars data"""

file_path = "apps/core/templates/core/home.html"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find where to add the code - after map initialization and before filterMapCars function
insert_marker = """    // Fit bounds to show all cars
    if (cars.length > 0) {
        var group = new L.featureGroup(markers.map(m => m.marker));
        map.fitBounds(group.getBounds().pad(0.1));
    }"""

new_code = """    // Fit bounds to show all cars
    if (cars.length > 0) {
        var group = new L.featureGroup(markers.map(m => m.marker));
        map.fitBounds(group.getBounds().pad(0.1));
    }

    // Populate map model dropdown with unique models from cars
    var mapModelFilter = document.getElementById('mapModelFilter');
    if (mapModelFilter && cars.length > 0) {
        var uniqueModels = [...new Set(cars.map(car => car.model))].sort();
        uniqueModels.forEach(function(model) {
            var option = document.createElement('option');
            option.value = model;
            option.textContent = model;
            mapModelFilter.appendChild(option);
        });
    }

    // Populate map brand dropdown with unique brands from cars
    var mapBrandFilter = document.getElementById('mapBrandFilter');
    if (mapBrandFilter && cars.length > 0) {
        var currentOptions = Array.from(mapBrandFilter.options).map(opt => opt.value);
        var uniqueBrands = [...new Set(cars.map(car => car.brand))].sort();

        // Add brands that aren't already in the dropdown
        uniqueBrands.forEach(function(brand) {
            if (!currentOptions.includes(brand)) {
                var option = document.createElement('option');
                option.value = brand;
                option.textContent = brand;
                mapBrandFilter.appendChild(option);
            }
        });
    }

    // Update map model dropdown when brand changes
    if (mapBrandFilter && mapModelFilter) {
        mapBrandFilter.addEventListener('change', function() {
            var selectedBrand = this.value;

            // Clear and repopulate model dropdown
            mapModelFilter.innerHTML = '<option value="">All Models</option>';

            var modelsToShow = selectedBrand
                ? cars.filter(car => car.brand === selectedBrand).map(car => car.model)
                : cars.map(car => car.model);

            var uniqueModels = [...new Set(modelsToShow)].sort();
            uniqueModels.forEach(function(model) {
                var option = document.createElement('option');
                option.value = model;
                option.textContent = model;
                mapModelFilter.appendChild(option);
            });
        });
    }"""

content = content.replace(insert_marker, new_code)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully added map model dropdown population!")
