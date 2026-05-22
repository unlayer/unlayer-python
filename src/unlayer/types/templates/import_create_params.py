# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ImportCreateParams", "Input"]


class ImportCreateParams(TypedDict, total=False):
    display_mode: Required[Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]]
    """Display mode for the imported design"""

    input: Required[Iterable[Input]]
    """Array of input parts.

    Must contain exactly one "html" or "image" part; may also contain one or more
    "text" parts with optional instructions.
    """

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The project ID (required for PAT auth, auto-resolved for API key auth)"""

    model: Literal["anthropic/claude-opus-4-6", "openai/gpt-5.2"]
    """AI model to use, in provider/model format.

    Optional — defaults to anthropic/claude-opus-4-6.
    """


class Input(TypedDict, total=False):
    type: Required[Literal["html", "image", "text"]]
    """The type of input part.

    "html" or "image" carries the source content; "text" carries optional
    instructions to apply during import.
    """

    data: str
    """Base64 image data URL, e.g. "data:image/png;base64,…" (for type: "image")"""

    html: str
    """HTML string to import (for type: "html")"""

    text: str
    """
    Optional natural-language instructions to apply during import (for type: "text")
    """

    url: str
    """Image URL to import (for type: "image")"""
