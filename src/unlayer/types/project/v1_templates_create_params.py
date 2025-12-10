# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V1TemplatesCreateParams"]


class V1TemplatesCreateParams(TypedDict, total=False):
    name: Required[str]
    """Template name"""

    body: str
    """Email body content"""

    subject: str
    """Email subject line"""
