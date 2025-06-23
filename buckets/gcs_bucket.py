from google.cloud import storage
import logging

# Authenticate using service account key
key_file = "/opt/airflow/gcp/service_account.json"
client = storage.Client.from_service_account_json(key_file)


def create_bucket(bucket_name, location='US', storage_class='STANDARD'):
    logging.info(f"Attempting to create GCS bucket: {bucket_name} in location '{location}' with storage class '{storage_class}'")

    try:
        existing_buckets = [bucket.name for bucket in client.list_buckets()]
        if bucket_name in existing_buckets:
            logging.info(f"Bucket '{bucket_name}' already exists.")
            return f"Bucket {bucket_name} already exists."  
        else:
            bucket = client.bucket(bucket_name)
            bucket.storage_class = storage_class
            new_bucket = client.create_bucket(bucket, location=location)
            new_bucket.versioning_enabled = True
            new_bucket.patch()

            logging.info(f"Bucket '{bucket_name}' created successfully.")
            return f"Bucket {bucket_name} created."  
    except Exception as e:
        logging.error(f"An error occurred while creating the bucket: {e}")
        return f"Error creating bucket: {str(e)}"  
