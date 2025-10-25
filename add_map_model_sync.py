#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Add JavaScript to sync map model dropdown with brand selection"""

file_path = "apps/core/templates/core/home.html"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the map brand filter change handler and add model sync
old_brand_handler = """document.getElementById('mapBrandFilter')"""

# Add after the DOMContentLoaded for main search
sync_code = """
            // Sync map model filter with brand selection
            const mapBrandFilter = document.getElementById('mapBrandFilter');
            const mapModelFilter = document.getElementById('mapModelFilter');

            if (mapBrandFilter && mapModelFilter) {
                // Populate map model filter on page load
                allModels.forEach(model => {
                    const option = document.createElement('option');
                    option.value = model.name;
                    option.textContent = model.name;
                    mapModelFilter.appendChild(option);
                });

                // Update map model filter when brand changes
                mapBrandFilter.addEventListener('change', function() {
                    const selectedBrand = this.value.toLowerCase();

                    // Clear current options
                    mapModelFilter.innerHTML = '<option value="">All Models</option>';

                    if (selectedBrand) {
                        // Filter models by selected brand name
                        const filteredModels = allModels.filter(model => {
                            // Match by brand name since mapBrandFilter uses brand name as value
                            const brandMatches = allModels.some(m =>
                                m.brandId.toString() === selectedBrand ||
                                brands.some(b => b.id === m.brandId && b.name.toLowerCase() === selectedBrand)
                            );
                            return model.name.toLowerCase().includes(selectedBrand) || brandMatches;
                        });

                        // Find brand ID from brand name
                        const brandObj = brands.find(b => b.name.toLowerCase() === selectedBrand);
                        if (brandObj) {
                            const brandModels = allModels.filter(m => m.brandId === brandObj.id);
                            brandModels.forEach(model => {
                                const option = document.createElement('option');
                                option.value = model.name;
                                option.textContent = model.name;
                                mapModelFilter.appendChild(option);
                            });
                        }
                    } else {
                        // Show all models
                        allModels.forEach(model => {
                            const option = document.createElement('option');
                            option.value = model.name;
                            option.textContent = model.name;
                            mapModelFilter.appendChild(option);
                        });
                    }
                });
            }"""

# Find the right place to insert - after the main model select population
insert_marker = """            // Initialize with all models on page load
            allModels.forEach(model => {
                const option = document.createElement('option');
                option.value = model.name;
                option.textContent = model.name;
                modelSelect.appendChild(option);
            });
        }
    });
});"""

replacement = (
    """            // Initialize with all models on page load
            allModels.forEach(model => {
                const option = document.createElement('option');
                option.value = model.name;
                option.textContent = model.name;
                modelSelect.appendChild(option);
            });

            // Also populate brands array for map filter
            const brands = [
                {% for brand in brands %}
                {
                    id: {{ brand.id }},
                    name: "{{ brand.name }}"
                }{% if not forloop.last %},{% endif %}
                {% endfor %}
            ];
"""
    + sync_code
    + """
        }
    });
});"""
)

content = content.replace(insert_marker, replacement)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully added map model dropdown sync!")
