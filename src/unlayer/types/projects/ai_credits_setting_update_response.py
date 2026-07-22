# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AICreditsSettingUpdateResponse"]


class AICreditsSettingUpdateResponse(BaseModel):
    exhaustion_behavior: Optional[str] = None

    has_signing_secret: Optional[bool] = None

    signing_secret: Optional[str] = None
    """The HMAC signing secret. Returned ONLY on the response that first generates it."""

    threshold_alerts: Optional[List[float]] = None

    webhook_url: Optional[str] = None
