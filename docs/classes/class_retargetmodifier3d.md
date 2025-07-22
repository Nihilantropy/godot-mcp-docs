github_url
:   hide

# RetargetModifier3D {#class_RetargetModifier3D}

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A modifier to transfer parent skeleton poses (or global poses) to child
skeletons in model space with different rests.

::: rst-class
classref-introduction-group
:::

## Description

Retrieves the pose (or global pose) relative to the parent Skeleton\'s
rest in model space and transfers it to the child Skeleton.

This modifier rewrites the pose of the child skeleton directly in the
parent skeleton\'s update process. This means that it overwrites the
mapped bone pose set in the normal process on the target skeleton. If
you want to set the target skeleton bone pose after retargeting, you
will need to add a
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} child to the target skeleton and thereby modify the pose.

\*\*Note:\*\* When the
`use_global_pose<class_RetargetModifier3D_property_use_global_pose>`{.interpreted-text
role="ref"} is enabled, even if it is an unmapped bone, it can cause
visual problems because the global pose is applied ignoring the parent
bone\'s pose **if it has mapped bone children**. See also
`use_global_pose<class_RetargetModifier3D_property_use_global_pose>`{.interpreted-text
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

## Enumerations

:::: {#enum_RetargetModifier3D_TransformFlag}
::: rst-class
classref-enumeration
:::
::::

flags **TransformFlag**:
`🔗<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
role="ref"}

:::: {#class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_POSITION** = `1`

If set, allows to retarget the position.

:::: {#class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_ROTATION** = `2`

If set, allows to retarget the rotation.

:::: {#class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_SCALE** = `4`

If set, allows to retarget the scale.

:::: {#class_RetargetModifier3D_constant_TRANSFORM_FLAG_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`TransformFlag<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
role="ref"} **TRANSFORM_FLAG_ALL** = `7`

If set, allows to retarget the position/rotation/scale.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RetargetModifier3D_property_enable}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TransformFlag<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
role="ref"}\] **enable** = `7`
`🔗<class_RetargetModifier3D_property_enable>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`TransformFlag<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`TransformFlag<enum_RetargetModifier3D_TransformFlag>`{.interpreted-text
  role="ref"}\] **get_enable_flags**()

Flags to control the process of the transform elements individually when
`use_global_pose<class_RetargetModifier3D_property_use_global_pose>`{.interpreted-text
role="ref"} is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RetargetModifier3D_property_profile}
::: rst-class
classref-property
:::
::::

`SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
**profile**
`🔗<class_RetargetModifier3D_property_profile>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_profile**(value:
  `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text
  role="ref"})
- `SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
  **get_profile**()

`SkeletonProfile<class_SkeletonProfile>`{.interpreted-text role="ref"}
for retargeting bones with names matching the bone list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RetargetModifier3D_property_use_global_pose}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_global_pose** =
`false`
`🔗<class_RetargetModifier3D_property_use_global_pose>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_global_pose**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_global_pose**()

If `false`, in case the target skeleton has fewer bones than the source
skeleton, the source bone parent\'s transform will be ignored.

Instead, it is possible to retarget between models with different body
shapes, and position, rotation, and scale can be retargeted separately.

If `true`, retargeting is performed taking into account global pose.

In case the target skeleton has fewer bones than the source skeleton,
the source bone parent\'s transform is taken into account. However, bone
length between skeletons must match exactly, if not, the bones will be
forced to expand or shrink.

This is useful for using dummy bone with length `0` to match postures
when retargeting between models with different number of bones.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RetargetModifier3D_method_is_position_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_position_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RetargetModifier3D_method_is_position_enabled>`{.interpreted-text
role="ref"}

Returns `true` if
`enable<class_RetargetModifier3D_property_enable>`{.interpreted-text
role="ref"} has
`TRANSFORM_FLAG_POSITION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RetargetModifier3D_method_is_rotation_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_rotation_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RetargetModifier3D_method_is_rotation_enabled>`{.interpreted-text
role="ref"}

Returns `true` if
`enable<class_RetargetModifier3D_property_enable>`{.interpreted-text
role="ref"} has
`TRANSFORM_FLAG_ROTATION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RetargetModifier3D_method_is_scale_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_scale_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RetargetModifier3D_method_is_scale_enabled>`{.interpreted-text
role="ref"}

Returns `true` if
`enable<class_RetargetModifier3D_property_enable>`{.interpreted-text
role="ref"} has
`TRANSFORM_FLAG_SCALE<class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RetargetModifier3D_method_set_position_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_position_enabled**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_RetargetModifier3D_method_set_position_enabled>`{.interpreted-text
role="ref"}

Sets
`TRANSFORM_FLAG_POSITION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_POSITION>`{.interpreted-text
role="ref"} into
`enable<class_RetargetModifier3D_property_enable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RetargetModifier3D_method_set_rotation_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_rotation_enabled**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_RetargetModifier3D_method_set_rotation_enabled>`{.interpreted-text
role="ref"}

Sets
`TRANSFORM_FLAG_ROTATION<class_RetargetModifier3D_constant_TRANSFORM_FLAG_ROTATION>`{.interpreted-text
role="ref"} into
`enable<class_RetargetModifier3D_property_enable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RetargetModifier3D_method_set_scale_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_scale_enabled**(enabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_RetargetModifier3D_method_set_scale_enabled>`{.interpreted-text
role="ref"}

Sets
`TRANSFORM_FLAG_SCALE<class_RetargetModifier3D_constant_TRANSFORM_FLAG_SCALE>`{.interpreted-text
role="ref"} into
`enable<class_RetargetModifier3D_property_enable>`{.interpreted-text
role="ref"}.
