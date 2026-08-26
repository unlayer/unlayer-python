# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SuppressionCreateResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email: Optional[str] = None

    reason: Optional[str] = None


class SuppressionCreateResponse(BaseModel):
    data: Data
