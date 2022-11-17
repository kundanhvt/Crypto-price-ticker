import logging

import azure.functions as func
def main(req: func.HttpRequest, connectionInfo) -> func.HttpResponse:
    logging.info(connectionInfo)
    return func.HttpResponse(connectionInfo)
