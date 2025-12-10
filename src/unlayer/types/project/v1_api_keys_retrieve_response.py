# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1APIKeysRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    active: Optional[bool] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domains: Optional[List[str]] = None

    key: Optional[str] = None

    last_used: Optional[datetime] = FieldInfo(alias="lastUsed", default=None)

    name: Optional[str] = None


class V1APIKeysRetrieveResponse(BaseModel):
    data: Optional[Data] = None
