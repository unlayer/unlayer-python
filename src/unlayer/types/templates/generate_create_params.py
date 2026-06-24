# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "GenerateCreateParams",
    "Message",
    "MessageContent",
    "MessageContentFile",
    "MessageMetadata",
    "MessageMetadataAction",
    "Output",
    "Context",
    "ContextCustomTool",
    "ContextSelection",
]


class GenerateCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """Conversation messages in chronological order, capped at 10 messages.

    The last `user` message is the prompt for this turn; any earlier
    `user`/`assistant` text turns are forwarded to the model as prior chat context.
    A `user` message may carry a predefined prompt action via `metadata.action.id`
    (e.g. SPELLING, REPHRASE).
    """

    output: Required[Output]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The project ID (required for PAT auth, auto-resolved for API key auth)"""

    context: Context

    conversation_id: Annotated[str, PropertyInfo(alias="conversationId")]
    """Reserved for future server-side conversation memory."""

    fallback_models: Annotated[Union[bool, SequenceNotStr[str]], PropertyInfo(alias="fallbackModels")]
    """Transient-outage fallback controls.

    Omit to use Unlayer defaults only when no model is pinned; true always uses
    Unlayer defaults; false disables the outage tail; an ordered array replaces the
    default provider/model strings.
    """

    locale: str
    """BCP-47 fallback locale for AI status messages."""

    model: str
    """Preferred AI model in "provider/id" form, e.g.

    "anthropic/claude-opus-4-7". Optional — server resolves a default per output
    kind.
    """


class MessageContentFile(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    url: Required[str]

    media_type: Annotated[str, PropertyInfo(alias="mediaType")]


class MessageContent(TypedDict, total=False):
    type: Required[Literal["text", "image", "file"]]

    file: MessageContentFile

    image: str
    """URL or data URL of the image"""

    text: str


class MessageMetadataAction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    id: Required[str]


class MessageMetadata(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    action: MessageMetadataAction


class Message(TypedDict, total=False):
    content: Required[Iterable[MessageContent]]

    role: Required[Literal["user", "assistant", "system"]]

    metadata: MessageMetadata


class Output(TypedDict, total=False):
    display_mode: Required[Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]]

    kind: Required[Literal["template", "page", "body", "header", "footer", "row", "column", "content", "text"]]

    schema_version: Annotated[int, PropertyInfo(alias="schemaVersion")]


class ContextCustomTool(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    options: Required[Dict[str, object]]

    slug: Required[str]


class ContextSelection(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    id: Required[Union[str, float]]

    collection: Required[Literal["pages", "bodies", "rows", "columns", "contents", "headers", "footers"]]

    value: str


class Context(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    available_tools: Annotated[SequenceNotStr[str], PropertyInfo(alias="availableTools")]

    custom_tools: Annotated[Iterable[ContextCustomTool], PropertyInfo(alias="customTools")]

    full_design: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="fullDesign")]

    selection: Optional[ContextSelection]
