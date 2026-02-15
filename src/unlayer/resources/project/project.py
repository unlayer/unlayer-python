# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .current import (
    CurrentResource,
    AsyncCurrentResource,
    CurrentResourceWithRawResponse,
    AsyncCurrentResourceWithRawResponse,
    CurrentResourceWithStreamingResponse,
    AsyncCurrentResourceWithStreamingResponse,
)
from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from .workspaces import (
    WorkspacesResource,
    AsyncWorkspacesResource,
    WorkspacesResourceWithRawResponse,
    AsyncWorkspacesResourceWithRawResponse,
    WorkspacesResourceWithStreamingResponse,
    AsyncWorkspacesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ProjectResource", "AsyncProjectResource"]


class ProjectResource(SyncAPIResource):
    @cached_property
    def current(self) -> CurrentResource:
        return CurrentResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def workspaces(self) -> WorkspacesResource:
        return WorkspacesResource(self._client)

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


class AsyncProjectResource(AsyncAPIResource):
    @cached_property
    def current(self) -> AsyncCurrentResource:
        return AsyncCurrentResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResource:
        return AsyncWorkspacesResource(self._client)

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


class ProjectResourceWithRawResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

    @cached_property
    def current(self) -> CurrentResourceWithRawResponse:
        return CurrentResourceWithRawResponse(self._project.current)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._project.domains)

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._project.templates)

    @cached_property
    def workspaces(self) -> WorkspacesResourceWithRawResponse:
        return WorkspacesResourceWithRawResponse(self._project.workspaces)


class AsyncProjectResourceWithRawResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def current(self) -> AsyncCurrentResourceWithRawResponse:
        return AsyncCurrentResourceWithRawResponse(self._project.current)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._project.domains)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._project.templates)

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResourceWithRawResponse:
        return AsyncWorkspacesResourceWithRawResponse(self._project.workspaces)


class ProjectResourceWithStreamingResponse:
    def __init__(self, project: ProjectResource) -> None:
        self._project = project

    @cached_property
    def current(self) -> CurrentResourceWithStreamingResponse:
        return CurrentResourceWithStreamingResponse(self._project.current)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._project.domains)

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._project.templates)

    @cached_property
    def workspaces(self) -> WorkspacesResourceWithStreamingResponse:
        return WorkspacesResourceWithStreamingResponse(self._project.workspaces)


class AsyncProjectResourceWithStreamingResponse:
    def __init__(self, project: AsyncProjectResource) -> None:
        self._project = project

    @cached_property
    def current(self) -> AsyncCurrentResourceWithStreamingResponse:
        return AsyncCurrentResourceWithStreamingResponse(self._project.current)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._project.domains)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._project.templates)

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResourceWithStreamingResponse:
        return AsyncWorkspacesResourceWithStreamingResponse(self._project.workspaces)
