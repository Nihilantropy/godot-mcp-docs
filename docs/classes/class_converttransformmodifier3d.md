github_url
:   hide

# ConvertTransformModifier3D {#class_ConvertTransformModifier3D}

**Inherits:**
`BoneConstraint3D<class_BoneConstraint3D>`{.interpreted-text role="ref"}
**\<** `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} that apply transform to the bone which converted from
reference.

::: rst-class
classref-introduction-group
:::

## Description

Apply the copied transform of the bone set by
`BoneConstraint3D.set_reference_bone()<class_BoneConstraint3D_method_set_reference_bone>`{.interpreted-text
role="ref"} to the bone set by
`BoneConstraint3D.set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>`{.interpreted-text
role="ref"} about the specific axis with remapping it with some options.

There are 4 ways to apply the transform, depending on the combination of
`set_relative()<class_ConvertTransformModifier3D_method_set_relative>`{.interpreted-text
role="ref"} and
`set_additive()<class_ConvertTransformModifier3D_method_set_additive>`{.interpreted-text
role="ref"}.

\*\*Relative + Additive:\*\*

- Extract reference pose relative to the rest and add it to the apply
  bone\'s pose.

\*\*Relative + Not Additive:\*\*

- Extract reference pose relative to the rest and add it to the apply
  bone\'s rest.

\*\*Not Relative + Additive:\*\*

- Extract reference pose absolutely and add it to the apply bone\'s
  pose.

\*\*Not Relative + Not Additive:\*\*

- Extract reference pose absolutely and the apply bone\'s pose is
  replaced with it.

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

## Enumerations

:::: {#enum_ConvertTransformModifier3D_TransformMode}
::: rst-class
classref-enumeration
:::
::::

enum **TransformMode**:
`🔗<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"}

:::: {#class_ConvertTransformModifier3D_constant_TRANSFORM_MODE_POSITION}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformMode<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"} **TRANSFORM_MODE_POSITION** = `0`

Convert with position. Transfer the difference.

:::: {#class_ConvertTransformModifier3D_constant_TRANSFORM_MODE_ROTATION}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformMode<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"} **TRANSFORM_MODE_ROTATION** = `1`

Convert with rotation. The angle is the roll for the specified axis.

:::: {#class_ConvertTransformModifier3D_constant_TRANSFORM_MODE_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformMode<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"} **TRANSFORM_MODE_SCALE** = `2`

Convert with scale. Transfers the ratio, not the difference.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ConvertTransformModifier3D_property_setting_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **setting_count** = `0`
`🔗<class_ConvertTransformModifier3D_property_setting_count>`{.interpreted-text
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

:::: {#class_ConvertTransformModifier3D_method_get_apply_axis}
::: rst-class
classref-method
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}
**get_apply_axis**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_apply_axis>`{.interpreted-text
role="ref"}

Returns the axis of the remapping destination transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_get_apply_range_max}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_apply_range_max**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_apply_range_max>`{.interpreted-text
role="ref"}

Returns the maximum value of the remapping destination range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_get_apply_range_min}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_apply_range_min**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_apply_range_min>`{.interpreted-text
role="ref"}

Returns the minimum value of the remapping destination range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_get_apply_transform_mode}
::: rst-class
classref-method
:::
::::

`TransformMode<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"} **get_apply_transform_mode**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_apply_transform_mode>`{.interpreted-text
role="ref"}

Returns the operation of the remapping destination transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_get_reference_axis}
::: rst-class
classref-method
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}
**get_reference_axis**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_reference_axis>`{.interpreted-text
role="ref"}

Returns the axis of the remapping source transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_get_reference_range_max}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_reference_range_max**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_reference_range_max>`{.interpreted-text
role="ref"}

Returns the maximum value of the remapping source range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_get_reference_range_min}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_reference_range_min**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_reference_range_min>`{.interpreted-text
role="ref"}

Returns the minimum value of the remapping source range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_get_reference_transform_mode}
::: rst-class
classref-method
:::
::::

`TransformMode<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"} **get_reference_transform_mode**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_get_reference_transform_mode>`{.interpreted-text
role="ref"}

Returns the operation of the remapping source transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_is_additive}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_additive**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_is_additive>`{.interpreted-text
role="ref"}

Returns `true` if the additive option is enabled in the setting at
`index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_is_relative}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_relative**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConvertTransformModifier3D_method_is_relative>`{.interpreted-text
role="ref"}

Returns `true` if the relative option is enabled in the setting at
`index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_additive}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additive**(index: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_additive>`{.interpreted-text
role="ref"}

Sets additive option in the setting at `index` to `enabled`. This mainly
affects the process of applying transform to the
`BoneConstraint3D.set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>`{.interpreted-text
role="ref"}.

If sets `enabled` to `true`, the processed transform is added to the
pose of the current apply bone.

If sets `enabled` to `false`, the pose of the current apply bone is
replaced with the processed transform. However, if set
`set_relative()<class_ConvertTransformModifier3D_method_set_relative>`{.interpreted-text
role="ref"} to `true`, the transform is relative to rest.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_apply_axis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_apply_axis**(index: `int<class_int>`{.interpreted-text
role="ref"}, axis: `Axis<enum_Vector3_Axis>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_apply_axis>`{.interpreted-text
role="ref"}

Sets the axis of the remapping destination transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_apply_range_max}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_apply_range_max**(index: `int<class_int>`{.interpreted-text
role="ref"}, range_max: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_apply_range_max>`{.interpreted-text
role="ref"}

Sets the maximum value of the remapping destination range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_apply_range_min}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_apply_range_min**(index: `int<class_int>`{.interpreted-text
role="ref"}, range_min: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_apply_range_min>`{.interpreted-text
role="ref"}

Sets the minimum value of the remapping destination range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_apply_transform_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_apply_transform_mode**(index: `int<class_int>`{.interpreted-text
role="ref"}, transform_mode:
`TransformMode<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_apply_transform_mode>`{.interpreted-text
role="ref"}

Sets the operation of the remapping destination transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_reference_axis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_reference_axis**(index: `int<class_int>`{.interpreted-text
role="ref"}, axis: `Axis<enum_Vector3_Axis>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_reference_axis>`{.interpreted-text
role="ref"}

Sets the axis of the remapping source transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_reference_range_max}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_reference_range_max**(index: `int<class_int>`{.interpreted-text
role="ref"}, range_max: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_reference_range_max>`{.interpreted-text
role="ref"}

Sets the maximum value of the remapping source range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_reference_range_min}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_reference_range_min**(index: `int<class_int>`{.interpreted-text
role="ref"}, range_min: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_reference_range_min>`{.interpreted-text
role="ref"}

Sets the minimum value of the remapping source range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_reference_transform_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_reference_transform_mode**(index:
`int<class_int>`{.interpreted-text role="ref"}, transform_mode:
`TransformMode<enum_ConvertTransformModifier3D_TransformMode>`{.interpreted-text
role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_reference_transform_mode>`{.interpreted-text
role="ref"}

Sets the operation of the remapping source transform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConvertTransformModifier3D_method_set_relative}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_relative**(index: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ConvertTransformModifier3D_method_set_relative>`{.interpreted-text
role="ref"}

Sets relative option in the setting at `index` to `enabled`.

If sets `enabled` to `true`, the extracted and applying transform is
relative to the rest.

If sets `enabled` to `false`, the extracted transform is absolute.
