# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
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
from ...types.templates import export_html_create_params
from ...types.templates.export_html_create_response import ExportHTMLCreateResponse

__all__ = ["ExportHTMLResource", "AsyncExportHTMLResource"]


class ExportHTMLResource(SyncAPIResource):
    """Render designs as HTML, images, PDFs, or ZIP files."""

    @cached_property
    def with_raw_response(self) -> ExportHTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ExportHTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportHTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ExportHTMLResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: object,
        project_id: str | Omit = omit,
        custom_js: Union[str, SequenceNotStr[str]] | Omit = omit,
        design_tags: object | Omit = omit,
        design_tags_config: object | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        editor_version: str | Omit = omit,
        language: str | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        merge_tags: object | Omit = omit,
        merge_tags_schema: object | Omit = omit,
        safe_html: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportHTMLCreateResponse:
        """
        Export a design as rendered HTML.

        Args:
          design: Unlayer design JSON

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/templates/export/html",
            body=maybe_transform(
                {
                    "design": design,
                    "custom_js": custom_js,
                    "design_tags": design_tags,
                    "design_tags_config": design_tags_config,
                    "display_mode": display_mode,
                    "editor_version": editor_version,
                    "language": language,
                    "languages": languages,
                    "merge_tags": merge_tags,
                    "merge_tags_schema": merge_tags_schema,
                    "safe_html": safe_html,
                },
                export_html_create_params.ExportHTMLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, export_html_create_params.ExportHTMLCreateParams),
            ),
            cast_to=ExportHTMLCreateResponse,
        )


class AsyncExportHTMLResource(AsyncAPIResource):
    """Render designs as HTML, images, PDFs, or ZIP files."""

    @cached_property
    def with_raw_response(self) -> AsyncExportHTMLResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportHTMLResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportHTMLResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncExportHTMLResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: object,
        project_id: str | Omit = omit,
        custom_js: Union[str, SequenceNotStr[str]] | Omit = omit,
        design_tags: object | Omit = omit,
        design_tags_config: object | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        editor_version: str | Omit = omit,
        language: str | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        merge_tags: object | Omit = omit,
        merge_tags_schema: object | Omit = omit,
        safe_html: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportHTMLCreateResponse:
        """
        Export a design as rendered HTML.

        Args:
          design: Unlayer design JSON

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/templates/export/html",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "custom_js": custom_js,
                    "design_tags": design_tags,
                    "design_tags_config": design_tags_config,
                    "display_mode": display_mode,
                    "editor_version": editor_version,
                    "language": language,
                    "languages": languages,
                    "merge_tags": merge_tags,
                    "merge_tags_schema": merge_tags_schema,
                    "safe_html": safe_html,
                },
                export_html_create_params.ExportHTMLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, export_html_create_params.ExportHTMLCreateParams
                ),
            ),
            cast_to=ExportHTMLCreateResponse,
        )


class ExportHTMLResourceWithRawResponse:
    def __init__(self, export_html: ExportHTMLResource) -> None:
        self._export_html = export_html

        self.create = to_raw_response_wrapper(
            export_html.create,
        )


class AsyncExportHTMLResourceWithRawResponse:
    def __init__(self, export_html: AsyncExportHTMLResource) -> None:
        self._export_html = export_html

        self.create = async_to_raw_response_wrapper(
            export_html.create,
        )


class ExportHTMLResourceWithStreamingResponse:
    def __init__(self, export_html: ExportHTMLResource) -> None:
        self._export_html = export_html

        self.create = to_streamed_response_wrapper(
            export_html.create,
        )


class AsyncExportHTMLResourceWithStreamingResponse:
    def __init__(self, export_html: AsyncExportHTMLResource) -> None:
        self._export_html = export_html

        self.create = async_to_streamed_response_wrapper(
            export_html.create,
        )
