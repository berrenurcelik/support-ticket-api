from fastapi import APIRouter, HTTPException

from app.schemas import Status, Ticket, TicketCreate
from app.services.tickets import TicketNotFoundError, service

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("", response_model=Ticket, status_code=201)
def post_ticket(data: TicketCreate):
    return service.create_ticket(data)


@router.get("", response_model=list[Ticket])
def get_tickets(status: Status | None = None):
    return service.list_tickets(status)


@router.get("/{ticket_id}", response_model=Ticket)
def get_ticket_by_id(ticket_id: int):
    try:
        return service.get_ticket(ticket_id)
    except TicketNotFoundError:
        raise HTTPException(status_code=404, detail="Ticket nicht gefunden")
