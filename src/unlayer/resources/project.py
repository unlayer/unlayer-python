# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    project_domains_create_params,
    project_domains_update_params,
    project_api_keys_create_params,
    project_api_keys_update_params,
    project_templates_create_params,
    project_templates_update_params,
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
from ..types.project_current_list_response import ProjectCurrentListResponse
from ..types.project_domains_list_response import ProjectDomainsListResponse
from ..types.project_api_keys_list_response import ProjectAPIKeysListResponse
from ..types.project_domains_create_response import ProjectDomainsCreateResponse
from ..types.project_domains_update_response import ProjectDomainsUpdateResponse
from ..types.project_templates_list_response import ProjectTemplatesListResponse
from ..types.project_api_keys_create_response import ProjectAPIKeysCreateResponse
from ..types.project_api_keys_update_response import ProjectAPIKeysUpdateResponse
from ..types.project_domains_retrieve_response import ProjectDomainsRetrieveResponse
from ..types.project_templates_create_response import ProjectTemplatesCreateResponse
from ..types.project_templates_update_response import ProjectTemplatesUpdateResponse
from ..types.project_api_keys_retrieve_response import ProjectAPIKeysRetrieveResponse
from ..types.project_templates_retrieve_response import ProjectTemplatesRetrieveResponse

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return ProjectResourceWithStreamingResponse(self)

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
    ) -> ProjectAPIKeysCreateResponse:
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
                project_api_keys_create_params.ProjectAPIKeysCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectAPIKeysCreateResponse,
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
    ) -> ProjectAPIKeysListResponse:
        """List all API keys for the project."""
        return self._get(
            "/project/v1/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectAPIKeysListResponse,
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
    ) -> ProjectAPIKeysRetrieveResponse:
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
            cast_to=ProjectAPIKeysRetrieveResponse,
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
    ) -> ProjectAPIKeysUpdateResponse:
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
                project_api_keys_update_params.ProjectAPIKeysUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectAPIKeysUpdateResponse,
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
    ) -> ProjectCurrentListResponse:
        """Get project details for the authenticated project."""
        return self._get(
            "/project/v1/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCurrentListResponse,
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
    ) -> ProjectDomainsCreateResponse:
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
            body=maybe_transform({"domain": domain}, project_domains_create_params.ProjectDomainsCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDomainsCreateResponse,
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
    ) -> ProjectDomainsListResponse:
        """List all domains for the project."""
        return self._get(
            "/project/v1/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDomainsListResponse,
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
    ) -> ProjectDomainsRetrieveResponse:
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
            cast_to=ProjectDomainsRetrieveResponse,
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
    ) -> ProjectDomainsUpdateResponse:
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
            body=maybe_transform({"domain": domain}, project_domains_update_params.ProjectDomainsUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDomainsUpdateResponse,
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
    ) -> ProjectTemplatesCreateResponse:
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
                project_templates_create_params.ProjectTemplatesCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTemplatesCreateResponse,
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
    ) -> ProjectTemplatesListResponse:
        """Get all project templates."""
        return self._get(
            "/project/v1/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTemplatesListResponse,
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
    ) -> ProjectTemplatesRetrieveResponse:
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
            cast_to=ProjectTemplatesRetrieveResponse,
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
    ) -> ProjectTemplatesUpdateResponse:
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
                project_templates_update_params.ProjectTemplatesUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTemplatesUpdateResponse,
        )


class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/unlayer-python#with_streaming_response
        """
        return AsyncProjectResourceWithStreamingResponse(self)

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
    ) -> ProjectAPIKeysCreateResponse:
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
                project_api_keys_create_params.ProjectAPIKeysCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectAPIKeysCreateResponse,
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
    ) -> ProjectAPIKeysListResponse:
        """List all API keys for the project."""
        return await self._get(
            "/project/v1/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectAPIKeysListResponse,
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
    ) -> ProjectAPIKeysRetrieveResponse:
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
            cast_to=ProjectAPIKeysRetrieveResponse,
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
    ) -> ProjectAPIKeysUpdateResponse:
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
                project_api_keys_update_params.ProjectAPIKeysUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectAPIKeysUpdateResponse,
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
    ) -> ProjectCurrentListResponse:
        """Get project details for the authenticated project."""
        return await self._get(
            "/project/v1/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCurrentListResponse,
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
    ) -> ProjectDomainsCreateResponse:
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
                {"domain": domain}, project_domains_create_params.ProjectDomainsCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDomainsCreateResponse,
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
    ) -> ProjectDomainsListResponse:
        """List all domains for the project."""
        return await self._get(
            "/project/v1/domains",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDomainsListResponse,
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
    ) -> ProjectDomainsRetrieveResponse:
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
            cast_to=ProjectDomainsRetrieveResponse,
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
    ) -> ProjectDomainsUpdateResponse:
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
                {"domain": domain}, project_domains_update_params.ProjectDomainsUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectDomainsUpdateResponse,
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
    ) -> ProjectTemplatesCreateResponse:
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
                project_templates_create_params.ProjectTemplatesCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTemplatesCreateResponse,
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
    ) -> ProjectTemplatesListResponse:
        """Get all project templates."""
        return await self._get(
            "/project/v1/templates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTemplatesListResponse,
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
    ) -> ProjectTemplatesRetrieveResponse:
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
            cast_to=ProjectTemplatesRetrieveResponse,
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
    ) -> ProjectTemplatesUpdateResponse:
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
                project_templates_update_params.ProjectTemplatesUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectTemplatesUpdateResponse,
        )


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.api_keys_create = to_raw_response_wrapper(
            project.api_keys_create,
        )
        self.api_keys_delete = to_raw_response_wrapper(
            project.api_keys_delete,
        )
        self.api_keys_list = to_raw_response_wrapper(
            project.api_keys_list,
        )
        self.api_keys_retrieve = to_raw_response_wrapper(
            project.api_keys_retrieve,
        )
        self.api_keys_update = to_raw_response_wrapper(
            project.api_keys_update,
        )
        self.current_list = to_raw_response_wrapper(
            project.current_list,
        )
        self.domains_create = to_raw_response_wrapper(
            project.domains_create,
        )
        self.domains_delete = to_raw_response_wrapper(
            project.domains_delete,
        )
        self.domains_list = to_raw_response_wrapper(
            project.domains_list,
        )
        self.domains_retrieve = to_raw_response_wrapper(
            project.domains_retrieve,
        )
        self.domains_update = to_raw_response_wrapper(
            project.domains_update,
        )
        self.templates_create = to_raw_response_wrapper(
            project.templates_create,
        )
        self.templates_delete = to_raw_response_wrapper(
            project.templates_delete,
        )
        self.templates_list = to_raw_response_wrapper(
            project.templates_list,
        )
        self.templates_retrieve = to_raw_response_wrapper(
            project.templates_retrieve,
        )
        self.templates_update = to_raw_response_wrapper(
            project.templates_update,
        )


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.api_keys_create = async_to_raw_response_wrapper(
            project.api_keys_create,
        )
        self.api_keys_delete = async_to_raw_response_wrapper(
            project.api_keys_delete,
        )
        self.api_keys_list = async_to_raw_response_wrapper(
            project.api_keys_list,
        )
        self.api_keys_retrieve = async_to_raw_response_wrapper(
            project.api_keys_retrieve,
        )
        self.api_keys_update = async_to_raw_response_wrapper(
            project.api_keys_update,
        )
        self.current_list = async_to_raw_response_wrapper(
            project.current_list,
        )
        self.domains_create = async_to_raw_response_wrapper(
            project.domains_create,
        )
        self.domains_delete = async_to_raw_response_wrapper(
            project.domains_delete,
        )
        self.domains_list = async_to_raw_response_wrapper(
            project.domains_list,
        )
        self.domains_retrieve = async_to_raw_response_wrapper(
            project.domains_retrieve,
        )
        self.domains_update = async_to_raw_response_wrapper(
            project.domains_update,
        )
        self.templates_create = async_to_raw_response_wrapper(
            project.templates_create,
        )
        self.templates_delete = async_to_raw_response_wrapper(
            project.templates_delete,
        )
        self.templates_list = async_to_raw_response_wrapper(
            project.templates_list,
        )
        self.templates_retrieve = async_to_raw_response_wrapper(
            project.templates_retrieve,
        )
        self.templates_update = async_to_raw_response_wrapper(
            project.templates_update,
        )


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

        self.api_keys_create = to_streamed_response_wrapper(
            project.api_keys_create,
        )
        self.api_keys_delete = to_streamed_response_wrapper(
            project.api_keys_delete,
        )
        self.api_keys_list = to_streamed_response_wrapper(
            project.api_keys_list,
        )
        self.api_keys_retrieve = to_streamed_response_wrapper(
            project.api_keys_retrieve,
        )
        self.api_keys_update = to_streamed_response_wrapper(
            project.api_keys_update,
        )
        self.current_list = to_streamed_response_wrapper(
            project.current_list,
        )
        self.domains_create = to_streamed_response_wrapper(
            project.domains_create,
        )
        self.domains_delete = to_streamed_response_wrapper(
            project.domains_delete,
        )
        self.domains_list = to_streamed_response_wrapper(
            project.domains_list,
        )
        self.domains_retrieve = to_streamed_response_wrapper(
            project.domains_retrieve,
        )
        self.domains_update = to_streamed_response_wrapper(
            project.domains_update,
        )
        self.templates_create = to_streamed_response_wrapper(
            project.templates_create,
        )
        self.templates_delete = to_streamed_response_wrapper(
            project.templates_delete,
        )
        self.templates_list = to_streamed_response_wrapper(
            project.templates_list,
        )
        self.templates_retrieve = to_streamed_response_wrapper(
            project.templates_retrieve,
        )
        self.templates_update = to_streamed_response_wrapper(
            project.templates_update,
        )


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

        self.api_keys_create = async_to_streamed_response_wrapper(
            project.api_keys_create,
        )
        self.api_keys_delete = async_to_streamed_response_wrapper(
            project.api_keys_delete,
        )
        self.api_keys_list = async_to_streamed_response_wrapper(
            project.api_keys_list,
        )
        self.api_keys_retrieve = async_to_streamed_response_wrapper(
            project.api_keys_retrieve,
        )
        self.api_keys_update = async_to_streamed_response_wrapper(
            project.api_keys_update,
        )
        self.current_list = async_to_streamed_response_wrapper(
            project.current_list,
        )
        self.domains_create = async_to_streamed_response_wrapper(
            project.domains_create,
        )
        self.domains_delete = async_to_streamed_response_wrapper(
            project.domains_delete,
        )
        self.domains_list = async_to_streamed_response_wrapper(
            project.domains_list,
        )
        self.domains_retrieve = async_to_streamed_response_wrapper(
            project.domains_retrieve,
        )
        self.domains_update = async_to_streamed_response_wrapper(
            project.domains_update,
        )
        self.templates_create = async_to_streamed_response_wrapper(
            project.templates_create,
        )
        self.templates_delete = async_to_streamed_response_wrapper(
            project.templates_delete,
        )
        self.templates_list = async_to_streamed_response_wrapper(
            project.templates_list,
        )
        self.templates_retrieve = async_to_streamed_response_wrapper(
            project.templates_retrieve,
        )
        self.templates_update = async_to_streamed_response_wrapper(
            project.templates_update,
        )
