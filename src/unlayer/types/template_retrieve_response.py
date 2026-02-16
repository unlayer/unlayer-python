# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TemplateRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    design: Optional[Dict[str, object]] = None

    display_mode: Optional[Literal["email", "web", "document"]] = FieldInfo(alias="displayMode", default=None)

    html: Optional[str] = None

    name: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class TemplateRetrieveResponse(BaseModel):
    data: Optional[Data] = None
