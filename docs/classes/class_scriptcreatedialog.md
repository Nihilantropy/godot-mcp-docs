github_url
:   hide

# ScriptCreateDialog {#class_ScriptCreateDialog}

**Inherits:**
`ConfirmationDialog<class_ConfirmationDialog>`{.interpreted-text
role="ref"} **\<** `AcceptDialog<class_AcceptDialog>`{.interpreted-text
role="ref"} **\<** `Window<class_Window>`{.interpreted-text role="ref"}
**\<** `Viewport<class_Viewport>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Godot editor\'s popup dialog for creating new
`Script<class_Script>`{.interpreted-text role="ref"} files.

::: rst-class
classref-introduction-group
:::

## Description

The **ScriptCreateDialog** creates script files according to a given
template for a given scripting language. The standard use is to
configure its fields prior to calling one of the
`Window.popup()<class_Window_method_popup>`{.interpreted-text
role="ref"} methods.

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var dialog = ScriptCreateDialog.new(); dialog.config(\"Node\",
    \"res://new_node.gd\") \# For in-engine types.
    dialog.config(\"\"res://base_node.gd\"\", \"res://derived_node.gd\")
    \# For script types. dialog.popup_centered()
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { var dialog = new
ScriptCreateDialog(); dialog.Config(\"Node\", \"res://NewNode.cs\"); //
For in-engine types. dialog.Config(\"\"res://BaseNode.cs\"\",
\"res://DerivedNode.cs\"); // For script types. dialog.PopupCentered();
}
:::
:::::

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

:::: {#class_ScriptCreateDialog_signal_script_created}
::: rst-class
classref-signal
:::
::::

**script_created**(script: `Script<class_Script>`{.interpreted-text
role="ref"})
`🔗<class_ScriptCreateDialog_signal_script_created>`{.interpreted-text
role="ref"}

Emitted when the user clicks the OK button.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ScriptCreateDialog_method_config}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**config**(inherits: `String<class_String>`{.interpreted-text
role="ref"}, path: `String<class_String>`{.interpreted-text role="ref"},
built_in_enabled: `bool<class_bool>`{.interpreted-text role="ref"} =
true, load_enabled: `bool<class_bool>`{.interpreted-text role="ref"} =
true) `🔗<class_ScriptCreateDialog_method_config>`{.interpreted-text
role="ref"}

Prefills required fields to configure the ScriptCreateDialog for use.
