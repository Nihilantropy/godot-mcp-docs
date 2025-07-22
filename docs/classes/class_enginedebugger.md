github_url
:   hide

# EngineDebugger {#class_EngineDebugger}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Exposes the internal debugger.

::: rst-class
classref-introduction-group
:::

## Description

**EngineDebugger** handles the communication between the editor and the
running game. It is active in the running game. Messages can be
sent/received through it. It also manages the profilers.

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

## Method Descriptions

:::: {#class_EngineDebugger_method_clear_breakpoints}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_breakpoints**()
`🔗<class_EngineDebugger_method_clear_breakpoints>`{.interpreted-text
role="ref"}

Clears all breakpoints.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_debug}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**debug**(can_continue: `bool<class_bool>`{.interpreted-text role="ref"}
= true, is_error_breakpoint: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_EngineDebugger_method_debug>`{.interpreted-text role="ref"}

Starts a debug break in script execution, optionally specifying whether
the program can continue based on `can_continue` and whether the break
was due to a breakpoint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_get_depth}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_depth**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EngineDebugger_method_get_depth>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Returns the current debug depth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_get_lines_left}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_lines_left**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EngineDebugger_method_get_lines_left>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Returns the number of lines that remain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_has_capture}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_capture**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_has_capture>`{.interpreted-text
role="ref"}

Returns `true` if a capture with the given name is present otherwise
`false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_has_profiler}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_profiler**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_has_profiler>`{.interpreted-text
role="ref"}

Returns `true` if a profiler with the given name is present otherwise
`false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_insert_breakpoint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**insert_breakpoint**(line: `int<class_int>`{.interpreted-text
role="ref"}, source: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_EngineDebugger_method_insert_breakpoint>`{.interpreted-text
role="ref"}

Inserts a new breakpoint with the given `source` and `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_active**()
`🔗<class_EngineDebugger_method_is_active>`{.interpreted-text
role="ref"}

Returns `true` if the debugger is active otherwise `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_is_breakpoint}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_breakpoint**(line:
`int<class_int>`{.interpreted-text role="ref"}, source:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EngineDebugger_method_is_breakpoint>`{.interpreted-text
role="ref"}

Returns `true` if the given `source` and `line` represent an existing
breakpoint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_is_profiling}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_profiling**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_is_profiling>`{.interpreted-text
role="ref"}

Returns `true` if a profiler with the given name is present and active
otherwise `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_is_skipping_breakpoints}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_skipping_breakpoints**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EngineDebugger_method_is_skipping_breakpoints>`{.interpreted-text
role="ref"}

Returns `true` if the debugger is skipping breakpoints otherwise
`false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_line_poll}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **line_poll**()
`🔗<class_EngineDebugger_method_line_poll>`{.interpreted-text
role="ref"}

Forces a processing loop of debugger events. The purpose of this method
is just processing events every now and then when the script might get
too busy, so that bugs like infinite loops can be caught.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_profiler_add_frame_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**profiler_add_frame_data**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, data:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_profiler_add_frame_data>`{.interpreted-text
role="ref"}

Calls the `add` callable of the profiler with given `name` and `data`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_profiler_enable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**profiler_enable**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"}, arguments:
`Array<class_Array>`{.interpreted-text role="ref"} = \[\])
`🔗<class_EngineDebugger_method_profiler_enable>`{.interpreted-text
role="ref"}

Calls the `toggle` callable of the profiler with given `name` and
`arguments`. Enables/Disables the same profiler depending on `enable`
argument.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_register_message_capture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_message_capture**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_register_message_capture>`{.interpreted-text
role="ref"}

Registers a message capture with given `name`. If `name` is
\"my_message\" then messages starting with \"my_message:\" will be
called with the given callable.

The callable must accept a message string and a data array as argument.
The callable should return `true` if the message is recognized.

\*\*Note:\*\* The callable will receive the message with the prefix
stripped, unlike
`EditorDebuggerPlugin._capture()<class_EditorDebuggerPlugin_private_method__capture>`{.interpreted-text
role="ref"}. See the
`EditorDebuggerPlugin<class_EditorDebuggerPlugin>`{.interpreted-text
role="ref"} description for an example.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_register_profiler}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_profiler**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, profiler:
`EngineProfiler<class_EngineProfiler>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_register_profiler>`{.interpreted-text
role="ref"}

Registers a profiler with the given `name`. See
`EngineProfiler<class_EngineProfiler>`{.interpreted-text role="ref"} for
more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_remove_breakpoint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_breakpoint**(line: `int<class_int>`{.interpreted-text
role="ref"}, source: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_EngineDebugger_method_remove_breakpoint>`{.interpreted-text
role="ref"}

Removes a breakpoint with the given `source` and `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_script_debug}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**script_debug**(language:
`ScriptLanguage<class_ScriptLanguage>`{.interpreted-text role="ref"},
can_continue: `bool<class_bool>`{.interpreted-text role="ref"} = true,
is_error_breakpoint: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_EngineDebugger_method_script_debug>`{.interpreted-text
role="ref"}

Starts a debug break in script execution, optionally specifying whether
the program can continue based on `can_continue` and whether the break
was due to a breakpoint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_send_message}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**send_message**(message: `String<class_String>`{.interpreted-text
role="ref"}, data: `Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_send_message>`{.interpreted-text
role="ref"}

Sends a message with given `message` and `data` array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_set_depth}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_depth**(depth: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_set_depth>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Sets the current debugging depth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_set_lines_left}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_lines_left**(lines: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_EngineDebugger_method_set_lines_left>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Sets the current debugging lines that remain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_unregister_message_capture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unregister_message_capture**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_unregister_message_capture>`{.interpreted-text
role="ref"}

Unregisters the message capture with given `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineDebugger_method_unregister_profiler}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unregister_profiler**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EngineDebugger_method_unregister_profiler>`{.interpreted-text
role="ref"}

Unregisters a profiler with given `name`.
