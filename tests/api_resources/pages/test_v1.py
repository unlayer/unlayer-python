# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.pages import V1RenderCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_render_create(self, client: Unlayer) -> None:
        v1 = client.pages.v1.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

    @parametrize
    def test_method_render_create_with_all_params(self, client: Unlayer) -> None:
        v1 = client.pages.v1.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            merge_tags={"foo": "string"},
        )
        assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_render_create(self, client: Unlayer) -> None:
        response = client.pages.v1.with_raw_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_render_create(self, client: Unlayer) -> None:
        with client.pages.v1.with_streaming_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_render_create(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.pages.v1.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

    @parametrize
    async def test_method_render_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.pages.v1.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            merge_tags={"foo": "string"},
        )
        assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_render_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.pages.v1.with_raw_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_render_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.pages.v1.with_streaming_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1RenderCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
