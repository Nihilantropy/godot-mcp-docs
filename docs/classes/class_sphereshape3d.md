github_url
:   hide

# SphereShape3D {#class_SphereShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D sphere shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D sphere shape, intended for use in physics. Usually used to provide
a shape for a
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}.

\*\*Performance:\*\* **SphereShape3D** is fast to check collisions
against. It is faster than
`BoxShape3D<class_BoxShape3D>`{.interpreted-text role="ref"},
`CapsuleShape3D<class_CapsuleShape3D>`{.interpreted-text role="ref"},
and `CylinderShape3D<class_CylinderShape3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Physics Tests
  Demo](https://godotengine.org/asset-library/asset/2747)

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

:::: {#class_SphereShape3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_SphereShape3D_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The sphere\'s radius. The shape\'s diameter is double the radius.
