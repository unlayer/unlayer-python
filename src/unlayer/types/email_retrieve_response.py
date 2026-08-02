# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    bcc: Optional[List[str]] = None

    cc: Optional[List[str]] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    failure_reason: Optional[str] = FieldInfo(alias="failureReason", default=None)

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    status: Optional[str] = None

    subject: Optional[str] = None

    tags: Optional[Dict[str, str]] = None

    to: Optional[object] = None


class EmailRetrieveResponse(BaseModel):
    data: Data
