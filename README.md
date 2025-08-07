# 🥗 CaloriePrep AI

**CaloriePrep AI** is a personalized meal planner that creates daily meal plans tailored to your calorie goals, dietary preferences, and restrictions — all powered by the Spoonacular API. It uses a LangGraph-based agent workflow to collect user input, generate recipes, check nutrition, and return structured meal plans with ingredients and instructions.

> ✨ Example use case: Generate a 3-day vegetarian meal plan with no peanuts, 1800 calories/day, and 3 meals/day — instantly!

---

## 🚀 Features

- 🍽️ Personalized meal plans
- 🥦 Diet-aware (e.g. vegetarian, keto, vegan)
- 🚫 Handles food restrictions (e.g. "no peanuts", "no dairy")
- 🔗 Uses Spoonacular API for real recipes
- 📊 Checks nutritional compliance for each meal
- 📋 Outputs ingredients, steps, and calories
- 🧠 Built using LangGraph (multi-agent state graph)
- 🖥️ Runs via Gradio UI

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/calorieprep-ai.git
cd calorieprep-ai
```

### 2. Install the Dependencies 
```pip install -r requirements.txt```

### 3. Set your SPOONACULAR API Key
```SPOONACULAR_API_KEY=your_spoonacular_api_key_here```

### 4. Running the App
```python main.py```

 



