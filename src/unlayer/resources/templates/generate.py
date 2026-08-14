# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.templates import generate_create_params
from ...types.templates.generate_create_response import GenerateCreateResponse

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
        messages: Iterable[generate_create_params.Message],
        output: generate_create_params.Output,
        project_id: str | Omit = omit,
        context: generate_create_params.Context | Omit = omit,
        conversation_id: str | Omit = omit,
        fallback_models: Union[bool, SequenceNotStr[str]] | Omit = omit,
        locale: str | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateCreateResponse:
        """Generate or modify an Unlayer design using AI.

        Send the conversation as
        `messages` (today only the last user message is consumed; earlier turns are
        accepted as chat history) and describe the target with `output.kind` +
        `output.displayMode`. Pass the current canvas state in `context` (full design
        JSON + selection pointer) to modify an existing design. Only `anthropic` and
        `openai` models are supported. To import existing HTML or an image instead, use
        POST /v3/templates/import.

        Args:
          messages: Conversation messages in chronological order, capped at 10 messages. The last
              `user` message is the prompt for this turn; the newest earlier
              `user`/`assistant` turns are forwarded within a 12,000-character aggregate
              history budget. A `user` message may carry a predefined prompt action via
              `metadata.action.id` (e.g. SPELLING, REPHRASE).

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          conversation_id: Reserved for future server-side conversation memory.

          fallback_models: Transient-outage fallback controls. Omit to use Unlayer defaults only when no
              model is pinned; true always uses Unlayer defaults; false disables the outage
              tail; an ordered array replaces the default provider/model strings.

          locale: BCP-47 fallback locale for AI status messages.

          model: Preferred AI model in "provider/id" form, e.g. "anthropic/claude-opus-5".
              Optional — server resolves a default per output kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/templates/generate",
            body=maybe_transform(
                {
                    "messages": messages,
                    "output": output,
                    "context": context,
                    "conversation_id": conversation_id,
                    "fallback_models": fallback_models,
                    "locale": locale,
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

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v3/templates/generate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        messages: Iterable[generate_create_params.Message],
        output: generate_create_params.Output,
        project_id: str | Omit = omit,
        context: generate_create_params.Context | Omit = omit,
        conversation_id: str | Omit = omit,
        fallback_models: Union[bool, SequenceNotStr[str]] | Omit = omit,
        locale: str | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateCreateResponse:
        """Generate or modify an Unlayer design using AI.

        Send the conversation as
        `messages` (today only the last user message is consumed; earlier turns are
        accepted as chat history) and describe the target with `output.kind` +
        `output.displayMode`. Pass the current canvas state in `context` (full design
        JSON + selection pointer) to modify an existing design. Only `anthropic` and
        `openai` models are supported. To import existing HTML or an image instead, use
        POST /v3/templates/import.

        Args:
          messages: Conversation messages in chronological order, capped at 10 messages. The last
              `user` message is the prompt for this turn; the newest earlier
              `user`/`assistant` turns are forwarded within a 12,000-character aggregate
              history budget. A `user` message may carry a predefined prompt action via
              `metadata.action.id` (e.g. SPELLING, REPHRASE).

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          conversation_id: Reserved for future server-side conversation memory.

          fallback_models: Transient-outage fallback controls. Omit to use Unlayer defaults only when no
              model is pinned; true always uses Unlayer defaults; false disables the outage
              tail; an ordered array replaces the default provider/model strings.

          locale: BCP-47 fallback locale for AI status messages.

          model: Preferred AI model in "provider/id" form, e.g. "anthropic/claude-opus-5".
              Optional — server resolves a default per output kind.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/templates/generate",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "output": output,
                    "context": context,
                    "conversation_id": conversation_id,
                    "fallback_models": fallback_models,
                    "locale": locale,
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

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v3/templates/generate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.create = to_raw_response_wrapper(
            generate.create,
        )
        self.retrieve = to_raw_response_wrapper(
            generate.retrieve,
        )


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.create = async_to_raw_response_wrapper(
            generate.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            generate.retrieve,
        )


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.create = to_streamed_response_wrapper(
            generate.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            generate.retrieve,
        )


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.create = async_to_streamed_response_wrapper(
            generate.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            generate.retrieve,
        )
