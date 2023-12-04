from enum import Enum

from pydantic import BaseModel, Field


class Status(str, Enum):
    OK = "ok"

class GetHealthResponse(BaseModel):
    status: Status = Field(Status.OK)
