github_url
:   hide

# CSGCylinder3D {#class_CSGCylinder3D}

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>`{.interpreted-text
role="ref"} **\<** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A CSG Cylinder shape.

::: rst-class
classref-introduction-group
:::

## Description

This node allows you to create a cylinder (or cone) for use with the CSG
system.

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

:::: {#class_CSGCylinder3D_property_cone}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **cone** = `false`
`🔗<class_CSGCylinder3D_property_cone>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cone**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_cone**()

If `true` a cone is created, the
`radius<class_CSGCylinder3D_property_radius>`{.interpreted-text
role="ref"} will only apply to one side.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGCylinder3D_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `2.0`
`🔗<class_CSGCylinder3D_property_height>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The height of the cylinder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGCylinder3D_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_CSGCylinder3D_property_material>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The material used to render the cylinder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGCylinder3D_property_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radius** = `0.5`
`🔗<class_CSGCylinder3D_property_radius>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_radius**()

The radius of the cylinder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGCylinder3D_property_sides}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sides** = `8`
`🔗<class_CSGCylinder3D_property_sides>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sides**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sides**()

The number of sides of the cylinder, the higher this number the more
detail there will be in the cylinder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGCylinder3D_property_smooth_faces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **smooth_faces** =
`true` `🔗<class_CSGCylinder3D_property_smooth_faces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_smooth_faces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_smooth_faces**()

If `true` the normals of the cylinder are set to give a smooth effect
making the cylinder seem rounded. If `false` the cylinder will have a
flat shaded look.
