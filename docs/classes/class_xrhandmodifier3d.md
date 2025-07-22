github_url
:   hide

# XRHandModifier3D {#class_XRHandModifier3D}

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node for driving hand meshes from
`XRHandTracker<class_XRHandTracker>`{.interpreted-text role="ref"} data.

::: rst-class
classref-introduction-group
:::

## Description

This node uses hand tracking data from an
`XRHandTracker<class_XRHandTracker>`{.interpreted-text role="ref"} to
pose the skeleton of a hand mesh.

Positioning of hands is performed by creating an
`XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"} ancestor of the
hand mesh driven by the same
`XRHandTracker<class_XRHandTracker>`{.interpreted-text role="ref"}.

The hand tracking position-data is scaled by
`Skeleton3D.motion_scale<class_Skeleton3D_property_motion_scale>`{.interpreted-text
role="ref"} when applied to the skeleton, which can be used to adjust
the tracked hand to match the scale of the hand model.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `XR documentation index <../tutorials/xr/index>`{.interpreted-text
  role="doc"}

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

:::: {#enum_XRHandModifier3D_BoneUpdate}
::: rst-class
classref-enumeration
:::
::::

enum **BoneUpdate**:
`🔗<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text role="ref"}

:::: {#class_XRHandModifier3D_constant_BONE_UPDATE_FULL}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **BONE_UPDATE_FULL** = `0`

The skeleton\'s bones are fully updated (both position and rotation) to
match the tracked bones.

:::: {#class_XRHandModifier3D_constant_BONE_UPDATE_ROTATION_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton\'s bones are only rotated to align with the tracked bones,
preserving bone length.

:::: {#class_XRHandModifier3D_constant_BONE_UPDATE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **BONE_UPDATE_MAX** = `2`

Represents the size of the
`BoneUpdate<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRHandModifier3D_property_bone_update}
::: rst-class
classref-property
:::
::::

`BoneUpdate<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **bone_update** = `0`
`🔗<class_XRHandModifier3D_property_bone_update>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_update**(value:
  `BoneUpdate<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text
  role="ref"})
- `BoneUpdate<enum_XRHandModifier3D_BoneUpdate>`{.interpreted-text
  role="ref"} **get_bone_update**()

Specifies the type of updates to perform on the bones.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandModifier3D_property_hand_tracker}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**hand_tracker** = `&"/user/hand_tracker/left"`
`🔗<class_XRHandModifier3D_property_hand_tracker>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hand_tracker**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_hand_tracker**()

The name of the `XRHandTracker<class_XRHandTracker>`{.interpreted-text
role="ref"} registered with `XRServer<class_XRServer>`{.interpreted-text
role="ref"} to obtain the hand tracking data from.
