import azure.functions as func
import azure.functions as func
from add_data import adddata_bp
from add_storage import addstorage_bp

app = func.FunctionApp()
app.register_functions(adddata_bp)
app.register_functions(addstorage_bp)

