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
from ...types.projects.ai_credits_settings_rotate_secret_create_response import (
    AICreditsSettingsRotateSecretCreateResponse,
)

__all__ = ["AICreditsSettingsRotateSecretResource", "AsyncAICreditsSettingsRotateSecretResource"]


class AICreditsSettingsRotateSecretResource(SyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AICreditsSettingsRotateSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AICreditsSettingsRotateSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICreditsSettingsRotateSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AICreditsSettingsRotateSecretResourceWithStreamingResponse(self)

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
    ) -> AICreditsSettingsRotateSecretCreateResponse:
        """
        Generates a new HMAC signing secret for the project and returns it exactly once.
        The previous secret stops working immediately, so update your webhook
        verification before rotating. Requires a webhook URL to be configured first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/v3/projects/{id}/ai-credits/settings/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsSettingsRotateSecretCreateResponse,
        )


class AsyncAICreditsSettingsRotateSecretResource(AsyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAICreditsSettingsRotateSecretResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICreditsSettingsRotateSecretResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICreditsSettingsRotateSecretResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncAICreditsSettingsRotateSecretResourceWithStreamingResponse(self)

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
    ) -> AICreditsSettingsRotateSecretCreateResponse:
        """
        Generates a new HMAC signing secret for the project and returns it exactly once.
        The previous secret stops working immediately, so update your webhook
        verification before rotating. Requires a webhook URL to be configured first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/v3/projects/{id}/ai-credits/settings/rotate-secret", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsSettingsRotateSecretCreateResponse,
        )


class AICreditsSettingsRotateSecretResourceWithRawResponse:
    def __init__(self, ai_credits_settings_rotate_secret: AICreditsSettingsRotateSecretResource) -> None:
        self._ai_credits_settings_rotate_secret = ai_credits_settings_rotate_secret

        self.create = to_raw_response_wrapper(
            ai_credits_settings_rotate_secret.create,
        )


class AsyncAICreditsSettingsRotateSecretResourceWithRawResponse:
    def __init__(self, ai_credits_settings_rotate_secret: AsyncAICreditsSettingsRotateSecretResource) -> None:
        self._ai_credits_settings_rotate_secret = ai_credits_settings_rotate_secret

        self.create = async_to_raw_response_wrapper(
            ai_credits_settings_rotate_secret.create,
        )


class AICreditsSettingsRotateSecretResourceWithStreamingResponse:
    def __init__(self, ai_credits_settings_rotate_secret: AICreditsSettingsRotateSecretResource) -> None:
        self._ai_credits_settings_rotate_secret = ai_credits_settings_rotate_secret

        self.create = to_streamed_response_wrapper(
            ai_credits_settings_rotate_secret.create,
        )


class AsyncAICreditsSettingsRotateSecretResourceWithStreamingResponse:
    def __init__(self, ai_credits_settings_rotate_secret: AsyncAICreditsSettingsRotateSecretResource) -> None:
        self._ai_credits_settings_rotate_secret = ai_credits_settings_rotate_secret

        self.create = async_to_streamed_response_wrapper(
            ai_credits_settings_rotate_secret.create,
        )
