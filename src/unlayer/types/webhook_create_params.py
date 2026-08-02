# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    url: Required[str]
    """The HTTPS URL to receive webhook events"""

    active: bool
    """Whether the webhook is active"""

    events: List[Literal["email.sent", "email.delivered", "email.bounced", "email.complained"]]
    """Event types to subscribe to. If omitted or empty, all events are sent."""
