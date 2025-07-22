github_url
:   hide

# OpenXRActionSet {#class_OpenXRActionSet}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Collection of `OpenXRAction<class_OpenXRAction>`{.interpreted-text
role="ref"} resources that make up an action set.

::: rst-class
classref-introduction-group
:::

## Description

Action sets in OpenXR define a collection of actions that can be
activated in unison. This allows games to easily change between
different states that require different inputs or need to reinterpret
inputs. For instance we could have an action set that is active when a
menu is open, an action set that is active when the player is freely
walking around and an action set that is active when the player is
controlling a vehicle.

Action sets can contain the same action with the same name, if such
action sets are active at the same time the action set with the highest
priority defines which binding is active.

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

## Property Descriptions

:::: {#class_OpenXRActionSet_property_actions}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **actions** = `[]`
`🔗<class_OpenXRActionSet_property_actions>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_actions**(value: `Array<class_Array>`{.interpreted-text
  role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"} **get_actions**()

Collection of actions for this action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionSet_property_localized_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **localized_name**
= `""`
`🔗<class_OpenXRActionSet_property_localized_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_localized_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_localized_name**()

The localized name of this action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionSet_property_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **priority** = `0`
`🔗<class_OpenXRActionSet_property_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_priority**()

The priority for this action set.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRActionSet_method_add_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_action**(action:
`OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"})
`🔗<class_OpenXRActionSet_method_add_action>`{.interpreted-text
role="ref"}

Add an action to this action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionSet_method_get_action_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_action_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRActionSet_method_get_action_count>`{.interpreted-text
role="ref"}

Retrieve the number of actions in our action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionSet_method_remove_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_action**(action:
`OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"})
`🔗<class_OpenXRActionSet_method_remove_action>`{.interpreted-text
role="ref"}

Remove an action from this action set.
