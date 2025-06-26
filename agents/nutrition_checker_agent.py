from models.state import CaloriePlanState

def nutrition_checker_agent(state: CaloriePlanState) -> CaloriePlanState: 

    per_meal_target = state.prefs.calories_per_day // state.prefs.meals_per_day
    tolerance = 0.25 

    for meal_name, details in state.meal_details.items(): 
        
        cal = details.get("calories", 0)

        if not cal: 
            details["nutrition check"] = "No calories available"
            state.meal_details[meal_name] = details
            continue
        
        lower_bound = per_meal_target * (1 - tolerance)
        upper_bound = per_meal_target * (1 + tolerance)

        if lower_bound <= cal <= upper_bound: 
            details["nutrition_check"] = f"Within range ({cal} kCal)."

        elif cal < lower_bound: 
            details["nutrition_check"] = f"Too low ({cal} kCal). Consider adding something."
            
        else: 
            details["nutrition_check"] = f"Too high ({cal} kCal). Consider substituting."
        
        state.meal_details[meal_name] = details  
    
    return state 
