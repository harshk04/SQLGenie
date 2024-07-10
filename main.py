from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import importlib

app = FastAPI()

# Define Pydantic models for request bodies
class ConnectionDetails(BaseModel):
    host: str
    dbname: str
    user: str
    password: str
    port: int

class ModelSelection(BaseModel):
    model_name: str

class ExtraInfo(BaseModel):
    extra_info: str

# Initialize session state for model if not already set
session_state = {"model": "llama3"}

# Function to reload the module based on model choice
def reload_module(model_name):
    if model_name == "llama3":
        return importlib.import_module("llama3")
    elif model_name == "openai":
        return importlib.import_module("model")
    elif model_name == "sqlcoder":
        return importlib.import_module("sqlcoder")
    else:
        raise HTTPException(status_code=400, detail="Invalid model name")

current_module = reload_module(session_state["model"])

# Endpoint for connection details
@app.post("/set-connection-details/")
def set_connection_details(details: ConnectionDetails):
    print(details)
    return {"message": "Connection details received"}

# Endpoint for model selection (POST)
@app.post("/set-model/")
def set_model(selection: ModelSelection):
    model_name = selection.model_name.lower()
    if model_name != session_state["model"]:
        session_state["model"] = model_name
        global current_module
        current_module = reload_module(session_state["model"])
    return {"message": f"Model changed to {model_name}"}

# Endpoint for extra information
@app.post("/set-extra-info/")
def set_extra_info(info: ExtraInfo):
    print(info)
    return {"message": "Extra information received"}

# GET endpoint to change model via query parameter
@app.get("/")
def change_model(
    host: str,
    dbname: str,
    user: str,
    password: str,
    port: int,
    extra_info: str,
    model_name: str = Query(default="llama3")
):
    model_name = model_name.lower()
    if model_name != session_state["model"]:
        session_state["model"] = model_name
        global current_module
        current_module = reload_module(session_state["model"])

    # Here you can use the connection details and extra info as needed
    connection_details = {
        "host": host,
        "dbname": dbname,
        "user": user,
        "password": password,
        "port": port
    }
    print(connection_details)
    print(extra_info)

    return {
        "message": f"Model changed to {model_name}",
        "connection_details": connection_details,
        "extra_info": extra_info
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
