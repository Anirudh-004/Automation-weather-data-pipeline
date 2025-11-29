import streamlit as st
from utils.api import get_json

st.title("🌤 Current Weather in New York")

data = get_json("/weather/latest")

col1, col2, col3 = st.columns(3)

col1.metric("Temperature (°C)", data["temperature"])
col2.metric("Wind Speed", data["wind_speed"])
col3.metric("Condition", data["weather_descriptions"])

st.info(f"Weather updated at: {data['weather_time_local']}")
