github_url
:   hide

# SkeletonModifier3D {#class_SkeletonModifier3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`BoneConstraint3D<class_BoneConstraint3D>`{.interpreted-text
role="ref"},
`LookAtModifier3D<class_LookAtModifier3D>`{.interpreted-text
role="ref"},
`ModifierBoneTarget3D<class_ModifierBoneTarget3D>`{.interpreted-text
role="ref"},
`PhysicalBoneSimulator3D<class_PhysicalBoneSimulator3D>`{.interpreted-text
role="ref"},
`RetargetModifier3D<class_RetargetModifier3D>`{.interpreted-text
role="ref"}, `SkeletonIK3D<class_SkeletonIK3D>`{.interpreted-text
role="ref"},
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"},
`XRBodyModifier3D<class_XRBodyModifier3D>`{.interpreted-text
role="ref"},
`XRHandModifier3D<class_XRHandModifier3D>`{.interpreted-text role="ref"}

A node that may modify a Skeleton3D\'s bones.

::: rst-class
classref-introduction-group
:::

## Description

**SkeletonModifier3D** retrieves a target
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} by having a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} parent.

If there is an `AnimationMixer<class_AnimationMixer>`{.interpreted-text
role="ref"}, a modification always performs after playback process of
the `AnimationMixer<class_AnimationMixer>`{.interpreted-text
role="ref"}.

This node should be used to implement custom IK solvers, constraints, or
skeleton physics.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Design of the Skeleton Modifier
  3D](https://godotengine.org/article/design-of-the-skeleton-modifier-3d/)

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

## Signals

:::: {#class_SkeletonModifier3D_signal_modification_processed}
::: rst-class
classref-signal
:::
::::

**modification_processed**()
`🔗<class_SkeletonModifier3D_signal_modification_processed>`{.interpreted-text
role="ref"}

Notifies when the modification have been finished.

\*\*Note:\*\* If you want to get the modified bone pose by the modifier,
you must use
`Skeleton3D.get_bone_pose()<class_Skeleton3D_method_get_bone_pose>`{.interpreted-text
role="ref"} or
`Skeleton3D.get_bone_global_pose()<class_Skeleton3D_method_get_bone_global_pose>`{.interpreted-text
role="ref"} at the moment this signal is fired.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_SkeletonModifier3D_BoneAxis}
::: rst-class
classref-enumeration
:::
::::

enum **BoneAxis**:
`🔗<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text role="ref"}

:::: {#class_SkeletonModifier3D_constant_BONE_AXIS_PLUS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **BONE_AXIS_PLUS_X** = `0`

Enumerated value for the +X axis.

:::: {#class_SkeletonModifier3D_constant_BONE_AXIS_MINUS_X}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **BONE_AXIS_MINUS_X** = `1`

Enumerated value for the -X axis.

:::: {#class_SkeletonModifier3D_constant_BONE_AXIS_PLUS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **BONE_AXIS_PLUS_Y** = `2`

Enumerated value for the +Y axis.

:::: {#class_SkeletonModifier3D_constant_BONE_AXIS_MINUS_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **BONE_AXIS_MINUS_Y** = `3`

Enumerated value for the -Y axis.

:::: {#class_SkeletonModifier3D_constant_BONE_AXIS_PLUS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **BONE_AXIS_PLUS_Z** = `4`

Enumerated value for the +Z axis.

:::: {#class_SkeletonModifier3D_constant_BONE_AXIS_MINUS_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneAxis<enum_SkeletonModifier3D_BoneAxis>`{.interpreted-text
role="ref"} **BONE_AXIS_MINUS_Z** = `5`

Enumerated value for the -Z axis.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SkeletonModifier3D_property_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **active** = `true`
`🔗<class_SkeletonModifier3D_property_active>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_active**()

If `true`, the **SkeletonModifier3D** will be processing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModifier3D_property_influence}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **influence** = `1.0`
`🔗<class_SkeletonModifier3D_property_influence>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_influence**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_influence**()

Sets the influence of the modification.

\*\*Note:\*\* This value is used by
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} to blend,
so the **SkeletonModifier3D** should always apply only 100% of the
result without interpolation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModifier3D_private_method__process_modification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_process_modification**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModifier3D_private_method__process_modification>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`_process_modification_with_delta()<class_SkeletonModifier3D_private_method__process_modification_with_delta>`{.interpreted-text
role="ref"} instead.

Override this virtual method to implement a custom skeleton modifier.
You should do things like get the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}\'s current
pose and apply the pose here.

`_process_modification()<class_SkeletonModifier3D_private_method__process_modification>`{.interpreted-text
role="ref"} must not apply
`influence<class_SkeletonModifier3D_property_influence>`{.interpreted-text
role="ref"} to bone poses because the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
automatically applies influence to all bone poses set by the modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModifier3D_private_method__process_modification_with_delta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_process_modification_with_delta**(delta:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModifier3D_private_method__process_modification_with_delta>`{.interpreted-text
role="ref"}

Override this virtual method to implement a custom skeleton modifier.
You should do things like get the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}\'s current
pose and apply the pose here.

`_process_modification_with_delta()<class_SkeletonModifier3D_private_method__process_modification_with_delta>`{.interpreted-text
role="ref"} must not apply
`influence<class_SkeletonModifier3D_property_influence>`{.interpreted-text
role="ref"} to bone poses because the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
automatically applies influence to all bone poses set by the modifier.

`delta` is passed from parent
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}. See also
`Skeleton3D.advance()<class_Skeleton3D_method_advance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModifier3D_private_method__skeleton_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_skeleton_changed**(old_skeleton:
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"},
new_skeleton: `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModifier3D_private_method__skeleton_changed>`{.interpreted-text
role="ref"}

Called when the skeleton is changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModifier3D_private_method__validate_bone_names}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_validate_bone_names**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModifier3D_private_method__validate_bone_names>`{.interpreted-text
role="ref"}

Called when bone name and index need to be validated such as the timing
of the entering tree or changing skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModifier3D_method_get_skeleton}
::: rst-class
classref-method
:::
::::

`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
**get_skeleton**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModifier3D_method_get_skeleton>`{.interpreted-text
role="ref"}

Get parent `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
node if found.
