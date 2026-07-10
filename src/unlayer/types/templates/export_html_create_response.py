# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExportHTMLCreateResponse", "Data", "DataChunks"]


class DataChunks(BaseModel):
    body: Optional[str] = None

    css: Optional[str] = None

    fonts: Optional[List[object]] = None

    js: Optional[str] = None


class Data(BaseModel):
    chunks: Optional[DataChunks] = None

    html: Optional[str] = None


class ExportHTMLCreateResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
