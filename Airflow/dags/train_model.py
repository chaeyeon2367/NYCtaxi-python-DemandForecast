from datetime import datetime, timedelta
from airflow import models
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'chaeyeon',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 22),
    'email': ['chaeyeon2367@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
    'project_id': 'nyctaxi-demand-forecast'
}

bash_command = """
    python3 /home/airflow/gcs/data/taxi-demand-prediction/main.py --mode train --dev_env production
"""

with models.DAG(
        dag_id='Train-taxi_demand_every_week',
        description='Train taxi demand',
        schedule='1 15 * * 0',  # Korea Monday 0 1
        default_args=default_args) as dag:

    train_operator = BashOperator(
        dag=dag,
        task_id='train_demand',
        bash_command=bash_command
    )

    train_operator
