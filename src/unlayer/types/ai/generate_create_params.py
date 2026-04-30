# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["GenerateCreateParams", "Input", "Output", "Context", "ContextCustomTool"]


class GenerateCreateParams(TypedDict, total=False):
    display_mode: Required[Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]]
    """Display mode for the design"""

    input: Required[Iterable[Input]]
    """Array of typed input parts (max 50)"""

    output: Required[Output]
    """What to generate"""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The project ID (required for PAT auth, auto-resolved for API key auth)"""

    context: Context
    """Editor environment context"""

    model: Literal["anthropic/claude-opus-4-6", "openai/gpt-5.2"]
    """AI model to use, in provider/model format.

    Optional — defaults to anthropic/claude-opus-4-6.
    """


class Input(TypedDict, total=False):
    type: Required[Literal["text", "prompt", "json", "html", "image"]]
    """The type of input part"""

    id: str
    """
    Predefined prompt ID: SPELLING, EXPAND, SUMMARIZE, REPHRASE, FRIENDLY, FORMAL
    (for type: "prompt")
    """

    block_type: Annotated[str, PropertyInfo(alias="blockType")]
    """Block type of the design data (for type: "json")"""

    data: Union[Dict[str, object], str]
    """
    Existing design data (object, for type: "json") or base64 image data (string,
    for type: "image")
    """

    html: str
    """HTML string to import (for type: "html")"""

    schema_version: Annotated[int, PropertyInfo(alias="schemaVersion")]
    """Design schema version (for type: "json")"""

    text: str
    """Natural language prompt (for type: "text")"""

    url: str
    """Image URL to import (for type: "image")"""


class Output(TypedDict, total=False):
    """What to generate"""

    block_type: Required[
        Annotated[Literal["template", "page", "body", "content", "row", "column"], PropertyInfo(alias="blockType")]
    ]
    """The type of design block to generate"""

    type: Required[Literal["json"]]
    """Output format — currently only "json" is supported"""


class ContextCustomTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    options: Required[Dict[str, object]]

    slug: Required[str]


class Context(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """Editor environment context"""

    available_tools: Annotated[SequenceNotStr[str], PropertyInfo(alias="availableTools")]
    """Filter content types available in the generated design"""

    custom_tools: Annotated[Iterable[ContextCustomTool], PropertyInfo(alias="customTools")]
    """Custom tool declarations with their options"""
