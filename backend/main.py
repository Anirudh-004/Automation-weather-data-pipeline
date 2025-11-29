from fastapi import FastAPI
from db import get_connection

app = FastAPI()


# ----MART MODELS ENDPOINTS--------

@app.get("/weather/latest")
def latest_weather():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.weather_report
        ORDER BY weather_time_local DESC
        LIMIT 1;
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
        ORDER BY date;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]

@app.get("/weather/extreme_weather")
def extreme_weather():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.extreme_weather
        ORDER BY weather_time_local;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]


@app.get("/weather/weather_trends")
def weather_trends():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.weather_trends
        ORDER BY day;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]


@app.get("/weather/temperature_trends")
def temperature_trends():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev."Consecutive_Temperature_Trends"
        ORDER BY weather_time_local;
    """)

    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]


@app.get("/weather/weather_type")
def weather_type():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.Average_by_Weather_Type
        ORDER BY avg_temp, avg_wind_speed;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]

#-------INTERMEDIATE MODELS ENDPOINTS------
@app.get("/weather/min_max")
def weather_min_max():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.daily_min_max
        ORDER BY max_temperature;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]

@app.get("/weather/description")
def weather_descriptions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.weather_description_frequency
        ORDER BY weather_descriptions desc;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]


@app.get("/weather/average_per_week")
def weather_average_per_week():
    try:
        conn = get_connection()
        print("CONNECTED OK")  # DEBUG
        cur = conn.cursor()

        cur.execute("""
            SELECT *
            FROM dev.weekly_average
            ORDER BY avg_temperature, avg_wind_speed DESC;
        """)

        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        conn.close()
        return [dict(zip(colnames, r)) for r in rows]

    except Exception as e:
        print("🔥 BACKEND ERROR:", e)
        raise

@app.get("/weather/average_per_month")
def weather_average_per_month():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT *
        FROM dev.monthly_average
        ORDER BY avg_temperature,avg_wind_speed desc;
    """)
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    conn.close()

    return [dict(zip(colnames, r)) for r in rows]
