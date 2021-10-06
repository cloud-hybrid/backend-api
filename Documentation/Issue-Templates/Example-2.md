## Table of Contents ##

[[_TOC_]]

## Tasks ##

### File Structure ###

- [ ] Create a `Mongo.Collections.Hook` Package
    - [ ] `/Mongo/Collections/Hooks` Directory
    - [ ] `/Mongo/Collections/Hooks/__init__.py` File
    - [ ] `/Mongo/Collections/Hooks/CRUD.py` File
- [ ] Create a `Mongo.Interfaces.Hook` Module
    - [ ] `/Mongo/Interfaces/Hook.py` File
- [ ] Create a `Mongo.Schemas.Hook` Module
    - [ ] `/Mongo/Schemas/Hook.py` File
    
## Schema + API ##

| Property | Type | Description |
|:---|:---|:---|
| `ID` | Hash | The Unique ID of the Web-Hook |
| `Type` | `Integer` (Positive) | The Webhook-Enumeration-Key-Value (`class WH(Enumeration, Integer).[Value]`) |
| `User` | `Optional[Nexus.User.ID]` | The Creator of the Document Entry/Web-Hook |
| `Name` | `Optional[String]` | Default Web-Hook Name |
| `Avatar` | `Optional[Upload[Image]]` | Default User-Avator Image Type w/URL |
| `Token` | `Optional[Union[String, Secret]]` | The **Secure Token** of the Web-Hook (Returned for Incoming Web-Hooks) |
| `Authentication` | Hash | Application-ID Unique Identifier |
| `URL` | `String` | The URL used for Executing the Webhook (Returned by OAuth Flow) |

## Traceback(s) ##

<Details>
    <Summary>
        <Strong>
            Error Traceback
        </Strong>
    </Summary>

```log
(most recent call last):
  File "/Application/.venv/lib/python3.9/site-packages/starlette/middleware/errors.py", line 159, in __call__
    await self.app(scope, receive, _send)
  File "/Application/.venv/lib/python3.9/site-packages/API/ASGI/Extensions.py", line 279, in __call__
    raise Error from None
  File "/Application/.venv/lib/python3.9/site-packages/API/ASGI/Extensions.py", line 277, in __call__
    await self.app(scope, inner_receive, inner_send)
  File "/Application/.venv/lib/python3.9/site-packages/API/ASGI/Extensions.py", line 213, in __call__
    await responder(scope, receive, send)
  File "/Application/.venv/lib/python3.9/site-packages/API/ASGI/Extensions.py", line 139, in __call__
    await self.app(scope, receive, self.send_with_gzip)
  File "/Application/.venv/lib/python3.9/site-packages/starlette/middleware/cors.py", line 78, in __call__
    await self.app(scope, receive, send)
  File "/Application/.venv/lib/python3.9/site-packages/starlette/exceptions.py", line 82, in __call__
    raise exc from None
  File "/Application/.venv/lib/python3.9/site-packages/starlette/exceptions.py", line 71, in __call__
    await self.app(scope, receive, sender)
  File "/Application/.venv/lib/python3.9/site-packages/starlette/routing.py", line 580, in __call__
    await route.handle(scope, receive, send)
  File "/Application/.venv/lib/python3.9/site-packages/starlette/routing.py", line 241, in handle
    await self.app(scope, receive, send)
  File "/Application/.venv/lib/python3.9/site-packages/starlette/routing.py", line 52, in app
    response = await func(request)
  File "/Application/.venv/lib/python3.9/site-packages/fastapi/routing.py", line 222, in app
    response_data = await serialize_response(
  File "/Application/.venv/lib/python3.9/site-packages/fastapi/routing.py", line 127, in serialize_response
    raise ValidationError(errors, field.type_)
pydantic.error_wrappers.ValidationError: 1 validation error for Schema
response
  value is not a valid list (type=type_error.list)
```

</Details>

### Reproduction ###

*The Steps Required to Reproduce the **Traceback, Error, or otherwise Unexpected
Behavior.***

1. ...
1. ...
1. ...

## Jira Description Template ##

```
{panel:bgColor=#fafafa}
User: [Jacob Sanders|~accountid:60a8993920ad1b0070b360df]
Repository: [Example|https://github.com]
Documentation: [Technical Guide|https://github.com]
{panel}

h1. \[Heading-1]

h2. \[Heading-2]

h3. \[Heading-3]

{code:none}[Code-Snippet-Example]{code}

{quote}\[Quote-Snippet-Example]{quote}

[\[Example-Link]|https://gitlab.cloud-technology.io/Nexus]

* Example Bullet 1
* Example Bullet 2

{{[Inline-Code-Example]}}

*\[Bold-Text-Example]*

_\[Emphasis-Text-Example]_
```
