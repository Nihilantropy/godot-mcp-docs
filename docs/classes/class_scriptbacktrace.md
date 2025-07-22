github_url
:   hide

# ScriptBacktrace {#class_ScriptBacktrace}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A captured backtrace of a specific script language.

::: rst-class
classref-introduction-group
:::

## Description

**ScriptBacktrace** holds an already captured backtrace of a specific
script language, such as GDScript or C#, which are captured using
`Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`{.interpreted-text
role="ref"}.

See
`ProjectSettings.debug/settings/gdscript/always_track_call_stacks<class_ProjectSettings_property_debug/settings/gdscript/always_track_call_stacks>`{.interpreted-text
role="ref"} and
`ProjectSettings.debug/settings/gdscript/always_track_local_variables<class_ProjectSettings_property_debug/settings/gdscript/always_track_local_variables>`{.interpreted-text
role="ref"} for ways of controlling the contents of this class.

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

:::: {#class_ScriptBacktrace_method_format}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**format**(indent_all: `int<class_int>`{.interpreted-text role="ref"} =
0, indent_frames: `int<class_int>`{.interpreted-text role="ref"} = 4)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ScriptBacktrace_method_format>`{.interpreted-text
role="ref"}

Converts the backtrace to a `String<class_String>`{.interpreted-text
role="ref"}, where the entire string will be indented by `indent_all`
number of spaces, and the individual stack frames will be additionally
indented by `indent_frames` number of spaces.

\*\*Note:\*\* Calling
`Object.to_string()<class_Object_method_to_string>`{.interpreted-text
role="ref"} on a **ScriptBacktrace** will produce the same output as
calling
`format()<class_ScriptBacktrace_method_format>`{.interpreted-text
role="ref"} with all parameters left at their default values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_frame_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_frame_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_frame_count>`{.interpreted-text
role="ref"}

Returns the number of stack frames in the backtrace.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_frame_file}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_frame_file**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_frame_file>`{.interpreted-text
role="ref"}

Returns the file name of the call site represented by the stack frame at
the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_frame_function}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_frame_function**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_frame_function>`{.interpreted-text
role="ref"}

Returns the name of the function called at the stack frame at the
specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_frame_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_frame_line**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_frame_line>`{.interpreted-text
role="ref"}

Returns the line number of the call site represented by the stack frame
at the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_global_variable_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_global_variable_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_global_variable_count>`{.interpreted-text
role="ref"}

Returns the number of global variables (e.g. autoload singletons) in the
backtrace.

\*\*Note:\*\* This will be non-zero only if the `include_variables`
parameter was `true` when capturing the backtrace with
`Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_global_variable_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_global_variable_name**(variable_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_global_variable_name>`{.interpreted-text
role="ref"}

Returns the name of the global variable at the specified index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_global_variable_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_global_variable_value**(variable_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_global_variable_value>`{.interpreted-text
role="ref"}

Returns the value of the global variable at the specified index.

\*\*Warning:\*\* With GDScript backtraces, the returned
`Variant<class_Variant>`{.interpreted-text role="ref"} will be the
variable\'s actual value, including any object references. This means
that storing the returned `Variant<class_Variant>`{.interpreted-text
role="ref"} will prevent any such object from being deallocated, so
it\'s generally recommended not to do so.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_language_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_language_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_language_name>`{.interpreted-text
role="ref"}

Returns the name of the script language that this backtrace was captured
from.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_local_variable_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_local_variable_count**(frame_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_local_variable_count>`{.interpreted-text
role="ref"}

Returns the number of local variables in the stack frame at the
specified index.

\*\*Note:\*\* This will be non-zero only if the `include_variables`
parameter was `true` when capturing the backtrace with
`Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_local_variable_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_local_variable_name**(frame_index:
`int<class_int>`{.interpreted-text role="ref"}, variable_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_local_variable_name>`{.interpreted-text
role="ref"}

Returns the name of the local variable at the specified `variable_index`
in the stack frame at the specified `frame_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_local_variable_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_local_variable_value**(frame_index:
`int<class_int>`{.interpreted-text role="ref"}, variable_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_local_variable_value>`{.interpreted-text
role="ref"}

Returns the value of the local variable at the specified
`variable_index` in the stack frame at the specified `frame_index`.

\*\*Warning:\*\* With GDScript backtraces, the returned
`Variant<class_Variant>`{.interpreted-text role="ref"} will be the
variable\'s actual value, including any object references. This means
that storing the returned `Variant<class_Variant>`{.interpreted-text
role="ref"} will prevent any such object from being deallocated, so
it\'s generally recommended not to do so.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_member_variable_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_member_variable_count**(frame_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_member_variable_count>`{.interpreted-text
role="ref"}

Returns the number of member variables in the stack frame at the
specified index.

\*\*Note:\*\* This will be non-zero only if the `include_variables`
parameter was `true` when capturing the backtrace with
`Engine.capture_script_backtraces()<class_Engine_method_capture_script_backtraces>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_member_variable_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_member_variable_name**(frame_index:
`int<class_int>`{.interpreted-text role="ref"}, variable_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_member_variable_name>`{.interpreted-text
role="ref"}

Returns the name of the member variable at the specified
`variable_index` in the stack frame at the specified `frame_index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_get_member_variable_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_member_variable_value**(frame_index:
`int<class_int>`{.interpreted-text role="ref"}, variable_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_get_member_variable_value>`{.interpreted-text
role="ref"}

Returns the value of the member variable at the specified
`variable_index` in the stack frame at the specified `frame_index`.

\*\*Warning:\*\* With GDScript backtraces, the returned
`Variant<class_Variant>`{.interpreted-text role="ref"} will be the
variable\'s actual value, including any object references. This means
that storing the returned `Variant<class_Variant>`{.interpreted-text
role="ref"} will prevent any such object from being deallocated, so
it\'s generally recommended not to do so.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptBacktrace_method_is_empty}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_empty**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptBacktrace_method_is_empty>`{.interpreted-text
role="ref"}

Returns `true` if the backtrace has no stack frames.
