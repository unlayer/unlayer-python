# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ValidateCreateResponse", "Data", "DataError"]


class DataError(BaseModel):
    code: str

    message: str

    path: str


class Data(BaseModel):
    valid: bool

    error_count: Optional[float] = FieldInfo(alias="errorCount", default=None)
    """
    Total number of issues found; greater than errors.length when the list was
    capped.
    """

    errors: Optional[List[DataError]] = None
    """Populated when valid is false, capped at 100 entries.

    Each issue carries the dotted path to the offending field, a human-readable
    message, and the underlying Zod issue code.
    """

    migrated_from: Optional[float] = FieldInfo(alias="migratedFrom", default=None)
    """
    Present when the design was upgraded from an older schemaVersion before
    validation; carries the original version number.
    """


class ValidateCreateResponse(BaseModel):
    data: Data

    success: Literal[True]
