github_url
:   hide

# BoxShape3D {#class_BoxShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D box shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D box shape, intended for use in physics. Usually used to provide a
shape for a `CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}.

\*\*Performance:\*\* **BoxShape3D** is fast to check collisions against.
It is faster than
`CapsuleShape3D<class_CapsuleShape3D>`{.interpreted-text role="ref"} and
`CylinderShape3D<class_CylinderShape3D>`{.interpreted-text role="ref"},
but slower than `SphereShape3D<class_SphereShape3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Physics Tests
  Demo](https://godotengine.org/asset-library/asset/2747)
- [3D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)

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

:::: {#class_BoxShape3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(1, 1, 1)`
`🔗<class_BoxShape3D_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The box\'s width, height and depth.
