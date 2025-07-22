github_url
:   hide

# TubeTrailMesh {#class_TubeTrailMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Represents a straight tube-shaped
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"} with
variable width.

::: rst-class
classref-introduction-group
:::

## Description

**TubeTrailMesh** represents a straight tube-shaped mesh with variable
width. The tube is composed of a number of cylindrical sections, each
with the same
`section_length<class_TubeTrailMesh_property_section_length>`{.interpreted-text
role="ref"} and number of
`section_rings<class_TubeTrailMesh_property_section_rings>`{.interpreted-text
role="ref"}. A
`curve<class_TubeTrailMesh_property_curve>`{.interpreted-text
role="ref"} is sampled along the total length of the tube, meaning that
the curve determines the radius of the tube along its length.

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

## Property Descriptions

:::: {#class_TubeTrailMesh_property_cap_bottom}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cap_bottom** = `true`
`🔗<class_TubeTrailMesh_property_cap_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cap_bottom**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_cap_bottom**()

If `true`, generates a cap at the bottom of the tube. This can be set to
`false` to speed up generation and rendering when the cap is never seen
by the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TubeTrailMesh_property_cap_top}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cap_top** = `true`
`🔗<class_TubeTrailMesh_property_cap_top>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cap_top**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_cap_top**()

If `true`, generates a cap at the top of the tube. This can be set to
`false` to speed up generation and rendering when the cap is never seen
by the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TubeTrailMesh_property_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **curve**
`🔗<class_TubeTrailMesh_property_curve>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"} **get_curve**()

Determines the radius of the tube along its length. The radius of a
particular section ring is obtained by multiplying the baseline
`radius<class_TubeTrailMesh_property_radius>`{.interpreted-text
role="ref"} by the value of this curve at the given distance. For values
smaller than `0`, the faces will be inverted. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TubeTrailMesh_property_radial_steps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **radial_steps** = `8`
`🔗<class_TubeTrailMesh_property_radial_steps>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radial_steps**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_radial_steps**()

The number of sides on the tube. For example, a value of `5` means the
tube will be pentagonal. Higher values result in a more detailed tube at
the cost of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TubeTrailMesh_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_TubeTrailMesh_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The baseline radius of the tube. The radius of a particular section ring
is obtained by multiplying this radius by the value of the
`curve<class_TubeTrailMesh_property_curve>`{.interpreted-text
role="ref"} at the given distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TubeTrailMesh_property_section_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **section_length** =
`0.2`
`🔗<class_TubeTrailMesh_property_section_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_section_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_section_length**()

The length of a section of the tube.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TubeTrailMesh_property_section_rings}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **section_rings** = `3`
`🔗<class_TubeTrailMesh_property_section_rings>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_section_rings**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_section_rings**()

The number of rings in a section. The
`curve<class_TubeTrailMesh_property_curve>`{.interpreted-text
role="ref"} is sampled on each ring to determine its radius. Higher
values result in a more detailed tube at the cost of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TubeTrailMesh_property_sections}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sections** = `5`
`🔗<class_TubeTrailMesh_property_sections>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sections**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sections**()

The total number of sections on the tube.
