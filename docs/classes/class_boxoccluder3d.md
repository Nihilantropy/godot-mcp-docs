github_url
:   hide

# BoxOccluder3D {#class_BoxOccluder3D}

**Inherits:** `Occluder3D<class_Occluder3D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Cuboid shape for use with occlusion culling in
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**BoxOccluder3D** stores a cuboid shape that can be used by the
engine\'s occlusion culling system.

See `OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"}\'s documentation for instructions on setting up occlusion
culling.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Occlusion culling <../tutorials/3d/occlusion_culling>`{.interpreted-text
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

:::: {#class_BoxOccluder3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(1, 1, 1)`
`🔗<class_BoxOccluder3D_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The box\'s size in 3D units.
