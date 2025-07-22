github_url
:   hide

::: {.meta keywords="batch"}
:::

# MultiMeshInstance3D {#class_MultiMeshInstance3D}

**Inherits:**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Node that instances a `MultiMesh<class_MultiMesh>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**MultiMeshInstance3D** is a specialized node to instance
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"}s based on a `MultiMesh<class_MultiMesh>`{.interpreted-text
role="ref"} resource.

This is useful to optimize the rendering of a high number of instances
of a given mesh (for example trees in a forest or grass strands).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using MultiMeshInstance <../tutorials/3d/using_multi_mesh_instance>`{.interpreted-text
  role="doc"}
- `Optimization using MultiMeshes <../tutorials/performance/using_multimesh>`{.interpreted-text
  role="doc"}
- `Animating thousands of fish with MultiMeshInstance <../tutorials/performance/vertex_animation/animating_thousands_of_fish>`{.interpreted-text
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

:::: {#class_MultiMeshInstance3D_property_multimesh}
::: rst-class
classref-property
:::
::::

`MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"} **multimesh**
`🔗<class_MultiMeshInstance3D_property_multimesh>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_multimesh**(value:
  `MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"})
- `MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"}
  **get_multimesh**()

The `MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"} resource
that will be used and shared among all instances of the
**MultiMeshInstance3D**.
