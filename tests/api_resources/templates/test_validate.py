# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.templates import ValidateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValidate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        validate = client.templates.validate.create(
            design={"foo": "bar"},
        )
        assert_matches_type(ValidateCreateResponse, validate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        validate = client.templates.validate.create(
            design={"foo": "bar"},
            custom_tools=[
                {
                    "options": {"foo": {"options": {}}},
                    "slug": "slug",
                    "label": "label",
                    "supported_display_modes": ["email"],
                    "type": "type",
                    "values": {"foo": "bar"},
                }
            ],
            display_mode="email",
            migrate=True,
            schema="full",
        )
        assert_matches_type(ValidateCreateResponse, validate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.templates.validate.with_raw_response.create(
            design={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = response.parse()
        assert_matches_type(ValidateCreateResponse, validate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.templates.validate.with_streaming_response.create(
            design={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = response.parse()
            assert_matches_type(ValidateCreateResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncValidate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        validate = await async_client.templates.validate.create(
            design={"foo": "bar"},
        )
        assert_matches_type(ValidateCreateResponse, validate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        validate = await async_client.templates.validate.create(
            design={"foo": "bar"},
            custom_tools=[
                {
                    "options": {"foo": {"options": {}}},
                    "slug": "slug",
                    "label": "label",
                    "supported_display_modes": ["email"],
                    "type": "type",
                    "values": {"foo": "bar"},
                }
            ],
            display_mode="email",
            migrate=True,
            schema="full",
        )
        assert_matches_type(ValidateCreateResponse, validate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.templates.validate.with_raw_response.create(
            design={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        validate = await response.parse()
        assert_matches_type(ValidateCreateResponse, validate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.templates.validate.with_streaming_response.create(
            design={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            validate = await response.parse()
            assert_matches_type(ValidateCreateResponse, validate, path=["response"])

        assert cast(Any, response.is_closed) is True
