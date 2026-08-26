# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.projects import (
    AICreditsSettingUpdateResponse,
    AICreditsSettingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAICreditsSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        ai_credits_setting = client.projects.ai_credits_settings.retrieve(
            "id",
        )
        assert_matches_type(AICreditsSettingRetrieveResponse, ai_credits_setting, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.projects.ai_credits_settings.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_credits_setting = response.parse()
        assert_matches_type(AICreditsSettingRetrieveResponse, ai_credits_setting, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.projects.ai_credits_settings.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_credits_setting = response.parse()
            assert_matches_type(AICreditsSettingRetrieveResponse, ai_credits_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.projects.ai_credits_settings.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unlayer) -> None:
        ai_credits_setting = client.projects.ai_credits_settings.update(
            id="id",
        )
        assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Unlayer) -> None:
        ai_credits_setting = client.projects.ai_credits_settings.update(
            id="id",
            exhaustion_behavior="disable",
            threshold_alerts=[1],
            webhook_url="https://example.com",
        )
        assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Unlayer) -> None:
        response = client.projects.ai_credits_settings.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_credits_setting = response.parse()
        assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Unlayer) -> None:
        with client.projects.ai_credits_settings.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_credits_setting = response.parse()
            assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.projects.ai_credits_settings.with_raw_response.update(
                id="",
            )


class TestAsyncAICreditsSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        ai_credits_setting = await async_client.projects.ai_credits_settings.retrieve(
            "id",
        )
        assert_matches_type(AICreditsSettingRetrieveResponse, ai_credits_setting, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.projects.ai_credits_settings.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_credits_setting = await response.parse()
        assert_matches_type(AICreditsSettingRetrieveResponse, ai_credits_setting, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.projects.ai_credits_settings.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_credits_setting = await response.parse()
            assert_matches_type(AICreditsSettingRetrieveResponse, ai_credits_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.projects.ai_credits_settings.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnlayer) -> None:
        ai_credits_setting = await async_client.projects.ai_credits_settings.update(
            id="id",
        )
        assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        ai_credits_setting = await async_client.projects.ai_credits_settings.update(
            id="id",
            exhaustion_behavior="disable",
            threshold_alerts=[1],
            webhook_url="https://example.com",
        )
        assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.projects.ai_credits_settings.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai_credits_setting = await response.parse()
        assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.projects.ai_credits_settings.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai_credits_setting = await response.parse()
            assert_matches_type(AICreditsSettingUpdateResponse, ai_credits_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.projects.ai_credits_settings.with_raw_response.update(
                id="",
            )
