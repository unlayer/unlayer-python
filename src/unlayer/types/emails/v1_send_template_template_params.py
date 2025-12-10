# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["V1SendTemplateTemplateParams"]


class V1SendTemplateTemplateParams(TypedDict, total=False):
    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]
    """ID of the template to use"""

    to: Required[str]
    """Recipient email address"""

    merge_tags: Annotated[Dict[str, str], PropertyInfo(alias="mergeTags")]
    """Optional merge tags for personalization"""

    subject: str
    """Email subject line (optional, uses template default if not provided)"""
