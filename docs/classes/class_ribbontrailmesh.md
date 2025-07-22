github_url
:   hide

# RibbonTrailMesh {#class_RibbonTrailMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Represents a straight ribbon-shaped
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"} with
variable width.

::: rst-class
classref-introduction-group
:::

## Description

**RibbonTrailMesh** represents a straight ribbon-shaped mesh with
variable width. The ribbon is composed of a number of flat or
cross-shaped sections, each with the same
`section_length<class_RibbonTrailMesh_property_section_length>`{.interpreted-text
role="ref"} and number of
`section_segments<class_RibbonTrailMesh_property_section_segments>`{.interpreted-text
role="ref"}. A
`curve<class_RibbonTrailMesh_property_curve>`{.interpreted-text
role="ref"} is sampled along the total length of the ribbon, meaning
that the curve determines the size of the ribbon along its length.

This primitive mesh is usually used for particle trails.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `3D Particle trails <../tutorials/3d/particles/trails>`{.interpreted-text
  role="doc"}
- `Particle systems (3D) <../tutorials/3d/particles/index>`{.interpreted-text
  role="doc"}

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

## Enumerations

:::: {#enum_RibbonTrailMesh_Shape}
::: rst-class
classref-enumeration
:::
::::

enum **Shape**: `🔗<enum_RibbonTrailMesh_Shape>`{.interpreted-text
role="ref"}

:::: {#class_RibbonTrailMesh_constant_SHAPE_FLAT}
::: rst-class
classref-enumeration-constant
:::
::::

`Shape<enum_RibbonTrailMesh_Shape>`{.interpreted-text role="ref"}
**SHAPE_FLAT** = `0`

Gives the mesh a single flat face.

:::: {#class_RibbonTrailMesh_constant_SHAPE_CROSS}
::: rst-class
classref-enumeration-constant
:::
::::

`Shape<enum_RibbonTrailMesh_Shape>`{.interpreted-text role="ref"}
**SHAPE_CROSS** = `1`

Gives the mesh two perpendicular flat faces, making a cross shape.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RibbonTrailMesh_property_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **curve**
`🔗<class_RibbonTrailMesh_property_curve>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"} **get_curve**()

Determines the size of the ribbon along its length. The size of a
particular section segment is obtained by multiplying the baseline
`size<class_RibbonTrailMesh_property_size>`{.interpreted-text
role="ref"} by the value of this curve at the given distance. For values
smaller than `0`, the faces will be inverted. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RibbonTrailMesh_property_section_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **section_length** =
`0.2`
`🔗<class_RibbonTrailMesh_property_section_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_section_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_section_length**()

The length of a section of the ribbon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RibbonTrailMesh_property_section_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **section_segments** =
`3`
`🔗<class_RibbonTrailMesh_property_section_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_section_segments**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_section_segments**()

The number of segments in a section. The
`curve<class_RibbonTrailMesh_property_curve>`{.interpreted-text
role="ref"} is sampled on each segment to determine its size. Higher
values result in a more detailed ribbon at the cost of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RibbonTrailMesh_property_sections}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sections** = `5`
`🔗<class_RibbonTrailMesh_property_sections>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sections**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sections**()

The total number of sections on the ribbon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RibbonTrailMesh_property_shape}
::: rst-class
classref-property
:::
::::

`Shape<enum_RibbonTrailMesh_Shape>`{.interpreted-text role="ref"}
**shape** = `1`
`🔗<class_RibbonTrailMesh_property_shape>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shape**(value:
  `Shape<enum_RibbonTrailMesh_Shape>`{.interpreted-text role="ref"})
- `Shape<enum_RibbonTrailMesh_Shape>`{.interpreted-text role="ref"}
  **get_shape**()

Determines the shape of the ribbon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RibbonTrailMesh_property_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **size** = `1.0`
`🔗<class_RibbonTrailMesh_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_size**()

The baseline size of the ribbon. The size of a particular section
segment is obtained by multiplying this size by the value of the
`curve<class_RibbonTrailMesh_property_curve>`{.interpreted-text
role="ref"} at the given distance.
