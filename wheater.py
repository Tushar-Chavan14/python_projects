import weather_forecast as wf
import json

def forecast():
    w = wf.forecast(place = "gulbarga")
    r = json.dumps(w) 
    return r
