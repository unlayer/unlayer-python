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
from ...types.emails import suppression_create_params, suppression_delete_params, suppression_retrieve_params
from ...types.emails.suppression_create_response import SuppressionCreateResponse
from ...types.emails.suppression_delete_response import SuppressionDeleteResponse
from ...types.emails.suppression_retrieve_response import SuppressionRetrieveResponse

__all__ = ["SuppressionsResource", "AsyncSuppressionsResource"]


class SuppressionsResource(SyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def with_raw_response(self) -> SuppressionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return SuppressionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuppressionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return SuppressionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionCreateResponse:
        """Manually add an email address to the suppression list.

        Future sends to this
        address will be blocked.

        Args:
          email: Email address to suppress

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/emails/suppressions",
            body=maybe_transform({"email": email}, suppression_create_params.SuppressionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuppressionCreateResponse,
        )

    def retrieve(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionRetrieveResponse:
        """
        List all email addresses suppressed for this project due to bounces, complaints,
        or manual suppression. Cursor-paginated.

        Args:
          cursor: Pagination cursor from a previous response. Omit to start from the beginning.

          limit: Max number of results (1-200)

          project_id: Project ID (auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/emails/suppressions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "project_id": project_id,
                    },
                    suppression_retrieve_params.SuppressionRetrieveParams,
                ),
            ),
            cast_to=SuppressionRetrieveResponse,
        )

    def delete(
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
    ) -> SuppressionDeleteResponse:
        """
        Remove an email address from the suppression list so it can receive emails
        again.

        Args:
          email: Email address to unsuppress

          project_id: Project ID (auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v3/emails/suppressions",
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
                    suppression_delete_params.SuppressionDeleteParams,
                ),
            ),
            cast_to=SuppressionDeleteResponse,
        )


class AsyncSuppressionsResource(AsyncAPIResource):
    """Send and manage transactional email."""

    @cached_property
    def with_raw_response(self) -> AsyncSuppressionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuppressionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuppressionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncSuppressionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionCreateResponse:
        """Manually add an email address to the suppression list.

        Future sends to this
        address will be blocked.

        Args:
          email: Email address to suppress

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/emails/suppressions",
            body=await async_maybe_transform({"email": email}, suppression_create_params.SuppressionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SuppressionCreateResponse,
        )

    async def retrieve(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SuppressionRetrieveResponse:
        """
        List all email addresses suppressed for this project due to bounces, complaints,
        or manual suppression. Cursor-paginated.

        Args:
          cursor: Pagination cursor from a previous response. Omit to start from the beginning.

          limit: Max number of results (1-200)

          project_id: Project ID (auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/emails/suppressions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "project_id": project_id,
                    },
                    suppression_retrieve_params.SuppressionRetrieveParams,
                ),
            ),
            cast_to=SuppressionRetrieveResponse,
        )

    async def delete(
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
    ) -> SuppressionDeleteResponse:
        """
        Remove an email address from the suppression list so it can receive emails
        again.

        Args:
          email: Email address to unsuppress

          project_id: Project ID (auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v3/emails/suppressions",
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
                    suppression_delete_params.SuppressionDeleteParams,
                ),
            ),
            cast_to=SuppressionDeleteResponse,
        )


class SuppressionsResourceWithRawResponse:
    def __init__(self, suppressions: SuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = to_raw_response_wrapper(
            suppressions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            suppressions.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            suppressions.delete,
        )


class AsyncSuppressionsResourceWithRawResponse:
    def __init__(self, suppressions: AsyncSuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = async_to_raw_response_wrapper(
            suppressions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            suppressions.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            suppressions.delete,
        )


class SuppressionsResourceWithStreamingResponse:
    def __init__(self, suppressions: SuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = to_streamed_response_wrapper(
            suppressions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            suppressions.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            suppressions.delete,
        )


class AsyncSuppressionsResourceWithStreamingResponse:
    def __init__(self, suppressions: AsyncSuppressionsResource) -> None:
        self._suppressions = suppressions

        self.create = async_to_streamed_response_wrapper(
            suppressions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            suppressions.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            suppressions.delete,
        )
