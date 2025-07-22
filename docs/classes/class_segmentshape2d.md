github_url
:   hide

# SegmentShape2D {#class_SegmentShape2D}

**Inherits:** `Shape2D<class_Shape2D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D line segment shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 2D line segment shape, intended for use in physics. Usually used to
provide a shape for a
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text
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

:::: {#class_SegmentShape2D_property_a}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **a** =
`Vector2(0, 0)` `🔗<class_SegmentShape2D_property_a>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_a**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_a**()

The segment\'s first point position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SegmentShape2D_property_b}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **b** =
`Vector2(0, 10)` `🔗<class_SegmentShape2D_property_b>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_b**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_b**()

The segment\'s second point position.
