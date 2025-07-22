github_url
:   hide

# EditorResourcePicker {#class_EditorResourcePicker}

**Inherits:** `HBoxContainer<class_HBoxContainer>`{.interpreted-text
role="ref"} **\<** `BoxContainer<class_BoxContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorScriptPicker<class_EditorScriptPicker>`{.interpreted-text
role="ref"}

Godot editor\'s control for selecting
`Resource<class_Resource>`{.interpreted-text role="ref"} type
properties.

::: rst-class
classref-introduction-group
:::

## Description

This `Control<class_Control>`{.interpreted-text role="ref"} node is used
in the editor\'s Inspector dock to allow editing of
`Resource<class_Resource>`{.interpreted-text role="ref"} type
properties. It provides options for creating, loading, saving and
converting resources. Can be used with
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"} to recreate the same behavior.

\*\*Note:\*\* This `Control<class_Control>`{.interpreted-text
role="ref"} does not include any editor for the resource, as editing is
controlled by the Inspector dock itself or sub-Inspectors.

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

:::: {#class_EditorResourcePicker_signal_resource_changed}
::: rst-class
classref-signal
:::
::::

**resource_changed**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_EditorResourcePicker_signal_resource_changed>`{.interpreted-text
role="ref"}

Emitted when the value of the edited resource was changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePicker_signal_resource_selected}
::: rst-class
classref-signal
:::
::::

**resource_selected**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"}, inspect:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorResourcePicker_signal_resource_selected>`{.interpreted-text
role="ref"}

Emitted when the resource value was set and user clicked to edit it.
When `inspect` is `true`, the signal was caused by the context menu
\"Edit\" or \"Inspect\" option.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EditorResourcePicker_property_base_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **base_type** =
`""`
`🔗<class_EditorResourcePicker_property_base_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_base_type**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_base_type**()

The base type of allowed resource types. Can be a comma-separated list
of several options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePicker_property_editable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editable** = `true`
`🔗<class_EditorResourcePicker_property_editable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_editable**()

If `true`, the value can be selected and edited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePicker_property_edited_resource}
::: rst-class
classref-property
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"}
**edited_resource**
`🔗<class_EditorResourcePicker_property_edited_resource>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edited_resource**(value:
  `Resource<class_Resource>`{.interpreted-text role="ref"})
- `Resource<class_Resource>`{.interpreted-text role="ref"}
  **get_edited_resource**()

The edited resource value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePicker_property_toggle_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **toggle_mode** =
`false`
`🔗<class_EditorResourcePicker_property_toggle_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_toggle_mode**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_toggle_mode**()

If `true`, the main button with the resource preview works in the toggle
mode. Use
`set_toggle_pressed()<class_EditorResourcePicker_method_set_toggle_pressed>`{.interpreted-text
role="ref"} to manually set the state.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorResourcePicker_private_method__handle_menu_selected}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_handle_menu_selected**(id: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePicker_private_method__handle_menu_selected>`{.interpreted-text
role="ref"}

This virtual method can be implemented to handle context menu items not
handled by default. See
`_set_create_options()<class_EditorResourcePicker_private_method__set_create_options>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePicker_private_method__set_create_options}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_create_options**(menu_node:
`Object<class_Object>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePicker_private_method__set_create_options>`{.interpreted-text
role="ref"}

This virtual method is called when updating the context menu of
**EditorResourcePicker**. Implement this method to override the \"New
\...\" items with your own options. `menu_node` is a reference to the
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"} node.

\*\*Note:\*\* Implement
`_handle_menu_selected()<class_EditorResourcePicker_private_method__handle_menu_selected>`{.interpreted-text
role="ref"} to handle these custom items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePicker_method_get_allowed_types}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_allowed_types**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorResourcePicker_method_get_allowed_types>`{.interpreted-text
role="ref"}

Returns a list of all allowed types and subtypes corresponding to the
`base_type<class_EditorResourcePicker_property_base_type>`{.interpreted-text
role="ref"}. If the
`base_type<class_EditorResourcePicker_property_base_type>`{.interpreted-text
role="ref"} is empty, an empty list is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorResourcePicker_method_set_toggle_pressed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_toggle_pressed**(pressed: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_EditorResourcePicker_method_set_toggle_pressed>`{.interpreted-text
role="ref"}

Sets the toggle mode state for the main button. Works only if
`toggle_mode<class_EditorResourcePicker_property_toggle_mode>`{.interpreted-text
role="ref"} is set to `true`.
