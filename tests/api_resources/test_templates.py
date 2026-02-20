# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import TemplateListResponse, TemplateRetrieveResponse
from unlayer.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        template = client.templates.retrieve(
            id="id",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unlayer) -> None:
        template = client.templates.retrieve(
            id="id",
            project_id="projectId",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.templates.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.templates.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unlayer) -> None:
        template = client.templates.list()
        assert_matches_type(SyncCursorPage[TemplateListResponse], template, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unlayer) -> None:
        template = client.templates.list(
            cursor="cursor",
            display_mode="email",
            limit=1,
            name="name",
            project_id="projectId",
        )
        assert_matches_type(SyncCursorPage[TemplateListResponse], template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unlayer) -> None:
        response = client.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(SyncCursorPage[TemplateListResponse], template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unlayer) -> None:
        with client.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(SyncCursorPage[TemplateListResponse], template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        template = await async_client.templates.retrieve(
            id="id",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnlayer) -> None:
        template = await async_client.templates.retrieve(
            id="id",
            project_id="projectId",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.templates.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.templates.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnlayer) -> None:
        template = await async_client.templates.list()
        assert_matches_type(AsyncCursorPage[TemplateListResponse], template, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnlayer) -> None:
        template = await async_client.templates.list(
            cursor="cursor",
            display_mode="email",
            limit=1,
            name="name",
            project_id="projectId",
        )
        assert_matches_type(AsyncCursorPage[TemplateListResponse], template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.templates.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(AsyncCursorPage[TemplateListResponse], template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.templates.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(AsyncCursorPage[TemplateListResponse], template, path=["response"])

        assert cast(Any, response.is_closed) is True
