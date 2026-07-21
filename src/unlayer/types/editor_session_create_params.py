# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EditorSessionCreateParams"]


class EditorSessionCreateParams(TypedDict, total=False):
    design: Required[Dict[str, object]]
    """Design JSON to load into the editor."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The project ID (required for PAT auth, auto-resolved for API key auth)"""

    display_mode: Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]
    """Editor display mode. Defaults to email."""
