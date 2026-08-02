# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.emails import (
    SuppressionCreateResponse,
    SuppressionDeleteResponse,
    SuppressionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuppressions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        suppression = client.emails.suppressions.create(
            email="dev@stainless.com",
        )
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.emails.suppressions.with_raw_response.create(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.emails.suppressions.with_streaming_response.create(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        suppression = client.emails.suppressions.retrieve()
        assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unlayer) -> None:
        suppression = client.emails.suppressions.retrieve(
            cursor="cursor",
            limit=1,
            project_id="projectId",
        )
        assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.emails.suppressions.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.emails.suppressions.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unlayer) -> None:
        suppression = client.emails.suppressions.delete(
            email="email",
        )
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Unlayer) -> None:
        suppression = client.emails.suppressions.delete(
            email="email",
            project_id="projectId",
        )
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Unlayer) -> None:
        response = client.emails.suppressions.with_raw_response.delete(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = response.parse()
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Unlayer) -> None:
        with client.emails.suppressions.with_streaming_response.delete(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = response.parse()
            assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSuppressions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        suppression = await async_client.emails.suppressions.create(
            email="dev@stainless.com",
        )
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.suppressions.with_raw_response.create(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.suppressions.with_streaming_response.create(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionCreateResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        suppression = await async_client.emails.suppressions.retrieve()
        assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnlayer) -> None:
        suppression = await async_client.emails.suppressions.retrieve(
            cursor="cursor",
            limit=1,
            project_id="projectId",
        )
        assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.suppressions.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.suppressions.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionRetrieveResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnlayer) -> None:
        suppression = await async_client.emails.suppressions.delete(
            email="email",
        )
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncUnlayer) -> None:
        suppression = await async_client.emails.suppressions.delete(
            email="email",
            project_id="projectId",
        )
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.suppressions.with_raw_response.delete(
            email="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        suppression = await response.parse()
        assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.suppressions.with_streaming_response.delete(
            email="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            suppression = await response.parse()
            assert_matches_type(SuppressionDeleteResponse, suppression, path=["response"])

        assert cast(Any, response.is_closed) is True
