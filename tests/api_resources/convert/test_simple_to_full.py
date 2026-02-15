# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.convert import SimpleToFullCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimpleToFull:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        simple_to_full = client.convert.simple_to_full.create(
            design={"body": {}},
        )
        assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        simple_to_full = client.convert.simple_to_full.create(
            design={
                "body": {},
                "_conversion": {
                    "data": "data",
                    "version": 0,
                },
                "counters": {},
                "schema_version": 0,
            },
            display_mode="email",
            include_default_values=True,
        )
        assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.convert.simple_to_full.with_raw_response.create(
            design={"body": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple_to_full = response.parse()
        assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.convert.simple_to_full.with_streaming_response.create(
            design={"body": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple_to_full = response.parse()
            assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimpleToFull:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        simple_to_full = await async_client.convert.simple_to_full.create(
            design={"body": {}},
        )
        assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        simple_to_full = await async_client.convert.simple_to_full.create(
            design={
                "body": {},
                "_conversion": {
                    "data": "data",
                    "version": 0,
                },
                "counters": {},
                "schema_version": 0,
            },
            display_mode="email",
            include_default_values=True,
        )
        assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.convert.simple_to_full.with_raw_response.create(
            design={"body": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simple_to_full = await response.parse()
        assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.convert.simple_to_full.with_streaming_response.create(
            design={"body": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simple_to_full = await response.parse()
            assert_matches_type(SimpleToFullCreateResponse, simple_to_full, path=["response"])

        assert cast(Any, response.is_closed) is True
