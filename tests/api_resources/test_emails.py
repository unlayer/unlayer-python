# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import EmailRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        email = client.emails.retrieve(
            id="id",
            project_id="projectId",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.emails.with_raw_response.retrieve(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.emails.with_streaming_response.retrieve(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emails.with_raw_response.retrieve(
                id="",
                project_id="projectId",
            )


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.retrieve(
            id="id",
            project_id="projectId",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.with_raw_response.retrieve(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.with_streaming_response.retrieve(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emails.with_raw_response.retrieve(
                id="",
                project_id="projectId",
            )
