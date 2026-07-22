# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from .ai_credits import (
    AICreditsResource,
    AsyncAICreditsResource,
    AICreditsResourceWithRawResponse,
    AsyncAICreditsResourceWithRawResponse,
    AICreditsResourceWithStreamingResponse,
    AsyncAICreditsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .ai_credits_usage import (
    AICreditsUsageResource,
    AsyncAICreditsUsageResource,
    AICreditsUsageResourceWithRawResponse,
    AsyncAICreditsUsageResourceWithRawResponse,
    AICreditsUsageResourceWithStreamingResponse,
    AsyncAICreditsUsageResourceWithStreamingResponse,
)
from .ai_credits_settings import (
    AICreditsSettingsResource,
    AsyncAICreditsSettingsResource,
    AICreditsSettingsResourceWithRawResponse,
    AsyncAICreditsSettingsResourceWithRawResponse,
    AICreditsSettingsResourceWithStreamingResponse,
    AsyncAICreditsSettingsResourceWithStreamingResponse,
)
from .ai_credits_webhooks_deliveries import (
    AICreditsWebhooksDeliveriesResource,
    AsyncAICreditsWebhooksDeliveriesResource,
    AICreditsWebhooksDeliveriesResourceWithRawResponse,
    AsyncAICreditsWebhooksDeliveriesResourceWithRawResponse,
    AICreditsWebhooksDeliveriesResourceWithStreamingResponse,
    AsyncAICreditsWebhooksDeliveriesResourceWithStreamingResponse,
)
from ...types.project_retrieve_response import ProjectRetrieveResponse
from .ai_credits_settings_rotate_secret import (
    AICreditsSettingsRotateSecretResource,
    AsyncAICreditsSettingsRotateSecretResource,
    AICreditsSettingsRotateSecretResourceWithRawResponse,
    AsyncAICreditsSettingsRotateSecretResourceWithRawResponse,
    AICreditsSettingsRotateSecretResourceWithStreamingResponse,
    AsyncAICreditsSettingsRotateSecretResourceWithStreamingResponse,
)
from .ai_credits_webhooks_deliveriesretry import (
    AICreditsWebhooksDeliveriesretryResource,
    AsyncAICreditsWebhooksDeliveriesretryResource,
    AICreditsWebhooksDeliveriesretryResourceWithRawResponse,
    AsyncAICreditsWebhooksDeliveriesretryResourceWithRawResponse,
    AICreditsWebhooksDeliveriesretryResourceWithStreamingResponse,
    AsyncAICreditsWebhooksDeliveriesretryResourceWithStreamingResponse,
)
from .ai_credits_webhooks_deliveriesattempts import (
    AICreditsWebhooksDeliveriesattemptsResource,
    AsyncAICreditsWebhooksDeliveriesattemptsResource,
    AICreditsWebhooksDeliveriesattemptsResourceWithRawResponse,
    AsyncAICreditsWebhooksDeliveriesattemptsResourceWithRawResponse,
    AICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse,
    AsyncAICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse,
)

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    """Project details and configuration."""

    @cached_property
    def ai_credits(self) -> AICreditsResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsResource(self._client)

    @cached_property
    def ai_credits_settings(self) -> AICreditsSettingsResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsSettingsResource(self._client)

    @cached_property
    def ai_credits_settings_rotate_secret(self) -> AICreditsSettingsRotateSecretResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsSettingsRotateSecretResource(self._client)

    @cached_property
    def ai_credits_usage(self) -> AICreditsUsageResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsUsageResource(self._client)

    @cached_property
    def ai_credits_webhooks_deliveries(self) -> AICreditsWebhooksDeliveriesResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesResource(self._client)

    @cached_property
    def ai_credits_webhooks_deliveriesattempts(self) -> AICreditsWebhooksDeliveriesattemptsResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesattemptsResource(self._client)

    @cached_property
    def ai_credits_webhooks_deliveriesretry(self) -> AICreditsWebhooksDeliveriesretryResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesretryResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Get project details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v3/projects/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )


class AsyncProjectsResource(AsyncAPIResource):
    """Project details and configuration."""

    @cached_property
    def ai_credits(self) -> AsyncAICreditsResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsResource(self._client)

    @cached_property
    def ai_credits_settings(self) -> AsyncAICreditsSettingsResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsSettingsResource(self._client)

    @cached_property
    def ai_credits_settings_rotate_secret(self) -> AsyncAICreditsSettingsRotateSecretResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsSettingsRotateSecretResource(self._client)

    @cached_property
    def ai_credits_usage(self) -> AsyncAICreditsUsageResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsUsageResource(self._client)

    @cached_property
    def ai_credits_webhooks_deliveries(self) -> AsyncAICreditsWebhooksDeliveriesResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesResource(self._client)

    @cached_property
    def ai_credits_webhooks_deliveriesattempts(self) -> AsyncAICreditsWebhooksDeliveriesattemptsResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesattemptsResource(self._client)

    @cached_property
    def ai_credits_webhooks_deliveriesretry(self) -> AsyncAICreditsWebhooksDeliveriesretryResource:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesretryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Get project details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v3/projects/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.retrieve = to_raw_response_wrapper(
            projects.retrieve,
        )

    @cached_property
    def ai_credits(self) -> AICreditsResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsResourceWithRawResponse(self._projects.ai_credits)

    @cached_property
    def ai_credits_settings(self) -> AICreditsSettingsResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsSettingsResourceWithRawResponse(self._projects.ai_credits_settings)

    @cached_property
    def ai_credits_settings_rotate_secret(self) -> AICreditsSettingsRotateSecretResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsSettingsRotateSecretResourceWithRawResponse(self._projects.ai_credits_settings_rotate_secret)

    @cached_property
    def ai_credits_usage(self) -> AICreditsUsageResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsUsageResourceWithRawResponse(self._projects.ai_credits_usage)

    @cached_property
    def ai_credits_webhooks_deliveries(self) -> AICreditsWebhooksDeliveriesResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesResourceWithRawResponse(self._projects.ai_credits_webhooks_deliveries)

    @cached_property
    def ai_credits_webhooks_deliveriesattempts(self) -> AICreditsWebhooksDeliveriesattemptsResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesattemptsResourceWithRawResponse(
            self._projects.ai_credits_webhooks_deliveriesattempts
        )

    @cached_property
    def ai_credits_webhooks_deliveriesretry(self) -> AICreditsWebhooksDeliveriesretryResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesretryResourceWithRawResponse(
            self._projects.ai_credits_webhooks_deliveriesretry
        )


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )

    @cached_property
    def ai_credits(self) -> AsyncAICreditsResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsResourceWithRawResponse(self._projects.ai_credits)

    @cached_property
    def ai_credits_settings(self) -> AsyncAICreditsSettingsResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsSettingsResourceWithRawResponse(self._projects.ai_credits_settings)

    @cached_property
    def ai_credits_settings_rotate_secret(self) -> AsyncAICreditsSettingsRotateSecretResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsSettingsRotateSecretResourceWithRawResponse(
            self._projects.ai_credits_settings_rotate_secret
        )

    @cached_property
    def ai_credits_usage(self) -> AsyncAICreditsUsageResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsUsageResourceWithRawResponse(self._projects.ai_credits_usage)

    @cached_property
    def ai_credits_webhooks_deliveries(self) -> AsyncAICreditsWebhooksDeliveriesResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesResourceWithRawResponse(self._projects.ai_credits_webhooks_deliveries)

    @cached_property
    def ai_credits_webhooks_deliveriesattempts(self) -> AsyncAICreditsWebhooksDeliveriesattemptsResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesattemptsResourceWithRawResponse(
            self._projects.ai_credits_webhooks_deliveriesattempts
        )

    @cached_property
    def ai_credits_webhooks_deliveriesretry(self) -> AsyncAICreditsWebhooksDeliveriesretryResourceWithRawResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesretryResourceWithRawResponse(
            self._projects.ai_credits_webhooks_deliveriesretry
        )


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )

    @cached_property
    def ai_credits(self) -> AICreditsResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsResourceWithStreamingResponse(self._projects.ai_credits)

    @cached_property
    def ai_credits_settings(self) -> AICreditsSettingsResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsSettingsResourceWithStreamingResponse(self._projects.ai_credits_settings)

    @cached_property
    def ai_credits_settings_rotate_secret(self) -> AICreditsSettingsRotateSecretResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsSettingsRotateSecretResourceWithStreamingResponse(
            self._projects.ai_credits_settings_rotate_secret
        )

    @cached_property
    def ai_credits_usage(self) -> AICreditsUsageResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsUsageResourceWithStreamingResponse(self._projects.ai_credits_usage)

    @cached_property
    def ai_credits_webhooks_deliveries(self) -> AICreditsWebhooksDeliveriesResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesResourceWithStreamingResponse(self._projects.ai_credits_webhooks_deliveries)

    @cached_property
    def ai_credits_webhooks_deliveriesattempts(
        self,
    ) -> AICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse(
            self._projects.ai_credits_webhooks_deliveriesattempts
        )

    @cached_property
    def ai_credits_webhooks_deliveriesretry(self) -> AICreditsWebhooksDeliveriesretryResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AICreditsWebhooksDeliveriesretryResourceWithStreamingResponse(
            self._projects.ai_credits_webhooks_deliveriesretry
        )


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )

    @cached_property
    def ai_credits(self) -> AsyncAICreditsResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsResourceWithStreamingResponse(self._projects.ai_credits)

    @cached_property
    def ai_credits_settings(self) -> AsyncAICreditsSettingsResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsSettingsResourceWithStreamingResponse(self._projects.ai_credits_settings)

    @cached_property
    def ai_credits_settings_rotate_secret(self) -> AsyncAICreditsSettingsRotateSecretResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsSettingsRotateSecretResourceWithStreamingResponse(
            self._projects.ai_credits_settings_rotate_secret
        )

    @cached_property
    def ai_credits_usage(self) -> AsyncAICreditsUsageResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsUsageResourceWithStreamingResponse(self._projects.ai_credits_usage)

    @cached_property
    def ai_credits_webhooks_deliveries(self) -> AsyncAICreditsWebhooksDeliveriesResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesResourceWithStreamingResponse(
            self._projects.ai_credits_webhooks_deliveries
        )

    @cached_property
    def ai_credits_webhooks_deliveriesattempts(
        self,
    ) -> AsyncAICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesattemptsResourceWithStreamingResponse(
            self._projects.ai_credits_webhooks_deliveriesattempts
        )

    @cached_property
    def ai_credits_webhooks_deliveriesretry(self) -> AsyncAICreditsWebhooksDeliveriesretryResourceWithStreamingResponse:
        """AI credit balance, usage breakdown, and webhook/alert settings.

        Credits are pooled per workspace; settings are per project.
        """
        return AsyncAICreditsWebhooksDeliveriesretryResourceWithStreamingResponse(
            self._projects.ai_credits_webhooks_deliveriesretry
        )
