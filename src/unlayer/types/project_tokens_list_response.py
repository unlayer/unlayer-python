# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectTokensListResponse", "Data"]


class Data(BaseModel):
    id: Optional[float] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)

    name: Optional[str] = None

    scope: Optional[str] = None

    workspace_id: Optional[float] = FieldInfo(alias="workspaceId", default=None)

    workspace_name: Optional[str] = FieldInfo(alias="workspaceName", default=None)


class ProjectTokensListResponse(BaseModel):
    data: Optional[List[Data]] = None
