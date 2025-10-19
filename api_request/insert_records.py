from api_request import mock_fetch_data
import psycopg2
from dotenv import load_dotenv
from psycopg2 import Error
import os


load_dotenv()

def connect_to_postgres():
    print('CConnecting to Postgres DB....')
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5000,
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD")
        )
        return conn
    except Error as e:
        print(f"Database connection failed: {e}")
        raise
    return conn

def create_table(conn):
    print("Creating a table if not exists....")
    try:
        cursor = conn.cursor()
        cursor.execute("""
        create schema if not exists dev;
        create table if not exists dev.raw_weather_data (
        id SERIAL PRIMARY KEY,
        city TEXT,
        temperature FLOAT,
        weather_Descriptions TEXT,
        wind_speed FLOAT,
        time TIMESTAMP,
        inserted_at TIMESTAMP DEFAULT NOW(),
        utc_offset TEXT
        );
        """)
        conn.commit()
        print("Table was created....")
    except Error as e:
        print(f"Failed to create the table: {e}")
        raise

def insert_records(conn, data):
    print("Inserting weather data into the database....")
    weather = data['current']
    location = data['location']
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO dev.raw_weather_data (
            city,
            temperature,
            weather_Descriptions,
            wind_speed,
            time,
            inserted_at,
            utc_offset
        ) VALUES(%s, %s, %s, %s, %s, NOW(), %s)
        """,(
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print("Data successfully inserted")
    except Error as e:
        print(f"Failed to insert the data: {e}")
        raise


def main():
    try:
        result = mock_fetch_data()
        conn = connect_to_postgres()
        create_table(conn)
        insert_records(conn, result)
    
if __name__ == "__main__":
    main()