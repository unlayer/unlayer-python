# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import (
    DocumentGenerateCreateResponse,
    DocumentDocumentsRetrieveResponse,
    DocumentGenerateTemplateTemplateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_documents_retrieve(self, client: Unlayer) -> None:
        document = client.documents.documents_retrieve(
            id="id",
            project_id="projectId",
        )
        assert_matches_type(DocumentDocumentsRetrieveResponse, document, path=["response"])

    @parametrize
    def test_raw_response_documents_retrieve(self, client: Unlayer) -> None:
        response = client.documents.with_raw_response.documents_retrieve(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentDocumentsRetrieveResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_documents_retrieve(self, client: Unlayer) -> None:
        with client.documents.with_streaming_response.documents_retrieve(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentDocumentsRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_documents_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.documents.with_raw_response.documents_retrieve(
                id="",
                project_id="projectId",
            )

    @parametrize
    def test_method_generate_create(self, client: Unlayer) -> None:
        document = client.documents.generate_create(
            project_id="projectId",
        )
        assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

    @parametrize
    def test_method_generate_create_with_all_params(self, client: Unlayer) -> None:
        document = client.documents.generate_create(
            project_id="projectId",
            design={"foo": "bar"},
            filename="filename",
            html="html",
            merge_tags={"foo": "string"},
            url="https://example.com",
        )
        assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

    @parametrize
    def test_raw_response_generate_create(self, client: Unlayer) -> None:
        response = client.documents.with_raw_response.generate_create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_generate_create(self, client: Unlayer) -> None:
        with client.documents.with_streaming_response.generate_create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_generate_template_template(self, client: Unlayer) -> None:
        document = client.documents.generate_template_template(
            project_id="projectId",
            template_id="templateId",
        )
        assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

    @parametrize
    def test_method_generate_template_template_with_all_params(self, client: Unlayer) -> None:
        document = client.documents.generate_template_template(
            project_id="projectId",
            template_id="templateId",
            filename="filename",
            merge_tags={"foo": "string"},
        )
        assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

    @parametrize
    def test_raw_response_generate_template_template(self, client: Unlayer) -> None:
        response = client.documents.with_raw_response.generate_template_template(
            project_id="projectId",
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_generate_template_template(self, client: Unlayer) -> None:
        with client.documents.with_streaming_response.generate_template_template(
            project_id="projectId",
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        document = await async_client.documents.documents_retrieve(
            id="id",
            project_id="projectId",
        )
        assert_matches_type(DocumentDocumentsRetrieveResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents.with_raw_response.documents_retrieve(
            id="id",
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentDocumentsRetrieveResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents.with_streaming_response.documents_retrieve(
            id="id",
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentDocumentsRetrieveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_documents_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.documents.with_raw_response.documents_retrieve(
                id="",
                project_id="projectId",
            )

    @parametrize
    async def test_method_generate_create(self, async_client: AsyncUnlayer) -> None:
        document = await async_client.documents.generate_create(
            project_id="projectId",
        )
        assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

    @parametrize
    async def test_method_generate_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        document = await async_client.documents.generate_create(
            project_id="projectId",
            design={"foo": "bar"},
            filename="filename",
            html="html",
            merge_tags={"foo": "string"},
            url="https://example.com",
        )
        assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_generate_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents.with_raw_response.generate_create(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_generate_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents.with_streaming_response.generate_create(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGenerateCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_generate_template_template(self, async_client: AsyncUnlayer) -> None:
        document = await async_client.documents.generate_template_template(
            project_id="projectId",
            template_id="templateId",
        )
        assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

    @parametrize
    async def test_method_generate_template_template_with_all_params(self, async_client: AsyncUnlayer) -> None:
        document = await async_client.documents.generate_template_template(
            project_id="projectId",
            template_id="templateId",
            filename="filename",
            merge_tags={"foo": "string"},
        )
        assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_generate_template_template(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.documents.with_raw_response.generate_template_template(
            project_id="projectId",
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_generate_template_template(self, async_client: AsyncUnlayer) -> None:
        async with async_client.documents.with_streaming_response.generate_template_template(
            project_id="projectId",
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentGenerateTemplateTemplateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True
