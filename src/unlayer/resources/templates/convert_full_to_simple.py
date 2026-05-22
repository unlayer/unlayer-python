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
from ...types.templates import convert_full_to_simple_create_params
from ...types.templates.convert_full_to_simple_create_response import ConvertFullToSimpleCreateResponse

__all__ = ["ConvertFullToSimpleResource", "AsyncConvertFullToSimpleResource"]


class ConvertFullToSimpleResource(SyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> ConvertFullToSimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ConvertFullToSimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConvertFullToSimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ConvertFullToSimpleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: convert_full_to_simple_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_conversion: bool | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConvertFullToSimpleCreateResponse:
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
            "/v3/templates/convert/full-to-simple",
            body=maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_conversion": include_conversion,
                    "include_default_values": include_default_values,
                },
                convert_full_to_simple_create_params.ConvertFullToSimpleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConvertFullToSimpleCreateResponse,
        )


class AsyncConvertFullToSimpleResource(AsyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncConvertFullToSimpleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConvertFullToSimpleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConvertFullToSimpleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncConvertFullToSimpleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: convert_full_to_simple_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_conversion: bool | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConvertFullToSimpleCreateResponse:
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
            "/v3/templates/convert/full-to-simple",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_conversion": include_conversion,
                    "include_default_values": include_default_values,
                },
                convert_full_to_simple_create_params.ConvertFullToSimpleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConvertFullToSimpleCreateResponse,
        )


class ConvertFullToSimpleResourceWithRawResponse:
    def __init__(self, convert_full_to_simple: ConvertFullToSimpleResource) -> None:
        self._convert_full_to_simple = convert_full_to_simple

        self.create = to_raw_response_wrapper(
            convert_full_to_simple.create,
        )


class AsyncConvertFullToSimpleResourceWithRawResponse:
    def __init__(self, convert_full_to_simple: AsyncConvertFullToSimpleResource) -> None:
        self._convert_full_to_simple = convert_full_to_simple

        self.create = async_to_raw_response_wrapper(
            convert_full_to_simple.create,
        )


class ConvertFullToSimpleResourceWithStreamingResponse:
    def __init__(self, convert_full_to_simple: ConvertFullToSimpleResource) -> None:
        self._convert_full_to_simple = convert_full_to_simple

        self.create = to_streamed_response_wrapper(
            convert_full_to_simple.create,
        )


class AsyncConvertFullToSimpleResourceWithStreamingResponse:
    def __init__(self, convert_full_to_simple: AsyncConvertFullToSimpleResource) -> None:
        self._convert_full_to_simple = convert_full_to_simple

        self.create = async_to_streamed_response_wrapper(
            convert_full_to_simple.create,
        )
