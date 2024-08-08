import os
import azure.functions as func
import logging
import azure.functions as func
from azure.data.tables import TableServiceClient

addstorage_bp = func.Blueprint()

database_name = os.getenv("COSMOS_DB_NAME")
container_name = os.getenv("COSMOS_CONTAINER_NAME")

storage_connection_string = os.getenv("STORAGE_CONNECTION")
storage_tablename = os.getenv("STORAGE_TABLENAME")

@addstorage_bp.cosmos_db_trigger(arg_name="items",
                    connection="COSMOS_CONNECTION",
                    database_name=database_name,
                    container_name=container_name,
                    create_lease_container_if_not_exists=True,
                    feed_poll_delay=5000,
                    lease_container_name="leases") 
def add_tablestorage(items: func.DocumentList):

    # Azure Table Storageクライアントの初期化
    table_service_client = TableServiceClient.from_connection_string(conn_str=storage_connection_string)
    table_client = table_service_client.get_table_client(table_name=storage_tablename)

    # テーブルがなければ作成する
    try:
        table_client.create_table()
        logging.info(f"Table '{storage_tablename}' created.")
    except Exception as e:
        logging.info(f"Table '{storage_tablename}' already exists or could not be created: {e}")

    for item in items:
        logging.info('triggered. ID: %s role:%s content:%s', item["id"], item["role"], item["content"])

        # assitant の時だけ書き込み
        if item["role"] != "assistant":
            continue

        # テーブルエンティティの作成
        entity = {
            "PartitionKey": "partition1",
            "RowKey": str(item["id"]),
            "role": item["role"],
            "content": item["content"],
            "date": item["date"]
        }

        # エンティティをテーブルに追加
        table_client.upsert_entity(entity=entity)

    logging.info("All items have been written to Azure Table Storage.")
