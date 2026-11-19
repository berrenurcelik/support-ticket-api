from datetime import datetime

from app.schemas import Status, Ticket, TicketCreate

_tickets: dict[int, Ticket] = {}
_next_id = 1


def create_ticket(data: TicketCreate) -> Ticket:
    global _next_id
    ticket = Ticket(
        id=_next_id,
        title=data.title,
        description=data.description,
        priority=data.priority,
        status=Status.open,
        created_at=datetime.now(),
    )
    _tickets[_next_id] = ticket
    _next_id += 1
    return ticket


def list_tickets() -> list[Ticket]:
    return list(_tickets.values())


def get_ticket(ticket_id: int) -> Ticket | None:
    return _tickets.get(ticket_id)
