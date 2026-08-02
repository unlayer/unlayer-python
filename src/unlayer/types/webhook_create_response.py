# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None
    """Webhook ID"""

    active: Optional[bool] = None
    """Whether the webhook is actively receiving events"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the webhook was created"""

    events: Optional[List[Literal["email.sent", "email.delivered", "email.bounced", "email.complained"]]] = None
    """Event types this webhook is subscribed to"""

    secret: Optional[str] = None
    """Signing secret — only returned on creation.

    Store it securely; you will not be able to retrieve it again.
    """

    url: Optional[str] = None
    """The HTTPS URL receiving webhook events"""


class WebhookCreateResponse(BaseModel):
    data: Data
