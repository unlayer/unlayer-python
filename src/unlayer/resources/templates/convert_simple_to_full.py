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
from ...types.templates import convert_simple_to_full_create_params
from ...types.templates.convert_simple_to_full_create_response import ConvertSimpleToFullCreateResponse

__all__ = ["ConvertSimpleToFullResource", "AsyncConvertSimpleToFullResource"]


class ConvertSimpleToFullResource(SyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> ConvertSimpleToFullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ConvertSimpleToFullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConvertSimpleToFullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ConvertSimpleToFullResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: convert_simple_to_full_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConvertSimpleToFullCreateResponse:
        """
        Convert design json from Simple to Full schema.

        Args:
          display_mode: Display mode of the design (email, web, document, popup). Defaults to "email",
              matching /v3/templates/validate. Mode-specific repairs apply during conversion
              (email caps contentWidth at 900px, for example), so pass the design's actual
              mode — a web design converted under the email default can be altered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/templates/convert/simple-to-full",
            body=maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_default_values": include_default_values,
                },
                convert_simple_to_full_create_params.ConvertSimpleToFullCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConvertSimpleToFullCreateResponse,
        )


class AsyncConvertSimpleToFullResource(AsyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncConvertSimpleToFullResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConvertSimpleToFullResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConvertSimpleToFullResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncConvertSimpleToFullResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: convert_simple_to_full_create_params.Design,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_default_values: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConvertSimpleToFullCreateResponse:
        """
        Convert design json from Simple to Full schema.

        Args:
          display_mode: Display mode of the design (email, web, document, popup). Defaults to "email",
              matching /v3/templates/validate. Mode-specific repairs apply during conversion
              (email caps contentWidth at 900px, for example), so pass the design's actual
              mode — a web design converted under the email default can be altered.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/templates/convert/simple-to-full",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                    "include_default_values": include_default_values,
                },
                convert_simple_to_full_create_params.ConvertSimpleToFullCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConvertSimpleToFullCreateResponse,
        )


class ConvertSimpleToFullResourceWithRawResponse:
    def __init__(self, convert_simple_to_full: ConvertSimpleToFullResource) -> None:
        self._convert_simple_to_full = convert_simple_to_full

        self.create = to_raw_response_wrapper(
            convert_simple_to_full.create,
        )


class AsyncConvertSimpleToFullResourceWithRawResponse:
    def __init__(self, convert_simple_to_full: AsyncConvertSimpleToFullResource) -> None:
        self._convert_simple_to_full = convert_simple_to_full

        self.create = async_to_raw_response_wrapper(
            convert_simple_to_full.create,
        )


class ConvertSimpleToFullResourceWithStreamingResponse:
    def __init__(self, convert_simple_to_full: ConvertSimpleToFullResource) -> None:
        self._convert_simple_to_full = convert_simple_to_full

        self.create = to_streamed_response_wrapper(
            convert_simple_to_full.create,
        )


class AsyncConvertSimpleToFullResourceWithStreamingResponse:
    def __init__(self, convert_simple_to_full: AsyncConvertSimpleToFullResource) -> None:
        self._convert_simple_to_full = convert_simple_to_full

        self.create = async_to_streamed_response_wrapper(
            convert_simple_to_full.create,
        )
