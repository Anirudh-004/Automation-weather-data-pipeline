import requests
import pandas as pd

API_BASE = "http://localhost:8000"

def get_json(endpoint):
    r = requests.get(f"{API_BASE}{endpoint}")
    r.raise_for_status()
    return r.json()

def get_df(endpoint):
    return pd.DataFrame(get_json(endpoint))
