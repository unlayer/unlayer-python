# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DomainUpdateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domain: Optional[str] = None

    status: Optional[str] = None

    verified: Optional[bool] = None


class DomainUpdateResponse(BaseModel):
    data: Optional[Data] = None
