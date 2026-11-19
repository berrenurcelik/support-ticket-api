from fastapi import FastAPI, HTTPException

from app.schemas import Status, Ticket, TicketCreate
from app.store import create_ticket, get_ticket, list_tickets

app = FastAPI(title="Support Ticket API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/tickets", response_model=Ticket, status_code=201)
def post_ticket(data: TicketCreate):
    return create_ticket(data)


@app.get("/tickets", response_model=list[Ticket])
def get_tickets(status: Status | None = None):
    return list_tickets(status)


@app.get("/tickets/{ticket_id}", response_model=Ticket)
def get_ticket_by_id(ticket_id: int):
    ticket = get_ticket(ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket nicht gefunden")
    return ticket
