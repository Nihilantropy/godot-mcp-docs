github_url
:   hide

# HTTPRequest {#class_HTTPRequest}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node with the ability to send HTTP(S) requests.

::: rst-class
classref-introduction-group
:::

## Description

A node with the ability to send HTTP requests. Uses
`HTTPClient<class_HTTPClient>`{.interpreted-text role="ref"} internally.

Can be used to make HTTP requests, i.e. download or upload files or web
content via HTTP.

\*\*Warning:\*\* See the notes and warnings on
`HTTPClient<class_HTTPClient>`{.interpreted-text role="ref"} for
limitations, especially regarding TLS security.

\*\*Note:\*\* When exporting to Android, make sure to enable the
`INTERNET` permission in the Android export preset before exporting the
project or using one-click deploy. Otherwise, network communication of
any kind will be blocked by Android.

\*\*Example:\*\* Contact a REST API and print one of its returned
fields:

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   \# Create an HTTP request node and connect its completion signal.
    var http_request = HTTPRequest.new() add_child(http_request)
    http_request.request_completed.connect(self.\_http_request_completed)

    \# Perform a GET request. The URL below returns JSON as of writing.
    var error = http_request.request(\"https://httpbin.org/get\") if
    error != OK: push_error(\"An error occurred in the HTTP request.\")

    \# Perform a POST request. The URL below returns JSON as of writing.
    \# Note: Don\'t make simultaneous requests using a single
    HTTPRequest node. \# The snippet below is provided for reference
    only. var body = JSON.new().stringify({\"name\": \"Godette\"}) error
    = http_request.request(\"https://httpbin.org/post\", \[\],
    HTTPClient.METHOD_POST, body) if error != OK: push_error(\"An error
    occurred in the HTTP request.\")

\# Called when the HTTP request is completed. func
[http_request_completed]{#http_request_completed}(result, response_code,
headers, body): var json = JSON.new()
json.parse(body.get_string_from_utf8()) var response = json.get_data()

> \# Will print the user agent string used by the HTTPRequest node (as
> recognized by httpbin.org). print(response.headers\[\"User-Agent\"\])
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { // Create an HTTP request node
and connect its completion signal. var httpRequest = new HttpRequest();
AddChild(httpRequest); httpRequest.RequestCompleted +=
HttpRequestCompleted;

> // Perform a GET request. The URL below returns JSON as of writing.
> Error error = httpRequest.Request(\"https://httpbin.org/get\"); if
> (error != Error.Ok) { GD.PushError(\"An error occurred in the HTTP
> request.\"); }
>
> // Perform a POST request. The URL below returns JSON as of writing.
> // Note: Don\'t make simultaneous requests using a single HTTPRequest
> node. // The snippet below is provided for reference only. string body
> = new Json().Stringify(new Godot.Collections.Dictionary { { \"name\",
> \"Godette\" } }); error =
> httpRequest.Request(\"https://httpbin.org/post\", null,
> HttpClient.Method.Post, body); if (error != Error.Ok) {
> GD.PushError(\"An error occurred in the HTTP request.\"); }

}

// Called when the HTTP request is completed. private void
HttpRequestCompleted(long result, long responseCode, string\[\] headers,
byte\[\] body) { var json = new Json();
json.Parse(body.GetStringFromUtf8()); var response =
json.GetData().AsGodotDictionary();

> // Will print the user agent string used by the HTTPRequest node (as
> recognized by httpbin.org).
> GD.Print((response\[\"headers\"\].AsGodotDictionary())\[\"User-Agent\"\]);

}
:::
:::::

\*\*Example:\*\* Load an image using **HTTPRequest** and display it:

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   \# Create an HTTP request node and connect its completion signal.
    var http_request = HTTPRequest.new() add_child(http_request)
    http_request.request_completed.connect(self.\_http_request_completed)

    \# Perform the HTTP request. The URL below returns a PNG image as of
    writing. var error =
    http_request.request(\"https://placehold.co/512.png\") if error !=
    OK: push_error(\"An error occurred in the HTTP request.\")

\# Called when the HTTP request is completed. func
[http_request_completed]{#http_request_completed}(result, response_code,
headers, body): if result != HTTPRequest.RESULT_SUCCESS:
push_error(\"Image couldn\'t be downloaded. Try a different image.\")

> var image = Image.new() var error = image.load_png_from_buffer(body)
> if error != OK: push_error(\"Couldn\'t load the image.\")
>
> var texture = ImageTexture.create_from_image(image)
>
> \# Display the image in a TextureRect node. var texture_rect =
> TextureRect.new() add_child(texture_rect) texture_rect.texture =
> texture
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { // Create an HTTP request node
and connect its completion signal. var httpRequest = new HttpRequest();
AddChild(httpRequest); httpRequest.RequestCompleted +=
HttpRequestCompleted;

> // Perform the HTTP request. The URL below returns a PNG image as of
> writing. Error error =
> httpRequest.Request(\"https://placehold.co/512.png\"); if (error !=
> Error.Ok) { GD.PushError(\"An error occurred in the HTTP request.\");
> }

}

// Called when the HTTP request is completed. private void
HttpRequestCompleted(long result, long responseCode, string\[\] headers,
byte\[\] body) { if (result != (long)HttpRequest.Result.Success) {
GD.PushError(\"Image couldn\'t be downloaded. Try a different image.\");
} var image = new Image(); Error error = image.LoadPngFromBuffer(body);
if (error != Error.Ok) { GD.PushError(\"Couldn\'t load the image.\"); }

> var texture = ImageTexture.CreateFromImage(image);
>
> // Display the image in a TextureRect node. var textureRect = new
> TextureRect(); AddChild(textureRect); textureRect.Texture = texture;

}
:::
:::::

\*\*Note:\*\* **HTTPRequest** nodes will automatically handle
decompression of response bodies. An `Accept-Encoding` header will be
automatically added to each of your requests, unless one is already
specified. Any response with a `Content-Encoding: gzip` header will
automatically be decompressed and delivered to you as uncompressed
bytes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Making HTTP requests <../tutorials/networking/http_request_class>`{.interpreted-text
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

## Signals

:::: {#class_HTTPRequest_signal_request_completed}
::: rst-class
classref-signal
:::
::::

**request_completed**(result: `int<class_int>`{.interpreted-text
role="ref"}, response_code: `int<class_int>`{.interpreted-text
role="ref"}, headers:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, body:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_HTTPRequest_signal_request_completed>`{.interpreted-text
role="ref"}

Emitted when a request is completed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_HTTPRequest_Result}
::: rst-class
classref-enumeration
:::
::::

enum **Result**: `🔗<enum_HTTPRequest_Result>`{.interpreted-text
role="ref"}

:::: {#class_HTTPRequest_constant_RESULT_SUCCESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_SUCCESS** = `0`

Request successful.

:::: {#class_HTTPRequest_constant_RESULT_CHUNKED_BODY_SIZE_MISMATCH}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_CHUNKED_BODY_SIZE_MISMATCH** = `1`

Request failed due to a mismatch between the expected and actual chunked
body size during transfer. Possible causes include network errors,
server misconfiguration, or issues with chunked encoding.

:::: {#class_HTTPRequest_constant_RESULT_CANT_CONNECT}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_CANT_CONNECT** = `2`

Request failed while connecting.

:::: {#class_HTTPRequest_constant_RESULT_CANT_RESOLVE}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_CANT_RESOLVE** = `3`

Request failed while resolving.

:::: {#class_HTTPRequest_constant_RESULT_CONNECTION_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_CONNECTION_ERROR** = `4`

Request failed due to connection (read/write) error.

:::: {#class_HTTPRequest_constant_RESULT_TLS_HANDSHAKE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_TLS_HANDSHAKE_ERROR** = `5`

Request failed on TLS handshake.

:::: {#class_HTTPRequest_constant_RESULT_NO_RESPONSE}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_NO_RESPONSE** = `6`

Request does not have a response (yet).

:::: {#class_HTTPRequest_constant_RESULT_BODY_SIZE_LIMIT_EXCEEDED}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_BODY_SIZE_LIMIT_EXCEEDED** = `7`

Request exceeded its maximum size limit, see
`body_size_limit<class_HTTPRequest_property_body_size_limit>`{.interpreted-text
role="ref"}.

:::: {#class_HTTPRequest_constant_RESULT_BODY_DECOMPRESS_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_BODY_DECOMPRESS_FAILED** = `8`

Request failed due to an error while decompressing the response body.
Possible causes include unsupported or incorrect compression format,
corrupted data, or incomplete transfer.

:::: {#class_HTTPRequest_constant_RESULT_REQUEST_FAILED}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_REQUEST_FAILED** = `9`

Request failed (currently unused).

:::: {#class_HTTPRequest_constant_RESULT_DOWNLOAD_FILE_CANT_OPEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_DOWNLOAD_FILE_CANT_OPEN** = `10`

HTTPRequest couldn\'t open the download file.

:::: {#class_HTTPRequest_constant_RESULT_DOWNLOAD_FILE_WRITE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_DOWNLOAD_FILE_WRITE_ERROR** = `11`

HTTPRequest couldn\'t write to the download file.

:::: {#class_HTTPRequest_constant_RESULT_REDIRECT_LIMIT_REACHED}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_REDIRECT_LIMIT_REACHED** = `12`

Request reached its maximum redirect limit, see
`max_redirects<class_HTTPRequest_property_max_redirects>`{.interpreted-text
role="ref"}.

:::: {#class_HTTPRequest_constant_RESULT_TIMEOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`Result<enum_HTTPRequest_Result>`{.interpreted-text role="ref"}
**RESULT_TIMEOUT** = `13`

Request failed due to a timeout. If you expect requests to take a long
time, try increasing the value of
`timeout<class_HTTPRequest_property_timeout>`{.interpreted-text
role="ref"} or setting it to `0.0` to remove the timeout completely.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_HTTPRequest_property_accept_gzip}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **accept_gzip** =
`true` `🔗<class_HTTPRequest_property_accept_gzip>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_accept_gzip**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_accepting_gzip**()

If `true`, this header will be added to each request:
`Accept-Encoding: gzip, deflate` telling servers that it\'s okay to
compress response bodies.

Any Response body declaring a `Content-Encoding` of either `gzip` or
`deflate` will then be automatically decompressed, and the uncompressed
bytes will be delivered via
`request_completed<class_HTTPRequest_signal_request_completed>`{.interpreted-text
role="ref"}.

If the user has specified their own `Accept-Encoding` header, then no
header will be added regardless of
`accept_gzip<class_HTTPRequest_property_accept_gzip>`{.interpreted-text
role="ref"}.

If `false` no header will be added, and no decompression will be
performed on response bodies. The raw bytes of the response body will be
returned via
`request_completed<class_HTTPRequest_signal_request_completed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_property_body_size_limit}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **body_size_limit** =
`-1` `🔗<class_HTTPRequest_property_body_size_limit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_body_size_limit**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_body_size_limit**()

Maximum allowed size for response bodies. If the response body is
compressed, this will be used as the maximum allowed size for the
decompressed body.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_property_download_chunk_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **download_chunk_size** =
`65536`
`🔗<class_HTTPRequest_property_download_chunk_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_download_chunk_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_download_chunk_size**()

The size of the buffer used and maximum bytes to read per iteration. See
`HTTPClient.read_chunk_size<class_HTTPClient_property_read_chunk_size>`{.interpreted-text
role="ref"}.

Set this to a lower value (e.g. 4096 for 4 KiB) when downloading small
files to decrease memory usage at the cost of download speeds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_property_download_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **download_file** =
`""` `🔗<class_HTTPRequest_property_download_file>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_download_file**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_download_file**()

The file to download into. Will output any received file into it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_property_max_redirects}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_redirects** = `8`
`🔗<class_HTTPRequest_property_max_redirects>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_redirects**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_redirects**()

Maximum number of allowed redirects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_property_timeout}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **timeout** = `0.0`
`🔗<class_HTTPRequest_property_timeout>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_timeout**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_timeout**()

The duration to wait in seconds before a request times out. If
`timeout<class_HTTPRequest_property_timeout>`{.interpreted-text
role="ref"} is set to `0.0` then the request will never time out. For
simple requests, such as communication with a REST API, it is
recommended that
`timeout<class_HTTPRequest_property_timeout>`{.interpreted-text
role="ref"} is set to a value suitable for the server response time
(e.g. between `1.0` and `10.0`). This will help prevent unwanted
timeouts caused by variation in server response times while still
allowing the application to detect when a request has timed out. For
larger requests such as file downloads it is suggested the
`timeout<class_HTTPRequest_property_timeout>`{.interpreted-text
role="ref"} be set to `0.0`, disabling the timeout functionality. This
will help to prevent large transfers from failing due to exceeding the
timeout value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_property_use_threads}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_threads** =
`false` `🔗<class_HTTPRequest_property_use_threads>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_threads**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_threads**()

If `true`, multithreading is used to improve performance.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_HTTPRequest_method_cancel_request}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cancel_request**()
`🔗<class_HTTPRequest_method_cancel_request>`{.interpreted-text
role="ref"}

Cancels the current request.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_get_body_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_body_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HTTPRequest_method_get_body_size>`{.interpreted-text
role="ref"}

Returns the response body length.

\*\*Note:\*\* Some Web servers may not send a body length. In this case,
the value returned will be `-1`. If using chunked transfer encoding, the
body length will also be `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_get_downloaded_bytes}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_downloaded_bytes**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HTTPRequest_method_get_downloaded_bytes>`{.interpreted-text
role="ref"}

Returns the number of bytes this HTTPRequest downloaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_get_http_client_status}
::: rst-class
classref-method
:::
::::

`Status<enum_HTTPClient_Status>`{.interpreted-text role="ref"}
**get_http_client_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_HTTPRequest_method_get_http_client_status>`{.interpreted-text
role="ref"}

Returns the current status of the underlying
`HTTPClient<class_HTTPClient>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_request}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**request**(url: `String<class_String>`{.interpreted-text role="ref"},
custom_headers:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} = PackedStringArray(), method:
`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"} = 0,
request_data: `String<class_String>`{.interpreted-text role="ref"} =
\"\") `🔗<class_HTTPRequest_method_request>`{.interpreted-text
role="ref"}

Creates request on the underlying
`HTTPClient<class_HTTPClient>`{.interpreted-text role="ref"}. If there
is no configuration errors, it tries to connect using
`HTTPClient.connect_to_host()<class_HTTPClient_method_connect_to_host>`{.interpreted-text
role="ref"} and passes parameters onto
`HTTPClient.request()<class_HTTPClient_method_request>`{.interpreted-text
role="ref"}.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if request is successfully created. (Does not imply that the
server has responded),
`@GlobalScope.ERR_UNCONFIGURED<class_@GlobalScope_constant_ERR_UNCONFIGURED>`{.interpreted-text
role="ref"} if not in the tree,
`@GlobalScope.ERR_BUSY<class_@GlobalScope_constant_ERR_BUSY>`{.interpreted-text
role="ref"} if still processing previous request,
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if given string is not a valid URL format, or
`@GlobalScope.ERR_CANT_CONNECT<class_@GlobalScope_constant_ERR_CANT_CONNECT>`{.interpreted-text
role="ref"} if not using thread and the
`HTTPClient<class_HTTPClient>`{.interpreted-text role="ref"} cannot
connect to host.

\*\*Note:\*\* When `method` is
`HTTPClient.METHOD_GET<class_HTTPClient_constant_METHOD_GET>`{.interpreted-text
role="ref"}, the payload sent via `request_data` might be ignored by the
server or even cause the server to reject the request (check [RFC 7231
section
4.3.1](https://datatracker.ietf.org/doc/html/rfc7231#section-4.3.1) for
more details). As a workaround, you can send data as a query string in
the URL (see
`String.uri_encode()<class_String_method_uri_encode>`{.interpreted-text
role="ref"} for an example).

\*\*Note:\*\* It\'s recommended to use transport encryption (TLS) and to
avoid sending sensitive information (such as login credentials) in HTTP
GET URL parameters. Consider using HTTP POST requests or HTTP headers
for such information instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_request_raw}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**request_raw**(url: `String<class_String>`{.interpreted-text
role="ref"}, custom_headers:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} = PackedStringArray(), method:
`Method<enum_HTTPClient_Method>`{.interpreted-text role="ref"} = 0,
request_data_raw:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"} =
PackedByteArray())
`🔗<class_HTTPRequest_method_request_raw>`{.interpreted-text role="ref"}

Creates request on the underlying
`HTTPClient<class_HTTPClient>`{.interpreted-text role="ref"} using a raw
array of bytes for the request body. If there is no configuration
errors, it tries to connect using
`HTTPClient.connect_to_host()<class_HTTPClient_method_connect_to_host>`{.interpreted-text
role="ref"} and passes parameters onto
`HTTPClient.request()<class_HTTPClient_method_request>`{.interpreted-text
role="ref"}.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if request is successfully created. (Does not imply that the
server has responded),
`@GlobalScope.ERR_UNCONFIGURED<class_@GlobalScope_constant_ERR_UNCONFIGURED>`{.interpreted-text
role="ref"} if not in the tree,
`@GlobalScope.ERR_BUSY<class_@GlobalScope_constant_ERR_BUSY>`{.interpreted-text
role="ref"} if still processing previous request,
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if given string is not a valid URL format, or
`@GlobalScope.ERR_CANT_CONNECT<class_@GlobalScope_constant_ERR_CANT_CONNECT>`{.interpreted-text
role="ref"} if not using thread and the
`HTTPClient<class_HTTPClient>`{.interpreted-text role="ref"} cannot
connect to host.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_set_http_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_http_proxy**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_HTTPRequest_method_set_http_proxy>`{.interpreted-text
role="ref"}

Sets the proxy server for HTTP requests.

The proxy server is unset if `host` is empty or `port` is -1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_set_https_proxy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_https_proxy**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_HTTPRequest_method_set_https_proxy>`{.interpreted-text
role="ref"}

Sets the proxy server for HTTPS requests.

The proxy server is unset if `host` is empty or `port` is -1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_HTTPRequest_method_set_tls_options}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tls_options**(client_options:
`TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"})
`🔗<class_HTTPRequest_method_set_tls_options>`{.interpreted-text
role="ref"}

Sets the `TLSOptions<class_TLSOptions>`{.interpreted-text role="ref"} to
be used when connecting to an HTTPS server. See
`TLSOptions.client()<class_TLSOptions_method_client>`{.interpreted-text
role="ref"}.
