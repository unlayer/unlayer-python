# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConvertFullToSimpleCreateResponse", "Data"]


class Data(BaseModel):
    design: Optional[Dict[str, object]] = None


class ConvertFullToSimpleCreateResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[Literal[True]] = None
