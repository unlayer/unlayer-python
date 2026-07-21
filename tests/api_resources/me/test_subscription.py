# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.me import SubscriptionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscription:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        subscription = client.me.subscription.retrieve()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unlayer) -> None:
        subscription = client.me.subscription.retrieve(
            project_id="projectId",
        )
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.me.subscription.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.me.subscription.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscription:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        subscription = await async_client.me.subscription.retrieve()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnlayer) -> None:
        subscription = await async_client.me.subscription.retrieve(
            project_id="projectId",
        )
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.me.subscription.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.me.subscription.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionRetrieveResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True
