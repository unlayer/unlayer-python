# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GenerateCreateResponse", "Model", "Output", "Usage"]


class Model(BaseModel):
    """
    The provider + model that actually produced the output (may differ from the requested model after failover).
    """

    id: Optional[str] = None
    """Resolved model id, e.g. "claude-opus-5"."""

    provider: Optional[str] = None
    """e.g. "anthropic", "openai"."""


class Output(BaseModel):
    """The generated output for the requested block."""

    data: Optional[Dict[str, object]] = None
    """
    The generated design JSON, scoped to the requested kind (the full design for
    template/page/body; the row/column/content/element for narrower kinds).
    """

    kind: Optional[str] = None
    """Echoes the requested `output.kind`."""


class Usage(BaseModel):
    """Aggregate token usage and billed AI credits for the turn.

    Estimated provider cost is included only by builder copilot endpoints in local/dev/QA.
    """

    ai_credits_used: Optional[float] = FieldInfo(alias="aiCreditsUsed", default=None)
    """
    Marked-up integer AI credits used by the complete turn, including failover
    attempts.
    """

    cached_input_tokens: Optional[float] = FieldInfo(alias="cachedInputTokens", default=None)

    estimated_cost_micro_usd: Optional[float] = FieldInfo(alias="estimatedCostMicroUsd", default=None)

    input_tokens: Optional[float] = FieldInfo(alias="inputTokens", default=None)

    output_tokens: Optional[float] = FieldInfo(alias="outputTokens", default=None)

    reasoning_tokens: Optional[float] = FieldInfo(alias="reasoningTokens", default=None)

    total_tokens: Optional[float] = FieldInfo(alias="totalTokens", default=None)


class GenerateCreateResponse(BaseModel):
    """
    The generated (or modified) design plus model metadata and optional usage metadata.
    """

    id: Optional[str] = None
    """Provider response id for the generation turn."""

    model: Optional[Model] = None
    """
    The provider + model that actually produced the output (may differ from the
    requested model after failover).
    """

    output: Optional[Output] = None
    """The generated output for the requested block."""

    usage: Optional[Usage] = None
    """Aggregate token usage and billed AI credits for the turn.

    Estimated provider cost is included only by builder copilot endpoints in
    local/dev/QA.
    """
