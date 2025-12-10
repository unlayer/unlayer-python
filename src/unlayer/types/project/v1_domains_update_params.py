# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V1DomainsUpdateParams"]


class V1DomainsUpdateParams(TypedDict, total=False):
    domain: str
    """Updated domain name"""
