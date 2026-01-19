# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DocumentGenerateCreateResponse", "Data"]


class Data(BaseModel):
    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Unique document identifier"""

    filename: Optional[str] = None
    """Generated filename"""

    pdf_url: Optional[str] = FieldInfo(alias="pdfUrl", default=None)
    """URL to download the generated PDF"""

    status: Optional[Literal["generating", "completed", "failed"]] = None


class DocumentGenerateCreateResponse(BaseModel):
    data: Optional[Data] = None
