# Project

Types:

```python
from unlayer.types import (
    ProjectAPIKeysCreateResponse,
    ProjectAPIKeysListResponse,
    ProjectAPIKeysRetrieveResponse,
    ProjectAPIKeysUpdateResponse,
    ProjectCurrentListResponse,
    ProjectDomainsCreateResponse,
    ProjectDomainsListResponse,
    ProjectDomainsRetrieveResponse,
    ProjectDomainsUpdateResponse,
    ProjectTemplatesCreateResponse,
    ProjectTemplatesListResponse,
    ProjectTemplatesRetrieveResponse,
    ProjectTemplatesUpdateResponse,
)
```

Methods:

- <code title="post /project/v1/api-keys">client.project.<a href="./src/unlayer/resources/project/project.py">api_keys_create</a>(\*\*<a href="src/unlayer/types/project_api_keys_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_api_keys_create_response.py">ProjectAPIKeysCreateResponse</a></code>
- <code title="delete /project/v1/api-keys/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">api_keys_delete</a>(id) -> None</code>
- <code title="get /project/v1/api-keys">client.project.<a href="./src/unlayer/resources/project/project.py">api_keys_list</a>() -> <a href="./src/unlayer/types/project_api_keys_list_response.py">ProjectAPIKeysListResponse</a></code>
- <code title="get /project/v1/api-keys/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">api_keys_retrieve</a>(id) -> <a href="./src/unlayer/types/project_api_keys_retrieve_response.py">ProjectAPIKeysRetrieveResponse</a></code>
- <code title="put /project/v1/api-keys/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">api_keys_update</a>(id, \*\*<a href="src/unlayer/types/project_api_keys_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_api_keys_update_response.py">ProjectAPIKeysUpdateResponse</a></code>
- <code title="get /project/v1/current">client.project.<a href="./src/unlayer/resources/project/project.py">current_list</a>() -> <a href="./src/unlayer/types/project_current_list_response.py">ProjectCurrentListResponse</a></code>
- <code title="post /project/v1/domains">client.project.<a href="./src/unlayer/resources/project/project.py">domains_create</a>(\*\*<a href="src/unlayer/types/project_domains_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_domains_create_response.py">ProjectDomainsCreateResponse</a></code>
- <code title="delete /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">domains_delete</a>(id) -> None</code>
- <code title="get /project/v1/domains">client.project.<a href="./src/unlayer/resources/project/project.py">domains_list</a>() -> <a href="./src/unlayer/types/project_domains_list_response.py">ProjectDomainsListResponse</a></code>
- <code title="get /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">domains_retrieve</a>(id) -> <a href="./src/unlayer/types/project_domains_retrieve_response.py">ProjectDomainsRetrieveResponse</a></code>
- <code title="put /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">domains_update</a>(id, \*\*<a href="src/unlayer/types/project_domains_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_domains_update_response.py">ProjectDomainsUpdateResponse</a></code>
- <code title="post /project/v1/templates">client.project.<a href="./src/unlayer/resources/project/project.py">templates_create</a>(\*\*<a href="src/unlayer/types/project_templates_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_templates_create_response.py">ProjectTemplatesCreateResponse</a></code>
- <code title="delete /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">templates_delete</a>(id) -> None</code>
- <code title="get /project/v1/templates">client.project.<a href="./src/unlayer/resources/project/project.py">templates_list</a>() -> <a href="./src/unlayer/types/project_templates_list_response.py">ProjectTemplatesListResponse</a></code>
- <code title="get /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">templates_retrieve</a>(id) -> <a href="./src/unlayer/types/project_templates_retrieve_response.py">ProjectTemplatesRetrieveResponse</a></code>
- <code title="put /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project/project.py">templates_update</a>(id, \*\*<a href="src/unlayer/types/project_templates_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_templates_update_response.py">ProjectTemplatesUpdateResponse</a></code>

## V1

Types:

```python
from unlayer.types.project import (
    V1APIKeysCreateResponse,
    V1APIKeysListResponse,
    V1APIKeysRetrieveResponse,
    V1APIKeysUpdateResponse,
    V1CurrentListResponse,
    V1DomainsCreateResponse,
    V1DomainsListResponse,
    V1DomainsRetrieveResponse,
    V1DomainsUpdateResponse,
    V1TemplatesCreateResponse,
    V1TemplatesListResponse,
    V1TemplatesRetrieveResponse,
    V1TemplatesUpdateResponse,
)
```

Methods:

- <code title="post /project/v1/api-keys">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">api_keys_create</a>(\*\*<a href="src/unlayer/types/project/v1_api_keys_create_params.py">params</a>) -> <a href="./src/unlayer/types/project/v1_api_keys_create_response.py">V1APIKeysCreateResponse</a></code>
- <code title="delete /project/v1/api-keys/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">api_keys_delete</a>(id) -> None</code>
- <code title="get /project/v1/api-keys">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">api_keys_list</a>() -> <a href="./src/unlayer/types/project/v1_api_keys_list_response.py">V1APIKeysListResponse</a></code>
- <code title="get /project/v1/api-keys/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">api_keys_retrieve</a>(id) -> <a href="./src/unlayer/types/project/v1_api_keys_retrieve_response.py">V1APIKeysRetrieveResponse</a></code>
- <code title="put /project/v1/api-keys/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">api_keys_update</a>(id, \*\*<a href="src/unlayer/types/project/v1_api_keys_update_params.py">params</a>) -> <a href="./src/unlayer/types/project/v1_api_keys_update_response.py">V1APIKeysUpdateResponse</a></code>
- <code title="get /project/v1/current">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">current_list</a>() -> <a href="./src/unlayer/types/project/v1_current_list_response.py">V1CurrentListResponse</a></code>
- <code title="post /project/v1/domains">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">domains_create</a>(\*\*<a href="src/unlayer/types/project/v1_domains_create_params.py">params</a>) -> <a href="./src/unlayer/types/project/v1_domains_create_response.py">V1DomainsCreateResponse</a></code>
- <code title="delete /project/v1/domains/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">domains_delete</a>(id) -> None</code>
- <code title="get /project/v1/domains">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">domains_list</a>() -> <a href="./src/unlayer/types/project/v1_domains_list_response.py">V1DomainsListResponse</a></code>
- <code title="get /project/v1/domains/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">domains_retrieve</a>(id) -> <a href="./src/unlayer/types/project/v1_domains_retrieve_response.py">V1DomainsRetrieveResponse</a></code>
- <code title="put /project/v1/domains/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">domains_update</a>(id, \*\*<a href="src/unlayer/types/project/v1_domains_update_params.py">params</a>) -> <a href="./src/unlayer/types/project/v1_domains_update_response.py">V1DomainsUpdateResponse</a></code>
- <code title="post /project/v1/templates">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">templates_create</a>(\*\*<a href="src/unlayer/types/project/v1_templates_create_params.py">params</a>) -> <a href="./src/unlayer/types/project/v1_templates_create_response.py">V1TemplatesCreateResponse</a></code>
- <code title="delete /project/v1/templates/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">templates_delete</a>(id) -> None</code>
- <code title="get /project/v1/templates">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">templates_list</a>() -> <a href="./src/unlayer/types/project/v1_templates_list_response.py">V1TemplatesListResponse</a></code>
- <code title="get /project/v1/templates/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">templates_retrieve</a>(id) -> <a href="./src/unlayer/types/project/v1_templates_retrieve_response.py">V1TemplatesRetrieveResponse</a></code>
- <code title="put /project/v1/templates/{id}">client.project.v1.<a href="./src/unlayer/resources/project/v1.py">templates_update</a>(id, \*\*<a href="src/unlayer/types/project/v1_templates_update_params.py">params</a>) -> <a href="./src/unlayer/types/project/v1_templates_update_response.py">V1TemplatesUpdateResponse</a></code>

# Emails

Types:

```python
from unlayer.types import (
    EmailEmailsRetrieveResponse,
    EmailRenderCreateResponse,
    EmailSendCreateResponse,
    EmailSendTemplateTemplateResponse,
)
```

Methods:

- <code title="get /emails/v1/emails/{id}">client.emails.<a href="./src/unlayer/resources/emails/emails.py">emails_retrieve</a>(id) -> <a href="./src/unlayer/types/email_emails_retrieve_response.py">EmailEmailsRetrieveResponse</a></code>
- <code title="post /emails/v1/render">client.emails.<a href="./src/unlayer/resources/emails/emails.py">render_create</a>(\*\*<a href="src/unlayer/types/email_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/email_render_create_response.py">EmailRenderCreateResponse</a></code>
- <code title="post /emails/v1/send">client.emails.<a href="./src/unlayer/resources/emails/emails.py">send_create</a>(\*\*<a href="src/unlayer/types/email_send_create_params.py">params</a>) -> <a href="./src/unlayer/types/email_send_create_response.py">EmailSendCreateResponse</a></code>
- <code title="post /emails/v1/send/template">client.emails.<a href="./src/unlayer/resources/emails/emails.py">send_template_template</a>(\*\*<a href="src/unlayer/types/email_send_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/email_send_template_template_response.py">EmailSendTemplateTemplateResponse</a></code>

## V1

Types:

```python
from unlayer.types.emails import (
    V1EmailsRetrieveResponse,
    V1RenderCreateResponse,
    V1SendCreateResponse,
    V1SendTemplateTemplateResponse,
)
```

Methods:

- <code title="get /emails/v1/emails/{id}">client.emails.v1.<a href="./src/unlayer/resources/emails/v1.py">emails_retrieve</a>(id) -> <a href="./src/unlayer/types/emails/v1_emails_retrieve_response.py">V1EmailsRetrieveResponse</a></code>
- <code title="post /emails/v1/render">client.emails.v1.<a href="./src/unlayer/resources/emails/v1.py">render_create</a>(\*\*<a href="src/unlayer/types/emails/v1_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/v1_render_create_response.py">V1RenderCreateResponse</a></code>
- <code title="post /emails/v1/send">client.emails.v1.<a href="./src/unlayer/resources/emails/v1.py">send_create</a>(\*\*<a href="src/unlayer/types/emails/v1_send_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/v1_send_create_response.py">V1SendCreateResponse</a></code>
- <code title="post /emails/v1/send/template">client.emails.v1.<a href="./src/unlayer/resources/emails/v1.py">send_template_template</a>(\*\*<a href="src/unlayer/types/emails/v1_send_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/emails/v1_send_template_template_response.py">V1SendTemplateTemplateResponse</a></code>

# Documents

Types:

```python
from unlayer.types import (
    DocumentDocumentsRetrieveResponse,
    DocumentGenerateCreateResponse,
    DocumentGenerateTemplateTemplateResponse,
)
```

Methods:

- <code title="get /documents/v1/documents/{id}">client.documents.<a href="./src/unlayer/resources/documents/documents.py">documents_retrieve</a>(id) -> <a href="./src/unlayer/types/document_documents_retrieve_response.py">DocumentDocumentsRetrieveResponse</a></code>
- <code title="post /documents/v1/generate">client.documents.<a href="./src/unlayer/resources/documents/documents.py">generate_create</a>(\*\*<a href="src/unlayer/types/document_generate_create_params.py">params</a>) -> <a href="./src/unlayer/types/document_generate_create_response.py">DocumentGenerateCreateResponse</a></code>
- <code title="post /documents/v1/generate/template">client.documents.<a href="./src/unlayer/resources/documents/documents.py">generate_template_template</a>(\*\*<a href="src/unlayer/types/document_generate_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/document_generate_template_template_response.py">DocumentGenerateTemplateTemplateResponse</a></code>

## V1

Types:

```python
from unlayer.types.documents import (
    V1DocumentsRetrieveResponse,
    V1GenerateCreateResponse,
    V1GenerateTemplateTemplateResponse,
)
```

Methods:

- <code title="get /documents/v1/documents/{id}">client.documents.v1.<a href="./src/unlayer/resources/documents/v1.py">documents_retrieve</a>(id) -> <a href="./src/unlayer/types/documents/v1_documents_retrieve_response.py">V1DocumentsRetrieveResponse</a></code>
- <code title="post /documents/v1/generate">client.documents.v1.<a href="./src/unlayer/resources/documents/v1.py">generate_create</a>(\*\*<a href="src/unlayer/types/documents/v1_generate_create_params.py">params</a>) -> <a href="./src/unlayer/types/documents/v1_generate_create_response.py">V1GenerateCreateResponse</a></code>
- <code title="post /documents/v1/generate/template">client.documents.v1.<a href="./src/unlayer/resources/documents/v1.py">generate_template_template</a>(\*\*<a href="src/unlayer/types/documents/v1_generate_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/documents/v1_generate_template_template_response.py">V1GenerateTemplateTemplateResponse</a></code>

# Pages

Types:

```python
from unlayer.types import PageRenderCreateResponse
```

Methods:

- <code title="post /pages/v1/render">client.pages.<a href="./src/unlayer/resources/pages/pages.py">render_create</a>(\*\*<a href="src/unlayer/types/page_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/page_render_create_response.py">PageRenderCreateResponse</a></code>

## V1

Types:

```python
from unlayer.types.pages import V1RenderCreateResponse
```

Methods:

- <code title="post /pages/v1/render">client.pages.v1.<a href="./src/unlayer/resources/pages/v1.py">render_create</a>(\*\*<a href="src/unlayer/types/pages/v1_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/pages/v1_render_create_response.py">V1RenderCreateResponse</a></code>
