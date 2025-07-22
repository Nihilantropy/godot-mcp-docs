github_url
:   hide

# OpenXRAction {#class_OpenXRAction}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

An OpenXR action.

::: rst-class
classref-introduction-group
:::

## Description

This resource defines an OpenXR action. Actions can be used both for
inputs (buttons, joysticks, triggers, etc.) and outputs (haptics).

OpenXR performs automatic conversion between action type and input type
whenever possible. An analog trigger bound to a boolean action will thus
return `false` if the trigger is depressed and `true` if pressed fully.

Actions are not directly bound to specific devices, instead OpenXR
recognizes a limited number of top level paths that identify devices by
usage. We can restrict which devices an action can be bound to by these
top level paths. For instance an action that should only be used for
hand held controllers can have the top level paths \"/user/hand/left\"
and \"/user/hand/right\" associated with them. See the [reserved path
section in the OpenXR
specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-reserved)
for more info on the top level paths.

Note that the name of the resource is used to register the action with.

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

## Enumerations

:::: {#enum_OpenXRAction_ActionType}
::: rst-class
classref-enumeration
:::
::::

enum **ActionType**:
`🔗<enum_OpenXRAction_ActionType>`{.interpreted-text role="ref"}

:::: {#class_OpenXRAction_constant_OPENXR_ACTION_BOOL}
::: rst-class
classref-enumeration-constant
:::
::::

`ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text role="ref"}
**OPENXR_ACTION_BOOL** = `0`

This action provides a boolean value.

:::: {#class_OpenXRAction_constant_OPENXR_ACTION_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text role="ref"}
**OPENXR_ACTION_FLOAT** = `1`

This action provides a float value between `0.0` and `1.0` for any
analog input such as triggers.

:::: {#class_OpenXRAction_constant_OPENXR_ACTION_VECTOR2}
::: rst-class
classref-enumeration-constant
:::
::::

`ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text role="ref"}
**OPENXR_ACTION_VECTOR2** = `2`

This action provides a `Vector2<class_Vector2>`{.interpreted-text
role="ref"} value and can be bound to embedded trackpads and joysticks.

:::: {#class_OpenXRAction_constant_OPENXR_ACTION_POSE}
::: rst-class
classref-enumeration-constant
:::
::::

`ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text role="ref"}
**OPENXR_ACTION_POSE** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OpenXRAction_property_action_type}
::: rst-class
classref-property
:::
::::

`ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text role="ref"}
**action_type** = `1`
`🔗<class_OpenXRAction_property_action_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_action_type**(value:
  `ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text
  role="ref"})
- `ActionType<enum_OpenXRAction_ActionType>`{.interpreted-text
  role="ref"} **get_action_type**()

The type of action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAction_property_localized_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **localized_name**
= `""`
`🔗<class_OpenXRAction_property_localized_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_localized_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_localized_name**()

The localized description of this action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRAction_property_toplevel_paths}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **toplevel_paths** = `PackedStringArray()`
`🔗<class_OpenXRAction_property_toplevel_paths>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_toplevel_paths**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_toplevel_paths**()

A collections of toplevel paths to which this action can be bound.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.
