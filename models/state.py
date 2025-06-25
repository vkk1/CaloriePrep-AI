from pydantic import BaseModel 
from typing import List, Dict

class UserPrefs(BaseModel):
    calories_per_day: int
    meals_per_day: int 
    days: int 
    diet: str 
    restrictions: List[str] = []


class CaloriePlanState(BaseModel):
    prefs: UserPrefs = None 
    planned_meals: Dict[str, dict[str, str]] = {}
    meal_details: Dict[str, List[str]] = {}
    final_markdown: str = ""