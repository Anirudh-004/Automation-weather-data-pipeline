#!/bin/bash
set -e

# This script runs only during first container initialization.
# It uses env vars from the container (provided via docker-compose env_file).

psql <<-EOSQL
-- create airflow user and db (if not exists)
DO
\$do\$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '${AIRFLOW_USER}') THEN
      CREATE ROLE "${AIRFLOW_USER}" LOGIN PASSWORD '${AIRFLOW_PASSWORD}';
   END IF;
END
\$do\$;

-- create database if not exists and assign owner
SELECT
  CASE
    WHEN EXISTS(SELECT FROM pg_database WHERE datname = '${AIRFLOW_DB}') THEN
      'database exists'
    ELSE
      (CREATE DATABASE "${AIRFLOW_DB}" OWNER "${AIRFLOW_USER}")
  END;
EOSQL
