github_url
:   hide

# ScriptEditorBase {#class_ScriptEditorBase}

**Inherits:** `VBoxContainer<class_VBoxContainer>`{.interpreted-text
role="ref"} **\<** `BoxContainer<class_BoxContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base editor for editing scripts in the
`ScriptEditor<class_ScriptEditor>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Base editor for editing scripts in the
`ScriptEditor<class_ScriptEditor>`{.interpreted-text role="ref"}. This
does not include documentation items.

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

:::: {#class_ScriptEditorBase_signal_edited_script_changed}
::: rst-class
classref-signal
:::
::::

**edited_script_changed**()
`🔗<class_ScriptEditorBase_signal_edited_script_changed>`{.interpreted-text
role="ref"}

Emitted after script validation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_go_to_help}
::: rst-class
classref-signal
:::
::::

**go_to_help**(what: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ScriptEditorBase_signal_go_to_help>`{.interpreted-text
role="ref"}

Emitted when the user requests a specific documentation page.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_go_to_method}
::: rst-class
classref-signal
:::
::::

**go_to_method**(script: `Object<class_Object>`{.interpreted-text
role="ref"}, method: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ScriptEditorBase_signal_go_to_method>`{.interpreted-text
role="ref"}

Emitted when the user requests to view a specific method of a script,
similar to
`request_open_script_at_line<class_ScriptEditorBase_signal_request_open_script_at_line>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_name_changed}
::: rst-class
classref-signal
:::
::::

**name_changed**()
`🔗<class_ScriptEditorBase_signal_name_changed>`{.interpreted-text
role="ref"}

Emitted after script validation or when the edited resource has changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_replace_in_files_requested}
::: rst-class
classref-signal
:::
::::

**replace_in_files_requested**(text:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditorBase_signal_replace_in_files_requested>`{.interpreted-text
role="ref"}

Emitted when the user request to find and replace text in the file
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_request_help}
::: rst-class
classref-signal
:::
::::

**request_help**(topic: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ScriptEditorBase_signal_request_help>`{.interpreted-text
role="ref"}

Emitted when the user requests contextual help.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_request_open_script_at_line}
::: rst-class
classref-signal
:::
::::

**request_open_script_at_line**(script:
`Object<class_Object>`{.interpreted-text role="ref"}, line:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditorBase_signal_request_open_script_at_line>`{.interpreted-text
role="ref"}

Emitted when the user requests to view a specific line of a script,
similar to
`go_to_method<class_ScriptEditorBase_signal_go_to_method>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_request_save_history}
::: rst-class
classref-signal
:::
::::

**request_save_history**()
`🔗<class_ScriptEditorBase_signal_request_save_history>`{.interpreted-text
role="ref"}

Emitted when the user contextual goto and the item is in the same
script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_request_save_previous_state}
::: rst-class
classref-signal
:::
::::

**request_save_previous_state**(state:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditorBase_signal_request_save_previous_state>`{.interpreted-text
role="ref"}

Emitted when the user changes current script or moves caret by 10 or
more columns within the same script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_signal_search_in_files_requested}
::: rst-class
classref-signal
:::
::::

**search_in_files_requested**(text:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ScriptEditorBase_signal_search_in_files_requested>`{.interpreted-text
role="ref"}

Emitted when the user request to search text in the file system.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ScriptEditorBase_method_add_syntax_highlighter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_syntax_highlighter**(highlighter:
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"})
`🔗<class_ScriptEditorBase_method_add_syntax_highlighter>`{.interpreted-text
role="ref"}

Adds an
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"} to the open script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ScriptEditorBase_method_get_base_editor}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**get_base_editor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ScriptEditorBase_method_get_base_editor>`{.interpreted-text
role="ref"}

Returns the underlying `Control<class_Control>`{.interpreted-text
role="ref"} used for editing scripts. For text scripts, this is a
`CodeEdit<class_CodeEdit>`{.interpreted-text role="ref"}.
