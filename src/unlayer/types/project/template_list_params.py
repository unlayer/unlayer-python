# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """The project ID to list templates for"""

    cursor: str
    """Pagination cursor from previous response"""

    display_mode: Annotated[Literal["email", "web", "document"], PropertyInfo(alias="displayMode")]
    """Filter by template type"""

    limit: int
    """Number of templates to return (1-100)"""

    name: str
    """Filter by name (case-insensitive search)"""
