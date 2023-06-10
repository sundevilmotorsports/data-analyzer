from session import Session
import pandas as pd
active_sessions = []

# add a session to the workspace
def add_session(df, time, lap, lat, lon, name, date, driver, car, track):
    new_session = Session(df, date, driver, car, track, name, lap, time, lon, lat)
    active_sessions.append(new_session)

# get all laps of all active sessions
def get_laps():
    laps = []

    for session in active_sessions:
        pass
    
    return laps

# get a session's lap's data
def get_lap(lap_code: str) -> pd.DataFrame:
    pass