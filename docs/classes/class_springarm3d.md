github_url
:   hide

# SpringArm3D {#class_SpringArm3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D raycast that dynamically moves its children near the collision
point.

::: rst-class
classref-introduction-group
:::

## Description

**SpringArm3D** casts a ray or a shape along its Z axis and moves all
its direct children to the collision point, with an optional margin.
This is useful for 3rd person cameras that move closer to the player
when inside a tight space (you may need to exclude the player\'s
collider from the **SpringArm3D**\'s collision check).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Third-person camera with spring arm <../tutorials/3d/spring_arm>`{.interpreted-text
  role="doc"}

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

:::: {#class_SpringArm3D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** = `1`
`🔗<class_SpringArm3D_property_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The layers against which the collision check shall be done. See
[Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringArm3D_property_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **margin** = `0.01`
`🔗<class_SpringArm3D_property_margin>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_margin**()

When the collision check is made, a candidate length for the SpringArm3D
is given.

The margin is then subtracted to this length and the translation is
applied to the child objects of the SpringArm3D.

This margin is useful for when the SpringArm3D has a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} as a child
node: without the margin, the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} would be placed
on the exact point of collision, while with the margin the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} would be placed
close to the point of collision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringArm3D_property_shape}
::: rst-class
classref-property
:::
::::

`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} **shape**
`🔗<class_SpringArm3D_property_shape>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value: `Shape3D<class_Shape3D>`{.interpreted-text
  role="ref"})
- `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} **get_shape**()

The `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} to use for
the SpringArm3D.

When the shape is set, the SpringArm3D will cast the
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} on its z axis
instead of performing a ray cast.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringArm3D_property_spring_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spring_length** =
`1.0` `🔗<class_SpringArm3D_property_spring_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_length**()

The maximum extent of the SpringArm3D. This is used as a length for both
the ray and the shape cast used internally to calculate the desired
position of the SpringArm3D\'s child nodes.

To know more about how to perform a shape cast or a ray cast, please
consult the
`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
role="ref"} documentation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SpringArm3D_method_add_excluded_object}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_excluded_object**(RID: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_SpringArm3D_method_add_excluded_object>`{.interpreted-text
role="ref"}

Adds the `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"} object with the given `RID<class_RID>`{.interpreted-text
role="ref"} to the list of
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
objects excluded from the collision check.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringArm3D_method_clear_excluded_objects}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_excluded_objects**()
`🔗<class_SpringArm3D_method_clear_excluded_objects>`{.interpreted-text
role="ref"}

Clears the list of
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
objects excluded from the collision check.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringArm3D_method_get_hit_length}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_hit_length**()
`🔗<class_SpringArm3D_method_get_hit_length>`{.interpreted-text
role="ref"}

Returns the spring arm\'s current length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpringArm3D_method_remove_excluded_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**remove_excluded_object**(RID: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_SpringArm3D_method_remove_excluded_object>`{.interpreted-text
role="ref"}

Removes the given `RID<class_RID>`{.interpreted-text role="ref"} from
the list of `PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text
role="ref"} objects excluded from the collision check.
