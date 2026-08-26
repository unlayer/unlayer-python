# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AICreditsUsageRetrieveParams"]


class AICreditsUsageRetrieveParams(TypedDict, total=False):
    end: str
    """End date (inclusive), YYYY-MM-DD."""

    end_user_id: str
    """Filter to a single end user id."""

    feature_type: Literal["full_template_gen", "block_edit", "html_import", "image_import", "image_generation"]
    """Filter to a single feature type."""

    limit: int
    """Max breakdown rows to return (1-1000)."""

    offset: int
    """Number of breakdown rows to skip (pagination)."""

    order: Literal["asc", "desc"]
    """Sort direction. Defaults to desc (highest credits first)."""

    sort: Literal["credits", "end_user_id", "feature_type"]
    """Field the breakdown is ordered by. Defaults to credits."""

    start: str
    """Start date (inclusive), YYYY-MM-DD."""
