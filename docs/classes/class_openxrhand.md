github_url
:   hide

# OpenXRHand {#class_OpenXRHand}

**Deprecated:** Use
`XRHandModifier3D<class_XRHandModifier3D>`{.interpreted-text role="ref"}
instead.

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node supporting hand and finger tracking in OpenXR.

::: rst-class
classref-introduction-group
:::

## Description

This node enables OpenXR\'s hand tracking functionality. The node should
be a child node of an `XROrigin3D<class_XROrigin3D>`{.interpreted-text
role="ref"} node, tracking will update its position to the player\'s
tracked hand Palm joint location (the center of the middle finger\'s
metacarpal bone). This node also updates the skeleton of a properly
skinned hand or avatar model.

If the skeleton is a hand (one of the hand bones is the root node of the
skeleton), then the skeleton will be placed relative to the hand palm
location and the hand mesh and skeleton should be children of the
OpenXRHand node.

If the hand bones are part of a full skeleton, then the root of the hand
will keep its location with the assumption that IK is used to position
the hand and arm.

By default the skeleton hand bones are repositioned to match the size of
the tracked hand. To preserve the modeled bone sizes change
`bone_update<class_OpenXRHand_property_bone_update>`{.interpreted-text
role="ref"} to apply rotation only.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_OpenXRHand_Hands}
::: rst-class
classref-enumeration
:::
::::

enum **Hands**: `🔗<enum_OpenXRHand_Hands>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRHand_constant_HAND_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`Hands<enum_OpenXRHand_Hands>`{.interpreted-text role="ref"}
**HAND_LEFT** = `0`

Tracking the player\'s left hand.

:::: {#class_OpenXRHand_constant_HAND_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Hands<enum_OpenXRHand_Hands>`{.interpreted-text role="ref"}
**HAND_RIGHT** = `1`

Tracking the player\'s right hand.

:::: {#class_OpenXRHand_constant_HAND_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Hands<enum_OpenXRHand_Hands>`{.interpreted-text role="ref"}
**HAND_MAX** = `2`

Maximum supported hands.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRHand_MotionRange}
::: rst-class
classref-enumeration
:::
::::

enum **MotionRange**:
`🔗<enum_OpenXRHand_MotionRange>`{.interpreted-text role="ref"}

:::: {#class_OpenXRHand_constant_MOTION_RANGE_UNOBSTRUCTED}
::: rst-class
classref-enumeration-constant
:::
::::

`MotionRange<enum_OpenXRHand_MotionRange>`{.interpreted-text role="ref"}
**MOTION_RANGE_UNOBSTRUCTED** = `0`

When player grips, hand skeleton will form a full fist.

:::: {#class_OpenXRHand_constant_MOTION_RANGE_CONFORM_TO_CONTROLLER}
::: rst-class
classref-enumeration-constant
:::
::::

`MotionRange<enum_OpenXRHand_MotionRange>`{.interpreted-text role="ref"}
**MOTION_RANGE_CONFORM_TO_CONTROLLER** = `1`

When player grips, hand skeleton conforms to the controller the player
is holding.

:::: {#class_OpenXRHand_constant_MOTION_RANGE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`MotionRange<enum_OpenXRHand_MotionRange>`{.interpreted-text role="ref"}
**MOTION_RANGE_MAX** = `2`

Maximum supported motion ranges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRHand_SkeletonRig}
::: rst-class
classref-enumeration
:::
::::

enum **SkeletonRig**:
`🔗<enum_OpenXRHand_SkeletonRig>`{.interpreted-text role="ref"}

:::: {#class_OpenXRHand_constant_SKELETON_RIG_OPENXR}
::: rst-class
classref-enumeration-constant
:::
::::

`SkeletonRig<enum_OpenXRHand_SkeletonRig>`{.interpreted-text role="ref"}
**SKELETON_RIG_OPENXR** = `0`

An OpenXR compliant skeleton.

:::: {#class_OpenXRHand_constant_SKELETON_RIG_HUMANOID}
::: rst-class
classref-enumeration-constant
:::
::::

`SkeletonRig<enum_OpenXRHand_SkeletonRig>`{.interpreted-text role="ref"}
**SKELETON_RIG_HUMANOID** = `1`

A
`SkeletonProfileHumanoid<class_SkeletonProfileHumanoid>`{.interpreted-text
role="ref"} compliant skeleton.

:::: {#class_OpenXRHand_constant_SKELETON_RIG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SkeletonRig<enum_OpenXRHand_SkeletonRig>`{.interpreted-text role="ref"}
**SKELETON_RIG_MAX** = `2`

Maximum supported hands.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRHand_BoneUpdate}
::: rst-class
classref-enumeration
:::
::::

enum **BoneUpdate**: `🔗<enum_OpenXRHand_BoneUpdate>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRHand_constant_BONE_UPDATE_FULL}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_OpenXRHand_BoneUpdate>`{.interpreted-text role="ref"}
**BONE_UPDATE_FULL** = `0`

The skeletons bones are fully updated (both position and rotation) to
match the tracked bones.

:::: {#class_OpenXRHand_constant_BONE_UPDATE_ROTATION_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_OpenXRHand_BoneUpdate>`{.interpreted-text role="ref"}
**BONE_UPDATE_ROTATION_ONLY** = `1`

The skeletons bones are only rotated to align with the tracked bones,
preserving bone length.

:::: {#class_OpenXRHand_constant_BONE_UPDATE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_OpenXRHand_BoneUpdate>`{.interpreted-text role="ref"}
**BONE_UPDATE_MAX** = `2`

Maximum supported bone update mode.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OpenXRHand_property_bone_update}
::: rst-class
classref-property
:::
::::

`BoneUpdate<enum_OpenXRHand_BoneUpdate>`{.interpreted-text role="ref"}
**bone_update** = `0`
`🔗<class_OpenXRHand_property_bone_update>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_update**(value:
  `BoneUpdate<enum_OpenXRHand_BoneUpdate>`{.interpreted-text
  role="ref"})
- `BoneUpdate<enum_OpenXRHand_BoneUpdate>`{.interpreted-text role="ref"}
  **get_bone_update**()

Specify the type of updates to perform on the bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRHand_property_hand}
::: rst-class
classref-property
:::
::::

`Hands<enum_OpenXRHand_Hands>`{.interpreted-text role="ref"} **hand** =
`0` `🔗<class_OpenXRHand_property_hand>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hand**(value: `Hands<enum_OpenXRHand_Hands>`{.interpreted-text
  role="ref"})
- `Hands<enum_OpenXRHand_Hands>`{.interpreted-text role="ref"}
  **get_hand**()

Specifies whether this node tracks the left or right hand of the player.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRHand_property_hand_skeleton}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**hand_skeleton** = `NodePath("")`
`🔗<class_OpenXRHand_property_hand_skeleton>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hand_skeleton**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_hand_skeleton**()

Set a `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node
for which the pose positions will be updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRHand_property_motion_range}
::: rst-class
classref-property
:::
::::

`MotionRange<enum_OpenXRHand_MotionRange>`{.interpreted-text role="ref"}
**motion_range** = `0`
`🔗<class_OpenXRHand_property_motion_range>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motion_range**(value:
  `MotionRange<enum_OpenXRHand_MotionRange>`{.interpreted-text
  role="ref"})
- `MotionRange<enum_OpenXRHand_MotionRange>`{.interpreted-text
  role="ref"} **get_motion_range**()

Set the motion range (if supported) limiting the hand motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRHand_property_skeleton_rig}
::: rst-class
classref-property
:::
::::

`SkeletonRig<enum_OpenXRHand_SkeletonRig>`{.interpreted-text role="ref"}
**skeleton_rig** = `0`
`🔗<class_OpenXRHand_property_skeleton_rig>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skeleton_rig**(value:
  `SkeletonRig<enum_OpenXRHand_SkeletonRig>`{.interpreted-text
  role="ref"})
- `SkeletonRig<enum_OpenXRHand_SkeletonRig>`{.interpreted-text
  role="ref"} **get_skeleton_rig**()

Set the type of skeleton rig the
`hand_skeleton<class_OpenXRHand_property_hand_skeleton>`{.interpreted-text
role="ref"} is compliant with.
