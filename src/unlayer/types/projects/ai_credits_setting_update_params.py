# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AICreditsSettingUpdateParams"]


class AICreditsSettingUpdateParams(TypedDict, total=False):
    exhaustion_behavior: Literal["disable", "show_error"]
    """What the editor does when the credit balance is exhausted."""

    threshold_alerts: Iterable[int]
    """
    Usage percentages (1-100) at which a threshold_reached webhook fires, once per
    crossing per period.
    """

    webhook_url: Optional[str]
    """HTTPS endpoint that receives AI credit webhooks."""
