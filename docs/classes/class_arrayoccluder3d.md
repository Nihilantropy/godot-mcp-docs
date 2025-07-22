github_url
:   hide

# ArrayOccluder3D {#class_ArrayOccluder3D}

**Inherits:** `Occluder3D<class_Occluder3D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

3D polygon shape for use with occlusion culling in
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**ArrayOccluder3D** stores an arbitrary 3D polygon shape that can be
used by the engine\'s occlusion culling system. This is analogous to
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}, but for
occluders.

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

## Property Descriptions

:::: {#class_ArrayOccluder3D_property_indices}
::: rst-class
classref-property
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**indices** = `PackedInt32Array()`
`🔗<class_ArrayOccluder3D_property_indices>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_indices**(value:
  `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"})
- `PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
  role="ref"} **get_indices**()

The occluder\'s index position. Indices determine which points from the
`vertices<class_ArrayOccluder3D_property_vertices>`{.interpreted-text
role="ref"} array should be drawn, and in which order.

\*\*Note:\*\* The occluder is always updated after setting this value.
If creating occluders procedurally, consider using
`set_arrays()<class_ArrayOccluder3D_method_set_arrays>`{.interpreted-text
role="ref"} instead to avoid updating the occluder twice when it\'s
created.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayOccluder3D_property_vertices}
::: rst-class
classref-property
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **vertices** = `PackedVector3Array()`
`🔗<class_ArrayOccluder3D_property_vertices>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertices**(value:
  `PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
  role="ref"})
- `PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
  role="ref"} **get_vertices**()

The occluder\'s vertex positions in local 3D coordinates.

\*\*Note:\*\* The occluder is always updated after setting this value.
If creating occluders procedurally, consider using
`set_arrays()<class_ArrayOccluder3D_method_set_arrays>`{.interpreted-text
role="ref"} instead to avoid updating the occluder twice when it\'s
created.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ArrayOccluder3D_method_set_arrays}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_arrays**(vertices:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, indices:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_ArrayOccluder3D_method_set_arrays>`{.interpreted-text
role="ref"}

Sets `indices<class_ArrayOccluder3D_property_indices>`{.interpreted-text
role="ref"} and
`vertices<class_ArrayOccluder3D_property_vertices>`{.interpreted-text
role="ref"}, while updating the final occluder only once after both
values are set.
