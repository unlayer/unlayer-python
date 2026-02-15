# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectRetrieveResponse", "Data", "DataWorkspace"]


class DataWorkspace(BaseModel):
    id: Optional[float] = None

    name: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None
    """The project ID."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the project was created."""

    name: Optional[str] = None
    """The project name."""

    status: Optional[str] = None
    """The project status."""

    workspace: Optional[DataWorkspace] = None


class ProjectRetrieveResponse(BaseModel):
    data: Optional[Data] = None
