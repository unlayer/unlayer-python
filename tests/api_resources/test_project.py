# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import (
    ProjectCurrentListResponse,
    ProjectDomainsListResponse,
    ProjectDomainsCreateResponse,
    ProjectDomainsUpdateResponse,
    ProjectTemplatesListResponse,
    ProjectWorkspacesListResponse,
    ProjectDomainsRetrieveResponse,
    ProjectTemplatesCreateResponse,
    ProjectTemplatesUpdateResponse,
    ProjectTemplatesRetrieveResponse,
    ProjectWorkspacesRetrieveResponse,
)
from unlayer.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProject:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_current_list(self, client: Unlayer) -> None:
        project = client.project.current_list(
            project_id="projectId",
        )
        assert_matches_type(ProjectCurrentListResponse, project, path=["response"])

    @parametrize
    def test_raw_response_current_list(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.current_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCurrentListResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_current_list(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.current_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCurrentListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_domains_create(self, client: Unlayer) -> None:
        project = client.project.domains_create(
            project_id="projectId",
            domain="domain",
        )
        assert_matches_type(ProjectDomainsCreateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_domains_create(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.domains_create(
            project_id="projectId",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectDomainsCreateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_domains_create(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.domains_create(
            project_id="projectId",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectDomainsCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_domains_delete(self, client: Unlayer) -> None:
        project = client.project.domains_delete(
            "id",
        )
        assert project is None

    @parametrize
    def test_raw_response_domains_delete(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.domains_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_domains_delete(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.domains_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_domains_delete(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.with_raw_response.domains_delete(
                "",
            )

    @parametrize
    def test_method_domains_list(self, client: Unlayer) -> None:
        project = client.project.domains_list(
            project_id="projectId",
        )
        assert_matches_type(ProjectDomainsListResponse, project, path=["response"])

    @parametrize
    def test_raw_response_domains_list(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.domains_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectDomainsListResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_domains_list(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.domains_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectDomainsListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_domains_retrieve(self, client: Unlayer) -> None:
        project = client.project.domains_retrieve(
            "id",
        )
        assert_matches_type(ProjectDomainsRetrieveResponse, project, path=["response"])

    @parametrize
    def test_raw_response_domains_retrieve(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.domains_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectDomainsRetrieveResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_domains_retrieve(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.domains_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectDomainsRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_domains_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.with_raw_response.domains_retrieve(
                "",
            )

    @parametrize
    def test_method_domains_update(self, client: Unlayer) -> None:
        project = client.project.domains_update(
            id="id",
        )
        assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

    @parametrize
    def test_method_domains_update_with_all_params(self, client: Unlayer) -> None:
        project = client.project.domains_update(
            id="id",
            domain="domain",
        )
        assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_domains_update(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.domains_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_domains_update(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.domains_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_domains_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.with_raw_response.domains_update(
                id="",
            )

    @parametrize
    def test_method_templates_create(self, client: Unlayer) -> None:
        project = client.project.templates_create(
            project_id="projectId",
            name="name",
        )
        assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

    @parametrize
    def test_method_templates_create_with_all_params(self, client: Unlayer) -> None:
        project = client.project.templates_create(
            project_id="projectId",
            name="name",
            display_mode="email",
        )
        assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_templates_create(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.templates_create(
            project_id="projectId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_templates_create(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.templates_create(
            project_id="projectId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_templates_delete(self, client: Unlayer) -> None:
        project = client.project.templates_delete(
            "id",
        )
        assert project is None

    @parametrize
    def test_raw_response_templates_delete(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.templates_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert project is None

    @parametrize
    def test_streaming_response_templates_delete(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.templates_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_templates_delete(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.with_raw_response.templates_delete(
                "",
            )

    @parametrize
    def test_method_templates_list(self, client: Unlayer) -> None:
        project = client.project.templates_list(
            project_id="projectId",
        )
        assert_matches_type(SyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

    @parametrize
    def test_method_templates_list_with_all_params(self, client: Unlayer) -> None:
        project = client.project.templates_list(
            project_id="projectId",
            cursor="cursor",
            display_mode="email",
            limit=1,
            name="name",
        )
        assert_matches_type(SyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

    @parametrize
    def test_raw_response_templates_list(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.templates_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(SyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

    @parametrize
    def test_streaming_response_templates_list(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.templates_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(SyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_templates_retrieve(self, client: Unlayer) -> None:
        project = client.project.templates_retrieve(
            "id",
        )
        assert_matches_type(ProjectTemplatesRetrieveResponse, project, path=["response"])

    @parametrize
    def test_raw_response_templates_retrieve(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.templates_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectTemplatesRetrieveResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_templates_retrieve(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.templates_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectTemplatesRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_templates_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.with_raw_response.templates_retrieve(
                "",
            )

    @parametrize
    def test_method_templates_update(self, client: Unlayer) -> None:
        project = client.project.templates_update(
            id="id",
        )
        assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

    @parametrize
    def test_method_templates_update_with_all_params(self, client: Unlayer) -> None:
        project = client.project.templates_update(
            id="id",
            body="body",
            name="name",
            subject="subject",
        )
        assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_templates_update(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.templates_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_templates_update(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.templates_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_templates_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.with_raw_response.templates_update(
                id="",
            )

    @parametrize
    def test_method_workspaces_list(self, client: Unlayer) -> None:
        project = client.project.workspaces_list()
        assert_matches_type(ProjectWorkspacesListResponse, project, path=["response"])

    @parametrize
    def test_raw_response_workspaces_list(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.workspaces_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectWorkspacesListResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_workspaces_list(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.workspaces_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectWorkspacesListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_workspaces_retrieve(self, client: Unlayer) -> None:
        project = client.project.workspaces_retrieve(
            "workspaceId",
        )
        assert_matches_type(ProjectWorkspacesRetrieveResponse, project, path=["response"])

    @parametrize
    def test_raw_response_workspaces_retrieve(self, client: Unlayer) -> None:
        response = client.project.with_raw_response.workspaces_retrieve(
            "workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectWorkspacesRetrieveResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_workspaces_retrieve(self, client: Unlayer) -> None:
        with client.project.with_streaming_response.workspaces_retrieve(
            "workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectWorkspacesRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_workspaces_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.project.with_raw_response.workspaces_retrieve(
                "",
            )


class TestAsyncProject:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_current_list(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.current_list(
            project_id="projectId",
        )
        assert_matches_type(ProjectCurrentListResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_current_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.current_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCurrentListResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_current_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.current_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCurrentListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_domains_create(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.domains_create(
            project_id="projectId",
            domain="domain",
        )
        assert_matches_type(ProjectDomainsCreateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_domains_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.domains_create(
            project_id="projectId",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectDomainsCreateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_domains_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.domains_create(
            project_id="projectId",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectDomainsCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_domains_delete(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.domains_delete(
            "id",
        )
        assert project is None

    @parametrize
    async def test_raw_response_domains_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.domains_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_domains_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.domains_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_domains_delete(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.with_raw_response.domains_delete(
                "",
            )

    @parametrize
    async def test_method_domains_list(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.domains_list(
            project_id="projectId",
        )
        assert_matches_type(ProjectDomainsListResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_domains_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.domains_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectDomainsListResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_domains_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.domains_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectDomainsListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.domains_retrieve(
            "id",
        )
        assert_matches_type(ProjectDomainsRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.domains_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectDomainsRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.domains_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectDomainsRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.with_raw_response.domains_retrieve(
                "",
            )

    @parametrize
    async def test_method_domains_update(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.domains_update(
            id="id",
        )
        assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

    @parametrize
    async def test_method_domains_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.domains_update(
            id="id",
            domain="domain",
        )
        assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_domains_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.domains_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_domains_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.domains_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectDomainsUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_domains_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.with_raw_response.domains_update(
                id="",
            )

    @parametrize
    async def test_method_templates_create(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_create(
            project_id="projectId",
            name="name",
        )
        assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

    @parametrize
    async def test_method_templates_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_create(
            project_id="projectId",
            name="name",
            display_mode="email",
        )
        assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_templates_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.templates_create(
            project_id="projectId",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_templates_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.templates_create(
            project_id="projectId",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectTemplatesCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_templates_delete(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_delete(
            "id",
        )
        assert project is None

    @parametrize
    async def test_raw_response_templates_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.templates_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert project is None

    @parametrize
    async def test_streaming_response_templates_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.templates_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert project is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_templates_delete(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.with_raw_response.templates_delete(
                "",
            )

    @parametrize
    async def test_method_templates_list(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_list(
            project_id="projectId",
        )
        assert_matches_type(AsyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

    @parametrize
    async def test_method_templates_list_with_all_params(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_list(
            project_id="projectId",
            cursor="cursor",
            display_mode="email",
            limit=1,
            name="name",
        )
        assert_matches_type(AsyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

    @parametrize
    async def test_raw_response_templates_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.templates_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(AsyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

    @parametrize
    async def test_streaming_response_templates_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.templates_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(AsyncCursorPage[ProjectTemplatesListResponse], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_retrieve(
            "id",
        )
        assert_matches_type(ProjectTemplatesRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.templates_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectTemplatesRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.templates_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectTemplatesRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.with_raw_response.templates_retrieve(
                "",
            )

    @parametrize
    async def test_method_templates_update(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_update(
            id="id",
        )
        assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

    @parametrize
    async def test_method_templates_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.templates_update(
            id="id",
            body="body",
            name="name",
            subject="subject",
        )
        assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_templates_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.templates_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_templates_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.templates_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectTemplatesUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_templates_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.with_raw_response.templates_update(
                id="",
            )

    @parametrize
    async def test_method_workspaces_list(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.workspaces_list()
        assert_matches_type(ProjectWorkspacesListResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_workspaces_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.workspaces_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectWorkspacesListResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_workspaces_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.workspaces_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectWorkspacesListResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_workspaces_retrieve(self, async_client: AsyncUnlayer) -> None:
        project = await async_client.project.workspaces_retrieve(
            "workspaceId",
        )
        assert_matches_type(ProjectWorkspacesRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_workspaces_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.with_raw_response.workspaces_retrieve(
            "workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectWorkspacesRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_workspaces_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.with_streaming_response.workspaces_retrieve(
            "workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectWorkspacesRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_workspaces_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.project.with_raw_response.workspaces_retrieve(
                "",
            )
