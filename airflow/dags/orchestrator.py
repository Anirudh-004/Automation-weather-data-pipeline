from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator
import sys
from docker.types import Mount

sys.path.append("/opt/airflow/api_request")
from insert_records import main


default_args = {
    'description': "A DAG to orchestrate data",
    'start_date': datetime(2025, 11, 8),
    'catchup': False,
}

dag = DAG(
    dag_id="weather-api-dbt-orchestrator",
    default_args=default_args,
    #schedule=timedelta(minutes=1)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=main,
    )

    task2 = DockerOperator(
        task_id='transform_data_task',
        image='ghcr.io/dbt-labs/dbt-postgres:1.9.latest',
        command='run',
        working_dir='/usr/app',
        mounts=[
            Mount(source='/root/repos/weather_data_project/.dbt/weather_analytics',
                  target='/usr/app',
                  type='bind'),
            Mount(source='/root/repos/weather_data_project/.dbt',
                  target='/root/.dbt',
                  type='bind'),
        ],
        network_mode='weather_data_project_my-network',
        docker_url='unix://var/run/docker.sock',
        auto_remove='success'
    )

    task1 >> task2