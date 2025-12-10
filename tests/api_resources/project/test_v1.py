# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types.project import (
    V1APIKeysListResponse,
    V1CurrentListResponse,
    V1DomainsListResponse,
    V1APIKeysCreateResponse,
    V1APIKeysUpdateResponse,
    V1DomainsCreateResponse,
    V1DomainsUpdateResponse,
    V1TemplatesListResponse,
    V1APIKeysRetrieveResponse,
    V1DomainsRetrieveResponse,
    V1TemplatesCreateResponse,
    V1TemplatesUpdateResponse,
    V1TemplatesRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_api_keys_create(self, client: Unlayer) -> None:
        v1 = client.project.v1.api_keys_create(
            name="name",
        )
        assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

    @parametrize
    def test_method_api_keys_create_with_all_params(self, client: Unlayer) -> None:
        v1 = client.project.v1.api_keys_create(
            name="name",
            domains=["string"],
        )
        assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_api_keys_create(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.api_keys_create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_api_keys_create(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.api_keys_create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_api_keys_delete(self, client: Unlayer) -> None:
        v1 = client.project.v1.api_keys_delete(
            "id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_api_keys_delete(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.api_keys_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_api_keys_delete(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.api_keys_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_api_keys_delete(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.api_keys_delete(
                "",
            )

    @parametrize
    def test_method_api_keys_list(self, client: Unlayer) -> None:
        v1 = client.project.v1.api_keys_list()
        assert_matches_type(V1APIKeysListResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_api_keys_list(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.api_keys_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1APIKeysListResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_api_keys_list(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.api_keys_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1APIKeysListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_api_keys_retrieve(self, client: Unlayer) -> None:
        v1 = client.project.v1.api_keys_retrieve(
            "id",
        )
        assert_matches_type(V1APIKeysRetrieveResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_api_keys_retrieve(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.api_keys_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1APIKeysRetrieveResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_api_keys_retrieve(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.api_keys_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1APIKeysRetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_api_keys_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.api_keys_retrieve(
                "",
            )

    @parametrize
    def test_method_api_keys_update(self, client: Unlayer) -> None:
        v1 = client.project.v1.api_keys_update(
            id="id",
        )
        assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

    @parametrize
    def test_method_api_keys_update_with_all_params(self, client: Unlayer) -> None:
        v1 = client.project.v1.api_keys_update(
            id="id",
            active=True,
            domains=["string"],
            name="name",
        )
        assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_api_keys_update(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.api_keys_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_api_keys_update(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.api_keys_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_api_keys_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.api_keys_update(
                id="",
            )

    @parametrize
    def test_method_current_list(self, client: Unlayer) -> None:
        v1 = client.project.v1.current_list()
        assert_matches_type(V1CurrentListResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_current_list(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.current_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1CurrentListResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_current_list(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.current_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1CurrentListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_domains_create(self, client: Unlayer) -> None:
        v1 = client.project.v1.domains_create(
            domain="domain",
        )
        assert_matches_type(V1DomainsCreateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_domains_create(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.domains_create(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DomainsCreateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_domains_create(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.domains_create(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DomainsCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_domains_delete(self, client: Unlayer) -> None:
        v1 = client.project.v1.domains_delete(
            "id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_domains_delete(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.domains_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_domains_delete(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.domains_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_domains_delete(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.domains_delete(
                "",
            )

    @parametrize
    def test_method_domains_list(self, client: Unlayer) -> None:
        v1 = client.project.v1.domains_list()
        assert_matches_type(V1DomainsListResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_domains_list(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.domains_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DomainsListResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_domains_list(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.domains_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DomainsListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_domains_retrieve(self, client: Unlayer) -> None:
        v1 = client.project.v1.domains_retrieve(
            "id",
        )
        assert_matches_type(V1DomainsRetrieveResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_domains_retrieve(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.domains_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DomainsRetrieveResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_domains_retrieve(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.domains_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DomainsRetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_domains_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.domains_retrieve(
                "",
            )

    @parametrize
    def test_method_domains_update(self, client: Unlayer) -> None:
        v1 = client.project.v1.domains_update(
            id="id",
        )
        assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

    @parametrize
    def test_method_domains_update_with_all_params(self, client: Unlayer) -> None:
        v1 = client.project.v1.domains_update(
            id="id",
            domain="domain",
        )
        assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_domains_update(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.domains_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_domains_update(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.domains_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_domains_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.domains_update(
                id="",
            )

    @parametrize
    def test_method_templates_create(self, client: Unlayer) -> None:
        v1 = client.project.v1.templates_create(
            name="name",
        )
        assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

    @parametrize
    def test_method_templates_create_with_all_params(self, client: Unlayer) -> None:
        v1 = client.project.v1.templates_create(
            name="name",
            body="body",
            subject="subject",
        )
        assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_templates_create(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.templates_create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_templates_create(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.templates_create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_templates_delete(self, client: Unlayer) -> None:
        v1 = client.project.v1.templates_delete(
            "id",
        )
        assert v1 is None

    @parametrize
    def test_raw_response_templates_delete(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.templates_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert v1 is None

    @parametrize
    def test_streaming_response_templates_delete(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.templates_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_templates_delete(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.templates_delete(
                "",
            )

    @parametrize
    def test_method_templates_list(self, client: Unlayer) -> None:
        v1 = client.project.v1.templates_list()
        assert_matches_type(V1TemplatesListResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_templates_list(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.templates_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1TemplatesListResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_templates_list(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.templates_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1TemplatesListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_templates_retrieve(self, client: Unlayer) -> None:
        v1 = client.project.v1.templates_retrieve(
            "id",
        )
        assert_matches_type(V1TemplatesRetrieveResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_templates_retrieve(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.templates_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1TemplatesRetrieveResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_templates_retrieve(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.templates_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1TemplatesRetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_templates_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.templates_retrieve(
                "",
            )

    @parametrize
    def test_method_templates_update(self, client: Unlayer) -> None:
        v1 = client.project.v1.templates_update(
            id="id",
        )
        assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

    @parametrize
    def test_method_templates_update_with_all_params(self, client: Unlayer) -> None:
        v1 = client.project.v1.templates_update(
            id="id",
            body="body",
            name="name",
            subject="subject",
        )
        assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_templates_update(self, client: Unlayer) -> None:
        response = client.project.v1.with_raw_response.templates_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_templates_update(self, client: Unlayer) -> None:
        with client.project.v1.with_streaming_response.templates_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_templates_update(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.project.v1.with_raw_response.templates_update(
                id="",
            )


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_api_keys_create(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.api_keys_create(
            name="name",
        )
        assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

    @parametrize
    async def test_method_api_keys_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.api_keys_create(
            name="name",
            domains=["string"],
        )
        assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_api_keys_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.api_keys_create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_api_keys_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.api_keys_create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1APIKeysCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_api_keys_delete(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.api_keys_delete(
            "id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_api_keys_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.api_keys_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_api_keys_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.api_keys_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_api_keys_delete(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.api_keys_delete(
                "",
            )

    @parametrize
    async def test_method_api_keys_list(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.api_keys_list()
        assert_matches_type(V1APIKeysListResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_api_keys_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.api_keys_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1APIKeysListResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_api_keys_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.api_keys_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1APIKeysListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_api_keys_retrieve(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.api_keys_retrieve(
            "id",
        )
        assert_matches_type(V1APIKeysRetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_api_keys_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.api_keys_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1APIKeysRetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_api_keys_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.api_keys_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1APIKeysRetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_api_keys_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.api_keys_retrieve(
                "",
            )

    @parametrize
    async def test_method_api_keys_update(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.api_keys_update(
            id="id",
        )
        assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_method_api_keys_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.api_keys_update(
            id="id",
            active=True,
            domains=["string"],
            name="name",
        )
        assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_api_keys_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.api_keys_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_api_keys_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.api_keys_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1APIKeysUpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_api_keys_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.api_keys_update(
                id="",
            )

    @parametrize
    async def test_method_current_list(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.current_list()
        assert_matches_type(V1CurrentListResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_current_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.current_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1CurrentListResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_current_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.current_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1CurrentListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_domains_create(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.domains_create(
            domain="domain",
        )
        assert_matches_type(V1DomainsCreateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_domains_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.domains_create(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DomainsCreateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_domains_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.domains_create(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DomainsCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_domains_delete(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.domains_delete(
            "id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_domains_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.domains_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_domains_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.domains_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_domains_delete(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.domains_delete(
                "",
            )

    @parametrize
    async def test_method_domains_list(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.domains_list()
        assert_matches_type(V1DomainsListResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_domains_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.domains_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DomainsListResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_domains_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.domains_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DomainsListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.domains_retrieve(
            "id",
        )
        assert_matches_type(V1DomainsRetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.domains_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DomainsRetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.domains_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DomainsRetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_domains_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.domains_retrieve(
                "",
            )

    @parametrize
    async def test_method_domains_update(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.domains_update(
            id="id",
        )
        assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_method_domains_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.domains_update(
            id="id",
            domain="domain",
        )
        assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_domains_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.domains_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_domains_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.domains_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1DomainsUpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_domains_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.domains_update(
                id="",
            )

    @parametrize
    async def test_method_templates_create(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.templates_create(
            name="name",
        )
        assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

    @parametrize
    async def test_method_templates_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.templates_create(
            name="name",
            body="body",
            subject="subject",
        )
        assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_templates_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.templates_create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_templates_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.templates_create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1TemplatesCreateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_templates_delete(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.templates_delete(
            "id",
        )
        assert v1 is None

    @parametrize
    async def test_raw_response_templates_delete(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.templates_delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert v1 is None

    @parametrize
    async def test_streaming_response_templates_delete(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.templates_delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert v1 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_templates_delete(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.templates_delete(
                "",
            )

    @parametrize
    async def test_method_templates_list(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.templates_list()
        assert_matches_type(V1TemplatesListResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_templates_list(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.templates_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1TemplatesListResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_templates_list(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.templates_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1TemplatesListResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.templates_retrieve(
            "id",
        )
        assert_matches_type(V1TemplatesRetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.templates_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1TemplatesRetrieveResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.templates_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1TemplatesRetrieveResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_templates_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.templates_retrieve(
                "",
            )

    @parametrize
    async def test_method_templates_update(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.templates_update(
            id="id",
        )
        assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_method_templates_update_with_all_params(self, async_client: AsyncUnlayer) -> None:
        v1 = await async_client.project.v1.templates_update(
            id="id",
            body="body",
            name="name",
            subject="subject",
        )
        assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_templates_update(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.project.v1.with_raw_response.templates_update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_templates_update(self, async_client: AsyncUnlayer) -> None:
        async with async_client.project.v1.with_streaming_response.templates_update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1TemplatesUpdateResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_templates_update(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.project.v1.with_raw_response.templates_update(
                id="",
            )
