# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.emails import StatRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        stat = client.emails.stats.retrieve()
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unlayer) -> None:
        stat = client.emails.stats.retrieve(
            group_by="day",
            period="7d",
            project_id="projectId",
        )
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.emails.stats.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = response.parse()
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.emails.stats.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = response.parse()
            assert_matches_type(StatRetrieveResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStats:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        stat = await async_client.emails.stats.retrieve()
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnlayer) -> None:
        stat = await async_client.emails.stats.retrieve(
            group_by="day",
            period="7d",
            project_id="projectId",
        )
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.stats.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stat = await response.parse()
        assert_matches_type(StatRetrieveResponse, stat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.stats.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stat = await response.parse()
            assert_matches_type(StatRetrieveResponse, stat, path=["response"])

        assert cast(Any, response.is_closed) is True
