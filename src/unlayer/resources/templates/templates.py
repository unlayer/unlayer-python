# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)
from ...types import template_list_params, template_retrieve_params
from .import_ import (
    ImportResource,
    AsyncImportResource,
    ImportResourceWithRawResponse,
    AsyncImportResourceWithRawResponse,
    ImportResourceWithStreamingResponse,
    AsyncImportResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .generate import (
    GenerateResource,
    AsyncGenerateResource,
    GenerateResourceWithRawResponse,
    AsyncGenerateResourceWithRawResponse,
    GenerateResourceWithStreamingResponse,
    AsyncGenerateResourceWithStreamingResponse,
)
from .validate import (
    ValidateResource,
    AsyncValidateResource,
    ValidateResourceWithRawResponse,
    AsyncValidateResourceWithRawResponse,
    ValidateResourceWithStreamingResponse,
    AsyncValidateResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .export_pdf import (
    ExportPdfResource,
    AsyncExportPdfResource,
    ExportPdfResourceWithRawResponse,
    AsyncExportPdfResourceWithRawResponse,
    ExportPdfResourceWithStreamingResponse,
    AsyncExportPdfResourceWithStreamingResponse,
)
from .export_zip import (
    ExportZipResource,
    AsyncExportZipResource,
    ExportZipResourceWithRawResponse,
    AsyncExportZipResourceWithRawResponse,
    ExportZipResourceWithStreamingResponse,
    AsyncExportZipResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .export_html import (
    ExportHTMLResource,
    AsyncExportHTMLResource,
    ExportHTMLResourceWithRawResponse,
    AsyncExportHTMLResourceWithRawResponse,
    ExportHTMLResourceWithStreamingResponse,
    AsyncExportHTMLResourceWithStreamingResponse,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from .export_image import (
    ExportImageResource,
    AsyncExportImageResource,
    ExportImageResourceWithRawResponse,
    AsyncExportImageResourceWithRawResponse,
    ExportImageResourceWithStreamingResponse,
    AsyncExportImageResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from .convert_full_to_simple import (
    ConvertFullToSimpleResource,
    AsyncConvertFullToSimpleResource,
    ConvertFullToSimpleResourceWithRawResponse,
    AsyncConvertFullToSimpleResourceWithRawResponse,
    ConvertFullToSimpleResourceWithStreamingResponse,
    AsyncConvertFullToSimpleResourceWithStreamingResponse,
)
from .convert_simple_to_full import (
    ConvertSimpleToFullResource,
    AsyncConvertSimpleToFullResource,
    ConvertSimpleToFullResourceWithRawResponse,
    AsyncConvertSimpleToFullResourceWithRawResponse,
    ConvertSimpleToFullResourceWithStreamingResponse,
    AsyncConvertSimpleToFullResourceWithStreamingResponse,
)
from ...types.template_list_response import TemplateListResponse
from ...types.template_retrieve_response import TemplateRetrieveResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def convert_full_to_simple(self) -> ConvertFullToSimpleResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ConvertFullToSimpleResource(self._client)

    @cached_property
    def convert_simple_to_full(self) -> ConvertSimpleToFullResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ConvertSimpleToFullResource(self._client)

    @cached_property
    def export_html(self) -> ExportHTMLResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportHTMLResource(self._client)

    @cached_property
    def export_image(self) -> ExportImageResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportImageResource(self._client)

    @cached_property
    def export_pdf(self) -> ExportPdfResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportPdfResource(self._client)

    @cached_property
    def export_zip(self) -> ExportZipResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportZipResource(self._client)

    @cached_property
    def generate(self) -> GenerateResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return GenerateResource(self._client)

    @cached_property
    def import_(self) -> ImportResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ImportResource(self._client)

    @cached_property
    def schema(self) -> SchemaResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return SchemaResource(self._client)

    @cached_property
    def validate(self) -> ValidateResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ValidateResource(self._client)

    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRetrieveResponse:
        """
        Get template by ID.

        Args:
          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, template_retrieve_params.TemplateRetrieveParams),
            ),
            cast_to=TemplateRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        display_mode: Literal["email", "web", "document"] | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[TemplateListResponse]:
        """List templates with cursor-based pagination.

        Returns templates in descending
        order by update time.

        Args:
          cursor: Pagination cursor from previous response

          display_mode: Filter by template type

          limit: Number of templates to return (1-100)

          name: Filter by name (case-insensitive search)

          project_id: The project ID to list templates for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/templates",
            page=SyncCursorPage[TemplateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "display_mode": display_mode,
                        "limit": limit,
                        "name": name,
                        "project_id": project_id,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            model=TemplateListResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def convert_full_to_simple(self) -> AsyncConvertFullToSimpleResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncConvertFullToSimpleResource(self._client)

    @cached_property
    def convert_simple_to_full(self) -> AsyncConvertSimpleToFullResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncConvertSimpleToFullResource(self._client)

    @cached_property
    def export_html(self) -> AsyncExportHTMLResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportHTMLResource(self._client)

    @cached_property
    def export_image(self) -> AsyncExportImageResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportImageResource(self._client)

    @cached_property
    def export_pdf(self) -> AsyncExportPdfResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportPdfResource(self._client)

    @cached_property
    def export_zip(self) -> AsyncExportZipResource:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportZipResource(self._client)

    @cached_property
    def generate(self) -> AsyncGenerateResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncGenerateResource(self._client)

    @cached_property
    def import_(self) -> AsyncImportResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncImportResource(self._client)

    @cached_property
    def schema(self) -> AsyncSchemaResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncSchemaResource(self._client)

    @cached_property
    def validate(self) -> AsyncValidateResource:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncValidateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateRetrieveResponse:
        """
        Get template by ID.

        Args:
          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/templates/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, template_retrieve_params.TemplateRetrieveParams
                ),
            ),
            cast_to=TemplateRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        display_mode: Literal["email", "web", "document"] | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TemplateListResponse, AsyncCursorPage[TemplateListResponse]]:
        """List templates with cursor-based pagination.

        Returns templates in descending
        order by update time.

        Args:
          cursor: Pagination cursor from previous response

          display_mode: Filter by template type

          limit: Number of templates to return (1-100)

          name: Filter by name (case-insensitive search)

          project_id: The project ID to list templates for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v3/templates",
            page=AsyncCursorPage[TemplateListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "display_mode": display_mode,
                        "limit": limit,
                        "name": name,
                        "project_id": project_id,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            model=TemplateListResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.retrieve = to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )

    @cached_property
    def convert_full_to_simple(self) -> ConvertFullToSimpleResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ConvertFullToSimpleResourceWithRawResponse(self._templates.convert_full_to_simple)

    @cached_property
    def convert_simple_to_full(self) -> ConvertSimpleToFullResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ConvertSimpleToFullResourceWithRawResponse(self._templates.convert_simple_to_full)

    @cached_property
    def export_html(self) -> ExportHTMLResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportHTMLResourceWithRawResponse(self._templates.export_html)

    @cached_property
    def export_image(self) -> ExportImageResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportImageResourceWithRawResponse(self._templates.export_image)

    @cached_property
    def export_pdf(self) -> ExportPdfResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportPdfResourceWithRawResponse(self._templates.export_pdf)

    @cached_property
    def export_zip(self) -> ExportZipResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportZipResourceWithRawResponse(self._templates.export_zip)

    @cached_property
    def generate(self) -> GenerateResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return GenerateResourceWithRawResponse(self._templates.generate)

    @cached_property
    def import_(self) -> ImportResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ImportResourceWithRawResponse(self._templates.import_)

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return SchemaResourceWithRawResponse(self._templates.schema)

    @cached_property
    def validate(self) -> ValidateResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ValidateResourceWithRawResponse(self._templates.validate)


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.retrieve = async_to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )

    @cached_property
    def convert_full_to_simple(self) -> AsyncConvertFullToSimpleResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncConvertFullToSimpleResourceWithRawResponse(self._templates.convert_full_to_simple)

    @cached_property
    def convert_simple_to_full(self) -> AsyncConvertSimpleToFullResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncConvertSimpleToFullResourceWithRawResponse(self._templates.convert_simple_to_full)

    @cached_property
    def export_html(self) -> AsyncExportHTMLResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportHTMLResourceWithRawResponse(self._templates.export_html)

    @cached_property
    def export_image(self) -> AsyncExportImageResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportImageResourceWithRawResponse(self._templates.export_image)

    @cached_property
    def export_pdf(self) -> AsyncExportPdfResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportPdfResourceWithRawResponse(self._templates.export_pdf)

    @cached_property
    def export_zip(self) -> AsyncExportZipResourceWithRawResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportZipResourceWithRawResponse(self._templates.export_zip)

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncGenerateResourceWithRawResponse(self._templates.generate)

    @cached_property
    def import_(self) -> AsyncImportResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncImportResourceWithRawResponse(self._templates.import_)

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncSchemaResourceWithRawResponse(self._templates.schema)

    @cached_property
    def validate(self) -> AsyncValidateResourceWithRawResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncValidateResourceWithRawResponse(self._templates.validate)


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.retrieve = to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )

    @cached_property
    def convert_full_to_simple(self) -> ConvertFullToSimpleResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ConvertFullToSimpleResourceWithStreamingResponse(self._templates.convert_full_to_simple)

    @cached_property
    def convert_simple_to_full(self) -> ConvertSimpleToFullResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ConvertSimpleToFullResourceWithStreamingResponse(self._templates.convert_simple_to_full)

    @cached_property
    def export_html(self) -> ExportHTMLResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportHTMLResourceWithStreamingResponse(self._templates.export_html)

    @cached_property
    def export_image(self) -> ExportImageResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportImageResourceWithStreamingResponse(self._templates.export_image)

    @cached_property
    def export_pdf(self) -> ExportPdfResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportPdfResourceWithStreamingResponse(self._templates.export_pdf)

    @cached_property
    def export_zip(self) -> ExportZipResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return ExportZipResourceWithStreamingResponse(self._templates.export_zip)

    @cached_property
    def generate(self) -> GenerateResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return GenerateResourceWithStreamingResponse(self._templates.generate)

    @cached_property
    def import_(self) -> ImportResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ImportResourceWithStreamingResponse(self._templates.import_)

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return SchemaResourceWithStreamingResponse(self._templates.schema)

    @cached_property
    def validate(self) -> ValidateResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return ValidateResourceWithStreamingResponse(self._templates.validate)


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.retrieve = async_to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )

    @cached_property
    def convert_full_to_simple(self) -> AsyncConvertFullToSimpleResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncConvertFullToSimpleResourceWithStreamingResponse(self._templates.convert_full_to_simple)

    @cached_property
    def convert_simple_to_full(self) -> AsyncConvertSimpleToFullResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncConvertSimpleToFullResourceWithStreamingResponse(self._templates.convert_simple_to_full)

    @cached_property
    def export_html(self) -> AsyncExportHTMLResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportHTMLResourceWithStreamingResponse(self._templates.export_html)

    @cached_property
    def export_image(self) -> AsyncExportImageResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportImageResourceWithStreamingResponse(self._templates.export_image)

    @cached_property
    def export_pdf(self) -> AsyncExportPdfResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportPdfResourceWithStreamingResponse(self._templates.export_pdf)

    @cached_property
    def export_zip(self) -> AsyncExportZipResourceWithStreamingResponse:
        """Render designs as HTML, images, PDFs, or ZIP files."""
        return AsyncExportZipResourceWithStreamingResponse(self._templates.export_zip)

    @cached_property
    def generate(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncGenerateResourceWithStreamingResponse(self._templates.generate)

    @cached_property
    def import_(self) -> AsyncImportResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncImportResourceWithStreamingResponse(self._templates.import_)

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncSchemaResourceWithStreamingResponse(self._templates.schema)

    @cached_property
    def validate(self) -> AsyncValidateResourceWithStreamingResponse:
        """
        Template management — list, retrieve, generate, import, export, and convert designs.
        """
        return AsyncValidateResourceWithStreamingResponse(self._templates.validate)
