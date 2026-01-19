# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import (
    document_generate_create_params,
    document_documents_retrieve_params,
    document_generate_template_template_params,
)
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
from ..types.document_generate_create_response import DocumentGenerateCreateResponse
from ..types.document_documents_retrieve_response import DocumentDocumentsRetrieveResponse
from ..types.document_generate_template_template_response import DocumentGenerateTemplateTemplateResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
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

    def documents_retrieve(
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
    ) -> DocumentDocumentsRetrieveResponse:
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
                query=maybe_transform(
                    {"project_id": project_id}, document_documents_retrieve_params.DocumentDocumentsRetrieveParams
                ),
            ),
            cast_to=DocumentDocumentsRetrieveResponse,
        )

    def generate_create(
        self,
        *,
        project_id: str,
        design: Dict[str, object] | Omit = omit,
        filename: str | Omit = omit,
        html: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGenerateCreateResponse:
        """
        Generate PDF document from JSON design, HTML content, or URL.

        Args:
          project_id: The project ID

          design: Proprietary design format JSON

          filename: Optional filename for the generated PDF

          html: HTML content to convert to PDF

          merge_tags: Optional merge tags for personalization

          url: URL to convert to PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/v1/generate",
            body=maybe_transform(
                {
                    "design": design,
                    "filename": filename,
                    "html": html,
                    "merge_tags": merge_tags,
                    "url": url,
                },
                document_generate_create_params.DocumentGenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"project_id": project_id}, document_generate_create_params.DocumentGenerateCreateParams
                ),
            ),
            cast_to=DocumentGenerateCreateResponse,
        )

    def generate_template_template(
        self,
        *,
        project_id: str,
        template_id: str,
        filename: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGenerateTemplateTemplateResponse:
        """
        Generate PDF document from an existing template with merge tags.

        Args:
          project_id: The project ID

          template_id: ID of the template to use for generation

          filename: Optional filename for the generated PDF

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/v1/generate/template",
            body=maybe_transform(
                {
                    "template_id": template_id,
                    "filename": filename,
                    "merge_tags": merge_tags,
                },
                document_generate_template_template_params.DocumentGenerateTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"project_id": project_id},
                    document_generate_template_template_params.DocumentGenerateTemplateTemplateParams,
                ),
            ),
            cast_to=DocumentGenerateTemplateTemplateResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
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

    async def documents_retrieve(
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
    ) -> DocumentDocumentsRetrieveResponse:
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
                    {"project_id": project_id}, document_documents_retrieve_params.DocumentDocumentsRetrieveParams
                ),
            ),
            cast_to=DocumentDocumentsRetrieveResponse,
        )

    async def generate_create(
        self,
        *,
        project_id: str,
        design: Dict[str, object] | Omit = omit,
        filename: str | Omit = omit,
        html: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGenerateCreateResponse:
        """
        Generate PDF document from JSON design, HTML content, or URL.

        Args:
          project_id: The project ID

          design: Proprietary design format JSON

          filename: Optional filename for the generated PDF

          html: HTML content to convert to PDF

          merge_tags: Optional merge tags for personalization

          url: URL to convert to PDF

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/v1/generate",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "filename": filename,
                    "html": html,
                    "merge_tags": merge_tags,
                    "url": url,
                },
                document_generate_create_params.DocumentGenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, document_generate_create_params.DocumentGenerateCreateParams
                ),
            ),
            cast_to=DocumentGenerateCreateResponse,
        )

    async def generate_template_template(
        self,
        *,
        project_id: str,
        template_id: str,
        filename: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGenerateTemplateTemplateResponse:
        """
        Generate PDF document from an existing template with merge tags.

        Args:
          project_id: The project ID

          template_id: ID of the template to use for generation

          filename: Optional filename for the generated PDF

          merge_tags: Optional merge tags for personalization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/v1/generate/template",
            body=await async_maybe_transform(
                {
                    "template_id": template_id,
                    "filename": filename,
                    "merge_tags": merge_tags,
                },
                document_generate_template_template_params.DocumentGenerateTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id},
                    document_generate_template_template_params.DocumentGenerateTemplateTemplateParams,
                ),
            ),
            cast_to=DocumentGenerateTemplateTemplateResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.documents_retrieve = to_raw_response_wrapper(
            documents.documents_retrieve,
        )
        self.generate_create = to_raw_response_wrapper(
            documents.generate_create,
        )
        self.generate_template_template = to_raw_response_wrapper(
            documents.generate_template_template,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.documents_retrieve = async_to_raw_response_wrapper(
            documents.documents_retrieve,
        )
        self.generate_create = async_to_raw_response_wrapper(
            documents.generate_create,
        )
        self.generate_template_template = async_to_raw_response_wrapper(
            documents.generate_template_template,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.documents_retrieve = to_streamed_response_wrapper(
            documents.documents_retrieve,
        )
        self.generate_create = to_streamed_response_wrapper(
            documents.generate_create,
        )
        self.generate_template_template = to_streamed_response_wrapper(
            documents.generate_template_template,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.documents_retrieve = async_to_streamed_response_wrapper(
            documents.documents_retrieve,
        )
        self.generate_create = async_to_streamed_response_wrapper(
            documents.generate_create,
        )
        self.generate_template_template = async_to_streamed_response_wrapper(
            documents.generate_template_template,
        )
