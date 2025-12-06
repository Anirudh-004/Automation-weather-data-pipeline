Weather Data Engineering & Analytics Platform

A complete end-to-end data pipeline with Airflow → Postgres → dbt → FastAPI → Streamlit Dashboard

📌 Overview

This project is a fully containerized modern data platform that ingests real-time weather data for New York, transforms it using dbt, orchestrates workflows using Apache Airflow, exposes backend APIs with FastAPI, and visualizes insights using a Streamlit analytics dashboard.

The architecture is designed for modularity, scalability, and ease of deployment.

🧩 Components
Component	Purpose
Airflow	Schedules data ingestion & dbt transformation jobs
Postgres	Central data warehouse using dev schema
dbt	SQL modeling (staging → intermediate → mart)
FastAPI	Serves weather insights through REST APIs
Streamlit	Frontend UI dashboard
Docker Compose	Manages and networks all services

🗄 Data Flow Summary
1️⃣ Ingestion (Airflow → Postgres raw table)

Orchestrator: Apache Airflow

Source: External real-time Weather API (New York)

Frequency: Every X minutes (configurable in Airflow DAG)

Target table:
dev.raw_weather_data

Columns include (not exhaustive):

id

city

temperature

wind_speed

weather_descriptions

weather_time_local

inserted_at_local

2️⃣ dbt Transformation

dbt converts raw data → clean models → analytics-ready marts, all in the dev schema.

🔹 Staging Layer

Example model:

staging.sql

Responsibilities:

Standardize column names

Enforce data types

Remove duplicates

Basic cleansing and deduplication

🔹 Intermediate Layer

Example models:

average_per_day.sql

daily_min_max.sql

weekly_average.sql

monthly_average.sql

weather_description_frequency.sql

Responsibilities:

Compute reusable aggregations

Prepare metrics at daily/weekly/monthly grain

Summarize descriptive statistics

🔹 Mart Layer

Final business-facing models powering the API & dashboard:

weather_report.sql

daily_average.sql

weather_trends.sql

Average_by_weather_type.sql

extreme_weather.sql

Consecutive_Temperature_Trends.sql

All materialized into tables/views under:

dev.*

🧩 Backend – FastAPI

The FastAPI service exposes REST endpoints that read from Postgres (dbt models) using psycopg2.

Endpoints

✔ Latest weather
GET /weather/latest

✔ Daily averages
GET /weather/daily-avg

✔ Trend analytics
GET /weather/trends

Data Access

Direct connection to Postgres

Uses psycopg2 for querying dbt models in the dev schema

Designed to be consumed by both Streamlit and external clients

🎨 Frontend – Streamlit Dashboard

A multi-page Streamlit app that visualizes the weather insights served by FastAPI.

📌 Pages

Home – Landing page with animation and overview

Daily Average Trends – Daily aggregated metrics and charts

Weather Trends & Extreme Events – Patterns and extreme weather analysis

Wind Speed & Temperature Patterns – Co-movement and correlations

UI Features

Lottie animation intro

Sidebar navigation

Plotly charts (interactive)

Metric cards for key KPIs

Clean light UI theme

Backend Communication

The Streamlit app makes HTTP requests to the FastAPI service for data.

API_BASE_URL is configurable for local vs Dockerized runs.

🐳 Docker Compose Setup

All core services run inside Docker (Streamlit can optionally run locally).

Services

postgres

airflow-webserver

airflow-scheduler

dbt (via DockerOperator in Airflow or a dedicated container)

fastapi

(optional) streamlit

Networking

FastAPI → Postgres:
host = "db" (service name in Docker network)

Streamlit → FastAPI:
API_BASE_URL = "http://fastapi:8000" (inside Docker network)
or http://localhost:8000 when Streamlit runs on the host.

🚀 Run the Entire System

From the project root (weather_data_project/):

docker-compose up --build

Access the services
Service	URL
Airflow UI	http://localhost:8080
FastAPI Docs (Swagger)	http://localhost:8000/docs
Streamlit App	http://localhost:8501
Postgres	Port 5432 (mapped from container)

🧪 Local Development Notes
Streamlit (local) → FastAPI (container)

In Streamlit config or code:

API_BASE_URL = "http://localhost:8000"

FastAPI (container) → Postgres (container)

Since both run inside the same Docker network, configure:

host = "db"


(Where db is the Postgres service name in docker-compose.yml.)

📦 Requirements
On Host

Docker + Docker Compose

Python 3.9+ (if running services like Streamlit or FastAPI locally outside Docker)

Python Packages (core)

streamlit

requests

pandas

plotly

psycopg2

fastapi

uvicorn

(These are typically specified in the relevant requirements.txt files for each service.)

✨ Features & Highlights

End-to-end real-time weather data pipeline

Automated orchestration using Apache Airflow

Modular, layered dbt modeling (staging → intermediate → mart)

REST API layer for both internal and external consumers

Fully containerized system managed with Docker Compose

Modern Streamlit UI dashboard with animations and interactive charts

Clean, simple, and extendable architecture suitable for production hardening and feature expansion