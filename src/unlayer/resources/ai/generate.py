# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.ai import generate_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.ai.generate_create_response import GenerateCreateResponse

__all__ = ["GenerateResource", "AsyncGenerateResource"]


class GenerateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return GenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return GenerateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        display_mode: Literal["email", "web", "popup", "document"],
        input: Iterable[generate_create_params.Input],
        output: generate_create_params.Output,
        project_id: str | Omit = omit,
        context: generate_create_params.Context | Omit = omit,
        model: Literal["anthropic/claude-opus-4-6", "openai/gpt-5.2"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateCreateResponse:
        """Generate, modify, or import an Unlayer design using AI.

        Provide typed input
        parts to describe what to generate.

        Args:
          display_mode: Display mode for the design

          input: Array of typed input parts (max 50)

          output: What to generate

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          context: Editor environment context

          model: AI model to use, in provider/model format. Optional — defaults to
              anthropic/claude-opus-4-6.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/ai/generate",
            body=maybe_transform(
                {
                    "display_mode": display_mode,
                    "input": input,
                    "output": output,
                    "context": context,
                    "model": model,
                },
                generate_create_params.GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, generate_create_params.GenerateCreateParams),
            ),
            cast_to=GenerateCreateResponse,
        )


class AsyncGenerateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncGenerateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        display_mode: Literal["email", "web", "popup", "document"],
        input: Iterable[generate_create_params.Input],
        output: generate_create_params.Output,
        project_id: str | Omit = omit,
        context: generate_create_params.Context | Omit = omit,
        model: Literal["anthropic/claude-opus-4-6", "openai/gpt-5.2"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateCreateResponse:
        """Generate, modify, or import an Unlayer design using AI.

        Provide typed input
        parts to describe what to generate.

        Args:
          display_mode: Display mode for the design

          input: Array of typed input parts (max 50)

          output: What to generate

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          context: Editor environment context

          model: AI model to use, in provider/model format. Optional — defaults to
              anthropic/claude-opus-4-6.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/ai/generate",
            body=await async_maybe_transform(
                {
                    "display_mode": display_mode,
                    "input": input,
                    "output": output,
                    "context": context,
                    "model": model,
                },
                generate_create_params.GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, generate_create_params.GenerateCreateParams
                ),
            ),
            cast_to=GenerateCreateResponse,
        )


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.create = to_raw_response_wrapper(
            generate.create,
        )


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.create = async_to_raw_response_wrapper(
            generate.create,
        )


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.create = to_streamed_response_wrapper(
            generate.create,
        )


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.create = async_to_streamed_response_wrapper(
            generate.create,
        )
