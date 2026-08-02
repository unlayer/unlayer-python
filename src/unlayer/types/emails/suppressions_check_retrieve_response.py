# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SuppressionsCheckRetrieveResponse", "Data"]


class Data(BaseModel):
    email: Optional[str] = None

    suppressed: Optional[bool] = None


class SuppressionsCheckRetrieveResponse(BaseModel):
    data: Data
