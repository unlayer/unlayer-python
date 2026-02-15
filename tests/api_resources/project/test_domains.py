# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.project import (
    DomainListResponse,
    DomainCreateResponse,
    DomainUpdateResponse,
    DomainRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Unlayer) -> None:
        domain = client.project.domains.create(
            project_id="projectId",
            domain="domain",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Unlayer) -> None:
        response = client.project.domains.with_raw_response.create(
            project_id="projectId",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Unlayer) -> None:
        with client.project.domains.with_streaming_response.create(
            project_id="projectId",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Unlayer) -> None:
        domain = client.project.domains.retrieve(
            "id",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unlayer) -> None:
        response = client.project.domains.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unlayer) -> None:
        with client.project.domains.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.domains.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Unlayer) -> None:
        domain = client.project.domains.update(
            id="id",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Unlayer) -> None:
        domain = client.project.domains.update(
            id="id",
            domain="domain",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Unlayer) -> None:
        response = client.project.domains.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Unlayer) -> None:
        with client.project.domains.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainUpdateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.domains.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Unlayer) -> None:
        domain = client.project.domains.list(
            project_id="projectId",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unlayer) -> None:
        response = client.project.domains.with_raw_response.list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unlayer) -> None:
        with client.project.domains.with_streaming_response.list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Unlayer) -> None:
        domain = client.project.domains.delete(
            "id",
        )
        assert domain is None

    @parametrize
    def test_raw_response_delete(self, client: Unlayer) -> None:
        response = client.project.domains.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert domain is None

    @parametrize
    def test_streaming_response_delete(self, client: Unlayer) -> None:
        with client.project.domains.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.domains.with_raw_response.delete(
                "",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncUnlayer) -> None:
        domain = await async_client.project.domains.create(
            project_id="projectId",
            domain="domain",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.domains.with_raw_response.create(
            project_id="projectId",
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.domains.with_streaming_response.create(
            project_id="projectId",
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnlayer) -> None:
        domain = await async_client.project.domains.retrieve(
            "id",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.domains.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.domains.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.domains.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncUnlayer) -> None:
        domain = await async_client.project.domains.update(
            id="id",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        domain = await async_client.project.domains.update(
            id="id",
            domain="domain",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.domains.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.domains.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainUpdateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.domains.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncUnlayer) -> None:
        domain = await async_client.project.domains.list(
            project_id="projectId",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.domains.with_raw_response.list(
            project_id="projectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.domains.with_streaming_response.list(
            project_id="projectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncUnlayer) -> None:
        domain = await async_client.project.domains.delete(
            "id",
        )
        assert domain is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.domains.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert domain is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.domains.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.domains.with_raw_response.delete(
                "",
            )
