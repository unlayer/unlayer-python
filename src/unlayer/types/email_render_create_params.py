# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailRenderCreateParams"]


class EmailRenderCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """The project ID"""

    design: Required[Dict[str, object]]
    """Proprietary design format JSON"""

    merge_tags: Annotated[Dict[str, str], PropertyInfo(alias="mergeTags")]
    """Optional merge tags for personalization"""
