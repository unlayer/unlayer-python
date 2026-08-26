# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AICreditsSettingUpdateResponse"]


class AICreditsSettingUpdateResponse(BaseModel):
    exhaustion_behavior: Literal["disable", "show_error"]

    has_signing_secret: bool

    threshold_alerts: List[int]

    webhook_url: Optional[str] = None

    signing_secret: Optional[str] = None
    """The HMAC signing secret. Returned ONLY on the response that first generates it."""
