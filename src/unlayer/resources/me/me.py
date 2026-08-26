# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .subscription import (
    SubscriptionResource,
    AsyncSubscriptionResource,
    SubscriptionResourceWithRawResponse,
    AsyncSubscriptionResourceWithRawResponse,
    SubscriptionResourceWithStreamingResponse,
    AsyncSubscriptionResourceWithStreamingResponse,
)

__all__ = ["MeResource", "AsyncMeResource"]


class MeResource(SyncAPIResource):
    @cached_property
    def subscription(self) -> SubscriptionResource:
        """Current user and token context."""
        return SubscriptionResource(self._client)

    @cached_property
    def with_raw_response(self) -> MeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return MeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return MeResourceWithStreamingResponse(self)


class AsyncMeResource(AsyncAPIResource):
    @cached_property
    def subscription(self) -> AsyncSubscriptionResource:
        """Current user and token context."""
        return AsyncSubscriptionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncMeResourceWithStreamingResponse(self)


class MeResourceWithRawResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

    @cached_property
    def subscription(self) -> SubscriptionResourceWithRawResponse:
        """Current user and token context."""
        return SubscriptionResourceWithRawResponse(self._me.subscription)


class AsyncMeResourceWithRawResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithRawResponse:
        """Current user and token context."""
        return AsyncSubscriptionResourceWithRawResponse(self._me.subscription)


class MeResourceWithStreamingResponse:
    def __init__(self, me: MeResource) -> None:
        self._me = me

    @cached_property
    def subscription(self) -> SubscriptionResourceWithStreamingResponse:
        """Current user and token context."""
        return SubscriptionResourceWithStreamingResponse(self._me.subscription)


class AsyncMeResourceWithStreamingResponse:
    def __init__(self, me: AsyncMeResource) -> None:
        self._me = me

    @cached_property
    def subscription(self) -> AsyncSubscriptionResourceWithStreamingResponse:
        """Current user and token context."""
        return AsyncSubscriptionResourceWithStreamingResponse(self._me.subscription)
