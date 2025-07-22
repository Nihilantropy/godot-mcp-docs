github_url
:   hide

# OpenXRActionMap {#class_OpenXRActionMap}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Collection of `OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text
role="ref"} and
`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`{.interpreted-text
role="ref"} resources for the OpenXR module.

::: rst-class
classref-introduction-group
:::

## Description

OpenXR uses an action system similar to Godots Input map system to bind
inputs and outputs on various types of XR controllers to named actions.
OpenXR specifies more detail on these inputs and outputs than Godot
supports.

Another important distinction is that OpenXR offers no control over
these bindings. The bindings we register are suggestions, it is up to
the XR runtime to offer users the ability to change these bindings. This
allows the XR runtime to fill in the gaps if new hardware becomes
available.

The action map therefore needs to be loaded at startup and can\'t be
changed afterwards. This resource is a container for the entire action
map.

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

:::: {#class_OpenXRActionMap_property_action_sets}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **action_sets** =
`[]` `🔗<class_OpenXRActionMap_property_action_sets>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_action_sets**(value: `Array<class_Array>`{.interpreted-text
  role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_action_sets**()

Collection of `OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text
role="ref"}s that are part of this action map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_property_interaction_profiles}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**interaction_profiles** = `[]`
`🔗<class_OpenXRActionMap_property_interaction_profiles>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interaction_profiles**(value:
  `Array<class_Array>`{.interpreted-text role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_interaction_profiles**()

Collection of
`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`{.interpreted-text
role="ref"}s that are part of this action map.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRActionMap_method_add_action_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_action_set**(action_set:
`OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text role="ref"})
`🔗<class_OpenXRActionMap_method_add_action_set>`{.interpreted-text
role="ref"}

Add an action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_add_interaction_profile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_interaction_profile**(interaction_profile:
`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRActionMap_method_add_interaction_profile>`{.interpreted-text
role="ref"}

Add an interaction profile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_create_default_action_sets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_default_action_sets**()
`🔗<class_OpenXRActionMap_method_create_default_action_sets>`{.interpreted-text
role="ref"}

Setup this action set with our default actions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_find_action_set}
::: rst-class
classref-method
:::
::::

`OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text role="ref"}
**find_action_set**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRActionMap_method_find_action_set>`{.interpreted-text
role="ref"}

Retrieve an action set by name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_find_interaction_profile}
::: rst-class
classref-method
:::
::::

`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`{.interpreted-text
role="ref"} **find_interaction_profile**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRActionMap_method_find_interaction_profile>`{.interpreted-text
role="ref"}

Find an interaction profile by its name (path).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_get_action_set}
::: rst-class
classref-method
:::
::::

`OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text role="ref"}
**get_action_set**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRActionMap_method_get_action_set>`{.interpreted-text
role="ref"}

Retrieve the action set at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_get_action_set_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_action_set_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRActionMap_method_get_action_set_count>`{.interpreted-text
role="ref"}

Retrieve the number of actions sets in our action map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_get_interaction_profile}
::: rst-class
classref-method
:::
::::

`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`{.interpreted-text
role="ref"} **get_interaction_profile**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRActionMap_method_get_interaction_profile>`{.interpreted-text
role="ref"}

Get the interaction profile at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_get_interaction_profile_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_interaction_profile_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRActionMap_method_get_interaction_profile_count>`{.interpreted-text
role="ref"}

Retrieve the number of interaction profiles in our action map.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_remove_action_set}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_action_set**(action_set:
`OpenXRActionSet<class_OpenXRActionSet>`{.interpreted-text role="ref"})
`🔗<class_OpenXRActionMap_method_remove_action_set>`{.interpreted-text
role="ref"}

Remove an action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRActionMap_method_remove_interaction_profile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_interaction_profile**(interaction_profile:
`OpenXRInteractionProfile<class_OpenXRInteractionProfile>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRActionMap_method_remove_interaction_profile>`{.interpreted-text
role="ref"}

Remove an interaction profile.
