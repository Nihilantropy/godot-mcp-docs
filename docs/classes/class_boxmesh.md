github_url
:   hide

# BoxMesh {#class_BoxMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Generate an axis-aligned box
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Generate an axis-aligned box
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

The box\'s UV layout is arranged in a 3×2 layout that allows texturing
each face individually. To apply the same texture on all faces, change
the material\'s UV property to `Vector3(3, 2, 1)`. This is equivalent to
adding `UV *= vec2(3.0, 2.0)` in a vertex shader.

\*\*Note:\*\* When using a large textured **BoxMesh** (e.g. as a floor),
you may stumble upon UV jittering issues depending on the camera angle.
To solve this, increase
`subdivide_depth<class_BoxMesh_property_subdivide_depth>`{.interpreted-text
role="ref"},
`subdivide_height<class_BoxMesh_property_subdivide_height>`{.interpreted-text
role="ref"} and
`subdivide_width<class_BoxMesh_property_subdivide_width>`{.interpreted-text
role="ref"} until you no longer notice UV jittering.

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

:::: {#class_BoxMesh_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(1, 1, 1)` `🔗<class_BoxMesh_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The box\'s width, height and depth.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoxMesh_property_subdivide_depth}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_depth** = `0`
`🔗<class_BoxMesh_property_subdivide_depth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_depth**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_depth**()

Number of extra edge loops inserted along the Z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoxMesh_property_subdivide_height}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_height** =
`0` `🔗<class_BoxMesh_property_subdivide_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_height**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_height**()

Number of extra edge loops inserted along the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_BoxMesh_property_subdivide_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subdivide_width** = `0`
`🔗<class_BoxMesh_property_subdivide_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subdivide_width**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_subdivide_width**()

Number of extra edge loops inserted along the X axis.
