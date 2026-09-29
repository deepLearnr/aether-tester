from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from Aether tester"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/status")
def status():
    return {"service": "aether-tester", "status": "running"}
