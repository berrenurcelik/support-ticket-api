from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class Status(StrEnum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


class Priority(StrEnum):
    low = "low"
    medium = "medium"
    high = "high"


class TicketCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    description: str
    priority: Priority = Priority.medium


class Ticket(TicketCreate):
    id: int
    status: Status
    created_at: datetime
