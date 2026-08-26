# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import (
    WebhookListResponse,
    WebhookCreateResponse,
    WebhookDeleteResponse,
    WebhookUpdateResponse,
    WebhookRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        webhook = client.webhooks.create(
            url="https://example.com",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        webhook = client.webhooks.create(
            url="https://example.com",
            active=True,
            events=["email.sent"],
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.webhooks.with_raw_response.create(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.webhooks.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        webhook = client.webhooks.retrieve(
            "id",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unlayer) -> None:
        webhook = client.webhooks.update(
            id="id",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Unlayer) -> None:
        webhook = client.webhooks.update(
            id="id",
            active=True,
            events=["email.sent"],
            url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Unlayer) -> None:
        response = client.webhooks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Unlayer) -> None:
        with client.webhooks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unlayer) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unlayer) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unlayer) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unlayer) -> None:
        webhook = client.webhooks.delete(
            "id",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Unlayer) -> None:
        response = client.webhooks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Unlayer) -> None:
        with client.webhooks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.delete(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        webhook = await async_client.webhooks.create(
            url="https://example.com",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        webhook = await async_client.webhooks.create(
            url="https://example.com",
            active=True,
            events=["email.sent"],
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        webhook = await async_client.webhooks.retrieve(
            "id",
        )
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRetrieveResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnlayer) -> None:
        webhook = await async_client.webhooks.update(
            id="id",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        webhook = await async_client.webhooks.update(
            id="id",
            active=True,
            events=["email.sent"],
            url="https://example.com",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnlayer) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnlayer) -> None:
        webhook = await async_client.webhooks.delete(
            "id",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                "",
            )
