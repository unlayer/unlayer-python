# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SchemaRetrieveParams"]


class SchemaRetrieveParams(TypedDict, total=False):
    display_mode: Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]
    """Display mode whose rules the schema describes (email, web, document, popup).

    Defaults to "email".
    """

    simple: bool
    """When true, returns the Simple schema instead of the Full schema."""
