# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import date
from typing_extensions import Literal

import httpx

from .stats import (
    StatsResource,
    AsyncStatsResource,
    StatsResourceWithRawResponse,
    AsyncStatsResourceWithRawResponse,
    StatsResourceWithStreamingResponse,
    AsyncStatsResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .render import (
    RenderResource,
    AsyncRenderResource,
    RenderResourceWithRawResponse,
    AsyncRenderResourceWithRawResponse,
    RenderResourceWithStreamingResponse,
    AsyncRenderResourceWithStreamingResponse,
)
from ...types import email_list_params, email_create_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .template import (
    TemplateResource,
    AsyncTemplateResource,
    TemplateResourceWithRawResponse,
    AsyncTemplateResourceWithRawResponse,
    TemplateResourceWithStreamingResponse,
    AsyncTemplateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .suppressions import (
    SuppressionsResource,
    AsyncSuppressionsResource,
    SuppressionsResourceWithRawResponse,
    AsyncSuppressionsResourceWithRawResponse,
    SuppressionsResourceWithStreamingResponse,
    AsyncSuppressionsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .suppressions_check import (
    SuppressionsCheckResource,
    AsyncSuppressionsCheckResource,
    SuppressionsCheckResourceWithRawResponse,
    AsyncSuppressionsCheckResourceWithRawResponse,
    SuppressionsCheckResourceWithStreamingResponse,
    AsyncSuppressionsCheckResourceWithStreamingResponse,
)
from ...types.email_list_response import EmailListResponse
from ...types.email_create_response import EmailCreateResponse
from ...types.email_retrieve_response import EmailRetrieveResponse

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def events(self) -> EventsResource:
        """Send and manage transactional email."""
        return EventsResource(self._client)

    @cached_property
    def render(self) -> RenderResource:
        """Send and manage transactional email."""
        return RenderResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        """Send and manage transactional email."""
        return SettingsResource(self._client)

    @cached_property
    def stats(self) -> StatsResource:
        """Send and manage transactional email."""
        return StatsResource(self._client)

    @cached_property
    def suppressions(self) -> SuppressionsResource:
        """Send and manage transactional email."""
        return SuppressionsResource(self._client)

    @cached_property
    def suppressions_check(self) -> SuppressionsCheckResource:
        """Send and manage transactional email."""
        return SuppressionsCheckResource(self._client)

    @cached_property
    def template(self) -> TemplateResource:
        """Send and manage transactional email."""
        return TemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        from_: str,
        html: str,
        subject: str,
        to: SequenceNotStr[str],
        attachments: Iterable[email_create_params.Attachment] | Omit = omit,
        bcc: Iterable[object] | Omit = omit,
        cc: Iterable[object] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        reply_to: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        text: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailCreateResponse:
        """Send a transactional email with raw HTML content.

        The sender domain must be
        verified in the project workspace; verified sender domains are shared by every
        Developer Email API project in that workspace.

        Args:
          from_: Sender email address or "Name <email>" format. Domain must be verified.

          html: HTML content of the email

          subject: Email subject line

          to: Exactly one recipient. Each request creates one independently tracked delivery.

          attachments: File attachments. Max 10 files per email, max 5 MB total payload size (including
              headers and base64 overhead).

          bcc: BCC is not supported by this endpoint.

          cc: CC is not supported by this endpoint.

          headers: Custom email headers. Up to 9 printable-ASCII X-\\** headers are allowed (e.g.
              {"X-Entity-Ref-ID": "abc123"}). Header names may contain up to 126 characters
              and each name plus value may contain up to 996 characters.

          reply_to: Reply-To email address

          tags: Key-value tags for categorizing the email (e.g. {"campaign": "welcome"}). Max 10
              tags. Keys (1-64 chars) and values (up to 256 chars) may only contain letters,
              numbers, underscores, and hyphens (the Amazon SES message-tag character set).

          text: Plain text version of the email. If provided, a multipart/alternative message is
              sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v3/emails",
            body=maybe_transform(
                {
                    "from_": from_,
                    "html": html,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "reply_to": reply_to,
                    "tags": tags,
                    "text": text,
                },
                email_create_params.EmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRetrieveResponse:
        """
        Retrieve details of a sent email, including its current delivery status, during
        the rolling 90-day history window. Expired emails return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/emails/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        from_: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        project_id: str | Omit = omit,
        search: str | Omit = omit,
        status: Literal["queued", "sending", "sent", "delivered", "bounced", "complained", "failed"] | Omit = omit,
        tag: str | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailListResponse:
        """
        List emails sent from this project within the rolling 90-day history window.
        Without a status filter, results and date bounds use acceptance time. With a
        status filter, results and date bounds use the time each email entered that
        status.

        Args:
          cursor: Pagination cursor from previous response

          from_: Start date (ISO date). Bounds acceptance time normally, or status transition
              time when status is supplied.

          limit: Number of emails to return (1-100)

          project_id: Project ID (auto-resolved for API key auth)

          search: Search recipient addresses and subjects by case-sensitive substring

          status: Filter by email delivery status

          tag: Filter by tag in "key=value" format (e.g. "campaign=welcome")

          to: End date (ISO date). Bounds acceptance time normally, or status transition time
              when status is supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/emails",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "project_id": project_id,
                        "search": search,
                        "status": status,
                        "tag": tag,
                        "to": to,
                    },
                    email_list_params.EmailListParams,
                ),
            ),
            cast_to=EmailListResponse,
        )


class AsyncEmailsResource(AsyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Send and manage transactional email."""
        return AsyncEventsResource(self._client)

    @cached_property
    def render(self) -> AsyncRenderResource:
        """Send and manage transactional email."""
        return AsyncRenderResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        """Send and manage transactional email."""
        return AsyncSettingsResource(self._client)

    @cached_property
    def stats(self) -> AsyncStatsResource:
        """Send and manage transactional email."""
        return AsyncStatsResource(self._client)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResource:
        """Send and manage transactional email."""
        return AsyncSuppressionsResource(self._client)

    @cached_property
    def suppressions_check(self) -> AsyncSuppressionsCheckResource:
        """Send and manage transactional email."""
        return AsyncSuppressionsCheckResource(self._client)

    @cached_property
    def template(self) -> AsyncTemplateResource:
        """Send and manage transactional email."""
        return AsyncTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        from_: str,
        html: str,
        subject: str,
        to: SequenceNotStr[str],
        attachments: Iterable[email_create_params.Attachment] | Omit = omit,
        bcc: Iterable[object] | Omit = omit,
        cc: Iterable[object] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        reply_to: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        text: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailCreateResponse:
        """Send a transactional email with raw HTML content.

        The sender domain must be
        verified in the project workspace; verified sender domains are shared by every
        Developer Email API project in that workspace.

        Args:
          from_: Sender email address or "Name <email>" format. Domain must be verified.

          html: HTML content of the email

          subject: Email subject line

          to: Exactly one recipient. Each request creates one independently tracked delivery.

          attachments: File attachments. Max 10 files per email, max 5 MB total payload size (including
              headers and base64 overhead).

          bcc: BCC is not supported by this endpoint.

          cc: CC is not supported by this endpoint.

          headers: Custom email headers. Up to 9 printable-ASCII X-\\** headers are allowed (e.g.
              {"X-Entity-Ref-ID": "abc123"}). Header names may contain up to 126 characters
              and each name plus value may contain up to 996 characters.

          reply_to: Reply-To email address

          tags: Key-value tags for categorizing the email (e.g. {"campaign": "welcome"}). Max 10
              tags. Keys (1-64 chars) and values (up to 256 chars) may only contain letters,
              numbers, underscores, and hyphens (the Amazon SES message-tag character set).

          text: Plain text version of the email. If provided, a multipart/alternative message is
              sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"idempotency-key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v3/emails",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "html": html,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "reply_to": reply_to,
                    "tags": tags,
                    "text": text,
                },
                email_create_params.EmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRetrieveResponse:
        """
        Retrieve details of a sent email, including its current delivery status, during
        the rolling 90-day history window. Expired emails return 404.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/emails/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        from_: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        project_id: str | Omit = omit,
        search: str | Omit = omit,
        status: Literal["queued", "sending", "sent", "delivered", "bounced", "complained", "failed"] | Omit = omit,
        tag: str | Omit = omit,
        to: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailListResponse:
        """
        List emails sent from this project within the rolling 90-day history window.
        Without a status filter, results and date bounds use acceptance time. With a
        status filter, results and date bounds use the time each email entered that
        status.

        Args:
          cursor: Pagination cursor from previous response

          from_: Start date (ISO date). Bounds acceptance time normally, or status transition
              time when status is supplied.

          limit: Number of emails to return (1-100)

          project_id: Project ID (auto-resolved for API key auth)

          search: Search recipient addresses and subjects by case-sensitive substring

          status: Filter by email delivery status

          tag: Filter by tag in "key=value" format (e.g. "campaign=welcome")

          to: End date (ISO date). Bounds acceptance time normally, or status transition time
              when status is supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/emails",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "from_": from_,
                        "limit": limit,
                        "project_id": project_id,
                        "search": search,
                        "status": status,
                        "tag": tag,
                        "to": to,
                    },
                    email_list_params.EmailListParams,
                ),
            ),
            cast_to=EmailListResponse,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.create = to_raw_response_wrapper(
            emails.create,
        )
        self.retrieve = to_raw_response_wrapper(
            emails.retrieve,
        )
        self.list = to_raw_response_wrapper(
            emails.list,
        )

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        """Send and manage transactional email."""
        return EventsResourceWithRawResponse(self._emails.events)

    @cached_property
    def render(self) -> RenderResourceWithRawResponse:
        """Send and manage transactional email."""
        return RenderResourceWithRawResponse(self._emails.render)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        """Send and manage transactional email."""
        return SettingsResourceWithRawResponse(self._emails.settings)

    @cached_property
    def stats(self) -> StatsResourceWithRawResponse:
        """Send and manage transactional email."""
        return StatsResourceWithRawResponse(self._emails.stats)

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithRawResponse:
        """Send and manage transactional email."""
        return SuppressionsResourceWithRawResponse(self._emails.suppressions)

    @cached_property
    def suppressions_check(self) -> SuppressionsCheckResourceWithRawResponse:
        """Send and manage transactional email."""
        return SuppressionsCheckResourceWithRawResponse(self._emails.suppressions_check)

    @cached_property
    def template(self) -> TemplateResourceWithRawResponse:
        """Send and manage transactional email."""
        return TemplateResourceWithRawResponse(self._emails.template)


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.create = async_to_raw_response_wrapper(
            emails.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            emails.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            emails.list,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        """Send and manage transactional email."""
        return AsyncEventsResourceWithRawResponse(self._emails.events)

    @cached_property
    def render(self) -> AsyncRenderResourceWithRawResponse:
        """Send and manage transactional email."""
        return AsyncRenderResourceWithRawResponse(self._emails.render)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        """Send and manage transactional email."""
        return AsyncSettingsResourceWithRawResponse(self._emails.settings)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithRawResponse:
        """Send and manage transactional email."""
        return AsyncStatsResourceWithRawResponse(self._emails.stats)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithRawResponse:
        """Send and manage transactional email."""
        return AsyncSuppressionsResourceWithRawResponse(self._emails.suppressions)

    @cached_property
    def suppressions_check(self) -> AsyncSuppressionsCheckResourceWithRawResponse:
        """Send and manage transactional email."""
        return AsyncSuppressionsCheckResourceWithRawResponse(self._emails.suppressions_check)

    @cached_property
    def template(self) -> AsyncTemplateResourceWithRawResponse:
        """Send and manage transactional email."""
        return AsyncTemplateResourceWithRawResponse(self._emails.template)


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.create = to_streamed_response_wrapper(
            emails.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            emails.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            emails.list,
        )

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return EventsResourceWithStreamingResponse(self._emails.events)

    @cached_property
    def render(self) -> RenderResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return RenderResourceWithStreamingResponse(self._emails.render)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return SettingsResourceWithStreamingResponse(self._emails.settings)

    @cached_property
    def stats(self) -> StatsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return StatsResourceWithStreamingResponse(self._emails.stats)

    @cached_property
    def suppressions(self) -> SuppressionsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return SuppressionsResourceWithStreamingResponse(self._emails.suppressions)

    @cached_property
    def suppressions_check(self) -> SuppressionsCheckResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return SuppressionsCheckResourceWithStreamingResponse(self._emails.suppressions_check)

    @cached_property
    def template(self) -> TemplateResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return TemplateResourceWithStreamingResponse(self._emails.template)


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.create = async_to_streamed_response_wrapper(
            emails.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            emails.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            emails.list,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return AsyncEventsResourceWithStreamingResponse(self._emails.events)

    @cached_property
    def render(self) -> AsyncRenderResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return AsyncRenderResourceWithStreamingResponse(self._emails.render)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return AsyncSettingsResourceWithStreamingResponse(self._emails.settings)

    @cached_property
    def stats(self) -> AsyncStatsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return AsyncStatsResourceWithStreamingResponse(self._emails.stats)

    @cached_property
    def suppressions(self) -> AsyncSuppressionsResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return AsyncSuppressionsResourceWithStreamingResponse(self._emails.suppressions)

    @cached_property
    def suppressions_check(self) -> AsyncSuppressionsCheckResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return AsyncSuppressionsCheckResourceWithStreamingResponse(self._emails.suppressions_check)

    @cached_property
    def template(self) -> AsyncTemplateResourceWithStreamingResponse:
        """Send and manage transactional email."""
        return AsyncTemplateResourceWithStreamingResponse(self._emails.template)
