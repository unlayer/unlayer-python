# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.documents import generate_template_create_params
from ...types.documents.generate_template_create_response import GenerateTemplateCreateResponse

__all__ = ["GenerateTemplateResource", "AsyncGenerateTemplateResource"]


class GenerateTemplateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return GenerateTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return GenerateTemplateResourceWithStreamingResponse(self)

    def create(
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
    ) -> GenerateTemplateCreateResponse:
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
                generate_template_create_params.GenerateTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"project_id": project_id}, generate_template_create_params.GenerateTemplateCreateParams
                ),
            ),
            cast_to=GenerateTemplateCreateResponse,
        )


class AsyncGenerateTemplateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncGenerateTemplateResourceWithStreamingResponse(self)

    async def create(
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
    ) -> GenerateTemplateCreateResponse:
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
                generate_template_create_params.GenerateTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, generate_template_create_params.GenerateTemplateCreateParams
                ),
            ),
            cast_to=GenerateTemplateCreateResponse,
        )


class GenerateTemplateResourceWithRawResponse:
    def __init__(self, generate_template: GenerateTemplateResource) -> None:
        self._generate_template = generate_template

        self.create = to_raw_response_wrapper(
            generate_template.create,
        )


class AsyncGenerateTemplateResourceWithRawResponse:
    def __init__(self, generate_template: AsyncGenerateTemplateResource) -> None:
        self._generate_template = generate_template

        self.create = async_to_raw_response_wrapper(
            generate_template.create,
        )


class GenerateTemplateResourceWithStreamingResponse:
    def __init__(self, generate_template: GenerateTemplateResource) -> None:
        self._generate_template = generate_template

        self.create = to_streamed_response_wrapper(
            generate_template.create,
        )


class AsyncGenerateTemplateResourceWithStreamingResponse:
    def __init__(self, generate_template: AsyncGenerateTemplateResource) -> None:
        self._generate_template = generate_template

        self.create = async_to_streamed_response_wrapper(
            generate_template.create,
        )
