# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AICreditsWebhooksDeliveriesretryCreateResponse"]


class AICreditsWebhooksDeliveriesretryCreateResponse(BaseModel):
    status: Optional[Literal["requeued"]] = None
