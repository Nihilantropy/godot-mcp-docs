github_url
:   hide

# CapsuleMesh {#class_CapsuleMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Class representing a capsule-shaped
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Class representing a capsule-shaped
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

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

:::: {#class_CapsuleMesh_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `2.0`
`🔗<class_CapsuleMesh_property_height>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

Total height of the capsule mesh (including the hemispherical ends).

\*\*Note:\*\* The
`height<class_CapsuleMesh_property_height>`{.interpreted-text
role="ref"} of a capsule must be at least twice its
`radius<class_CapsuleMesh_property_radius>`{.interpreted-text
role="ref"}. Otherwise, the capsule becomes a circle. If the
`height<class_CapsuleMesh_property_height>`{.interpreted-text
role="ref"} is less than twice the
`radius<class_CapsuleMesh_property_radius>`{.interpreted-text
role="ref"}, the properties adjust to a valid value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CapsuleMesh_property_radial_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **radial_segments** =
`64` `🔗<class_CapsuleMesh_property_radial_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radial_segments**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_radial_segments**()

Number of radial segments on the capsule mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CapsuleMesh_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_CapsuleMesh_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

Radius of the capsule mesh.

\*\*Note:\*\* The
`radius<class_CapsuleMesh_property_radius>`{.interpreted-text
role="ref"} of a capsule cannot be greater than half of its
`height<class_CapsuleMesh_property_height>`{.interpreted-text
role="ref"}. Otherwise, the capsule becomes a circle. If the
`radius<class_CapsuleMesh_property_radius>`{.interpreted-text
role="ref"} is greater than half of the
`height<class_CapsuleMesh_property_height>`{.interpreted-text
role="ref"}, the properties adjust to a valid value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CapsuleMesh_property_rings}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rings** = `8`
`🔗<class_CapsuleMesh_property_rings>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rings**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_rings**()

Number of rings along the height of the capsule.
