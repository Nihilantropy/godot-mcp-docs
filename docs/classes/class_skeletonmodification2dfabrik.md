github_url
:   hide

# SkeletonModification2DFABRIK {#class_SkeletonModification2DFABRIK}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A modification that uses FABRIK to manipulate a series of
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} nodes to reach a
target.

::: rst-class
classref-introduction-group
:::

## Description

This
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} uses an algorithm called Forward And Backward Reaching
Inverse Kinematics, or FABRIK, to rotate a bone chain so that it reaches
a target.

FABRIK works by knowing the positions and lengths of a series of bones,
typically called a \"bone chain\". It first starts by running a forward
pass, which places the final bone at the target\'s position. Then all
other bones are moved towards the tip bone, so they stay at the defined
bone length away. Then a backwards pass is performed, where the
root/first bone in the FABRIK chain is placed back at the origin. Then
all other bones are moved so they stay at the defined bone length away.
This positions the bone chain so that it reaches the target when
possible, but all of the bones stay the correct length away from each
other.

Because of how FABRIK works, it often gives more natural results than
those seen in
`SkeletonModification2DCCDIK<class_SkeletonModification2DCCDIK>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The FABRIK modifier has `fabrik_joints`, which are the
data objects that hold the data for each joint in the FABRIK chain. This
is different from `Bone2D<class_Bone2D>`{.interpreted-text role="ref"}
nodes! FABRIK joints hold the data needed for each
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} in the bone chain
used by FABRIK.

To help control how the FABRIK joints move, a magnet vector can be
passed, which can nudge the bones in a certain direction prior to
solving, giving a level of control over the final result.

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

:::: {#class_SkeletonModification2DFABRIK_property_fabrik_data_chain_length}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**fabrik_data_chain_length** = `0`
`🔗<class_SkeletonModification2DFABRIK_property_fabrik_data_chain_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fabrik_data_chain_length**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_fabrik_data_chain_length**()

The number of FABRIK joints in the FABRIK modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_property_target_nodepath}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**target_nodepath** = `NodePath("")`
`🔗<class_SkeletonModification2DFABRIK_property_target_nodepath>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target_node**()

The NodePath to the node that is the target for the FABRIK modification.
This node is what the FABRIK chain will attempt to rotate the bone chain
to.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModification2DFABRIK_method_get_fabrik_joint_bone2d_node}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_fabrik_joint_bone2d_node**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_bone2d_node>`{.interpreted-text
role="ref"}

Returns the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
assigned to the FABRIK joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_method_get_fabrik_joint_bone_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_fabrik_joint_bone_index**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_bone_index>`{.interpreted-text
role="ref"}

Returns the index of the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node assigned to the FABRIK joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_method_get_fabrik_joint_magnet_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_fabrik_joint_magnet_position**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_magnet_position>`{.interpreted-text
role="ref"}

Returns the magnet position vector for the joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_method_get_fabrik_joint_use_target_rotation}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_fabrik_joint_use_target_rotation**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DFABRIK_method_get_fabrik_joint_use_target_rotation>`{.interpreted-text
role="ref"}

Returns whether the joint is using the target\'s rotation rather than
allowing FABRIK to rotate the joint. This option only applies to the
tip/final joint in the chain.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_method_set_fabrik_joint_bone2d_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_fabrik_joint_bone2d_node**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, bone2d_nodepath:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_bone2d_node>`{.interpreted-text
role="ref"}

Sets the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
assigned to the FABRIK joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_method_set_fabrik_joint_bone_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_fabrik_joint_bone_index**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_bone_index>`{.interpreted-text
role="ref"}

Sets the bone index, `bone_idx`, of the FABRIK joint at `joint_idx`.
When possible, this will also update the `bone2d_node` of the FABRIK
joint based on data provided by the linked skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_method_set_fabrik_joint_magnet_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_fabrik_joint_magnet_position**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, magnet_position:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_magnet_position>`{.interpreted-text
role="ref"}

Sets the magnet position vector for the joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DFABRIK_method_set_fabrik_joint_use_target_rotation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_fabrik_joint_use_target_rotation**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, use_target_rotation:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DFABRIK_method_set_fabrik_joint_use_target_rotation>`{.interpreted-text
role="ref"}

Sets whether the joint at `joint_idx` will use the target node\'s
rotation rather than letting FABRIK rotate the node.

\*\*Note:\*\* This option only works for the tip/final joint in the
chain. For all other nodes, this option will be ignored.
