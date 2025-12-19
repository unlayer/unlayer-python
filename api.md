# Emails

Types:

```python
from unlayer.types import (
    EmailRetrieveResponse,
    EmailRenderCreateResponse,
    EmailSendCreateResponse,
    EmailSendTemplateTemplateResponse,
)
```

Methods:

- <code title="get /emails/v1/emails/{id}">client.emails.<a href="./src/unlayer/resources/emails.py">retrieve</a>(id) -> <a href="./src/unlayer/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="post /emails/v1/render">client.emails.<a href="./src/unlayer/resources/emails.py">render_create</a>(\*\*<a href="src/unlayer/types/email_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/email_render_create_response.py">EmailRenderCreateResponse</a></code>
- <code title="post /emails/v1/send">client.emails.<a href="./src/unlayer/resources/emails.py">send_create</a>(\*\*<a href="src/unlayer/types/email_send_create_params.py">params</a>) -> <a href="./src/unlayer/types/email_send_create_response.py">EmailSendCreateResponse</a></code>
- <code title="post /emails/v1/send/template">client.emails.<a href="./src/unlayer/resources/emails.py">send_template_template</a>(\*\*<a href="src/unlayer/types/email_send_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/email_send_template_template_response.py">EmailSendTemplateTemplateResponse</a></code>

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

- <code title="post /project/v1/api-keys">client.project.<a href="./src/unlayer/resources/project.py">api_keys_create</a>(\*\*<a href="src/unlayer/types/project_api_keys_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_api_keys_create_response.py">ProjectAPIKeysCreateResponse</a></code>
- <code title="delete /project/v1/api-keys/{id}">client.project.<a href="./src/unlayer/resources/project.py">api_keys_delete</a>(id) -> None</code>
- <code title="get /project/v1/api-keys">client.project.<a href="./src/unlayer/resources/project.py">api_keys_list</a>() -> <a href="./src/unlayer/types/project_api_keys_list_response.py">ProjectAPIKeysListResponse</a></code>
- <code title="get /project/v1/api-keys/{id}">client.project.<a href="./src/unlayer/resources/project.py">api_keys_retrieve</a>(id) -> <a href="./src/unlayer/types/project_api_keys_retrieve_response.py">ProjectAPIKeysRetrieveResponse</a></code>
- <code title="put /project/v1/api-keys/{id}">client.project.<a href="./src/unlayer/resources/project.py">api_keys_update</a>(id, \*\*<a href="src/unlayer/types/project_api_keys_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_api_keys_update_response.py">ProjectAPIKeysUpdateResponse</a></code>
- <code title="get /project/v1/current">client.project.<a href="./src/unlayer/resources/project.py">current_list</a>() -> <a href="./src/unlayer/types/project_current_list_response.py">ProjectCurrentListResponse</a></code>
- <code title="post /project/v1/domains">client.project.<a href="./src/unlayer/resources/project.py">domains_create</a>(\*\*<a href="src/unlayer/types/project_domains_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_domains_create_response.py">ProjectDomainsCreateResponse</a></code>
- <code title="delete /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project.py">domains_delete</a>(id) -> None</code>
- <code title="get /project/v1/domains">client.project.<a href="./src/unlayer/resources/project.py">domains_list</a>() -> <a href="./src/unlayer/types/project_domains_list_response.py">ProjectDomainsListResponse</a></code>
- <code title="get /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project.py">domains_retrieve</a>(id) -> <a href="./src/unlayer/types/project_domains_retrieve_response.py">ProjectDomainsRetrieveResponse</a></code>
- <code title="put /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project.py">domains_update</a>(id, \*\*<a href="src/unlayer/types/project_domains_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_domains_update_response.py">ProjectDomainsUpdateResponse</a></code>
- <code title="post /project/v1/templates">client.project.<a href="./src/unlayer/resources/project.py">templates_create</a>(\*\*<a href="src/unlayer/types/project_templates_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_templates_create_response.py">ProjectTemplatesCreateResponse</a></code>
- <code title="delete /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project.py">templates_delete</a>(id) -> None</code>
- <code title="get /project/v1/templates">client.project.<a href="./src/unlayer/resources/project.py">templates_list</a>() -> <a href="./src/unlayer/types/project_templates_list_response.py">ProjectTemplatesListResponse</a></code>
- <code title="get /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project.py">templates_retrieve</a>(id) -> <a href="./src/unlayer/types/project_templates_retrieve_response.py">ProjectTemplatesRetrieveResponse</a></code>
- <code title="put /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project.py">templates_update</a>(id, \*\*<a href="src/unlayer/types/project_templates_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_templates_update_response.py">ProjectTemplatesUpdateResponse</a></code>

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

- <code title="get /documents/v1/documents/{id}">client.documents.<a href="./src/unlayer/resources/documents.py">documents_retrieve</a>(id) -> <a href="./src/unlayer/types/document_documents_retrieve_response.py">DocumentDocumentsRetrieveResponse</a></code>
- <code title="post /documents/v1/generate">client.documents.<a href="./src/unlayer/resources/documents.py">generate_create</a>(\*\*<a href="src/unlayer/types/document_generate_create_params.py">params</a>) -> <a href="./src/unlayer/types/document_generate_create_response.py">DocumentGenerateCreateResponse</a></code>
- <code title="post /documents/v1/generate/template">client.documents.<a href="./src/unlayer/resources/documents.py">generate_template_template</a>(\*\*<a href="src/unlayer/types/document_generate_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/document_generate_template_template_response.py">DocumentGenerateTemplateTemplateResponse</a></code>

# Pages

Types:

```python
from unlayer.types import PageRenderCreateResponse
```

Methods:

- <code title="post /pages/v1/render">client.pages.<a href="./src/unlayer/resources/pages.py">render_create</a>(\*\*<a href="src/unlayer/types/page_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/page_render_create_response.py">PageRenderCreateResponse</a></code>
