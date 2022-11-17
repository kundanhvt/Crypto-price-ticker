import logging

import azure.functions as func
import os

def main(req: func.HttpRequest) -> func.HttpResponse:    
    f = open('view_index/index.html')
    logging.info('index')
    logging.info(f)
    return func.HttpResponse(f.read(), mimetype='text/html')

