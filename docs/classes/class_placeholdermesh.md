github_url
:   hide

# PlaceholderMesh {#class_PlaceholderMesh}

**Inherits:** `Mesh<class_Mesh>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Placeholder class for a mesh.

::: rst-class
classref-introduction-group
:::

## Description

This class is used when loading a project that uses a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} subclass in 2
conditions:

- When running the project exported in dedicated server mode, only the
  texture\'s dimensions are kept (as they may be relied upon for
  gameplay purposes or positioning of other elements). This allows
  reducing the exported PCK\'s size significantly.
- When this subclass is missing due to using a different engine version
  or build (e.g. modules disabled).

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

:::: {#class_PlaceholderMesh_property_aabb}
::: rst-class
classref-property
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **aabb** =
`AABB(0, 0, 0, 0, 0, 0)`
`🔗<class_PlaceholderMesh_property_aabb>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_aabb**(value: `AABB<class_AABB>`{.interpreted-text role="ref"})
- `AABB<class_AABB>`{.interpreted-text role="ref"} **get_aabb**()

The smallest `AABB<class_AABB>`{.interpreted-text role="ref"} enclosing
this mesh in local space.
