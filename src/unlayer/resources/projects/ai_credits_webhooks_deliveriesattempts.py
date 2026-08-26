# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.projects import ai_credits_webhooks_deliveriesattempt_retrieve_params
from ...types.projects.ai_credits_webhooks_deliveriesattempt_retrieve_response import (
    AICreditsWebhooksDeliveriesattemptRetrieveResponse,
)

__all__ = ["AICreditsWebhooksDeliveriesattemptsResource", "AsyncAICreditsWebhooksDeliveriesattemptsResource"]


class AICreditsWebhooksDeliveriesattemptsResource(SyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AICreditsWebhooksDeliveriesattemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AICreditsWebhooksDeliveriesattemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        delivery_id: str,
        *,
        id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsWebhooksDeliveriesattemptRetrieveResponse:
        """
        Returns the per-attempt history for a single delivery, newest attempt first —
        the response code, error, and time of each POST (including automatic retries).
        Returns 404 if the delivery is not found for this project.

        Args:
          limit: Max attempts to return (1-100).

          offset: Number of attempts to skip (pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._get(
            path_template(
                "/v3/projects/{id}/ai-credits/webhooks/deliveries/{delivery_id}/attempts",
                id=id,
                delivery_id=delivery_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    ai_credits_webhooks_deliveriesattempt_retrieve_params.AICreditsWebhooksDeliveriesattemptRetrieveParams,
                ),
            ),
            cast_to=AICreditsWebhooksDeliveriesattemptRetrieveResponse,
        )


class AsyncAICreditsWebhooksDeliveriesattemptsResource(AsyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAICreditsWebhooksDeliveriesattemptsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICreditsWebhooksDeliveriesattemptsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncAICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        delivery_id: str,
        *,
        id: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsWebhooksDeliveriesattemptRetrieveResponse:
        """
        Returns the per-attempt history for a single delivery, newest attempt first —
        the response code, error, and time of each POST (including automatic retries).
        Returns 404 if the delivery is not found for this project.

        Args:
          limit: Max attempts to return (1-100).

          offset: Number of attempts to skip (pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._get(
            path_template(
                "/v3/projects/{id}/ai-credits/webhooks/deliveries/{delivery_id}/attempts",
                id=id,
                delivery_id=delivery_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    ai_credits_webhooks_deliveriesattempt_retrieve_params.AICreditsWebhooksDeliveriesattemptRetrieveParams,
                ),
            ),
            cast_to=AICreditsWebhooksDeliveriesattemptRetrieveResponse,
        )


class AICreditsWebhooksDeliveriesattemptsResourceWithRawResponse:
    def __init__(self, ai_credits_webhooks_deliveriesattempts: AICreditsWebhooksDeliveriesattemptsResource) -> None:
        self._ai_credits_webhooks_deliveriesattempts = ai_credits_webhooks_deliveriesattempts

        self.retrieve = to_raw_response_wrapper(
            ai_credits_webhooks_deliveriesattempts.retrieve,
        )


class AsyncAICreditsWebhooksDeliveriesattemptsResourceWithRawResponse:
    def __init__(
        self, ai_credits_webhooks_deliveriesattempts: AsyncAICreditsWebhooksDeliveriesattemptsResource
    ) -> None:
        self._ai_credits_webhooks_deliveriesattempts = ai_credits_webhooks_deliveriesattempts

        self.retrieve = async_to_raw_response_wrapper(
            ai_credits_webhooks_deliveriesattempts.retrieve,
        )


class AICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse:
    def __init__(self, ai_credits_webhooks_deliveriesattempts: AICreditsWebhooksDeliveriesattemptsResource) -> None:
        self._ai_credits_webhooks_deliveriesattempts = ai_credits_webhooks_deliveriesattempts

        self.retrieve = to_streamed_response_wrapper(
            ai_credits_webhooks_deliveriesattempts.retrieve,
        )


class AsyncAICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse:
    def __init__(
        self, ai_credits_webhooks_deliveriesattempts: AsyncAICreditsWebhooksDeliveriesattemptsResource
    ) -> None:
        self._ai_credits_webhooks_deliveriesattempts = ai_credits_webhooks_deliveriesattempts

        self.retrieve = async_to_streamed_response_wrapper(
            ai_credits_webhooks_deliveriesattempts.retrieve,
        )
