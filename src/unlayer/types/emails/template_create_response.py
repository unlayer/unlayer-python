# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TemplateCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Unique email ID (UUID).

    Use this with GET /v3/emails/:id to retrieve delivery status and events.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the email was accepted and queued for delivery (ISO-8601)."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The sender address the email was sent from."""

    status: Optional[Literal["queued", "sending", "sent", "delivered", "bounced", "complained", "failed"]] = None
    """Usually "queued" for a fresh send.

    An idempotent replay of a previously accepted request returns that email's
    current status instead. Use webhooks or GET /v3/emails/:id for live delivery
    status.
    """

    subject: Optional[str] = None
    """The resolved subject line after merge variables were applied."""

    to: Optional[List[str]] = None
    """The single accepted recipient address."""


class TemplateCreateResponse(BaseModel):
    """Email accepted and queued for delivery"""

    data: Data
