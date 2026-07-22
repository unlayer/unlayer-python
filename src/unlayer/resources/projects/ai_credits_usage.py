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
from ...types.projects import ai_credits_usage_retrieve_params
from ...types.projects.ai_credits_usage_retrieve_response import AICreditsUsageRetrieveResponse

__all__ = ["AICreditsUsageResource", "AsyncAICreditsUsageResource"]


class AICreditsUsageResource(SyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AICreditsUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AICreditsUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICreditsUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AICreditsUsageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        end: str | Omit = omit,
        end_user_id: str | Omit = omit,
        feature_type: Literal["full_template_gen", "block_edit", "html_import", "image_import", "image_generation"]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["credits", "end_user_id", "feature_type"] | Omit = omit,
        start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsUsageRetrieveResponse:
        """
        Returns AI credit consumption for the project, broken down by end user and
        feature type. Filterable by date range, end user, and feature type. Defaults to
        the current billing period. Only credit counts are returned; token counts, model
        names, and costs are never exposed. Per-end-user attribution requires the
        partner to pass `endUserId` on editor initialization.

        Args:
          end: End date (inclusive), YYYY-MM-DD.

          end_user_id: Filter to a single end user id.

          feature_type: Filter to a single feature type.

          limit: Max breakdown rows to return (1-1000).

          offset: Number of breakdown rows to skip (pagination).

          order: Sort direction. Defaults to desc (highest credits first).

          sort: Field the breakdown is ordered by. Defaults to credits.

          start: Start date (inclusive), YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/projects/{id}/ai-credits/usage", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "end_user_id": end_user_id,
                        "feature_type": feature_type,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "start": start,
                    },
                    ai_credits_usage_retrieve_params.AICreditsUsageRetrieveParams,
                ),
            ),
            cast_to=AICreditsUsageRetrieveResponse,
        )


class AsyncAICreditsUsageResource(AsyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAICreditsUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICreditsUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICreditsUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncAICreditsUsageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        end: str | Omit = omit,
        end_user_id: str | Omit = omit,
        feature_type: Literal["full_template_gen", "block_edit", "html_import", "image_import", "image_generation"]
        | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        sort: Literal["credits", "end_user_id", "feature_type"] | Omit = omit,
        start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AICreditsUsageRetrieveResponse:
        """
        Returns AI credit consumption for the project, broken down by end user and
        feature type. Filterable by date range, end user, and feature type. Defaults to
        the current billing period. Only credit counts are returned; token counts, model
        names, and costs are never exposed. Per-end-user attribution requires the
        partner to pass `endUserId` on editor initialization.

        Args:
          end: End date (inclusive), YYYY-MM-DD.

          end_user_id: Filter to a single end user id.

          feature_type: Filter to a single feature type.

          limit: Max breakdown rows to return (1-1000).

          offset: Number of breakdown rows to skip (pagination).

          order: Sort direction. Defaults to desc (highest credits first).

          sort: Field the breakdown is ordered by. Defaults to credits.

          start: Start date (inclusive), YYYY-MM-DD.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/projects/{id}/ai-credits/usage", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "end_user_id": end_user_id,
                        "feature_type": feature_type,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "sort": sort,
                        "start": start,
                    },
                    ai_credits_usage_retrieve_params.AICreditsUsageRetrieveParams,
                ),
            ),
            cast_to=AICreditsUsageRetrieveResponse,
        )


class AICreditsUsageResourceWithRawResponse:
    def __init__(self, ai_credits_usage: AICreditsUsageResource) -> None:
        self._ai_credits_usage = ai_credits_usage

        self.retrieve = to_raw_response_wrapper(
            ai_credits_usage.retrieve,
        )


class AsyncAICreditsUsageResourceWithRawResponse:
    def __init__(self, ai_credits_usage: AsyncAICreditsUsageResource) -> None:
        self._ai_credits_usage = ai_credits_usage

        self.retrieve = async_to_raw_response_wrapper(
            ai_credits_usage.retrieve,
        )


class AICreditsUsageResourceWithStreamingResponse:
    def __init__(self, ai_credits_usage: AICreditsUsageResource) -> None:
        self._ai_credits_usage = ai_credits_usage

        self.retrieve = to_streamed_response_wrapper(
            ai_credits_usage.retrieve,
        )


class AsyncAICreditsUsageResourceWithStreamingResponse:
    def __init__(self, ai_credits_usage: AsyncAICreditsUsageResource) -> None:
        self._ai_credits_usage = ai_credits_usage

        self.retrieve = async_to_streamed_response_wrapper(
            ai_credits_usage.retrieve,
        )
