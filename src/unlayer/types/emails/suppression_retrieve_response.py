# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SuppressionRetrieveResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email: Optional[str] = None

    reason: Optional[Literal["hard_bounce", "complaint", "manual", "unsubscribe"]] = None


class SuppressionRetrieveResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
