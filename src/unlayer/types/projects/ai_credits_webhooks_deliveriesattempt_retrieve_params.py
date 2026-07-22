# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AICreditsWebhooksDeliveriesattemptRetrieveParams"]


class AICreditsWebhooksDeliveriesattemptRetrieveParams(TypedDict, total=False):
    id: Required[str]

    limit: int
    """Max attempts to return (1-100)."""

    offset: int
    """Number of attempts to skip (pagination)."""
