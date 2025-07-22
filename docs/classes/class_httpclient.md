github_url
:   hide

# HTTPClient {#class_HTTPClient}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Low-level hyper-text transfer protocol client.

::: rst-class
classref-introduction-group
:::

## Description

Hyper-text transfer protocol client (sometimes called \"User Agent\").
Used to make HTTP requests to download web content, upload files and
other data or to communicate with various services, among other use
cases.

See the `HTTPRequest<class_HTTPRequest>`{.interpreted-text role="ref"}
node for a higher-level alternative.

\*\*Note:\*\* This client only needs to connect to a host once (see
`connect_to_host()<class_HTTPClient_method_connect_to_host>`{.interpreted-text
role="ref"}) to send multiple requests. Because of this, methods that
take URLs usually take just the part after the host instead of the full
URL, as the client is already connected to a host. See
`request()<class_HTTPClient_method_request>`{.interpreted-text
role="ref"} for a full example and to get started.

An **HTTPClient** should be reused between multiple requests or to
connect to different hosts instead of creating one client per request.
Supports Transport Layer Security (TLS), including server certificate
verification. HTTP status codes in the 2xx range indicate success, 3xx
redirection (i.e. \"try again, but over here\"), 4xx something was wrong
with the request, and 5xx something went wrong on the server\'s side.

For more information on HTTP, see [MDN\'s documentation on
HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) (or read [RFC
2616](https://tools.ietf.org/html/rfc2616) to get it straight from the
source).

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

\*\*Note:\*\* It\'s recommended to use transport encryption (TLS) and to
avoid sending sensitive information (such as login credentials) in HTTP
GET URL parameters. Consider using HTTP POST requests or HTTP headers
for such information instead.

\*\*Note:\*\* When performing HTTP requests from a project exported to
Web, keep in mind the remote server may not allow requests from foreign
origins due to
[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS). If you
host the server in question, you should modify its backend to allow
requests from foreign origins by adding the
`Access-Control-Allow-Origin: *` HTTP header.

\*\*Note:\*\* TLS support is currently limited to TLSv1.2 and TLSv1.3.
Attempting to connect to a server that only supports older (insecure)
TLS versions will return an error.

\*\*Warning:\*\* TLS certificate revocation and certificate pinning are
currently not supported. Revoked certificates are accepted as long as
they are otherwise valid. If this is a concern, you may want to use
automatically managed certificates with a short validity period.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `HTTP client class <../tutorials/networking/http_client_class>`{.interpreted-text
  role="doc"}
- `TLS certificates <../tutorials/networking/ssl_certificates>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_HTTPClient_Method}
::: rst-class
classref-enumeration
:::
::::

enum **Method**: `🔗<enum_HTTPClient_Method>`{.interpreted-text
role="ref"}

:::: {#class_HTTPClient_constant_METHOD_GET}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_GET** = `0`

HTTP GET method. The GET method requests a representation of the
specified resource. Requests using GET should only retrieve data.

:::: {#class_HTTPClient_constant_METHOD_HEAD}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_HEAD** = `1`

HTTP HEAD method. The HEAD method asks for a response identical to that
of a GET request, but without the response body. This is useful to
request metadata like HTTP headers or to check if a resource exists.

:::: {#class_HTTPClient_constant_METHOD_POST}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_POST** = `2`

HTTP POST method. The POST method is used to submit an entity to the
specified resource, often causing a change in state or side effects on
the server. This is often used for forms and submitting data or
uploading files.

:::: {#class_HTTPClient_constant_METHOD_PUT}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_PUT** = `3`

HTTP PUT method. The PUT method asks to replace all current
representations of the target resource with the request payload. (You
can think of POST as \"create or update\" and PUT as \"update\",
although many services tend to not make a clear distinction or change
their meaning).

:::: {#class_HTTPClient_constant_METHOD_DELETE}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_DELETE** = `4`

HTTP DELETE method. The DELETE method requests to delete the specified
resource.

:::: {#class_HTTPClient_constant_METHOD_OPTIONS}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_OPTIONS** = `5`

HTTP OPTIONS method. The OPTIONS method asks for a description of the
communication options for the target resource. Rarely used.

:::: {#class_HTTPClient_constant_METHOD_TRACE}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_TRACE** = `6`

HTTP TRACE method. The TRACE method performs a message loop-back test
along the path to the target resource. Returns the entire HTTP request
received in the response body. Rarely used.

:::: {#class_HTTPClient_constant_METHOD_CONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_CONNECT** = `7`

HTTP CONNECT method. The CONNECT method establishes a tunnel to the
server identified by the target resource. Rarely used.

:::: {#class_HTTPClient_constant_METHOD_PATCH}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_PATCH** = `8`

HTTP PATCH method. The PATCH method is used to apply partial
modifications to a resource.

:::: {#class_HTTPClient_constant_METHOD_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}
**METHOD_MAX** = `9`

Represents the size of the
`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_HTTPClient_Status}
::: rst-class
classref-enumeration
:::
::::

enum **Status**: `🔗<enum_HTTPClient_Status>`{.interpreted-text
role="ref"}

:::: {#class_HTTPClient_constant_STATUS_DISCONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_DISCONNECTED** = `0`

Status: Disconnected from the server.

:::: {#class_HTTPClient_constant_STATUS_RESOLVING}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_RESOLVING** = `1`

Status: Currently resolving the hostname for the given URL into an IP.

:::: {#class_HTTPClient_constant_STATUS_CANT_RESOLVE}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_CANT_RESOLVE** = `2`

Status: DNS failure: Can\'t resolve the hostname for the given URL.

:::: {#class_HTTPClient_constant_STATUS_CONNECTING}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_CONNECTING** = `3`

Status: Currently connecting to server.

:::: {#class_HTTPClient_constant_STATUS_CANT_CONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_CANT_CONNECT** = `4`

Status: Can\'t connect to the server.

:::: {#class_HTTPClient_constant_STATUS_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_CONNECTED** = `5`

Status: Connection established.

:::: {#class_HTTPClient_constant_STATUS_REQUESTING}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_REQUESTING** = `6`

Status: Currently sending request.

:::: {#class_HTTPClient_constant_STATUS_BODY}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_BODY** = `7`

Status: HTTP body received.

:::: {#class_HTTPClient_constant_STATUS_CONNECTION_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_CONNECTION_ERROR** = `8`

Status: Error in HTTP connection.

:::: {#class_HTTPClient_constant_STATUS_TLS_HANDSHAKE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**STATUS_TLS_HANDSHAKE_ERROR** = `9`

Status: Error in TLS handshake.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_HTTPClient_ResponseCode}
::: rst-class
classref-enumeration
:::
::::

enum **ResponseCode**:
`🔗<enum_HTTPClient_ResponseCode>`{.interpreted-text role="ref"}

:::: {#class_HTTPClient_constant_RESPONSE_CONTINUE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_CONTINUE** = `100`

HTTP status code `100 Continue`. Interim response that indicates
everything so far is OK and that the client should continue with the
request (or ignore this status if already finished).

:::: {#class_HTTPClient_constant_RESPONSE_SWITCHING_PROTOCOLS}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_SWITCHING_PROTOCOLS** = `101`

HTTP status code `101 Switching Protocol`. Sent in response to an
`Upgrade` request header by the client. Indicates the protocol the
server is switching to.

:::: {#class_HTTPClient_constant_RESPONSE_PROCESSING}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_PROCESSING** = `102`

HTTP status code `102 Processing` (WebDAV). Indicates that the server
has received and is processing the request, but no response is available
yet.

:::: {#class_HTTPClient_constant_RESPONSE_OK}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_OK** = `200`

HTTP status code `200 OK`. The request has succeeded. Default response
for successful requests. Meaning varies depending on the request:

- `METHOD_GET<class_HTTPClient_constant_METHOD_GET>`{.interpreted-text
  role="ref"}: The resource has been fetched and is transmitted in the
  message body.
- `METHOD_HEAD<class_HTTPClient_constant_METHOD_HEAD>`{.interpreted-text
  role="ref"}: The entity headers are in the message body.
- `METHOD_POST<class_HTTPClient_constant_METHOD_POST>`{.interpreted-text
  role="ref"}: The resource describing the result of the action is
  transmitted in the message body.
- `METHOD_TRACE<class_HTTPClient_constant_METHOD_TRACE>`{.interpreted-text
  role="ref"}: The message body contains the request message as received
  by the server.

:::: {#class_HTTPClient_constant_RESPONSE_CREATED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_CREATED** = `201`

HTTP status code `201 Created`. The request has succeeded and a new
resource has been created as a result of it. This is typically the
response sent after a PUT request.

:::: {#class_HTTPClient_constant_RESPONSE_ACCEPTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_ACCEPTED** = `202`

HTTP status code `202 Accepted`. The request has been received but not
yet acted upon. It is non-committal, meaning that there is no way in
HTTP to later send an asynchronous response indicating the outcome of
processing the request. It is intended for cases where another process
or server handles the request, or for batch processing.

:::: {#class_HTTPClient_constant_RESPONSE_NON_AUTHORITATIVE_INFORMATION}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NON_AUTHORITATIVE_INFORMATION** = `203`

HTTP status code `203 Non-Authoritative Information`. This response code
means returned meta-information set is not exact set as available from
the origin server, but collected from a local or a third party copy.
Except this condition, 200 OK response should be preferred instead of
this response.

:::: {#class_HTTPClient_constant_RESPONSE_NO_CONTENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NO_CONTENT** = `204`

HTTP status code `204 No Content`. There is no content to send for this
request, but the headers may be useful. The user-agent may update its
cached headers for this resource with the new ones.

:::: {#class_HTTPClient_constant_RESPONSE_RESET_CONTENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_RESET_CONTENT** = `205`

HTTP status code `205 Reset Content`. The server has fulfilled the
request and desires that the client resets the \"document view\" that
caused the request to be sent to its original state as received from the
origin server.

:::: {#class_HTTPClient_constant_RESPONSE_PARTIAL_CONTENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_PARTIAL_CONTENT** = `206`

HTTP status code `206 Partial Content`. This response code is used
because of a range header sent by the client to separate download into
multiple streams.

:::: {#class_HTTPClient_constant_RESPONSE_MULTI_STATUS}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_MULTI_STATUS** = `207`

HTTP status code `207 Multi-Status` (WebDAV). A Multi-Status response
conveys information about multiple resources in situations where
multiple status codes might be appropriate.

:::: {#class_HTTPClient_constant_RESPONSE_ALREADY_REPORTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_ALREADY_REPORTED** = `208`

HTTP status code `208 Already Reported` (WebDAV). Used inside a DAV:
propstat response element to avoid enumerating the internal members of
multiple bindings to the same collection repeatedly.

:::: {#class_HTTPClient_constant_RESPONSE_IM_USED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_IM_USED** = `226`

HTTP status code `226 IM Used` (WebDAV). The server has fulfilled a GET
request for the resource, and the response is a representation of the
result of one or more instance-manipulations applied to the current
instance.

:::: {#class_HTTPClient_constant_RESPONSE_MULTIPLE_CHOICES}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_MULTIPLE_CHOICES** = `300`

HTTP status code `300 Multiple Choice`. The request has more than one
possible responses and there is no standardized way to choose one of the
responses. User-agent or user should choose one of them.

:::: {#class_HTTPClient_constant_RESPONSE_MOVED_PERMANENTLY}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_MOVED_PERMANENTLY** = `301`

HTTP status code `301 Moved Permanently`. Redirection. This response
code means the URI of requested resource has been changed. The new URI
is usually included in the response.

:::: {#class_HTTPClient_constant_RESPONSE_FOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_FOUND** = `302`

HTTP status code `302 Found`. Temporary redirection. This response code
means the URI of requested resource has been changed temporarily. New
changes in the URI might be made in the future. Therefore, this same URI
should be used by the client in future requests.

:::: {#class_HTTPClient_constant_RESPONSE_SEE_OTHER}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_SEE_OTHER** = `303`

HTTP status code `303 See Other`. The server is redirecting the user
agent to a different resource, as indicated by a URI in the Location
header field, which is intended to provide an indirect response to the
original request.

:::: {#class_HTTPClient_constant_RESPONSE_NOT_MODIFIED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NOT_MODIFIED** = `304`

HTTP status code `304 Not Modified`. A conditional GET or HEAD request
has been received and would have resulted in a 200 OK response if it
were not for the fact that the condition evaluated to `false`.

:::: {#class_HTTPClient_constant_RESPONSE_USE_PROXY}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_USE_PROXY** = `305`

**Deprecated:** Many clients ignore this response code for security
reasons. It is also deprecated by the HTTP standard.

HTTP status code `305 Use Proxy`.

:::: {#class_HTTPClient_constant_RESPONSE_SWITCH_PROXY}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_SWITCH_PROXY** = `306`

**Deprecated:** Many clients ignore this response code for security
reasons. It is also deprecated by the HTTP standard.

HTTP status code `306 Switch Proxy`.

:::: {#class_HTTPClient_constant_RESPONSE_TEMPORARY_REDIRECT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_TEMPORARY_REDIRECT** = `307`

HTTP status code `307 Temporary Redirect`. The target resource resides
temporarily under a different URI and the user agent MUST NOT change the
request method if it performs an automatic redirection to that URI.

:::: {#class_HTTPClient_constant_RESPONSE_PERMANENT_REDIRECT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_PERMANENT_REDIRECT** = `308`

HTTP status code `308 Permanent Redirect`. The target resource has been
assigned a new permanent URI and any future references to this resource
ought to use one of the enclosed URIs.

:::: {#class_HTTPClient_constant_RESPONSE_BAD_REQUEST}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_BAD_REQUEST** = `400`

HTTP status code `400 Bad Request`. The request was invalid. The server
cannot or will not process the request due to something that is
perceived to be a client error (e.g., malformed request syntax, invalid
request message framing, invalid request contents, or deceptive request
routing).

:::: {#class_HTTPClient_constant_RESPONSE_UNAUTHORIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_UNAUTHORIZED** = `401`

HTTP status code `401 Unauthorized`. Credentials required. The request
has not been applied because it lacks valid authentication credentials
for the target resource.

:::: {#class_HTTPClient_constant_RESPONSE_PAYMENT_REQUIRED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_PAYMENT_REQUIRED** = `402`

HTTP status code `402 Payment Required`. This response code is reserved
for future use. Initial aim for creating this code was using it for
digital payment systems, however this is not currently used.

:::: {#class_HTTPClient_constant_RESPONSE_FORBIDDEN}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_FORBIDDEN** = `403`

HTTP status code `403 Forbidden`. The client does not have access rights
to the content, i.e. they are unauthorized, so server is rejecting to
give proper response. Unlike `401`, the client\'s identity is known to
the server.

:::: {#class_HTTPClient_constant_RESPONSE_NOT_FOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NOT_FOUND** = `404`

HTTP status code `404 Not Found`. The server can not find requested
resource. Either the URL is not recognized or the endpoint is valid but
the resource itself does not exist. May also be sent instead of 403 to
hide existence of a resource if the client is not authorized.

:::: {#class_HTTPClient_constant_RESPONSE_METHOD_NOT_ALLOWED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_METHOD_NOT_ALLOWED** = `405`

HTTP status code `405 Method Not Allowed`. The request\'s HTTP method is
known by the server but has been disabled and cannot be used. For
example, an API may forbid DELETE-ing a resource. The two mandatory
methods, GET and HEAD, must never be disabled and should not return this
error code.

:::: {#class_HTTPClient_constant_RESPONSE_NOT_ACCEPTABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NOT_ACCEPTABLE** = `406`

HTTP status code `406 Not Acceptable`. The target resource does not have
a current representation that would be acceptable to the user agent,
according to the proactive negotiation header fields received in the
request. Used when negotiation content.

:::: {#class_HTTPClient_constant_RESPONSE_PROXY_AUTHENTICATION_REQUIRED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_PROXY_AUTHENTICATION_REQUIRED** = `407`

HTTP status code `407 Proxy Authentication Required`. Similar to 401
Unauthorized, but it indicates that the client needs to authenticate
itself in order to use a proxy.

:::: {#class_HTTPClient_constant_RESPONSE_REQUEST_TIMEOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_REQUEST_TIMEOUT** = `408`

HTTP status code `408 Request Timeout`. The server did not receive a
complete request message within the time that it was prepared to wait.

:::: {#class_HTTPClient_constant_RESPONSE_CONFLICT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_CONFLICT** = `409`

HTTP status code `409 Conflict`. The request could not be completed due
to a conflict with the current state of the target resource. This code
is used in situations where the user might be able to resolve the
conflict and resubmit the request.

:::: {#class_HTTPClient_constant_RESPONSE_GONE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_GONE** = `410`

HTTP status code `410 Gone`. The target resource is no longer available
at the origin server and this condition is likely permanent.

:::: {#class_HTTPClient_constant_RESPONSE_LENGTH_REQUIRED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_LENGTH_REQUIRED** = `411`

HTTP status code `411 Length Required`. The server refuses to accept the
request without a defined Content-Length header.

:::: {#class_HTTPClient_constant_RESPONSE_PRECONDITION_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_PRECONDITION_FAILED** = `412`

HTTP status code `412 Precondition Failed`. One or more conditions given
in the request header fields evaluated to `false` when tested on the
server.

:::: {#class_HTTPClient_constant_RESPONSE_REQUEST_ENTITY_TOO_LARGE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_REQUEST_ENTITY_TOO_LARGE** = `413`

HTTP status code `413 Entity Too Large`. The server is refusing to
process a request because the request payload is larger than the server
is willing or able to process.

:::: {#class_HTTPClient_constant_RESPONSE_REQUEST_URI_TOO_LONG}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_REQUEST_URI_TOO_LONG** = `414`

HTTP status code `414 Request-URI Too Long`. The server is refusing to
service the request because the request-target is longer than the server
is willing to interpret.

:::: {#class_HTTPClient_constant_RESPONSE_UNSUPPORTED_MEDIA_TYPE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_UNSUPPORTED_MEDIA_TYPE** = `415`

HTTP status code `415 Unsupported Media Type`. The origin server is
refusing to service the request because the payload is in a format not
supported by this method on the target resource.

:::: {#class_HTTPClient_constant_RESPONSE_REQUESTED_RANGE_NOT_SATISFIABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_REQUESTED_RANGE_NOT_SATISFIABLE** = `416`

HTTP status code `416 Requested Range Not Satisfiable`. None of the
ranges in the request\'s Range header field overlap the current extent
of the selected resource or the set of ranges requested has been
rejected due to invalid ranges or an excessive request of small or
overlapping ranges.

:::: {#class_HTTPClient_constant_RESPONSE_EXPECTATION_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_EXPECTATION_FAILED** = `417`

HTTP status code `417 Expectation Failed`. The expectation given in the
request\'s Expect header field could not be met by at least one of the
inbound servers.

:::: {#class_HTTPClient_constant_RESPONSE_IM_A_TEAPOT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_IM_A_TEAPOT** = `418`

HTTP status code `418 I'm A Teapot`. Any attempt to brew coffee with a
teapot should result in the error code \"418 I\'m a teapot\". The
resulting entity body MAY be short and stout.

:::: {#class_HTTPClient_constant_RESPONSE_MISDIRECTED_REQUEST}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_MISDIRECTED_REQUEST** = `421`

HTTP status code `421 Misdirected Request`. The request was directed at
a server that is not able to produce a response. This can be sent by a
server that is not configured to produce responses for the combination
of scheme and authority that are included in the request URI.

:::: {#class_HTTPClient_constant_RESPONSE_UNPROCESSABLE_ENTITY}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_UNPROCESSABLE_ENTITY** = `422`

HTTP status code `422 Unprocessable Entity` (WebDAV). The server
understands the content type of the request entity (hence a 415
Unsupported Media Type status code is inappropriate), and the syntax of
the request entity is correct (thus a 400 Bad Request status code is
inappropriate) but was unable to process the contained instructions.

:::: {#class_HTTPClient_constant_RESPONSE_LOCKED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_LOCKED** = `423`

HTTP status code `423 Locked` (WebDAV). The source or destination
resource of a method is locked.

:::: {#class_HTTPClient_constant_RESPONSE_FAILED_DEPENDENCY}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_FAILED_DEPENDENCY** = `424`

HTTP status code `424 Failed Dependency` (WebDAV). The method could not
be performed on the resource because the requested action depended on
another action and that action failed.

:::: {#class_HTTPClient_constant_RESPONSE_UPGRADE_REQUIRED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_UPGRADE_REQUIRED** = `426`

HTTP status code `426 Upgrade Required`. The server refuses to perform
the request using the current protocol but might be willing to do so
after the client upgrades to a different protocol.

:::: {#class_HTTPClient_constant_RESPONSE_PRECONDITION_REQUIRED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_PRECONDITION_REQUIRED** = `428`

HTTP status code `428 Precondition Required`. The origin server requires
the request to be conditional.

:::: {#class_HTTPClient_constant_RESPONSE_TOO_MANY_REQUESTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_TOO_MANY_REQUESTS** = `429`

HTTP status code `429 Too Many Requests`. The user has sent too many
requests in a given amount of time (see \"rate limiting\"). Back off and
increase time between requests or try again later.

:::: {#class_HTTPClient_constant_RESPONSE_REQUEST_HEADER_FIELDS_TOO_LARGE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_REQUEST_HEADER_FIELDS_TOO_LARGE** = `431`

HTTP status code `431 Request Header Fields Too Large`. The server is
unwilling to process the request because its header fields are too
large. The request MAY be resubmitted after reducing the size of the
request header fields.

:::: {#class_HTTPClient_constant_RESPONSE_UNAVAILABLE_FOR_LEGAL_REASONS}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_UNAVAILABLE_FOR_LEGAL_REASONS** = `451`

HTTP status code `451 Response Unavailable For Legal Reasons`. The
server is denying access to the resource as a consequence of a legal
demand.

:::: {#class_HTTPClient_constant_RESPONSE_INTERNAL_SERVER_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_INTERNAL_SERVER_ERROR** = `500`

HTTP status code `500 Internal Server Error`. The server encountered an
unexpected condition that prevented it from fulfilling the request.

:::: {#class_HTTPClient_constant_RESPONSE_NOT_IMPLEMENTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NOT_IMPLEMENTED** = `501`

HTTP status code `501 Not Implemented`. The server does not support the
functionality required to fulfill the request.

:::: {#class_HTTPClient_constant_RESPONSE_BAD_GATEWAY}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_BAD_GATEWAY** = `502`

HTTP status code `502 Bad Gateway`. The server, while acting as a
gateway or proxy, received an invalid response from an inbound server it
accessed while attempting to fulfill the request. Usually returned by
load balancers or proxies.

:::: {#class_HTTPClient_constant_RESPONSE_SERVICE_UNAVAILABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_SERVICE_UNAVAILABLE** = `503`

HTTP status code `503 Service Unavailable`. The server is currently
unable to handle the request due to a temporary overload or scheduled
maintenance, which will likely be alleviated after some delay. Try again
later.

:::: {#class_HTTPClient_constant_RESPONSE_GATEWAY_TIMEOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_GATEWAY_TIMEOUT** = `504`

HTTP status code `504 Gateway Timeout`. The server, while acting as a
gateway or proxy, did not receive a timely response from an upstream
server it needed to access in order to complete the request. Usually
returned by load balancers or proxies.

:::: {#class_HTTPClient_constant_RESPONSE_HTTP_VERSION_NOT_SUPPORTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_HTTP_VERSION_NOT_SUPPORTED** = `505`

HTTP status code `505 HTTP Version Not Supported`. The server does not
support, or refuses to support, the major version of HTTP that was used
in the request message.

:::: {#class_HTTPClient_constant_RESPONSE_VARIANT_ALSO_NEGOTIATES}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_VARIANT_ALSO_NEGOTIATES** = `506`

HTTP status code `506 Variant Also Negotiates`. The server has an
internal configuration error: the chosen variant resource is configured
to engage in transparent content negotiation itself, and is therefore
not a proper end point in the negotiation process.

:::: {#class_HTTPClient_constant_RESPONSE_INSUFFICIENT_STORAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_INSUFFICIENT_STORAGE** = `507`

HTTP status code `507 Insufficient Storage`. The method could not be
performed on the resource because the server is unable to store the
representation needed to successfully complete the request.

:::: {#class_HTTPClient_constant_RESPONSE_LOOP_DETECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_LOOP_DETECTED** = `508`

HTTP status code `508 Loop Detected`. The server terminated an operation
because it encountered an infinite loop while processing a request with
\"Depth: infinity\". This status indicates that the entire operation
failed.

:::: {#class_HTTPClient_constant_RESPONSE_NOT_EXTENDED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NOT_EXTENDED** = `510`

HTTP status code `510 Not Extended`. The policy for accessing the
resource has not been met in the request. The server should send back
all the information necessary for the client to issue an extended
request.

:::: {#class_HTTPClient_constant_RESPONSE_NETWORK_AUTH_REQUIRED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResponseCode<enum_HTTPClient_ResponseCode>`{.interpreted-text
role="ref"} **RESPONSE_NETWORK_AUTH_REQUIRED** = `511`

HTTP status code `511 Network Authentication Required`. The client needs
to authenticate to gain network access.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_HTTPClient_property_blocking_mode_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**blocking_mode_enabled** = `false`
`🔗<class_HTTPClient_property_blocking_mode_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blocking_mode**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_blocking_mode_enabled**()

If `true`, execution will block until all data is read from the
response.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_property_connection}
::: rst-class
classref-property
:::
::::

`StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"}
**connection**
`🔗<class_HTTPClient_property_connection>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_connection**(value:
  `StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"})
- `StreamPeer<class_StreamPeer>`{.interpreted-text role="ref"}
  **get_connection**()

The connection to use for this client.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_property_read_chunk_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **read_chunk_size** =
`65536`
`🔗<class_HTTPClient_property_read_chunk_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_read_chunk_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_read_chunk_size**()

The size of the buffer used and maximum bytes to read per iteration. See
`read_response_body_chunk()<class_HTTPClient_method_read_response_body_chunk>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_HTTPClient_method_close}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **close**()
`🔗<class_HTTPClient_method_close>`{.interpreted-text role="ref"}

Closes the current connection, allowing reuse of this **HTTPClient**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_connect_to_host}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**connect_to_host**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"} = -1,
tls_options: `TLSOptions<class_TLSOptions>`{.interpreted-text
role="ref"} = null)
`🔗<class_HTTPClient_method_connect_to_host>`{.interpreted-text
role="ref"}

Connects to a host. This needs to be done before any requests are sent.

If no `port` is specified (or `-1` is used), it is automatically set to
80 for HTTP and 443 for HTTPS. You can pass the optional `tls_options`
parameter to customize the trusted certification authorities, or the
common name verification when using HTTPS. See
`TLSOptions.client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"} and
`TLSOptions.client_unsafe()<class_TLSOptions_method_client_unsafe>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_get_response_body_length}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_response_body_length**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HTTPClient_method_get_response_body_length>`{.interpreted-text
role="ref"}

Returns the response\'s body length.

\*\*Note:\*\* Some Web servers may not send a body length. In this case,
the value returned will be `-1`. If using chunked transfer encoding, the
body length will also be `-1`.

\*\*Note:\*\* This function always returns `-1` on the Web platform due
to browsers limitations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_get_response_code}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_response_code**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HTTPClient_method_get_response_code>`{.interpreted-text
role="ref"}

Returns the response\'s HTTP status code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_get_response_headers}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_response_headers**()
`🔗<class_HTTPClient_method_get_response_headers>`{.interpreted-text
role="ref"}

Returns the response headers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_get_response_headers_as_dictionary}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_response_headers_as_dictionary**()
`🔗<class_HTTPClient_method_get_response_headers_as_dictionary>`{.interpreted-text
role="ref"}

Returns all response headers as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}. Each entry
is composed by the header name, and a
`String<class_String>`{.interpreted-text role="ref"} containing the
values separated by `"; "`. The casing is kept the same as the headers
were received.

    {
        "content-length": 12,
        "Content-Type": "application/json; charset=UTF-8",
    }

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_get_status}
::: rst-class
classref-method
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**get_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_HTTPClient_method_get_status>`{.interpreted-text
role="ref"}

Returns a `Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
constant. Need to call
`poll()<class_HTTPClient_method_poll>`{.interpreted-text role="ref"} in
order to get status updates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_has_response}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_response**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HTTPClient_method_has_response>`{.interpreted-text role="ref"}

If `true`, this **HTTPClient** has a response available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_is_response_chunked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_response_chunked**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HTTPClient_method_is_response_chunked>`{.interpreted-text
role="ref"}

If `true`, this **HTTPClient** has a response that is chunked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_poll}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**poll**() `🔗<class_HTTPClient_method_poll>`{.interpreted-text
role="ref"}

This needs to be called in order to have any request processed. Check
results with
`get_status()<class_HTTPClient_method_get_status>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_query_string_from_dict}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**query_string_from_dict**(fields:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_HTTPClient_method_query_string_from_dict>`{.interpreted-text
role="ref"}

Generates a GET/POST application/x-www-form-urlencoded style query
string from a provided dictionary, e.g.:

::::: tabs
::: code-tab
gdscript

var fields = { \"username\": \"user\", \"password\": \"pass\" } var
query_string = http_client.query_string_from_dict(fields) \# Returns
\"username=user&password=pass\"
:::

::: code-tab
csharp

var fields = new Godot.Collections.Dictionary { { \"username\", \"user\"
}, { \"password\", \"pass\" } }; string queryString =
httpClient.QueryStringFromDict(fields); // Returns
\"username=user&password=pass\"
:::
:::::

Furthermore, if a key has a `null` value, only the key itself is added,
without equal sign and value. If the value is an array, for each value
in it a pair with the same key is added.

::::: tabs
::: code-tab
gdscript

var fields = { \"single\": 123, \"not_valued\": null, \"multiple\":
\[22, 33, 44\] } var query_string =
http_client.query_string_from_dict(fields) \# Returns
\"single=123&not_valued&multiple=22&multiple=33&multiple=44\"
:::

::: code-tab
csharp

var fields = new Godot.Collections.Dictionary { { \"single\", 123 }, {
\"notValued\", default }, { \"multiple\", new Godot.Collections.Array {
22, 33, 44 } }, }; string queryString =
httpClient.QueryStringFromDict(fields); // Returns
\"single=123&not_valued&multiple=22&multiple=33&multiple=44\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_read_response_body_chunk}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**read_response_body_chunk**()
`🔗<class_HTTPClient_method_read_response_body_chunk>`{.interpreted-text
role="ref"}

Reads one chunk from the response.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_request}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**request**(method: `Method<enum_HTTPClient_Method>`{.interpreted-text
role="ref"}, url: `String<class_String>`{.interpreted-text role="ref"},
headers: `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, body: `String<class_String>`{.interpreted-text role="ref"}
= \"\") `🔗<class_HTTPClient_method_request>`{.interpreted-text
role="ref"}

Sends an HTTP request to the connected host with the given `method`.

The URL parameter is usually just the part after the host, so for
`https://example.com/index.php`, it is `/index.php`. When sending
requests to an HTTP proxy server, it should be an absolute URL. For
`METHOD_OPTIONS<class_HTTPClient_constant_METHOD_OPTIONS>`{.interpreted-text
role="ref"} requests, `*` is also allowed. For
`METHOD_CONNECT<class_HTTPClient_constant_METHOD_CONNECT>`{.interpreted-text
role="ref"} requests, it should be the authority component
(`host:port`).

`headers` are HTTP request headers.

To create a POST request with query strings to push to the server, do:

::::: tabs
::: code-tab
gdscript

var fields = { \"username\": \"user\", \"password\": \"pass\" } var
query_string = http_client.query_string_from_dict(fields) var headers =
\[\"Content-Type: application/x-www-form-urlencoded\", \"Content-Length:
\" + str(query_string.length())\] var result =
http_client.request(http_client.METHOD_POST, \"/index.php\", headers,
query_string)
:::

::: code-tab
csharp

var fields = new Godot.Collections.Dictionary { { \"username\", \"user\"
}, { \"password\", \"pass\" } }; string queryString = new
HttpClient().QueryStringFromDict(fields); string\[\] headers =
\[\"Content-Type: application/x-www-form-urlencoded\",
\$\"Content-Length: {queryString.Length}\"\]; var result = new
HttpClient().Request(HttpClient.Method.Post, \"index.php\", headers,
queryString);
:::
:::::

\*\*Note:\*\* The `body` parameter is ignored if `method` is
`METHOD_GET<class_HTTPClient_constant_METHOD_GET>`{.interpreted-text
role="ref"}. This is because GET methods can\'t contain request data. As
a workaround, you can pass request data as a query string in the URL.
See
`String.uri_encode()<class_String_method_uri_encode>`{.interpreted-text
role="ref"} for an example.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_request_raw}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**request_raw**(method:
`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"}, url:
`String<class_String>`{.interpreted-text role="ref"}, headers:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, body:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_HTTPClient_method_request_raw>`{.interpreted-text role="ref"}

Sends a raw HTTP request to the connected host with the given `method`.

The URL parameter is usually just the part after the host, so for
`https://example.com/index.php`, it is `/index.php`. When sending
requests to an HTTP proxy server, it should be an absolute URL. For
`METHOD_OPTIONS<class_HTTPClient_constant_METHOD_OPTIONS>`{.interpreted-text
role="ref"} requests, `*` is also allowed. For
`METHOD_CONNECT<class_HTTPClient_constant_METHOD_CONNECT>`{.interpreted-text
role="ref"} requests, it should be the authority component
(`host:port`).

`headers` are HTTP request headers.

Sends the body data raw, as a byte array and does not encode it in any
way.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_set_http_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_http_proxy**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_HTTPClient_method_set_http_proxy>`{.interpreted-text
role="ref"}

Sets the proxy server for HTTP requests.

The proxy server is unset if `host` is empty or `port` is -1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPClient_method_set_https_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_https_proxy**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_HTTPClient_method_set_https_proxy>`{.interpreted-text
role="ref"}

Sets the proxy server for HTTPS requests.

The proxy server is unset if `host` is empty or `port` is -1.
