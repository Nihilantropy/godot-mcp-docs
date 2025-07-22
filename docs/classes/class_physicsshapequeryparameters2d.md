github_url
:   hide

# PhysicsShapeQueryParameters2D {#class_PhysicsShapeQueryParameters2D}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides parameters for
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"}\'s methods.

::: rst-class
classref-introduction-group
:::

## Description

By changing various properties of this object, such as the shape, you
can configure the parameters for
`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"}\'s methods.

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

:::: {#class_PhysicsShapeQueryParameters2D_property_collide_with_areas}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_areas**
= `false`
`🔗<class_PhysicsShapeQueryParameters2D_property_collide_with_areas>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collide_with_areas**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collide_with_areas_enabled**()

If `true`, the query will take `Area2D<class_Area2D>`{.interpreted-text
role="ref"}s into account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsShapeQueryParameters2D_property_collide_with_bodies}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collide_with_bodies**
= `true`
`🔗<class_PhysicsShapeQueryParameters2D_property_collide_with_bodies>`{.interpreted-text
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
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}s into
account.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsShapeQueryParameters2D_property_collision_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **collision_mask** =
`4294967295`
`🔗<class_PhysicsShapeQueryParameters2D_property_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsShapeQueryParameters2D_property_exclude}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**exclude** = `[]`
`🔗<class_PhysicsShapeQueryParameters2D_property_exclude>`{.interpreted-text
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
`CollisionObject2D.get_rid()<class_CollisionObject2D_method_get_rid>`{.interpreted-text
role="ref"} to get the `RID<class_RID>`{.interpreted-text role="ref"}
associated with a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"}-derived node.

\*\*Note:\*\* The returned array is copied and any changes to it will
not update the original property value. To update the value you need to
modify the returned array, and then assign it to the property again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsShapeQueryParameters2D_property_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **margin** = `0.0`
`🔗<class_PhysicsShapeQueryParameters2D_property_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_margin**()

The collision margin for the shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsShapeQueryParameters2D_property_motion}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **motion** =
`Vector2(0, 0)`
`🔗<class_PhysicsShapeQueryParameters2D_property_motion>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_motion**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_motion**()

The motion of the shape being queried for.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsShapeQueryParameters2D_property_shape}
::: rst-class
classref-property
:::
::::

`Resource<class_Resource>`{.interpreted-text role="ref"} **shape**
`🔗<class_PhysicsShapeQueryParameters2D_property_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value: `Resource<class_Resource>`{.interpreted-text
  role="ref"})
- `Resource<class_Resource>`{.interpreted-text role="ref"}
  **get_shape**()

The `Shape2D<class_Shape2D>`{.interpreted-text role="ref"} that will be
used for collision/intersection queries. This stores the actual
reference which avoids the shape to be released while being used for
queries, so always prefer using this over
`shape_rid<class_PhysicsShapeQueryParameters2D_property_shape_rid>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsShapeQueryParameters2D_property_shape_rid}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **shape_rid** = `RID()`
`🔗<class_PhysicsShapeQueryParameters2D_property_shape_rid>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape_rid**(value: `RID<class_RID>`{.interpreted-text
  role="ref"})
- `RID<class_RID>`{.interpreted-text role="ref"} **get_shape_rid**()

The queried shape\'s `RID<class_RID>`{.interpreted-text role="ref"} that
will be used for collision/intersection queries. Use this over
`shape<class_PhysicsShapeQueryParameters2D_property_shape>`{.interpreted-text
role="ref"} if you want to optimize for performance using the Servers
API:

::::: tabs
::: code-tab
gdscript

var shape_rid = PhysicsServer2D.circle_shape_create() var radius = 64
PhysicsServer2D.shape_set_data(shape_rid, radius)

var params = PhysicsShapeQueryParameters2D.new() params.shape_rid =
shape_rid

\# Execute physics queries here\...

\# Release the shape when done with physics queries.
PhysicsServer2D.free_rid(shape_rid)
:::

::: code-tab
csharp

RID shapeRid = PhysicsServer2D.CircleShapeCreate(); int radius = 64;
PhysicsServer2D.ShapeSetData(shapeRid, radius);

var params = new PhysicsShapeQueryParameters2D(); params.ShapeRid =
shapeRid;

// Execute physics queries here\...

// Release the shape when done with physics queries.
PhysicsServer2D.FreeRid(shapeRid);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsShapeQueryParameters2D_property_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**transform** = `Transform2D(1, 0, 0, 1, 0, 0)`
`🔗<class_PhysicsShapeQueryParameters2D_property_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_transform**()

The queried shape\'s transform matrix.
