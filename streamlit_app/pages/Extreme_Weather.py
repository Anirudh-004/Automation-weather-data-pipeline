import streamlit as st
from utils.api import get_df
import plotly.express as px

st.title("🌪️ Extreme Weather Events")

df = get_df("/weather/extreme_weather")

fig = px.scatter(
    df,
    x="weather_time_local",
    y="temperature",
    size="wind_speed",
    color="temp_flag",
    title="Extreme Weather Points"
)

st.plotly_chart(fig, use_container_width=True)
