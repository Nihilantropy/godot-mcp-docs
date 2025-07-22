github_url
:   hide

::: {.meta keywords="ragdoll"}
:::

# PhysicalBone2D {#class_PhysicalBone2D}

**Inherits:** `RigidBody2D<class_RigidBody2D>`{.interpreted-text
role="ref"} **\<**
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}
**\<** `CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} **\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `RigidBody2D<class_RigidBody2D>`{.interpreted-text role="ref"}-derived
node used to make `Bone2D<class_Bone2D>`{.interpreted-text role="ref"}s
in a `Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} react
to physics.

::: rst-class
classref-introduction-group
:::

## Description

The **PhysicalBone2D** node is a
`RigidBody2D<class_RigidBody2D>`{.interpreted-text role="ref"}-based
node that can be used to make `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"}s in a `Skeleton2D<class_Skeleton2D>`{.interpreted-text
role="ref"} react to physics.

\*\*Note:\*\* To make the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"}s visually follow the **PhysicalBone2D** node, use a
`SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>`{.interpreted-text
role="ref"} modification on the
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} parent.

\*\*Note:\*\* The **PhysicalBone2D** node does not automatically create
a `Joint2D<class_Joint2D>`{.interpreted-text role="ref"} node to keep
**PhysicalBone2D** nodes together. They must be created manually. For
most cases, you want to use a
`PinJoint2D<class_PinJoint2D>`{.interpreted-text role="ref"} node. The
**PhysicalBone2D** node will automatically configure the
`Joint2D<class_Joint2D>`{.interpreted-text role="ref"} node once it\'s
been added as a child node.

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

:::: {#class_PhysicalBone2D_property_auto_configure_joint}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**auto_configure_joint** = `true`
`🔗<class_PhysicalBone2D_property_auto_configure_joint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_configure_joint**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_auto_configure_joint**()

If `true`, the **PhysicalBone2D** will automatically configure the first
`Joint2D<class_Joint2D>`{.interpreted-text role="ref"} child node. The
automatic configuration is limited to setting up the node properties and
positioning the `Joint2D<class_Joint2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone2D_property_bone2d_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bone2d_index** = `-1`
`🔗<class_PhysicalBone2D_property_bone2d_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone2d_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_bone2d_index**()

The index of the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"}
that this **PhysicalBone2D** should simulate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone2D_property_bone2d_nodepath}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**bone2d_nodepath** = `NodePath("")`
`🔗<class_PhysicalBone2D_property_bone2d_nodepath>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bone2d_nodepath**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_bone2d_nodepath**()

The `NodePath<class_NodePath>`{.interpreted-text role="ref"} to the
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} that this
**PhysicalBone2D** should simulate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone2D_property_follow_bone_when_simulating}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**follow_bone_when_simulating** = `false`
`🔗<class_PhysicalBone2D_property_follow_bone_when_simulating>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_follow_bone_when_simulating**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_follow_bone_when_simulating**()

If `true`, the **PhysicalBone2D** will keep the transform of the bone it
is bound to when simulating physics.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone2D_property_simulate_physics}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **simulate_physics** =
`false`
`🔗<class_PhysicalBone2D_property_simulate_physics>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_simulate_physics**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_simulate_physics**()

If `true`, the **PhysicalBone2D** will start simulating using physics.
If `false`, the **PhysicalBone2D** will follow the transform of the
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node.

\*\*Note:\*\* To have the `Bone2D<class_Bone2D>`{.interpreted-text
role="ref"}s visually follow the **PhysicalBone2D**, use a
`SkeletonModification2DPhysicalBones<class_SkeletonModification2DPhysicalBones>`{.interpreted-text
role="ref"} modification on the
`Skeleton2D<class_Skeleton2D>`{.interpreted-text role="ref"} node with
the `Bone2D<class_Bone2D>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PhysicalBone2D_method_get_joint}
::: rst-class
classref-method
:::
::::

`Joint2D<class_Joint2D>`{.interpreted-text role="ref"} **get_joint**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicalBone2D_method_get_joint>`{.interpreted-text
role="ref"}

Returns the first `Joint2D<class_Joint2D>`{.interpreted-text role="ref"}
child node, if one exists. This is mainly a helper function to make it
easier to get the `Joint2D<class_Joint2D>`{.interpreted-text role="ref"}
that the **PhysicalBone2D** is autoconfiguring.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicalBone2D_method_is_simulating_physics}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_simulating_physics**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicalBone2D_method_is_simulating_physics>`{.interpreted-text
role="ref"}

Returns a boolean that indicates whether the **PhysicalBone2D** is
running and simulating using the Godot 2D physics engine. When `true`,
the PhysicalBone2D node is using physics.
