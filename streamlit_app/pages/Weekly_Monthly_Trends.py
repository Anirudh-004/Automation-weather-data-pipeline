import streamlit as st
from utils.api import get_df
import plotly.express as px

st.title("📈 Weekly & Monthly Weather Trends")

weekly = get_df("/weather/average_per_week")
monthly = get_df("/weather/average_per_month")

tab1, tab2 = st.tabs(["Weekly Averages", "Monthly Averages"])

with tab1:
    fig = px.bar(
        weekly,
        x="week_start",
        y=["avg_temperature", "avg_wind_speed"],
        barmode="group",
        title="Weekly Avg Temperature & Wind Speed"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig = px.bar(
        monthly,
        x="month_start",
        y=["avg_temperature", "avg_wind_speed"],
        barmode="group",
        title="Monthly Avg Temperature & Wind Speed"
    )
    st.plotly_chart(fig, use_container_width=True)
