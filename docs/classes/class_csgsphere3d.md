github_url
:   hide

# CSGSphere3D {#class_CSGSphere3D}

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>`{.interpreted-text
role="ref"} **\<** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A CSG Sphere shape.

::: rst-class
classref-introduction-group
:::

## Description

This node allows you to create a sphere for use with the CSG system.

\*\*Note:\*\* CSG nodes are intended to be used for level prototyping.
Creating CSG nodes has a significant CPU cost compared to creating a
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
with a `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"}. Moving a CSG node within another CSG node also has a
significant CPU cost, so it should be avoided during gameplay.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Prototyping levels with CSG <../tutorials/3d/csg_tools>`{.interpreted-text
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

:::: {#class_CSGSphere3D_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_CSGSphere3D_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The material used to render the sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGSphere3D_property_radial_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **radial_segments** =
`12` `🔗<class_CSGSphere3D_property_radial_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radial_segments**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_radial_segments**()

Number of vertical slices for the sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGSphere3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_CSGSphere3D_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

Radius of the sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGSphere3D_property_rings}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rings** = `6`
`🔗<class_CSGSphere3D_property_rings>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rings**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_rings**()

Number of horizontal slices for the sphere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGSphere3D_property_smooth_faces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **smooth_faces** =
`true` `🔗<class_CSGSphere3D_property_smooth_faces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_smooth_faces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_smooth_faces**()

If `true` the normals of the sphere are set to give a smooth effect
making the sphere seem rounded. If `false` the sphere will have a flat
shaded look.
