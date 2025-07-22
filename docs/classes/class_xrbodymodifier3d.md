github_url
:   hide

# XRBodyModifier3D {#class_XRBodyModifier3D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node for driving body meshes from
`XRBodyTracker<class_XRBodyTracker>`{.interpreted-text role="ref"} data.

::: rst-class
classref-introduction-group
:::

## Description

This node uses body tracking data from an
`XRBodyTracker<class_XRBodyTracker>`{.interpreted-text role="ref"} to
pose the skeleton of a body mesh.

Positioning of the body is performed by creating an
`XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"} ancestor of the
body mesh driven by the same
`XRBodyTracker<class_XRBodyTracker>`{.interpreted-text role="ref"}.

The body tracking position-data is scaled by
`Skeleton3D.motion_scale<class_Skeleton3D_property_motion_scale>`{.interpreted-text
role="ref"} when applied to the skeleton, which can be used to adjust
the tracked body to match the scale of the body model.

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

:::: {#enum_XRBodyModifier3D_BodyUpdate}
::: rst-class
classref-enumeration
:::
::::

flags **BodyUpdate**:
`🔗<enum_XRBodyModifier3D_BodyUpdate>`{.interpreted-text role="ref"}

:::: {#class_XRBodyModifier3D_constant_BODY_UPDATE_UPPER_BODY}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`{.interpreted-text
role="ref"} **BODY_UPDATE_UPPER_BODY** = `1`

The skeleton\'s upper body joints are updated.

:::: {#class_XRBodyModifier3D_constant_BODY_UPDATE_LOWER_BODY}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`{.interpreted-text
role="ref"} **BODY_UPDATE_LOWER_BODY** = `2`

The skeleton\'s lower body joints are updated.

:::: {#class_XRBodyModifier3D_constant_BODY_UPDATE_HANDS}
::: rst-class
classref-enumeration-constant
:::
::::

`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`{.interpreted-text
role="ref"} **BODY_UPDATE_HANDS** = `4`

The skeleton\'s hand joints are updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRBodyModifier3D_BoneUpdate}
::: rst-class
classref-enumeration
:::
::::

enum **BoneUpdate**:
`🔗<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text role="ref"}

:::: {#class_XRBodyModifier3D_constant_BONE_UPDATE_FULL}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **BONE_UPDATE_FULL** = `0`

The skeleton\'s bones are fully updated (both position and rotation) to
match the tracked bones.

:::: {#class_XRBodyModifier3D_constant_BONE_UPDATE_ROTATION_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **BONE_UPDATE_ROTATION_ONLY** = `1`

The skeleton\'s bones are only rotated to align with the tracked bones,
preserving bone length.

:::: {#class_XRBodyModifier3D_constant_BONE_UPDATE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **BONE_UPDATE_MAX** = `2`

Represents the size of the
`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRBodyModifier3D_property_body_tracker}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**body_tracker** = `&"/user/body_tracker"`
`🔗<class_XRBodyModifier3D_property_body_tracker>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_body_tracker**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_body_tracker**()

The name of the `XRBodyTracker<class_XRBodyTracker>`{.interpreted-text
role="ref"} registered with `XRServer<class_XRServer>`{.interpreted-text
role="ref"} to obtain the body tracking data from.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRBodyModifier3D_property_body_update}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`{.interpreted-text
role="ref"}\] **body_update** = `7`
`🔗<class_XRBodyModifier3D_property_body_update>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_body_update**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`BodyUpdate<enum_XRBodyModifier3D_BodyUpdate>`{.interpreted-text
  role="ref"}\] **get_body_update**()

Specifies the body parts to update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRBodyModifier3D_property_bone_update}
::: rst-class
classref-property
:::
::::

`BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text
role="ref"} **bone_update** = `0`
`🔗<class_XRBodyModifier3D_property_bone_update>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_update**(value:
  `BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text
  role="ref"})
- `BoneUpdate<enum_XRBodyModifier3D_BoneUpdate>`{.interpreted-text
  role="ref"} **get_bone_update**()

Specifies the type of updates to perform on the bones.
