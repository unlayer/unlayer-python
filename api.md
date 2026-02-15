# Convert

## FullToSimple

Types:

```python
from unlayer.types.convert import FullToSimpleCreateResponse
```

Methods:

- <code title="post /convert/full-to-simple">client.convert.full_to_simple.<a href="./src/unlayer/resources/convert/full_to_simple.py">create</a>(\*\*<a href="src/unlayer/types/convert/full_to_simple_create_params.py">params</a>) -> <a href="./src/unlayer/types/convert/full_to_simple_create_response.py">FullToSimpleCreateResponse</a></code>

## SimpleToFull

Types:

```python
from unlayer.types.convert import SimpleToFullCreateResponse
```

Methods:

- <code title="post /convert/simple-to-full">client.convert.simple_to_full.<a href="./src/unlayer/resources/convert/simple_to_full.py">create</a>(\*\*<a href="src/unlayer/types/convert/simple_to_full_create_params.py">params</a>) -> <a href="./src/unlayer/types/convert/simple_to_full_create_response.py">SimpleToFullCreateResponse</a></code>

# Documents

Types:

```python
from unlayer.types import DocumentRetrieveResponse
```

Methods:

- <code title="get /documents/v1/documents/{id}">client.documents.<a href="./src/unlayer/resources/documents/documents.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/document_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/document_retrieve_response.py">DocumentRetrieveResponse</a></code>

## Generate

Types:

```python
from unlayer.types.documents import GenerateCreateResponse
```

Methods:

- <code title="post /documents/v1/generate">client.documents.generate.<a href="./src/unlayer/resources/documents/generate.py">create</a>(\*\*<a href="src/unlayer/types/documents/generate_create_params.py">params</a>) -> <a href="./src/unlayer/types/documents/generate_create_response.py">GenerateCreateResponse</a></code>

## GenerateTemplate

Types:

```python
from unlayer.types.documents import GenerateTemplateCreateResponse
```

Methods:

- <code title="post /documents/v1/generate/template">client.documents.generate_template.<a href="./src/unlayer/resources/documents/generate_template.py">create</a>(\*\*<a href="src/unlayer/types/documents/generate_template_create_params.py">params</a>) -> <a href="./src/unlayer/types/documents/generate_template_create_response.py">GenerateTemplateCreateResponse</a></code>

# Emails

Types:

```python
from unlayer.types import EmailRetrieveResponse
```

Methods:

- <code title="get /emails/v1/emails/{id}">client.emails.<a href="./src/unlayer/resources/emails/emails.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/email_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>

## Render

Types:

```python
from unlayer.types.emails import RenderCreateResponse
```

Methods:

- <code title="post /emails/v1/render">client.emails.render.<a href="./src/unlayer/resources/emails/render.py">create</a>(\*\*<a href="src/unlayer/types/emails/render_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/render_create_response.py">RenderCreateResponse</a></code>

## Send

Types:

```python
from unlayer.types.emails import SendCreateResponse
```

Methods:

- <code title="post /emails/v1/send">client.emails.send.<a href="./src/unlayer/resources/emails/send.py">create</a>(\*\*<a href="src/unlayer/types/emails/send_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/send_create_response.py">SendCreateResponse</a></code>

## SendTemplate

Types:

```python
from unlayer.types.emails import SendTemplateCreateResponse
```

Methods:

- <code title="post /emails/v1/send/template">client.emails.send_template.<a href="./src/unlayer/resources/emails/send_template.py">create</a>(\*\*<a href="src/unlayer/types/emails/send_template_create_params.py">params</a>) -> <a href="./src/unlayer/types/emails/send_template_create_response.py">SendTemplateCreateResponse</a></code>

# Export

## HTML

Types:

```python
from unlayer.types.export import HTMLRetrieveResponse
```

Methods:

- <code title="get /export/v3/html">client.export.html.<a href="./src/unlayer/resources/export/html.py">retrieve</a>(\*\*<a href="src/unlayer/types/export/html_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/export/html_retrieve_response.py">HTMLRetrieveResponse</a></code>

## Image

Types:

```python
from unlayer.types.export import ImageRetrieveResponse
```

Methods:

- <code title="get /export/v3/image">client.export.image.<a href="./src/unlayer/resources/export/image.py">retrieve</a>(\*\*<a href="src/unlayer/types/export/image_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/export/image_retrieve_response.py">ImageRetrieveResponse</a></code>

## Pdf

Types:

```python
from unlayer.types.export import PdfRetrieveResponse
```

Methods:

- <code title="get /export/v3/pdf">client.export.pdf.<a href="./src/unlayer/resources/export/pdf.py">retrieve</a>(\*\*<a href="src/unlayer/types/export/pdf_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/export/pdf_retrieve_response.py">PdfRetrieveResponse</a></code>

## Zip

Types:

```python
from unlayer.types.export import ZipRetrieveResponse
```

Methods:

- <code title="get /export/v3/zip">client.export.zip.<a href="./src/unlayer/resources/export/zip.py">retrieve</a>(\*\*<a href="src/unlayer/types/export/zip_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/export/zip_retrieve_response.py">ZipRetrieveResponse</a></code>

# Pages

## Render

Types:

```python
from unlayer.types.pages import RenderCreateResponse
```

Methods:

- <code title="post /pages/v1/render">client.pages.render.<a href="./src/unlayer/resources/pages/render.py">create</a>(\*\*<a href="src/unlayer/types/pages/render_create_params.py">params</a>) -> <a href="./src/unlayer/types/pages/render_create_response.py">RenderCreateResponse</a></code>

# Project

## Current

Types:

```python
from unlayer.types.project import CurrentRetrieveResponse
```

Methods:

- <code title="get /project/v1/current">client.project.current.<a href="./src/unlayer/resources/project/current.py">retrieve</a>(\*\*<a href="src/unlayer/types/project/current_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/project/current_retrieve_response.py">CurrentRetrieveResponse</a></code>

## Domains

Types:

```python
from unlayer.types.project import (
    DomainCreateResponse,
    DomainRetrieveResponse,
    DomainUpdateResponse,
    DomainListResponse,
)
```

Methods:

- <code title="post /project/v1/domains">client.project.domains.<a href="./src/unlayer/resources/project/domains.py">create</a>(\*\*<a href="src/unlayer/types/project/domain_create_params.py">params</a>) -> <a href="./src/unlayer/types/project/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /project/v1/domains/{id}">client.project.domains.<a href="./src/unlayer/resources/project/domains.py">retrieve</a>(id) -> <a href="./src/unlayer/types/project/domain_retrieve_response.py">DomainRetrieveResponse</a></code>
- <code title="put /project/v1/domains/{id}">client.project.domains.<a href="./src/unlayer/resources/project/domains.py">update</a>(id, \*\*<a href="src/unlayer/types/project/domain_update_params.py">params</a>) -> <a href="./src/unlayer/types/project/domain_update_response.py">DomainUpdateResponse</a></code>
- <code title="get /project/v1/domains">client.project.domains.<a href="./src/unlayer/resources/project/domains.py">list</a>(\*\*<a href="src/unlayer/types/project/domain_list_params.py">params</a>) -> <a href="./src/unlayer/types/project/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /project/v1/domains/{id}">client.project.domains.<a href="./src/unlayer/resources/project/domains.py">delete</a>(id) -> None</code>

## Templates

Types:

```python
from unlayer.types.project import (
    TemplateCreateResponse,
    TemplateRetrieveResponse,
    TemplateUpdateResponse,
    TemplateListResponse,
)
```

Methods:

- <code title="post /project/v1/templates">client.project.templates.<a href="./src/unlayer/resources/project/templates.py">create</a>(\*\*<a href="src/unlayer/types/project/template_create_params.py">params</a>) -> <a href="./src/unlayer/types/project/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /project/v1/templates/{id}">client.project.templates.<a href="./src/unlayer/resources/project/templates.py">retrieve</a>(id) -> <a href="./src/unlayer/types/project/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="put /project/v1/templates/{id}">client.project.templates.<a href="./src/unlayer/resources/project/templates.py">update</a>(id, \*\*<a href="src/unlayer/types/project/template_update_params.py">params</a>) -> <a href="./src/unlayer/types/project/template_update_response.py">TemplateUpdateResponse</a></code>
- <code title="get /project/v1/templates">client.project.templates.<a href="./src/unlayer/resources/project/templates.py">list</a>(\*\*<a href="src/unlayer/types/project/template_list_params.py">params</a>) -> <a href="./src/unlayer/types/project/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /project/v1/templates/{id}">client.project.templates.<a href="./src/unlayer/resources/project/templates.py">delete</a>(id) -> None</code>

## Workspaces

Types:

```python
from unlayer.types.project import WorkspaceRetrieveResponse, WorkspaceListResponse
```

Methods:

- <code title="get /project/v1/workspaces/{workspaceId}">client.project.workspaces.<a href="./src/unlayer/resources/project/workspaces.py">retrieve</a>(workspace_id) -> <a href="./src/unlayer/types/project/workspace_retrieve_response.py">WorkspaceRetrieveResponse</a></code>
- <code title="get /project/v1/workspaces">client.project.workspaces.<a href="./src/unlayer/resources/project/workspaces.py">list</a>() -> <a href="./src/unlayer/types/project/workspace_list_response.py">WorkspaceListResponse</a></code>
