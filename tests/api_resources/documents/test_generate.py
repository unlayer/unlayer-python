# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.documents import GenerateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        generate = client.documents.generate.create(
            project_id="projectId",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        generate = client.documents.generate.create(
            project_id="projectId",
            design={"foo": "bar"},
            filename="filename",
            html="html",
            merge_tags={"foo": "string"},
            url="https://example.com",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.documents.generate.with_raw_response.create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.documents.generate.with_streaming_response.create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateCreateResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        generate = await async_client.documents.generate.create(
            project_id="projectId",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        generate = await async_client.documents.generate.create(
            project_id="projectId",
            design={"foo": "bar"},
            filename="filename",
            html="html",
            merge_tags={"foo": "string"},
            url="https://example.com",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents.generate.with_raw_response.create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents.generate.with_streaming_response.create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateCreateResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True
