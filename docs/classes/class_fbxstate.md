github_url
:   hide

# FBXState {#class_FBXState}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `GLTFState<class_GLTFState>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

::: rst-class
classref-introduction-group
:::

## Description

The FBXState handles the state data imported from FBX files.

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

:::: {#class_FBXState_property_allow_geometry_helper_nodes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**allow_geometry_helper_nodes** = `false`
`🔗<class_FBXState_property_allow_geometry_helper_nodes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_geometry_helper_nodes**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_allow_geometry_helper_nodes**()

If `true`, the import process used auxiliary nodes called geometry
helper nodes. These nodes help preserve the pivots and transformations
of the original 3D model during import.
