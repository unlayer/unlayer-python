# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.templates import ImportCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestImport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        import_ = client.templates.import_.create(
            display_mode="email",
            input=[{"type": "html"}],
        )
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        import_ = client.templates.import_.create(
            display_mode="email",
            input=[
                {
                    "type": "html",
                    "data": "data",
                    "html": "html",
                    "text": "text",
                    "url": "url",
                }
            ],
            project_id="projectId",
            fallback_models=True,
            model="model",
        )
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.templates.import_.with_raw_response.create(
            display_mode="email",
            input=[{"type": "html"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = response.parse()
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.templates.import_.with_streaming_response.create(
            display_mode="email",
            input=[{"type": "html"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = response.parse()
            assert_matches_type(ImportCreateResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncImport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        import_ = await async_client.templates.import_.create(
            display_mode="email",
            input=[{"type": "html"}],
        )
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        import_ = await async_client.templates.import_.create(
            display_mode="email",
            input=[
                {
                    "type": "html",
                    "data": "data",
                    "html": "html",
                    "text": "text",
                    "url": "url",
                }
            ],
            project_id="projectId",
            fallback_models=True,
            model="model",
        )
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.templates.import_.with_raw_response.create(
            display_mode="email",
            input=[{"type": "html"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        import_ = await response.parse()
        assert_matches_type(ImportCreateResponse, import_, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.templates.import_.with_streaming_response.create(
            display_mode="email",
            input=[{"type": "html"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            import_ = await response.parse()
            assert_matches_type(ImportCreateResponse, import_, path=["response"])

        assert cast(Any, response.is_closed) is True
