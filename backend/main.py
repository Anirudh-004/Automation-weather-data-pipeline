from fastapi import FastAPI
from db import get_connection

app = FastAPI()

@app.get("/weather/latest")
def latest_weather():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.weather_report
        ORDER BY weather_time_local DESC
        LIMIT 1
    """)
    row = cur.fetchone()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return dict(zip(colnames, row))

@app.get("/weather/daily-avg")
def daily_avg():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.daily_average
        ORDER BY date
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]
