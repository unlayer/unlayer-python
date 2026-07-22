# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AICreditsSettingRetrieveResponse"]


class AICreditsSettingRetrieveResponse(BaseModel):
    exhaustion_behavior: Optional[str] = None

    has_signing_secret: Optional[bool] = None

    threshold_alerts: Optional[List[float]] = None

    webhook_url: Optional[str] = None
