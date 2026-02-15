# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WorkspaceRetrieveResponse", "Data", "DataProject"]


class DataProject(BaseModel):
    id: Optional[float] = None

    name: Optional[str] = None

    status: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None

    name: Optional[str] = None

    projects: Optional[List[DataProject]] = None


class WorkspaceRetrieveResponse(BaseModel):
    data: Optional[Data] = None
