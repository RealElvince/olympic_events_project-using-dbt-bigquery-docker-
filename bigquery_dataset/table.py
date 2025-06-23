from google.cloud import bigquery
from dotenv import load_dotenv
import os
import logging
from google.api_core.exceptions import NotFound

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_NAME = os.getenv("DATASET_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")
KEY_FILE = "/opt/airflow/gcp/service_account.json"

client = bigquery.Client.from_service_account_json(KEY_FILE)

def create_table(project_id=None, dataset_name=None, table_name=None):
    project_id = project_id or os.getenv("PROJECT_ID")
    dataset_name = dataset_name or os.getenv("DATASET_NAME")
    table_name = table_name or os.getenv("TABLE_NAME")

    dataset_id = f"{project_id}.{dataset_name}"
    table_id = f"{dataset_id}.{table_name}"

    logging.info(f"Creating table '{table_name}' in dataset '{dataset_name}' under project '{project_id}'...")

    schema = [
        bigquery.SchemaField("ID", "INTEGER", mode="REQUIRED"),
        bigquery.SchemaField("Name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Sex", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Age", "INTEGER", mode="REQUIRED"),
        bigquery.SchemaField("Height", "FLOAT", mode="REQUIRED"),
        bigquery.SchemaField("Weight", "FLOAT", mode="REQUIRED"),
        bigquery.SchemaField("Team", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("NOC", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Games", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Year", "INTEGER", mode="REQUIRED"),
        bigquery.SchemaField("Season", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("City", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Sport", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Event", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("Medal", "STRING", mode="NULLABLE"),
    ]

    table = bigquery.Table(table_id, schema=schema)

    try:
        # Check if table already exists
        client.get_table(table_id)
        logging.info(f"Table '{table_name}' already exists in dataset '{dataset_name}'.")
        return None
    except NotFound:
        # Table does not exist, proceed to create
        try:
            created_table = client.create_table(table)
            logging.info(f"Table '{table_name}' created successfully.")
            return created_table
        except Exception as e:
            logging.error(f"An error occurred while creating the table: {e}")
            return None
