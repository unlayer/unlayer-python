# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExportImageCreateResponse", "Data"]


class Data(BaseModel):
    url: Optional[str] = None


class ExportImageCreateResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
