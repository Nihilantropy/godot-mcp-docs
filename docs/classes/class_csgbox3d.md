github_url
:   hide

# CSGBox3D {#class_CSGBox3D}

**Inherits:** `CSGPrimitive3D<class_CSGPrimitive3D>`{.interpreted-text
role="ref"} **\<** `CSGShape3D<class_CSGShape3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A CSG Box shape.

::: rst-class
classref-introduction-group
:::

## Description

This node allows you to create a box for use with the CSG system.

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

:::: {#class_CSGBox3D_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_CSGBox3D_property_material>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The material used to render the box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CSGBox3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(1, 1, 1)` `🔗<class_CSGBox3D_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The box\'s width, height and depth.
