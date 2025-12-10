# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import pages_v1_render_create_params
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
from ..types.pages_v1_render_create_response import PagesV1RenderCreateResponse

__all__ = ["PagesV1Resource", "AsyncPagesV1Resource"]


class PagesV1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PagesV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return PagesV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return PagesV1ResourceWithStreamingResponse(self)

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
    ) -> PagesV1RenderCreateResponse:
        """
        Convert page design JSON to HTML with optional merge tags.

        Args:
          design: Proprietary design format JSON

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pages/v1/render",
            body=maybe_transform(
                {
                    "design": design,
                    "merge_tags": merge_tags,
                },
                pages_v1_render_create_params.PagesV1RenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesV1RenderCreateResponse,
        )


class AsyncPagesV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPagesV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncPagesV1ResourceWithStreamingResponse(self)

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
    ) -> PagesV1RenderCreateResponse:
        """
        Convert page design JSON to HTML with optional merge tags.

        Args:
          design: Proprietary design format JSON

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pages/v1/render",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "merge_tags": merge_tags,
                },
                pages_v1_render_create_params.PagesV1RenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PagesV1RenderCreateResponse,
        )


class PagesV1ResourceWithRawResponse:
    def __init__(self, pages_v1: PagesV1Resource) -> None:
        self._pages_v1 = pages_v1

        self.render_create = to_raw_response_wrapper(
            pages_v1.render_create,
        )


class AsyncPagesV1ResourceWithRawResponse:
    def __init__(self, pages_v1: AsyncPagesV1Resource) -> None:
        self._pages_v1 = pages_v1

        self.render_create = async_to_raw_response_wrapper(
            pages_v1.render_create,
        )


class PagesV1ResourceWithStreamingResponse:
    def __init__(self, pages_v1: PagesV1Resource) -> None:
        self._pages_v1 = pages_v1

        self.render_create = to_streamed_response_wrapper(
            pages_v1.render_create,
        )


class AsyncPagesV1ResourceWithStreamingResponse:
    def __init__(self, pages_v1: AsyncPagesV1Resource) -> None:
        self._pages_v1 = pages_v1

        self.render_create = async_to_streamed_response_wrapper(
            pages_v1.render_create,
        )
