# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import (
    emails_v1_send_create_params,
    emails_v1_render_create_params,
    emails_v1_send_template_template_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.emails_v1_send_create_response import EmailsV1SendCreateResponse
from ..types.emails_v1_render_create_response import EmailsV1RenderCreateResponse
from ..types.emails_v1_emails_retrieve_response import EmailsV1EmailsRetrieveResponse
from ..types.emails_v1_send_template_template_response import EmailsV1SendTemplateTemplateResponse

__all__ = ["EmailsV1Resource", "AsyncEmailsV1Resource"]


class EmailsV1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailsV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return EmailsV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return EmailsV1ResourceWithStreamingResponse(self)

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
    ) -> EmailsV1EmailsRetrieveResponse:
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
            cast_to=EmailsV1EmailsRetrieveResponse,
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
    ) -> EmailsV1RenderCreateResponse:
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
                emails_v1_render_create_params.EmailsV1RenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailsV1RenderCreateResponse,
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
    ) -> EmailsV1SendCreateResponse:
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
                emails_v1_send_create_params.EmailsV1SendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailsV1SendCreateResponse,
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
    ) -> EmailsV1SendTemplateTemplateResponse:
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
                emails_v1_send_template_template_params.EmailsV1SendTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailsV1SendTemplateTemplateResponse,
        )


class AsyncEmailsV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailsV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncEmailsV1ResourceWithStreamingResponse(self)

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
    ) -> EmailsV1EmailsRetrieveResponse:
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
            cast_to=EmailsV1EmailsRetrieveResponse,
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
    ) -> EmailsV1RenderCreateResponse:
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
                emails_v1_render_create_params.EmailsV1RenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailsV1RenderCreateResponse,
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
    ) -> EmailsV1SendCreateResponse:
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
                emails_v1_send_create_params.EmailsV1SendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailsV1SendCreateResponse,
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
    ) -> EmailsV1SendTemplateTemplateResponse:
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
                emails_v1_send_template_template_params.EmailsV1SendTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailsV1SendTemplateTemplateResponse,
        )


class EmailsV1ResourceWithRawResponse:
    def __init__(self, emails_v1: EmailsV1Resource) -> None:
        self._emails_v1 = emails_v1

        self.emails_retrieve = to_raw_response_wrapper(
            emails_v1.emails_retrieve,
        )
        self.render_create = to_raw_response_wrapper(
            emails_v1.render_create,
        )
        self.send_create = to_raw_response_wrapper(
            emails_v1.send_create,
        )
        self.send_template_template = to_raw_response_wrapper(
            emails_v1.send_template_template,
        )


class AsyncEmailsV1ResourceWithRawResponse:
    def __init__(self, emails_v1: AsyncEmailsV1Resource) -> None:
        self._emails_v1 = emails_v1

        self.emails_retrieve = async_to_raw_response_wrapper(
            emails_v1.emails_retrieve,
        )
        self.render_create = async_to_raw_response_wrapper(
            emails_v1.render_create,
        )
        self.send_create = async_to_raw_response_wrapper(
            emails_v1.send_create,
        )
        self.send_template_template = async_to_raw_response_wrapper(
            emails_v1.send_template_template,
        )


class EmailsV1ResourceWithStreamingResponse:
    def __init__(self, emails_v1: EmailsV1Resource) -> None:
        self._emails_v1 = emails_v1

        self.emails_retrieve = to_streamed_response_wrapper(
            emails_v1.emails_retrieve,
        )
        self.render_create = to_streamed_response_wrapper(
            emails_v1.render_create,
        )
        self.send_create = to_streamed_response_wrapper(
            emails_v1.send_create,
        )
        self.send_template_template = to_streamed_response_wrapper(
            emails_v1.send_template_template,
        )


class AsyncEmailsV1ResourceWithStreamingResponse:
    def __init__(self, emails_v1: AsyncEmailsV1Resource) -> None:
        self._emails_v1 = emails_v1

        self.emails_retrieve = async_to_streamed_response_wrapper(
            emails_v1.emails_retrieve,
        )
        self.render_create = async_to_streamed_response_wrapper(
            emails_v1.render_create,
        )
        self.send_create = async_to_streamed_response_wrapper(
            emails_v1.send_create,
        )
        self.send_template_template = async_to_streamed_response_wrapper(
            emails_v1.send_template_template,
        )
