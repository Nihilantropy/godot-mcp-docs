github_url
:   hide

# NavigationObstacle2D {#class_NavigationObstacle2D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

2D obstacle used to affect navigation mesh baking or constrain
velocities of avoidance controlled agents.

::: rst-class
classref-introduction-group
:::

## Description

An obstacle needs a navigation map and outline
`vertices<class_NavigationObstacle2D_property_vertices>`{.interpreted-text
role="ref"} defined to work correctly. The outlines can not cross or
overlap.

Obstacles can be included in the navigation mesh baking process when
`affect_navigation_mesh<class_NavigationObstacle2D_property_affect_navigation_mesh>`{.interpreted-text
role="ref"} is enabled. They do not add walkable geometry, instead their
role is to discard other source geometry inside the shape. This can be
used to prevent navigation mesh from appearing in unwanted places. If
`carve_navigation_mesh<class_NavigationObstacle2D_property_carve_navigation_mesh>`{.interpreted-text
role="ref"} is enabled the baked shape will not be affected by offsets
of the navigation mesh baking, e.g. the agent radius.

With
`avoidance_enabled<class_NavigationObstacle2D_property_avoidance_enabled>`{.interpreted-text
role="ref"} the obstacle can constrain the avoidance velocities of
avoidance using agents. If the obstacle\'s vertices are wound in
clockwise order, avoidance agents will be pushed in by the obstacle,
otherwise, avoidance agents will be pushed out. Obstacles using vertices
and avoidance can warp to a new position but should not be moved every
single frame as each change requires a rebuild of the avoidance map.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using NavigationObstacles <../tutorials/navigation/navigation_using_navigationobstacles>`{.interpreted-text
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

:::: {#class_NavigationObstacle2D_property_affect_navigation_mesh}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**affect_navigation_mesh** = `false`
`🔗<class_NavigationObstacle2D_property_affect_navigation_mesh>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_affect_navigation_mesh**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_affect_navigation_mesh**()

If enabled and parsed in a navigation mesh baking process the obstacle
will discard source geometry inside its
`vertices<class_NavigationObstacle2D_property_vertices>`{.interpreted-text
role="ref"} defined shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_property_avoidance_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **avoidance_enabled** =
`true`
`🔗<class_NavigationObstacle2D_property_avoidance_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_avoidance_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_avoidance_enabled**()

If `true` the obstacle affects avoidance using agents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_property_avoidance_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **avoidance_layers** =
`1`
`🔗<class_NavigationObstacle2D_property_avoidance_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_avoidance_layers**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_avoidance_layers**()

A bitfield determining the avoidance layers for this obstacle. Agents
with a matching bit on the their avoidance mask will avoid this
obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_property_carve_navigation_mesh}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**carve_navigation_mesh** = `false`
`🔗<class_NavigationObstacle2D_property_carve_navigation_mesh>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_carve_navigation_mesh**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_carve_navigation_mesh**()

If enabled the obstacle vertices will carve into the baked navigation
mesh with the shape unaffected by additional offsets (e.g. agent
radius).

It will still be affected by further postprocessing of the baking
process, like edge and polygon simplification.

Requires
`affect_navigation_mesh<class_NavigationObstacle2D_property_affect_navigation_mesh>`{.interpreted-text
role="ref"} to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.0`
`🔗<class_NavigationObstacle2D_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

Sets the avoidance radius for the obstacle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_property_velocity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **velocity** =
`Vector2(0, 0)`
`🔗<class_NavigationObstacle2D_property_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_velocity**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_velocity**()

Sets the wanted velocity for the obstacle so other agent\'s can better
predict the obstacle if it is moved with a velocity regularly (every
frame) instead of warped to a new position. Does only affect avoidance
for the obstacles
`radius<class_NavigationObstacle2D_property_radius>`{.interpreted-text
role="ref"}. Does nothing for the obstacles static vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_property_vertices}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **vertices** = `PackedVector2Array()`
`🔗<class_NavigationObstacle2D_property_vertices>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertices**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_vertices**()

The outline vertices of the obstacle. If the vertices are winded in
clockwise order agents will be pushed in by the obstacle, else they will
be pushed out. Outlines can not be crossed or overlap. Should the
vertices using obstacle be warped to a new position agent\'s can not
predict this movement and may get trapped inside the obstacle.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_NavigationObstacle2D_method_get_avoidance_layer_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_avoidance_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationObstacle2D_method_get_avoidance_layer_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`avoidance_layers<class_NavigationObstacle2D_property_avoidance_layers>`{.interpreted-text
role="ref"} bitmask is enabled, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_method_get_navigation_map}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_navigation_map**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationObstacle2D_method_get_navigation_map>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map for this NavigationObstacle node. This function returns
always the map set on the NavigationObstacle node and not the map of the
abstract obstacle on the NavigationServer. If the obstacle map is
changed directly with the NavigationServer API the NavigationObstacle
node will not be aware of the map change. Use
`set_navigation_map()<class_NavigationObstacle2D_method_set_navigation_map>`{.interpreted-text
role="ref"} to change the navigation map for the NavigationObstacle and
also update the obstacle on the NavigationServer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_method_get_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationObstacle2D_method_get_rid>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"} of this
obstacle on the
`NavigationServer2D<class_NavigationServer2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_method_set_avoidance_layer_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_avoidance_layer_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationObstacle2D_method_set_avoidance_layer_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`avoidance_layers<class_NavigationObstacle2D_property_avoidance_layers>`{.interpreted-text
role="ref"} bitmask, given a `layer_number` between 1 and 32.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationObstacle2D_method_set_navigation_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_navigation_map**(navigation_map:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_NavigationObstacle2D_method_set_navigation_map>`{.interpreted-text
role="ref"}

Sets the `RID<class_RID>`{.interpreted-text role="ref"} of the
navigation map this NavigationObstacle node should use and also updates
the `obstacle` on the NavigationServer.
