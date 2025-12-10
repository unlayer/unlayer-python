# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DocumentDocumentsRetrieveResponse"]


class DocumentDocumentsRetrieveResponse(BaseModel):
    id: Optional[str] = None
    """Document ID"""

    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """When the document generation was completed"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the document was created"""

    filename: Optional[str] = None
    """Generated filename"""

    file_size: Optional[float] = FieldInfo(alias="fileSize", default=None)
    """File size in bytes"""

    page_count: Optional[float] = FieldInfo(alias="pageCount", default=None)
    """Number of pages in the PDF"""

    pdf_url: Optional[str] = FieldInfo(alias="pdfUrl", default=None)
    """URL to download the PDF"""

    status: Optional[Literal["generating", "completed", "failed"]] = None
    """Current document status"""
