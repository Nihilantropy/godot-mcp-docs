github_url
:   hide

# ShapeCast3D {#class_ShapeCast3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D shape that sweeps a region of space to detect
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

Shape casting allows to detect collision objects by sweeping its
`shape<class_ShapeCast3D_property_shape>`{.interpreted-text role="ref"}
along the cast direction determined by
`target_position<class_ShapeCast3D_property_target_position>`{.interpreted-text
role="ref"}. This is similar to
`RayCast3D<class_RayCast3D>`{.interpreted-text role="ref"}, but it
allows for sweeping a region of space, rather than just a straight line.
**ShapeCast3D** can detect multiple collision objects. It is useful for
things like wide laser beams or snapping a simple shape to a floor.

Immediate collision overlaps can be done with the
`target_position<class_ShapeCast3D_property_target_position>`{.interpreted-text
role="ref"} set to `Vector3(0, 0, 0)` and by calling
`force_shapecast_update()<class_ShapeCast3D_method_force_shapecast_update>`{.interpreted-text
role="ref"} within the same physics frame. This helps to overcome some
limitations of `Area3D<class_Area3D>`{.interpreted-text role="ref"} when
used as an instantaneous detection area, as collision information isn\'t
immediately available to it.

\*\*Note:\*\* Shape casting is more computationally expensive than ray
casting.

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

:::: {#class_ShapeCast3D_property_collide_with_areas}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_areas**
= `false`
`🔗<class_ShapeCast3D_property_collide_with_areas>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_with_areas**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_with_areas_enabled**()

If `true`, collisions with `Area3D<class_Area3D>`{.interpreted-text
role="ref"}s will be reported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_collide_with_bodies}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_bodies**
= `true`
`🔗<class_ShapeCast3D_property_collide_with_bodies>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_with_bodies**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_with_bodies_enabled**()

If `true`, collisions with
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}s will
be reported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** = `1`
`🔗<class_ShapeCast3D_property_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The shape\'s collision mask. Only objects in at least one collision
layer enabled in the mask will be detected. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_collision_result}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **collision_result**
= `[]`
`🔗<class_ShapeCast3D_property_collision_result>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_collision_result**()

Returns the complete collision information from the collision sweep. The
data returned is the same as in the
`PhysicsDirectSpaceState3D.get_rest_info()<class_PhysicsDirectSpaceState3D_method_get_rest_info>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_debug_shape_custom_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**debug_shape_custom_color** = `Color(0, 0, 0, 1)`
`🔗<class_ShapeCast3D_property_debug_shape_custom_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_shape_custom_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_debug_shape_custom_color**()

The custom color to use to draw the shape in the editor and at run-time
if **Visible Collision Shapes** is enabled in the **Debug** menu. This
color will be highlighted at run-time if the **ShapeCast3D** is
colliding with something.

If set to `Color(0.0, 0.0, 0.0)` (by default), the color set in
`ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enabled** = `true`
`🔗<class_ShapeCast3D_property_enabled>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_enabled**()

If `true`, collisions will be reported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_exclude_parent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **exclude_parent** =
`true` `🔗<class_ShapeCast3D_property_exclude_parent>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exclude_parent_body**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_exclude_parent_body**()

If `true`, the parent node will be excluded from collision detection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **margin** = `0.0`
`🔗<class_ShapeCast3D_property_margin>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_margin**()

The collision margin for the shape. A larger margin helps detecting
collisions more consistently, at the cost of precision.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_max_results}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_results** = `32`
`🔗<class_ShapeCast3D_property_max_results>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_results**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_results**()

The number of intersections can be limited with this parameter, to
reduce the processing time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_shape}
::: rst-class
classref-property
:::
::::

`Shape3D<class_Shape3D>`{.interpreted-text role="ref"} **shape**
`🔗<class_ShapeCast3D_property_shape>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value: `Shape3D<class_Shape3D>`{.interpreted-text
  role="ref"})
- `Shape3D<class_Shape3D>`{.interpreted-text role="ref"} **get_shape**()

The shape to be used for collision queries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_property_target_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**target_position** = `Vector3(0, -1, 0)`
`🔗<class_ShapeCast3D_property_target_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_position**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_target_position**()

The shape\'s destination point, relative to this node\'s
`Node3D.position<class_Node3D_property_position>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ShapeCast3D_method_add_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_exception**(node:
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"})
`🔗<class_ShapeCast3D_method_add_exception>`{.interpreted-text
role="ref"}

Adds a collision exception so the shape does not report collisions with
the specified node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_add_exception_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_exception_rid**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_ShapeCast3D_method_add_exception_rid>`{.interpreted-text
role="ref"}

Adds a collision exception so the shape does not report collisions with
the specified `RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_clear_exceptions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_exceptions**()
`🔗<class_ShapeCast3D_method_clear_exceptions>`{.interpreted-text
role="ref"}

Removes all collision exceptions for this shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_force_shapecast_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_shapecast_update**()
`🔗<class_ShapeCast3D_method_force_shapecast_update>`{.interpreted-text
role="ref"}

Updates the collision information for the shape immediately, without
waiting for the next `_physics_process` call. Use this method, for
example, when the shape or its parent has changed state.

\*\*Note:\*\* Setting
`enabled<class_ShapeCast3D_property_enabled>`{.interpreted-text
role="ref"} to `true` is not required for this to work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_closest_collision_safe_fraction}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_closest_collision_safe_fraction**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_closest_collision_safe_fraction>`{.interpreted-text
role="ref"}

Returns the fraction from this cast\'s origin to its
`target_position<class_ShapeCast3D_property_target_position>`{.interpreted-text
role="ref"} of how far the shape can move without triggering a
collision, as a value between `0.0` and `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_closest_collision_unsafe_fraction}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_closest_collision_unsafe_fraction**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_closest_collision_unsafe_fraction>`{.interpreted-text
role="ref"}

Returns the fraction from this cast\'s origin to its
`target_position<class_ShapeCast3D_property_target_position>`{.interpreted-text
role="ref"} of how far the shape must move to trigger a collision, as a
value between `0.0` and `1.0`.

In ideal conditions this would be the same as
`get_closest_collision_safe_fraction()<class_ShapeCast3D_method_get_closest_collision_safe_fraction>`{.interpreted-text
role="ref"}, however shape casting is calculated in discrete steps, so
the precise point of collision can occur between two calculated
positions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_collider}
::: rst-class
classref-method
:::
::::

`Object<class_Object>`{.interpreted-text role="ref"}
**get_collider**(index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_collider>`{.interpreted-text
role="ref"}

Returns the collided `Object<class_Object>`{.interpreted-text
role="ref"} of one of the multiple collisions at `index`, or `null` if
no object is intersecting the shape (i.e.
`is_colliding()<class_ShapeCast3D_method_is_colliding>`{.interpreted-text
role="ref"} returns `false`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_collider_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_collider_rid**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_collider_rid>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
collided object of one of the multiple collisions at `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_collider_shape}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_collider_shape**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_collider_shape>`{.interpreted-text
role="ref"}

Returns the shape ID of the colliding shape of one of the multiple
collisions at `index`, or `0` if no object is intersecting the shape
(i.e.
`is_colliding()<class_ShapeCast3D_method_is_colliding>`{.interpreted-text
role="ref"} returns `false`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_collision_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_collision_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_collision_count>`{.interpreted-text
role="ref"}

The number of collisions detected at the point of impact. Use this to
iterate over multiple collisions as provided by
`get_collider()<class_ShapeCast3D_method_get_collider>`{.interpreted-text
role="ref"},
`get_collider_shape()<class_ShapeCast3D_method_get_collider_shape>`{.interpreted-text
role="ref"},
`get_collision_point()<class_ShapeCast3D_method_get_collision_point>`{.interpreted-text
role="ref"}, and
`get_collision_normal()<class_ShapeCast3D_method_get_collision_normal>`{.interpreted-text
role="ref"} methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_collision_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_collision_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`collision_mask<class_ShapeCast3D_property_collision_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_collision_normal}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_collision_normal**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_collision_normal>`{.interpreted-text
role="ref"}

Returns the normal of one of the multiple collisions at `index` of the
intersecting object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_get_collision_point}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_collision_point**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_get_collision_point>`{.interpreted-text
role="ref"}

Returns the collision point of one of the multiple collisions at `index`
where the shape intersects the colliding object.

\*\*Note:\*\* This point is in the **global** coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_is_colliding}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_colliding**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ShapeCast3D_method_is_colliding>`{.interpreted-text
role="ref"}

Returns whether any object is intersecting with the shape\'s vector
(considering the vector length).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_remove_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_exception**(node:
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"})
`🔗<class_ShapeCast3D_method_remove_exception>`{.interpreted-text
role="ref"}

Removes a collision exception so the shape does report collisions with
the specified node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_remove_exception_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_exception_rid**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_ShapeCast3D_method_remove_exception_rid>`{.interpreted-text
role="ref"}

Removes a collision exception so the shape does report collisions with
the specified `RID<class_RID>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_resource_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**resource_changed**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_ShapeCast3D_method_resource_changed>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`Resource.changed<class_Resource_signal_changed>`{.interpreted-text
role="ref"} instead.

This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ShapeCast3D_method_set_collision_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_collision_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ShapeCast3D_method_set_collision_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`collision_mask<class_ShapeCast3D_property_collision_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 32.
