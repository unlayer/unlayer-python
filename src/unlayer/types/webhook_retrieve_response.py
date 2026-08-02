# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None
    """Webhook ID"""

    active: Optional[bool] = None
    """Whether the webhook is actively receiving events"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the webhook was created"""

    events: Optional[List[Literal["email.sent", "email.delivered", "email.bounced", "email.complained"]]] = None
    """Event types this webhook is subscribed to"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the webhook was last updated"""

    url: Optional[str] = None
    """The HTTPS URL receiving webhook events"""


class WebhookRetrieveResponse(BaseModel):
    data: Data
