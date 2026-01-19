# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExportImageListResponse", "Data"]


class Data(BaseModel):
    success: Optional[bool] = None


class ExportImageListResponse(BaseModel):
    data: Optional[Data] = None
