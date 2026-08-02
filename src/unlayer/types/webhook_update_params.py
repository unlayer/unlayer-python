# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    active: bool
    """Whether the webhook is actively receiving events"""

    events: List[Literal["email.sent", "email.delivered", "email.bounced", "email.complained"]]
    """Event types to subscribe to. If omitted or empty, all events are sent."""

    url: str
    """The HTTPS URL to receive webhook events"""
