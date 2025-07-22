github_url
:   hide

# SphereMesh {#class_SphereMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Class representing a spherical
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Class representing a spherical
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

:::: {#class_SphereMesh_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `1.0`
`🔗<class_SphereMesh_property_height>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

Full height of the sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SphereMesh_property_is_hemisphere}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_hemisphere** =
`false` `🔗<class_SphereMesh_property_is_hemisphere>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_is_hemisphere**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_is_hemisphere**()

If `true`, a hemisphere is created rather than a full sphere.

\*\*Note:\*\* To get a regular hemisphere, the height and radius of the
sphere must be equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SphereMesh_property_radial_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **radial_segments** =
`64` `🔗<class_SphereMesh_property_radial_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radial_segments**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_radial_segments**()

Number of radial segments on the sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SphereMesh_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_SphereMesh_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

Radius of sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SphereMesh_property_rings}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rings** = `32`
`🔗<class_SphereMesh_property_rings>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rings**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_rings**()

Number of segments along the height of the sphere.
