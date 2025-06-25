import os, sys
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gradio as gr
from langgraph.graph import StateGraph
from agents.input_agent import input_agent
from agents.meal_planner_agent import meal_planner_agent
from agents.recipe_agent import recipe_agent
from agents.nutrition_checker_agent import nutrition_checker_agent
from agents.formatter_agent import formatter_agent
from models.state import CaloriePlanState, UserPrefs  

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

def generate_plan(calories, meals, days, diet, restrictions_text):

    prefs = UserPrefs(
        calories_per_day=int(calories),
        meals_per_day=int(meals),
        days=int(days),
        diet=diet.strip(),
        restrictions=[r.strip() for r in restrictions_text.split(",") if r.strip()],
    )

    initial_state = CaloriePlanState(prefs=prefs)

    result = builder.invoke(initial_state)
    return result["final_markdown"]


demo = gr.Interface(
    fn=generate_plan,
    inputs=[
        gr.Number(label="Calories per day", value=1800),
        gr.Number(label="Meals per day", value=3),
        gr.Number(label="Days", value=3),
        gr.Textbox(label="Diet (e.g. vegetarian)", value="vegetarian"),
        gr.Textbox(label="Restrictions (comma-separated)", placeholder="no mushrooms, no peanuts")
    ],
    outputs=gr.Markdown(label = "Meal Plan"),
    title="CaloriePrep AI",
    description="Generate a custom meal plan with recipes and calories."
)

if __name__ == "__main__":
    demo.launch()
