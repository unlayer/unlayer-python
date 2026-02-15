# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["HTMLRetrieveResponse", "Data"]


class Data(BaseModel):
    success: Optional[bool] = None


class HTMLRetrieveResponse(BaseModel):
    data: Optional[Data] = None
