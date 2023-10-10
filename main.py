"""
simple web app listing its environment variables
"""
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

envars={}

@app.get("/", response_class=JSONResponse)
def list_env_vars(request: Request):
    for k, v in os.environ.items():
        envars.update({k:v})
    return envars