github_url
:   hide

# EditorCommandPalette {#class_EditorCommandPalette}

**Inherits:**
`ConfirmationDialog<class_ConfirmationDialog>`{.interpreted-text
role="ref"} **\<** `AcceptDialog<class_AcceptDialog>`{.interpreted-text
role="ref"} **\<** `Window<class_Window>`{.interpreted-text role="ref"}
**\<** `Viewport<class_Viewport>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Godot editor\'s command palette.

::: rst-class
classref-introduction-group
:::

## Description

Object that holds all the available Commands and their shortcuts text.
These Commands can be accessed through **Editor \> Command Palette**
menu.

Command key names use slash delimiters to distinguish sections, for
example: `"example/command1"` then `example` will be the section name.

::::: tabs
::: code-tab
gdscript

var command_palette = EditorInterface.get_command_palette() \#
external_command is a function that will be called with the command is
executed. var command_callable = Callable(self,
\"external_command\").bind(arguments)
command_palette.add_command(\"command\",
\"test/command\",command_callable)
:::

::: code-tab
csharp

EditorCommandPalette commandPalette =
EditorInterface.Singleton.GetCommandPalette(); // ExternalCommand is a
function that will be called with the command is executed. Callable
commandCallable = new Callable(this, MethodName.ExternalCommand);
commandPalette.AddCommand(\"command\", \"test/command\",
commandCallable)
:::
:::::

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton using
`EditorInterface.get_command_palette()<class_EditorInterface_method_get_command_palette>`{.interpreted-text
role="ref"}.

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

## Method Descriptions

:::: {#class_EditorCommandPalette_method_add_command}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_command**(command_name: `String<class_String>`{.interpreted-text
role="ref"}, key_name: `String<class_String>`{.interpreted-text
role="ref"}, binded_callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, shortcut_text:
`String<class_String>`{.interpreted-text role="ref"} = \"None\")
`🔗<class_EditorCommandPalette_method_add_command>`{.interpreted-text
role="ref"}

Adds a custom command to EditorCommandPalette.

- `command_name`: `String<class_String>`{.interpreted-text role="ref"}
  (Name of the **Command**. This is displayed to the user.)
- `key_name`: `String<class_String>`{.interpreted-text role="ref"} (Name
  of the key for a particular **Command**. This is used to uniquely
  identify the **Command**.)
- `binded_callable`: `Callable<class_Callable>`{.interpreted-text
  role="ref"} (Callable of the **Command**. This will be executed when
  the **Command** is selected.)
- `shortcut_text`: `String<class_String>`{.interpreted-text role="ref"}
  (Shortcut text of the **Command** if available.)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorCommandPalette_method_remove_command}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_command**(key_name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorCommandPalette_method_remove_command>`{.interpreted-text
role="ref"}

Removes the custom command from EditorCommandPalette.

- `key_name`: `String<class_String>`{.interpreted-text role="ref"} (Name
  of the key for a particular **Command**.)
