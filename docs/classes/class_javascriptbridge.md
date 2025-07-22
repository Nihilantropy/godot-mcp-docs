github_url
:   hide

# JavaScriptBridge {#class_JavaScriptBridge}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Singleton that connects the engine with the browser\'s JavaScript
context in Web export.

::: rst-class
classref-introduction-group
:::

## Description

The JavaScriptBridge singleton is implemented only in the Web export.
It\'s used to access the browser\'s JavaScript context. This allows
interaction with embedding pages or calling third-party JavaScript APIs.

\*\*Note:\*\* This singleton can be disabled at build-time to improve
security. By default, the JavaScriptBridge singleton is enabled.
Official export templates also have the JavaScriptBridge singleton
enabled. See
`Compiling for the Web <../contributing/development/compiling/compiling_for_web>`{.interpreted-text
role="doc"} in the documentation for more information.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Exporting for the Web: Calling JavaScript from
  script](../tutorials/export/exporting_for_web.html#calling-javascript-from-script)

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

:::: {#class_JavaScriptBridge_signal_pwa_update_available}
::: rst-class
classref-signal
:::
::::

**pwa_update_available**()
`🔗<class_JavaScriptBridge_signal_pwa_update_available>`{.interpreted-text
role="ref"}

Emitted when an update for this progressive web app has been detected
but is waiting to be activated because a previous version is active. See
`pwa_update()<class_JavaScriptBridge_method_pwa_update>`{.interpreted-text
role="ref"} to force the update to take place immediately.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_JavaScriptBridge_method_create_callback}
::: rst-class
classref-method
:::
::::

`JavaScriptObject<class_JavaScriptObject>`{.interpreted-text role="ref"}
**create_callback**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_JavaScriptBridge_method_create_callback>`{.interpreted-text
role="ref"}

Creates a reference to a `Callable<class_Callable>`{.interpreted-text
role="ref"} that can be used as a callback by JavaScript. The reference
must be kept until the callback happens, or it won\'t be called at all.
See `JavaScriptObject<class_JavaScriptObject>`{.interpreted-text
role="ref"} for usage.

\*\*Note:\*\* The callback function must take exactly one
`Array<class_Array>`{.interpreted-text role="ref"} argument, which is
going to be the JavaScript [arguments
object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
converted to an array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_create_object}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**create_object**(object: `String<class_String>`{.interpreted-text
role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_JavaScriptBridge_method_create_object>`{.interpreted-text
role="ref"}

Creates a new JavaScript object using the `new` constructor. The
`object` must a valid property of the JavaScript `window`. See
`JavaScriptObject<class_JavaScriptObject>`{.interpreted-text role="ref"}
for usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_download_buffer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**download_buffer**(buffer:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
name: `String<class_String>`{.interpreted-text role="ref"}, mime:
`String<class_String>`{.interpreted-text role="ref"} =
\"application/octet-stream\")
`🔗<class_JavaScriptBridge_method_download_buffer>`{.interpreted-text
role="ref"}

Prompts the user to download a file containing the specified `buffer`.
The file will have the given `name` and `mime` type.

\*\*Note:\*\* The browser may override the [MIME
type](https://en.wikipedia.org/wiki/Media_type) provided based on the
file `name`\'s extension.

\*\*Note:\*\* Browsers might block the download if
`download_buffer()<class_JavaScriptBridge_method_download_buffer>`{.interpreted-text
role="ref"} is not being called from a user interaction (e.g. button
click).

\*\*Note:\*\* Browsers might ask the user for permission or block the
download if multiple download requests are made in a quick succession.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_eval}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **eval**(code:
`String<class_String>`{.interpreted-text role="ref"},
use_global_execution_context: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_JavaScriptBridge_method_eval>`{.interpreted-text role="ref"}

Execute the string `code` as JavaScript code within the browser window.
This is a call to the actual global JavaScript function `eval()`.

If `use_global_execution_context` is `true`, the code will be evaluated
in the global execution context. Otherwise, it is evaluated in the
execution context of a function within the engine\'s runtime
environment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_force_fs_sync}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_fs_sync**()
`🔗<class_JavaScriptBridge_method_force_fs_sync>`{.interpreted-text
role="ref"}

Force synchronization of the persistent file system (when enabled).

\*\*Note:\*\* This is only useful for modules or extensions that can\'t
use `FileAccess<class_FileAccess>`{.interpreted-text role="ref"} to
write files.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_get_interface}
::: rst-class
classref-method
:::
::::

`JavaScriptObject<class_JavaScriptObject>`{.interpreted-text role="ref"}
**get_interface**(interface: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_JavaScriptBridge_method_get_interface>`{.interpreted-text
role="ref"}

Returns an interface to a JavaScript object that can be used by scripts.
The `interface` must be a valid property of the JavaScript `window`. The
callback must accept a single `Array<class_Array>`{.interpreted-text
role="ref"} argument, which will contain the JavaScript `arguments`. See
`JavaScriptObject<class_JavaScriptObject>`{.interpreted-text role="ref"}
for usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_is_js_buffer}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_js_buffer**(javascript_object:
`JavaScriptObject<class_JavaScriptObject>`{.interpreted-text
role="ref"})
`🔗<class_JavaScriptBridge_method_is_js_buffer>`{.interpreted-text
role="ref"}

Returns `true` if the given `javascript_object` is of type
[\[code\]ArrayBuffer\[/code\]](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer),
[\[code\]DataView\[/code\]](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/DataView),
or one of the many [typed array
objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_js_buffer_to_packed_byte_array}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**js_buffer_to_packed_byte_array**(javascript_buffer:
`JavaScriptObject<class_JavaScriptObject>`{.interpreted-text
role="ref"})
`🔗<class_JavaScriptBridge_method_js_buffer_to_packed_byte_array>`{.interpreted-text
role="ref"}

Returns a copy of `javascript_buffer`\'s contents as a
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}.
See also
`is_js_buffer()<class_JavaScriptBridge_method_is_js_buffer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_pwa_needs_update}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pwa_needs_update**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_JavaScriptBridge_method_pwa_needs_update>`{.interpreted-text
role="ref"}

Returns `true` if a new version of the progressive web app is waiting to
be activated.

\*\*Note:\*\* Only relevant when exported as a Progressive Web App.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_JavaScriptBridge_method_pwa_update}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**pwa_update**()
`🔗<class_JavaScriptBridge_method_pwa_update>`{.interpreted-text
role="ref"}

Performs the live update of the progressive web app. Forcing the new
version to be installed and the page to be reloaded.

\*\*Note:\*\* Your application will be **reloaded in all browser tabs**.

\*\*Note:\*\* Only relevant when exported as a Progressive Web App and
`pwa_needs_update()<class_JavaScriptBridge_method_pwa_needs_update>`{.interpreted-text
role="ref"} returns `true`.
