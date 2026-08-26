# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.emails import suppressions_check_retrieve_params
from ...types.emails.suppressions_check_retrieve_response import SuppressionsCheckRetrieveResponse

__all__ = ["SuppressionsCheckResource", "AsyncSuppressionsCheckResource"]


class SuppressionsCheckResource(SyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def with_raw_response(self) -> SuppressionsCheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return SuppressionsCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuppressionsCheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return SuppressionsCheckResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        email: str,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionsCheckRetrieveResponse:
        """
        Look up a specific email address to see if it is currently on the suppression
        list.

        Args:
          email: Email address to check

          project_id: Project ID (auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/emails/suppressions/check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "project_id": project_id,
                    },
                    suppressions_check_retrieve_params.SuppressionsCheckRetrieveParams,
                ),
            ),
            cast_to=SuppressionsCheckRetrieveResponse,
        )


class AsyncSuppressionsCheckResource(AsyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def with_raw_response(self) -> AsyncSuppressionsCheckResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuppressionsCheckResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuppressionsCheckResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncSuppressionsCheckResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        email: str,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionsCheckRetrieveResponse:
        """
        Look up a specific email address to see if it is currently on the suppression
        list.

        Args:
          email: Email address to check

          project_id: Project ID (auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/emails/suppressions/check",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "project_id": project_id,
                    },
                    suppressions_check_retrieve_params.SuppressionsCheckRetrieveParams,
                ),
            ),
            cast_to=SuppressionsCheckRetrieveResponse,
        )


class SuppressionsCheckResourceWithRawResponse:
    def __init__(self, suppressions_check: SuppressionsCheckResource) -> None:
        self._suppressions_check = suppressions_check

        self.retrieve = to_raw_response_wrapper(
            suppressions_check.retrieve,
        )


class AsyncSuppressionsCheckResourceWithRawResponse:
    def __init__(self, suppressions_check: AsyncSuppressionsCheckResource) -> None:
        self._suppressions_check = suppressions_check

        self.retrieve = async_to_raw_response_wrapper(
            suppressions_check.retrieve,
        )


class SuppressionsCheckResourceWithStreamingResponse:
    def __init__(self, suppressions_check: SuppressionsCheckResource) -> None:
        self._suppressions_check = suppressions_check

        self.retrieve = to_streamed_response_wrapper(
            suppressions_check.retrieve,
        )


class AsyncSuppressionsCheckResourceWithStreamingResponse:
    def __init__(self, suppressions_check: AsyncSuppressionsCheckResource) -> None:
        self._suppressions_check = suppressions_check

        self.retrieve = async_to_streamed_response_wrapper(
            suppressions_check.retrieve,
        )
