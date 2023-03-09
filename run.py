from fastapi import FastAPI, status
import requests
import os
import json
import subprocess
import uvicorn



app = FastAPI()

@app.get("/gpu")
def get_gpu():
    result = subprocess.run("gpustat --json", shell=True, stdout=subprocess.PIPE)
    gpu_info = json.loads(result.stdout)

    return gpu_info

@app.get("/status")
def get_status():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9069)
