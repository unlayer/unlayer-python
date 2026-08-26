# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BlockRetrieveResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Block ID"""

    category: Optional[str] = None
    """Block category"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    data: Optional[Dict[str, object]] = None
    """The block design JSON. Omitted when includeData=false is passed."""

    display_mode: Optional[str] = FieldInfo(alias="displayMode", default=None)
    """Display mode the block was saved for: email, web, popup, or document"""

    is_sync_enabled: Optional[bool] = FieldInfo(alias="isSyncEnabled", default=None)
    """Whether the block is currently a synced block"""

    sync_id: Optional[str] = FieldInfo(alias="syncId", default=None)
    """Synced-block ID referenced by designs using this block.

    Null when the block has never been synced.
    """

    tags: Optional[List[str]] = None
    """Block tags"""

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)
    """URL of the auto-generated block thumbnail, if available"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """
    End-user ID the block was saved under (the user id your app passes to the
    editor). Null for shared project blocks.
    """


class BlockRetrieveResponse(BaseModel):
    data: List[Data]

    has_more: bool
    """Whether there are more results after this page"""

    next_cursor: Optional[str] = None
    """Cursor for the next page. Null if no more results."""
