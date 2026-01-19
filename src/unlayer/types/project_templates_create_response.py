# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectTemplatesCreateResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Template ID"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    display_mode: Optional[Literal["email", "web", "document"]] = FieldInfo(alias="displayMode", default=None)
    """Template type/display mode"""

    name: Optional[str] = None
    """Template name"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class ProjectTemplatesCreateResponse(BaseModel):
    data: Optional[Data] = None
