# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import editor_session_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.editor_session_create_response import EditorSessionCreateResponse

__all__ = ["EditorSessionsResource", "AsyncEditorSessionsResource"]


class EditorSessionsResource(SyncAPIResource):
    """Ephemeral editor session creation and access."""

    @cached_property
    def with_raw_response(self) -> EditorSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return EditorSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EditorSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return EditorSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: Dict[str, object],
        project_id: str | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EditorSessionCreateResponse:
        """
        Create an ephemeral, no-DB editor session for a design and return a hosted
        editor URL the user can open to edit it in the real Unlayer editor.

        Args:
          design: Design JSON to load into the editor.

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          display_mode: Editor display mode. Defaults to email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/editor-sessions",
            body=maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                },
                editor_session_create_params.EditorSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"project_id": project_id}, editor_session_create_params.EditorSessionCreateParams
                ),
            ),
            cast_to=EditorSessionCreateResponse,
        )


class AsyncEditorSessionsResource(AsyncAPIResource):
    """Ephemeral editor session creation and access."""

    @cached_property
    def with_raw_response(self) -> AsyncEditorSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEditorSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEditorSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncEditorSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: Dict[str, object],
        project_id: str | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EditorSessionCreateResponse:
        """
        Create an ephemeral, no-DB editor session for a design and return a hosted
        editor URL the user can open to edit it in the real Unlayer editor.

        Args:
          design: Design JSON to load into the editor.

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          display_mode: Editor display mode. Defaults to email.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/editor-sessions",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "display_mode": display_mode,
                },
                editor_session_create_params.EditorSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, editor_session_create_params.EditorSessionCreateParams
                ),
            ),
            cast_to=EditorSessionCreateResponse,
        )


class EditorSessionsResourceWithRawResponse:
    def __init__(self, editor_sessions: EditorSessionsResource) -> None:
        self._editor_sessions = editor_sessions

        self.create = to_raw_response_wrapper(
            editor_sessions.create,
        )


class AsyncEditorSessionsResourceWithRawResponse:
    def __init__(self, editor_sessions: AsyncEditorSessionsResource) -> None:
        self._editor_sessions = editor_sessions

        self.create = async_to_raw_response_wrapper(
            editor_sessions.create,
        )


class EditorSessionsResourceWithStreamingResponse:
    def __init__(self, editor_sessions: EditorSessionsResource) -> None:
        self._editor_sessions = editor_sessions

        self.create = to_streamed_response_wrapper(
            editor_sessions.create,
        )


class AsyncEditorSessionsResourceWithStreamingResponse:
    def __init__(self, editor_sessions: AsyncEditorSessionsResource) -> None:
        self._editor_sessions = editor_sessions

        self.create = async_to_streamed_response_wrapper(
            editor_sessions.create,
        )
