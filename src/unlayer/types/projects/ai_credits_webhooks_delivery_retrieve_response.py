# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AICreditsWebhooksDeliveryRetrieveResponse", "Delivery"]


class Delivery(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    created_at: Optional[datetime] = None

    delivered_at: Optional[str] = None

    end_user_id: Optional[str] = None

    event: Optional[str] = None

    last_status_code: Optional[float] = None

    payload: Optional[Dict[str, object]] = None

    status: Optional[Literal["pending", "delivered", "failed"]] = None


class AICreditsWebhooksDeliveryRetrieveResponse(BaseModel):
    deliveries: Optional[List[Delivery]] = None

    total: Optional[float] = None
    """Total deliveries matching the filter (ignores limit/offset)."""
