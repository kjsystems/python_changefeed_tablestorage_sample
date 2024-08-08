import os
import azure.functions as func
import logging
import azure.functions as func

addstorage_bp = func.Blueprint()

database_name = os.getenv("COSMOS_DB_NAME")
container_name = os.getenv("COSMOS_CONTAINER_NAME")

@addstorage_bp.cosmos_db_trigger(arg_name="items",
                    connection="COSMOS_CONNECTION",
                    database_name=database_name,
                    container_name=container_name,
                    create_lease_container_if_not_exists=True,
                    feed_poll_delay=5000,
                    lease_container_name="leases") 
def add_tablestorage(items: func.DocumentList):

    for item in items:
        logging.info('triggered. ID: %s role:%s content:%s', item["id"], item["role"], item["content"])
