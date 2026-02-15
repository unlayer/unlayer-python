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
from ...types.emails import send_template_create_params
from ...types.emails.send_template_create_response import SendTemplateCreateResponse

__all__ = ["SendTemplateResource", "AsyncSendTemplateResource"]


class SendTemplateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SendTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return SendTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SendTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return SendTemplateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        project_id: str,
        template_id: str,
        to: str,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SendTemplateCreateResponse:
        """
        Send email using an existing template with merge tags.

        Args:
          project_id: The project ID

          template_id: ID of the template to use

          to: Recipient email address

          merge_tags: Optional merge tags for personalization

          subject: Email subject line (optional, uses template default if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/emails/v1/send/template",
            body=maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                send_template_create_params.SendTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, send_template_create_params.SendTemplateCreateParams),
            ),
            cast_to=SendTemplateCreateResponse,
        )


class AsyncSendTemplateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSendTemplateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSendTemplateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSendTemplateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncSendTemplateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        project_id: str,
        template_id: str,
        to: str,
        merge_tags: Dict[str, str] | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SendTemplateCreateResponse:
        """
        Send email using an existing template with merge tags.

        Args:
          project_id: The project ID

          template_id: ID of the template to use

          to: Recipient email address

          merge_tags: Optional merge tags for personalization

          subject: Email subject line (optional, uses template default if not provided)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/emails/v1/send/template",
            body=await async_maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "merge_tags": merge_tags,
                    "subject": subject,
                },
                send_template_create_params.SendTemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, send_template_create_params.SendTemplateCreateParams
                ),
            ),
            cast_to=SendTemplateCreateResponse,
        )


class SendTemplateResourceWithRawResponse:
    def __init__(self, send_template: SendTemplateResource) -> None:
        self._send_template = send_template

        self.create = to_raw_response_wrapper(
            send_template.create,
        )


class AsyncSendTemplateResourceWithRawResponse:
    def __init__(self, send_template: AsyncSendTemplateResource) -> None:
        self._send_template = send_template

        self.create = async_to_raw_response_wrapper(
            send_template.create,
        )


class SendTemplateResourceWithStreamingResponse:
    def __init__(self, send_template: SendTemplateResource) -> None:
        self._send_template = send_template

        self.create = to_streamed_response_wrapper(
            send_template.create,
        )


class AsyncSendTemplateResourceWithStreamingResponse:
    def __init__(self, send_template: AsyncSendTemplateResource) -> None:
        self._send_template = send_template

        self.create = async_to_streamed_response_wrapper(
            send_template.create,
        )
