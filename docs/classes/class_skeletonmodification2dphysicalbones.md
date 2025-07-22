github_url
:   hide

# SkeletonModification2DPhysicalBones {#class_SkeletonModification2DPhysicalBones}

**Experimental:** Physical bones may be changed in the future to perform
the position update of `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} on their own, without needing this resource.

**Inherits:**
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A modification that applies the transforms of
`PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text role="ref"}
nodes to `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-introduction-group
:::

## Description

This modification takes the transforms of
`PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text role="ref"}
nodes and applies them to `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} nodes. This allows the
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} nodes to react to
physics thanks to the linked
`PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text role="ref"}
nodes.

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

:::: {#class_SkeletonModification2DPhysicalBones_property_physical_bone_chain_length}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**physical_bone_chain_length** = `0`
`🔗<class_SkeletonModification2DPhysicalBones_property_physical_bone_chain_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physical_bone_chain_length**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_physical_bone_chain_length**()

The number of `PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text
role="ref"} nodes linked in this modification.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModification2DPhysicalBones_method_fetch_physical_bones}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fetch_physical_bones**()
`🔗<class_SkeletonModification2DPhysicalBones_method_fetch_physical_bones>`{.interpreted-text
role="ref"}

Empties the list of
`PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text role="ref"}
nodes and populates it with all
`PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text role="ref"}
nodes that are children of the
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DPhysicalBones_method_get_physical_bone_node}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_physical_bone_node**(joint_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DPhysicalBones_method_get_physical_bone_node>`{.interpreted-text
role="ref"}

Returns the `PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text
role="ref"} node at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DPhysicalBones_method_set_physical_bone_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_physical_bone_node**(joint_idx: `int<class_int>`{.interpreted-text
role="ref"}, physicalbone2d_node:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DPhysicalBones_method_set_physical_bone_node>`{.interpreted-text
role="ref"}

Sets the `PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text
role="ref"} node at `joint_idx`.

\*\*Note:\*\* This is just the index used for this modification, not the
bone index used in the `Skeleton2D<class_Skeleton2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DPhysicalBones_method_start_simulation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start_simulation**(bones: `Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_SkeletonModification2DPhysicalBones_method_start_simulation>`{.interpreted-text
role="ref"}

Tell the `PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text
role="ref"} nodes to start simulating and interacting with the physics
world.

Optionally, an array of bone names can be passed to this function, and
that will cause only
`PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text role="ref"}
nodes with those names to start simulating.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DPhysicalBones_method_stop_simulation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**stop_simulation**(bones: `Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_SkeletonModification2DPhysicalBones_method_stop_simulation>`{.interpreted-text
role="ref"}

Tell the `PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text
role="ref"} nodes to stop simulating and interacting with the physics
world.

Optionally, an array of bone names can be passed to this function, and
that will cause only
`PhysicalBone2D<class_PhysicalBone2D>`{.interpreted-text role="ref"}
nodes with those names to stop simulating.
