# Convert

## FullToSimple

Types:

```python
from unlayer.types.convert import FullToSimpleCreateResponse
```

Methods:

- <code title="post /v3/convert/full-to-simple">client.convert.full_to_simple.<a href="./src/unlayer/resources/convert/full_to_simple.py">create</a>(\*\*<a href="src/unlayer/types/convert/full_to_simple_create_params.py">params</a>) -> <a href="./src/unlayer/types/convert/full_to_simple_create_response.py">FullToSimpleCreateResponse</a></code>

## SimpleToFull

Types:

```python
from unlayer.types.convert import SimpleToFullCreateResponse
```

Methods:

- <code title="post /v3/convert/simple-to-full">client.convert.simple_to_full.<a href="./src/unlayer/resources/convert/simple_to_full.py">create</a>(\*\*<a href="src/unlayer/types/convert/simple_to_full_create_params.py">params</a>) -> <a href="./src/unlayer/types/convert/simple_to_full_create_response.py">SimpleToFullCreateResponse</a></code>

# Project

Types:

```python
from unlayer.types import ProjectRetrieveResponse
```

Methods:

- <code title="get /v3/project">client.project.<a href="./src/unlayer/resources/project/project.py">retrieve</a>(\*\*<a href="src/unlayer/types/project_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

## Templates

Types:

```python
from unlayer.types.project import TemplateRetrieveResponse, TemplateListResponse
```

Methods:

- <code title="get /v3/project/templates/{id}">client.project.templates.<a href="./src/unlayer/resources/project/templates.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/project/template_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/project/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="get /v3/project/templates">client.project.templates.<a href="./src/unlayer/resources/project/templates.py">list</a>(\*\*<a href="src/unlayer/types/project/template_list_params.py">params</a>) -> <a href="./src/unlayer/types/project/template_list_response.py">SyncCursorPage[TemplateListResponse]</a></code>

# Workspaces

Types:

```python
from unlayer.types import WorkspaceRetrieveResponse, WorkspaceListResponse
```

Methods:

- <code title="get /v3/workspaces/{workspaceId}">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">retrieve</a>(workspace_id) -> <a href="./src/unlayer/types/workspace_retrieve_response.py">WorkspaceRetrieveResponse</a></code>
- <code title="get /v3/workspaces">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">list</a>() -> <a href="./src/unlayer/types/workspace_list_response.py">WorkspaceListResponse</a></code>
