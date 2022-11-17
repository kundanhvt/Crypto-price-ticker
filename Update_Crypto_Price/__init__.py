import logging

import azure.functions as func
import requests
from azure.cosmos import CosmosClient, PartitionKey
from datetime import datetime

def get_crypto_response():
    headers = {
        "authorization":"Apikey 5d567721-911e-40c2-a460-842351ec88c5"
    }
    return requests.get(url="https://api.coincap.io/v2/assets")
    

def upload_into_cosmos_db(data):
    client = CosmosClient(url="https://cosmosdb-crypto-poc.documents.azure.com:443/", credential="w6npRvwlvCpSKBXubCaJlyyoHxXMrZmtOqfiUz8GvEw5iDRJfI7VVFTZP85wpFyVl0ZnSzkVWC72ACDboH6ylA==")
    database = client.create_database_if_not_exists(id="crypto-details")
    partitionKeyPath = PartitionKey(path="/id")
    container = database.create_container_if_not_exists(id="crypto",partition_key=partitionKeyPath)
    data["id"]=str(datetime.now().timestamp())
    container.create_item(data)

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.now()

    response = get_crypto_response()
    if response.status_code == 200:
        upload_into_cosmos_db(response.json())

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
