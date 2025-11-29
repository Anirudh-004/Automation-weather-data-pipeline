import streamlit as st
import plotly.express as px
from utils.api import get_df

st.title("📊 Daily Average Trends")

df = get_df("/weather/daily-avg")

tab1, tab2 = st.tabs(["Temperature", "Wind Speed"])

with tab1:
    fig = px.line(
        df,
        x="date",
        y="avg_temperature",
        title="Daily Avg Temperature"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.line(
        df,
        x="date",
        y="avg_wind_speed",
        title="Daily Avg Wind Speed"
    )
    st.plotly_chart(fig, use_container_width=True)
