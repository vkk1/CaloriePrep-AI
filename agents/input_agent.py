from models.state import UserPrefs, CaloriePlanState

def input_agent(input_data: dict) -> CaloriePlanState: 

    # ingest user preferences, and return the CaloriePlanState
    prefs = UserPrefs(**input_data)
    return CaloriePlanState(prefs = prefs)
