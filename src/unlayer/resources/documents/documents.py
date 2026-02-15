# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import document_retrieve_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .generate import (
    GenerateResource,
    AsyncGenerateResource,
    GenerateResourceWithRawResponse,
    AsyncGenerateResourceWithRawResponse,
    GenerateResourceWithStreamingResponse,
    AsyncGenerateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .generate_template import (
    GenerateTemplateResource,
    AsyncGenerateTemplateResource,
    GenerateTemplateResourceWithRawResponse,
    AsyncGenerateTemplateResourceWithRawResponse,
    GenerateTemplateResourceWithStreamingResponse,
    AsyncGenerateTemplateResourceWithStreamingResponse,
)
from ...types.document_retrieve_response import DocumentRetrieveResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def generate(self) -> GenerateResource:
        return GenerateResource(self._client)

    @cached_property
    def generate_template(self) -> GenerateTemplateResource:
        return GenerateTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetrieveResponse:
        """
        Retrieve details of a previously generated document.

        Args:
          project_id: The project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/documents/v1/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, document_retrieve_params.DocumentRetrieveParams),
            ),
            cast_to=DocumentRetrieveResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def generate(self) -> AsyncGenerateResource:
        return AsyncGenerateResource(self._client)

    @cached_property
    def generate_template(self) -> AsyncGenerateTemplateResource:
        return AsyncGenerateTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        project_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetrieveResponse:
        """
        Retrieve details of a previously generated document.

        Args:
          project_id: The project ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/documents/v1/documents/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, document_retrieve_params.DocumentRetrieveParams
                ),
            ),
            cast_to=DocumentRetrieveResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.retrieve = to_raw_response_wrapper(
            documents.retrieve,
        )

    @cached_property
    def generate(self) -> GenerateResourceWithRawResponse:
        return GenerateResourceWithRawResponse(self._documents.generate)

    @cached_property
    def generate_template(self) -> GenerateTemplateResourceWithRawResponse:
        return GenerateTemplateResourceWithRawResponse(self._documents.generate_template)


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.retrieve = async_to_raw_response_wrapper(
            documents.retrieve,
        )

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithRawResponse:
        return AsyncGenerateResourceWithRawResponse(self._documents.generate)

    @cached_property
    def generate_template(self) -> AsyncGenerateTemplateResourceWithRawResponse:
        return AsyncGenerateTemplateResourceWithRawResponse(self._documents.generate_template)


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.retrieve = to_streamed_response_wrapper(
            documents.retrieve,
        )

    @cached_property
    def generate(self) -> GenerateResourceWithStreamingResponse:
        return GenerateResourceWithStreamingResponse(self._documents.generate)

    @cached_property
    def generate_template(self) -> GenerateTemplateResourceWithStreamingResponse:
        return GenerateTemplateResourceWithStreamingResponse(self._documents.generate_template)


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.retrieve = async_to_streamed_response_wrapper(
            documents.retrieve,
        )

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithStreamingResponse:
        return AsyncGenerateResourceWithStreamingResponse(self._documents.generate)

    @cached_property
    def generate_template(self) -> AsyncGenerateTemplateResourceWithStreamingResponse:
        return AsyncGenerateTemplateResourceWithStreamingResponse(self._documents.generate_template)
