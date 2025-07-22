github_url
:   hide

# CapsuleShape3D {#class_CapsuleShape3D}

**Inherits:** `Shape3D<class_Shape3D>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D capsule shape used for physics collision.

::: rst-class
classref-introduction-group
:::

## Description

A 3D capsule shape, intended for use in physics. Usually used to provide
a shape for a
`CollisionShape3D<class_CollisionShape3D>`{.interpreted-text
role="ref"}.

\*\*Performance:\*\* **CapsuleShape3D** is fast to check collisions
against. It is faster than
`CylinderShape3D<class_CylinderShape3D>`{.interpreted-text role="ref"},
but slower than `SphereShape3D<class_SphereShape3D>`{.interpreted-text
role="ref"} and `BoxShape3D<class_BoxShape3D>`{.interpreted-text
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

:::: {#class_CapsuleShape3D_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `2.0`
`🔗<class_CapsuleShape3D_property_height>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The capsule\'s full height, including the hemispheres.

\*\*Note:\*\* The
`height<class_CapsuleShape3D_property_height>`{.interpreted-text
role="ref"} of a capsule must be at least twice its
`radius<class_CapsuleShape3D_property_radius>`{.interpreted-text
role="ref"}. Otherwise, the capsule becomes a sphere. If the
`height<class_CapsuleShape3D_property_height>`{.interpreted-text
role="ref"} is less than twice the
`radius<class_CapsuleShape3D_property_radius>`{.interpreted-text
role="ref"}, the properties adjust to a valid value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CapsuleShape3D_property_mid_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **mid_height**
`🔗<class_CapsuleShape3D_property_mid_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mid_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_mid_height**()

The capsule\'s height, excluding the hemispheres. This is the height of
the central cylindrical part in the middle of the capsule, and is the
distance between the centers of the two hemispheres. This is a wrapper
for `height<class_CapsuleShape3D_property_height>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CapsuleShape3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_CapsuleShape3D_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The capsule\'s radius.

\*\*Note:\*\* The
`radius<class_CapsuleShape3D_property_radius>`{.interpreted-text
role="ref"} of a capsule cannot be greater than half of its
`height<class_CapsuleShape3D_property_height>`{.interpreted-text
role="ref"}. Otherwise, the capsule becomes a sphere. If the
`radius<class_CapsuleShape3D_property_radius>`{.interpreted-text
role="ref"} is greater than half of the
`height<class_CapsuleShape3D_property_height>`{.interpreted-text
role="ref"}, the properties adjust to a valid value.
