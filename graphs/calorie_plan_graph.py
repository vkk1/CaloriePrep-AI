import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langgraph.graph import StateGraph
from agents.input_agent import input_agent
from models.state import CaloriePlanState
from models.state import UserPrefs
from agents.recipe_agent import recipe_agent
from agents.meal_planner_agent import meal_planner_agent
from agents.nutrition_checker_agent import nutrition_checker_agent
from agents.formatter_agent import formatter_agent

graph = StateGraph(CaloriePlanState)

graph.add_node("input", input_agent)
graph.add_node("planner", meal_planner_agent)
graph.add_node("recipes", recipe_agent)
graph.add_node("checker", nutrition_checker_agent)
graph.add_node("formatter", formatter_agent)

graph.set_entry_point("input")
graph.add_edge("input", "planner")
graph.add_edge("planner", "recipes")
graph.add_edge("recipes", "checker")
graph.add_edge("checker", "formatter")

builder = graph.compile()

if __name__ == "__main__":
    sample_input = {
        "calories_per_day": 1800, 
        "meals_per_day": 3, 
        "days": 2, 
        "diet": "vegetarian", 
        "restrictions": []
    }

    prefs = UserPrefs(**sample_input)
    initial_state = CaloriePlanState(prefs=prefs)
    result = builder.invoke(initial_state)   
    print(result)
