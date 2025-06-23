from google.cloud import storage
from dotenv import load_dotenv
import os
import logging

load_dotenv()
key_file = "/opt/airflow/gcp/service_account.json"
client = storage.Client.from_service_account_json(key_file)

def create_bucket(bucket_name=None):
    if bucket_name is None:
        bucket_name = os.getenv("BUCKET_NAME")

    logging.info(f"Attempting to create GCS bucket: {bucket_name}")

    try:
        existing_buckets = [bucket.name for bucket in client.list_buckets()]
        if bucket_name in existing_buckets:
            logging.info(f"Bucket '{bucket_name}' already exists.")
            return client.get_bucket(bucket_name)

        bucket = client.bucket(bucket_name)
        bucket.storage_class = "STANDARD"
        new_bucket = client.create_bucket(bucket, location="US")
        logging.info(f"Bucket '{bucket_name}' created successfully in location 'US' with STANDARD storage class.")

        new_bucket.versioning_enabled = True
        new_bucket.patch()
        logging.info("Bucket versioning enabled.")

        return new_bucket

    except Exception as e:
        logging.error(f"Error creating bucket '{bucket_name}': {e}")
        return None
