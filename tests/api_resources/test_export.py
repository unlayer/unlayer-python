# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import (
    ExportPdfListResponse,
    ExportZipListResponse,
    ExportHTMLListResponse,
    ExportImageListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_html_list(self, client: Unlayer) -> None:
        export = client.export.html_list(
            project_id="projectId",
        )
        assert_matches_type(ExportHTMLListResponse, export, path=["response"])

    @parametrize
    def test_raw_response_html_list(self, client: Unlayer) -> None:
        response = client.export.with_raw_response.html_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportHTMLListResponse, export, path=["response"])

    @parametrize
    def test_streaming_response_html_list(self, client: Unlayer) -> None:
        with client.export.with_streaming_response.html_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportHTMLListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_image_list(self, client: Unlayer) -> None:
        export = client.export.image_list(
            project_id="projectId",
        )
        assert_matches_type(ExportImageListResponse, export, path=["response"])

    @parametrize
    def test_raw_response_image_list(self, client: Unlayer) -> None:
        response = client.export.with_raw_response.image_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportImageListResponse, export, path=["response"])

    @parametrize
    def test_streaming_response_image_list(self, client: Unlayer) -> None:
        with client.export.with_streaming_response.image_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportImageListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_pdf_list(self, client: Unlayer) -> None:
        export = client.export.pdf_list(
            project_id="projectId",
        )
        assert_matches_type(ExportPdfListResponse, export, path=["response"])

    @parametrize
    def test_raw_response_pdf_list(self, client: Unlayer) -> None:
        response = client.export.with_raw_response.pdf_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportPdfListResponse, export, path=["response"])

    @parametrize
    def test_streaming_response_pdf_list(self, client: Unlayer) -> None:
        with client.export.with_streaming_response.pdf_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportPdfListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_zip_list(self, client: Unlayer) -> None:
        export = client.export.zip_list(
            project_id="projectId",
        )
        assert_matches_type(ExportZipListResponse, export, path=["response"])

    @parametrize
    def test_raw_response_zip_list(self, client: Unlayer) -> None:
        response = client.export.with_raw_response.zip_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = response.parse()
        assert_matches_type(ExportZipListResponse, export, path=["response"])

    @parametrize
    def test_streaming_response_zip_list(self, client: Unlayer) -> None:
        with client.export.with_streaming_response.zip_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = response.parse()
            assert_matches_type(ExportZipListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_html_list(self, async_client: AsyncUnlayer) -> None:
        export = await async_client.export.html_list(
            project_id="projectId",
        )
        assert_matches_type(ExportHTMLListResponse, export, path=["response"])

    @parametrize
    async def test_raw_response_html_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.export.with_raw_response.html_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportHTMLListResponse, export, path=["response"])

    @parametrize
    async def test_streaming_response_html_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.export.with_streaming_response.html_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportHTMLListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_image_list(self, async_client: AsyncUnlayer) -> None:
        export = await async_client.export.image_list(
            project_id="projectId",
        )
        assert_matches_type(ExportImageListResponse, export, path=["response"])

    @parametrize
    async def test_raw_response_image_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.export.with_raw_response.image_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportImageListResponse, export, path=["response"])

    @parametrize
    async def test_streaming_response_image_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.export.with_streaming_response.image_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportImageListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_pdf_list(self, async_client: AsyncUnlayer) -> None:
        export = await async_client.export.pdf_list(
            project_id="projectId",
        )
        assert_matches_type(ExportPdfListResponse, export, path=["response"])

    @parametrize
    async def test_raw_response_pdf_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.export.with_raw_response.pdf_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportPdfListResponse, export, path=["response"])

    @parametrize
    async def test_streaming_response_pdf_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.export.with_streaming_response.pdf_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportPdfListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_zip_list(self, async_client: AsyncUnlayer) -> None:
        export = await async_client.export.zip_list(
            project_id="projectId",
        )
        assert_matches_type(ExportZipListResponse, export, path=["response"])

    @parametrize
    async def test_raw_response_zip_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.export.with_raw_response.zip_list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export = await response.parse()
        assert_matches_type(ExportZipListResponse, export, path=["response"])

    @parametrize
    async def test_streaming_response_zip_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.export.with_streaming_response.zip_list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export = await response.parse()
            assert_matches_type(ExportZipListResponse, export, path=["response"])

        assert cast(Any, response.is_closed) is True
