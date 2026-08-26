# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ExportImageCreateParams"]


class ExportImageCreateParams(TypedDict, total=False):
    design: Required[object]
    """Unlayer design JSON"""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """The project ID (required for PAT auth, auto-resolved for API key auth)"""

    custom_js: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="customJS")]

    design_tags: Annotated[object, PropertyInfo(alias="designTags")]

    design_tags_config: Annotated[object, PropertyInfo(alias="designTagsConfig")]

    device_scale_factor: Annotated[float, PropertyInfo(alias="deviceScaleFactor")]

    display_mode: Annotated[Literal["email", "web", "popup", "document"], PropertyInfo(alias="displayMode")]

    editor_version: Annotated[str, PropertyInfo(alias="editorVersion")]

    full_page: Annotated[bool, PropertyInfo(alias="fullPage")]

    height: float

    language: str

    languages: SequenceNotStr[str]

    merge_tags: Annotated[object, PropertyInfo(alias="mergeTags")]

    merge_tags_schema: Annotated[object, PropertyInfo(alias="mergeTagsSchema")]

    safe_html: Annotated[bool, PropertyInfo(alias="safeHtml")]

    width: float
