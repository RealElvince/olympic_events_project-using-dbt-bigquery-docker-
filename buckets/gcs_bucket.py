from google.cloud import storage
from dotenv import load_dotenv
import os

load_dotenv()
key_file = "/gcp/service_account.json"

client = storage.Client.from_service_account_json(key_file)

BUCKET_NAME = os.getenv("BUCKET_NAME")

def create_bucket(BUCKET_NAME):
    print(f"Creating gcs bucket {BUCKET_NAME}..")
   
    bucket = client.bucket(BUCKET_NAME)

    try:
        if not bucket.exists():
            bucket = client.create_bucket(BUCKET_NAME,location="US",storage_class="STANDARD",versioning=True)
            print(f"Bucket {BUCKET_NAME} created successfully.")
        else:
            print(f"Bucket {BUCKET_NAME} already exists.")
    except Exception as e:
        print(f"An error occurred while creating the bucket: {e}")
        return None
    return bucket