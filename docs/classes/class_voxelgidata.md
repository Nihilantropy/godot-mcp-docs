github_url
:   hide

# VoxelGIData {#class_VoxelGIData}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Contains baked voxel global illumination data for use in a
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} node.

::: rst-class
classref-introduction-group
:::

## Description

**VoxelGIData** contains baked voxel global illumination for use in a
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} node.
**VoxelGIData** also offers several properties to adjust the final
appearance of the global illumination. These properties can be adjusted
at run-time without having to bake the
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} node again.

\*\*Note:\*\* To prevent text-based scene files (`.tscn`) from growing
too much and becoming slow to load and save, always save **VoxelGIData**
to an external binary resource file (`.res`) instead of embedding it
within the scene. This can be done by clicking the dropdown arrow next
to the **VoxelGIData** resource, choosing **Edit**, clicking the floppy
disk icon at the top of the Inspector then choosing **Save As\...**.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

:::: {#class_VoxelGIData_property_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **bias** = `1.5`
`🔗<class_VoxelGIData_property_bias>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_bias**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_bias**()

The normal bias to use for indirect lighting and reflections. Higher
values reduce self-reflections visible in non-rough materials, at the
cost of more visible light leaking and flatter-looking indirect
lighting. To prioritize hiding self-reflections over lighting quality,
set `bias<class_VoxelGIData_property_bias>`{.interpreted-text
role="ref"} to `0.0` and
`normal_bias<class_VoxelGIData_property_normal_bias>`{.interpreted-text
role="ref"} to a value between `1.0` and `2.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_property_dynamic_range}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dynamic_range** =
`2.0` `🔗<class_VoxelGIData_property_dynamic_range>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dynamic_range**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_dynamic_range**()

The dynamic range to use (`1.0` represents a low dynamic range scene
brightness). Higher values can be used to provide brighter indirect
lighting, at the cost of more visible color banding in dark areas (both
in indirect lighting and reflections). To avoid color banding, it\'s
recommended to use the lowest value that does not result in visible
light clipping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_property_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **energy** = `1.0`
`🔗<class_VoxelGIData_property_energy>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_energy**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_energy**()

The energy of the indirect lighting and reflections produced by the
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} node. Higher
values result in brighter indirect lighting. If indirect lighting looks
too flat, try decreasing
`propagation<class_VoxelGIData_property_propagation>`{.interpreted-text
role="ref"} while increasing
`energy<class_VoxelGIData_property_energy>`{.interpreted-text
role="ref"} at the same time. See also
`use_two_bounces<class_VoxelGIData_property_use_two_bounces>`{.interpreted-text
role="ref"} which influences the indirect lighting\'s effective
brightness.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_property_interior}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **interior** = `false`
`🔗<class_VoxelGIData_property_interior>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interior**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_interior**()

If `true`, `Environment<class_Environment>`{.interpreted-text
role="ref"} lighting is ignored by the
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} node. If `false`,
`Environment<class_Environment>`{.interpreted-text role="ref"} lighting
is taken into account by the `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} node. `Environment<class_Environment>`{.interpreted-text
role="ref"} lighting updates in real-time, which means it can be changed
without having to bake the `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} node again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_property_normal_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **normal_bias** =
`0.0` `🔗<class_VoxelGIData_property_normal_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_normal_bias**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_normal_bias**()

The normal bias to use for indirect lighting and reflections. Higher
values reduce self-reflections visible in non-rough materials, at the
cost of more visible light leaking and flatter-looking indirect
lighting. See also
`bias<class_VoxelGIData_property_bias>`{.interpreted-text role="ref"}.
To prioritize hiding self-reflections over lighting quality, set
`bias<class_VoxelGIData_property_bias>`{.interpreted-text role="ref"} to
`0.0` and
`normal_bias<class_VoxelGIData_property_normal_bias>`{.interpreted-text
role="ref"} to a value between `1.0` and `2.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_property_propagation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **propagation** =
`0.5` `🔗<class_VoxelGIData_property_propagation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_propagation**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_propagation**()

The multiplier to use when light bounces off a surface. Higher values
result in brighter indirect lighting. If indirect lighting looks too
flat, try decreasing
`propagation<class_VoxelGIData_property_propagation>`{.interpreted-text
role="ref"} while increasing
`energy<class_VoxelGIData_property_energy>`{.interpreted-text
role="ref"} at the same time. See also
`use_two_bounces<class_VoxelGIData_property_use_two_bounces>`{.interpreted-text
role="ref"} which influences the indirect lighting\'s effective
brightness.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_property_use_two_bounces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_two_bounces** =
`true`
`🔗<class_VoxelGIData_property_use_two_bounces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_two_bounces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_two_bounces**()

If `true`, performs two bounces of indirect lighting instead of one.
This makes indirect lighting look more natural and brighter at a small
performance cost. The second bounce is also visible in reflections. If
the scene appears too bright after enabling
`use_two_bounces<class_VoxelGIData_property_use_two_bounces>`{.interpreted-text
role="ref"}, adjust
`propagation<class_VoxelGIData_property_propagation>`{.interpreted-text
role="ref"} and
`energy<class_VoxelGIData_property_energy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VoxelGIData_method_allocate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**allocate**(to_cell_xform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}, aabb:
`AABB<class_AABB>`{.interpreted-text role="ref"}, octree_size:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, octree_cells:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
data_cells: `PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}, distance_field:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"},
level_counts:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}) `🔗<class_VoxelGIData_method_allocate>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_method_get_bounds}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **get_bounds**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_VoxelGIData_method_get_bounds>`{.interpreted-text
role="ref"}

Returns the bounds of the baked voxel data as an
`AABB<class_AABB>`{.interpreted-text role="ref"}, which should match
`VoxelGI.size<class_VoxelGI_property_size>`{.interpreted-text
role="ref"} after being baked (which only contains the size as a
`Vector3<class_Vector3>`{.interpreted-text role="ref"}).

\*\*Note:\*\* If the size was modified without baking the VoxelGI data,
then the value of
`get_bounds()<class_VoxelGIData_method_get_bounds>`{.interpreted-text
role="ref"} and
`VoxelGI.size<class_VoxelGI_property_size>`{.interpreted-text
role="ref"} will not match.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_method_get_data_cells}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_data_cells**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VoxelGIData_method_get_data_cells>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_method_get_level_counts}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_level_counts**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VoxelGIData_method_get_level_counts>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_method_get_octree_cells}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_octree_cells**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VoxelGIData_method_get_octree_cells>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_method_get_octree_size}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_octree_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VoxelGIData_method_get_octree_size>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VoxelGIData_method_get_to_cell_xform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_to_cell_xform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VoxelGIData_method_get_to_cell_xform>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
