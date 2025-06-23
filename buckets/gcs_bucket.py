from google.cloud import storage
import logging

key_file = "/opt/airflow/gcp/service_account.json"
client = storage.Client.from_service_account_json(key_file)

def create_bucket(bucket_name, location='US', storage_class='STANDARD'):
    logging.info(f"Attempting to create GCS bucket: {bucket_name} in location '{location}' with storage class '{storage_class}'")

    try:
        # Check if bucket already exists
        existing_buckets = [bucket.name for bucket in client.list_buckets()]
        if bucket_name in existing_buckets:
            logging.info(f"Bucket '{bucket_name}' already exists.")
            return client.get_bucket(bucket_name)

        # Create new bucket
        bucket = client.bucket(bucket_name)
        bucket.storage_class = storage_class
        new_bucket = client.create_bucket(bucket, location=location)

        # Enable versioning
        new_bucket.versioning_enabled = True
        new_bucket.patch()

        logging.info(f"Bucket '{bucket_name}' created successfully and versioning enabled.")
        return new_bucket

    except Exception as e:
        logging.error(f"An error occurred while creating the bucket: {e}")
        return None
