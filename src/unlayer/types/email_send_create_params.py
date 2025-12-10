# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailSendCreateParams"]


class EmailSendCreateParams(TypedDict, total=False):
    design: Required[Dict[str, object]]
    """Proprietary design format JSON"""

    to: Required[str]
    """Recipient email address"""

    html: str
    """HTML content to send"""

    merge_tags: Annotated[Dict[str, str], PropertyInfo(alias="mergeTags")]
    """Optional merge tags for personalization"""

    subject: str
    """Email subject line"""
