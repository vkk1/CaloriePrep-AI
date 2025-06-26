import os 
import requests 
from dotenv import load_dotenv 
from models.state import CaloriePlanState

API_KEY = os.getenv("SPOONACULAR_API_KEY")

def search_recipe_id(title):

    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
        "apiKey": API_KEY,
        "query": title, 
        "number": 1
    }

    response = requests.get(url, params = params).json()
    results = response.get("results", [])

    if results:
        return results[0]["id"]
    return None

def fetch_recipe_details(recipe_id):

    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"

    params = {
        "apiKey": API_KEY, 
        "includeNutrition": "true"
    }

    response = requests.get(url, params = params).json()

    return {
        "title": response.get("title"),
        "calories": response.get("nutrition", {}).get("nutrients", [{}])[0].get("amount", 0),
        "ingredients": [i["original"] for i in response.get("extendedIngredients", [])],
        "instructions": [step["step"] for section in response.get("analyzedInstructions", []) for step in section.get("steps", [])]
    }

def recipe_agent(state: CaloriePlanState) -> CaloriePlanState:
    
    all_meals = set()

    for day_meals in state.planned_meals.values(): 
        all_meals.update(day_meals.values())

    for title in all_meals: 
        recipe_id = search_recipe_id(title)

        if recipe_id: 
            print(f"Fetching recipe for {title}")
            state.meal_details[title] = fetch_recipe_details(recipe_id)
        else: 
            print(f"Could not find recipe for {title}")
            state.meal_details[title] = {
                "ingredients": ["Unavailable"], 
                "instructions": ["Unavailable"], 
                "calories": 0
            }
    return state 