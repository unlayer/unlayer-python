# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AICreditsWebhooksDeliveryRetrieveResponse", "Delivery"]


class Delivery(BaseModel):
    id: str

    attempts: int

    created_at: datetime

    delivered_at: Optional[datetime] = None

    end_user_id: Optional[str] = None

    event: Literal["ai.credits.usage_recorded", "ai.credits.threshold_reached", "ai.credits.exhausted"]

    last_status_code: Optional[int] = None

    payload: Dict[str, object]

    status: Literal["pending", "delivered", "failed"]


class AICreditsWebhooksDeliveryRetrieveResponse(BaseModel):
    deliveries: List[Delivery]

    total: int
    """Total deliveries matching the filter (ignores limit/offset)."""
