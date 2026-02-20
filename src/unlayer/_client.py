# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import convert, project, templates, workspaces
    from .resources.project import ProjectResource, AsyncProjectResource
    from .resources.templates import TemplatesResource, AsyncTemplatesResource
    from .resources.workspaces import WorkspacesResource, AsyncWorkspacesResource
    from .resources.convert.convert import ConvertResource, AsyncConvertResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Unlayer", "AsyncUnlayer", "Client", "AsyncClient"]


class Unlayer(SyncAPIClient):
    # client options
    api_key: str | None
    personal_access_token: str | None
    project_id: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        personal_access_token: str | None = None,
        project_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Unlayer client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `UNLAYER_API_KEY`
        - `personal_access_token` from `UNLAYER_PERSONAL_ACCESS_TOKEN`
        - `project_id` from `UNLAYER_PROJECT_ID`
        """
        if api_key is None:
            api_key = os.environ.get("UNLAYER_API_KEY")
        self.api_key = api_key

        if personal_access_token is None:
            personal_access_token = os.environ.get("UNLAYER_PERSONAL_ACCESS_TOKEN")
        self.personal_access_token = personal_access_token

        if project_id is None:
            project_id = os.environ.get("UNLAYER_PROJECT_ID")
        self.project_id = project_id

        if base_url is None:
            base_url = os.environ.get("UNLAYER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.unlayer.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def convert(self) -> ConvertResource:
        from .resources.convert import ConvertResource

        return ConvertResource(self)

    @cached_property
    def project(self) -> ProjectResource:
        from .resources.project import ProjectResource

        return ProjectResource(self)

    @cached_property
    def templates(self) -> TemplatesResource:
        from .resources.templates import TemplatesResource

        return TemplatesResource(self)

    @cached_property
    def workspaces(self) -> WorkspacesResource:
        from .resources.workspaces import WorkspacesResource

        return WorkspacesResource(self)

    @cached_property
    def with_raw_response(self) -> UnlayerWithRawResponse:
        return UnlayerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UnlayerWithStreamedResponse:
        return UnlayerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._personal_access_token_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _personal_access_token_auth(self) -> dict[str, str]:
        personal_access_token = self.personal_access_token
        if personal_access_token is None:
            return {}
        return {"Authorization": f"Bearer {personal_access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "X-Project-ID": self.project_id if self.project_id is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or personal_access_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        personal_access_token: str | None = None,
        project_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            personal_access_token=personal_access_token or self.personal_access_token,
            project_id=project_id or self.project_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncUnlayer(AsyncAPIClient):
    # client options
    api_key: str | None
    personal_access_token: str | None
    project_id: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        personal_access_token: str | None = None,
        project_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncUnlayer client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `UNLAYER_API_KEY`
        - `personal_access_token` from `UNLAYER_PERSONAL_ACCESS_TOKEN`
        - `project_id` from `UNLAYER_PROJECT_ID`
        """
        if api_key is None:
            api_key = os.environ.get("UNLAYER_API_KEY")
        self.api_key = api_key

        if personal_access_token is None:
            personal_access_token = os.environ.get("UNLAYER_PERSONAL_ACCESS_TOKEN")
        self.personal_access_token = personal_access_token

        if project_id is None:
            project_id = os.environ.get("UNLAYER_PROJECT_ID")
        self.project_id = project_id

        if base_url is None:
            base_url = os.environ.get("UNLAYER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.unlayer.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def convert(self) -> AsyncConvertResource:
        from .resources.convert import AsyncConvertResource

        return AsyncConvertResource(self)

    @cached_property
    def project(self) -> AsyncProjectResource:
        from .resources.project import AsyncProjectResource

        return AsyncProjectResource(self)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        from .resources.templates import AsyncTemplatesResource

        return AsyncTemplatesResource(self)

    @cached_property
    def workspaces(self) -> AsyncWorkspacesResource:
        from .resources.workspaces import AsyncWorkspacesResource

        return AsyncWorkspacesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncUnlayerWithRawResponse:
        return AsyncUnlayerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUnlayerWithStreamedResponse:
        return AsyncUnlayerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._api_key_auth, **self._personal_access_token_auth}

    @property
    def _api_key_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    def _personal_access_token_auth(self) -> dict[str, str]:
        personal_access_token = self.personal_access_token
        if personal_access_token is None:
            return {}
        return {"Authorization": f"Bearer {personal_access_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "X-Project-ID": self.project_id if self.project_id is not None else Omit(),
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key or personal_access_token to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        personal_access_token: str | None = None,
        project_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            personal_access_token=personal_access_token or self.personal_access_token,
            project_id=project_id or self.project_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class UnlayerWithRawResponse:
    _client: Unlayer

    def __init__(self, client: Unlayer) -> None:
        self._client = client

    @cached_property
    def convert(self) -> convert.ConvertResourceWithRawResponse:
        from .resources.convert import ConvertResourceWithRawResponse

        return ConvertResourceWithRawResponse(self._client.convert)

    @cached_property
    def project(self) -> project.ProjectResourceWithRawResponse:
        from .resources.project import ProjectResourceWithRawResponse

        return ProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithRawResponse:
        from .resources.templates import TemplatesResourceWithRawResponse

        return TemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def workspaces(self) -> workspaces.WorkspacesResourceWithRawResponse:
        from .resources.workspaces import WorkspacesResourceWithRawResponse

        return WorkspacesResourceWithRawResponse(self._client.workspaces)


class AsyncUnlayerWithRawResponse:
    _client: AsyncUnlayer

    def __init__(self, client: AsyncUnlayer) -> None:
        self._client = client

    @cached_property
    def convert(self) -> convert.AsyncConvertResourceWithRawResponse:
        from .resources.convert import AsyncConvertResourceWithRawResponse

        return AsyncConvertResourceWithRawResponse(self._client.convert)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithRawResponse:
        from .resources.project import AsyncProjectResourceWithRawResponse

        return AsyncProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithRawResponse:
        from .resources.templates import AsyncTemplatesResourceWithRawResponse

        return AsyncTemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def workspaces(self) -> workspaces.AsyncWorkspacesResourceWithRawResponse:
        from .resources.workspaces import AsyncWorkspacesResourceWithRawResponse

        return AsyncWorkspacesResourceWithRawResponse(self._client.workspaces)


class UnlayerWithStreamedResponse:
    _client: Unlayer

    def __init__(self, client: Unlayer) -> None:
        self._client = client

    @cached_property
    def convert(self) -> convert.ConvertResourceWithStreamingResponse:
        from .resources.convert import ConvertResourceWithStreamingResponse

        return ConvertResourceWithStreamingResponse(self._client.convert)

    @cached_property
    def project(self) -> project.ProjectResourceWithStreamingResponse:
        from .resources.project import ProjectResourceWithStreamingResponse

        return ProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithStreamingResponse:
        from .resources.templates import TemplatesResourceWithStreamingResponse

        return TemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def workspaces(self) -> workspaces.WorkspacesResourceWithStreamingResponse:
        from .resources.workspaces import WorkspacesResourceWithStreamingResponse

        return WorkspacesResourceWithStreamingResponse(self._client.workspaces)


class AsyncUnlayerWithStreamedResponse:
    _client: AsyncUnlayer

    def __init__(self, client: AsyncUnlayer) -> None:
        self._client = client

    @cached_property
    def convert(self) -> convert.AsyncConvertResourceWithStreamingResponse:
        from .resources.convert import AsyncConvertResourceWithStreamingResponse

        return AsyncConvertResourceWithStreamingResponse(self._client.convert)

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithStreamingResponse:
        from .resources.project import AsyncProjectResourceWithStreamingResponse

        return AsyncProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithStreamingResponse:
        from .resources.templates import AsyncTemplatesResourceWithStreamingResponse

        return AsyncTemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def workspaces(self) -> workspaces.AsyncWorkspacesResourceWithStreamingResponse:
        from .resources.workspaces import AsyncWorkspacesResourceWithStreamingResponse

        return AsyncWorkspacesResourceWithStreamingResponse(self._client.workspaces)


Client = Unlayer

AsyncClient = AsyncUnlayer
