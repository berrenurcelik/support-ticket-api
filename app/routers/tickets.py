from fastapi import APIRouter, HTTPException

from app.schemas import Status, Ticket, TicketCreate
from app.store import store

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("", response_model=Ticket, status_code=201)
def post_ticket(data: TicketCreate):
    return store.create_ticket(data)


@router.get("", response_model=list[Ticket])
def get_tickets(status: Status | None = None):
    return store.list_tickets(status)


@router.get("/{ticket_id}", response_model=Ticket)
def get_ticket_by_id(ticket_id: int):
    ticket = store.get_ticket(ticket_id)
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket nicht gefunden")
    return ticket
