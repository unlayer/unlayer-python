# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.convert import simple_to_full_create_params
from ...types.convert.simple_to_full_create_response import SimpleToFullCreateResponse

__all__ = ["SimpleToFullResource", "AsyncSimpleToFullResource"]


class SimpleToFullResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimpleToFullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return SimpleToFullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimpleToFullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return SimpleToFullResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: simple_to_full_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleToFullCreateResponse:
        """
        Convert design json from Simple to Full schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/convert/simple-to-full",
            body=maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_default_values": include_default_values,
                },
                simple_to_full_create_params.SimpleToFullCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleToFullCreateResponse,
        )


class AsyncSimpleToFullResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimpleToFullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimpleToFullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimpleToFullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncSimpleToFullResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: simple_to_full_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimpleToFullCreateResponse:
        """
        Convert design json from Simple to Full schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/convert/simple-to-full",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_default_values": include_default_values,
                },
                simple_to_full_create_params.SimpleToFullCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimpleToFullCreateResponse,
        )


class SimpleToFullResourceWithRawResponse:
    def __init__(self, simple_to_full: SimpleToFullResource) -> None:
        self._simple_to_full = simple_to_full

        self.create = to_raw_response_wrapper(
            simple_to_full.create,
        )


class AsyncSimpleToFullResourceWithRawResponse:
    def __init__(self, simple_to_full: AsyncSimpleToFullResource) -> None:
        self._simple_to_full = simple_to_full

        self.create = async_to_raw_response_wrapper(
            simple_to_full.create,
        )


class SimpleToFullResourceWithStreamingResponse:
    def __init__(self, simple_to_full: SimpleToFullResource) -> None:
        self._simple_to_full = simple_to_full

        self.create = to_streamed_response_wrapper(
            simple_to_full.create,
        )


class AsyncSimpleToFullResourceWithStreamingResponse:
    def __init__(self, simple_to_full: AsyncSimpleToFullResource) -> None:
        self._simple_to_full = simple_to_full

        self.create = async_to_streamed_response_wrapper(
            simple_to_full.create,
        )
