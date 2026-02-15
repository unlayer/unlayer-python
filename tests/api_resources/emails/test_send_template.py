# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.emails import SendTemplateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSendTemplate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        send_template = client.emails.send_template.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
        )
        assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        send_template = client.emails.send_template.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
            merge_tags={"foo": "string"},
            subject="subject",
        )
        assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.emails.send_template.with_raw_response.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send_template = response.parse()
        assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.emails.send_template.with_streaming_response.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send_template = response.parse()
            assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSendTemplate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        send_template = await async_client.emails.send_template.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
        )
        assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        send_template = await async_client.emails.send_template.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
            merge_tags={"foo": "string"},
            subject="subject",
        )
        assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.send_template.with_raw_response.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send_template = await response.parse()
        assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.send_template.with_streaming_response.create(
            project_id="projectId",
            template_id="templateId",
            to="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send_template = await response.parse()
            assert_matches_type(SendTemplateCreateResponse, send_template, path=["response"])

        assert cast(Any, response.is_closed) is True
