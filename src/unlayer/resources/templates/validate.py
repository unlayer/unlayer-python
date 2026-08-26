# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.templates import validate_create_params
from ...types.templates.validate_create_response import ValidateCreateResponse

__all__ = ["ValidateResource", "AsyncValidateResource"]


class ValidateResource(SyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> ValidateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return ValidateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return ValidateResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        design: Dict[str, object],
        custom_tools: Iterable[validate_create_params.CustomTool] | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        migrate: bool | Omit = omit,
        schema: Literal["full", "simple"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateCreateResponse:
        """Validate a design JSON against the Unlayer design schema.

        Returns { success:
        true, data: { valid: true } } when the payload conforms; otherwise data is {
        valid: false, errors: [...] } with descriptive issues. Every checked design gets
        HTTP 200 — `data.valid` is the source of truth, not the status code. Only
        malformed requests (e.g. a missing design field or an unknown displayMode) fail
        request validation with 400 VALIDATION_ERROR.

        Args:
          design: The design JSON to validate.

          custom_tools: Custom tool declarations, in the same shape passed to unlayer.registerTool. When
              provided, blocks matching a declared tool have their values checked against the
              tool's declared options (wrong types are reported at their exact path). Blocks
              of undeclared tools keep envelope-only validation.

          display_mode: Display mode for the design (email, web, document, popup). Some validation rules
              differ per mode. Defaults to "email" — without a default, options from every
              mode would apply at once, the strictest possible check, and real editor-saved
              designs could be reported invalid.

          migrate: When true (default), a full-form design with an older schemaVersion is upgraded
              to the current schema before validating — matching how the editor and the
              convert endpoints treat stored designs. Designs without a schemaVersion predate
              versioning and are fully migrated the same way. Set to false to check strict
              conformance with the current schema version. Designs with a newer schemaVersion
              than this API knows are validated as-if-current.

          schema: Which form of the schema to validate against. Defaults to "full".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v3/templates/validate",
            body=maybe_transform(
                {
                    "design": design,
                    "custom_tools": custom_tools,
                    "display_mode": display_mode,
                    "migrate": migrate,
                    "schema": schema,
                },
                validate_create_params.ValidateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateCreateResponse,
        )


class AsyncValidateResource(AsyncAPIResource):
    """
    Template management — list, retrieve, generate, import, export, and convert designs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncValidateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/unlayer/unlayer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValidateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/unlayer/unlayer-python#with_streaming_response
        """
        return AsyncValidateResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        design: Dict[str, object],
        custom_tools: Iterable[validate_create_params.CustomTool] | Omit = omit,
        display_mode: Literal["email", "web", "popup", "document"] | Omit = omit,
        migrate: bool | Omit = omit,
        schema: Literal["full", "simple"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ValidateCreateResponse:
        """Validate a design JSON against the Unlayer design schema.

        Returns { success:
        true, data: { valid: true } } when the payload conforms; otherwise data is {
        valid: false, errors: [...] } with descriptive issues. Every checked design gets
        HTTP 200 — `data.valid` is the source of truth, not the status code. Only
        malformed requests (e.g. a missing design field or an unknown displayMode) fail
        request validation with 400 VALIDATION_ERROR.

        Args:
          design: The design JSON to validate.

          custom_tools: Custom tool declarations, in the same shape passed to unlayer.registerTool. When
              provided, blocks matching a declared tool have their values checked against the
              tool's declared options (wrong types are reported at their exact path). Blocks
              of undeclared tools keep envelope-only validation.

          display_mode: Display mode for the design (email, web, document, popup). Some validation rules
              differ per mode. Defaults to "email" — without a default, options from every
              mode would apply at once, the strictest possible check, and real editor-saved
              designs could be reported invalid.

          migrate: When true (default), a full-form design with an older schemaVersion is upgraded
              to the current schema before validating — matching how the editor and the
              convert endpoints treat stored designs. Designs without a schemaVersion predate
              versioning and are fully migrated the same way. Set to false to check strict
              conformance with the current schema version. Designs with a newer schemaVersion
              than this API knows are validated as-if-current.

          schema: Which form of the schema to validate against. Defaults to "full".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v3/templates/validate",
            body=await async_maybe_transform(
                {
                    "design": design,
                    "custom_tools": custom_tools,
                    "display_mode": display_mode,
                    "migrate": migrate,
                    "schema": schema,
                },
                validate_create_params.ValidateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ValidateCreateResponse,
        )


class ValidateResourceWithRawResponse:
    def __init__(self, validate: ValidateResource) -> None:
        self._validate = validate

        self.create = to_raw_response_wrapper(
            validate.create,
        )


class AsyncValidateResourceWithRawResponse:
    def __init__(self, validate: AsyncValidateResource) -> None:
        self._validate = validate

        self.create = async_to_raw_response_wrapper(
            validate.create,
        )


class ValidateResourceWithStreamingResponse:
    def __init__(self, validate: ValidateResource) -> None:
        self._validate = validate

        self.create = to_streamed_response_wrapper(
            validate.create,
        )


class AsyncValidateResourceWithStreamingResponse:
    def __init__(self, validate: AsyncValidateResource) -> None:
        self._validate = validate

        self.create = async_to_streamed_response_wrapper(
            validate.create,
        )
