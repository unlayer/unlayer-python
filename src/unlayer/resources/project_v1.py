# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    project_v1_domains_create_params,
    project_v1_domains_update_params,
    project_v1_api_keys_create_params,
    project_v1_api_keys_update_params,
    project_v1_templates_create_params,
    project_v1_templates_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.project_v1_current_list_response import ProjectV1CurrentListResponse
from ..types.project_v1_domains_list_response import ProjectV1DomainsListResponse
from ..types.project_v1_api_keys_list_response import ProjectV1APIKeysListResponse
from ..types.project_v1_domains_create_response import ProjectV1DomainsCreateResponse
from ..types.project_v1_domains_update_response import ProjectV1DomainsUpdateResponse
from ..types.project_v1_templates_list_response import ProjectV1TemplatesListResponse
from ..types.project_v1_api_keys_create_response import ProjectV1APIKeysCreateResponse
from ..types.project_v1_api_keys_update_response import ProjectV1APIKeysUpdateResponse
from ..types.project_v1_domains_retrieve_response import ProjectV1DomainsRetrieveResponse
from ..types.project_v1_templates_create_response import ProjectV1TemplatesCreateResponse
from ..types.project_v1_templates_update_response import ProjectV1TemplatesUpdateResponse
from ..types.project_v1_api_keys_retrieve_response import ProjectV1APIKeysRetrieveResponse
from ..types.project_v1_templates_retrieve_response import ProjectV1TemplatesRetrieveResponse

__all__ = ["ProjectV1Resource", "AsyncProjectV1Resource"]


class ProjectV1Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ProjectV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return ProjectV1ResourceWithStreamingResponse(self)

    def api_keys_create(
        self,
        *,
        name: str,
        domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysCreateResponse:
        """
        Create a new API key for the project.

        Args:
          name: Name for the API key

          domains: Allowed domains for this API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/project/v1/api-keys",
            body=maybe_transform(
                {
                    "name": name,
                    "domains": domains,
                },
                project_v1_api_keys_create_params.ProjectV1APIKeysCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysCreateResponse,
        )

    def api_keys_delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revoke API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/project/v1/api-keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def api_keys_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysListResponse:
        """List all API keys for the project."""
        return self._get(
            "/project/v1/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysListResponse,
        )

    def api_keys_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysRetrieveResponse:
        """
        Get API key details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/project/v1/api-keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysRetrieveResponse,
        )

    def api_keys_update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysUpdateResponse:
        """
        Update API key settings.

        Args:
          active: Whether the API key is active

          domains: Updated allowed domains

          name: Updated name for the API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/project/v1/api-keys/{id}",
            body=maybe_transform(
                {
                    "active": active,
                    "domains": domains,
                    "name": name,
                },
                project_v1_api_keys_update_params.ProjectV1APIKeysUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysUpdateResponse,
        )

    def current_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1CurrentListResponse:
        """Get project details for the authenticated project."""
        return self._get(
            "/project/v1/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1CurrentListResponse,
        )

    def domains_create(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsCreateResponse:
        """
        Add a new domain to the project.

        Args:
          domain: Domain name to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/project/v1/domains",
            body=maybe_transform({"domain": domain}, project_v1_domains_create_params.ProjectV1DomainsCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsCreateResponse,
        )

    def domains_delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove domain from project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/project/v1/domains/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def domains_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsListResponse:
        """List all domains for the project."""
        return self._get(
            "/project/v1/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsListResponse,
        )

    def domains_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsRetrieveResponse:
        """
        Get domain details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/project/v1/domains/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsRetrieveResponse,
        )

    def domains_update(
        self,
        id: str,
        *,
        domain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsUpdateResponse:
        """
        Update domain settings.

        Args:
          domain: Updated domain name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/project/v1/domains/{id}",
            body=maybe_transform({"domain": domain}, project_v1_domains_update_params.ProjectV1DomainsUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsUpdateResponse,
        )

    def templates_create(
        self,
        *,
        name: str,
        body: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesCreateResponse:
        """
        Create a new project template.

        Args:
          name: Template name

          body: Email body content

          subject: Email subject line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/project/v1/templates",
            body=maybe_transform(
                {
                    "name": name,
                    "body": body,
                    "subject": subject,
                },
                project_v1_templates_create_params.ProjectV1TemplatesCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesCreateResponse,
        )

    def templates_delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete project template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/project/v1/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def templates_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesListResponse:
        """Get all project templates."""
        return self._get(
            "/project/v1/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesListResponse,
        )

    def templates_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesRetrieveResponse:
        """
        Get project template by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/project/v1/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesRetrieveResponse,
        )

    def templates_update(
        self,
        id: str,
        *,
        body: str | Omit = omit,
        name: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesUpdateResponse:
        """
        Update project template.

        Args:
          body: Updated email body content

          name: Updated template name

          subject: Updated email subject line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/project/v1/templates/{id}",
            body=maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "subject": subject,
                },
                project_v1_templates_update_params.ProjectV1TemplatesUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesUpdateResponse,
        )


class AsyncProjectV1Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncProjectV1ResourceWithStreamingResponse(self)

    async def api_keys_create(
        self,
        *,
        name: str,
        domains: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysCreateResponse:
        """
        Create a new API key for the project.

        Args:
          name: Name for the API key

          domains: Allowed domains for this API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/project/v1/api-keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "domains": domains,
                },
                project_v1_api_keys_create_params.ProjectV1APIKeysCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysCreateResponse,
        )

    async def api_keys_delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revoke API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/project/v1/api-keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def api_keys_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysListResponse:
        """List all API keys for the project."""
        return await self._get(
            "/project/v1/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysListResponse,
        )

    async def api_keys_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysRetrieveResponse:
        """
        Get API key details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/project/v1/api-keys/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysRetrieveResponse,
        )

    async def api_keys_update(
        self,
        id: str,
        *,
        active: bool | Omit = omit,
        domains: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1APIKeysUpdateResponse:
        """
        Update API key settings.

        Args:
          active: Whether the API key is active

          domains: Updated allowed domains

          name: Updated name for the API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/project/v1/api-keys/{id}",
            body=await async_maybe_transform(
                {
                    "active": active,
                    "domains": domains,
                    "name": name,
                },
                project_v1_api_keys_update_params.ProjectV1APIKeysUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1APIKeysUpdateResponse,
        )

    async def current_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1CurrentListResponse:
        """Get project details for the authenticated project."""
        return await self._get(
            "/project/v1/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1CurrentListResponse,
        )

    async def domains_create(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsCreateResponse:
        """
        Add a new domain to the project.

        Args:
          domain: Domain name to add

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/project/v1/domains",
            body=await async_maybe_transform(
                {"domain": domain}, project_v1_domains_create_params.ProjectV1DomainsCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsCreateResponse,
        )

    async def domains_delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove domain from project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/project/v1/domains/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def domains_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsListResponse:
        """List all domains for the project."""
        return await self._get(
            "/project/v1/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsListResponse,
        )

    async def domains_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsRetrieveResponse:
        """
        Get domain details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/project/v1/domains/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsRetrieveResponse,
        )

    async def domains_update(
        self,
        id: str,
        *,
        domain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1DomainsUpdateResponse:
        """
        Update domain settings.

        Args:
          domain: Updated domain name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/project/v1/domains/{id}",
            body=await async_maybe_transform(
                {"domain": domain}, project_v1_domains_update_params.ProjectV1DomainsUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1DomainsUpdateResponse,
        )

    async def templates_create(
        self,
        *,
        name: str,
        body: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesCreateResponse:
        """
        Create a new project template.

        Args:
          name: Template name

          body: Email body content

          subject: Email subject line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/project/v1/templates",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "body": body,
                    "subject": subject,
                },
                project_v1_templates_create_params.ProjectV1TemplatesCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesCreateResponse,
        )

    async def templates_delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete project template.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/project/v1/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def templates_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesListResponse:
        """Get all project templates."""
        return await self._get(
            "/project/v1/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesListResponse,
        )

    async def templates_retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesRetrieveResponse:
        """
        Get project template by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/project/v1/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesRetrieveResponse,
        )

    async def templates_update(
        self,
        id: str,
        *,
        body: str | Omit = omit,
        name: str | Omit = omit,
        subject: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectV1TemplatesUpdateResponse:
        """
        Update project template.

        Args:
          body: Updated email body content

          name: Updated template name

          subject: Updated email subject line

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/project/v1/templates/{id}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "name": name,
                    "subject": subject,
                },
                project_v1_templates_update_params.ProjectV1TemplatesUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectV1TemplatesUpdateResponse,
        )


class ProjectV1ResourceWithRawResponse:
    def __init__(self, project_v1: ProjectV1Resource) -> None:
        self._project_v1 = project_v1

        self.api_keys_create = to_raw_response_wrapper(
            project_v1.api_keys_create,
        )
        self.api_keys_delete = to_raw_response_wrapper(
            project_v1.api_keys_delete,
        )
        self.api_keys_list = to_raw_response_wrapper(
            project_v1.api_keys_list,
        )
        self.api_keys_retrieve = to_raw_response_wrapper(
            project_v1.api_keys_retrieve,
        )
        self.api_keys_update = to_raw_response_wrapper(
            project_v1.api_keys_update,
        )
        self.current_list = to_raw_response_wrapper(
            project_v1.current_list,
        )
        self.domains_create = to_raw_response_wrapper(
            project_v1.domains_create,
        )
        self.domains_delete = to_raw_response_wrapper(
            project_v1.domains_delete,
        )
        self.domains_list = to_raw_response_wrapper(
            project_v1.domains_list,
        )
        self.domains_retrieve = to_raw_response_wrapper(
            project_v1.domains_retrieve,
        )
        self.domains_update = to_raw_response_wrapper(
            project_v1.domains_update,
        )
        self.templates_create = to_raw_response_wrapper(
            project_v1.templates_create,
        )
        self.templates_delete = to_raw_response_wrapper(
            project_v1.templates_delete,
        )
        self.templates_list = to_raw_response_wrapper(
            project_v1.templates_list,
        )
        self.templates_retrieve = to_raw_response_wrapper(
            project_v1.templates_retrieve,
        )
        self.templates_update = to_raw_response_wrapper(
            project_v1.templates_update,
        )


class AsyncProjectV1ResourceWithRawResponse:
    def __init__(self, project_v1: AsyncProjectV1Resource) -> None:
        self._project_v1 = project_v1

        self.api_keys_create = async_to_raw_response_wrapper(
            project_v1.api_keys_create,
        )
        self.api_keys_delete = async_to_raw_response_wrapper(
            project_v1.api_keys_delete,
        )
        self.api_keys_list = async_to_raw_response_wrapper(
            project_v1.api_keys_list,
        )
        self.api_keys_retrieve = async_to_raw_response_wrapper(
            project_v1.api_keys_retrieve,
        )
        self.api_keys_update = async_to_raw_response_wrapper(
            project_v1.api_keys_update,
        )
        self.current_list = async_to_raw_response_wrapper(
            project_v1.current_list,
        )
        self.domains_create = async_to_raw_response_wrapper(
            project_v1.domains_create,
        )
        self.domains_delete = async_to_raw_response_wrapper(
            project_v1.domains_delete,
        )
        self.domains_list = async_to_raw_response_wrapper(
            project_v1.domains_list,
        )
        self.domains_retrieve = async_to_raw_response_wrapper(
            project_v1.domains_retrieve,
        )
        self.domains_update = async_to_raw_response_wrapper(
            project_v1.domains_update,
        )
        self.templates_create = async_to_raw_response_wrapper(
            project_v1.templates_create,
        )
        self.templates_delete = async_to_raw_response_wrapper(
            project_v1.templates_delete,
        )
        self.templates_list = async_to_raw_response_wrapper(
            project_v1.templates_list,
        )
        self.templates_retrieve = async_to_raw_response_wrapper(
            project_v1.templates_retrieve,
        )
        self.templates_update = async_to_raw_response_wrapper(
            project_v1.templates_update,
        )


class ProjectV1ResourceWithStreamingResponse:
    def __init__(self, project_v1: ProjectV1Resource) -> None:
        self._project_v1 = project_v1

        self.api_keys_create = to_streamed_response_wrapper(
            project_v1.api_keys_create,
        )
        self.api_keys_delete = to_streamed_response_wrapper(
            project_v1.api_keys_delete,
        )
        self.api_keys_list = to_streamed_response_wrapper(
            project_v1.api_keys_list,
        )
        self.api_keys_retrieve = to_streamed_response_wrapper(
            project_v1.api_keys_retrieve,
        )
        self.api_keys_update = to_streamed_response_wrapper(
            project_v1.api_keys_update,
        )
        self.current_list = to_streamed_response_wrapper(
            project_v1.current_list,
        )
        self.domains_create = to_streamed_response_wrapper(
            project_v1.domains_create,
        )
        self.domains_delete = to_streamed_response_wrapper(
            project_v1.domains_delete,
        )
        self.domains_list = to_streamed_response_wrapper(
            project_v1.domains_list,
        )
        self.domains_retrieve = to_streamed_response_wrapper(
            project_v1.domains_retrieve,
        )
        self.domains_update = to_streamed_response_wrapper(
            project_v1.domains_update,
        )
        self.templates_create = to_streamed_response_wrapper(
            project_v1.templates_create,
        )
        self.templates_delete = to_streamed_response_wrapper(
            project_v1.templates_delete,
        )
        self.templates_list = to_streamed_response_wrapper(
            project_v1.templates_list,
        )
        self.templates_retrieve = to_streamed_response_wrapper(
            project_v1.templates_retrieve,
        )
        self.templates_update = to_streamed_response_wrapper(
            project_v1.templates_update,
        )


class AsyncProjectV1ResourceWithStreamingResponse:
    def __init__(self, project_v1: AsyncProjectV1Resource) -> None:
        self._project_v1 = project_v1

        self.api_keys_create = async_to_streamed_response_wrapper(
            project_v1.api_keys_create,
        )
        self.api_keys_delete = async_to_streamed_response_wrapper(
            project_v1.api_keys_delete,
        )
        self.api_keys_list = async_to_streamed_response_wrapper(
            project_v1.api_keys_list,
        )
        self.api_keys_retrieve = async_to_streamed_response_wrapper(
            project_v1.api_keys_retrieve,
        )
        self.api_keys_update = async_to_streamed_response_wrapper(
            project_v1.api_keys_update,
        )
        self.current_list = async_to_streamed_response_wrapper(
            project_v1.current_list,
        )
        self.domains_create = async_to_streamed_response_wrapper(
            project_v1.domains_create,
        )
        self.domains_delete = async_to_streamed_response_wrapper(
            project_v1.domains_delete,
        )
        self.domains_list = async_to_streamed_response_wrapper(
            project_v1.domains_list,
        )
        self.domains_retrieve = async_to_streamed_response_wrapper(
            project_v1.domains_retrieve,
        )
        self.domains_update = async_to_streamed_response_wrapper(
            project_v1.domains_update,
        )
        self.templates_create = async_to_streamed_response_wrapper(
            project_v1.templates_create,
        )
        self.templates_delete = async_to_streamed_response_wrapper(
            project_v1.templates_delete,
        )
        self.templates_list = async_to_streamed_response_wrapper(
            project_v1.templates_list,
        )
        self.templates_retrieve = async_to_streamed_response_wrapper(
            project_v1.templates_retrieve,
        )
        self.templates_update = async_to_streamed_response_wrapper(
            project_v1.templates_update,
        )
