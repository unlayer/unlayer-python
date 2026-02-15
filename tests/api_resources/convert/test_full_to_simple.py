# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.convert import FullToSimpleCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFullToSimple:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        full_to_simple = client.convert.full_to_simple.create(
            design={"body": {}},
        )
        assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        full_to_simple = client.convert.full_to_simple.create(
            design={
                "body": {},
                "counters": {},
                "schema_version": 0,
            },
            display_mode="email",
            include_default_values=True,
        )
        assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.convert.full_to_simple.with_raw_response.create(
            design={"body": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full_to_simple = response.parse()
        assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.convert.full_to_simple.with_streaming_response.create(
            design={"body": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full_to_simple = response.parse()
            assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFullToSimple:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        full_to_simple = await async_client.convert.full_to_simple.create(
            design={"body": {}},
        )
        assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        full_to_simple = await async_client.convert.full_to_simple.create(
            design={
                "body": {},
                "counters": {},
                "schema_version": 0,
            },
            display_mode="email",
            include_default_values=True,
        )
        assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.convert.full_to_simple.with_raw_response.create(
            design={"body": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        full_to_simple = await response.parse()
        assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.convert.full_to_simple.with_streaming_response.create(
            design={"body": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            full_to_simple = await response.parse()
            assert_matches_type(FullToSimpleCreateResponse, full_to_simple, path=["response"])

        assert cast(Any, response.is_closed) is True
