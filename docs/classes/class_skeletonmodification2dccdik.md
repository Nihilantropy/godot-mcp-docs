github_url
:   hide

# SkeletonModification2DCCDIK {#class_SkeletonModification2DCCDIK}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A modification that uses CCDIK to manipulate a series of bones to reach
a target in 2D.

::: rst-class
classref-introduction-group
:::

## Description

This
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} uses an algorithm called Cyclic Coordinate Descent Inverse
Kinematics, or CCDIK, to manipulate a chain of bones in a
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} so it
reaches a defined target.

CCDIK works by rotating a set of bones, typically called a \"bone
chain\", on a single axis. Each bone is rotated to face the target from
the tip (by default), which over a chain of bones allow it to rotate
properly to reach the target. Because the bones only rotate on a single
axis, CCDIK *can* look more robotic than other IK solvers.

\*\*Note:\*\* The CCDIK modifier has `ccdik_joints`, which are the data
objects that hold the data for each joint in the CCDIK chain. This is
different from a bone! CCDIK joints hold the data needed for each bone
in the bone chain used by CCDIK.

CCDIK also fully supports angle constraints, allowing for more control
over how a solution is met.

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

:::: {#class_SkeletonModification2DCCDIK_property_ccdik_data_chain_length}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**ccdik_data_chain_length** = `0`
`🔗<class_SkeletonModification2DCCDIK_property_ccdik_data_chain_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ccdik_data_chain_length**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_ccdik_data_chain_length**()

The number of CCDIK joints in the CCDIK modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_property_target_nodepath}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**target_nodepath** = `NodePath("")`
`🔗<class_SkeletonModification2DCCDIK_property_target_nodepath>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target_node**()

The NodePath to the node that is the target for the CCDIK modification.
This node is what the CCDIK chain will attempt to rotate the bone chain
to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_property_tip_nodepath}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**tip_nodepath** = `NodePath("")`
`🔗<class_SkeletonModification2DCCDIK_property_tip_nodepath>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tip_node**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_tip_node**()

The end position of the CCDIK chain. Typically, this should be a child
of a `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node attached
to the final `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} in the
CCDIK chain.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone2d_node}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_ccdik_joint_bone2d_node**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone2d_node>`{.interpreted-text
role="ref"}

Returns the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
assigned to the CCDIK joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_ccdik_joint_bone_index**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DCCDIK_method_get_ccdik_joint_bone_index>`{.interpreted-text
role="ref"}

Returns the index of the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node assigned to the CCDIK joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_invert}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_ccdik_joint_constraint_angle_invert**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_invert>`{.interpreted-text
role="ref"}

Returns whether the CCDIK joint at `joint_idx` uses an inverted joint
constraint. See
`set_ccdik_joint_constraint_angle_invert()<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_invert>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_max}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_ccdik_joint_constraint_angle_max**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_max>`{.interpreted-text
role="ref"}

Returns the maximum angle constraint for the joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_min}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_ccdik_joint_constraint_angle_min**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DCCDIK_method_get_ccdik_joint_constraint_angle_min>`{.interpreted-text
role="ref"}

Returns the minimum angle constraint for the joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_enable_constraint}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_ccdik_joint_enable_constraint**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DCCDIK_method_get_ccdik_joint_enable_constraint>`{.interpreted-text
role="ref"}

Returns whether angle constraints on the CCDIK joint at `joint_idx` are
enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_get_ccdik_joint_rotate_from_joint}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_ccdik_joint_rotate_from_joint**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DCCDIK_method_get_ccdik_joint_rotate_from_joint>`{.interpreted-text
role="ref"}

Returns whether the joint at `joint_idx` is set to rotate from the
joint, `true`, or to rotate from the tip, `false`. The default is to
rotate from the tip.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone2d_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ccdik_joint_bone2d_node**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, bone2d_nodepath:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone2d_node>`{.interpreted-text
role="ref"}

Sets the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
assigned to the CCDIK joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ccdik_joint_bone_index**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_bone_index>`{.interpreted-text
role="ref"}

Sets the bone index, `bone_idx`, of the CCDIK joint at `joint_idx`. When
possible, this will also update the `bone2d_node` of the CCDIK joint
based on data provided by the linked skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_invert}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ccdik_joint_constraint_angle_invert**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, invert:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_invert>`{.interpreted-text
role="ref"}

Sets whether the CCDIK joint at `joint_idx` uses an inverted joint
constraint.

An inverted joint constraint only constraints the CCDIK joint to the
angles *outside of* the inputted minimum and maximum angles. For this
reason, it is referred to as an inverted joint constraint, as it
constraints the joint to the outside of the inputted values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_max}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ccdik_joint_constraint_angle_max**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, angle_max:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_max>`{.interpreted-text
role="ref"}

Sets the maximum angle constraint for the joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_min}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ccdik_joint_constraint_angle_min**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, angle_min:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_constraint_angle_min>`{.interpreted-text
role="ref"}

Sets the minimum angle constraint for the joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_enable_constraint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ccdik_joint_enable_constraint**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, enable_constraint:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_enable_constraint>`{.interpreted-text
role="ref"}

Determines whether angle constraints on the CCDIK joint at `joint_idx`
are enabled. When `true`, constraints will be enabled and taken into
account when solving.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DCCDIK_method_set_ccdik_joint_rotate_from_joint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_ccdik_joint_rotate_from_joint**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, rotate_from_joint:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DCCDIK_method_set_ccdik_joint_rotate_from_joint>`{.interpreted-text
role="ref"}

Sets whether the joint at `joint_idx` is set to rotate from the joint,
`true`, or to rotate from the tip, `false`.
