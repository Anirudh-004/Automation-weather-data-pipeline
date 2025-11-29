import streamlit as st


st.title("🏠 Welcome to the New York Weather Intelligence Dashboard")

st.write("""
    This platform provides real-time & historical analytics on **New York’s weather**,  
    powered by:

    - **Apache Airflow** for automated data ingestion  
    - **dbt Core** for transformations  
    - **Postgres** as the warehouse  
    - **FastAPI** for backend API  
    - **Streamlit** for this interactive UI  

    Use the menu on the left to explore:

    📊 Daily averages  
    📈 Weekly & monthly trends  
    🌡️ Temperature patterns  
    🌪️ Extreme weather  
    📝 Weather condition frequency  
    """)

st.success("Select a page from the left sidebar to begin exploring the insights!")