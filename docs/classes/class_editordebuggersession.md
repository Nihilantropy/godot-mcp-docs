github_url
:   hide

# EditorDebuggerSession {#class_EditorDebuggerSession}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A class to interact with the editor debugger.

::: rst-class
classref-introduction-group
:::

## Description

This class cannot be directly instantiated and must be retrieved via an
`EditorDebuggerPlugin<class_EditorDebuggerPlugin>`{.interpreted-text
role="ref"}.

You can add tabs to the session UI via
`add_session_tab()<class_EditorDebuggerSession_method_add_session_tab>`{.interpreted-text
role="ref"}, send messages via
`send_message()<class_EditorDebuggerSession_method_send_message>`{.interpreted-text
role="ref"}, and toggle
`EngineProfiler<class_EngineProfiler>`{.interpreted-text role="ref"}s
via
`toggle_profiler()<class_EditorDebuggerSession_method_toggle_profiler>`{.interpreted-text
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

## Signals

:::: {#class_EditorDebuggerSession_signal_breaked}
::: rst-class
classref-signal
:::
::::

**breaked**(can_debug: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorDebuggerSession_signal_breaked>`{.interpreted-text
role="ref"}

Emitted when the attached remote instance enters a break state. If
`can_debug` is `true`, the remote instance will enter the debug loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_signal_continued}
::: rst-class
classref-signal
:::
::::

**continued**()
`🔗<class_EditorDebuggerSession_signal_continued>`{.interpreted-text
role="ref"}

Emitted when the attached remote instance exits a break state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_signal_started}
::: rst-class
classref-signal
:::
::::

**started**()
`🔗<class_EditorDebuggerSession_signal_started>`{.interpreted-text
role="ref"}

Emitted when a remote instance is attached to this session (i.e. the
session becomes active).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_signal_stopped}
::: rst-class
classref-signal
:::
::::

**stopped**()
`🔗<class_EditorDebuggerSession_signal_stopped>`{.interpreted-text
role="ref"}

Emitted when a remote instance is detached from this session (i.e. the
session becomes inactive).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorDebuggerSession_method_add_session_tab}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_session_tab**(control: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_EditorDebuggerSession_method_add_session_tab>`{.interpreted-text
role="ref"}

Adds the given `control` to the debug session UI in the debugger bottom
panel. The `control`\'s node name will be used as the tab title.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_method_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_active**()
`🔗<class_EditorDebuggerSession_method_is_active>`{.interpreted-text
role="ref"}

Returns `true` if the debug session is currently attached to a remote
instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_method_is_breaked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_breaked**()
`🔗<class_EditorDebuggerSession_method_is_breaked>`{.interpreted-text
role="ref"}

Returns `true` if the attached remote instance is currently in the debug
loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_method_is_debuggable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_debuggable**()
`🔗<class_EditorDebuggerSession_method_is_debuggable>`{.interpreted-text
role="ref"}

Returns `true` if the attached remote instance can be debugged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_method_remove_session_tab}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_session_tab**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_EditorDebuggerSession_method_remove_session_tab>`{.interpreted-text
role="ref"}

Removes the given `control` from the debug session UI in the debugger
bottom panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_method_send_message}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**send_message**(message: `String<class_String>`{.interpreted-text
role="ref"}, data: `Array<class_Array>`{.interpreted-text role="ref"} =
\[\])
`🔗<class_EditorDebuggerSession_method_send_message>`{.interpreted-text
role="ref"}

Sends the given `message` to the attached remote instance, optionally
passing additionally `data`. See
`EngineDebugger<class_EngineDebugger>`{.interpreted-text role="ref"} for
how to retrieve those messages.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_method_set_breakpoint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_breakpoint**(path: `String<class_String>`{.interpreted-text
role="ref"}, line: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorDebuggerSession_method_set_breakpoint>`{.interpreted-text
role="ref"}

Enables or disables a specific breakpoint based on `enabled`, updating
the Editor Breakpoint Panel accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerSession_method_toggle_profiler}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**toggle_profiler**(profiler: `String<class_String>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"},
data: `Array<class_Array>`{.interpreted-text role="ref"} = \[\])
`🔗<class_EditorDebuggerSession_method_toggle_profiler>`{.interpreted-text
role="ref"}

Toggle the given `profiler` on the attached remote instance, optionally
passing additionally `data`. See
`EngineProfiler<class_EngineProfiler>`{.interpreted-text role="ref"} for
more details.
