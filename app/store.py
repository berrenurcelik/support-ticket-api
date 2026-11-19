from abc import ABC, abstractmethod
from datetime import datetime

from app.schemas import Status, Ticket, TicketCreate


class TicketStore(ABC):
    @abstractmethod
    def create_ticket(self, data: TicketCreate) -> Ticket: ...

    @abstractmethod
    def list_tickets(self, status: Status | None = None) -> list[Ticket]: ...

    @abstractmethod
    def get_ticket(self, ticket_id: int) -> Ticket | None: ...


class InMemoryTicketStore(TicketStore):
    def __init__(self) -> None:
        self._tickets: dict[int, Ticket] = {}
        self._next_id = 1

    def create_ticket(self, data: TicketCreate) -> Ticket:
        ticket = Ticket(
            id=self._next_id,
            title=data.title,
            description=data.description,
            priority=data.priority,
            status=Status.open,
            created_at=datetime.now(),
        )
        self._tickets[self._next_id] = ticket
        self._next_id += 1
        return ticket

    def list_tickets(self, status: Status | None = None) -> list[Ticket]:
        tickets = list(self._tickets.values())
        if status is not None:
            tickets = [t for t in tickets if t.status == status]
        return tickets

    def get_ticket(self, ticket_id: int) -> Ticket | None:
        return self._tickets.get(ticket_id)


store: TicketStore = InMemoryTicketStore()
