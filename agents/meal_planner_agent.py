import os 
import requests 
import random 
from dotenv import load_dotenv
from models.state import CaloriePlanState

API_KEY = os.getenv("SPOONACULAR_API_KEY")

def fetch_meals(diet, target_calories, restrictions, count):

    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
        "apiKey": API_KEY,
        "diet": diet,
        "number": 30,
        "addRecipeInformation": True
    }

    if restrictions:
        params["intolerances"] = ",".join(restrictions)

    response = requests.get(url, params=params)

    data = response.json()
    recipes = data.get("results", [])

    return recipes  

def meal_planner_agent(state: CaloriePlanState) -> CaloriePlanState:

    days = {}
    meals_per_day = state.prefs.meals_per_day
    total_days = state.prefs.days
    per_meal_cal = state.prefs.calories_per_day

    for d in range(total_days):
        
        day_name = f"Day {d+1}"

        meal_list = fetch_meals(
            diet = state.prefs.diet,
            target_calories = per_meal_cal,
            restrictions = state.prefs.restrictions,
            count = meals_per_day
        )

        if len(meal_list) < meals_per_day:
            # use what we have
            print(f"Warning: only found {len(meal_list)} meals for Day {d+1}")
            chosen = meal_list  

        else:
            chosen = random.sample(meal_list, meals_per_day)

        meal_labels = ["Breakfast", "Lunch", "Dinner"]

        days[day_name] = {
            label: meal["title"]
            for label, meal in zip(meal_labels, chosen)
        }


    state.planned_meals = days
    return state



