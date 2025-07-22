github_url
:   hide

# CSGTorus3D {#class_CSGTorus3D}

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>`{.interpreted-text
role="ref"} **\<** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A CSG Torus shape.

::: rst-class
classref-introduction-group
:::

## Description

This node allows you to create a torus for use with the CSG system.

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

:::: {#class_CSGTorus3D_property_inner_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **inner_radius** =
`0.5` `🔗<class_CSGTorus3D_property_inner_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inner_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_inner_radius**()

The inner radius of the torus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGTorus3D_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_CSGTorus3D_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The material used to render the torus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGTorus3D_property_outer_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **outer_radius** =
`1.0` `🔗<class_CSGTorus3D_property_outer_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outer_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_outer_radius**()

The outer radius of the torus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGTorus3D_property_ring_sides}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **ring_sides** = `6`
`🔗<class_CSGTorus3D_property_ring_sides>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ring_sides**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_ring_sides**()

The number of edges each ring of the torus is constructed of.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGTorus3D_property_sides}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sides** = `8`
`🔗<class_CSGTorus3D_property_sides>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sides**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sides**()

The number of slices the torus is constructed of.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGTorus3D_property_smooth_faces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **smooth_faces** =
`true` `🔗<class_CSGTorus3D_property_smooth_faces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_smooth_faces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_smooth_faces**()

If `true` the normals of the torus are set to give a smooth effect
making the torus seem rounded. If `false` the torus will have a flat
shaded look.
