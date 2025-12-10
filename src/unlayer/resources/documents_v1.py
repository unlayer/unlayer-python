# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import documents_v1_generate_create_params, documents_v1_generate_template_template_params
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
from ..types.documents_v1_generate_create_response import DocumentsV1GenerateCreateResponse
from ..types.documents_v1_documents_retrieve_response import DocumentsV1DocumentsRetrieveResponse
from ..types.documents_v1_generate_template_template_response import DocumentsV1GenerateTemplateTemplateResponse

__all__ = ["DocumentsV1Resource", "AsyncDocumentsV1Resource"]


class DocumentsV1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return DocumentsV1ResourceWithStreamingResponse(self)

    def documents_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentsV1DocumentsRetrieveResponse:
        """
        Retrieve details of a previously generated document.

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentsV1DocumentsRetrieveResponse,
        )

    def generate_create(
        self,
        *,
        design: Dict[str, object],
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
    ) -> DocumentsV1GenerateCreateResponse:
        """
        Generate PDF document from JSON design, HTML content, or URL.

        Args:
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
                documents_v1_generate_create_params.DocumentsV1GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentsV1GenerateCreateResponse,
        )

    def generate_template_template(
        self,
        *,
        template_id: str,
        filename: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentsV1GenerateTemplateTemplateResponse:
        """
        Generate PDF document from an existing template with merge tags.

        Args:
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
                documents_v1_generate_template_template_params.DocumentsV1GenerateTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentsV1GenerateTemplateTemplateResponse,
        )


class AsyncDocumentsV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncDocumentsV1ResourceWithStreamingResponse(self)

    async def documents_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentsV1DocumentsRetrieveResponse:
        """
        Retrieve details of a previously generated document.

        Args:
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentsV1DocumentsRetrieveResponse,
        )

    async def generate_create(
        self,
        *,
        design: Dict[str, object],
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
    ) -> DocumentsV1GenerateCreateResponse:
        """
        Generate PDF document from JSON design, HTML content, or URL.

        Args:
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
                documents_v1_generate_create_params.DocumentsV1GenerateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentsV1GenerateCreateResponse,
        )

    async def generate_template_template(
        self,
        *,
        template_id: str,
        filename: str | Omit = omit,
        merge_tags: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentsV1GenerateTemplateTemplateResponse:
        """
        Generate PDF document from an existing template with merge tags.

        Args:
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
                documents_v1_generate_template_template_params.DocumentsV1GenerateTemplateTemplateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentsV1GenerateTemplateTemplateResponse,
        )


class DocumentsV1ResourceWithRawResponse:
    def __init__(self, documents_v1: DocumentsV1Resource) -> None:
        self._documents_v1 = documents_v1

        self.documents_retrieve = to_raw_response_wrapper(
            documents_v1.documents_retrieve,
        )
        self.generate_create = to_raw_response_wrapper(
            documents_v1.generate_create,
        )
        self.generate_template_template = to_raw_response_wrapper(
            documents_v1.generate_template_template,
        )


class AsyncDocumentsV1ResourceWithRawResponse:
    def __init__(self, documents_v1: AsyncDocumentsV1Resource) -> None:
        self._documents_v1 = documents_v1

        self.documents_retrieve = async_to_raw_response_wrapper(
            documents_v1.documents_retrieve,
        )
        self.generate_create = async_to_raw_response_wrapper(
            documents_v1.generate_create,
        )
        self.generate_template_template = async_to_raw_response_wrapper(
            documents_v1.generate_template_template,
        )


class DocumentsV1ResourceWithStreamingResponse:
    def __init__(self, documents_v1: DocumentsV1Resource) -> None:
        self._documents_v1 = documents_v1

        self.documents_retrieve = to_streamed_response_wrapper(
            documents_v1.documents_retrieve,
        )
        self.generate_create = to_streamed_response_wrapper(
            documents_v1.generate_create,
        )
        self.generate_template_template = to_streamed_response_wrapper(
            documents_v1.generate_template_template,
        )


class AsyncDocumentsV1ResourceWithStreamingResponse:
    def __init__(self, documents_v1: AsyncDocumentsV1Resource) -> None:
        self._documents_v1 = documents_v1

        self.documents_retrieve = async_to_streamed_response_wrapper(
            documents_v1.documents_retrieve,
        )
        self.generate_create = async_to_streamed_response_wrapper(
            documents_v1.generate_create,
        )
        self.generate_template_template = async_to_streamed_response_wrapper(
            documents_v1.generate_template_template,
        )
