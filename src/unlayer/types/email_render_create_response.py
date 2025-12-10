# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EmailRenderCreateResponse"]


class EmailRenderCreateResponse(BaseModel):
    html: Optional[str] = None
    """Rendered HTML content"""
