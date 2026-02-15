# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.emails import RenderCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRender:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        render = client.emails.render.create(
            project_id="projectId",
            design={"foo": "bar"},
        )
        assert_matches_type(RenderCreateResponse, render, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        render = client.emails.render.create(
            project_id="projectId",
            design={"foo": "bar"},
            merge_tags={"foo": "string"},
        )
        assert_matches_type(RenderCreateResponse, render, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.emails.render.with_raw_response.create(
            project_id="projectId",
            design={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        render = response.parse()
        assert_matches_type(RenderCreateResponse, render, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.emails.render.with_streaming_response.create(
            project_id="projectId",
            design={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            render = response.parse()
            assert_matches_type(RenderCreateResponse, render, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRender:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        render = await async_client.emails.render.create(
            project_id="projectId",
            design={"foo": "bar"},
        )
        assert_matches_type(RenderCreateResponse, render, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        render = await async_client.emails.render.create(
            project_id="projectId",
            design={"foo": "bar"},
            merge_tags={"foo": "string"},
        )
        assert_matches_type(RenderCreateResponse, render, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.render.with_raw_response.create(
            project_id="projectId",
            design={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        render = await response.parse()
        assert_matches_type(RenderCreateResponse, render, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.render.with_streaming_response.create(
            project_id="projectId",
            design={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            render = await response.parse()
            assert_matches_type(RenderCreateResponse, render, path=["response"])

        assert cast(Any, response.is_closed) is True
