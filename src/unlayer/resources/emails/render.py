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
from ...types.emails import render_create_params
from ...types.emails.render_create_response import RenderCreateResponse

__all__ = ["RenderResource", "AsyncRenderResource"]


class RenderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RenderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return RenderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RenderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return RenderResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        design: Dict[str, object],
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RenderCreateResponse:
        """
        Convert design JSON to HTML with optional merge tags.

        Args:
          project_id: The project ID

          design: Proprietary design format JSON

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/emails/v1/render",
            body=maybe_transform(
                {
                    "design": design,
                    "merge_tags": merge_tags,
                },
                render_create_params.RenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, render_create_params.RenderCreateParams),
            ),
            cast_to=RenderCreateResponse,
        )


class AsyncRenderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRenderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRenderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRenderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncRenderResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        design: Dict[str, object],
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RenderCreateResponse:
        """
        Convert design JSON to HTML with optional merge tags.

        Args:
          project_id: The project ID

          design: Proprietary design format JSON

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/emails/v1/render",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "merge_tags": merge_tags,
                },
                render_create_params.RenderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, render_create_params.RenderCreateParams),
            ),
            cast_to=RenderCreateResponse,
        )


class RenderResourceWithRawResponse:
    def __init__(self, render: RenderResource) -> None:
        self._render = render

        self.create = to_raw_response_wrapper(
            render.create,
        )


class AsyncRenderResourceWithRawResponse:
    def __init__(self, render: AsyncRenderResource) -> None:
        self._render = render

        self.create = async_to_raw_response_wrapper(
            render.create,
        )


class RenderResourceWithStreamingResponse:
    def __init__(self, render: RenderResource) -> None:
        self._render = render

        self.create = to_streamed_response_wrapper(
            render.create,
        )


class AsyncRenderResourceWithStreamingResponse:
    def __init__(self, render: AsyncRenderResource) -> None:
        self._render = render

        self.create = async_to_streamed_response_wrapper(
            render.create,
        )
