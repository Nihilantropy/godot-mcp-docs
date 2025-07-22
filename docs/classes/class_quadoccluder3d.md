github_url
:   hide

# QuadOccluder3D {#class_QuadOccluder3D}

**Inherits:** `Occluder3D<class_Occluder3D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Flat plane shape for use with occlusion culling in
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**QuadOccluder3D** stores a flat plane shape that can be used by the
engine\'s occlusion culling system. See also
`PolygonOccluder3D<class_PolygonOccluder3D>`{.interpreted-text
role="ref"} if you need to customize the quad\'s shape.

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

:::: {#class_QuadOccluder3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **size** =
`Vector2(1, 1)`
`🔗<class_QuadOccluder3D_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()

The quad\'s size in 3D units.
