# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionRetrieveResponse", "Data", "DataFeature", "DataLimit"]


class DataFeature(BaseModel):
    available: Optional[bool] = None

    name: Optional[str] = None


class DataLimit(BaseModel):
    name: Optional[str] = None

    unit: Optional[str] = None

    value: Optional[float] = None


class Data(BaseModel):
    expires_at: Optional[str] = FieldInfo(alias="expiresAt", default=None)

    features: Optional[List[DataFeature]] = None

    limits: Optional[List[DataLimit]] = None

    plan_name: Optional[str] = FieldInfo(alias="planName", default=None)

    status: Optional[str] = None


class SubscriptionRetrieveResponse(BaseModel):
    data: Optional[Data] = None
