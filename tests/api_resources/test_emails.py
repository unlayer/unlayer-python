# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from unlayer import Unlayer, AsyncUnlayer
from tests.utils import assert_matches_type
from unlayer.types import (
    EmailSendCreateResponse,
    EmailRenderCreateResponse,
    EmailEmailsRetrieveResponse,
    EmailSendTemplateTemplateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_emails_retrieve(self, client: Unlayer) -> None:
        email = client.emails.emails_retrieve(
            "id",
        )
        assert_matches_type(EmailEmailsRetrieveResponse, email, path=["response"])

    @parametrize
    def test_raw_response_emails_retrieve(self, client: Unlayer) -> None:
        response = client.emails.with_raw_response.emails_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailEmailsRetrieveResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_emails_retrieve(self, client: Unlayer) -> None:
        with client.emails.with_streaming_response.emails_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailEmailsRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_emails_retrieve(self, client: Unlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emails.with_raw_response.emails_retrieve(
                "",
            )

    @parametrize
    def test_method_render_create(self, client: Unlayer) -> None:
        email = client.emails.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

    @parametrize
    def test_method_render_create_with_all_params(self, client: Unlayer) -> None:
        email = client.emails.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            merge_tags={"foo": "string"},
        )
        assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

    @parametrize
    def test_raw_response_render_create(self, client: Unlayer) -> None:
        response = client.emails.with_raw_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_render_create(self, client: Unlayer) -> None:
        with client.emails.with_streaming_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_create(self, client: Unlayer) -> None:
        email = client.emails.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
        )
        assert_matches_type(EmailSendCreateResponse, email, path=["response"])

    @parametrize
    def test_method_send_create_with_all_params(self, client: Unlayer) -> None:
        email = client.emails.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
            html="html",
            merge_tags={"foo": "string"},
            subject="Test",
        )
        assert_matches_type(EmailSendCreateResponse, email, path=["response"])

    @parametrize
    def test_raw_response_send_create(self, client: Unlayer) -> None:
        response = client.emails.with_raw_response.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailSendCreateResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_send_create(self, client: Unlayer) -> None:
        with client.emails.with_streaming_response.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailSendCreateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_template_template(self, client: Unlayer) -> None:
        email = client.emails.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
        )
        assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

    @parametrize
    def test_method_send_template_template_with_all_params(self, client: Unlayer) -> None:
        email = client.emails.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
            merge_tags={"foo": "string"},
            subject="subject",
        )
        assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

    @parametrize
    def test_raw_response_send_template_template(self, client: Unlayer) -> None:
        response = client.emails.with_raw_response.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

    @parametrize
    def test_streaming_response_send_template_template(self, client: Unlayer) -> None:
        with client.emails.with_streaming_response.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_emails_retrieve(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.emails_retrieve(
            "id",
        )
        assert_matches_type(EmailEmailsRetrieveResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_emails_retrieve(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.with_raw_response.emails_retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailEmailsRetrieveResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_emails_retrieve(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.with_streaming_response.emails_retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailEmailsRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_emails_retrieve(self, async_client: AsyncUnlayer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emails.with_raw_response.emails_retrieve(
                "",
            )

    @parametrize
    async def test_method_render_create(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )
        assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

    @parametrize
    async def test_method_render_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            merge_tags={"foo": "string"},
        )
        assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_render_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.with_raw_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_render_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.with_streaming_response.render_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailRenderCreateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_create(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
        )
        assert_matches_type(EmailSendCreateResponse, email, path=["response"])

    @parametrize
    async def test_method_send_create_with_all_params(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
            html="html",
            merge_tags={"foo": "string"},
            subject="Test",
        )
        assert_matches_type(EmailSendCreateResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_send_create(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.with_raw_response.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailSendCreateResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_send_create(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.with_streaming_response.send_create(
            design={
                "counters": "bar",
                "body": "bar",
            },
            to="test@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailSendCreateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_template_template(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
        )
        assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

    @parametrize
    async def test_method_send_template_template_with_all_params(self, async_client: AsyncUnlayer) -> None:
        email = await async_client.emails.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
            merge_tags={"foo": "string"},
            subject="subject",
        )
        assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

    @parametrize
    async def test_raw_response_send_template_template(self, async_client: AsyncUnlayer) -> None:
        response = await async_client.emails.with_raw_response.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

    @parametrize
    async def test_streaming_response_send_template_template(self, async_client: AsyncUnlayer) -> None:
        async with async_client.emails.with_streaming_response.send_template_template(
            template_id="templateId",
            to="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailSendTemplateTemplateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True
