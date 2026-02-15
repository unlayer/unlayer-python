# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.documents import GenerateTemplateCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerateTemplate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        generate_template = client.documents.generate_template.create(
            project_id="projectId",
            template_id="templateId",
        )
        assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        generate_template = client.documents.generate_template.create(
            project_id="projectId",
            template_id="templateId",
            filename="filename",
            merge_tags={"foo": "string"},
        )
        assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.documents.generate_template.with_raw_response.create(
            project_id="projectId",
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_template = response.parse()
        assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.documents.generate_template.with_streaming_response.create(
            project_id="projectId",
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_template = response.parse()
            assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerateTemplate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        generate_template = await async_client.documents.generate_template.create(
            project_id="projectId",
            template_id="templateId",
        )
        assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        generate_template = await async_client.documents.generate_template.create(
            project_id="projectId",
            template_id="templateId",
            filename="filename",
            merge_tags={"foo": "string"},
        )
        assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents.generate_template.with_raw_response.create(
            project_id="projectId",
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate_template = await response.parse()
        assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents.generate_template.with_streaming_response.create(
            project_id="projectId",
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate_template = await response.parse()
            assert_matches_type(GenerateTemplateCreateResponse, generate_template, path=["response"])

        assert cast(Any, response.is_closed) is True
