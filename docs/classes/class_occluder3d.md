github_url
:   hide

# Occluder3D {#class_Occluder3D}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`ArrayOccluder3D<class_ArrayOccluder3D>`{.interpreted-text role="ref"},
`BoxOccluder3D<class_BoxOccluder3D>`{.interpreted-text role="ref"},
`PolygonOccluder3D<class_PolygonOccluder3D>`{.interpreted-text
role="ref"}, `QuadOccluder3D<class_QuadOccluder3D>`{.interpreted-text
role="ref"},
`SphereOccluder3D<class_SphereOccluder3D>`{.interpreted-text role="ref"}

Occluder shape resource for use with occlusion culling in
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**Occluder3D** stores an occluder shape that can be used by the
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

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Occluder3D_method_get_indices}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_indices**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Occluder3D_method_get_indices>`{.interpreted-text
role="ref"}

Returns the occluder shape\'s vertex indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Occluder3D_method_get_vertices}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_vertices**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Occluder3D_method_get_vertices>`{.interpreted-text role="ref"}

Returns the occluder shape\'s vertex positions.
