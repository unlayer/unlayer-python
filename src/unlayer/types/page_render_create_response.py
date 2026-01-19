# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PageRenderCreateResponse", "Data"]


class Data(BaseModel):
    html: Optional[str] = None
    """Rendered HTML content"""


class PageRenderCreateResponse(BaseModel):
    data: Optional[Data] = None
