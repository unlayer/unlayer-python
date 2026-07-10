# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.templates import ExportZipCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExportZip:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        export_zip = client.templates.export_zip.create(
            design={},
        )
        assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Unlayer) -> None:
        export_zip = client.templates.export_zip.create(
            design={},
            project_id="projectId",
            custom_js="string",
            design_tags={},
            design_tags_config={},
            display_mode="email",
            editor_version="editorVersion",
            language="language",
            languages=["string"],
            merge_tags={},
            merge_tags_schema={},
            safe_html=True,
        )
        assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.templates.export_zip.with_raw_response.create(
            design={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_zip = response.parse()
        assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.templates.export_zip.with_streaming_response.create(
            design={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_zip = response.parse()
            assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExportZip:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        export_zip = await async_client.templates.export_zip.create(
            design={},
        )
        assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        export_zip = await async_client.templates.export_zip.create(
            design={},
            project_id="projectId",
            custom_js="string",
            design_tags={},
            design_tags_config={},
            display_mode="email",
            editor_version="editorVersion",
            language="language",
            languages=["string"],
            merge_tags={},
            merge_tags_schema={},
            safe_html=True,
        )
        assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.templates.export_zip.with_raw_response.create(
            design={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_zip = await response.parse()
        assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.templates.export_zip.with_streaming_response.create(
            design={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_zip = await response.parse()
            assert_matches_type(ExportZipCreateResponse, export_zip, path=["response"])

        assert cast(Any, response.is_closed) is True
