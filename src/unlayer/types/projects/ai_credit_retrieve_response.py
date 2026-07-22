# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AICreditRetrieveResponse"]


class AICreditRetrieveResponse(BaseModel):
    credits_remaining: Optional[float] = None
    """AI credits remaining in the current period."""

    credits_total: Optional[float] = None
    """Total AI credits available for the current period."""

    credits_used: Optional[float] = None
    """AI credits consumed so far in the current period."""

    reset_date: Optional[datetime] = None
    """
    When the current credit period resets, or null if there is no active billing
    period — including once a subscription is cancelled or its term has ended.
    """
