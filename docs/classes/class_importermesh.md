github_url
:   hide

# ImporterMesh {#class_ImporterMesh}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A `Resource<class_Resource>`{.interpreted-text role="ref"} that contains
vertex array-based geometry during the import process.

::: rst-class
classref-introduction-group
:::

## Description

ImporterMesh is a type of `Resource<class_Resource>`{.interpreted-text
role="ref"} analogous to `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"}. It contains vertex array-based geometry, divided in
*surfaces*. Each surface contains a completely separate array and a
material used to draw it. Design wise, a mesh with multiple surfaces is
preferred to a single surface, because objects created in 3D editing
software commonly contain multiple materials.

Unlike its runtime counterpart, **ImporterMesh** contains mesh data
before various import steps, such as lod and shadow mesh generation,
have taken place. Modify surface data by calling
`clear()<class_ImporterMesh_method_clear>`{.interpreted-text
role="ref"}, followed by
`add_surface()<class_ImporterMesh_method_add_surface>`{.interpreted-text
role="ref"} for each surface.

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

:::: {#class_ImporterMesh_method_add_blend_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_blend_shape**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ImporterMesh_method_add_blend_shape>`{.interpreted-text
role="ref"}

Adds name for a blend shape that will be added with
`add_surface()<class_ImporterMesh_method_add_surface>`{.interpreted-text
role="ref"}. Must be called before surface is added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_add_surface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_surface**(primitive:
`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"},
arrays: `Array<class_Array>`{.interpreted-text role="ref"},
blend_shapes: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\] =
\[\], lods: `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
= {}, material: `Material<class_Material>`{.interpreted-text role="ref"}
= null, name: `String<class_String>`{.interpreted-text role="ref"} =
\"\", flags: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_ImporterMesh_method_add_surface>`{.interpreted-text
role="ref"}

Creates a new surface.
`Mesh.get_surface_count()<class_Mesh_method_get_surface_count>`{.interpreted-text
role="ref"} will become the `surf_idx` for this new surface.

Surfaces are created to be rendered using a `primitive`, which may be
any of the values defined in
`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}.

The `arrays` argument is an array of arrays. Each of the
`Mesh.ARRAY_MAX<class_Mesh_constant_ARRAY_MAX>`{.interpreted-text
role="ref"} elements contains an array with some of the mesh data for
this surface as described by the corresponding member of
`ArrayType<enum_Mesh_ArrayType>`{.interpreted-text role="ref"} or `null`
if it is not used by the surface. For example, `arrays[0]` is the array
of vertices. That first vertex sub-array is always required; the others
are optional. Adding an index array puts this surface into \"index
mode\" where the vertex and other arrays become the sources of data and
the index array defines the vertex order. All sub-arrays must have the
same length as the vertex array (or be an exact multiple of the vertex
array\'s length, when multiple elements of a sub-array correspond to a
single vertex) or be empty, except for
`Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>`{.interpreted-text
role="ref"} if it is used.

The `blend_shapes` argument is an array of vertex data for each blend
shape. Each element is an array of the same structure as `arrays`, but
`Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>`{.interpreted-text
role="ref"},
`Mesh.ARRAY_NORMAL<class_Mesh_constant_ARRAY_NORMAL>`{.interpreted-text
role="ref"}, and
`Mesh.ARRAY_TANGENT<class_Mesh_constant_ARRAY_TANGENT>`{.interpreted-text
role="ref"} are set if and only if they are set in `arrays` and all
other entries are `null`.

The `lods` argument is a dictionary with
`float<class_float>`{.interpreted-text role="ref"} keys and
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
values. Each entry in the dictionary represents an LOD level of the
surface, where the value is the
`Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>`{.interpreted-text
role="ref"} array to use for the LOD level and the key is roughly
proportional to the distance at which the LOD stats being used. I.e.,
increasing the key of an LOD also increases the distance that the
objects has to be from the camera before the LOD is used.

The `flags` argument is the bitwise OR of, as required: One value of
`ArrayCustomFormat<enum_Mesh_ArrayCustomFormat>`{.interpreted-text
role="ref"} left shifted by `ARRAY_FORMAT_CUSTOMn_SHIFT` for each custom
channel in use,
`Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE<class_Mesh_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE>`{.interpreted-text
role="ref"},
`Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>`{.interpreted-text
role="ref"}, or
`Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY<class_Mesh_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When using indices, it is recommended to only use points,
lines, or triangles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_ImporterMesh_method_clear>`{.interpreted-text role="ref"}

Removes all surfaces and blend shapes from this **ImporterMesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_generate_lods}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**generate_lods**(normal_merge_angle:
`float<class_float>`{.interpreted-text role="ref"}, normal_split_angle:
`float<class_float>`{.interpreted-text role="ref"},
bone_transform_array: `Array<class_Array>`{.interpreted-text
role="ref"})
`🔗<class_ImporterMesh_method_generate_lods>`{.interpreted-text
role="ref"}

Generates all lods for this ImporterMesh.

`normal_merge_angle` is in degrees and used in the same way as the
importer settings in `lods`.

`normal_split_angle` is not used and only remains for compatibility with
older versions of the API.

The number of generated lods can be accessed using
`get_surface_lod_count()<class_ImporterMesh_method_get_surface_lod_count>`{.interpreted-text
role="ref"}, and each LOD is available in
`get_surface_lod_size()<class_ImporterMesh_method_get_surface_lod_size>`{.interpreted-text
role="ref"} and
`get_surface_lod_indices()<class_ImporterMesh_method_get_surface_lod_indices>`{.interpreted-text
role="ref"}.

`bone_transform_array` is an `Array<class_Array>`{.interpreted-text
role="ref"} which can be either empty or contain
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}s which,
for each of the mesh\'s bone IDs, will apply mesh skinning when
generating the LOD mesh variations. This is usually used to account for
discrepancies in scale between the mesh itself and its skinning data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_blend_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_blend_shape_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_blend_shape_count>`{.interpreted-text
role="ref"}

Returns the number of blend shapes that the mesh holds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_blend_shape_mode}
::: rst-class
classref-method
:::
::::

`BlendShapeMode<enum_Mesh_BlendShapeMode>`{.interpreted-text role="ref"}
**get_blend_shape_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_blend_shape_mode>`{.interpreted-text
role="ref"}

Returns the blend shape mode for this Mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_blend_shape_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_blend_shape_name**(blend_shape_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_blend_shape_name>`{.interpreted-text
role="ref"}

Returns the name of the blend shape at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_lightmap_size_hint}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_lightmap_size_hint**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_lightmap_size_hint>`{.interpreted-text
role="ref"}

Returns the size hint of this mesh for lightmap-unwrapping in UV-space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_mesh}
::: rst-class
classref-method
:::
::::

`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
**get_mesh**(base_mesh: `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"} = null)
`🔗<class_ImporterMesh_method_get_mesh>`{.interpreted-text role="ref"}

Returns the mesh data represented by this **ImporterMesh** as a usable
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}.

This method caches the returned mesh, and subsequent calls will return
the cached data until
`clear()<class_ImporterMesh_method_clear>`{.interpreted-text role="ref"}
is called.

If not yet cached and `base_mesh` is provided, `base_mesh` will be used
and mutated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_surface_arrays**(surface_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_arrays>`{.interpreted-text
role="ref"}

Returns the arrays for the vertices, normals, UVs, etc. that make up the
requested surface. See
`add_surface()<class_ImporterMesh_method_add_surface>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_blend_shape_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_surface_blend_shape_arrays**(surface_idx:
`int<class_int>`{.interpreted-text role="ref"}, blend_shape_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_blend_shape_arrays>`{.interpreted-text
role="ref"}

Returns a single set of blend shape arrays for the requested blend shape
index for a surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_surface_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_count>`{.interpreted-text
role="ref"}

Returns the number of surfaces that the mesh holds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_format}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_surface_format**(surface_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_format>`{.interpreted-text
role="ref"}

Returns the format of the surface that the mesh holds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_lod_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_surface_lod_count**(surface_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_lod_count>`{.interpreted-text
role="ref"}

Returns the number of lods that the mesh holds on a given surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_lod_indices}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_surface_lod_indices**(surface_idx:
`int<class_int>`{.interpreted-text role="ref"}, lod_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_lod_indices>`{.interpreted-text
role="ref"}

Returns the index buffer of a lod for a surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_lod_size}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_surface_lod_size**(surface_idx: `int<class_int>`{.interpreted-text
role="ref"}, lod_idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_lod_size>`{.interpreted-text
role="ref"}

Returns the screen ratio which activates a lod for a surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_material}
::: rst-class
classref-method
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**get_surface_material**(surface_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_material>`{.interpreted-text
role="ref"}

Returns a `Material<class_Material>`{.interpreted-text role="ref"} in a
given surface. Surface is rendered using this material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_surface_name**(surface_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ImporterMesh_method_get_surface_name>`{.interpreted-text
role="ref"}

Gets the name assigned to this surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_get_surface_primitive_type}
::: rst-class
classref-method
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**get_surface_primitive_type**(surface_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_ImporterMesh_method_get_surface_primitive_type>`{.interpreted-text
role="ref"}

Returns the primitive type of the requested surface (see
`add_surface()<class_ImporterMesh_method_add_surface>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_set_blend_shape_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_shape_mode**(mode:
`BlendShapeMode<enum_Mesh_BlendShapeMode>`{.interpreted-text
role="ref"})
`🔗<class_ImporterMesh_method_set_blend_shape_mode>`{.interpreted-text
role="ref"}

Sets the blend shape mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_set_lightmap_size_hint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_lightmap_size_hint**(size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_ImporterMesh_method_set_lightmap_size_hint>`{.interpreted-text
role="ref"}

Sets the size hint of this mesh for lightmap-unwrapping in UV-space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_set_surface_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_surface_material**(surface_idx: `int<class_int>`{.interpreted-text
role="ref"}, material: `Material<class_Material>`{.interpreted-text
role="ref"})
`🔗<class_ImporterMesh_method_set_surface_material>`{.interpreted-text
role="ref"}

Sets a `Material<class_Material>`{.interpreted-text role="ref"} for a
given surface. Surface will be rendered using this material.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImporterMesh_method_set_surface_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_surface_name**(surface_idx: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ImporterMesh_method_set_surface_name>`{.interpreted-text
role="ref"}

Sets a name for a given surface.
