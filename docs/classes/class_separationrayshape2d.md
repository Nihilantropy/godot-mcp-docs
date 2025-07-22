github_url
:   hide

# SeparationRayShape2D {#class_SeparationRayShape2D}

**Inherits:** `Shape2D<class_Shape2D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D ray shape used for physics collision that tries to separate itself
from any collider.

::: rst-class
classref-introduction-group
:::

## Description

A 2D ray shape, intended for use in physics. Usually used to provide a
shape for a `CollisionShape2D<class_CollisionShape2D>`{.interpreted-text
role="ref"}. When a **SeparationRayShape2D** collides with an object, it
tries to separate itself from it by moving its endpoint to the collision
point. For example, a **SeparationRayShape2D** next to a character can
allow it to instantly move up when touching stairs.

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

:::: {#class_SeparationRayShape2D_property_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **length** = `20.0`
`🔗<class_SeparationRayShape2D_property_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_length**()

The ray\'s length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SeparationRayShape2D_property_slide_on_slope}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **slide_on_slope** =
`false`
`🔗<class_SeparationRayShape2D_property_slide_on_slope>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_slide_on_slope**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_slide_on_slope**()

If `false` (default), the shape always separates and returns a normal
along its own direction.

If `true`, the shape can return the correct normal and separate in any
direction, allowing sliding motion on slopes.
