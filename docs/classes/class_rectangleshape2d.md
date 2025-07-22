github_url
:   hide

# RectangleShape2D {#class_RectangleShape2D}

**Inherits:** `Shape2D<class_Shape2D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D rectangle shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 2D rectangle shape, intended for use in physics. Usually used to
provide a shape for a
`CollisionShape2D<class_CollisionShape2D>`{.interpreted-text
role="ref"}.

\*\*Performance:\*\* **RectangleShape2D** is fast to check collisions
against. It is faster than
`CapsuleShape2D<class_CapsuleShape2D>`{.interpreted-text role="ref"},
but slower than `CircleShape2D<class_CircleShape2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

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

:::: {#class_RectangleShape2D_property_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **size** =
`Vector2(20, 20)`
`🔗<class_RectangleShape2D_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()

The rectangle\'s width and height.
