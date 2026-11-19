from datetime import datetime

from pydantic import BaseModel, Field


class TicketCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str


class Ticket(TicketCreate):
    id: int
    status: str
    created_at: datetime
