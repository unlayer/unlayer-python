# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentDocumentsRetrieveParams"]


class DocumentDocumentsRetrieveParams(TypedDict, total=False):
    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The project ID (required for PAT auth, not needed for API Key auth)"""
