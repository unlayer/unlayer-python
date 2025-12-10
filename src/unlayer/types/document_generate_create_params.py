# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentGenerateCreateParams"]


class DocumentGenerateCreateParams(TypedDict, total=False):
    design: Required[Dict[str, object]]
    """Proprietary design format JSON"""

    filename: str
    """Optional filename for the generated PDF"""

    html: str
    """HTML content to convert to PDF"""

    merge_tags: Annotated[Dict[str, str], PropertyInfo(alias="mergeTags")]
    """Optional merge tags for personalization"""

    url: str
    """URL to convert to PDF"""
