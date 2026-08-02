# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["EventRetrieveResponse", "Data"]


class Data(BaseModel):
    metadata: Optional[Dict[str, object]] = None

    timestamp: Optional[datetime] = None

    type: Optional[str] = None
    """Event type (send, delivery, bounce, complaint)"""


class EventRetrieveResponse(BaseModel):
    data: List[Data]
