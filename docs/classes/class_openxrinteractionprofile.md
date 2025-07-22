github_url
:   hide

# OpenXRInteractionProfile {#class_OpenXRInteractionProfile}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Suggested bindings object for OpenXR.

::: rst-class
classref-introduction-group
:::

## Description

This object stores suggested bindings for an interaction profile.
Interaction profiles define the metadata for a tracked XR device such as
an XR controller.

For more information see the [interaction profiles info in the OpenXR
specification](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#semantic-path-interaction-profiles).

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

:::: {#class_OpenXRInteractionProfile_property_binding_modifiers}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **binding_modifiers**
= `[]`
`🔗<class_OpenXRInteractionProfile_property_binding_modifiers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_binding_modifiers**(value:
  `Array<class_Array>`{.interpreted-text role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_binding_modifiers**()

Binding modifiers for this interaction profile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfile_property_bindings}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **bindings** = `[]`
`🔗<class_OpenXRInteractionProfile_property_bindings>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bindings**(value: `Array<class_Array>`{.interpreted-text
  role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"} **get_bindings**()

Action bindings for this interaction profile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfile_property_interaction_profile_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interaction_profile_path** = `""`
`🔗<class_OpenXRInteractionProfile_property_interaction_profile_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interaction_profile_path**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_interaction_profile_path**()

The interaction profile path identifying the XR device.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRInteractionProfile_method_get_binding}
::: rst-class
classref-method
:::
::::

`OpenXRIPBinding<class_OpenXRIPBinding>`{.interpreted-text role="ref"}
**get_binding**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInteractionProfile_method_get_binding>`{.interpreted-text
role="ref"}

Retrieve the binding at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfile_method_get_binding_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_binding_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInteractionProfile_method_get_binding_count>`{.interpreted-text
role="ref"}

Get the number of bindings in this interaction profile.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfile_method_get_binding_modifier}
::: rst-class
classref-method
:::
::::

`OpenXRIPBindingModifier<class_OpenXRIPBindingModifier>`{.interpreted-text
role="ref"} **get_binding_modifier**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInteractionProfile_method_get_binding_modifier>`{.interpreted-text
role="ref"}

Get the
`OpenXRBindingModifier<class_OpenXRBindingModifier>`{.interpreted-text
role="ref"} at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRInteractionProfile_method_get_binding_modifier_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_binding_modifier_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRInteractionProfile_method_get_binding_modifier_count>`{.interpreted-text
role="ref"}

Get the number of binding modifiers in this interaction profile.
