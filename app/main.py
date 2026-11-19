from fastapi import FastAPI

from app.routers import tickets

app = FastAPI(title="Support Ticket API")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(tickets.router)
