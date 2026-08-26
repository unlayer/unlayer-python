# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import block_retrieve_params
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
from ..types.block_retrieve_response import BlockRetrieveResponse

__all__ = ["BlocksResource", "AsyncBlocksResource"]


class BlocksResource(SyncAPIResource):
    """
    Reusable design blocks — list shared project blocks and end-user saved blocks for backup, migration, and usage reporting.
    """

    @cached_property
    def with_raw_response(self) -> BlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return BlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return BlocksResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        category: str | Omit = omit,
        cursor: str | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_data: bool | Omit = omit,
        limit: int | Omit = omit,
        project_id: str | Omit = omit,
        scope: Literal["all", "shared", "user"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockRetrieveResponse:
        """List blocks with cursor-based pagination.

        Returns both shared project blocks and
        blocks saved by end-users; each user-saved block carries the userId it was saved
        under (null for shared blocks), so usage can be aggregated per end-user without
        enumerating user IDs. Returns blocks in descending order by creation.

        Args:
          category: Filter by category (case-insensitive search)

          cursor: Pagination cursor from previous response

          display_mode: Filter by display mode

          include_data: Include the block design JSON in each item. Pass false for lightweight sweeps
              (e.g. usage reports).

          limit: Number of blocks to return (1-100)

          project_id: The project ID to list blocks for

          scope: Filter by block ownership: shared project blocks, end-user saved blocks, or both

          user_id: Only blocks saved by this end-user (exact match on the user id your app passes
              to the editor)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/blocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "cursor": cursor,
                        "display_mode": display_mode,
                        "include_data": include_data,
                        "limit": limit,
                        "project_id": project_id,
                        "scope": scope,
                        "user_id": user_id,
                    },
                    block_retrieve_params.BlockRetrieveParams,
                ),
            ),
            cast_to=BlockRetrieveResponse,
        )


class AsyncBlocksResource(AsyncAPIResource):
    """
    Reusable design blocks — list shared project blocks and end-user saved blocks for backup, migration, and usage reporting.
    """

    @cached_property
    def with_raw_response(self) -> AsyncBlocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncBlocksResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        category: str | Omit = omit,
        cursor: str | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        include_data: bool | Omit = omit,
        limit: int | Omit = omit,
        project_id: str | Omit = omit,
        scope: Literal["all", "shared", "user"] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockRetrieveResponse:
        """List blocks with cursor-based pagination.

        Returns both shared project blocks and
        blocks saved by end-users; each user-saved block carries the userId it was saved
        under (null for shared blocks), so usage can be aggregated per end-user without
        enumerating user IDs. Returns blocks in descending order by creation.

        Args:
          category: Filter by category (case-insensitive search)

          cursor: Pagination cursor from previous response

          display_mode: Filter by display mode

          include_data: Include the block design JSON in each item. Pass false for lightweight sweeps
              (e.g. usage reports).

          limit: Number of blocks to return (1-100)

          project_id: The project ID to list blocks for

          scope: Filter by block ownership: shared project blocks, end-user saved blocks, or both

          user_id: Only blocks saved by this end-user (exact match on the user id your app passes
              to the editor)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/blocks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "cursor": cursor,
                        "display_mode": display_mode,
                        "include_data": include_data,
                        "limit": limit,
                        "project_id": project_id,
                        "scope": scope,
                        "user_id": user_id,
                    },
                    block_retrieve_params.BlockRetrieveParams,
                ),
            ),
            cast_to=BlockRetrieveResponse,
        )


class BlocksResourceWithRawResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = to_raw_response_wrapper(
            blocks.retrieve,
        )


class AsyncBlocksResourceWithRawResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = async_to_raw_response_wrapper(
            blocks.retrieve,
        )


class BlocksResourceWithStreamingResponse:
    def __init__(self, blocks: BlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = to_streamed_response_wrapper(
            blocks.retrieve,
        )


class AsyncBlocksResourceWithStreamingResponse:
    def __init__(self, blocks: AsyncBlocksResource) -> None:
        self._blocks = blocks

        self.retrieve = async_to_streamed_response_wrapper(
            blocks.retrieve,
        )
