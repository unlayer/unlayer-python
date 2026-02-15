# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.project import CurrentRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        current = client.project.current.retrieve(
            project_id="projectId",
        )
        assert_matches_type(CurrentRetrieveResponse, current, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.project.current.with_raw_response.retrieve(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current = response.parse()
        assert_matches_type(CurrentRetrieveResponse, current, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.project.current.with_streaming_response.retrieve(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current = response.parse()
            assert_matches_type(CurrentRetrieveResponse, current, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        current = await async_client.project.current.retrieve(
            project_id="projectId",
        )
        assert_matches_type(CurrentRetrieveResponse, current, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.current.with_raw_response.retrieve(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        current = await response.parse()
        assert_matches_type(CurrentRetrieveResponse, current, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.current.with_streaming_response.retrieve(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            current = await response.parse()
            assert_matches_type(CurrentRetrieveResponse, current, path=["response"])

        assert cast(Any, response.is_closed) is True
