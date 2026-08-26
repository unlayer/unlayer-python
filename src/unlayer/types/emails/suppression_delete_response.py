# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SuppressionDeleteResponse", "Data"]


class Data(BaseModel):
    email: Optional[str] = None

    removed: Optional[bool] = None


class SuppressionDeleteResponse(BaseModel):
    data: Data
