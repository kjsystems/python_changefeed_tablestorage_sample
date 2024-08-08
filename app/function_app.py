import os
import azure.functions as func
import datetime
import json
import logging
from azure.cosmos import CosmosClient


app = func.FunctionApp()

cosmos_client = CosmosClient.from_connection_string(os.getenv("COSMOS_CONNECTION"))

@app.route(route="add_data",
           methods=["POST"],
           auth_level=func.AuthLevel.FUNCTION)
def add_data(req: func.HttpRequest) -> func.HttpResponse:
    client = cosmos_client.get_database_client(os.getenv("COSMOS_DB_NAME"))
    container = client.get_container_client(os.getenv("COSMOS_CONTAINER_NAME"))

    items = req.get_json()

    for item in items:
        container.upsert_item(item)

    return func.HttpResponse(f"{len(items)} data uploaded.", status_code=200)


database_name = os.getenv("COSMOS_DB_NAME")
container_name = os.getenv("COSMOS_CONTAINER_NAME")


@app.cosmos_db_trigger(arg_name="items",
                    connection="COSMOS_CONNECTION",
                    database_name=database_name,
                    container_name=container_name,
                    create_lease_container_if_not_exists=True,
                    feed_poll_delay=5000,
                    lease_container_name="leases") 
def add_tablestorage(items: func.DocumentList):

    for item in items:
        logging.info('triggered. ID: %s role:%s content:%s', item["id"], item["role"], item["content"])
