#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Change Model input to dropdown select"""

file_path = "apps/core/templates/core/home.html"

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace text input with select dropdown
old_model_input = """                        <input
                            type="text"
                            name="model"
                            placeholder="Enter model..."
                            class="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-orange-500"
                        />"""

new_model_select = """                        <select
                            id="modelSelect"
                            name="model"
                            class="w-full px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-orange-500"
                        >
                            <option value="">All Models</option>
                        </select>"""

content = content.replace(old_model_input, new_model_select)

# Add JavaScript at the end before {% endblock %}
javascript_code = """
<!-- Brand/Model Dynamic Filter Script -->
<script>
    document.addEventListener('DOMContentLoaded', function() {
        // Store all models data
        const allModels = [
            {% for model in models %}
            {
                id: "{{ model.name }}",
                name: "{{ model.name }}",
                brandId: {{ model.brand.id }}
            }{% if not forloop.last %},{% endif %}
            {% endfor %}
        ];

        // Get brand and model select elements
        const brandSelect = document.querySelector('select[name="brand"]');
        const modelSelect = document.getElementById('modelSelect');

        if (brandSelect && modelSelect) {
            // Update models when brand changes
            brandSelect.addEventListener('change', function() {
                const selectedBrandId = parseInt(this.value);

                // Clear current options except "All Models"
                modelSelect.innerHTML = '<option value="">All Models</option>';

                if (selectedBrandId) {
                    // Filter models by selected brand
                    const filteredModels = allModels.filter(model => model.brandId === selectedBrandId);

                    // Add filtered models to select
                    filteredModels.forEach(model => {
                        const option = document.createElement('option');
                        option.value = model.name;
                        option.textContent = model.name;
                        modelSelect.appendChild(option);
                    });
                } else {
                    // If no brand selected, show all models
                    allModels.forEach(model => {
                        const option = document.createElement('option');
                        option.value = model.name;
                        option.textContent = model.name;
                        modelSelect.appendChild(option);
                    });
                }
            });

            // Initialize with all models on page load
            allModels.forEach(model => {
                const option = document.createElement('option');
                option.value = model.name;
                option.textContent = model.name;
                modelSelect.appendChild(option);
            });
        }
    });
</script>

{% endblock %}"""

# Replace the endblock
content = content.replace("{% endblock %}", javascript_code)

# Write back
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully changed Model to dropdown with JavaScript!")
