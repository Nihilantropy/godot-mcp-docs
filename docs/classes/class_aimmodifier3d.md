github_url
:   hide

# AimModifier3D {#class_AimModifier3D}

**Inherits:**
`BoneConstraint3D<class_BoneConstraint3D>`{.interpreted-text role="ref"}
**\<** `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

The **AimModifier3D** rotates a bone to look at a reference bone.

::: rst-class
classref-introduction-group
:::

## Description

This is a simple version of
`LookAtModifier3D<class_LookAtModifier3D>`{.interpreted-text role="ref"}
that only allows bone to the reference without advanced options such as
angle limitation or time-based interpolation.

The feature is simplified, but instead it is implemented with smooth
tracking without euler, see
`set_use_euler()<class_AimModifier3D_method_set_use_euler>`{.interpreted-text
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

## Property Descriptions

:::: {#class_AimModifier3D_property_setting_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **setting_count** = `0`
`🔗<class_AimModifier3D_property_setting_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_setting_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_setting_count**()

The number of settings in the modifier.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AimModifier3D_method_get_forward_axis}
::: rst-class
classref-method
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **get_forward_axis**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AimModifier3D_method_get_forward_axis>`{.interpreted-text
role="ref"}

Returns the forward axis of the bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AimModifier3D_method_get_primary_rotation_axis}
::: rst-class
classref-method
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}
**get_primary_rotation_axis**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AimModifier3D_method_get_primary_rotation_axis>`{.interpreted-text
role="ref"}

Returns the axis of the first rotation. It is enabled only if
`is_using_euler()<class_AimModifier3D_method_is_using_euler>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AimModifier3D_method_is_using_euler}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_using_euler**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AimModifier3D_method_is_using_euler>`{.interpreted-text
role="ref"}

Returns `true` if it provides rotation with using euler.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AimModifier3D_method_is_using_secondary_rotation}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_using_secondary_rotation**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AimModifier3D_method_is_using_secondary_rotation>`{.interpreted-text
role="ref"}

Returns `true` if it provides rotation by two axes. It is enabled only
if
`is_using_euler()<class_AimModifier3D_method_is_using_euler>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AimModifier3D_method_set_forward_axis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_forward_axis**(index: `int<class_int>`{.interpreted-text
role="ref"}, axis:
`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"})
`🔗<class_AimModifier3D_method_set_forward_axis>`{.interpreted-text
role="ref"}

Sets the forward axis of the bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AimModifier3D_method_set_primary_rotation_axis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_primary_rotation_axis**(index: `int<class_int>`{.interpreted-text
role="ref"}, axis: `Axis<enum_Vector3_Axis>`{.interpreted-text
role="ref"})
`🔗<class_AimModifier3D_method_set_primary_rotation_axis>`{.interpreted-text
role="ref"}

Sets the axis of the first rotation. It is enabled only if
`is_using_euler()<class_AimModifier3D_method_is_using_euler>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AimModifier3D_method_set_use_euler}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_use_euler**(index: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AimModifier3D_method_set_use_euler>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, it provides rotation with using euler.

If sets `enabled` to `false`, it provides rotation with using rotation
by arc generated from the forward axis vector and the vector toward the
reference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AimModifier3D_method_set_use_secondary_rotation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_use_secondary_rotation**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_AimModifier3D_method_set_use_secondary_rotation>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, it provides rotation by two axes. It is
enabled only if
`is_using_euler()<class_AimModifier3D_method_is_using_euler>`{.interpreted-text
role="ref"} is `true`.
