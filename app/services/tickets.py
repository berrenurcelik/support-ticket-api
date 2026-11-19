from app.schemas import Status, Ticket, TicketCreate
from app.store import TicketStore, store


class TicketNotFoundError(Exception):
    pass


class TicketService:
    def __init__(self, ticket_store: TicketStore) -> None:
        self._store = ticket_store

    def create_ticket(self, data: TicketCreate) -> Ticket:
        return self._store.create_ticket(data)

    def list_tickets(self, status: Status | None = None) -> list[Ticket]:
        return self._store.list_tickets(status)

    def get_ticket(self, ticket_id: int) -> Ticket:
        ticket = self._store.get_ticket(ticket_id)
        if ticket is None:
            raise TicketNotFoundError(ticket_id)
        return ticket


service = TicketService(store)
