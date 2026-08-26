# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.emails import SuppressionsCheckRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuppressionsCheck:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        suppressions_check = client.emails.suppressions_check.retrieve(
            email="email",
        )
        assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unlayer) -> None:
        suppressions_check = client.emails.suppressions_check.retrieve(
            email="email",
            project_id="projectId",
        )
        assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.emails.suppressions_check.with_raw_response.retrieve(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppressions_check = response.parse()
        assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.emails.suppressions_check.with_streaming_response.retrieve(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppressions_check = response.parse()
            assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSuppressionsCheck:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        suppressions_check = await async_client.emails.suppressions_check.retrieve(
            email="email",
        )
        assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnlayer) -> None:
        suppressions_check = await async_client.emails.suppressions_check.retrieve(
            email="email",
            project_id="projectId",
        )
        assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.suppressions_check.with_raw_response.retrieve(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppressions_check = await response.parse()
        assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.suppressions_check.with_streaming_response.retrieve(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppressions_check = await response.parse()
            assert_matches_type(SuppressionsCheckRetrieveResponse, suppressions_check, path=["response"])

        assert cast(Any, response.is_closed) is True
