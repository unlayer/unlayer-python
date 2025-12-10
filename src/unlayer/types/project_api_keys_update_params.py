# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ProjectAPIKeysUpdateParams"]


class ProjectAPIKeysUpdateParams(TypedDict, total=False):
    active: bool
    """Whether the API key is active"""

    domains: SequenceNotStr[str]
    """Updated allowed domains"""

    name: str
    """Updated name for the API key"""
