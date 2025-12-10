# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import (
    DocumentsV1GenerateCreateResponse,
    DocumentsV1DocumentsRetrieveResponse,
    DocumentsV1GenerateTemplateTemplateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocumentsV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_documents_retrieve(self, client: Unlayer) -> None:
        documents_v1 = client.documents_v1.documents_retrieve(
            "id",
        )
        assert_matches_type(DocumentsV1DocumentsRetrieveResponse, documents_v1, path=["response"])

    @parametrize
    def test_raw_response_documents_retrieve(self, client: Unlayer) -> None:
        response = client.documents_v1.with_raw_response.documents_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        documents_v1 = response.parse()
        assert_matches_type(DocumentsV1DocumentsRetrieveResponse, documents_v1, path=["response"])

    @parametrize
    def test_streaming_response_documents_retrieve(self, client: Unlayer) -> None:
        with client.documents_v1.with_streaming_response.documents_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            documents_v1 = response.parse()
            assert_matches_type(DocumentsV1DocumentsRetrieveResponse, documents_v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_documents_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents_v1.with_raw_response.documents_retrieve(
                "",
            )

    @parametrize
    def test_method_generate_create(self, client: Unlayer) -> None:
        documents_v1 = client.documents_v1.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

    @parametrize
    def test_method_generate_create_with_all_params(self, client: Unlayer) -> None:
        documents_v1 = client.documents_v1.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            filename="filename",
            html="html",
            merge_tags={"foo": "string"},
            url="https://example.com",
        )
        assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

    @parametrize
    def test_raw_response_generate_create(self, client: Unlayer) -> None:
        response = client.documents_v1.with_raw_response.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        documents_v1 = response.parse()
        assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

    @parametrize
    def test_streaming_response_generate_create(self, client: Unlayer) -> None:
        with client.documents_v1.with_streaming_response.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            documents_v1 = response.parse()
            assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate_template_template(self, client: Unlayer) -> None:
        documents_v1 = client.documents_v1.generate_template_template(
            template_id="templateId",
        )
        assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

    @parametrize
    def test_method_generate_template_template_with_all_params(self, client: Unlayer) -> None:
        documents_v1 = client.documents_v1.generate_template_template(
            template_id="templateId",
            filename="filename",
            merge_tags={"foo": "string"},
        )
        assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

    @parametrize
    def test_raw_response_generate_template_template(self, client: Unlayer) -> None:
        response = client.documents_v1.with_raw_response.generate_template_template(
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        documents_v1 = response.parse()
        assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

    @parametrize
    def test_streaming_response_generate_template_template(self, client: Unlayer) -> None:
        with client.documents_v1.with_streaming_response.generate_template_template(
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            documents_v1 = response.parse()
            assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocumentsV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        documents_v1 = await async_client.documents_v1.documents_retrieve(
            "id",
        )
        assert_matches_type(DocumentsV1DocumentsRetrieveResponse, documents_v1, path=["response"])

    @parametrize
    async def test_raw_response_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents_v1.with_raw_response.documents_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        documents_v1 = await response.parse()
        assert_matches_type(DocumentsV1DocumentsRetrieveResponse, documents_v1, path=["response"])

    @parametrize
    async def test_streaming_response_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents_v1.with_streaming_response.documents_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            documents_v1 = await response.parse()
            assert_matches_type(DocumentsV1DocumentsRetrieveResponse, documents_v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents_v1.with_raw_response.documents_retrieve(
                "",
            )

    @parametrize
    async def test_method_generate_create(self, async_client: AsyncUnlayer) -> None:
        documents_v1 = await async_client.documents_v1.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

    @parametrize
    async def test_method_generate_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        documents_v1 = await async_client.documents_v1.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            filename="filename",
            html="html",
            merge_tags={"foo": "string"},
            url="https://example.com",
        )
        assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

    @parametrize
    async def test_raw_response_generate_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents_v1.with_raw_response.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        documents_v1 = await response.parse()
        assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

    @parametrize
    async def test_streaming_response_generate_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents_v1.with_streaming_response.generate_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            documents_v1 = await response.parse()
            assert_matches_type(DocumentsV1GenerateCreateResponse, documents_v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate_template_template(self, async_client: AsyncUnlayer) -> None:
        documents_v1 = await async_client.documents_v1.generate_template_template(
            template_id="templateId",
        )
        assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

    @parametrize
    async def test_method_generate_template_template_with_all_params(self, async_client: AsyncUnlayer) -> None:
        documents_v1 = await async_client.documents_v1.generate_template_template(
            template_id="templateId",
            filename="filename",
            merge_tags={"foo": "string"},
        )
        assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

    @parametrize
    async def test_raw_response_generate_template_template(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents_v1.with_raw_response.generate_template_template(
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        documents_v1 = await response.parse()
        assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

    @parametrize
    async def test_streaming_response_generate_template_template(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents_v1.with_streaming_response.generate_template_template(
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            documents_v1 = await response.parse()
            assert_matches_type(DocumentsV1GenerateTemplateTemplateResponse, documents_v1, path=["response"])

        assert cast(Any, response.is_closed) is True
