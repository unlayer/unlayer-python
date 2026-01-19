# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExportZipListResponse", "Data"]


class Data(BaseModel):
    success: Optional[bool] = None


class ExportZipListResponse(BaseModel):
    data: Optional[Data] = None
