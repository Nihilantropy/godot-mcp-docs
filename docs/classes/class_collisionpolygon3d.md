github_url
:   hide

# CollisionPolygon3D {#class_CollisionPolygon3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that provides a thickened polygon shape (a prism) to a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} parent.

::: rst-class
classref-introduction-group
:::

## Description

A node that provides a thickened polygon shape (a prism) to a
`CollisionObject3D<class_CollisionObject3D>`{.interpreted-text
role="ref"} parent and allows to edit it. The polygon can be concave or
convex. This can give a detection shape to an
`Area3D<class_Area3D>`{.interpreted-text role="ref"} or turn
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"} into
a solid object.

\*\*Warning:\*\* A non-uniformly scaled
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text role="ref"}
will likely not behave as expected. Make sure to keep its scale the same
on all axes and adjust its shape resource instead.

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

:::: {#class_CollisionPolygon3D_property_debug_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **debug_color** =
`Color(0, 0, 0, 0)`
`🔗<class_CollisionPolygon3D_property_debug_color>`{.interpreted-text
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

:::: {#class_CollisionPolygon3D_property_debug_fill}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **debug_fill** = `true`
`🔗<class_CollisionPolygon3D_property_debug_fill>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_debug_fill**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_debug_fill**()

If `true`, when the shape is displayed, it will show a solid fill color
in addition to its wireframe.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon3D_property_depth}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth** = `1.0`
`🔗<class_CollisionPolygon3D_property_depth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_depth**()

Length that the resulting collision extends in either direction
perpendicular to its 2D polygon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon3D_property_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disabled** = `false`
`🔗<class_CollisionPolygon3D_property_disabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_disabled**()

If `true`, no collision will be produced. This property should be
changed with
`Object.set_deferred()<class_Object_method_set_deferred>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon3D_property_margin}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **margin** = `0.04`
`🔗<class_CollisionPolygon3D_property_margin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_margin**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_margin**()

The collision margin for the generated
`Shape3D<class_Shape3D>`{.interpreted-text role="ref"}. See
`Shape3D.margin<class_Shape3D_property_margin>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CollisionPolygon3D_property_polygon}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **polygon** = `PackedVector2Array()`
`🔗<class_CollisionPolygon3D_property_polygon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_polygon**()

Array of vertices which define the 2D polygon in the local XY plane.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.
