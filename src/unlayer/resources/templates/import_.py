# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.templates import import_create_params
from ...types.templates.import_create_response import ImportCreateResponse

__all__ = ["ImportResource", "AsyncImportResource"]


class ImportResource(SyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> ImportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ImportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ImportResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        display_mode: Literal["email", "web", "popup", "document"],
        input: Iterable[import_create_params.Input],
        project_id: str | Omit = omit,
        fallback_models: Union[bool, SequenceNotStr[str]] | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportCreateResponse:
        """
        Import an existing template from HTML or an image (URL or base64) and return the
        resulting Unlayer design JSON. No template DB entry is created.

        Args:
          display_mode: Display mode for the imported design

          input: Array of input parts. Must contain exactly one "html" or "image" part; may also
              contain one or more "text" parts with optional instructions.

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          fallback_models: Transient-outage fallback controls. Omit to use Unlayer defaults only when no
              model is pinned; true always uses Unlayer defaults; false disables the outage
              tail; an ordered array replaces the default provider/model strings.

          model: Preferred AI model. Accepts a provider/model string (e.g.
              "anthropic/claude-opus-5", "openai/gpt-5.6-luna"), a bare provider ("anthropic",
              "openai") which uses that provider's default model, or a bare model id
              ("claude-opus-5", "gpt-5.6-luna") with the provider inferred from the name.
              Optional — defaults to anthropic/claude-opus-5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/templates/import",
            body=maybe_transform(
                {
                    "display_mode": display_mode,
                    "input": input,
                    "fallback_models": fallback_models,
                    "model": model,
                },
                import_create_params.ImportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, import_create_params.ImportCreateParams),
            ),
            cast_to=ImportCreateResponse,
        )


class AsyncImportResource(AsyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncImportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncImportResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        display_mode: Literal["email", "web", "popup", "document"],
        input: Iterable[import_create_params.Input],
        project_id: str | Omit = omit,
        fallback_models: Union[bool, SequenceNotStr[str]] | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportCreateResponse:
        """
        Import an existing template from HTML or an image (URL or base64) and return the
        resulting Unlayer design JSON. No template DB entry is created.

        Args:
          display_mode: Display mode for the imported design

          input: Array of input parts. Must contain exactly one "html" or "image" part; may also
              contain one or more "text" parts with optional instructions.

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          fallback_models: Transient-outage fallback controls. Omit to use Unlayer defaults only when no
              model is pinned; true always uses Unlayer defaults; false disables the outage
              tail; an ordered array replaces the default provider/model strings.

          model: Preferred AI model. Accepts a provider/model string (e.g.
              "anthropic/claude-opus-5", "openai/gpt-5.6-luna"), a bare provider ("anthropic",
              "openai") which uses that provider's default model, or a bare model id
              ("claude-opus-5", "gpt-5.6-luna") with the provider inferred from the name.
              Optional — defaults to anthropic/claude-opus-5.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/templates/import",
            body=await async_maybe_transform(
                {
                    "display_mode": display_mode,
                    "input": input,
                    "fallback_models": fallback_models,
                    "model": model,
                },
                import_create_params.ImportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"project_id": project_id}, import_create_params.ImportCreateParams),
            ),
            cast_to=ImportCreateResponse,
        )


class ImportResourceWithRawResponse:
    def __init__(self, import_: ImportResource) -> None:
        self._import_ = import_

        self.create = to_raw_response_wrapper(
            import_.create,
        )


class AsyncImportResourceWithRawResponse:
    def __init__(self, import_: AsyncImportResource) -> None:
        self._import_ = import_

        self.create = async_to_raw_response_wrapper(
            import_.create,
        )


class ImportResourceWithStreamingResponse:
    def __init__(self, import_: ImportResource) -> None:
        self._import_ = import_

        self.create = to_streamed_response_wrapper(
            import_.create,
        )


class AsyncImportResourceWithStreamingResponse:
    def __init__(self, import_: AsyncImportResource) -> None:
        self._import_ = import_

        self.create = async_to_streamed_response_wrapper(
            import_.create,
        )
