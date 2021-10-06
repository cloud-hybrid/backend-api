"""
HTTP Methods

DELETE, GET, HEAD, POST, PUT, CONNECT, OPTIONS, TRACE, COPY,
        LOCK, MKCOL, MOVE, PROPFIND, PROPPATCH, SEARCH, UNLOCK, BIND,
        REBIND, UNBIND, ACL, REPORT, MKACTIVITY, CHECKOUT, MERGE,
        MSEARCH, NOTIFY, SUBSCRIBE, UNSUBSCRIBE, PATCH, PURGE, MKCALENDAR,
        LINK, UNLINK
URL Schema UF_SCHEMA   = 0,
        UF_HOST     = 1,
        UF_PORT     = 2,
        UF_PATH     = 3,
        UF_QUERY    = 4,
        UF_FRAGMENT = 5,
        UF_USERINFO = 6,
        UF_MAX      = 7
        git clone --recursive git@github.com:MagicStack/httptools.git
"""

import dataclasses

HTTP_STATUS_CODES = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "Switch Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request URI Too Long",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    449: "Retry With",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Failed",
}

@dataclasses.dataclass(frozen = True, order = False, unsafe_hash = False)
class Success:
    """
    Successful HTTP Responses

    Properties::
        Success.Ok (int): The request has succeeded. The meaning of the success depends
            on the HTTP method.
            - GET: The resource has been fetched and is transmitted in the message body.
            - HEAD: The entity headers are in the message body.
            - PUT or POST: The resource describing the result of the action is transmitted
              in the message body.
            - TRACE: The message body contains the request message as received by the server.
        Success.Created (int): Created
            The request has succeeded and a new resource has been created as a result.
            This is typically the response sent after POST requests, or some PUT requests.
        Success.Accepted (int): Accepted
            The request has been received but not yet acted upon. It is noncommittal,
            since there is no way in HTTP to later send an asynchronous response indicating
            the outcome of the request. It is intended for cases where another process or
            server handles the request, or for batch processing.
        Success.Information (int): Non-Authoritative Information
            This response code means the returned meta-information is not exactly the same
            as is available from the origin server, but is collected from a local or a
            third-party copy. This is mostly used for mirrors or backups of another resource.
            Except for that specific case, the "200 OK" response is preferred to this status.
        Success.Empty (int): No Content
            There is no content to send for this request, but the headers may be useful. The
            user-agent may update its cached headers for this resource with the new ones.
        Success.Reset (int): Reset Content
            Tells the user-agent to reset the document which sent this request.
        Success.Partial (int): Partial Content
            This response code is used when the Range header is sent from the client to request
            only part of a resource.
        Success.Multi (int): Multi-Status (WebDAV)
            Conveys information about multiple resources, for situations where multiple status
             codes might be appropriate.
        Success.Enumerated (int): Already Reported (WebDAV)
            Used inside a <dav:propstat> response element to avoid repeatedly enumerating the
            internal members of multiple bindings to the same collection.
        Success.Issued (int): IM Used (HTTP Delta encoding)
            The server has fulfilled a GET request for the resource, and the response is a
            representation of the result of one or more instance-manipulations applied to
            the current instance.
    """

    Ok: int = 200
    Created: int = 201
    Accepted: int = 202
    Information: int = 203
    Empty: int = 204
    Reset: int = 204
    Partial: int = 206
    Multi: int = 207
    Enumerated: int = 208
    Issued: int = 226

Types = {
    200:
        {
            "description": "Successful Request Resolution"
        },
    # ... 201:
    # ...     {
    # ...         "description": "Created - Request has Successfully Provisioned a New Resource"
    # ...     },
    # ... 202:
    # ...     {
    # ...         "description": "Accepted & Processing - Request has been Queued but Cannot be Awaited"
    # ...     },
    # ... 204:
    # ...     {
    # ...         "description": "Successful Query - Response has been Cached"
    # ...     },
    # ... 205:
    # ...     {
    # ...         "description": "Request Initiated - Client is Requested for a DOM Reset"
    # ...     },
    # ... 400:
    # ...     {
    # ...         "description": "Malformed Request - Client Modification(s) Required"
    # ...     },
    401:
        {
            "description": "Access Conditionally Denied - Client Authentication Required"
        },
    # ... 403:
    # ...     {
    # ...         "description": "Access Denied - Insufficient Application Permission(s)"
    # ...     },
    # ... 404:
    # ...     {
    # ...         "description": "Resource Not Found - Requested Target Resource is Temporarily or Permanently Missing"
    # ...     },
    # ... 405:
    # ...     {
    # ...         "description": "Unsupported Request Method - Target Resource URI is Denied"
    # ...     },
    # ... 409:
    # ...     {
    # ...         "description": "Write Conflict - Source State Conflict with Requested Target Resource"
    # ...     },
    # ... 415:
    # ...     {
    # ...         "description": "Unsupported Media Type - Content Encoding || Type Refused by Server"
    # ...     },
    422:
        {
            "description": "Unprocessable Entity - Content Encoding && Type Accepted, Malformed Client Data"
        }
}
