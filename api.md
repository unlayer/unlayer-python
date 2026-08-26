# Blocks

Types:

```python
from unlayer.types import BlockRetrieveResponse
```

Methods:

- <code title="get /v3/blocks">client.blocks.<a href="./src/unlayer/resources/blocks.py">retrieve</a>(\*\*<a href="src/unlayer/types/block_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/block_retrieve_response.py">BlockRetrieveResponse</a></code>

# Domains

Types:

```python
from unlayer.types import (
    DomainCreateResponse,
    DomainRetrieveResponse,
    DomainListResponse,
    DomainDeleteResponse,
)
```

Methods:

- <code title="post /v3/domains">client.domains.<a href="./src/unlayer/resources/domains/domains.py">create</a>(\*\*<a href="src/unlayer/types/domain_create_params.py">params</a>) -> <a href="./src/unlayer/types/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /v3/domains/{id}">client.domains.<a href="./src/unlayer/resources/domains/domains.py">retrieve</a>(id) -> <a href="./src/unlayer/types/domain_retrieve_response.py">DomainRetrieveResponse</a></code>
- <code title="get /v3/domains">client.domains.<a href="./src/unlayer/resources/domains/domains.py">list</a>() -> <a href="./src/unlayer/types/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /v3/domains/{id}">client.domains.<a href="./src/unlayer/resources/domains/domains.py">delete</a>(id) -> <a href="./src/unlayer/types/domain_delete_response.py">DomainDeleteResponse</a></code>

## Verify

Types:

```python
from unlayer.types.domains import VerifyCreateResponse
```

Methods:

- <code title="post /v3/domains/{id}/verify">client.domains.verify.<a href="./src/unlayer/resources/domains/verify.py">create</a>(id) -> <a href="./src/unlayer/types/domains/verify_create_response.py">VerifyCreateResponse</a></code>

# EditorSessions

Types:

```python
from unlayer.types import EditorSessionCreateResponse
```

Methods:

- <code title="post /v3/editor-sessions">client.editor_sessions.<a href="./src/unlayer/resources/editor_sessions.py">create</a>(\*\*<a href="src/unlayer/types/editor_session_create_params.py">params</a>) -> <a href="./src/unlayer/types/editor_session_create_response.py">EditorSessionCreateResponse</a></code>

# Emails

Types:

```python
from unlayer.types import EmailCreateResponse, EmailRetrieveResponse, EmailListResponse
```

Methods:

- <code title="post /v3/emails">client.emails.<a href="./src/unlayer/resources/emails/emails.py">create</a>(\*\*<a href="src/unlayer/types/email_create_params.py">params</a>) -> <a href="./src/unlayer/types/email_create_response.py">EmailCreateResponse</a></code>
- <code title="get /v3/emails/{id}">client.emails.<a href="./src/unlayer/resources/emails/emails.py">retrieve</a>(id) -> <a href="./src/unlayer/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="get /v3/emails">client.emails.<a href="./src/unlayer/resources/emails/emails.py">list</a>(\*\*<a href="src/unlayer/types/email_list_params.py">params</a>) -> <a href="./src/unlayer/types/email_list_response.py">EmailListResponse</a></code>

## Events

Types:

```python
from unlayer.types.emails import EventRetrieveResponse
```

Methods:

- <code title="get /v3/emails/{id}/events">client.emails.events.<a href="./src/unlayer/resources/emails/events.py">retrieve</a>(id) -> <a href="./src/unlayer/types/emails/event_retrieve_response.py">EventRetrieveResponse</a></code>

## Render

Types:

```python
from unlayer.types.emails import RenderCreateResponse
```

Methods:

- <code title="post /v3/emails/render">client.emails.render.<a href="./src/unlayer/resources/emails/render.py">create</a>(\*\*<a href="src/unlayer/types/emails/render_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/render_create_response.py">RenderCreateResponse</a></code>

## Settings

Types:

```python
from unlayer.types.emails import SettingRetrieveResponse, SettingUpdateResponse
```

Methods:

- <code title="get /v3/emails/settings">client.emails.settings.<a href="./src/unlayer/resources/emails/settings.py">retrieve</a>() -> <a href="./src/unlayer/types/emails/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
- <code title="patch /v3/emails/settings">client.emails.settings.<a href="./src/unlayer/resources/emails/settings.py">update</a>(\*\*<a href="src/unlayer/types/emails/setting_update_params.py">params</a>) -> <a href="./src/unlayer/types/emails/setting_update_response.py">SettingUpdateResponse</a></code>

## Stats

Types:

```python
from unlayer.types.emails import StatRetrieveResponse
```

Methods:

- <code title="get /v3/emails/stats">client.emails.stats.<a href="./src/unlayer/resources/emails/stats.py">retrieve</a>(\*\*<a href="src/unlayer/types/emails/stat_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/emails/stat_retrieve_response.py">StatRetrieveResponse</a></code>

## Suppressions

Types:

```python
from unlayer.types.emails import (
    SuppressionCreateResponse,
    SuppressionRetrieveResponse,
    SuppressionDeleteResponse,
)
```

Methods:

- <code title="post /v3/emails/suppressions">client.emails.suppressions.<a href="./src/unlayer/resources/emails/suppressions.py">create</a>(\*\*<a href="src/unlayer/types/emails/suppression_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/suppression_create_response.py">SuppressionCreateResponse</a></code>
- <code title="get /v3/emails/suppressions">client.emails.suppressions.<a href="./src/unlayer/resources/emails/suppressions.py">retrieve</a>(\*\*<a href="src/unlayer/types/emails/suppression_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/emails/suppression_retrieve_response.py">SuppressionRetrieveResponse</a></code>
- <code title="delete /v3/emails/suppressions">client.emails.suppressions.<a href="./src/unlayer/resources/emails/suppressions.py">delete</a>(\*\*<a href="src/unlayer/types/emails/suppression_delete_params.py">params</a>) -> <a href="./src/unlayer/types/emails/suppression_delete_response.py">SuppressionDeleteResponse</a></code>

## SuppressionsCheck

Types:

```python
from unlayer.types.emails import SuppressionsCheckRetrieveResponse
```

Methods:

- <code title="get /v3/emails/suppressions/check">client.emails.suppressions_check.<a href="./src/unlayer/resources/emails/suppressions_check.py">retrieve</a>(\*\*<a href="src/unlayer/types/emails/suppressions_check_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/emails/suppressions_check_retrieve_response.py">SuppressionsCheckRetrieveResponse</a></code>

## Template

Types:

```python
from unlayer.types.emails import TemplateCreateResponse
```

Methods:

- <code title="post /v3/emails/template">client.emails.template.<a href="./src/unlayer/resources/emails/template.py">create</a>(\*\*<a href="src/unlayer/types/emails/template_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/template_create_response.py">TemplateCreateResponse</a></code>

# Me

## Subscription

Types:

```python
from unlayer.types.me import SubscriptionRetrieveResponse
```

Methods:

- <code title="get /v3/me/subscription">client.me.subscription.<a href="./src/unlayer/resources/me/subscription.py">retrieve</a>(\*\*<a href="src/unlayer/types/me/subscription_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/me/subscription_retrieve_response.py">SubscriptionRetrieveResponse</a></code>

# Projects

Types:

```python
from unlayer.types import ProjectRetrieveResponse
```

Methods:

- <code title="get /v3/projects/{id}">client.projects.<a href="./src/unlayer/resources/projects/projects.py">retrieve</a>(id) -> <a href="./src/unlayer/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

## AICredits

Types:

```python
from unlayer.types.projects import AICreditRetrieveResponse
```

Methods:

- <code title="get /v3/projects/{id}/ai-credits">client.projects.ai_credits.<a href="./src/unlayer/resources/projects/ai_credits.py">retrieve</a>(id) -> <a href="./src/unlayer/types/projects/ai_credit_retrieve_response.py">AICreditRetrieveResponse</a></code>

## AICreditsSettings

Types:

```python
from unlayer.types.projects import AICreditsSettingRetrieveResponse, AICreditsSettingUpdateResponse
```

Methods:

- <code title="get /v3/projects/{id}/ai-credits/settings">client.projects.ai_credits_settings.<a href="./src/unlayer/resources/projects/ai_credits_settings.py">retrieve</a>(id) -> <a href="./src/unlayer/types/projects/ai_credits_setting_retrieve_response.py">AICreditsSettingRetrieveResponse</a></code>
- <code title="put /v3/projects/{id}/ai-credits/settings">client.projects.ai_credits_settings.<a href="./src/unlayer/resources/projects/ai_credits_settings.py">update</a>(id, \*\*<a href="src/unlayer/types/projects/ai_credits_setting_update_params.py">params</a>) -> <a href="./src/unlayer/types/projects/ai_credits_setting_update_response.py">AICreditsSettingUpdateResponse</a></code>

## AICreditsSettingsRotateSecret

Types:

```python
from unlayer.types.projects import AICreditsSettingsRotateSecretCreateResponse
```

Methods:

- <code title="post /v3/projects/{id}/ai-credits/settings/rotate-secret">client.projects.ai_credits_settings_rotate_secret.<a href="./src/unlayer/resources/projects/ai_credits_settings_rotate_secret.py">create</a>(id) -> <a href="./src/unlayer/types/projects/ai_credits_settings_rotate_secret_create_response.py">AICreditsSettingsRotateSecretCreateResponse</a></code>

## AICreditsUsage

Types:

```python
from unlayer.types.projects import AICreditsUsageRetrieveResponse
```

Methods:

- <code title="get /v3/projects/{id}/ai-credits/usage">client.projects.ai_credits_usage.<a href="./src/unlayer/resources/projects/ai_credits_usage.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/projects/ai_credits_usage_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/projects/ai_credits_usage_retrieve_response.py">AICreditsUsageRetrieveResponse</a></code>

## AICreditsWebhooksDeliveries

Types:

```python
from unlayer.types.projects import AICreditsWebhooksDeliveryRetrieveResponse
```

Methods:

- <code title="get /v3/projects/{id}/ai-credits/webhooks/deliveries">client.projects.ai_credits_webhooks_deliveries.<a href="./src/unlayer/resources/projects/ai_credits_webhooks_deliveries.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/projects/ai_credits_webhooks_delivery_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/projects/ai_credits_webhooks_delivery_retrieve_response.py">AICreditsWebhooksDeliveryRetrieveResponse</a></code>

## AICreditsWebhooksDeliveriesattempts

Types:

```python
from unlayer.types.projects import AICreditsWebhooksDeliveriesattemptRetrieveResponse
```

Methods:

- <code title="get /v3/projects/{id}/ai-credits/webhooks/deliveries/{deliveryId}/attempts">client.projects.ai_credits_webhooks_deliveriesattempts.<a href="./src/unlayer/resources/projects/ai_credits_webhooks_deliveriesattempts.py">retrieve</a>(delivery_id, \*, id, \*\*<a href="src/unlayer/types/projects/ai_credits_webhooks_deliveriesattempt_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/projects/ai_credits_webhooks_deliveriesattempt_retrieve_response.py">AICreditsWebhooksDeliveriesattemptRetrieveResponse</a></code>

## AICreditsWebhooksDeliveriesretry

Types:

```python
from unlayer.types.projects import AICreditsWebhooksDeliveriesretryCreateResponse
```

Methods:

- <code title="post /v3/projects/{id}/ai-credits/webhooks/deliveries/{deliveryId}/retry">client.projects.ai_credits_webhooks_deliveriesretry.<a href="./src/unlayer/resources/projects/ai_credits_webhooks_deliveriesretry.py">create</a>(delivery_id, \*, id) -> <a href="./src/unlayer/types/projects/ai_credits_webhooks_deliveriesretry_create_response.py">AICreditsWebhooksDeliveriesretryCreateResponse</a></code>

# Templates

Types:

```python
from unlayer.types import TemplateRetrieveResponse, TemplateListResponse
```

Methods:

- <code title="get /v3/templates/{id}">client.templates.<a href="./src/unlayer/resources/templates/templates.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/template_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="get /v3/templates">client.templates.<a href="./src/unlayer/resources/templates/templates.py">list</a>(\*\*<a href="src/unlayer/types/template_list_params.py">params</a>) -> <a href="./src/unlayer/types/template_list_response.py">SyncCursorPage[TemplateListResponse]</a></code>

## ConvertFullToSimple

Types:

```python
from unlayer.types.templates import ConvertFullToSimpleCreateResponse
```

Methods:

- <code title="post /v3/templates/convert/full-to-simple">client.templates.convert_full_to_simple.<a href="./src/unlayer/resources/templates/convert_full_to_simple.py">create</a>(\*\*<a href="src/unlayer/types/templates/convert_full_to_simple_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/convert_full_to_simple_create_response.py">ConvertFullToSimpleCreateResponse</a></code>

## ConvertSimpleToFull

Types:

```python
from unlayer.types.templates import ConvertSimpleToFullCreateResponse
```

Methods:

- <code title="post /v3/templates/convert/simple-to-full">client.templates.convert_simple_to_full.<a href="./src/unlayer/resources/templates/convert_simple_to_full.py">create</a>(\*\*<a href="src/unlayer/types/templates/convert_simple_to_full_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/convert_simple_to_full_create_response.py">ConvertSimpleToFullCreateResponse</a></code>

## ExportHTML

Types:

```python
from unlayer.types.templates import ExportHTMLCreateResponse
```

Methods:

- <code title="post /v3/templates/export/html">client.templates.export_html.<a href="./src/unlayer/resources/templates/export_html.py">create</a>(\*\*<a href="src/unlayer/types/templates/export_html_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/export_html_create_response.py">ExportHTMLCreateResponse</a></code>

## ExportImage

Types:

```python
from unlayer.types.templates import ExportImageCreateResponse
```

Methods:

- <code title="post /v3/templates/export/image">client.templates.export_image.<a href="./src/unlayer/resources/templates/export_image.py">create</a>(\*\*<a href="src/unlayer/types/templates/export_image_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/export_image_create_response.py">ExportImageCreateResponse</a></code>

## ExportPdf

Types:

```python
from unlayer.types.templates import ExportPdfCreateResponse
```

Methods:

- <code title="post /v3/templates/export/pdf">client.templates.export_pdf.<a href="./src/unlayer/resources/templates/export_pdf.py">create</a>(\*\*<a href="src/unlayer/types/templates/export_pdf_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/export_pdf_create_response.py">ExportPdfCreateResponse</a></code>

## ExportZip

Types:

```python
from unlayer.types.templates import ExportZipCreateResponse
```

Methods:

- <code title="post /v3/templates/export/zip">client.templates.export_zip.<a href="./src/unlayer/resources/templates/export_zip.py">create</a>(\*\*<a href="src/unlayer/types/templates/export_zip_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/export_zip_create_response.py">ExportZipCreateResponse</a></code>

## Generate

Types:

```python
from unlayer.types.templates import GenerateCreateResponse
```

Methods:

- <code title="post /v3/templates/generate">client.templates.generate.<a href="./src/unlayer/resources/templates/generate.py">create</a>(\*\*<a href="src/unlayer/types/templates/generate_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/generate_create_response.py">GenerateCreateResponse</a></code>

## Import

Types:

```python
from unlayer.types.templates import ImportCreateResponse
```

Methods:

- <code title="post /v3/templates/import">client.templates.import*.<a href="./src/unlayer/resources/templates/import*.py">create</a>(\*\*<a href="src/unlayer/types/templates/import_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/import_create_response.py">ImportCreateResponse</a></code>

## Schema

Methods:

- <code title="get /v3/templates/schema">client.templates.schema.<a href="./src/unlayer/resources/templates/schema.py">retrieve</a>(\*\*<a href="src/unlayer/types/templates/schema_retrieve_params.py">params</a>) -> None</code>

## Validate

Types:

```python
from unlayer.types.templates import ValidateCreateResponse
```

Methods:

- <code title="post /v3/templates/validate">client.templates.validate.<a href="./src/unlayer/resources/templates/validate.py">create</a>(\*\*<a href="src/unlayer/types/templates/validate_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/validate_create_response.py">ValidateCreateResponse</a></code>

# Webhooks

Types:

```python
from unlayer.types import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
)
```

Methods:

- <code title="post /v3/webhooks">client.webhooks.<a href="./src/unlayer/resources/webhooks/webhooks.py">create</a>(\*\*<a href="src/unlayer/types/webhook_create_params.py">params</a>) -> <a href="./src/unlayer/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /v3/webhooks/{id}">client.webhooks.<a href="./src/unlayer/resources/webhooks/webhooks.py">retrieve</a>(id) -> <a href="./src/unlayer/types/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="patch /v3/webhooks/{id}">client.webhooks.<a href="./src/unlayer/resources/webhooks/webhooks.py">update</a>(id, \*\*<a href="src/unlayer/types/webhook_update_params.py">params</a>) -> <a href="./src/unlayer/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /v3/webhooks">client.webhooks.<a href="./src/unlayer/resources/webhooks/webhooks.py">list</a>() -> <a href="./src/unlayer/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v3/webhooks/{id}">client.webhooks.<a href="./src/unlayer/resources/webhooks/webhooks.py">delete</a>(id) -> <a href="./src/unlayer/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>

## RotateSecret

Types:

```python
from unlayer.types.webhooks import RotateSecretCreateResponse
```

Methods:

- <code title="post /v3/webhooks/{id}/rotate-secret">client.webhooks.rotate_secret.<a href="./src/unlayer/resources/webhooks/rotate_secret.py">create</a>(id) -> <a href="./src/unlayer/types/webhooks/rotate_secret_create_response.py">RotateSecretCreateResponse</a></code>

# Workspaces

Types:

```python
from unlayer.types import WorkspaceRetrieveResponse, WorkspaceListResponse
```

Methods:

- <code title="get /v3/workspaces/{workspaceId}">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">retrieve</a>(workspace_id) -> <a href="./src/unlayer/types/workspace_retrieve_response.py">WorkspaceRetrieveResponse</a></code>
- <code title="get /v3/workspaces">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">list</a>() -> <a href="./src/unlayer/types/workspace_list_response.py">WorkspaceListResponse</a></code>
