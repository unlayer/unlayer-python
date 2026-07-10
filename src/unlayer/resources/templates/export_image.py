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
from ...types.templates import export_image_create_params
from ...types.templates.export_image_create_response import ExportImageCreateResponse

__all__ = ["ExportImageResource", "AsyncExportImageResource"]


class ExportImageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ExportImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ExportImageResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: object,
        project_id: str | Omit = omit,
        custom_js: Union[str, SequenceNotStr[str]] | Omit = omit,
        design_tags: object | Omit = omit,
        design_tags_config: object | Omit = omit,
        device_scale_factor: float | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        editor_version: str | Omit = omit,
        full_page: bool | Omit = omit,
        height: float | Omit = omit,
        language: str | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        merge_tags: object | Omit = omit,
        merge_tags_schema: object | Omit = omit,
        safe_html: bool | Omit = omit,
        width: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportImageCreateResponse:
        """
        Export a design as a PNG image.

        Args:
          design: Unlayer design JSON

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/templates/export/image",
            body=maybe_transform(
                {
                    "design": design,
                    "custom_js": custom_js,
                    "design_tags": design_tags,
                    "design_tags_config": design_tags_config,
                    "device_scale_factor": device_scale_factor,
                    "display_mode": display_mode,
                    "editor_version": editor_version,
                    "full_page": full_page,
                    "height": height,
                    "language": language,
                    "languages": languages,
                    "merge_tags": merge_tags,
                    "merge_tags_schema": merge_tags_schema,
                    "safe_html": safe_html,
                    "width": width,
                },
                export_image_create_params.ExportImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, export_image_create_params.ExportImageCreateParams),
            ),
            cast_to=ExportImageCreateResponse,
        )


class AsyncExportImageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportImageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportImageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportImageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncExportImageResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: object,
        project_id: str | Omit = omit,
        custom_js: Union[str, SequenceNotStr[str]] | Omit = omit,
        design_tags: object | Omit = omit,
        design_tags_config: object | Omit = omit,
        device_scale_factor: float | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        editor_version: str | Omit = omit,
        full_page: bool | Omit = omit,
        height: float | Omit = omit,
        language: str | Omit = omit,
        languages: SequenceNotStr[str] | Omit = omit,
        merge_tags: object | Omit = omit,
        merge_tags_schema: object | Omit = omit,
        safe_html: bool | Omit = omit,
        width: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExportImageCreateResponse:
        """
        Export a design as a PNG image.

        Args:
          design: Unlayer design JSON

          project_id: The project ID (required for PAT auth, auto-resolved for API key auth)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/templates/export/image",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "custom_js": custom_js,
                    "design_tags": design_tags,
                    "design_tags_config": design_tags_config,
                    "device_scale_factor": device_scale_factor,
                    "display_mode": display_mode,
                    "editor_version": editor_version,
                    "full_page": full_page,
                    "height": height,
                    "language": language,
                    "languages": languages,
                    "merge_tags": merge_tags,
                    "merge_tags_schema": merge_tags_schema,
                    "safe_html": safe_html,
                    "width": width,
                },
                export_image_create_params.ExportImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, export_image_create_params.ExportImageCreateParams
                ),
            ),
            cast_to=ExportImageCreateResponse,
        )


class ExportImageResourceWithRawResponse:
    def __init__(self, export_image: ExportImageResource) -> None:
        self._export_image = export_image

        self.create = to_raw_response_wrapper(
            export_image.create,
        )


class AsyncExportImageResourceWithRawResponse:
    def __init__(self, export_image: AsyncExportImageResource) -> None:
        self._export_image = export_image

        self.create = async_to_raw_response_wrapper(
            export_image.create,
        )


class ExportImageResourceWithStreamingResponse:
    def __init__(self, export_image: ExportImageResource) -> None:
        self._export_image = export_image

        self.create = to_streamed_response_wrapper(
            export_image.create,
        )


class AsyncExportImageResourceWithStreamingResponse:
    def __init__(self, export_image: AsyncExportImageResource) -> None:
        self._export_image = export_image

        self.create = async_to_streamed_response_wrapper(
            export_image.create,
        )
