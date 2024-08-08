import os
import azure.functions as func
import datetime
import json
import logging
from azure.cosmos import CosmosClient

adddata_bp = func.Blueprint()

cosmos_client = CosmosClient.from_connection_string(os.getenv("COSMOS_CONNECTION"))

@adddata_bp.route(route="add_data",
                    methods=["POST"],
                    auth_level=func.AuthLevel.FUNCTION)
def add_data(req: func.HttpRequest) -> func.HttpResponse:
    client = cosmos_client.get_database_client(os.getenv("COSMOS_DB_NAME"))
    container = client.get_container_client(os.getenv("COSMOS_CONTAINER_NAME"))

    items = req.get_json()

    for item in items:
        container.upsert_item(item)

    return func.HttpResponse(f"{len(items)} data uploaded.", status_code=200)

