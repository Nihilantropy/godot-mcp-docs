github_url
:   hide

# Logger {#class_Logger}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Custom logger to receive messages from the internal error/warning
stream.

::: rst-class
classref-introduction-group
:::

## Description

Custom logger to receive messages from the internal error/warning
stream. Loggers are registered via
`OS.add_logger()<class_OS_method_add_logger>`{.interpreted-text
role="ref"}.

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

:::: {#enum_Logger_ErrorType}
::: rst-class
classref-enumeration
:::
::::

enum **ErrorType**: `🔗<enum_Logger_ErrorType>`{.interpreted-text
role="ref"}

:::: {#class_Logger_constant_ERROR_TYPE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorType<enum_Logger_ErrorType>`{.interpreted-text role="ref"}
**ERROR_TYPE_ERROR** = `0`

The message received is an error.

:::: {#class_Logger_constant_ERROR_TYPE_WARNING}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorType<enum_Logger_ErrorType>`{.interpreted-text role="ref"}
**ERROR_TYPE_WARNING** = `1`

The message received is a warning.

:::: {#class_Logger_constant_ERROR_TYPE_SCRIPT}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorType<enum_Logger_ErrorType>`{.interpreted-text role="ref"}
**ERROR_TYPE_SCRIPT** = `2`

The message received is a script error.

:::: {#class_Logger_constant_ERROR_TYPE_SHADER}
::: rst-class
classref-enumeration-constant
:::
::::

`ErrorType<enum_Logger_ErrorType>`{.interpreted-text role="ref"}
**ERROR_TYPE_SHADER** = `3`

The message received is a shader error.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Logger_private_method__log_error}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_log_error**(function: `String<class_String>`{.interpreted-text
role="ref"}, file: `String<class_String>`{.interpreted-text role="ref"},
line: `int<class_int>`{.interpreted-text role="ref"}, code:
`String<class_String>`{.interpreted-text role="ref"}, rationale:
`String<class_String>`{.interpreted-text role="ref"}, editor_notify:
`bool<class_bool>`{.interpreted-text role="ref"}, error_type:
`int<class_int>`{.interpreted-text role="ref"}, script_backtraces:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`ScriptBacktrace<class_ScriptBacktrace>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Logger_private_method__log_error>`{.interpreted-text
role="ref"}

Called when an error is logged. The error provides the `function`,
`file`, and `line` that it originated from, as well as either the `code`
that generated the error or a `rationale`.

The type of error provided by `error_type` is described in the
`ErrorType<enum_Logger_ErrorType>`{.interpreted-text role="ref"}
enumeration.

Additionally, `script_backtraces` provides backtraces for each of the
script languages. These will only contain stack frames in editor builds
and debug builds by default. To enable them for release builds as well,
you need to enable
`ProjectSettings.debug/settings/gdscript/always_track_call_stacks<class_ProjectSettings_property_debug/settings/gdscript/always_track_call_stacks>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* This function may be called from multiple different
threads, so you may need to do your own locking.

\*\*Note:\*\* `script_backtraces` will not contain any captured
variables, due to its prohibitively high cost. To get those you will
need to capture the backtraces yourself, from within the **Logger**
virtual methods, using
`Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Logger_private_method__log_message}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_log_message**(message: `String<class_String>`{.interpreted-text
role="ref"}, error: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Logger_private_method__log_message>`{.interpreted-text
role="ref"}

Called when a message is logged. If `error` is `true`, then this message
was meant to be sent to `stderr`.

\*\*Warning:\*\* This function may be called from multiple different
threads, so you may need to do your own locking.
