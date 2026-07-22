# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.projects import AICreditsWebhooksDeliveriesretryCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAICreditsWebhooksDeliveriesretry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        ai_credits_webhooks_deliveriesretry = client.projects.ai_credits_webhooks_deliveriesretry.create(
            delivery_id="deliveryId",
            id="id",
        )
        assert_matches_type(
            AICreditsWebhooksDeliveriesretryCreateResponse, ai_credits_webhooks_deliveriesretry, path=["response"]
        )

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.projects.ai_credits_webhooks_deliveriesretry.with_raw_response.create(
            delivery_id="deliveryId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_credits_webhooks_deliveriesretry = response.parse()
        assert_matches_type(
            AICreditsWebhooksDeliveriesretryCreateResponse, ai_credits_webhooks_deliveriesretry, path=["response"]
        )

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.projects.ai_credits_webhooks_deliveriesretry.with_streaming_response.create(
            delivery_id="deliveryId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_credits_webhooks_deliveriesretry = response.parse()
            assert_matches_type(
                AICreditsWebhooksDeliveriesretryCreateResponse, ai_credits_webhooks_deliveriesretry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.projects.ai_credits_webhooks_deliveriesretry.with_raw_response.create(
                delivery_id="deliveryId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.projects.ai_credits_webhooks_deliveriesretry.with_raw_response.create(
                delivery_id="",
                id="id",
            )


class TestAsyncAICreditsWebhooksDeliveriesretry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        ai_credits_webhooks_deliveriesretry = await async_client.projects.ai_credits_webhooks_deliveriesretry.create(
            delivery_id="deliveryId",
            id="id",
        )
        assert_matches_type(
            AICreditsWebhooksDeliveriesretryCreateResponse, ai_credits_webhooks_deliveriesretry, path=["response"]
        )

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.projects.ai_credits_webhooks_deliveriesretry.with_raw_response.create(
            delivery_id="deliveryId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_credits_webhooks_deliveriesretry = await response.parse()
        assert_matches_type(
            AICreditsWebhooksDeliveriesretryCreateResponse, ai_credits_webhooks_deliveriesretry, path=["response"]
        )

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.projects.ai_credits_webhooks_deliveriesretry.with_streaming_response.create(
            delivery_id="deliveryId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_credits_webhooks_deliveriesretry = await response.parse()
            assert_matches_type(
                AICreditsWebhooksDeliveriesretryCreateResponse, ai_credits_webhooks_deliveriesretry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.projects.ai_credits_webhooks_deliveriesretry.with_raw_response.create(
                delivery_id="deliveryId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.projects.ai_credits_webhooks_deliveriesretry.with_raw_response.create(
                delivery_id="",
                id="id",
            )
