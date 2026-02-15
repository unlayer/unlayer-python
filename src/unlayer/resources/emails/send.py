# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

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
from ...types.emails import send_create_params
from ...types.emails.send_create_response import SendCreateResponse

__all__ = ["SendResource", "AsyncSendResource"]


class SendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return SendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return SendResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        to: str,
        design: Dict[str, object] | Omit = omit,
        html: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SendCreateResponse:
        """
        Send email with design JSON or HTML content.

        Args:
          project_id: The project ID

          to: Recipient email address

          design: Proprietary design format JSON

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
                    "to": to,
                    "design": design,
                    "html": html,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                send_create_params.SendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, send_create_params.SendCreateParams),
            ),
            cast_to=SendCreateResponse,
        )


class AsyncSendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncSendResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        to: str,
        design: Dict[str, object] | Omit = omit,
        html: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SendCreateResponse:
        """
        Send email with design JSON or HTML content.

        Args:
          project_id: The project ID

          to: Recipient email address

          design: Proprietary design format JSON

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
                    "to": to,
                    "design": design,
                    "html": html,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                send_create_params.SendCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, send_create_params.SendCreateParams),
            ),
            cast_to=SendCreateResponse,
        )


class SendResourceWithRawResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.create = to_raw_response_wrapper(
            send.create,
        )


class AsyncSendResourceWithRawResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.create = async_to_raw_response_wrapper(
            send.create,
        )


class SendResourceWithStreamingResponse:
    def __init__(self, send: SendResource) -> None:
        self._send = send

        self.create = to_streamed_response_wrapper(
            send.create,
        )


class AsyncSendResourceWithStreamingResponse:
    def __init__(self, send: AsyncSendResource) -> None:
        self._send = send

        self.create = async_to_streamed_response_wrapper(
            send.create,
        )
