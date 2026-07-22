# EditorSessions

Types:

```python
from unlayer.types import EditorSessionCreateResponse
```

Methods:

- <code title="post /v3/editor-sessions">client.editor_sessions.<a href="./src/unlayer/resources/editor_sessions.py">create</a>(\*\*<a href="src/unlayer/types/editor_session_create_params.py">params</a>) -> <a href="./src/unlayer/types/editor_session_create_response.py">EditorSessionCreateResponse</a></code>

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
- <code title="get /v3/templates/generate">client.templates.generate.<a href="./src/unlayer/resources/templates/generate.py">retrieve</a>() -> None</code>

## Import

Types:

```python
from unlayer.types.templates import ImportCreateResponse
```

Methods:

- <code title="post /v3/templates/import">client.templates.import*.<a href="./src/unlayer/resources/templates/import*.py">create</a>(\*\*<a href="src/unlayer/types/templates/import_create_params.py">params</a>) -> <a href="./src/unlayer/types/templates/import_create_response.py">ImportCreateResponse</a></code>

# Workspaces

Types:

```python
from unlayer.types import WorkspaceRetrieveResponse, WorkspaceListResponse
```

Methods:

- <code title="get /v3/workspaces/{workspaceId}">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">retrieve</a>(workspace_id) -> <a href="./src/unlayer/types/workspace_retrieve_response.py">WorkspaceRetrieveResponse</a></code>
- <code title="get /v3/workspaces">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">list</a>() -> <a href="./src/unlayer/types/workspace_list_response.py">WorkspaceListResponse</a></code>
