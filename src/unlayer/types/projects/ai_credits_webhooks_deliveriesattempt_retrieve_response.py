# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AICreditsWebhooksDeliveriesattemptRetrieveResponse", "Attempt"]


class Attempt(BaseModel):
    attempt: Optional[float] = None

    attempted_at: Optional[datetime] = None

    error: Optional[str] = None

    status_code: Optional[float] = None


class AICreditsWebhooksDeliveriesattemptRetrieveResponse(BaseModel):
    attempts: Optional[List[Attempt]] = None

    total: Optional[float] = None
    """Total attempts for the delivery (ignores limit/offset)."""
