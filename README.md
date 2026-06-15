# VAT Examples

Example scripts for accessing the Berlin United Visual Analytics Tool (VAT) through the vaapi Python client.

Running the demos requires a instance of the Visual Analytics Tool running. 

## Setup
You need to the environment variables for the URL and the API token. 

```
export VAT_API_URL=<http://127.0.0.1:8000/ or https://vat.berlin-united.com/>
export VAT_API_TOKEN=<your token>
```

If you are using vat.berlin-united.com you should have received a token from the admin. If you are using the self hosted version you can get the token by login to the django admin panel. 

## API Reference

An interactive reference for all available API endpoints is available at:

https://vat.berlin-united.com/api/

The reference lists the supported operations for each endpoint, including available query parameters, request formats, and response schemas.

## Demos for the Berlin United Visual Analytics Tool

### Creating a Client

All examples initialize the client in the same way:

```
import os
from vaapi.client import Vaapi

client = Vaapi(
    base_url=os.environ.get("VAT_API_URL"),
    api_key=os.environ.get("VAT_API_TOKEN"),
)
```

### Querying the API

For example, the get_teams.py example queries the team endpoint using client.team.list():

```
my_list = client.team.list()
if my_list:
    print(my_list)
```

The list() methods return iterable generators. Results are fetched as they are requested rather than loading the complete dataset into memory:


Each returned item is a Python model object whose fields can be accessed directly, such as team.id, team.team_id, and team.name.

```
d = {team.id: team.name for team in my_list}
print()
print(d)
```

Some VAT endpoints contain millions of entries. When querying frame-level data such as images or team states, always filter by log ID, for example:

```
for team_state in client.teamstate.list(log=1):
    print(team_state)
```

