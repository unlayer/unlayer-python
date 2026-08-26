# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.emails import template_create_params
from ...types.emails.template_create_response import TemplateCreateResponse

__all__ = ["TemplateResource", "AsyncTemplateResource"]


class TemplateResource(SyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def with_raw_response(self) -> TemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return TemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return TemplateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        from_: str,
        template_id: str,
        to: SequenceNotStr[str],
        attachments: Iterable[template_create_params.Attachment] | Omit = omit,
        bcc: Iterable[object] | Omit = omit,
        cc: Iterable[object] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        reply_to: str | Omit = omit,
        subject: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        text: str | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        """
        Send a transactional email by rendering a saved template with optional merge
        variables. The template must have rendered HTML (saved at least once in the
        editor). The sender domain must be verified in the project workspace; verified
        sender domains are shared by every Developer Email API project in that
        workspace.

        Args:
          from_: Sender email address or "Name <email>" format. Domain must be verified.

          template_id: Template ID to use for the email body

          to: Exactly one recipient. Each request creates one independently tracked delivery.

          attachments: File attachments. Max 10 files per email, max 5 MB total payload size.

          bcc: BCC is not supported by this endpoint.

          cc: CC is not supported by this endpoint.

          headers: Custom email headers. Up to 9 printable-ASCII X-\\** headers are allowed. Header
              names may contain up to 126 characters and each name plus value may contain up
              to 996 characters.

          reply_to: Reply-To email address

          subject: Email subject line. Supports {{variable}} merge syntax. Defaults to template
              name if omitted.

          tags: Key-value tags for categorizing the email (e.g. {"campaign": "welcome"}). Max 10
              tags. Keys (1-64 chars) and values (up to 256 chars) may only contain letters,
              numbers, underscores, and hyphens (the Amazon SES message-tag character set).

          text: Plain text version of the email. Supports {{variable}} merge syntax.

          variables: Merge variables to substitute in the template and subject. Use {{key}} syntax in
              your template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v3/emails/template",
            body=maybe_transform(
                {
                    "from_": from_,
                    "template_id": template_id,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "reply_to": reply_to,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "variables": variables,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )


class AsyncTemplateResource(AsyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def with_raw_response(self) -> AsyncTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncTemplateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        from_: str,
        template_id: str,
        to: SequenceNotStr[str],
        attachments: Iterable[template_create_params.Attachment] | Omit = omit,
        bcc: Iterable[object] | Omit = omit,
        cc: Iterable[object] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        reply_to: str | Omit = omit,
        subject: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        text: str | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateCreateResponse:
        """
        Send a transactional email by rendering a saved template with optional merge
        variables. The template must have rendered HTML (saved at least once in the
        editor). The sender domain must be verified in the project workspace; verified
        sender domains are shared by every Developer Email API project in that
        workspace.

        Args:
          from_: Sender email address or "Name <email>" format. Domain must be verified.

          template_id: Template ID to use for the email body

          to: Exactly one recipient. Each request creates one independently tracked delivery.

          attachments: File attachments. Max 10 files per email, max 5 MB total payload size.

          bcc: BCC is not supported by this endpoint.

          cc: CC is not supported by this endpoint.

          headers: Custom email headers. Up to 9 printable-ASCII X-\\** headers are allowed. Header
              names may contain up to 126 characters and each name plus value may contain up
              to 996 characters.

          reply_to: Reply-To email address

          subject: Email subject line. Supports {{variable}} merge syntax. Defaults to template
              name if omitted.

          tags: Key-value tags for categorizing the email (e.g. {"campaign": "welcome"}). Max 10
              tags. Keys (1-64 chars) and values (up to 256 chars) may only contain letters,
              numbers, underscores, and hyphens (the Amazon SES message-tag character set).

          text: Plain text version of the email. Supports {{variable}} merge syntax.

          variables: Merge variables to substitute in the template and subject. Use {{key}} syntax in
              your template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v3/emails/template",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "template_id": template_id,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "reply_to": reply_to,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "variables": variables,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateCreateResponse,
        )


class TemplateResourceWithRawResponse:
    def __init__(self, template: TemplateResource) -> None:
        self._template = template

        self.create = to_raw_response_wrapper(
            template.create,
        )


class AsyncTemplateResourceWithRawResponse:
    def __init__(self, template: AsyncTemplateResource) -> None:
        self._template = template

        self.create = async_to_raw_response_wrapper(
            template.create,
        )


class TemplateResourceWithStreamingResponse:
    def __init__(self, template: TemplateResource) -> None:
        self._template = template

        self.create = to_streamed_response_wrapper(
            template.create,
        )


class AsyncTemplateResourceWithStreamingResponse:
    def __init__(self, template: AsyncTemplateResource) -> None:
        self._template = template

        self.create = async_to_streamed_response_wrapper(
            template.create,
        )
