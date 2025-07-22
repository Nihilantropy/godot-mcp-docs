github_url
:   hide

::: {.meta keywords="tag"}
:::

# BoneAttachment3D {#class_BoneAttachment3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

А node that dynamically copies or overrides the 3D transform of a bone
in its parent `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This node selects a bone in a
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} and
attaches to it. This means that the **BoneAttachment3D** node will
either dynamically copy or override the 3D transform of the selected
bone.

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

:::: {#class_BoneAttachment3D_property_bone_idx}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bone_idx** = `-1`
`🔗<class_BoneAttachment3D_property_bone_idx>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_idx**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bone_idx**()

The index of the attached bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneAttachment3D_property_bone_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **bone_name** =
`""` `🔗<class_BoneAttachment3D_property_bone_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_bone_name**()

The name of the attached bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneAttachment3D_property_external_skeleton}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**external_skeleton**
`🔗<class_BoneAttachment3D_property_external_skeleton>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_external_skeleton**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_external_skeleton**()

The `NodePath<class_NodePath>`{.interpreted-text role="ref"} to the
external `Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneAttachment3D_property_override_pose}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **override_pose** =
`false`
`🔗<class_BoneAttachment3D_property_override_pose>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_override_pose**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_override_pose**()

Whether the **BoneAttachment3D** node will override the bone pose of the
bone it is attached to. When set to `true`, the **BoneAttachment3D**
node can change the pose of the bone. When set to `false`, the
**BoneAttachment3D** will always be set to the bone\'s transform.

\*\*Note:\*\* This override performs interruptively in the skeleton
update process using signals due to the old design. It may cause
unintended behavior when used at the same time with
`SkeletonModifier3D<class_SkeletonModifier3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneAttachment3D_property_use_external_skeleton}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_external_skeleton** = `false`
`🔗<class_BoneAttachment3D_property_use_external_skeleton>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_external_skeleton**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_external_skeleton**()

Whether the **BoneAttachment3D** node will use an external
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node rather
than attempting to use its parent node as the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}. When set
to `true`, the **BoneAttachment3D** node will use the external
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node set in
`external_skeleton<class_BoneAttachment3D_property_external_skeleton>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_BoneAttachment3D_method_get_skeleton}
::: rst-class
classref-method
:::
::::

`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"}
**get_skeleton**()
`🔗<class_BoneAttachment3D_method_get_skeleton>`{.interpreted-text
role="ref"}

Returns the parent or external
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} node if it
exists, otherwise returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoneAttachment3D_method_on_skeleton_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**on_skeleton_update**()
`🔗<class_BoneAttachment3D_method_on_skeleton_update>`{.interpreted-text
role="ref"}

A function that is called automatically when the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} is updated.
This function is where the **BoneAttachment3D** node updates its
position so it is correctly bound when it is *not* set to override the
bone pose.
