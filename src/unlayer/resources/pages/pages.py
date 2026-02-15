# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .render import (
    RenderResource,
    AsyncRenderResource,
    RenderResourceWithRawResponse,
    AsyncRenderResourceWithRawResponse,
    RenderResourceWithStreamingResponse,
    AsyncRenderResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def render(self) -> RenderResource:
        return RenderResource(self._client)

    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return PagesResourceWithStreamingResponse(self)


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def render(self) -> AsyncRenderResource:
        return AsyncRenderResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncPagesResourceWithStreamingResponse(self)


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

    @cached_property
    def render(self) -> RenderResourceWithRawResponse:
        return RenderResourceWithRawResponse(self._pages.render)


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

    @cached_property
    def render(self) -> AsyncRenderResourceWithRawResponse:
        return AsyncRenderResourceWithRawResponse(self._pages.render)


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

    @cached_property
    def render(self) -> RenderResourceWithStreamingResponse:
        return RenderResourceWithStreamingResponse(self._pages.render)


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

    @cached_property
    def render(self) -> AsyncRenderResourceWithStreamingResponse:
        return AsyncRenderResourceWithStreamingResponse(self._pages.render)
