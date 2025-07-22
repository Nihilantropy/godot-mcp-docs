github_url
:   hide

# EditorScriptPicker {#class_EditorScriptPicker}

**Inherits:**
`EditorResourcePicker<class_EditorResourcePicker>`{.interpreted-text
role="ref"} **\<**
`HBoxContainer<class_HBoxContainer>`{.interpreted-text role="ref"}
**\<** `BoxContainer<class_BoxContainer>`{.interpreted-text role="ref"}
**\<** `Container<class_Container>`{.interpreted-text role="ref"} **\<**
`Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Godot editor\'s control for selecting the `script` property of a
`Node<class_Node>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Similar to
`EditorResourcePicker<class_EditorResourcePicker>`{.interpreted-text
role="ref"} this `Control<class_Control>`{.interpreted-text role="ref"}
node is used in the editor\'s Inspector dock, but only to edit the
`script` property of a `Node<class_Node>`{.interpreted-text role="ref"}.
Default options for creating new resources of all possible subtypes are
replaced with dedicated buttons that open the \"Attach Node Script\"
dialog. Can be used with
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"} to recreate the same behavior.

\*\*Note:\*\* You must set the
`script_owner<class_EditorScriptPicker_property_script_owner>`{.interpreted-text
role="ref"} for the custom context menu items to work.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EditorScriptPicker_property_script_owner}
::: rst-class
classref-property
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **script_owner**
`🔗<class_EditorScriptPicker_property_script_owner>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_script_owner**(value: `Node<class_Node>`{.interpreted-text
  role="ref"})
- `Node<class_Node>`{.interpreted-text role="ref"}
  **get_script_owner**()

The owner `Node<class_Node>`{.interpreted-text role="ref"} of the script
property that holds the edited resource.
