# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["VerifyCreateResponse", "Data", "DataDkim", "DataOwnership"]


class DataDkim(BaseModel):
    status: Optional[str] = None

    tokens: Optional[List[str]] = None


class DataOwnership(BaseModel):
    verified: Optional[bool] = None


class Data(BaseModel):
    id: Optional[float] = None

    dkim: Optional[DataDkim] = None

    domain: Optional[str] = None

    ownership: Optional[DataOwnership] = None

    status: Optional[str] = None


class VerifyCreateResponse(BaseModel):
    data: Data
