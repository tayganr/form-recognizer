import json
import requests
import logging
import azure.functions as func
from azure.storage.blob import BlockBlobService

SUPPORTED_CONTENT_TYPES = ['application/pdf', 'image/jpeg', 'image/png']

def main(req: func.HttpRequest) -> func.HttpResponse:
    # 1. Get Header Values - Azure Blob Storage
    storage_account_name = req.headers.get('storage_account_name')
    storage_account_key = req.headers.get('storage_account_key')
    container_name = req.headers.get('container_name')
    blob_name = req.headers.get('blob_name')

    # 2. Get Header Values - Form Recognizer Cognitive Service
    region = req.headers.get('region')
    model_id = req.headers.get('model_id')
    subscription_key = req.headers.get('subscription_key')
    
    # 3. Get Form from Blob Storage
    blob_service = BlockBlobService(account_name=storage_account_name, account_key=storage_account_key)
    blob = blob_service.get_blob_to_bytes(container_name, blob_name)
    data = blob.content
    content_type = blob.properties.content_settings.content_type

    if content_type in SUPPORTED_CONTENT_TYPES:

        # 4. Generate Endpoint and HTTP Header
        endpoint = 'https://{0}.api.cognitive.microsoft.com/formrecognizer/v1.0-preview/custom/models/{1}/analyze'.format(region, model_id)
        headers = {
            'Content-Type': content_type,
            'Ocp-Apim-Subscription-Key': subscription_key
        }

        # 5. Analyze Form
        response = requests.post(endpoint, headers=headers, data=data)
        logging.info(response.json())

    # 6. Return HTTP Response
    body = {
        'account_name': storage_account_name,
        'account_key': 'YOUR_SECRET_ACCOUNT_KEY' if storage_account_key else None,
        'blob_name': blob_name,
        'content_type': content_type
    }
    return func.HttpResponse(json.dumps(body),headers={'Content-Type':'application/json'})