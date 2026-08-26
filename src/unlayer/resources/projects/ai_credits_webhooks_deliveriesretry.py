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
from ...types.projects.ai_credits_webhooks_deliveriesretry_create_response import (
    AICreditsWebhooksDeliveriesretryCreateResponse,
)

__all__ = ["AICreditsWebhooksDeliveriesretryResource", "AsyncAICreditsWebhooksDeliveriesretryResource"]


class AICreditsWebhooksDeliveriesretryResource(SyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AICreditsWebhooksDeliveriesretryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AICreditsWebhooksDeliveriesretryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICreditsWebhooksDeliveriesretryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AICreditsWebhooksDeliveriesretryResourceWithStreamingResponse(self)

    def create(
        self,
        delivery_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsWebhooksDeliveriesretryCreateResponse:
        """
        Re-queues a single previously-failed (or pending) webhook delivery for another
        attempt. Returns 404 if the delivery is not found for this project, and 409 if
        it was already delivered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._post(
            path_template(
                "/v3/projects/{id}/ai-credits/webhooks/deliveries/{delivery_id}/retry", id=id, delivery_id=delivery_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsWebhooksDeliveriesretryCreateResponse,
        )


class AsyncAICreditsWebhooksDeliveriesretryResource(AsyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAICreditsWebhooksDeliveriesretryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICreditsWebhooksDeliveriesretryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICreditsWebhooksDeliveriesretryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncAICreditsWebhooksDeliveriesretryResourceWithStreamingResponse(self)

    async def create(
        self,
        delivery_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsWebhooksDeliveriesretryCreateResponse:
        """
        Re-queues a single previously-failed (or pending) webhook delivery for another
        attempt. Returns 404 if the delivery is not found for this project, and 409 if
        it was already delivered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._post(
            path_template(
                "/v3/projects/{id}/ai-credits/webhooks/deliveries/{delivery_id}/retry", id=id, delivery_id=delivery_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditsWebhooksDeliveriesretryCreateResponse,
        )


class AICreditsWebhooksDeliveriesretryResourceWithRawResponse:
    def __init__(self, ai_credits_webhooks_deliveriesretry: AICreditsWebhooksDeliveriesretryResource) -> None:
        self._ai_credits_webhooks_deliveriesretry = ai_credits_webhooks_deliveriesretry

        self.create = to_raw_response_wrapper(
            ai_credits_webhooks_deliveriesretry.create,
        )


class AsyncAICreditsWebhooksDeliveriesretryResourceWithRawResponse:
    def __init__(self, ai_credits_webhooks_deliveriesretry: AsyncAICreditsWebhooksDeliveriesretryResource) -> None:
        self._ai_credits_webhooks_deliveriesretry = ai_credits_webhooks_deliveriesretry

        self.create = async_to_raw_response_wrapper(
            ai_credits_webhooks_deliveriesretry.create,
        )


class AICreditsWebhooksDeliveriesretryResourceWithStreamingResponse:
    def __init__(self, ai_credits_webhooks_deliveriesretry: AICreditsWebhooksDeliveriesretryResource) -> None:
        self._ai_credits_webhooks_deliveriesretry = ai_credits_webhooks_deliveriesretry

        self.create = to_streamed_response_wrapper(
            ai_credits_webhooks_deliveriesretry.create,
        )


class AsyncAICreditsWebhooksDeliveriesretryResourceWithStreamingResponse:
    def __init__(self, ai_credits_webhooks_deliveriesretry: AsyncAICreditsWebhooksDeliveriesretryResource) -> None:
        self._ai_credits_webhooks_deliveriesretry = ai_credits_webhooks_deliveriesretry

        self.create = async_to_streamed_response_wrapper(
            ai_credits_webhooks_deliveriesretry.create,
        )
