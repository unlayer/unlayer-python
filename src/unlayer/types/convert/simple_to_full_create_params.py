# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SimpleToFullCreateParams", "Design", "Design_Conversion"]


class SimpleToFullCreateParams(TypedDict, total=False):
    design: Required[Design]

    display_mode: Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]

    include_default_values: Annotated[bool, PropertyInfo(alias="includeDefaultValues")]


class Design_Conversion(TypedDict, total=False):
    data: str

    version: float


class DesignTyped(TypedDict, total=False):
    body: Required[Dict[str, object]]

    _conversion: Design_Conversion

    counters: Dict[str, object]

    schema_version: Annotated[float, PropertyInfo(alias="schemaVersion")]


Design: TypeAlias = Union[DesignTyped, Dict[str, object]]
