# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.projects import ai_credits_webhooks_delivery_retrieve_params
from ...types.projects.ai_credits_webhooks_delivery_retrieve_response import AICreditsWebhooksDeliveryRetrieveResponse

__all__ = ["AICreditsWebhooksDeliveriesResource", "AsyncAICreditsWebhooksDeliveriesResource"]


class AICreditsWebhooksDeliveriesResource(SyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AICreditsWebhooksDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AICreditsWebhooksDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICreditsWebhooksDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AICreditsWebhooksDeliveriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        event: Literal["ai.credits.usage_recorded", "ai.credits.threshold_reached", "ai.credits.exhausted"]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["pending", "delivered", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsWebhooksDeliveryRetrieveResponse:
        """
        Returns the webhook delivery history for the project, newest first — the event,
        delivery status, attempt count, and last response code for each. Use it to spot
        failed deliveries and drive the retry endpoint. Payloads expose credits only.

        Args:
          event: Filter to a single event type.

          limit: Max deliveries to return (1-100).

          offset: Number of deliveries to skip (pagination).

          status: Filter to a single delivery status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/projects/{id}/ai-credits/webhooks/deliveries", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "event": event,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    ai_credits_webhooks_delivery_retrieve_params.AICreditsWebhooksDeliveryRetrieveParams,
                ),
            ),
            cast_to=AICreditsWebhooksDeliveryRetrieveResponse,
        )


class AsyncAICreditsWebhooksDeliveriesResource(AsyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAICreditsWebhooksDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICreditsWebhooksDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICreditsWebhooksDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncAICreditsWebhooksDeliveriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        event: Literal["ai.credits.usage_recorded", "ai.credits.threshold_reached", "ai.credits.exhausted"]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: Literal["pending", "delivered", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsWebhooksDeliveryRetrieveResponse:
        """
        Returns the webhook delivery history for the project, newest first — the event,
        delivery status, attempt count, and last response code for each. Use it to spot
        failed deliveries and drive the retry endpoint. Payloads expose credits only.

        Args:
          event: Filter to a single event type.

          limit: Max deliveries to return (1-100).

          offset: Number of deliveries to skip (pagination).

          status: Filter to a single delivery status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/projects/{id}/ai-credits/webhooks/deliveries", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "event": event,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    ai_credits_webhooks_delivery_retrieve_params.AICreditsWebhooksDeliveryRetrieveParams,
                ),
            ),
            cast_to=AICreditsWebhooksDeliveryRetrieveResponse,
        )


class AICreditsWebhooksDeliveriesResourceWithRawResponse:
    def __init__(self, ai_credits_webhooks_deliveries: AICreditsWebhooksDeliveriesResource) -> None:
        self._ai_credits_webhooks_deliveries = ai_credits_webhooks_deliveries

        self.retrieve = to_raw_response_wrapper(
            ai_credits_webhooks_deliveries.retrieve,
        )


class AsyncAICreditsWebhooksDeliveriesResourceWithRawResponse:
    def __init__(self, ai_credits_webhooks_deliveries: AsyncAICreditsWebhooksDeliveriesResource) -> None:
        self._ai_credits_webhooks_deliveries = ai_credits_webhooks_deliveries

        self.retrieve = async_to_raw_response_wrapper(
            ai_credits_webhooks_deliveries.retrieve,
        )


class AICreditsWebhooksDeliveriesResourceWithStreamingResponse:
    def __init__(self, ai_credits_webhooks_deliveries: AICreditsWebhooksDeliveriesResource) -> None:
        self._ai_credits_webhooks_deliveries = ai_credits_webhooks_deliveries

        self.retrieve = to_streamed_response_wrapper(
            ai_credits_webhooks_deliveries.retrieve,
        )


class AsyncAICreditsWebhooksDeliveriesResourceWithStreamingResponse:
    def __init__(self, ai_credits_webhooks_deliveries: AsyncAICreditsWebhooksDeliveriesResource) -> None:
        self._ai_credits_webhooks_deliveries = ai_credits_webhooks_deliveries

        self.retrieve = async_to_streamed_response_wrapper(
            ai_credits_webhooks_deliveries.retrieve,
        )
