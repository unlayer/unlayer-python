# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectDomainsUpdateParams"]


class ProjectDomainsUpdateParams(TypedDict, total=False):
    domain: str
    """Updated domain name"""
