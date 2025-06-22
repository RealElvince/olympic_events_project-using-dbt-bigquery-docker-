from google.cloud import bigquery
from dotenv import load_dotenv
import os

load_dotenv()
key_file = "/gcp/service_account.json"
client = bigquery.Client.from_service_account_json(key_file)

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_NAME = os.getenv("DATASET_NAME")

def create_dataset(PROJECT_ID, DATASET_NAME,location="US"):
    print(f"Creating BigQuery dataset {DATASET_NAME} in project {PROJECT_ID}..")
    
    dataset_id = f"{PROJECT_ID}.{DATASET_NAME}"
    dataset = bigquery.Dataset(dataset_id)

    try:
        
        if dataset.exists():
            print(f"Dataset {DATASET_NAME} already exists.")
        else:
            dataset = client.create_dataset(dataset, location=location)
            print(f"ataset {DATASET_NAME} created successfully in project {PROJECT_ID}.")
    except Exception as e:
        print(f"An error occurred while creating the dataset: {e}")
        return None
    return dataset
