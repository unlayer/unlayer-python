# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
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

    fallback_models: Annotated[Union[bool, SequenceNotStr[str]], PropertyInfo(alias="fallbackModels")]
    """Transient-outage fallback controls.

    Omit to use Unlayer defaults only when no model is pinned; true always uses
    Unlayer defaults; false disables the outage tail; an ordered array replaces the
    default provider/model strings.
    """

    model: str
    """Preferred AI model.

    Accepts a provider/model string (e.g. "anthropic/claude-opus-4-7",
    "openai/gpt-5.5"), a bare provider ("anthropic", "openai") which uses that
    provider's default model, or a bare model id ("claude-opus-4-7", "gpt-5.5") with
    the provider inferred from the name. Optional — defaults to
    anthropic/claude-opus-4-7.
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
