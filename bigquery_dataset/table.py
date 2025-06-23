from google.cloud import bigquery
import logging
from google.api_core.exceptions import NotFound

# Initialize BigQuery client
key_file = "/opt/airflow/gcp/service_account.json"
client = bigquery.Client.from_service_account_json(key_file)

def create_table(project_id, dataset_name, table_name):
    logging.info(f"Creating table '{table_name}' in dataset '{dataset_name}' under project '{project_id}'...")

    dataset_id = f"{project_id}.{dataset_name}"
    table_id = f"{dataset_id}.{table_name}"

    # Define the schema
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
        # Check if the table already exists
        client.get_table(table_id)
        logging.info(f"Table '{table_name}' already exists in dataset '{dataset_name}'.")
        return f"Table '{table_name}' already exists."
    except NotFound:
        try:
            client.create_table(table)
            logging.info(f"Table '{table_name}' created successfully in dataset '{dataset_name}'.")
            return f"Table '{table_name}' created successfully."
        except Exception as e:
            logging.error(f"Error creating table '{table_name}': {e}")
            return f"Error creating table '{table_name}': {str(e)}"


