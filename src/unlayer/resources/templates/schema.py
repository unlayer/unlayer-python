# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.templates import schema_retrieve_params

__all__ = ["SchemaResource", "AsyncSchemaResource"]


class SchemaResource(SyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> SchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return SchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return SchemaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        simple: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns the canonical design schema as a standard JSON Schema document — the
        exact schema POST /v3/templates/validate checks against, ready to plug into any
        JSON Schema validator or editor tooling. Serves the Full schema by default; pass
        simple=true for the compact Simple schema. No authentication required. Responses
        carry a strong ETag and long-lived cache headers; send If-None-Match to
        revalidate for free.

        Args:
          display_mode: Display mode whose rules the schema describes (email, web, document, popup).
              Defaults to "email".

          simple: When true, returns the Simple schema instead of the Full schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/v3/templates/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "display_mode": display_mode,
                        "simple": simple,
                    },
                    schema_retrieve_params.SchemaRetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncSchemaResource(AsyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncSchemaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        simple: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Returns the canonical design schema as a standard JSON Schema document — the
        exact schema POST /v3/templates/validate checks against, ready to plug into any
        JSON Schema validator or editor tooling. Serves the Full schema by default; pass
        simple=true for the compact Simple schema. No authentication required. Responses
        carry a strong ETag and long-lived cache headers; send If-None-Match to
        revalidate for free.

        Args:
          display_mode: Display mode whose rules the schema describes (email, web, document, popup).
              Defaults to "email".

          simple: When true, returns the Simple schema instead of the Full schema.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/v3/templates/schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "display_mode": display_mode,
                        "simple": simple,
                    },
                    schema_retrieve_params.SchemaRetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class SchemaResourceWithRawResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.retrieve = to_raw_response_wrapper(
            schema.retrieve,
        )


class AsyncSchemaResourceWithRawResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.retrieve = async_to_raw_response_wrapper(
            schema.retrieve,
        )


class SchemaResourceWithStreamingResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.retrieve = to_streamed_response_wrapper(
            schema.retrieve,
        )


class AsyncSchemaResourceWithStreamingResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.retrieve = async_to_streamed_response_wrapper(
            schema.retrieve,
        )
