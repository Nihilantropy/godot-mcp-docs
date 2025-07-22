github_url
:   hide

# PolygonOccluder3D {#class_PolygonOccluder3D}

**Inherits:** `Occluder3D<class_Occluder3D>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Flat 2D polygon shape for use with occlusion culling in
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**PolygonOccluder3D** stores a polygon shape that can be used by the
engine\'s occlusion culling system. When an
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"} with a **PolygonOccluder3D** is selected in the editor, an
editor will appear at the top of the 3D viewport so you can add/remove
points. All points must be placed on the same 2D plane, which means it
is not possible to create arbitrary 3D shapes with a single
**PolygonOccluder3D**. To use arbitrary 3D shapes as occluders, use
`ArrayOccluder3D<class_ArrayOccluder3D>`{.interpreted-text role="ref"}
or `OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"}\'s baking feature instead.

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

:::: {#class_PolygonOccluder3D_property_polygon}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **polygon** = `PackedVector2Array()`
`🔗<class_PolygonOccluder3D_property_polygon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_polygon**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_polygon**()

The polygon to use for occlusion culling. The polygon can be convex or
concave, but it should have as few points as possible to maximize
performance.

The polygon must *not* have intersecting lines. Otherwise, triangulation
will fail (with an error message printed).

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.
