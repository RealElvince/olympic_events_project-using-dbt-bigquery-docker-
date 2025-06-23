from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
import sys
from airflow.utils.task_group import TaskGroup
import os
from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv('PROJECT_ID')
bucket_name = os.getenv('BUCKET_NAME')
dataset_name = os.getenv('DATASET_NAME')
table_name = os.getenv('TABLE_NAME')

sys.path.append('/opt/airflow')

from bigquery_dataset.dataset import create_dataset
from bigquery_dataset.table import create_table
from buckets.gcs_bucket import create_bucket

def bucket_creation():
    create_bucket(bucket_name)

def dataset_creation():
    create_dataset(project_id,dataset_name)

def table_creation():
    create_table(project_id,dataset_name,table_name)

default_args = {
    'owner': 'realelvince',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'depends_on_past': False
}

with DAG(
    'create_gcs_bucket_bigquery_dataset_table',
    default_args=default_args,
    tags=['gcs', 'bucket', 'bigquery'],
    catchup=False,
    schedule=None
) as dag:

    with TaskGroup(
        'create_bucket_bigquery_dataset_table',
        tooltip="bucket and table creation tasks",
        ui_color="CornflowerBlue"
    ) as create_bucket_bigquery_dataset_table:

        gcs_bucket_task = PythonOperator(
            task_id='create_gcs_bucket',
            python_callable=bucket_creation
        )

        dataset_creation_task = PythonOperator(
            task_id="bigquery_dataset_creation",
            python_callable=dataset_creation
        )

        table_creation_task = PythonOperator(
            task_id='bigquery_table_creation',
            python_callable=table_creation
        )

        gcs_bucket_task >> dataset_creation_task >> table_creation_task
