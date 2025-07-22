github_url
:   hide

# WorldBoundaryShape2D {#class_WorldBoundaryShape2D}

**Inherits:** `Shape2D<class_Shape2D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D world boundary (half-plane) shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 2D world boundary shape, intended for use in physics.
**WorldBoundaryShape2D** works like an infinite straight line that
forces all physics bodies to stay above it. The line\'s normal
determines which direction is considered as \"above\" and in the editor,
the smaller line over it represents this direction. It can for example
be used for endless flat floors.

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

:::: {#class_WorldBoundaryShape2D_property_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **distance** = `0.0`
`🔗<class_WorldBoundaryShape2D_property_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_distance**()

The distance from the origin to the line, expressed in terms of
`normal<class_WorldBoundaryShape2D_property_normal>`{.interpreted-text
role="ref"} (according to its direction and magnitude). Actual absolute
distance from the origin to the line can be calculated as
`abs(distance) / normal.length()`.

In the scalar equation of the line `ax + by = d`, this is `d`, while the
`(a, b)` coordinates are represented by the
`normal<class_WorldBoundaryShape2D_property_normal>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorldBoundaryShape2D_property_normal}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **normal** =
`Vector2(0, -1)`
`🔗<class_WorldBoundaryShape2D_property_normal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_normal**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_normal**()

The line\'s normal, typically a unit vector. Its direction indicates the
non-colliding half-plane. Can be of any length but zero. Defaults to
`Vector2.UP<class_Vector2_constant_UP>`{.interpreted-text role="ref"}.
