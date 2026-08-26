# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StatRetrieveResponse", "Data", "DataUnionMember0", "DataUnionMember1"]


class DataUnionMember0(BaseModel):
    """Aggregated totals for the requested period (default response)."""

    bounced: Optional[float] = None
    """Number of emails that were bounced by the recipient mail server."""

    bounce_rate: Optional[float] = FieldInfo(alias="bounceRate", default=None)
    """Bounced / sent as a percentage (0-100, 2 decimal places)."""

    complained: Optional[float] = None
    """Number of spam complaint events received."""

    delivered: Optional[float] = None
    """Number of successfully delivered emails."""

    delivery_rate: Optional[float] = FieldInfo(alias="deliveryRate", default=None)
    """Delivered / sent as a percentage (0-100, 2 decimal places)."""

    period: Optional[Literal["7d", "30d", "90d"]] = None
    """The period these stats cover."""

    sent: Optional[float] = None
    """Total emails sent (one per recipient)."""


class DataUnionMember1(BaseModel):
    bounced: Optional[float] = None
    """Emails bounced on this day."""

    complained: Optional[float] = None
    """Spam complaints received for this send cohort."""

    date: Optional[datetime.date] = None
    """The email send-cohort day in YYYY-MM-DD format."""

    delivered: Optional[float] = None
    """Emails from this send cohort that were delivered."""

    sent: Optional[float] = None
    """Emails sent on this day."""


Data: TypeAlias = Union[DataUnionMember0, List[DataUnionMember1]]


class StatRetrieveResponse(BaseModel):
    """Email statistics.

    Shape depends on the `groupBy` query parameter: an aggregated totals object by default, or a daily breakdown array when groupBy=day.
    """

    data: Data
    """Aggregated totals for the requested period (default response)."""
