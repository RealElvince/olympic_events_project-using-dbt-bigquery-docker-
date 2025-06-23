from google.cloud import bigquery
import logging
from google.api_core.exceptions import NotFound

key_file = "/opt/airflow/gcp/service_account.json"
client = bigquery.Client.from_service_account_json(key_file)

def create_dataset(project_id, dataset_name, location="US"):
    dataset_id = f"{project_id}.{dataset_name}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = location

    logging.info(f"Creating BigQuery dataset '{dataset_name}' in project '{project_id}'...")

    try:
        client.get_dataset(dataset_id)
        logging.info(f"Dataset '{dataset_name}' already exists.")
        return None
    except NotFound:
        try:
            created_dataset = client.create_dataset(dataset)
            logging.info(f"Dataset '{dataset_name}' created successfully.")
            return created_dataset
        except Exception as e:
            logging.error(f"Error creating dataset: {e}")
            return None
