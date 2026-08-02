# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailListParams"]


class EmailListParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from previous response"""

    from_: Annotated[Union[str, date], PropertyInfo(alias="from", format="iso8601")]
    """Start date (ISO date).

    Bounds acceptance time normally, or status transition time when status is
    supplied.
    """

    limit: int
    """Number of emails to return (1-100)"""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project ID (auto-resolved for API key auth)"""

    search: str
    """Search recipient addresses and subjects by case-sensitive substring"""

    status: Literal["queued", "sending", "sent", "delivered", "bounced", "complained", "failed"]
    """Filter by email delivery status"""

    tag: str
    """Filter by tag in "key=value" format (e.g. "campaign=welcome")"""

    to: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """End date (ISO date).

    Bounds acceptance time normally, or status transition time when status is
    supplied.
    """
