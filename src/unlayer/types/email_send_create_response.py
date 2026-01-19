# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailSendCreateResponse", "Data"]


class Data(BaseModel):
    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)
    """Unique message identifier"""

    status: Optional[Literal["sent", "queued", "failed"]] = None


class EmailSendCreateResponse(BaseModel):
    data: Optional[Data] = None
