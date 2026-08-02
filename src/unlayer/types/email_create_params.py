# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailCreateParams", "Attachment"]


class EmailCreateParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Sender email address or "Name <email>" format. Domain must be verified."""

    html: Required[str]
    """HTML content of the email"""

    subject: Required[str]
    """Email subject line"""

    to: Required[SequenceNotStr[str]]
    """Exactly one recipient. Each request creates one independently tracked delivery."""

    attachments: Iterable[Attachment]
    """File attachments.

    Max 10 files per email, max 5 MB total payload size (including headers and
    base64 overhead).
    """

    bcc: Iterable[object]
    """BCC is not supported by this endpoint."""

    cc: Iterable[object]
    """CC is not supported by this endpoint."""

    headers: Dict[str, str]
    """Custom email headers.

    Up to 9 printable-ASCII X-\\** headers are allowed (e.g. {"X-Entity-Ref-ID":
    "abc123"}). Header names may contain up to 126 characters and each name plus
    value may contain up to 996 characters.
    """

    reply_to: Annotated[str, PropertyInfo(alias="replyTo")]
    """Reply-To email address"""

    tags: Dict[str, str]
    """Key-value tags for categorizing the email (e.g.

    {"campaign": "welcome"}). Max 10 tags. Keys (1-64 chars) and values (up to 256
    chars) may only contain letters, numbers, underscores, and hyphens (the Amazon
    SES message-tag character set).
    """

    text: str
    """Plain text version of the email.

    If provided, a multipart/alternative message is sent.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="idempotency-key")]


class Attachment(TypedDict, total=False):
    content: Required[str]
    """Base64-encoded file content.

    Whitespace and MIME line wrapping are removed before validation; invalid base64
    is rejected with a 400 error.
    """

    content_type: Required[
        Annotated[
            Literal[
                "application/pdf",
                "application/zip",
                "application/json",
                "application/xml",
                "application/csv",
                "application/msword",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                "application/vnd.ms-excel",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "application/vnd.ms-powerpoint",
                "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                "text/plain",
                "text/html",
                "text/csv",
                "text/xml",
                "text/calendar",
                "image/png",
                "image/jpeg",
                "image/gif",
                "image/webp",
                "image/svg+xml",
                "audio/mpeg",
                "audio/wav",
                "video/mp4",
            ],
            PropertyInfo(alias="contentType"),
        ]
    ]
    """MIME type of the attachment. Required; must be one of the allowed types."""

    filename: Required[str]
    """The filename as it will appear to the recipient.

    Line breaks are rejected; quotes are stripped before it is written into the
    message.
    """
