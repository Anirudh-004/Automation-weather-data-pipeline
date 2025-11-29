import streamlit as st
from utils.api import get_df
import plotly.express as px

st.title("🌡️ Temperature Patterns")

df_minmax = get_df("/weather/min_max")
df_trends = get_df("/weather/temperature_trends")

col1, col2 = st.columns(2)

with col1:
    fig = px.bar(df_minmax, x="day", y=["min_temperature", "max_temperature"],
                 title="Daily Min-Max Temperature")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(df_trends, x="weather_time_local", y="temp_change",
                  title="Consecutive Temperature Changes")
    st.plotly_chart(fig, use_container_width=True)
