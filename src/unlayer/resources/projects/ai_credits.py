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
from ...types.projects.ai_credit_retrieve_response import AICreditRetrieveResponse

__all__ = ["AICreditsResource", "AsyncAICreditsResource"]


class AICreditsResource(SyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AICreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AICreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AICreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AICreditsResourceWithStreamingResponse(self)

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
    ) -> AICreditRetrieveResponse:
        """Returns the current AI credit balance for the project.

        Credits are pooled per
        workspace — every project in a workspace shares one balance. Only credit counts
        are returned; token counts, model names, and costs are never exposed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/projects/{id}/ai-credits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditRetrieveResponse,
        )


class AsyncAICreditsResource(AsyncAPIResource):
    """AI credit balance, usage breakdown, and webhook/alert settings.

    Credits are pooled per workspace; settings are per project.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAICreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAICreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAICreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncAICreditsResourceWithStreamingResponse(self)

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
    ) -> AICreditRetrieveResponse:
        """Returns the current AI credit balance for the project.

        Credits are pooled per
        workspace — every project in a workspace shares one balance. Only credit counts
        are returned; token counts, model names, and costs are never exposed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/projects/{id}/ai-credits", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AICreditRetrieveResponse,
        )


class AICreditsResourceWithRawResponse:
    def __init__(self, ai_credits: AICreditsResource) -> None:
        self._ai_credits = ai_credits

        self.retrieve = to_raw_response_wrapper(
            ai_credits.retrieve,
        )


class AsyncAICreditsResourceWithRawResponse:
    def __init__(self, ai_credits: AsyncAICreditsResource) -> None:
        self._ai_credits = ai_credits

        self.retrieve = async_to_raw_response_wrapper(
            ai_credits.retrieve,
        )


class AICreditsResourceWithStreamingResponse:
    def __init__(self, ai_credits: AICreditsResource) -> None:
        self._ai_credits = ai_credits

        self.retrieve = to_streamed_response_wrapper(
            ai_credits.retrieve,
        )


class AsyncAICreditsResourceWithStreamingResponse:
    def __init__(self, ai_credits: AsyncAICreditsResource) -> None:
        self._ai_credits = ai_credits

        self.retrieve = async_to_streamed_response_wrapper(
            ai_credits.retrieve,
        )
