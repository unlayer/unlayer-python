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
from ...types.convert import full_to_simple_create_params
from ...types.convert.full_to_simple_create_response import FullToSimpleCreateResponse

__all__ = ["FullToSimpleResource", "AsyncFullToSimpleResource"]


class FullToSimpleResource(SyncAPIResource):
    """Design schema conversion between Full and Simple formats."""

    @cached_property
    def with_raw_response(self) -> FullToSimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return FullToSimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FullToSimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return FullToSimpleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: full_to_simple_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_conversion: bool | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FullToSimpleCreateResponse:
        """
        Convert design json from Full to Simple schema.

        Args:
          include_conversion: When true, includes \\__conversion metadata in the response. This metadata can be
              passed to simple-to-full to restore original values without data loss.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/convert/full-to-simple",
            body=maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_conversion": include_conversion,
                    "include_default_values": include_default_values,
                },
                full_to_simple_create_params.FullToSimpleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FullToSimpleCreateResponse,
        )


class AsyncFullToSimpleResource(AsyncAPIResource):
    """Design schema conversion between Full and Simple formats."""

    @cached_property
    def with_raw_response(self) -> AsyncFullToSimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFullToSimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFullToSimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncFullToSimpleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: full_to_simple_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_conversion: bool | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FullToSimpleCreateResponse:
        """
        Convert design json from Full to Simple schema.

        Args:
          include_conversion: When true, includes \\__conversion metadata in the response. This metadata can be
              passed to simple-to-full to restore original values without data loss.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/convert/full-to-simple",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_conversion": include_conversion,
                    "include_default_values": include_default_values,
                },
                full_to_simple_create_params.FullToSimpleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FullToSimpleCreateResponse,
        )


class FullToSimpleResourceWithRawResponse:
    def __init__(self, full_to_simple: FullToSimpleResource) -> None:
        self._full_to_simple = full_to_simple

        self.create = to_raw_response_wrapper(
            full_to_simple.create,
        )


class AsyncFullToSimpleResourceWithRawResponse:
    def __init__(self, full_to_simple: AsyncFullToSimpleResource) -> None:
        self._full_to_simple = full_to_simple

        self.create = async_to_raw_response_wrapper(
            full_to_simple.create,
        )


class FullToSimpleResourceWithStreamingResponse:
    def __init__(self, full_to_simple: FullToSimpleResource) -> None:
        self._full_to_simple = full_to_simple

        self.create = to_streamed_response_wrapper(
            full_to_simple.create,
        )


class AsyncFullToSimpleResourceWithStreamingResponse:
    def __init__(self, full_to_simple: AsyncFullToSimpleResource) -> None:
        self._full_to_simple = full_to_simple

        self.create = async_to_streamed_response_wrapper(
            full_to_simple.create,
        )
