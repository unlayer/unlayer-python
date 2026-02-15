# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .send import (
    SendResource,
    AsyncSendResource,
    SendResourceWithRawResponse,
    AsyncSendResourceWithRawResponse,
    SendResourceWithStreamingResponse,
    AsyncSendResourceWithStreamingResponse,
)
from .render import (
    RenderResource,
    AsyncRenderResource,
    RenderResourceWithRawResponse,
    AsyncRenderResourceWithRawResponse,
    RenderResourceWithStreamingResponse,
    AsyncRenderResourceWithStreamingResponse,
)
from ...types import email_retrieve_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .send_template import (
    SendTemplateResource,
    AsyncSendTemplateResource,
    SendTemplateResourceWithRawResponse,
    AsyncSendTemplateResourceWithRawResponse,
    SendTemplateResourceWithStreamingResponse,
    AsyncSendTemplateResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.email_retrieve_response import EmailRetrieveResponse

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def render(self) -> RenderResource:
        return RenderResource(self._client)

    @cached_property
    def send(self) -> SendResource:
        return SendResource(self._client)

    @cached_property
    def send_template(self) -> SendTemplateResource:
        return SendTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)

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
    ) -> EmailRetrieveResponse:
        """
        Retrieve details of a previously sent email.

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
            f"/emails/v1/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"project_id": project_id}, email_retrieve_params.EmailRetrieveParams),
            ),
            cast_to=EmailRetrieveResponse,
        )


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def render(self) -> AsyncRenderResource:
        return AsyncRenderResource(self._client)

    @cached_property
    def send(self) -> AsyncSendResource:
        return AsyncSendResource(self._client)

    @cached_property
    def send_template(self) -> AsyncSendTemplateResource:
        return AsyncSendTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)

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
    ) -> EmailRetrieveResponse:
        """
        Retrieve details of a previously sent email.

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
            f"/emails/v1/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"project_id": project_id}, email_retrieve_params.EmailRetrieveParams
                ),
            ),
            cast_to=EmailRetrieveResponse,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.retrieve = to_raw_response_wrapper(
            emails.retrieve,
        )

    @cached_property
    def render(self) -> RenderResourceWithRawResponse:
        return RenderResourceWithRawResponse(self._emails.render)

    @cached_property
    def send(self) -> SendResourceWithRawResponse:
        return SendResourceWithRawResponse(self._emails.send)

    @cached_property
    def send_template(self) -> SendTemplateResourceWithRawResponse:
        return SendTemplateResourceWithRawResponse(self._emails.send_template)


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.retrieve = async_to_raw_response_wrapper(
            emails.retrieve,
        )

    @cached_property
    def render(self) -> AsyncRenderResourceWithRawResponse:
        return AsyncRenderResourceWithRawResponse(self._emails.render)

    @cached_property
    def send(self) -> AsyncSendResourceWithRawResponse:
        return AsyncSendResourceWithRawResponse(self._emails.send)

    @cached_property
    def send_template(self) -> AsyncSendTemplateResourceWithRawResponse:
        return AsyncSendTemplateResourceWithRawResponse(self._emails.send_template)


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.retrieve = to_streamed_response_wrapper(
            emails.retrieve,
        )

    @cached_property
    def render(self) -> RenderResourceWithStreamingResponse:
        return RenderResourceWithStreamingResponse(self._emails.render)

    @cached_property
    def send(self) -> SendResourceWithStreamingResponse:
        return SendResourceWithStreamingResponse(self._emails.send)

    @cached_property
    def send_template(self) -> SendTemplateResourceWithStreamingResponse:
        return SendTemplateResourceWithStreamingResponse(self._emails.send_template)


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.retrieve = async_to_streamed_response_wrapper(
            emails.retrieve,
        )

    @cached_property
    def render(self) -> AsyncRenderResourceWithStreamingResponse:
        return AsyncRenderResourceWithStreamingResponse(self._emails.render)

    @cached_property
    def send(self) -> AsyncSendResourceWithStreamingResponse:
        return AsyncSendResourceWithStreamingResponse(self._emails.send)

    @cached_property
    def send_template(self) -> AsyncSendTemplateResourceWithStreamingResponse:
        return AsyncSendTemplateResourceWithStreamingResponse(self._emails.send_template)
