github_url
:   hide

# EditorDebuggerPlugin {#class_EditorDebuggerPlugin}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A base class to implement debugger plugins.

::: rst-class
classref-introduction-group
:::

## Description

**EditorDebuggerPlugin** provides functions related to the editor side
of the debugger.

To interact with the debugger, an instance of this class must be added
to the editor via
`EditorPlugin.add_debugger_plugin()<class_EditorPlugin_method_add_debugger_plugin>`{.interpreted-text
role="ref"}.

Once added, the
`_setup_session()<class_EditorDebuggerPlugin_private_method__setup_session>`{.interpreted-text
role="ref"} callback will be called for every
`EditorDebuggerSession<class_EditorDebuggerSession>`{.interpreted-text
role="ref"} available to the plugin, and when new ones are created (the
sessions may be inactive during this stage).

You can retrieve the available
`EditorDebuggerSession<class_EditorDebuggerSession>`{.interpreted-text
role="ref"}s via
`get_sessions()<class_EditorDebuggerPlugin_method_get_sessions>`{.interpreted-text
role="ref"} or get a specific one via
`get_session()<class_EditorDebuggerPlugin_method_get_session>`{.interpreted-text
role="ref"}.

:::: tabs
::: code-tab
gdscript

\@tool extends EditorPlugin

class ExampleEditorDebugger extends EditorDebuggerPlugin:

> 
>
> func [has_capture]{#has_capture}(capture):
>
> :   \# Return true if you wish to handle messages with the prefix
>     \"my_plugin:\". return capture == \"my_plugin\"
>
> func [capture]{#capture}(message, data, session_id):
>
> :   
>
>     if message == \"my_plugin:ping\":
>
>     :   get_session(session_id).send_message(\"my_plugin:echo\", data)
>         return true
>
>     return false
>
> func [setup_session]{#setup_session}(session_id):
>
> :   \# Add a new tab in the debugger session UI containing a label.
>     var label = Label.new() label.name = \"Example plugin\" \# Will be
>     used as the tab title. label.text = \"Example plugin\" var session
>     = get_session(session_id) \# Listens to the session started and
>     stopped signals. session.started.connect(func (): print(\"Session
>     started\")) session.stopped.connect(func (): print(\"Session
>     stopped\")) session.add_session_tab(label)

var debugger = ExampleEditorDebugger.new()

func [enter_tree]{#enter_tree}():

:   add_debugger_plugin(debugger)

func [exit_tree]{#exit_tree}():

:   remove_debugger_plugin(debugger)
:::
::::

To connect on the running game side, use the
`EngineDebugger<class_EngineDebugger>`{.interpreted-text role="ref"}
singleton:

:::: tabs
::: code-tab
gdscript

extends Node

func [ready]{#ready}():

:   EngineDebugger.register_message_capture(\"my_plugin\",
    [capture]{#capture}) EngineDebugger.send_message(\"my_plugin:ping\",
    \[\"test\"\])

func [capture]{#capture}(message, data):

:   \# Note that the \"my_plugin:\" prefix is not used here. if message
    == \"echo\": prints(\"Echo received:\", data) return true return
    false
:::
::::

\*\*Note:\*\* While the game is running,
`@GlobalScope.print()<class_@GlobalScope_method_print>`{.interpreted-text
role="ref"} and similar functions *called in the editor* do not print
anything, the Output Log prints only game messages.

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

:::: {#class_EditorDebuggerPlugin_private_method__breakpoint_set_in_tree}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_breakpoint_set_in_tree**(script:
`Script<class_Script>`{.interpreted-text role="ref"}, line:
`int<class_int>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorDebuggerPlugin_private_method__breakpoint_set_in_tree>`{.interpreted-text
role="ref"}

Override this method to be notified when a breakpoint is set in the
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerPlugin_private_method__breakpoints_cleared_in_tree}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_breakpoints_cleared_in_tree**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorDebuggerPlugin_private_method__breakpoints_cleared_in_tree>`{.interpreted-text
role="ref"}

Override this method to be notified when all breakpoints are cleared in
the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerPlugin_private_method__capture}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_capture**(message:
`String<class_String>`{.interpreted-text role="ref"}, data:
`Array<class_Array>`{.interpreted-text role="ref"}, session_id:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorDebuggerPlugin_private_method__capture>`{.interpreted-text
role="ref"}

Override this method to process incoming messages. The `session_id` is
the ID of the
`EditorDebuggerSession<class_EditorDebuggerSession>`{.interpreted-text
role="ref"} that received the `message`. Use
`get_session()<class_EditorDebuggerPlugin_method_get_session>`{.interpreted-text
role="ref"} to retrieve the session. This method should return `true` if
the message is recognized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerPlugin_private_method__goto_script_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_goto_script_line**(script: `Script<class_Script>`{.interpreted-text
role="ref"}, line: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorDebuggerPlugin_private_method__goto_script_line>`{.interpreted-text
role="ref"}

Override this method to be notified when a breakpoint line has been
clicked in the debugger breakpoint panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerPlugin_private_method__has_capture}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_has_capture**(capture: `String<class_String>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorDebuggerPlugin_private_method__has_capture>`{.interpreted-text
role="ref"}

Override this method to enable receiving messages from the debugger. If
`capture` is \"my_message\" then messages starting with \"my_message:\"
will be passed to the
`_capture()<class_EditorDebuggerPlugin_private_method__capture>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerPlugin_private_method__setup_session}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_setup_session**(session_id: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorDebuggerPlugin_private_method__setup_session>`{.interpreted-text
role="ref"}

Override this method to be notified whenever a new
`EditorDebuggerSession<class_EditorDebuggerSession>`{.interpreted-text
role="ref"} is created. Note that the session may be inactive during
this stage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerPlugin_method_get_session}
::: rst-class
classref-method
:::
::::

`EditorDebuggerSession<class_EditorDebuggerSession>`{.interpreted-text
role="ref"} **get_session**(id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_EditorDebuggerPlugin_method_get_session>`{.interpreted-text
role="ref"}

Returns the
`EditorDebuggerSession<class_EditorDebuggerSession>`{.interpreted-text
role="ref"} with the given `id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorDebuggerPlugin_method_get_sessions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_sessions**()
`🔗<class_EditorDebuggerPlugin_method_get_sessions>`{.interpreted-text
role="ref"}

Returns an array of
`EditorDebuggerSession<class_EditorDebuggerSession>`{.interpreted-text
role="ref"} currently available to this debugger plugin.

\*\*Note:\*\* Sessions in the array may be inactive, check their state
via
`EditorDebuggerSession.is_active()<class_EditorDebuggerSession_method_is_active>`{.interpreted-text
role="ref"}.
