from pydantic import (
    BaseModel,
    ConfigDict,
)

from datetime import datetime


class BaseSm(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
