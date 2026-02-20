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

# Projects

Types:

```python
from unlayer.types import ProjectRetrieveResponse
```

Methods:

- <code title="get /v3/projects/{id}">client.projects.<a href="./src/unlayer/resources/projects.py">retrieve</a>(id) -> <a href="./src/unlayer/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>

# Templates

Types:

```python
from unlayer.types import TemplateRetrieveResponse, TemplateListResponse
```

Methods:

- <code title="get /v3/templates/{id}">client.templates.<a href="./src/unlayer/resources/templates.py">retrieve</a>(id, \*\*<a href="src/unlayer/types/template_retrieve_params.py">params</a>) -> <a href="./src/unlayer/types/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="get /v3/templates">client.templates.<a href="./src/unlayer/resources/templates.py">list</a>(\*\*<a href="src/unlayer/types/template_list_params.py">params</a>) -> <a href="./src/unlayer/types/template_list_response.py">SyncCursorPage[TemplateListResponse]</a></code>

# Workspaces

Types:

```python
from unlayer.types import WorkspaceRetrieveResponse, WorkspaceListResponse
```

Methods:

- <code title="get /v3/workspaces/{workspaceId}">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">retrieve</a>(workspace_id) -> <a href="./src/unlayer/types/workspace_retrieve_response.py">WorkspaceRetrieveResponse</a></code>
- <code title="get /v3/workspaces">client.workspaces.<a href="./src/unlayer/resources/workspaces.py">list</a>() -> <a href="./src/unlayer/types/workspace_list_response.py">WorkspaceListResponse</a></code>
