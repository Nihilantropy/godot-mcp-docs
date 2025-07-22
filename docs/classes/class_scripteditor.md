github_url
:   hide

# ScriptEditor {#class_ScriptEditor}

**Inherits:** `PanelContainer<class_PanelContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Godot editor\'s script editor.

::: rst-class
classref-introduction-group
:::

## Description

Godot editor\'s script editor.

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton using
`EditorInterface.get_script_editor()<class_EditorInterface_method_get_script_editor>`{.interpreted-text
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

:::: {#class_ScriptEditor_signal_editor_script_changed}
::: rst-class
classref-signal
:::
::::

**editor_script_changed**(script:
`Script<class_Script>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditor_signal_editor_script_changed>`{.interpreted-text
role="ref"}

Emitted when user changed active script. Argument is a freshly activated
`Script<class_Script>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_signal_script_close}
::: rst-class
classref-signal
:::
::::

**script_close**(script: `Script<class_Script>`{.interpreted-text
role="ref"})
`🔗<class_ScriptEditor_signal_script_close>`{.interpreted-text
role="ref"}

Emitted when editor is about to close the active script. Argument is a
`Script<class_Script>`{.interpreted-text role="ref"} that is going to be
closed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ScriptEditor_method_clear_docs_from_script}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_docs_from_script**(script:
`Script<class_Script>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditor_method_clear_docs_from_script>`{.interpreted-text
role="ref"}

Removes the documentation for the given `script`.

\*\*Note:\*\* This should be called whenever the script is changed to
keep the open documentation state up to date.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_get_breakpoints}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_breakpoints**()
`🔗<class_ScriptEditor_method_get_breakpoints>`{.interpreted-text
role="ref"}

Returns array of breakpoints.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_get_current_editor}
::: rst-class
classref-method
:::
::::

`ScriptEditorBase<class_ScriptEditorBase>`{.interpreted-text role="ref"}
**get_current_editor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptEditor_method_get_current_editor>`{.interpreted-text
role="ref"}

Returns the `ScriptEditorBase<class_ScriptEditorBase>`{.interpreted-text
role="ref"} object that the user is currently editing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_get_current_script}
::: rst-class
classref-method
:::
::::

`Script<class_Script>`{.interpreted-text role="ref"}
**get_current_script**()
`🔗<class_ScriptEditor_method_get_current_script>`{.interpreted-text
role="ref"}

Returns a `Script<class_Script>`{.interpreted-text role="ref"} that is
currently active in editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_get_open_script_editors}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`ScriptEditorBase<class_ScriptEditorBase>`{.interpreted-text
role="ref"}\] **get_open_script_editors**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptEditor_method_get_open_script_editors>`{.interpreted-text
role="ref"}

Returns an array with all
`ScriptEditorBase<class_ScriptEditorBase>`{.interpreted-text role="ref"}
objects which are currently open in editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_get_open_scripts}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Script<class_Script>`{.interpreted-text role="ref"}\]
**get_open_scripts**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptEditor_method_get_open_scripts>`{.interpreted-text
role="ref"}

Returns an array with all `Script<class_Script>`{.interpreted-text
role="ref"} objects which are currently open in editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_goto_help}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**goto_help**(topic: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_ScriptEditor_method_goto_help>`{.interpreted-text
role="ref"}

Opens help for the given topic. The `topic` is an encoded string that
controls which class, method, constant, signal, annotation, property, or
theme item should be focused.

The supported `topic` formats include `class_name:class`,
`class_method:class:method`, `class_constant:class:constant`,
`class_signal:class:signal`, `class_annotation:class:@annotation`,
`class_property:class:property`, and `class_theme_item:class:item`,
where `class` is the class name, `method` is the method name, `constant`
is the constant name, `signal` is the signal name, `annotation` is the
annotation name, `property` is the property name, and `item` is the
theme item.

    # Shows help for the Node class.
    class_name:Node
    # Shows help for the global min function.
    # Global objects are accessible in the `@GlobalScope` namespace, shown here.
    class_method:@GlobalScope:min
    # Shows help for get_viewport in the Node class.
    class_method:Node:get_viewport
    # Shows help for the Input constant MOUSE_BUTTON_MIDDLE.
    class_constant:Input:MOUSE_BUTTON_MIDDLE
    # Shows help for the BaseButton signal pressed.
    class_signal:BaseButton:pressed
    # Shows help for the CanvasItem property visible.
    class_property:CanvasItem:visible
    # Shows help for the GDScript annotation export.
    # Annotations should be prefixed with the `@` symbol in the descriptor, as shown here.
    class_annotation:@GDScript:@export
    # Shows help for the GraphNode theme item named panel_selected.
    class_theme_item:GraphNode:panel_selected

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_goto_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**goto_line**(line_number: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_ScriptEditor_method_goto_line>`{.interpreted-text
role="ref"}

Goes to the specified line in the current script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_open_script_create_dialog}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**open_script_create_dialog**(base_name:
`String<class_String>`{.interpreted-text role="ref"}, base_path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditor_method_open_script_create_dialog>`{.interpreted-text
role="ref"}

Opens the script create dialog. The script will extend `base_name`. The
file extension can be omitted from `base_path`. It will be added based
on the selected scripting language.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_register_syntax_highlighter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**register_syntax_highlighter**(syntax_highlighter:
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"})
`🔗<class_ScriptEditor_method_register_syntax_highlighter>`{.interpreted-text
role="ref"}

Registers the
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"} to the editor, the
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"} will be available on all open scripts.

\*\*Note:\*\* Does not apply to scripts that are already opened.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_unregister_syntax_highlighter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unregister_syntax_highlighter**(syntax_highlighter:
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"})
`🔗<class_ScriptEditor_method_unregister_syntax_highlighter>`{.interpreted-text
role="ref"}

Unregisters the
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"} from the editor.

\*\*Note:\*\* The
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"} will still be applied to scripts that are already opened.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditor_method_update_docs_from_script}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_docs_from_script**(script:
`Script<class_Script>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditor_method_update_docs_from_script>`{.interpreted-text
role="ref"}

Updates the documentation for the given `script`.

\*\*Note:\*\* This should be called whenever the script is changed to
keep the open documentation state up to date.
