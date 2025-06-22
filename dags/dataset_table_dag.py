from airflow import  DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
import sys

default_args ={
    'owner': 'realelvince',
    'start_date': datetime(2024, 1, 1),
    'retries':1,
    'retray_delay':timedelta(minutes=5),
    'depends_on_past':False
}