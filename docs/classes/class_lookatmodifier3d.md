github_url
:   hide

# LookAtModifier3D {#class_LookAtModifier3D}

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

The **LookAtModifier3D** rotates a bone to look at a target.

::: rst-class
classref-introduction-group
:::

## Description

This `SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} rotates a bone to look at a target. This is helpful for
moving a character\'s head to look at the player, rotating a turret to
look at a target, or any other case where you want to make a bone rotate
towards something quickly and easily.

When applying multiple **LookAtModifier3D**s, the **LookAtModifier3D**
assigned to the parent bone must be put above the **LookAtModifier3D**
assigned to the child bone in the list in order for the child bone
results to be correct.

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

:::: {#enum_LookAtModifier3D_OriginFrom}
::: rst-class
classref-enumeration
:::
::::

enum **OriginFrom**:
`🔗<enum_LookAtModifier3D_OriginFrom>`{.interpreted-text role="ref"}

:::: {#class_LookAtModifier3D_constant_ORIGIN_FROM_SELF}
::: rst-class
classref-enumeration-constant
:::
::::

`OriginFrom<enum_LookAtModifier3D_OriginFrom>`{.interpreted-text
role="ref"} **ORIGIN_FROM_SELF** = `0`

The bone rest position of the bone specified in
`bone<class_LookAtModifier3D_property_bone>`{.interpreted-text
role="ref"} is used as origin.

:::: {#class_LookAtModifier3D_constant_ORIGIN_FROM_SPECIFIC_BONE}
::: rst-class
classref-enumeration-constant
:::
::::

`OriginFrom<enum_LookAtModifier3D_OriginFrom>`{.interpreted-text
role="ref"} **ORIGIN_FROM_SPECIFIC_BONE** = `1`

The bone global pose position of the bone specified in
`origin_bone<class_LookAtModifier3D_property_origin_bone>`{.interpreted-text
role="ref"} is used as origin.

\*\*Note:\*\* It is recommended that you select only the parent bone
unless you are familiar with the bone processing process. The specified
bone pose at the time the **LookAtModifier3D** is processed is used as a
reference. In other words, if you specify a child bone and the
**LookAtModifier3D** causes the child bone to move, the rendered result
and direction will not match.

:::: {#class_LookAtModifier3D_constant_ORIGIN_FROM_EXTERNAL_NODE}
::: rst-class
classref-enumeration-constant
:::
::::

`OriginFrom<enum_LookAtModifier3D_OriginFrom>`{.interpreted-text
role="ref"} **ORIGIN_FROM_EXTERNAL_NODE** = `2`

The global position of the `Node3D<class_Node3D>`{.interpreted-text
role="ref"} specified in
`origin_external_node<class_LookAtModifier3D_property_origin_external_node>`{.interpreted-text
role="ref"} is used as origin.

\*\*Note:\*\* Same as
`ORIGIN_FROM_SPECIFIC_BONE<class_LookAtModifier3D_constant_ORIGIN_FROM_SPECIFIC_BONE>`{.interpreted-text
role="ref"}, when specifying a
`BoneAttachment3D<class_BoneAttachment3D>`{.interpreted-text role="ref"}
with a child bone assigned, the rendered result and direction will not
match.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_LookAtModifier3D_property_bone}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bone** = `-1`
`🔗<class_LookAtModifier3D_property_bone>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bone**()

Index of the
`bone_name<class_LookAtModifier3D_property_bone_name>`{.interpreted-text
role="ref"} in the parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_bone_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **bone_name** =
`""` `🔗<class_LookAtModifier3D_property_bone_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_bone_name**()

The bone name of the `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} that the modification will operate on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_duration}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **duration** = `0.0`
`🔗<class_LookAtModifier3D_property_duration>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_duration**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_duration**()

The duration of the time-based interpolation. Interpolation is triggered
at the following cases:

- When the target node is changed
- When an axis is flipped due to angle limitation

\*\*Note:\*\* The flipping occurs when the target is outside the angle
limitation and the internally computed secondary rotation axis of the
forward vector is flipped. Visually, it occurs when the target is
outside the angle limitation and crosses the plane of the
`forward_axis<class_LookAtModifier3D_property_forward_axis>`{.interpreted-text
role="ref"} and
`primary_rotation_axis<class_LookAtModifier3D_property_primary_rotation_axis>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_ease_type}
::: rst-class
classref-property
:::
::::

`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
**ease_type** = `0`
`🔗<class_LookAtModifier3D_property_ease_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ease_type**(value:
  `EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"})
- `EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
  **get_ease_type**()

The ease type of the time-based interpolation. See also
`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_forward_axis}
::: rst-class
classref-property
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **forward_axis** = `4`
`🔗<class_LookAtModifier3D_property_forward_axis>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_forward_axis**(value:
  `BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
  role="ref"})
- `BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
  role="ref"} **get_forward_axis**()

The forward axis of the bone. This
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} modifies the bone so that this axis points toward the
`target_node<class_LookAtModifier3D_property_target_node>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_origin_bone}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **origin_bone**
`🔗<class_LookAtModifier3D_property_origin_bone>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_origin_bone**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_origin_bone**()

Index of the
`origin_bone_name<class_LookAtModifier3D_property_origin_bone_name>`{.interpreted-text
role="ref"} in the parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_origin_bone_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**origin_bone_name**
`🔗<class_LookAtModifier3D_property_origin_bone_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_origin_bone_name**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_origin_bone_name**()

If
`origin_from<class_LookAtModifier3D_property_origin_from>`{.interpreted-text
role="ref"} is
`ORIGIN_FROM_SPECIFIC_BONE<class_LookAtModifier3D_constant_ORIGIN_FROM_SPECIFIC_BONE>`{.interpreted-text
role="ref"}, the bone global pose position specified for this is used as
origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_origin_external_node}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**origin_external_node**
`🔗<class_LookAtModifier3D_property_origin_external_node>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_origin_external_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_origin_external_node**()

If
`origin_from<class_LookAtModifier3D_property_origin_from>`{.interpreted-text
role="ref"} is
`ORIGIN_FROM_EXTERNAL_NODE<class_LookAtModifier3D_constant_ORIGIN_FROM_EXTERNAL_NODE>`{.interpreted-text
role="ref"}, the global position of the
`Node3D<class_Node3D>`{.interpreted-text role="ref"} specified for this
is used as origin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_origin_from}
::: rst-class
classref-property
:::
::::

`OriginFrom<enum_LookAtModifier3D_OriginFrom>`{.interpreted-text
role="ref"} **origin_from** = `0`
`🔗<class_LookAtModifier3D_property_origin_from>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_origin_from**(value:
  `OriginFrom<enum_LookAtModifier3D_OriginFrom>`{.interpreted-text
  role="ref"})
- `OriginFrom<enum_LookAtModifier3D_OriginFrom>`{.interpreted-text
  role="ref"} **get_origin_from**()

This value determines from what origin is retrieved for use in the
calculation of the forward vector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_origin_offset}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **origin_offset**
= `Vector3(0, 0, 0)`
`🔗<class_LookAtModifier3D_property_origin_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_origin_offset**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_origin_offset**()

The offset of the bone pose origin. Matching the origins by offset is
useful for cases where multiple bones must always face the same
direction, such as the eyes.

\*\*Note:\*\* This value indicates the local position of the object set
in
`origin_from<class_LookAtModifier3D_property_origin_from>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_origin_safe_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**origin_safe_margin** = `0.1`
`🔗<class_LookAtModifier3D_property_origin_safe_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_origin_safe_margin**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_origin_safe_margin**()

If the target passes through too close to the origin than this value,
time-based interpolation is used even if the target is within the
angular limitations, to prevent the angular velocity from becoming too
high.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_primary_damp_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**primary_damp_threshold**
`🔗<class_LookAtModifier3D_property_primary_damp_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_damp_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_primary_damp_threshold**()

The threshold to start damping for
`primary_limit_angle<class_LookAtModifier3D_property_primary_limit_angle>`{.interpreted-text
role="ref"}. It provides non-linear (b-spline) interpolation, let it
feel more resistance the more it rotate to the edge limit. This is
useful for simulating the limits of human motion.

If `1.0`, no damping is performed. If `0.0`, damping is always
performed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_primary_limit_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**primary_limit_angle**
`🔗<class_LookAtModifier3D_property_primary_limit_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_limit_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_primary_limit_angle**()

The limit angle of the primary rotation when
`symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_primary_negative_damp_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**primary_negative_damp_threshold**
`🔗<class_LookAtModifier3D_property_primary_negative_damp_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_negative_damp_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_primary_negative_damp_threshold**()

The threshold to start damping for
`primary_negative_limit_angle<class_LookAtModifier3D_property_primary_negative_limit_angle>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_primary_negative_limit_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**primary_negative_limit_angle**
`🔗<class_LookAtModifier3D_property_primary_negative_limit_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_negative_limit_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_primary_negative_limit_angle**()

The limit angle of negative side of the primary rotation when
`symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_primary_positive_damp_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**primary_positive_damp_threshold**
`🔗<class_LookAtModifier3D_property_primary_positive_damp_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_positive_damp_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_primary_positive_damp_threshold**()

The threshold to start damping for
`primary_positive_limit_angle<class_LookAtModifier3D_property_primary_positive_limit_angle>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_primary_positive_limit_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**primary_positive_limit_angle**
`🔗<class_LookAtModifier3D_property_primary_positive_limit_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_positive_limit_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_primary_positive_limit_angle**()

The limit angle of positive side of the primary rotation when
`symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_primary_rotation_axis}
::: rst-class
classref-property
:::
::::

`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}
**primary_rotation_axis** = `1`
`🔗<class_LookAtModifier3D_property_primary_rotation_axis>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_rotation_axis**(value:
  `Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"})
- `Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}
  **get_primary_rotation_axis**()

The axis of the first rotation. This
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} works by compositing the rotation by Euler angles to prevent
to rotate the
`forward_axis<class_LookAtModifier3D_property_forward_axis>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_secondary_damp_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**secondary_damp_threshold**
`🔗<class_LookAtModifier3D_property_secondary_damp_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secondary_damp_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_secondary_damp_threshold**()

The threshold to start damping for
`secondary_limit_angle<class_LookAtModifier3D_property_secondary_limit_angle>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_secondary_limit_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**secondary_limit_angle**
`🔗<class_LookAtModifier3D_property_secondary_limit_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secondary_limit_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_secondary_limit_angle**()

The limit angle of the secondary rotation when
`symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_secondary_negative_damp_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**secondary_negative_damp_threshold**
`🔗<class_LookAtModifier3D_property_secondary_negative_damp_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secondary_negative_damp_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_secondary_negative_damp_threshold**()

The threshold to start damping for
`secondary_negative_limit_angle<class_LookAtModifier3D_property_secondary_negative_limit_angle>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_secondary_negative_limit_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**secondary_negative_limit_angle**
`🔗<class_LookAtModifier3D_property_secondary_negative_limit_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secondary_negative_limit_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_secondary_negative_limit_angle**()

The limit angle of negative side of the secondary rotation when
`symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_secondary_positive_damp_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**secondary_positive_damp_threshold**
`🔗<class_LookAtModifier3D_property_secondary_positive_damp_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secondary_positive_damp_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_secondary_positive_damp_threshold**()

The threshold to start damping for
`secondary_positive_limit_angle<class_LookAtModifier3D_property_secondary_positive_limit_angle>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_secondary_positive_limit_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**secondary_positive_limit_angle**
`🔗<class_LookAtModifier3D_property_secondary_positive_limit_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secondary_positive_limit_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_secondary_positive_limit_angle**()

The limit angle of positive side of the secondary rotation when
`symmetry_limitation<class_LookAtModifier3D_property_symmetry_limitation>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_symmetry_limitation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **symmetry_limitation**
`🔗<class_LookAtModifier3D_property_symmetry_limitation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_symmetry_limitation**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_limitation_symmetry**()

If `true`, the limitations are spread from the bone symmetrically.

If `false`, the limitation can be specified separately for each side of
the bone rest.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_target_node}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **target_node**
= `NodePath("")`
`🔗<class_LookAtModifier3D_property_target_node>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target_node**()

The `NodePath<class_NodePath>`{.interpreted-text role="ref"} to the node
that is the target for the look at modification. This node is what the
modification will rotate the bone to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_transition_type}
::: rst-class
classref-property
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **transition_type** = `0`
`🔗<class_LookAtModifier3D_property_transition_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transition_type**(value:
  `TransitionType<enum_Tween_TransitionType>`{.interpreted-text
  role="ref"})
- `TransitionType<enum_Tween_TransitionType>`{.interpreted-text
  role="ref"} **get_transition_type**()

The transition type of the time-based interpolation. See also
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_use_angle_limitation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_angle_limitation** = `false`
`🔗<class_LookAtModifier3D_property_use_angle_limitation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_angle_limitation**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_angle_limitation**()

If `true`, limits the amount of rotation. For example, this helps to
prevent a character\'s neck from rotating 360 degrees.

\*\*Note:\*\* As with
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}
blending, interpolation is provided that favors
`Skeleton3D.get_bone_rest()<class_Skeleton3D_method_get_bone_rest>`{.interpreted-text
role="ref"}. This means that interpolation does not select the shortest
path in some cases.

\*\*Note:\*\* Some values for
`transition_type<class_LookAtModifier3D_property_transition_type>`{.interpreted-text
role="ref"} (such as
`Tween.TRANS_BACK<class_Tween_constant_TRANS_BACK>`{.interpreted-text
role="ref"},
`Tween.TRANS_ELASTIC<class_Tween_constant_TRANS_ELASTIC>`{.interpreted-text
role="ref"}, and
`Tween.TRANS_SPRING<class_Tween_constant_TRANS_SPRING>`{.interpreted-text
role="ref"}) may exceed the limitations. If interpolation occurs while
overshooting the limitations, the result might not respect the bone
rest.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_property_use_secondary_rotation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_secondary_rotation** = `true`
`🔗<class_LookAtModifier3D_property_use_secondary_rotation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_secondary_rotation**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_secondary_rotation**()

If `true`, provides rotation by two axes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_LookAtModifier3D_method_get_interpolation_remaining}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_interpolation_remaining**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LookAtModifier3D_method_get_interpolation_remaining>`{.interpreted-text
role="ref"}

Returns the remaining seconds of the time-based interpolation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_method_is_interpolating}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_interpolating**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LookAtModifier3D_method_is_interpolating>`{.interpreted-text
role="ref"}

Returns `true` if time-based interpolation is running. If `true`, it is
equivalent to
`get_interpolation_remaining()<class_LookAtModifier3D_method_get_interpolation_remaining>`{.interpreted-text
role="ref"} returning `0.0`.

This is useful to determine whether a **LookAtModifier3D** can be
removed safely.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LookAtModifier3D_method_is_target_within_limitation}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_target_within_limitation**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LookAtModifier3D_method_is_target_within_limitation>`{.interpreted-text
role="ref"}

Returns whether the target is within the angle limitations. It is useful
for unsetting the
`target_node<class_LookAtModifier3D_property_target_node>`{.interpreted-text
role="ref"} when the target is outside of the angle limitations.

\*\*Note:\*\* The value is updated after
`SkeletonModifier3D._process_modification()<class_SkeletonModifier3D_private_method__process_modification>`{.interpreted-text
role="ref"}. To retrieve this value correctly, we recommend using the
signal
`SkeletonModifier3D.modification_processed<class_SkeletonModifier3D_signal_modification_processed>`{.interpreted-text
role="ref"}.
