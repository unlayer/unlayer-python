# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FullToSimpleCreateParams", "Design"]


class FullToSimpleCreateParams(TypedDict, total=False):
    design: Required[Design]

    display_mode: Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]

    include_conversion: Annotated[bool, PropertyInfo(alias="includeConversion")]
    """When true, includes \\__conversion metadata in the response.

    This metadata can be passed to simple-to-full to restore original values without
    data loss.
    """

    include_default_values: Annotated[bool, PropertyInfo(alias="includeDefaultValues")]


class Design(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    body: Required[Dict[str, object]]

    counters: Dict[str, object]

    schema_version: Annotated[float, PropertyInfo(alias="schemaVersion")]
