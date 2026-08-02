# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainListResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domain: Optional[str] = None

    status: Optional[Literal["pending", "verified", "failed"]] = None


class DomainListResponse(BaseModel):
    data: List[Data]
