github_url
:   hide

# SkeletonModification2DJiggle {#class_SkeletonModification2DJiggle}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:**
`SkeletonModification2D<class_SkeletonModification2D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A modification that jiggles `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} nodes as they move towards a target.

::: rst-class
classref-introduction-group
:::

## Description

This modification moves a series of bones, typically called a bone
chain, towards a target. What makes this modification special is that it
calculates the velocity and acceleration for each bone in the bone
chain, and runs a very light physics-like calculation using the inputted
values. This allows the bones to overshoot the target and \"jiggle\"
around. It can be configured to act more like a spring, or sway around
like cloth might.

This modification is useful for adding additional motion to things like
hair, the edges of clothing, and more. It has several settings to that
allow control over how the joint moves when the target moves.

\*\*Note:\*\* The Jiggle modifier has `jiggle_joints`, which are the
data objects that hold the data for each joint in the Jiggle chain. This
is different from than `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} nodes! Jiggle joints hold the data needed for each
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} in the bone chain
used by the Jiggle modification.

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

:::: {#class_SkeletonModification2DJiggle_property_damping}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **damping** = `0.75`
`🔗<class_SkeletonModification2DJiggle_property_damping>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_damping**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_damping**()

The default amount of damping applied to the Jiggle joints, if they are
not overridden. Higher values lead to more of the calculated velocity
being applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_property_gravity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **gravity** =
`Vector2(0, 6)`
`🔗<class_SkeletonModification2DJiggle_property_gravity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_gravity**()

The default amount of gravity applied to the Jiggle joints, if they are
not overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_property_jiggle_data_chain_length}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**jiggle_data_chain_length** = `0`
`🔗<class_SkeletonModification2DJiggle_property_jiggle_data_chain_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_jiggle_data_chain_length**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_jiggle_data_chain_length**()

The amount of Jiggle joints in the Jiggle modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_property_mass}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mass** = `0.75`
`🔗<class_SkeletonModification2DJiggle_property_mass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mass**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_mass**()

The default amount of mass assigned to the Jiggle joints, if they are
not overridden. Higher values lead to faster movements and more
overshooting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_property_stiffness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **stiffness** = `3.0`
`🔗<class_SkeletonModification2DJiggle_property_stiffness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stiffness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_stiffness**()

The default amount of stiffness assigned to the Jiggle joints, if they
are not overridden. Higher values act more like springs, quickly moving
into the correct position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_property_target_nodepath}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**target_nodepath** = `NodePath("")`
`🔗<class_SkeletonModification2DJiggle_property_target_nodepath>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_node**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_target_node**()

The NodePath to the node that is the target for the Jiggle modification.
This node is what the Jiggle chain will attempt to rotate the bone chain
to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_property_use_gravity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_gravity** =
`false`
`🔗<class_SkeletonModification2DJiggle_property_use_gravity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_gravity**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_use_gravity**()

Whether the gravity vector,
`gravity<class_SkeletonModification2DJiggle_property_gravity>`{.interpreted-text
role="ref"}, should be applied to the Jiggle joints, assuming they are
not overriding the default settings.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SkeletonModification2DJiggle_method_get_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_collision_mask**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_collision_mask>`{.interpreted-text
role="ref"}

Returns the collision mask used by the Jiggle modifier when collisions
are enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone2d_node}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_jiggle_joint_bone2d_node**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone2d_node>`{.interpreted-text
role="ref"}

Returns the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
assigned to the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_jiggle_joint_bone_index**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_bone_index>`{.interpreted-text
role="ref"}

Returns the index of the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"} node assigned to the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_damping}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_jiggle_joint_damping**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_damping>`{.interpreted-text
role="ref"}

Returns the amount of damping of the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_gravity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_jiggle_joint_gravity**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_gravity>`{.interpreted-text
role="ref"}

Returns a `Vector2<class_Vector2>`{.interpreted-text role="ref"}
representing the amount of gravity the Jiggle joint at `joint_idx` is
influenced by.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_mass}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_jiggle_joint_mass**(joint_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_mass>`{.interpreted-text
role="ref"}

Returns the amount of mass of the jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_jiggle_joint_override**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_override>`{.interpreted-text
role="ref"}

Returns a boolean that indicates whether the joint at `joint_idx` is
overriding the default Jiggle joint data defined in the modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_stiffness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_jiggle_joint_stiffness**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_stiffness>`{.interpreted-text
role="ref"}

Returns the stiffness of the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_jiggle_joint_use_gravity}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_jiggle_joint_use_gravity**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_jiggle_joint_use_gravity>`{.interpreted-text
role="ref"}

Returns a boolean that indicates whether the joint at `joint_idx` is
using gravity or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_get_use_colliders}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_use_colliders**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SkeletonModification2DJiggle_method_get_use_colliders>`{.interpreted-text
role="ref"}

Returns whether the jiggle modifier is taking physics colliders into
account when solving.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask**(collision_mask:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_collision_mask>`{.interpreted-text
role="ref"}

Sets the collision mask that the Jiggle modifier will use when reacting
to colliders, if the Jiggle modifier is set to take colliders into
account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone2d_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_bone2d_node**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, bone2d_node:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone2d_node>`{.interpreted-text
role="ref"}

Sets the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node
assigned to the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_bone_index**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, bone_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_bone_index>`{.interpreted-text
role="ref"}

Sets the bone index, `bone_idx`, of the Jiggle joint at `joint_idx`.
When possible, this will also update the `bone2d_node` of the Jiggle
joint based on data provided by the linked skeleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_damping}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_damping**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, damping:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_damping>`{.interpreted-text
role="ref"}

Sets the amount of damping of the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_gravity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_gravity**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, gravity:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_gravity>`{.interpreted-text
role="ref"}

Sets the gravity vector of the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_mass}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_mass**(joint_idx: `int<class_int>`{.interpreted-text
role="ref"}, mass: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_mass>`{.interpreted-text
role="ref"}

Sets the of mass of the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_override**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, override:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_override>`{.interpreted-text
role="ref"}

Sets whether the Jiggle joint at `joint_idx` should override the default
Jiggle joint settings. Setting this to `true` will make the joint use
its own settings rather than the default ones attached to the
modification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_stiffness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_stiffness**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, stiffness:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_stiffness>`{.interpreted-text
role="ref"}

Sets the of stiffness of the Jiggle joint at `joint_idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_jiggle_joint_use_gravity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_jiggle_joint_use_gravity**(joint_idx:
`int<class_int>`{.interpreted-text role="ref"}, use_gravity:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_jiggle_joint_use_gravity>`{.interpreted-text
role="ref"}

Sets whether the Jiggle joint at `joint_idx` should use gravity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SkeletonModification2DJiggle_method_set_use_colliders}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_use_colliders**(use_colliders:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SkeletonModification2DJiggle_method_set_use_colliders>`{.interpreted-text
role="ref"}

If `true`, the Jiggle modifier will take colliders into account, keeping
them from entering into these collision objects.
