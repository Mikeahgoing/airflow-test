from airflow.decorators import dag, task
from datetime import datetime


@dag(
    dag_id="creator_metric_length_check",
    schedule="0 10 * * *",
    max_active_runs=1,
    catchup=False,
    tags=["mike"],
    start_date=datetime(2025, 12, 16),
)
def creator_metric_length_check():

    @task
    def check_length():
        print("Hello Airflow 3!")
        return "Hello Airflow 3!"

    check_length()


creator_metric_length_check_dag = creator_metric_length_check()
