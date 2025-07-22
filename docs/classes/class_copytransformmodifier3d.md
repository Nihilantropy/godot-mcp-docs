github_url
:   hide

# CopyTransformModifier3D {#class_CopyTransformModifier3D}

**Inherits:**
`BoneConstraint3D<class_BoneConstraint3D>`{.interpreted-text role="ref"}
**\<** `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} that apply transform to the bone which copied from
reference.

::: rst-class
classref-introduction-group
:::

## Description

Apply the copied transform of the bone set by
`BoneConstraint3D.set_reference_bone()<class_BoneConstraint3D_method_set_reference_bone>`{.interpreted-text
role="ref"} to the bone set by
`BoneConstraint3D.set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>`{.interpreted-text
role="ref"} with processing it with some masks and options.

There are 4 ways to apply the transform, depending on the combination of
`set_relative()<class_CopyTransformModifier3D_method_set_relative>`{.interpreted-text
role="ref"} and
`set_additive()<class_CopyTransformModifier3D_method_set_additive>`{.interpreted-text
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

:::: {#enum_CopyTransformModifier3D_TransformFlag}
::: rst-class
classref-enumeration
:::
::::

flags **TransformFlag**:
`🔗<enum_CopyTransformModifier3D_TransformFlag>`{.interpreted-text
role="ref"}

:::: {#class_CopyTransformModifier3D_constant_TRANSFORM_FLAG_POSITION}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_POSITION** = `1`

If set, allows to copy the position.

:::: {#class_CopyTransformModifier3D_constant_TRANSFORM_FLAG_ROTATION}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_ROTATION** = `2`

If set, allows to copy the rotation.

:::: {#class_CopyTransformModifier3D_constant_TRANSFORM_FLAG_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_SCALE** = `4`

If set, allows to copy the scale.

:::: {#class_CopyTransformModifier3D_constant_TRANSFORM_FLAG_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_ALL** = `7`

If set, allows to copy the position/rotation/scale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CopyTransformModifier3D_AxisFlag}
::: rst-class
classref-enumeration
:::
::::

flags **AxisFlag**:
`🔗<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"}

:::: {#class_CopyTransformModifier3D_constant_AXIS_FLAG_X}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"} **AXIS_FLAG_X** = `1`

If set, allows to process the X-axis.

:::: {#class_CopyTransformModifier3D_constant_AXIS_FLAG_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"} **AXIS_FLAG_Y** = `2`

If set, allows to process the Y-axis.

:::: {#class_CopyTransformModifier3D_constant_AXIS_FLAG_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"} **AXIS_FLAG_Z** = `4`

If set, allows to process the Z-axis.

:::: {#class_CopyTransformModifier3D_constant_AXIS_FLAG_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"} **AXIS_FLAG_ALL** = `7`

If set, allows to process the all axes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CopyTransformModifier3D_property_setting_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **setting_count** = `0`
`🔗<class_CopyTransformModifier3D_property_setting_count>`{.interpreted-text
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

:::: {#class_CopyTransformModifier3D_method_get_axis_flags}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"}\] **get_axis_flags**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_get_axis_flags>`{.interpreted-text
role="ref"}

Returns the axis flags of the setting at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_get_copy_flags}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`{.interpreted-text
role="ref"}\] **get_copy_flags**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_get_copy_flags>`{.interpreted-text
role="ref"}

Returns the copy flags of the setting at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_get_invert_flags}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"}\] **get_invert_flags**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_get_invert_flags>`{.interpreted-text
role="ref"}

Returns the invert flags of the setting at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_additive}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_additive**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_additive>`{.interpreted-text
role="ref"}

Returns `true` if the additive option is enabled in the setting at
`index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_axis_x_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_axis_x_enabled**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_axis_x_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the enable flags has the flag for the X-axis in the
setting at `index`. See also
`set_axis_flags()<class_CopyTransformModifier3D_method_set_axis_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_axis_x_inverted}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_axis_x_inverted**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_axis_x_inverted>`{.interpreted-text
role="ref"}

Returns `true` if the invert flags has the flag for the X-axis in the
setting at `index`. See also
`set_invert_flags()<class_CopyTransformModifier3D_method_set_invert_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_axis_y_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_axis_y_enabled**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_axis_y_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the enable flags has the flag for the Y-axis in the
setting at `index`. See also
`set_axis_flags()<class_CopyTransformModifier3D_method_set_axis_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_axis_y_inverted}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_axis_y_inverted**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_axis_y_inverted>`{.interpreted-text
role="ref"}

Returns `true` if the invert flags has the flag for the Y-axis in the
setting at `index`. See also
`set_invert_flags()<class_CopyTransformModifier3D_method_set_invert_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_axis_z_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_axis_z_enabled**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_axis_z_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the enable flags has the flag for the Z-axis in the
setting at `index`. See also
`set_axis_flags()<class_CopyTransformModifier3D_method_set_axis_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_axis_z_inverted}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_axis_z_inverted**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_axis_z_inverted>`{.interpreted-text
role="ref"}

Returns `true` if the invert flags has the flag for the Z-axis in the
setting at `index`. See also
`set_invert_flags()<class_CopyTransformModifier3D_method_set_invert_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_position_copying}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_position_copying**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_position_copying>`{.interpreted-text
role="ref"}

Returns `true` if the copy flags has the flag for the position in the
setting at `index`. See also
`set_copy_flags()<class_CopyTransformModifier3D_method_set_copy_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_relative}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_relative**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_relative>`{.interpreted-text
role="ref"}

Returns `true` if the relative option is enabled in the setting at
`index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_rotation_copying}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_rotation_copying**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_rotation_copying>`{.interpreted-text
role="ref"}

Returns `true` if the copy flags has the flag for the rotation in the
setting at `index`. See also
`set_copy_flags()<class_CopyTransformModifier3D_method_set_copy_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_is_scale_copying}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_scale_copying**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CopyTransformModifier3D_method_is_scale_copying>`{.interpreted-text
role="ref"}

Returns `true` if the copy flags has the flag for the scale in the
setting at `index`. See also
`set_copy_flags()<class_CopyTransformModifier3D_method_set_copy_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_additive}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_additive**(index: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_additive>`{.interpreted-text
role="ref"}

Sets additive option in the setting at `index` to `enabled`. This mainly
affects the process of applying transform to the
`BoneConstraint3D.set_apply_bone()<class_BoneConstraint3D_method_set_apply_bone>`{.interpreted-text
role="ref"}.

If sets `enabled` to `true`, the processed transform is added to the
pose of the current apply bone.

If sets `enabled` to `false`, the pose of the current apply bone is
replaced with the processed transform. However, if set
`set_relative()<class_CopyTransformModifier3D_method_set_relative>`{.interpreted-text
role="ref"} to `true`, the transform is relative to rest.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_axis_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_flags**(index: `int<class_int>`{.interpreted-text
role="ref"}, axis_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"}\])
`🔗<class_CopyTransformModifier3D_method_set_axis_flags>`{.interpreted-text
role="ref"}

Sets the flags to copy axes. If the flag is valid, the axis is copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_axis_x_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_x_enabled**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_axis_x_enabled>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the X-axis will be copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_axis_x_inverted}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_x_inverted**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_axis_x_inverted>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the X-axis will be inverted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_axis_y_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_y_enabled**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_axis_y_enabled>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the Y-axis will be copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_axis_y_inverted}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_y_inverted**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_axis_y_inverted>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the Y-axis will be inverted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_axis_z_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_z_enabled**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_axis_z_enabled>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the Z-axis will be copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_axis_z_inverted}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_axis_z_inverted**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_axis_z_inverted>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the Z-axis will be inverted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_copy_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_copy_flags**(index: `int<class_int>`{.interpreted-text
role="ref"}, copy_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TransformFlag<enum_CopyTransformModifier3D_TransformFlag>`{.interpreted-text
role="ref"}\])
`🔗<class_CopyTransformModifier3D_method_set_copy_flags>`{.interpreted-text
role="ref"}

Sets the flags to process the transform operations. If the flag is
valid, the transform operation is processed.

\*\*Note:\*\* If the rotation is valid for only one axis, it respects
the roll of the valid axis. If the rotation is valid for two axes, it
discards the roll of the invalid axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_copy_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_copy_position**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_copy_position>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the position will be copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_copy_rotation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_copy_rotation**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_copy_rotation>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the rotation will be copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_copy_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_copy_scale**(index: `int<class_int>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_copy_scale>`{.interpreted-text
role="ref"}

If sets `enabled` to `true`, the scale will be copied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_invert_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_invert_flags**(index: `int<class_int>`{.interpreted-text
role="ref"}, axis_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`AxisFlag<enum_CopyTransformModifier3D_AxisFlag>`{.interpreted-text
role="ref"}\])
`🔗<class_CopyTransformModifier3D_method_set_invert_flags>`{.interpreted-text
role="ref"}

Sets the flags to inverte axes. If the flag is valid, the axis is
copied.

\*\*Note:\*\* An inverted scale means an inverse number, not a negative
scale. For example, inverting `2.0` means `0.5`.

\*\*Note:\*\* An inverted rotation flips the elements of the quaternion.
For example, a two-axis inversion will flip the roll of each axis, and a
three-axis inversion will flip the final orientation. However, be aware
that flipping only one axis may cause unintended rotation by the
unflipped axes, due to the characteristics of the quaternion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CopyTransformModifier3D_method_set_relative}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_relative**(index: `int<class_int>`{.interpreted-text role="ref"},
enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CopyTransformModifier3D_method_set_relative>`{.interpreted-text
role="ref"}

Sets relative option in the setting at `index` to `enabled`.

If sets `enabled` to `true`, the extracted and applying transform is
relative to the rest.

If sets `enabled` to `false`, the extracted transform is absolute.
