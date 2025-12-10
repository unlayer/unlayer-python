# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["V1CurrentListResponse", "Data", "DataWorkspace"]


class DataWorkspace(BaseModel):
    id: Optional[float] = None

    name: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    status: Optional[str] = None

    workspace: Optional[DataWorkspace] = None


class V1CurrentListResponse(BaseModel):
    data: Optional[Data] = None
