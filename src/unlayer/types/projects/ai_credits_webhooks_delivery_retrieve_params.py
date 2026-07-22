# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AICreditsWebhooksDeliveryRetrieveParams"]


class AICreditsWebhooksDeliveryRetrieveParams(TypedDict, total=False):
    event: Literal["ai.credits.usage_recorded", "ai.credits.threshold_reached", "ai.credits.exhausted"]
    """Filter to a single event type."""

    limit: int
    """Max deliveries to return (1-100)."""

    offset: int
    """Number of deliveries to skip (pagination)."""

    status: Literal["pending", "delivered", "failed"]
    """Filter to a single delivery status."""
