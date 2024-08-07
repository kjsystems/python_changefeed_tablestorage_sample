import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="add_data", auth_level=func.AuthLevel.FUNCTION)
def add_data(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


@app.cosmos_db_trigger(arg_name="azcosmosdb", container_name="chat",
                        database_name="aoai", connection="CosmosDbConnectionString") 
def add_tablestorage(azcosmosdb: func.DocumentList):
    logging.info('Python CosmosDB triggered.')
