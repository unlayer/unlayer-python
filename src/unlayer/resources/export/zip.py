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
from ...types.export import zip_retrieve_params
from ...types.export.zip_retrieve_response import ZipRetrieveResponse

__all__ = ["ZipResource", "AsyncZipResource"]


class ZipResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ZipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ZipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ZipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return ZipResourceWithStreamingResponse(self)

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
    ) -> ZipRetrieveResponse:
        """
        Export design to ZIP archive.

        Args:
          project_id: The project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/export/v3/zip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, zip_retrieve_params.ZipRetrieveParams),
            ),
            cast_to=ZipRetrieveResponse,
        )


class AsyncZipResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncZipResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncZipResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncZipResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncZipResourceWithStreamingResponse(self)

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
    ) -> ZipRetrieveResponse:
        """
        Export design to ZIP archive.

        Args:
          project_id: The project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/export/v3/zip",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, zip_retrieve_params.ZipRetrieveParams),
            ),
            cast_to=ZipRetrieveResponse,
        )


class ZipResourceWithRawResponse:
    def __init__(self, zip: ZipResource) -> None:
        self._zip = zip

        self.retrieve = to_raw_response_wrapper(
            zip.retrieve,
        )


class AsyncZipResourceWithRawResponse:
    def __init__(self, zip: AsyncZipResource) -> None:
        self._zip = zip

        self.retrieve = async_to_raw_response_wrapper(
            zip.retrieve,
        )


class ZipResourceWithStreamingResponse:
    def __init__(self, zip: ZipResource) -> None:
        self._zip = zip

        self.retrieve = to_streamed_response_wrapper(
            zip.retrieve,
        )


class AsyncZipResourceWithStreamingResponse:
    def __init__(self, zip: AsyncZipResource) -> None:
        self._zip = zip

        self.retrieve = async_to_streamed_response_wrapper(
            zip.retrieve,
        )
