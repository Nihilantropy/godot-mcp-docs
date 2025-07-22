github_url
:   hide

# CylinderMesh {#class_CylinderMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Class representing a cylindrical
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Class representing a cylindrical
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}. This
class can be used to create cones by setting either the
`top_radius<class_CylinderMesh_property_top_radius>`{.interpreted-text
role="ref"} or
`bottom_radius<class_CylinderMesh_property_bottom_radius>`{.interpreted-text
role="ref"} properties to `0.0`.

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

:::: {#class_CylinderMesh_property_bottom_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bottom_radius** =
`0.5` `🔗<class_CylinderMesh_property_bottom_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bottom_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_bottom_radius**()

Bottom radius of the cylinder. If set to `0.0`, the bottom faces will
not be generated, resulting in a conic shape. See also
`cap_bottom<class_CylinderMesh_property_cap_bottom>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CylinderMesh_property_cap_bottom}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cap_bottom** = `true`
`🔗<class_CylinderMesh_property_cap_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cap_bottom**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_cap_bottom**()

If `true`, generates a cap at the bottom of the cylinder. This can be
set to `false` to speed up generation and rendering when the cap is
never seen by the camera. See also
`bottom_radius<class_CylinderMesh_property_bottom_radius>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`bottom_radius<class_CylinderMesh_property_bottom_radius>`{.interpreted-text
role="ref"} is `0.0`, cap generation is always skipped even if
`cap_bottom<class_CylinderMesh_property_cap_bottom>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CylinderMesh_property_cap_top}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cap_top** = `true`
`🔗<class_CylinderMesh_property_cap_top>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cap_top**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_cap_top**()

If `true`, generates a cap at the top of the cylinder. This can be set
to `false` to speed up generation and rendering when the cap is never
seen by the camera. See also
`top_radius<class_CylinderMesh_property_top_radius>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`top_radius<class_CylinderMesh_property_top_radius>`{.interpreted-text
role="ref"} is `0.0`, cap generation is always skipped even if
`cap_top<class_CylinderMesh_property_cap_top>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CylinderMesh_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `2.0`
`🔗<class_CylinderMesh_property_height>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

Full height of the cylinder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CylinderMesh_property_radial_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **radial_segments** =
`64` `🔗<class_CylinderMesh_property_radial_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radial_segments**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_radial_segments**()

Number of radial segments on the cylinder. Higher values result in a
more detailed cylinder/cone at the cost of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CylinderMesh_property_rings}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rings** = `4`
`🔗<class_CylinderMesh_property_rings>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rings**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_rings**()

Number of edge rings along the height of the cylinder. Changing
`rings<class_CylinderMesh_property_rings>`{.interpreted-text role="ref"}
does not have any visual impact unless a shader or procedural mesh tool
is used to alter the vertex data. Higher values result in more
subdivisions, which can be used to create smoother-looking effects with
shaders or procedural mesh tools (at the cost of performance). When not
altering the vertex data using a shader or procedural mesh tool,
`rings<class_CylinderMesh_property_rings>`{.interpreted-text role="ref"}
should be kept to its default value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CylinderMesh_property_top_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **top_radius** =
`0.5` `🔗<class_CylinderMesh_property_top_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_top_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_top_radius**()

Top radius of the cylinder. If set to `0.0`, the top faces will not be
generated, resulting in a conic shape. See also
`cap_top<class_CylinderMesh_property_cap_top>`{.interpreted-text
role="ref"}.
