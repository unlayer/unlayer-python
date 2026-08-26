# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainCreateResponse", "Data", "DataDNSRecord"]


class DataDNSRecord(BaseModel):
    name: Optional[str] = None

    purpose: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class Data(BaseModel):
    id: Optional[float] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    dkim_tokens: Optional[List[str]] = FieldInfo(alias="dkimTokens", default=None)

    dns_records: Optional[List[DataDNSRecord]] = FieldInfo(alias="dnsRecords", default=None)

    domain: Optional[str] = None

    status: Optional[Literal["pending", "verified", "failed"]] = None


class DomainCreateResponse(BaseModel):
    data: Data
