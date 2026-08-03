# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BlockRetrieveParams"]


class BlockRetrieveParams(TypedDict, total=False):
    category: str
    """Filter by category (case-insensitive search)"""

    cursor: str
    """Pagination cursor from previous response"""

    display_mode: Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]
    """Filter by display mode"""

    include_data: Annotated[bool, PropertyInfo(alias="includeData")]
    """Include the block design JSON in each item.

    Pass false for lightweight sweeps (e.g. usage reports).
    """

    limit: int
    """Number of blocks to return (1-100)"""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The project ID to list blocks for"""

    scope: Literal["all", "shared", "user"]
    """
    Filter by block ownership: shared project blocks, end-user saved blocks, or both
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """
    Only blocks saved by this end-user (exact match on the user id your app passes
    to the editor)
    """
