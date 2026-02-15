# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.project import WorkspaceListResponse, WorkspaceRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        workspace = client.project.workspaces.retrieve(
            "workspaceId",
        )
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.project.workspaces.with_raw_response.retrieve(
            "workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.project.workspaces.with_streaming_response.retrieve(
            "workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.project.workspaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Unlayer) -> None:
        workspace = client.project.workspaces.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unlayer) -> None:
        response = client.project.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unlayer) -> None:
        with client.project.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        workspace = await async_client.project.workspaces.retrieve(
            "workspaceId",
        )
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.workspaces.with_raw_response.retrieve(
            "workspaceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.workspaces.with_streaming_response.retrieve(
            "workspaceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceRetrieveResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.project.workspaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnlayer) -> None:
        workspace = await async_client.project.workspaces.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True
