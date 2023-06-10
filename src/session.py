import pandas as pd
import numpy as np

class Session():
    def __init__(self, df, date, driver, car, track, name, lap, time, lon, lat):
        self.date = date
        self.driver = driver
        self.car = car
        self.track = track
        self.name = name
        self.notes = ""
        
        self.lap_idx = lap
        self.time_idx = time
        self.gps_lon_idx = lon
        self.gps_lat_idx = lat

        self.data: pd.DataFrame = df
    
    def get_lap_code(lapno) -> str:
        pass
