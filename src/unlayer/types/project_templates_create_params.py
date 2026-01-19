# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectTemplatesCreateParams"]


class ProjectTemplatesCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """The project ID to create the template in"""

    name: Required[str]
    """Template name"""

    display_mode: Annotated[Literal["email", "web", "document"], PropertyInfo(alias="displayMode")]
    """Template type/display mode"""
