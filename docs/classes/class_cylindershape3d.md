github_url
:   hide

# CylinderShape3D {#class_CylinderShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D cylinder shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D cylinder shape, intended for use in physics. Usually used to
provide a shape for a
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* There are several known bugs with cylinder collision
shapes. Using `CapsuleShape3D<class_CapsuleShape3D>`{.interpreted-text
role="ref"} or `BoxShape3D<class_BoxShape3D>`{.interpreted-text
role="ref"} instead is recommended.

\*\*Performance:\*\* **CylinderShape3D** is fast to check collisions
against, but it is slower than
`CapsuleShape3D<class_CapsuleShape3D>`{.interpreted-text role="ref"},
`BoxShape3D<class_BoxShape3D>`{.interpreted-text role="ref"}, and
`SphereShape3D<class_SphereShape3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)
- [3D Physics Tests
  Demo](https://godotengine.org/asset-library/asset/2747)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

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

:::: {#class_CylinderShape3D_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `2.0`
`🔗<class_CylinderShape3D_property_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The cylinder\'s height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CylinderShape3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_CylinderShape3D_property_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The cylinder\'s radius.
