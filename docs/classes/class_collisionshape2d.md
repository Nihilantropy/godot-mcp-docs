github_url
:   hide

# CollisionShape2D {#class_CollisionShape2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that provides a `Shape2D<class_Shape2D>`{.interpreted-text
role="ref"} to a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} parent.

::: rst-class
classref-introduction-group
:::

## Description

A node that provides a `Shape2D<class_Shape2D>`{.interpreted-text
role="ref"} to a
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} parent and allows to edit it. This can give a detection
shape to an `Area2D<class_Area2D>`{.interpreted-text role="ref"} or turn
a `PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}
into a solid object.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Physics introduction <../tutorials/physics/physics_introduction>`{.interpreted-text
  role="doc"}
- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)
- [2D Pong Demo](https://godotengine.org/asset-library/asset/2728)
- [2D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2719)

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

:::: {#class_CollisionShape2D_property_debug_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **debug_color** =
`Color(0, 0, 0, 0)`
`🔗<class_CollisionShape2D_property_debug_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_debug_color**()

The collision shape color that is displayed in the editor, or in the
running project if **Debug \> Visible Collision Shapes** is checked at
the top of the editor.

\*\*Note:\*\* The default value is
`ProjectSettings.debug/shapes/collision/shape_color<class_ProjectSettings_property_debug/shapes/collision/shape_color>`{.interpreted-text
role="ref"}. The `Color(0, 0, 0, 0)` value documented here is a
placeholder, and not the actual default debug color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionShape2D_property_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disabled** = `false`
`🔗<class_CollisionShape2D_property_disabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_disabled**()

A disabled collision shape has no effect in the world. This property
should be changed with
`Object.set_deferred()<class_Object_method_set_deferred>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionShape2D_property_one_way_collision}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **one_way_collision** =
`false`
`🔗<class_CollisionShape2D_property_one_way_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_one_way_collision**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_one_way_collision_enabled**()

Sets whether this collision shape should only detect collision on one
side (top or bottom).

\*\*Note:\*\* This property has no effect if this **CollisionShape2D**
is a child of an `Area2D<class_Area2D>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionShape2D_property_one_way_collision_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**one_way_collision_margin** = `1.0`
`🔗<class_CollisionShape2D_property_one_way_collision_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_one_way_collision_margin**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_one_way_collision_margin**()

The margin used for one-way collision (in pixels). Higher values will
make the shape thicker, and work better for colliders that enter the
shape at a high velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionShape2D_property_shape}
::: rst-class
classref-property
:::
::::

`Shape2D<class_Shape2D>`{.interpreted-text role="ref"} **shape**
`🔗<class_CollisionShape2D_property_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value: `Shape2D<class_Shape2D>`{.interpreted-text
  role="ref"})
- `Shape2D<class_Shape2D>`{.interpreted-text role="ref"} **get_shape**()

The actual shape owned by this collision shape.
