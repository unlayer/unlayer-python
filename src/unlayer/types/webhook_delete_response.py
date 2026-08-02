# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WebhookDeleteResponse", "Data"]


class Data(BaseModel):
    success: Optional[bool] = None


class WebhookDeleteResponse(BaseModel):
    data: Optional[Data] = None
