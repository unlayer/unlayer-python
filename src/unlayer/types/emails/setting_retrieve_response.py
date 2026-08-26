# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SettingRetrieveResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the settings row was first created."""

    default_from_name: Optional[str] = FieldInfo(alias="defaultFromName", default=None)
    """Default sender display name"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the settings were last updated."""


class SettingRetrieveResponse(BaseModel):
    data: Data
