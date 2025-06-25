from models.state import UserPrefs, CaloriePlanState

def input_agent(state: CaloriePlanState) -> CaloriePlanState: 

    # ingest user preferences, and return the CaloriePlanState
    if state.prefs: 
        return state 
    prefs = UserPrefs(**state.dict())
    return CaloriePlanState(prefs = prefs)
