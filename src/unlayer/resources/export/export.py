# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .pdf import (
    PdfResource,
    AsyncPdfResource,
    PdfResourceWithRawResponse,
    AsyncPdfResourceWithRawResponse,
    PdfResourceWithStreamingResponse,
    AsyncPdfResourceWithStreamingResponse,
)
from .zip import (
    ZipResource,
    AsyncZipResource,
    ZipResourceWithRawResponse,
    AsyncZipResourceWithRawResponse,
    ZipResourceWithStreamingResponse,
    AsyncZipResourceWithStreamingResponse,
)
from .html import (
    HTMLResource,
    AsyncHTMLResource,
    HTMLResourceWithRawResponse,
    AsyncHTMLResourceWithRawResponse,
    HTMLResourceWithStreamingResponse,
    AsyncHTMLResourceWithStreamingResponse,
)
from .image import (
    ImageResource,
    AsyncImageResource,
    ImageResourceWithRawResponse,
    AsyncImageResourceWithRawResponse,
    ImageResourceWithStreamingResponse,
    AsyncImageResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def html(self) -> HTMLResource:
        return HTMLResource(self._client)

    @cached_property
    def image(self) -> ImageResource:
        return ImageResource(self._client)

    @cached_property
    def pdf(self) -> PdfResource:
        return PdfResource(self._client)

    @cached_property
    def zip(self) -> ZipResource:
        return ZipResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def html(self) -> AsyncHTMLResource:
        return AsyncHTMLResource(self._client)

    @cached_property
    def image(self) -> AsyncImageResource:
        return AsyncImageResource(self._client)

    @cached_property
    def pdf(self) -> AsyncPdfResource:
        return AsyncPdfResource(self._client)

    @cached_property
    def zip(self) -> AsyncZipResource:
        return AsyncZipResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

    @cached_property
    def html(self) -> HTMLResourceWithRawResponse:
        return HTMLResourceWithRawResponse(self._export.html)

    @cached_property
    def image(self) -> ImageResourceWithRawResponse:
        return ImageResourceWithRawResponse(self._export.image)

    @cached_property
    def pdf(self) -> PdfResourceWithRawResponse:
        return PdfResourceWithRawResponse(self._export.pdf)

    @cached_property
    def zip(self) -> ZipResourceWithRawResponse:
        return ZipResourceWithRawResponse(self._export.zip)


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

    @cached_property
    def html(self) -> AsyncHTMLResourceWithRawResponse:
        return AsyncHTMLResourceWithRawResponse(self._export.html)

    @cached_property
    def image(self) -> AsyncImageResourceWithRawResponse:
        return AsyncImageResourceWithRawResponse(self._export.image)

    @cached_property
    def pdf(self) -> AsyncPdfResourceWithRawResponse:
        return AsyncPdfResourceWithRawResponse(self._export.pdf)

    @cached_property
    def zip(self) -> AsyncZipResourceWithRawResponse:
        return AsyncZipResourceWithRawResponse(self._export.zip)


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

    @cached_property
    def html(self) -> HTMLResourceWithStreamingResponse:
        return HTMLResourceWithStreamingResponse(self._export.html)

    @cached_property
    def image(self) -> ImageResourceWithStreamingResponse:
        return ImageResourceWithStreamingResponse(self._export.image)

    @cached_property
    def pdf(self) -> PdfResourceWithStreamingResponse:
        return PdfResourceWithStreamingResponse(self._export.pdf)

    @cached_property
    def zip(self) -> ZipResourceWithStreamingResponse:
        return ZipResourceWithStreamingResponse(self._export.zip)


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

    @cached_property
    def html(self) -> AsyncHTMLResourceWithStreamingResponse:
        return AsyncHTMLResourceWithStreamingResponse(self._export.html)

    @cached_property
    def image(self) -> AsyncImageResourceWithStreamingResponse:
        return AsyncImageResourceWithStreamingResponse(self._export.image)

    @cached_property
    def pdf(self) -> AsyncPdfResourceWithStreamingResponse:
        return AsyncPdfResourceWithStreamingResponse(self._export.pdf)

    @cached_property
    def zip(self) -> AsyncZipResourceWithStreamingResponse:
        return AsyncZipResourceWithStreamingResponse(self._export.zip)
