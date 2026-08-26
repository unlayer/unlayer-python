# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.emails import TemplateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        template = client.emails.template.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        template = client.emails.template.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
            attachments=[
                {
                    "content": "content",
                    "content_type": "application/pdf",
                    "filename": "filename",
                }
            ],
            bcc=[],
            cc=[],
            headers={"foo": "J!Q0Ok0bzJb7"},
            reply_to="dev@stainless.com",
            subject="subject",
            tags={"foo": "_1"},
            text="text",
            variables={"foo": "string"},
            idempotency_key="idempotency-key",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.emails.template.with_raw_response.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.emails.template.with_streaming_response.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTemplate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        template = await async_client.emails.template.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        template = await async_client.emails.template.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
            attachments=[
                {
                    "content": "content",
                    "content_type": "application/pdf",
                    "filename": "filename",
                }
            ],
            bcc=[],
            cc=[],
            headers={"foo": "J!Q0Ok0bzJb7"},
            reply_to="dev@stainless.com",
            subject="subject",
            tags={"foo": "_1"},
            text="text",
            variables={"foo": "string"},
            idempotency_key="idempotency-key",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.template.with_raw_response.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.template.with_streaming_response.create(
            from_="from",
            template_id="496",
            to=["dev@stainless.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True
