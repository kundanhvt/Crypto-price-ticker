import logging

import azure.functions as func
from azure.storage.blob import BlobServiceClient
import json

def main(documents: func.DocumentList,signalRMessages: func.Out[str]) -> str:
    if documents:
        logging.info('Document id: %s', documents[0]['id'])
        html = '<table><tr> <th>Name Of Coin</th><th>Price(USD)</th></tr>'
        for data in documents[0]['data']:
            html+=f'<tr><td>{data["name"]}</td><td>{data["priceUsd"]}</td></tr>'
        html+='</table>'

        signalRMessages.set(json.dumps({
            'target': 'newMessage',
            'arguments': [html]
        }))
        logging.info('data is inserted')


