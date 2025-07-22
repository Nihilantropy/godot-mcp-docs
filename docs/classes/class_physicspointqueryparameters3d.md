github_url
:   hide

# PhysicsPointQueryParameters3D {#class_PhysicsPointQueryParameters3D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides parameters for
`PhysicsDirectSpaceState3D.intersect_point()<class_PhysicsDirectSpaceState3D_method_intersect_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

By changing various properties of this object, such as the point
position, you can configure the parameters for
`PhysicsDirectSpaceState3D.intersect_point()<class_PhysicsDirectSpaceState3D_method_intersect_point>`{.interpreted-text
role="ref"}.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_PhysicsPointQueryParameters3D_property_collide_with_areas}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_areas**
= `false`
`🔗<class_PhysicsPointQueryParameters3D_property_collide_with_areas>`{.interpreted-text
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

:::: {#class_PhysicsPointQueryParameters3D_property_collide_with_bodies}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_bodies**
= `true`
`🔗<class_PhysicsPointQueryParameters3D_property_collide_with_bodies>`{.interpreted-text
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

:::: {#class_PhysicsPointQueryParameters3D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** =
`4294967295`
`🔗<class_PhysicsPointQueryParameters3D_property_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsPointQueryParameters3D_property_exclude}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**exclude** = `[]`
`🔗<class_PhysicsPointQueryParameters3D_property_exclude>`{.interpreted-text
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

:::: {#class_PhysicsPointQueryParameters3D_property_position}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **position** =
`Vector3(0, 0, 0)`
`🔗<class_PhysicsPointQueryParameters3D_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_position**()

The position being queried for, in global coordinates.
