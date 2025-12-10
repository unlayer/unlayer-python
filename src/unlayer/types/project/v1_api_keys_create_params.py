# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["V1APIKeysCreateParams"]


class V1APIKeysCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name for the API key"""

    domains: SequenceNotStr[str]
    """Allowed domains for this API key"""
