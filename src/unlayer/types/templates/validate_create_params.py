# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ValidateCreateParams", "CustomTool", "CustomToolOptions"]


class ValidateCreateParams(TypedDict, total=False):
    design: Required[Dict[str, object]]
    """The design JSON to validate."""

    custom_tools: Annotated[Iterable[CustomTool], PropertyInfo(alias="customTools")]
    """Custom tool declarations, in the same shape passed to unlayer.registerTool.

    When provided, blocks matching a declared tool have their values checked against
    the tool's declared options (wrong types are reported at their exact path).
    Blocks of undeclared tools keep envelope-only validation.
    """

    display_mode: Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]
    """Display mode for the design (email, web, document, popup).

    Some validation rules differ per mode. Defaults to "email" — without a default,
    options from every mode would apply at once, the strictest possible check, and
    real editor-saved designs could be reported invalid.
    """

    migrate: bool
    """
    When true (default), a full-form design with an older schemaVersion is upgraded
    to the current schema before validating — matching how the editor and the
    convert endpoints treat stored designs. Designs without a schemaVersion predate
    versioning and are fully migrated the same way. Set to false to check strict
    conformance with the current schema version. Designs with a newer schemaVersion
    than this API knows are validated as-if-current.
    """

    schema: Literal["full", "simple"]
    """Which form of the schema to validate against. Defaults to "full"."""


class CustomToolOptions(TypedDict, total=False):
    options: object


class CustomTool(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    options: Required[Dict[str, CustomToolOptions]]

    slug: Required[str]

    label: str

    supported_display_modes: Annotated[
        List[Literal["email", "web", "popup", "document"]], PropertyInfo(alias="supportedDisplayModes")
    ]

    type: str

    values: Dict[str, object]
