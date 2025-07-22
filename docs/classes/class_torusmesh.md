github_url
:   hide

# TorusMesh {#class_TorusMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Class representing a torus
`PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Class representing a torus
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

:::: {#class_TorusMesh_property_inner_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **inner_radius** =
`0.5` `🔗<class_TorusMesh_property_inner_radius>`{.interpreted-text
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

:::: {#class_TorusMesh_property_outer_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **outer_radius** =
`1.0` `🔗<class_TorusMesh_property_outer_radius>`{.interpreted-text
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

:::: {#class_TorusMesh_property_ring_segments}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **ring_segments** = `32`
`🔗<class_TorusMesh_property_ring_segments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ring_segments**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_ring_segments**()

The number of edges each ring of the torus is constructed of.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TorusMesh_property_rings}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rings** = `64`
`🔗<class_TorusMesh_property_rings>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_rings**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_rings**()

The number of slices the torus is constructed of.
