from fastapi import FastAPI
from core.loop import run_loop

app = FastAPI()

@app.get("/")
def root():
    return {"status": "F0 system running"}

@app.post("/run")
def run(data: dict):
    if "message" not in data:
        return {"ok": False, "error": "missing message"}
    return run_loop(data)