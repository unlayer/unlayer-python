# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ZipRetrieveResponse", "Data"]


class Data(BaseModel):
    success: Optional[bool] = None


class ZipRetrieveResponse(BaseModel):
    data: Optional[Data] = None
