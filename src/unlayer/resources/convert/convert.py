# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .full_to_simple import (
    FullToSimpleResource,
    AsyncFullToSimpleResource,
    FullToSimpleResourceWithRawResponse,
    AsyncFullToSimpleResourceWithRawResponse,
    FullToSimpleResourceWithStreamingResponse,
    AsyncFullToSimpleResourceWithStreamingResponse,
)
from .simple_to_full import (
    SimpleToFullResource,
    AsyncSimpleToFullResource,
    SimpleToFullResourceWithRawResponse,
    AsyncSimpleToFullResourceWithRawResponse,
    SimpleToFullResourceWithStreamingResponse,
    AsyncSimpleToFullResourceWithStreamingResponse,
)

__all__ = ["ConvertResource", "AsyncConvertResource"]


class ConvertResource(SyncAPIResource):
    @cached_property
    def full_to_simple(self) -> FullToSimpleResource:
        """Design schema conversion between Full and Simple formats."""
        return FullToSimpleResource(self._client)

    @cached_property
    def simple_to_full(self) -> SimpleToFullResource:
        """Design schema conversion between Full and Simple formats."""
        return SimpleToFullResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConvertResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ConvertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConvertResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ConvertResourceWithStreamingResponse(self)


class AsyncConvertResource(AsyncAPIResource):
    @cached_property
    def full_to_simple(self) -> AsyncFullToSimpleResource:
        """Design schema conversion between Full and Simple formats."""
        return AsyncFullToSimpleResource(self._client)

    @cached_property
    def simple_to_full(self) -> AsyncSimpleToFullResource:
        """Design schema conversion between Full and Simple formats."""
        return AsyncSimpleToFullResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConvertResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConvertResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConvertResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncConvertResourceWithStreamingResponse(self)


class ConvertResourceWithRawResponse:
    def __init__(self, convert: ConvertResource) -> None:
        self._convert = convert

    @cached_property
    def full_to_simple(self) -> FullToSimpleResourceWithRawResponse:
        """Design schema conversion between Full and Simple formats."""
        return FullToSimpleResourceWithRawResponse(self._convert.full_to_simple)

    @cached_property
    def simple_to_full(self) -> SimpleToFullResourceWithRawResponse:
        """Design schema conversion between Full and Simple formats."""
        return SimpleToFullResourceWithRawResponse(self._convert.simple_to_full)


class AsyncConvertResourceWithRawResponse:
    def __init__(self, convert: AsyncConvertResource) -> None:
        self._convert = convert

    @cached_property
    def full_to_simple(self) -> AsyncFullToSimpleResourceWithRawResponse:
        """Design schema conversion between Full and Simple formats."""
        return AsyncFullToSimpleResourceWithRawResponse(self._convert.full_to_simple)

    @cached_property
    def simple_to_full(self) -> AsyncSimpleToFullResourceWithRawResponse:
        """Design schema conversion between Full and Simple formats."""
        return AsyncSimpleToFullResourceWithRawResponse(self._convert.simple_to_full)


class ConvertResourceWithStreamingResponse:
    def __init__(self, convert: ConvertResource) -> None:
        self._convert = convert

    @cached_property
    def full_to_simple(self) -> FullToSimpleResourceWithStreamingResponse:
        """Design schema conversion between Full and Simple formats."""
        return FullToSimpleResourceWithStreamingResponse(self._convert.full_to_simple)

    @cached_property
    def simple_to_full(self) -> SimpleToFullResourceWithStreamingResponse:
        """Design schema conversion between Full and Simple formats."""
        return SimpleToFullResourceWithStreamingResponse(self._convert.simple_to_full)


class AsyncConvertResourceWithStreamingResponse:
    def __init__(self, convert: AsyncConvertResource) -> None:
        self._convert = convert

    @cached_property
    def full_to_simple(self) -> AsyncFullToSimpleResourceWithStreamingResponse:
        """Design schema conversion between Full and Simple formats."""
        return AsyncFullToSimpleResourceWithStreamingResponse(self._convert.full_to_simple)

    @cached_property
    def simple_to_full(self) -> AsyncSimpleToFullResourceWithStreamingResponse:
        """Design schema conversion between Full and Simple formats."""
        return AsyncSimpleToFullResourceWithStreamingResponse(self._convert.simple_to_full)
