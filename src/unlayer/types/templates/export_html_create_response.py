# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["ExportHTMLCreateResponse", "Data", "DataChunks"]


class DataChunks(BaseModel):
    body: Optional[str] = None

    css: Optional[str] = None

    fonts: Optional[List[object]] = None

    js: Optional[str] = None

    tags: Optional[List[str]] = None


class Data(BaseModel):
    amp: Optional[Dict[str, object]] = None

    chunks: Optional[DataChunks] = None

    design: Optional[Dict[str, object]] = None

    html: Optional[str] = None


class ExportHTMLCreateResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
