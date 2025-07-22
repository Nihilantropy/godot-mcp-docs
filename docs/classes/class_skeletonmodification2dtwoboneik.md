github_url
:   hide

# SkeletonModification2DTwoBoneIK {#class_SkeletonModification2DTwoBoneIK}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A modification that rotates two bones using the law of cosines to reach
the target.

::: rst-class
classref-introduction-group
:::

## Description

This
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} uses an algorithm typically called TwoBoneIK. This algorithm
works by leveraging the law of cosines and the lengths of the bones to
figure out what rotation the bones currently have, and what rotation
they need to make a complete triangle, where the first bone, the second
bone, and the target form the three vertices of the triangle. Because
the algorithm works by making a triangle, it can only operate on two
bones.

TwoBoneIK is great for arms, legs, and really any joints that can be
represented by just two bones that bend to reach a target. This solver
is more lightweight than
`SkeletonModification2DFABRIK<class_SkeletonModification2DFABRIK>`{.interpreted-text
role="ref"}, but gives similar, natural looking results.

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

:::: {#class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_bend_direction**
= `false`
`🔗<class_SkeletonModification2DTwoBoneIK_property_flip_bend_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_bend_direction**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_flip_bend_direction**()

If `true`, the bones in the modification will bend outward as opposed to
inwards when contracting. If `false`, the bones will bend inwards when
contracting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**target_maximum_distance** = `0.0`
`🔗<class_SkeletonModification2DTwoBoneIK_property_target_maximum_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_maximum_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_target_maximum_distance**()

The maximum distance the target can be at. If the target is farther than
this distance, the modification will solve as if it\'s at this maximum
distance. When set to `0`, the modification will solve without distance
constraints.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**target_minimum_distance** = `0.0`
`🔗<class_SkeletonModification2DTwoBoneIK_property_target_minimum_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_minimum_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_target_minimum_distance**()

The minimum distance the target can be at. If the target is closer than
this distance, the modification will solve as if it\'s at this minimum
distance. When set to `0`, the modification will solve without distance
constraints.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_property_target_nodepath}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**target_nodepath** = `NodePath("")`
`🔗<class_SkeletonModification2DTwoBoneIK_property_target_nodepath>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target_node**()

The NodePath to the node that is the target for the TwoBoneIK
modification. This node is what the modification will use when bending
the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_joint_one_bone2d_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone2d_node>`{.interpreted-text
role="ref"}

Returns the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
that is being used as the first bone in the TwoBoneIK modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_joint_one_bone_idx**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_one_bone_idx>`{.interpreted-text
role="ref"}

Returns the index of the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node that is being used as the first bone in the TwoBoneIK
modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_joint_two_bone2d_node**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone2d_node>`{.interpreted-text
role="ref"}

Returns the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
that is being used as the second bone in the TwoBoneIK modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_joint_two_bone_idx**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DTwoBoneIK_method_get_joint_two_bone_idx>`{.interpreted-text
role="ref"}

Returns the index of the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node that is being used as the second bone in the TwoBoneIK
modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_one_bone2d_node**(bone2d_node:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone2d_node>`{.interpreted-text
role="ref"}

Sets the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node that
is being used as the first bone in the TwoBoneIK modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_one_bone_idx**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_one_bone_idx>`{.interpreted-text
role="ref"}

Sets the index of the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node that is being used as the first bone in the TwoBoneIK
modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_two_bone2d_node**(bone2d_node:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone2d_node>`{.interpreted-text
role="ref"}

Sets the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node that
is being used as the second bone in the TwoBoneIK modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_joint_two_bone_idx**(bone_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SkeletonModification2DTwoBoneIK_method_set_joint_two_bone_idx>`{.interpreted-text
role="ref"}

Sets the index of the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node that is being used as the second bone in the TwoBoneIK
modification.
