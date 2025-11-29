import streamlit as st
import plotly.express as px
from utils.api import get_df

st.title("📝 Weather Description Frequency")

df = get_df("/weather/description")

fig = px.pie(df, names="weather_descriptions", values="occurrences",
             title="Weather Condition Frequency")

st.plotly_chart(fig, use_container_width=True)
