# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.webhooks.rotate_secret_create_response import RotateSecretCreateResponse

__all__ = ["RotateSecretResource", "AsyncRotateSecretResource"]


class RotateSecretResource(SyncAPIResource):
    """Manage Developer Email API webhooks."""

    @cached_property
    def with_raw_response(self) -> RotateSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return RotateSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RotateSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return RotateSecretResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotateSecretCreateResponse:
        """Generate a new signing secret for a webhook.

        The new secret is returned once —
        store it securely. The old secret is invalidated immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v3/webhooks/{id}/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RotateSecretCreateResponse,
        )


class AsyncRotateSecretResource(AsyncAPIResource):
    """Manage Developer Email API webhooks."""

    @cached_property
    def with_raw_response(self) -> AsyncRotateSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRotateSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRotateSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncRotateSecretResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RotateSecretCreateResponse:
        """Generate a new signing secret for a webhook.

        The new secret is returned once —
        store it securely. The old secret is invalidated immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v3/webhooks/{id}/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RotateSecretCreateResponse,
        )


class RotateSecretResourceWithRawResponse:
    def __init__(self, rotate_secret: RotateSecretResource) -> None:
        self._rotate_secret = rotate_secret

        self.create = to_raw_response_wrapper(
            rotate_secret.create,
        )


class AsyncRotateSecretResourceWithRawResponse:
    def __init__(self, rotate_secret: AsyncRotateSecretResource) -> None:
        self._rotate_secret = rotate_secret

        self.create = async_to_raw_response_wrapper(
            rotate_secret.create,
        )


class RotateSecretResourceWithStreamingResponse:
    def __init__(self, rotate_secret: RotateSecretResource) -> None:
        self._rotate_secret = rotate_secret

        self.create = to_streamed_response_wrapper(
            rotate_secret.create,
        )


class AsyncRotateSecretResourceWithStreamingResponse:
    def __init__(self, rotate_secret: AsyncRotateSecretResource) -> None:
        self._rotate_secret = rotate_secret

        self.create = async_to_streamed_response_wrapper(
            rotate_secret.create,
        )
