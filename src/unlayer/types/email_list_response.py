# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    status: Optional[str] = None

    status_updated_at: Optional[datetime] = FieldInfo(alias="statusUpdatedAt", default=None)
    """When the email entered its current status.

    For a newly queued email, this equals createdAt.
    """

    subject: Optional[str] = None

    to: Optional[object] = None


class EmailListResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether there are more results after this page"""

    next_cursor: Optional[str] = None
    """Cursor for the next page. Null if no more results."""
