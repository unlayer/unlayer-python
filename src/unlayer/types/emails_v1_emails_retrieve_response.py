# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailsV1EmailsRetrieveResponse"]


class EmailsV1EmailsRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """Email message ID"""

    html: Optional[str] = None
    """HTML content of the email (optional)"""

    sent_at: Optional[datetime] = FieldInfo(alias="sentAt", default=None)
    """When the email was sent"""

    status: Optional[Literal["sent", "delivered", "opened", "clicked", "bounced", "failed"]] = None
    """Current email status"""

    subject: Optional[str] = None
    """Email subject line"""

    to: Optional[str] = None
    """Recipient email address"""
