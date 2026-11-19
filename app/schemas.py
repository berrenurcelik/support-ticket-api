from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, field_validator


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

    @field_validator("description")
    @classmethod
    def validate_description(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Die Beschreibung darf nicht leer sein.")
        return value


class Ticket(TicketCreate):
    id: int
    status: Status
    created_at: datetime
