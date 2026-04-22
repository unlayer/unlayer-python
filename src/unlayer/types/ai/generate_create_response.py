# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["GenerateCreateResponse", "Output", "Usage"]


class Output(BaseModel):
    block_type: Optional[str] = FieldInfo(alias="blockType", default=None)

    data: Optional[Dict[str, object]] = None
    """Generated design data"""

    type: Optional[str] = None


class Usage(BaseModel):
    cached_input_tokens: Optional[int] = FieldInfo(alias="cachedInputTokens", default=None)

    input_tokens: Optional[int] = FieldInfo(alias="inputTokens", default=None)

    output_tokens: Optional[int] = FieldInfo(alias="outputTokens", default=None)

    reasoning_tokens: Optional[int] = FieldInfo(alias="reasoningTokens", default=None)

    total_tokens: Optional[int] = FieldInfo(alias="totalTokens", default=None)


class GenerateCreateResponse(BaseModel):
    """Successfully generated design"""

    id: Optional[str] = None
    """AI response ID"""

    model: Optional[str] = None

    output: Optional[Output] = None

    provider: Optional[str] = None

    usage: Optional[Usage] = None
