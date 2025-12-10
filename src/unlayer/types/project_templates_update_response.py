# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectTemplatesUpdateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    body: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    subject: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class ProjectTemplatesUpdateResponse(BaseModel):
    data: Optional[Data] = None
