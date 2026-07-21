# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EditorSessionCreateResponse", "Data"]


class Data(BaseModel):
    token: Optional[str] = None

    editor_url: Optional[str] = FieldInfo(alias="editorUrl", default=None)

    expires_at: Optional[str] = FieldInfo(alias="expiresAt", default=None)


class EditorSessionCreateResponse(BaseModel):
    data: Optional[Data] = None
