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

- <code title="get /documents/v1/documents/{id}">client.documents.<a href="./src/unlayer/resources/documents.py">documents_retrieve</a>(id, \*\*<a href="src/unlayer/types/document_documents_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/document_documents_retrieve_response.py">DocumentDocumentsRetrieveResponse</a></code>
- <code title="post /documents/v1/generate">client.documents.<a href="./src/unlayer/resources/documents.py">generate_create</a>(\*\*<a href="src/unlayer/types/document_generate_create_params.py">params</a>) -> <a href="./src/unlayer/types/document_generate_create_response.py">DocumentGenerateCreateResponse</a></code>
- <code title="post /documents/v1/generate/template">client.documents.<a href="./src/unlayer/resources/documents.py">generate_template_template</a>(\*\*<a href="src/unlayer/types/document_generate_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/document_generate_template_template_response.py">DocumentGenerateTemplateTemplateResponse</a></code>

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

- <code title="get /emails/v1/emails/{id}">client.emails.<a href="./src/unlayer/resources/emails.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/email_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="post /emails/v1/render">client.emails.<a href="./src/unlayer/resources/emails.py">render_create</a>(\*\*<a href="src/unlayer/types/email_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/email_render_create_response.py">EmailRenderCreateResponse</a></code>
- <code title="post /emails/v1/send">client.emails.<a href="./src/unlayer/resources/emails.py">send_create</a>(\*\*<a href="src/unlayer/types/email_send_create_params.py">params</a>) -> <a href="./src/unlayer/types/email_send_create_response.py">EmailSendCreateResponse</a></code>
- <code title="post /emails/v1/send/template">client.emails.<a href="./src/unlayer/resources/emails.py">send_template_template</a>(\*\*<a href="src/unlayer/types/email_send_template_template_params.py">params</a>) -> <a href="./src/unlayer/types/email_send_template_template_response.py">EmailSendTemplateTemplateResponse</a></code>

# Export

Types:

```python
from unlayer.types import (
    ExportHTMLListResponse,
    ExportImageListResponse,
    ExportPdfListResponse,
    ExportZipListResponse,
)
```

Methods:

- <code title="get /export/v3/html">client.export.<a href="./src/unlayer/resources/export.py">html_list</a>(\*\*<a href="src/unlayer/types/export_html_list_params.py">params</a>) -> <a href="./src/unlayer/types/export_html_list_response.py">ExportHTMLListResponse</a></code>
- <code title="get /export/v3/image">client.export.<a href="./src/unlayer/resources/export.py">image_list</a>(\*\*<a href="src/unlayer/types/export_image_list_params.py">params</a>) -> <a href="./src/unlayer/types/export_image_list_response.py">ExportImageListResponse</a></code>
- <code title="get /export/v3/pdf">client.export.<a href="./src/unlayer/resources/export.py">pdf_list</a>(\*\*<a href="src/unlayer/types/export_pdf_list_params.py">params</a>) -> <a href="./src/unlayer/types/export_pdf_list_response.py">ExportPdfListResponse</a></code>
- <code title="get /export/v3/zip">client.export.<a href="./src/unlayer/resources/export.py">zip_list</a>(\*\*<a href="src/unlayer/types/export_zip_list_params.py">params</a>) -> <a href="./src/unlayer/types/export_zip_list_response.py">ExportZipListResponse</a></code>

# Pages

Types:

```python
from unlayer.types import PageRenderCreateResponse
```

Methods:

- <code title="post /pages/v1/render">client.pages.<a href="./src/unlayer/resources/pages.py">render_create</a>(\*\*<a href="src/unlayer/types/page_render_create_params.py">params</a>) -> <a href="./src/unlayer/types/page_render_create_response.py">PageRenderCreateResponse</a></code>

# Project

Types:

```python
from unlayer.types import (
    ProjectCurrentListResponse,
    ProjectDomainsCreateResponse,
    ProjectDomainsListResponse,
    ProjectDomainsRetrieveResponse,
    ProjectDomainsUpdateResponse,
    ProjectTemplatesCreateResponse,
    ProjectTemplatesListResponse,
    ProjectTemplatesRetrieveResponse,
    ProjectTemplatesUpdateResponse,
    ProjectWorkspacesListResponse,
    ProjectWorkspacesRetrieveResponse,
)
```

Methods:

- <code title="get /project/v1/current">client.project.<a href="./src/unlayer/resources/project.py">current_list</a>(\*\*<a href="src/unlayer/types/project_current_list_params.py">params</a>) -> <a href="./src/unlayer/types/project_current_list_response.py">ProjectCurrentListResponse</a></code>
- <code title="post /project/v1/domains">client.project.<a href="./src/unlayer/resources/project.py">domains_create</a>(\*\*<a href="src/unlayer/types/project_domains_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_domains_create_response.py">ProjectDomainsCreateResponse</a></code>
- <code title="delete /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project.py">domains_delete</a>(id) -> None</code>
- <code title="get /project/v1/domains">client.project.<a href="./src/unlayer/resources/project.py">domains_list</a>(\*\*<a href="src/unlayer/types/project_domains_list_params.py">params</a>) -> <a href="./src/unlayer/types/project_domains_list_response.py">ProjectDomainsListResponse</a></code>
- <code title="get /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project.py">domains_retrieve</a>(id) -> <a href="./src/unlayer/types/project_domains_retrieve_response.py">ProjectDomainsRetrieveResponse</a></code>
- <code title="put /project/v1/domains/{id}">client.project.<a href="./src/unlayer/resources/project.py">domains_update</a>(id, \*\*<a href="src/unlayer/types/project_domains_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_domains_update_response.py">ProjectDomainsUpdateResponse</a></code>
- <code title="post /project/v1/templates">client.project.<a href="./src/unlayer/resources/project.py">templates_create</a>(\*\*<a href="src/unlayer/types/project_templates_create_params.py">params</a>) -> <a href="./src/unlayer/types/project_templates_create_response.py">ProjectTemplatesCreateResponse</a></code>
- <code title="delete /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project.py">templates_delete</a>(id) -> None</code>
- <code title="get /project/v1/templates">client.project.<a href="./src/unlayer/resources/project.py">templates_list</a>(\*\*<a href="src/unlayer/types/project_templates_list_params.py">params</a>) -> <a href="./src/unlayer/types/project_templates_list_response.py">SyncCursorPage[ProjectTemplatesListResponse]</a></code>
- <code title="get /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project.py">templates_retrieve</a>(id) -> <a href="./src/unlayer/types/project_templates_retrieve_response.py">ProjectTemplatesRetrieveResponse</a></code>
- <code title="put /project/v1/templates/{id}">client.project.<a href="./src/unlayer/resources/project.py">templates_update</a>(id, \*\*<a href="src/unlayer/types/project_templates_update_params.py">params</a>) -> <a href="./src/unlayer/types/project_templates_update_response.py">ProjectTemplatesUpdateResponse</a></code>
- <code title="get /project/v1/workspaces">client.project.<a href="./src/unlayer/resources/project.py">workspaces_list</a>() -> <a href="./src/unlayer/types/project_workspaces_list_response.py">ProjectWorkspacesListResponse</a></code>
- <code title="get /project/v1/workspaces/{workspaceId}">client.project.<a href="./src/unlayer/resources/project.py">workspaces_retrieve</a>(workspace_id) -> <a href="./src/unlayer/types/project_workspaces_retrieve_response.py">ProjectWorkspacesRetrieveResponse</a></code>
