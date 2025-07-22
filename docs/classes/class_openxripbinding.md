github_url
:   hide

# OpenXRIPBinding {#class_OpenXRIPBinding}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Defines a binding between an
`OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"} and an
XR input or output.

::: rst-class
classref-introduction-group
:::

## Description

This binding resource binds an
`OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"} to an
input or output. As most controllers have left hand and right versions
that are handled by the same interaction profile we can specify multiple
bindings. For instance an action \"Fire\" could be bound to both
\"/user/hand/left/input/trigger\" and
\"/user/hand/right/input/trigger\". This would require two binding
entries.

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

:::: {#class_OpenXRIPBinding_property_action}
::: rst-class
classref-property
:::
::::

`OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"}
**action** `🔗<class_OpenXRIPBinding_property_action>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_action**(value:
  `OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"})
- `OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"}
  **get_action**()

`OpenXRAction<class_OpenXRAction>`{.interpreted-text role="ref"} that is
bound to
`binding_path<class_OpenXRIPBinding_property_binding_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_property_binding_modifiers}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **binding_modifiers**
= `[]`
`🔗<class_OpenXRIPBinding_property_binding_modifiers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_binding_modifiers**(value:
  `Array<class_Array>`{.interpreted-text role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_binding_modifiers**()

Binding modifiers for this binding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_property_binding_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **binding_path** =
`""` `🔗<class_OpenXRIPBinding_property_binding_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_binding_path**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_binding_path**()

Binding path that defines the input or output bound to
`action<class_OpenXRIPBinding_property_action>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Binding paths are suggestions, an XR runtime may choose to
bind the action to a different input or output emulating this input or
output.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_property_paths}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **paths**
`🔗<class_OpenXRIPBinding_property_paths>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_paths**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_paths**()

**Deprecated:** Use
`binding_path<class_OpenXRIPBinding_property_binding_path>`{.interpreted-text
role="ref"} instead.

Paths that define the inputs or outputs bound on the device.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRIPBinding_method_add_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_path**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_OpenXRIPBinding_method_add_path>`{.interpreted-text
role="ref"}

**Deprecated:** Binding is for a single path.

Add an input/output path to this binding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_method_get_binding_modifier}
::: rst-class
classref-method
:::
::::

`OpenXRActionBindingModifier<class_OpenXRActionBindingModifier>`{.interpreted-text
role="ref"} **get_binding_modifier**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRIPBinding_method_get_binding_modifier>`{.interpreted-text
role="ref"}

Get the
`OpenXRBindingModifier<class_OpenXRBindingModifier>`{.interpreted-text
role="ref"} at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_method_get_binding_modifier_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_binding_modifier_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRIPBinding_method_get_binding_modifier_count>`{.interpreted-text
role="ref"}

Get the number of binding modifiers for this binding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_method_get_path_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_path_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRIPBinding_method_get_path_count>`{.interpreted-text
role="ref"}

**Deprecated:** Binding is for a single path.

Get the number of input/output paths in this binding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_method_has_path}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_path**(path:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRIPBinding_method_has_path>`{.interpreted-text
role="ref"}

**Deprecated:** Binding is for a single path.

Returns `true` if this input/output path is part of this binding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRIPBinding_method_remove_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_path**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRIPBinding_method_remove_path>`{.interpreted-text
role="ref"}

**Deprecated:** Binding is for a single path.

Removes this input/output path from this binding.
