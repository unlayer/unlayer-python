# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.projects import ai_credits_setting_update_params
from ...types.projects.ai_credits_setting_update_response import AICreditsSettingUpdateResponse
from ...types.projects.ai_credits_setting_retrieve_response import AICreditsSettingRetrieveResponse

__all__ = ["AICreditsSettingsResource", "AsyncAICreditsSettingsResource"]


class AICreditsSettingsResource(SyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AICreditsSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AICreditsSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICreditsSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AICreditsSettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsSettingRetrieveResponse:
        """
        Returns a project's AI credit exhaustion behavior, alert thresholds, and webhook
        endpoint. The signing secret is never returned — only whether one exists
        (`has_signing_secret`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/projects/{id}/ai-credits/settings", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsSettingRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        exhaustion_behavior: Literal["disable", "show_error"] | Omit = omit,
        threshold_alerts: Iterable[int] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsSettingUpdateResponse:
        """
        Configures AI credit exhaustion behavior, usage alert thresholds, and the
        webhook endpoint for a project. The HMAC signing secret is generated the first
        time a webhook URL is set and returned exactly once in the response — store it
        securely; it is never shown again.

        Args:
          exhaustion_behavior: What the editor does when the credit balance is exhausted.

          threshold_alerts: Usage percentages (1-100) at which a threshold_reached webhook fires, once per
              crossing per period.

          webhook_url: HTTPS endpoint that receives AI credit webhooks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/v3/projects/{id}/ai-credits/settings", id=id),
            body=maybe_transform(
                {
                    "exhaustion_behavior": exhaustion_behavior,
                    "threshold_alerts": threshold_alerts,
                    "webhook_url": webhook_url,
                },
                ai_credits_setting_update_params.AICreditsSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsSettingUpdateResponse,
        )


class AsyncAICreditsSettingsResource(AsyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAICreditsSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICreditsSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICreditsSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncAICreditsSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsSettingRetrieveResponse:
        """
        Returns a project's AI credit exhaustion behavior, alert thresholds, and webhook
        endpoint. The signing secret is never returned — only whether one exists
        (`has_signing_secret`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/projects/{id}/ai-credits/settings", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsSettingRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        exhaustion_behavior: Literal["disable", "show_error"] | Omit = omit,
        threshold_alerts: Iterable[int] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsSettingUpdateResponse:
        """
        Configures AI credit exhaustion behavior, usage alert thresholds, and the
        webhook endpoint for a project. The HMAC signing secret is generated the first
        time a webhook URL is set and returned exactly once in the response — store it
        securely; it is never shown again.

        Args:
          exhaustion_behavior: What the editor does when the credit balance is exhausted.

          threshold_alerts: Usage percentages (1-100) at which a threshold_reached webhook fires, once per
              crossing per period.

          webhook_url: HTTPS endpoint that receives AI credit webhooks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/v3/projects/{id}/ai-credits/settings", id=id),
            body=await async_maybe_transform(
                {
                    "exhaustion_behavior": exhaustion_behavior,
                    "threshold_alerts": threshold_alerts,
                    "webhook_url": webhook_url,
                },
                ai_credits_setting_update_params.AICreditsSettingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsSettingUpdateResponse,
        )


class AICreditsSettingsResourceWithRawResponse:
    def __init__(self, ai_credits_settings: AICreditsSettingsResource) -> None:
        self._ai_credits_settings = ai_credits_settings

        self.retrieve = to_raw_response_wrapper(
            ai_credits_settings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            ai_credits_settings.update,
        )


class AsyncAICreditsSettingsResourceWithRawResponse:
    def __init__(self, ai_credits_settings: AsyncAICreditsSettingsResource) -> None:
        self._ai_credits_settings = ai_credits_settings

        self.retrieve = async_to_raw_response_wrapper(
            ai_credits_settings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            ai_credits_settings.update,
        )


class AICreditsSettingsResourceWithStreamingResponse:
    def __init__(self, ai_credits_settings: AICreditsSettingsResource) -> None:
        self._ai_credits_settings = ai_credits_settings

        self.retrieve = to_streamed_response_wrapper(
            ai_credits_settings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            ai_credits_settings.update,
        )


class AsyncAICreditsSettingsResourceWithStreamingResponse:
    def __init__(self, ai_credits_settings: AsyncAICreditsSettingsResource) -> None:
        self._ai_credits_settings = ai_credits_settings

        self.retrieve = async_to_streamed_response_wrapper(
            ai_credits_settings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            ai_credits_settings.update,
        )
