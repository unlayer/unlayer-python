# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TemplateUpdateParams"]


class TemplateUpdateParams(TypedDict, total=False):
    body: str
    """Updated email body content"""

    name: str
    """Updated template name"""

    subject: str
    """Updated email subject line"""
