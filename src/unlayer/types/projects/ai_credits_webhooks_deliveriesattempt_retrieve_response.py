# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AICreditsWebhooksDeliveriesattemptRetrieveResponse", "Attempt"]


class Attempt(BaseModel):
    attempt: int

    attempted_at: datetime

    error: Optional[str] = None

    status_code: Optional[int] = None


class AICreditsWebhooksDeliveriesattemptRetrieveResponse(BaseModel):
    attempts: List[Attempt]

    total: int
    """Total attempts for the delivery (ignores limit/offset)."""
