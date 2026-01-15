# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ProjectWorkspacesListResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    name: Optional[str] = None


class ProjectWorkspacesListResponse(BaseModel):
    data: Optional[List[Data]] = None
