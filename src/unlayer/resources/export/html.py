# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
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
from ...types.export import html_retrieve_params
from ...types.export.html_retrieve_response import HTMLRetrieveResponse

__all__ = ["HTMLResource", "AsyncHTMLResource"]


class HTMLResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return HTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return HTMLResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTMLRetrieveResponse:
        """
        Export design to HTML.

        Args:
          project_id: The project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/export/v3/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, html_retrieve_params.HTMLRetrieveParams),
            ),
            cast_to=HTMLRetrieveResponse,
        )


class AsyncHTMLResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncHTMLResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HTMLRetrieveResponse:
        """
        Export design to HTML.

        Args:
          project_id: The project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/export/v3/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, html_retrieve_params.HTMLRetrieveParams),
            ),
            cast_to=HTMLRetrieveResponse,
        )


class HTMLResourceWithRawResponse:
    def __init__(self, html: HTMLResource) -> None:
        self._html = html

        self.retrieve = to_raw_response_wrapper(
            html.retrieve,
        )


class AsyncHTMLResourceWithRawResponse:
    def __init__(self, html: AsyncHTMLResource) -> None:
        self._html = html

        self.retrieve = async_to_raw_response_wrapper(
            html.retrieve,
        )


class HTMLResourceWithStreamingResponse:
    def __init__(self, html: HTMLResource) -> None:
        self._html = html

        self.retrieve = to_streamed_response_wrapper(
            html.retrieve,
        )


class AsyncHTMLResourceWithStreamingResponse:
    def __init__(self, html: AsyncHTMLResource) -> None:
        self._html = html

        self.retrieve = async_to_streamed_response_wrapper(
            html.retrieve,
        )
