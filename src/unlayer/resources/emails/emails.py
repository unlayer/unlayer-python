# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from .v1 import (
    V1Resource,
    AsyncV1Resource,
    V1ResourceWithRawResponse,
    AsyncV1ResourceWithRawResponse,
    V1ResourceWithStreamingResponse,
    AsyncV1ResourceWithStreamingResponse,
)
from ...types import email_send_create_params, email_render_create_params, email_send_template_template_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.email_send_create_response import EmailSendCreateResponse
from ...types.email_render_create_response import EmailRenderCreateResponse
from ...types.email_emails_retrieve_response import EmailEmailsRetrieveResponse
from ...types.email_send_template_template_response import EmailSendTemplateTemplateResponse

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def v1(self) -> V1Resource:
        return V1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)

    def emails_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailEmailsRetrieveResponse:
        """
        Retrieve details of a previously sent email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/emails/v1/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailEmailsRetrieveResponse,
        )

    def render_create(
        self,
        *,
        design: Dict[str, object],
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRenderCreateResponse:
        """
        Convert design JSON to HTML with optional merge tags.

        Args:
          design: Proprietary design format JSON

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/emails/v1/render",
            body=maybe_transform(
                {
                    "design": design,
                    "merge_tags": merge_tags,
                },
                email_render_create_params.EmailRenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRenderCreateResponse,
        )

    def send_create(
        self,
        *,
        design: Dict[str, object],
        to: str,
        html: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendCreateResponse:
        """
        Send email with design JSON or HTML content.

        Args:
          design: Proprietary design format JSON

          to: Recipient email address

          html: HTML content to send

          merge_tags: Optional merge tags for personalization

          subject: Email subject line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/emails/v1/send",
            body=maybe_transform(
                {
                    "design": design,
                    "to": to,
                    "html": html,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                email_send_create_params.EmailSendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendCreateResponse,
        )

    def send_template_template(
        self,
        *,
        template_id: str,
        to: str,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendTemplateTemplateResponse:
        """
        Send email using an existing template with merge tags.

        Args:
          template_id: ID of the template to use

          to: Recipient email address

          merge_tags: Optional merge tags for personalization

          subject: Email subject line (optional, uses template default if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/emails/v1/send/template",
            body=maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                email_send_template_template_params.EmailSendTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendTemplateTemplateResponse,
        )


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def v1(self) -> AsyncV1Resource:
        return AsyncV1Resource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)

    async def emails_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailEmailsRetrieveResponse:
        """
        Retrieve details of a previously sent email.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/emails/v1/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailEmailsRetrieveResponse,
        )

    async def render_create(
        self,
        *,
        design: Dict[str, object],
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRenderCreateResponse:
        """
        Convert design JSON to HTML with optional merge tags.

        Args:
          design: Proprietary design format JSON

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/emails/v1/render",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "merge_tags": merge_tags,
                },
                email_render_create_params.EmailRenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRenderCreateResponse,
        )

    async def send_create(
        self,
        *,
        design: Dict[str, object],
        to: str,
        html: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendCreateResponse:
        """
        Send email with design JSON or HTML content.

        Args:
          design: Proprietary design format JSON

          to: Recipient email address

          html: HTML content to send

          merge_tags: Optional merge tags for personalization

          subject: Email subject line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/emails/v1/send",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "to": to,
                    "html": html,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                email_send_create_params.EmailSendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendCreateResponse,
        )

    async def send_template_template(
        self,
        *,
        template_id: str,
        to: str,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendTemplateTemplateResponse:
        """
        Send email using an existing template with merge tags.

        Args:
          template_id: ID of the template to use

          to: Recipient email address

          merge_tags: Optional merge tags for personalization

          subject: Email subject line (optional, uses template default if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/emails/v1/send/template",
            body=await async_maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                email_send_template_template_params.EmailSendTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendTemplateTemplateResponse,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.emails_retrieve = to_raw_response_wrapper(
            emails.emails_retrieve,
        )
        self.render_create = to_raw_response_wrapper(
            emails.render_create,
        )
        self.send_create = to_raw_response_wrapper(
            emails.send_create,
        )
        self.send_template_template = to_raw_response_wrapper(
            emails.send_template_template,
        )

    @cached_property
    def v1(self) -> V1ResourceWithRawResponse:
        return V1ResourceWithRawResponse(self._emails.v1)


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.emails_retrieve = async_to_raw_response_wrapper(
            emails.emails_retrieve,
        )
        self.render_create = async_to_raw_response_wrapper(
            emails.render_create,
        )
        self.send_create = async_to_raw_response_wrapper(
            emails.send_create,
        )
        self.send_template_template = async_to_raw_response_wrapper(
            emails.send_template_template,
        )

    @cached_property
    def v1(self) -> AsyncV1ResourceWithRawResponse:
        return AsyncV1ResourceWithRawResponse(self._emails.v1)


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.emails_retrieve = to_streamed_response_wrapper(
            emails.emails_retrieve,
        )
        self.render_create = to_streamed_response_wrapper(
            emails.render_create,
        )
        self.send_create = to_streamed_response_wrapper(
            emails.send_create,
        )
        self.send_template_template = to_streamed_response_wrapper(
            emails.send_template_template,
        )

    @cached_property
    def v1(self) -> V1ResourceWithStreamingResponse:
        return V1ResourceWithStreamingResponse(self._emails.v1)


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.emails_retrieve = async_to_streamed_response_wrapper(
            emails.emails_retrieve,
        )
        self.render_create = async_to_streamed_response_wrapper(
            emails.render_create,
        )
        self.send_create = async_to_streamed_response_wrapper(
            emails.send_create,
        )
        self.send_template_template = async_to_streamed_response_wrapper(
            emails.send_template_template,
        )

    @cached_property
    def v1(self) -> AsyncV1ResourceWithStreamingResponse:
        return AsyncV1ResourceWithStreamingResponse(self._emails.v1)
