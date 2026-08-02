# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["StatRetrieveParams"]


class StatRetrieveParams(TypedDict, total=False):
    group_by: Annotated[Literal["day"], PropertyInfo(alias="groupBy")]
    """Group results by day for chart data"""

    period: Literal["7d", "30d", "90d"]
    """Time period for stats"""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Project ID (auto-resolved for API key auth)"""
