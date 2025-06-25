from langgraph.graph import StateGraph
from agents.input_agent import input_agent
from models.state import CaloriePlanState

# minimal langgraph test 
graph = StateGraph(CaloriePlanState)
graph.add_node("input", input_agent)
graph.set_entry_point("input")
builder = graph.compile()

if __name__ == "__main__":
    sample_input = {
        "calories_per_day": 1800, 
        "meals_per_day": 3, 
        "days": 2, 
        "diet": "vegetarian", 
        "restrictions": ["no mushrooms"]
    }

    result = builder.invoke(sample_input)
    print(result)