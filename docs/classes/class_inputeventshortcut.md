github_url
:   hide

# InputEventShortcut {#class_InputEventShortcut}

**Inherits:** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a triggered keyboard
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

InputEventShortcut is a special event that can be received in
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"},
`Node._shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"}, and
`Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"}. It is typically sent by the editor\'s Command Palette to
trigger actions, but can also be sent manually using
`Viewport.push_input()<class_Viewport_method_push_input>`{.interpreted-text
role="ref"}.

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

:::: {#class_InputEventShortcut_property_shortcut}
::: rst-class
classref-property
:::
::::

`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} **shortcut**
`🔗<class_InputEventShortcut_property_shortcut>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shortcut**(value: `Shortcut<class_Shortcut>`{.interpreted-text
  role="ref"})
- `Shortcut<class_Shortcut>`{.interpreted-text role="ref"}
  **get_shortcut**()

The `Shortcut<class_Shortcut>`{.interpreted-text role="ref"} represented
by this event. Its
`Shortcut.matches_event()<class_Shortcut_method_matches_event>`{.interpreted-text
role="ref"} method will always return `true` for this event.
