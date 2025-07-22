github_url
:   hide

# JSONRPC {#class_JSONRPC}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A helper to handle dictionaries which look like JSONRPC documents.

::: rst-class
classref-introduction-group
:::

## Description

[JSON-RPC](https://www.jsonrpc.org/) is a standard which wraps a method
call in a `JSON<class_JSON>`{.interpreted-text role="ref"} object. The
object has a particular structure and identifies which method is called,
the parameters to that function, and carries an ID to keep track of
responses. This class implements that standard on top of
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}; you will
have to convert between a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} and
`JSON<class_JSON>`{.interpreted-text role="ref"} with other functions.

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

:::: {#enum_JSONRPC_ErrorCode}
::: rst-class
classref-enumeration
:::
::::

enum **ErrorCode**: `🔗<enum_JSONRPC_ErrorCode>`{.interpreted-text
role="ref"}

:::: {#class_JSONRPC_constant_PARSE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorCode<enum_JSONRPC_ErrorCode>`{.interpreted-text role="ref"}
**PARSE_ERROR** = `-32700`

The request could not be parsed as it was not valid by JSON standard
(`JSON.parse()<class_JSON_method_parse>`{.interpreted-text role="ref"}
failed).

:::: {#class_JSONRPC_constant_INVALID_REQUEST}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorCode<enum_JSONRPC_ErrorCode>`{.interpreted-text role="ref"}
**INVALID_REQUEST** = `-32600`

A method call was requested but the request\'s format is not valid.

:::: {#class_JSONRPC_constant_METHOD_NOT_FOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorCode<enum_JSONRPC_ErrorCode>`{.interpreted-text role="ref"}
**METHOD_NOT_FOUND** = `-32601`

A method call was requested but no function of that name existed in the
JSONRPC subclass.

:::: {#class_JSONRPC_constant_INVALID_PARAMS}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorCode<enum_JSONRPC_ErrorCode>`{.interpreted-text role="ref"}
**INVALID_PARAMS** = `-32602`

A method call was requested but the given method parameters are not
valid. Not used by the built-in JSONRPC.

:::: {#class_JSONRPC_constant_INTERNAL_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorCode<enum_JSONRPC_ErrorCode>`{.interpreted-text role="ref"}
**INTERNAL_ERROR** = `-32603`

An internal error occurred while processing the request. Not used by the
built-in JSONRPC.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_JSONRPC_method_make_notification}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**make_notification**(method: `String<class_String>`{.interpreted-text
role="ref"}, params: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_JSONRPC_method_make_notification>`{.interpreted-text
role="ref"}

Returns a dictionary in the form of a JSON-RPC notification.
Notifications are one-shot messages which do not expect a response.

- `method`: Name of the method being called.
- `params`: An array or dictionary of parameters being passed to the
  method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSONRPC_method_make_request}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**make_request**(method: `String<class_String>`{.interpreted-text
role="ref"}, params: `Variant<class_Variant>`{.interpreted-text
role="ref"}, id: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_JSONRPC_method_make_request>`{.interpreted-text role="ref"}

Returns a dictionary in the form of a JSON-RPC request. Requests are
sent to a server with the expectation of a response. The ID field is
used for the server to specify which exact request it is responding to.

- `method`: Name of the method being called.
- `params`: An array or dictionary of parameters being passed to the
  method.
- `id`: Uniquely identifies this request. The server is expected to send
  a response with the same ID.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSONRPC_method_make_response}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**make_response**(result: `Variant<class_Variant>`{.interpreted-text
role="ref"}, id: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_JSONRPC_method_make_response>`{.interpreted-text role="ref"}

When a server has received and processed a request, it is expected to
send a response. If you did not want a response then you need to have
sent a Notification instead.

- `result`: The return value of the function which was called.
- `id`: The ID of the request this response is targeted to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSONRPC_method_make_response_error}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**make_response_error**(code: `int<class_int>`{.interpreted-text
role="ref"}, message: `String<class_String>`{.interpreted-text
role="ref"}, id: `Variant<class_Variant>`{.interpreted-text role="ref"}
= null)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_JSONRPC_method_make_response_error>`{.interpreted-text
role="ref"}

Creates a response which indicates a previous reply has failed in some
way.

- `code`: The error code corresponding to what kind of error this is.
  See the `ErrorCode<enum_JSONRPC_ErrorCode>`{.interpreted-text
  role="ref"} constants.
- `message`: A custom message about this error.
- `id`: The request this error is a response to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSONRPC_method_process_action}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**process_action**(action: `Variant<class_Variant>`{.interpreted-text
role="ref"}, recurse: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_JSONRPC_method_process_action>`{.interpreted-text
role="ref"}

Given a Dictionary which takes the form of a JSON-RPC request: unpack
the request and run it. Methods are resolved by looking at the field
called \"method\" and looking for an equivalently named function in the
JSONRPC object. If one is found that method is called.

To add new supported methods extend the JSONRPC class and call
`process_action()<class_JSONRPC_method_process_action>`{.interpreted-text
role="ref"} on your subclass.

`action`: The action to be run, as a Dictionary in the form of a
JSON-RPC request or notification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSONRPC_method_process_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**process_string**(action: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_JSONRPC_method_process_string>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JSONRPC_method_set_method}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_method**(name: `String<class_String>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"}) `🔗<class_JSONRPC_method_set_method>`{.interpreted-text
role="ref"}

Registers a callback for the given method name.

- `name` The name that clients can use to access the callback.
- `callback` The callback which will handle the specific method.
