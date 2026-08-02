# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SuppressionRetrieveParams"]


class SuppressionRetrieveParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from a previous response. Omit to start from the beginning."""

    limit: int
    """Max number of results (1-200)"""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project ID (auto-resolved for API key auth)"""
