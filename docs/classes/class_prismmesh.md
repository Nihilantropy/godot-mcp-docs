github_url
:   hide

# PrismMesh {#class_PrismMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Class representing a prism-shaped
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Class representing a prism-shaped
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

:::: {#class_PrismMesh_property_left_to_right}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **left_to_right** =
`0.5` `🔗<class_PrismMesh_property_left_to_right>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_left_to_right**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_left_to_right**()

Displacement of the upper edge along the X axis. 0.0 positions edge
straight above the bottom-left edge.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrismMesh_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(1, 1, 1)` `🔗<class_PrismMesh_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

Size of the prism.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrismMesh_property_subdivide_depth}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_depth** = `0`
`🔗<class_PrismMesh_property_subdivide_depth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_depth**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_depth**()

Number of added edge loops along the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrismMesh_property_subdivide_height}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_height** =
`0` `🔗<class_PrismMesh_property_subdivide_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_height**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_height**()

Number of added edge loops along the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrismMesh_property_subdivide_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_width** = `0`
`🔗<class_PrismMesh_property_subdivide_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_width**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_width**()

Number of added edge loops along the X axis.
