from google.cloud import bigquery
from dotenv import load_dotenv
import os  

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_NAME = os.getenv("DATASET_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")
key_file = "/opt/airflow/gcp/service_account.json"
client = bigquery.Client.from_service_account_json(key_file)

def create_table(PROJECT_ID, DATASET_NAME, TABLE_NAME):
    print(f"Creating {TABLE_NAME} table in dataset {DATASET_NAME} of project {PROJECT_ID}...")

    dataset_id = f"{PROJECT_ID}.{DATASET_NAME}"
    table_id = f"{dataset_id}.{TABLE_NAME}"

    table = bigquery.Table(table_id)
    table.schema =[
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
    
    try:
        if client.get_table(table_id):
            print(f"Table {TABLE_NAME} already exists in dataset {DATASET_NAME}.")
        else:
            table = client.create_table(table)
            print(f"Table {TABLE_NAME} created successfully in dataset {DATASET_NAME}.")
    except Exception as e:
        print(f"An error occurred while creating the table: {e}")
        return None
    return table