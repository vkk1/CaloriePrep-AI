from models.state import CaloriePlanState
from jinja2 import Template
import os

def formatter_agent(state: CaloriePlanState) -> CaloriePlanState:
    template_str = """
# 🥗 CaloriePrep AI Meal Plan

{% for day, meals in planned_meals.items() %}
## {{ day }}

{% for meal_type, meal_name in meals.items() %}
### 🍽️ {{ meal_type.title() }}: {{ meal_name }}

{% set details = meal_details.get(meal_name, {}) %}
- **Calories**: {{ details.get("calories", "N/A") }}
- **Nutrition Check**: {{ details.get("nutrition_check", "N/A") }}

**🧂 Ingredients:**
{% for ing in details.get("ingredients", []) %}
- {{ ing }}
{% endfor %}

**📝 Instructions:**
{% for step in details.get("instructions", []) %}
{{ loop.index }}. {{ step }}
{% endfor %}

---
{% endfor %}
{% endfor %}
"""

    template = Template(template_str)
    markdown = template.render(
        planned_meals=state.planned_meals,
        meal_details=state.meal_details
    )

    state.final_markdown = markdown

    # Save to file
    os.makedirs("output", exist_ok=True)
    with open("output/sample_plan.md", "w", encoding="utf-8") as f:
        f.write(markdown)

    return state
