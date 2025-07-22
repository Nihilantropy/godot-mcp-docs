github_url
:   hide

# PhysicsRayQueryParameters3D {#class_PhysicsRayQueryParameters3D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides parameters for
`PhysicsDirectSpaceState3D.intersect_ray()<class_PhysicsDirectSpaceState3D_method_intersect_ray>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

By changing various properties of this object, such as the ray position,
you can configure the parameters for
`PhysicsDirectSpaceState3D.intersect_ray()<class_PhysicsDirectSpaceState3D_method_intersect_ray>`{.interpreted-text
role="ref"}.

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

:::: {#class_PhysicsRayQueryParameters3D_property_collide_with_areas}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_areas**
= `false`
`🔗<class_PhysicsRayQueryParameters3D_property_collide_with_areas>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_with_areas**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_with_areas_enabled**()

If `true`, the query will take `Area3D<class_Area3D>`{.interpreted-text
role="ref"}s into account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsRayQueryParameters3D_property_collide_with_bodies}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_bodies**
= `true`
`🔗<class_PhysicsRayQueryParameters3D_property_collide_with_bodies>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_with_bodies**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_with_bodies_enabled**()

If `true`, the query will take
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}s into
account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsRayQueryParameters3D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** =
`4294967295`
`🔗<class_PhysicsRayQueryParameters3D_property_collision_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_collision_mask**()

The physics layers the query will detect (as a bitmask). By default, all
collision layers are detected. See [Collision layers and
masks](../tutorials/physics/physics_introduction.html#collision-layers-and-masks)
in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsRayQueryParameters3D_property_exclude}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**exclude** = `[]`
`🔗<class_PhysicsRayQueryParameters3D_property_exclude>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exclude**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
  **get_exclude**()

The list of object `RID<class_RID>`{.interpreted-text role="ref"}s that
will be excluded from collisions. Use
`CollisionObject3D.get_rid()<class_CollisionObject3D_method_get_rid>`{.interpreted-text
role="ref"} to get the `RID<class_RID>`{.interpreted-text role="ref"}
associated with a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"}-derived node.

\*\*Note:\*\* The returned array is copied and any changes to it will
not update the original property value. To update the value you need to
modify the returned array, and then assign it to the property again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsRayQueryParameters3D_property_from}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **from** =
`Vector3(0, 0, 0)`
`🔗<class_PhysicsRayQueryParameters3D_property_from>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_from**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_from**()

The starting point of the ray being queried for, in global coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsRayQueryParameters3D_property_hit_back_faces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hit_back_faces** =
`true`
`🔗<class_PhysicsRayQueryParameters3D_property_hit_back_faces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hit_back_faces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hit_back_faces_enabled**()

If `true`, the query will hit back faces with concave polygon shapes
with back face enabled or heightmap shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsRayQueryParameters3D_property_hit_from_inside}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hit_from_inside** =
`false`
`🔗<class_PhysicsRayQueryParameters3D_property_hit_from_inside>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hit_from_inside**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hit_from_inside_enabled**()

If `true`, the query will detect a hit when starting inside shapes. In
this case the collision normal will be `Vector3(0, 0, 0)`. Does not
affect concave polygon shapes or heightmap shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsRayQueryParameters3D_property_to}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **to** =
`Vector3(0, 0, 0)`
`🔗<class_PhysicsRayQueryParameters3D_property_to>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_to**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_to**()

The ending point of the ray being queried for, in global coordinates.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PhysicsRayQueryParameters3D_method_create}
::: rst-class
classref-method
:::
::::

`PhysicsRayQueryParameters3D<class_PhysicsRayQueryParameters3D>`{.interpreted-text
role="ref"} **create**(from: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, to: `Vector3<class_Vector3>`{.interpreted-text role="ref"},
collision_mask: `int<class_int>`{.interpreted-text role="ref"} =
4294967295, exclude: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\] = \[\])
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsRayQueryParameters3D_method_create>`{.interpreted-text
role="ref"}

Returns a new, pre-configured **PhysicsRayQueryParameters3D** object.
Use it to quickly create query parameters using the most common options.

    var query = PhysicsRayQueryParameters3D.create(position, position + Vector3(0, -10, 0))
    var collision = get_world_3d().direct_space_state.intersect_ray(query)
