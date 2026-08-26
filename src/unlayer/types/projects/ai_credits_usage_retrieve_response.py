# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AICreditsUsageRetrieveResponse", "Breakdown"]


class Breakdown(BaseModel):
    credits: int
    """AI credits used by this end user and feature type."""

    end_user_id: Optional[str] = None
    """The end user id, or null for unattributed usage."""

    feature_type: Literal["full_template_gen", "block_edit", "html_import", "image_import", "image_generation"]
    """The partner-facing feature type."""


class AICreditsUsageRetrieveResponse(BaseModel):
    breakdown: List[Breakdown]

    total: int
    """Number of breakdown rows matching the filter (ignores paging)."""

    total_credits_used: int
    """
    Total AI credits used across the full filtered range (not just the returned
    page).
    """
