# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AICreditsSettingsRotateSecretCreateResponse"]


class AICreditsSettingsRotateSecretCreateResponse(BaseModel):
    signing_secret: str
    """The new HMAC signing secret. Shown only once."""
