from fastapi import FastAPI

app = FastAPI(title="Support Ticket API")


@app.get("/health")
def health():
    return {"status": "ok"}
