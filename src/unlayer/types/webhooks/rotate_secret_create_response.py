# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RotateSecretCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    secret: Optional[str] = None
    """New signing secret — only returned once. Store it securely."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class RotateSecretCreateResponse(BaseModel):
    data: Data
