# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.templates import GenerateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        generate = client.templates.generate.create(
            messages=[
                {
                    "content": [{"type": "text"}],
                    "role": "user",
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
            },
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        generate = client.templates.generate.create(
            messages=[
                {
                    "content": [
                        {
                            "type": "text",
                            "file": {
                                "url": "url",
                                "media_type": "mediaType",
                            },
                            "image": "image",
                            "text": "text",
                        }
                    ],
                    "role": "user",
                    "metadata": {"action": {"id": "id"}},
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
                "schema_version": 0,
            },
            project_id="projectId",
            context={
                "available_fonts": [
                    {
                        "label": "x",
                        "value": "x",
                    }
                ],
                "available_tools": ["string"],
                "brand": {
                    "colors": {
                        "accent": "accent",
                        "primary": "primary",
                        "secondary": "secondary",
                    },
                    "company_name": "companyName",
                    "fonts": {
                        "body": "body",
                        "heading": "heading",
                    },
                    "guidelines": "guidelines",
                    "logos": {
                        "primary": "https://example.com",
                        "secondary": "https://example.com",
                    },
                    "product_description": "productDescription",
                    "target_audience": "targetAudience",
                    "voice": "voice",
                },
                "custom_tools": [
                    {
                        "options": {"foo": "bar"},
                        "slug": "slug",
                    }
                ],
                "full_design": {"foo": "bar"},
                "selection": {
                    "id": "string",
                    "collection": "pages",
                    "value": "value",
                },
            },
            conversation_id="conversationId",
            fallback_models=True,
            locale="locale",
            model="model",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.templates.generate.with_raw_response.create(
            messages=[
                {
                    "content": [{"type": "text"}],
                    "role": "user",
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.templates.generate.with_streaming_response.create(
            messages=[
                {
                    "content": [{"type": "text"}],
                    "role": "user",
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateCreateResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        generate = client.templates.generate.retrieve()
        assert generate is None

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.templates.generate.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert generate is None

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.templates.generate.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert generate is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        generate = await async_client.templates.generate.create(
            messages=[
                {
                    "content": [{"type": "text"}],
                    "role": "user",
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
            },
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        generate = await async_client.templates.generate.create(
            messages=[
                {
                    "content": [
                        {
                            "type": "text",
                            "file": {
                                "url": "url",
                                "media_type": "mediaType",
                            },
                            "image": "image",
                            "text": "text",
                        }
                    ],
                    "role": "user",
                    "metadata": {"action": {"id": "id"}},
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
                "schema_version": 0,
            },
            project_id="projectId",
            context={
                "available_fonts": [
                    {
                        "label": "x",
                        "value": "x",
                    }
                ],
                "available_tools": ["string"],
                "brand": {
                    "colors": {
                        "accent": "accent",
                        "primary": "primary",
                        "secondary": "secondary",
                    },
                    "company_name": "companyName",
                    "fonts": {
                        "body": "body",
                        "heading": "heading",
                    },
                    "guidelines": "guidelines",
                    "logos": {
                        "primary": "https://example.com",
                        "secondary": "https://example.com",
                    },
                    "product_description": "productDescription",
                    "target_audience": "targetAudience",
                    "voice": "voice",
                },
                "custom_tools": [
                    {
                        "options": {"foo": "bar"},
                        "slug": "slug",
                    }
                ],
                "full_design": {"foo": "bar"},
                "selection": {
                    "id": "string",
                    "collection": "pages",
                    "value": "value",
                },
            },
            conversation_id="conversationId",
            fallback_models=True,
            locale="locale",
            model="model",
        )
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.templates.generate.with_raw_response.create(
            messages=[
                {
                    "content": [{"type": "text"}],
                    "role": "user",
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateCreateResponse, generate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.templates.generate.with_streaming_response.create(
            messages=[
                {
                    "content": [{"type": "text"}],
                    "role": "user",
                }
            ],
            output={
                "display_mode": "email",
                "kind": "template",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateCreateResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        generate = await async_client.templates.generate.retrieve()
        assert generate is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.templates.generate.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert generate is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.templates.generate.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert generate is None

        assert cast(Any, response.is_closed) is True
