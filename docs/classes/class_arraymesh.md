github_url
:   hide

# ArrayMesh {#class_ArrayMesh}

**Inherits:** `Mesh<class_Mesh>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

`Mesh<class_Mesh>`{.interpreted-text role="ref"} type that provides
utility for constructing a surface from arrays.

::: rst-class
classref-introduction-group
:::

## Description

The **ArrayMesh** is used to construct a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} by specifying the
attributes as arrays.

The most basic example is the creation of a single triangle:

::::: tabs
::: code-tab
gdscript

var vertices = PackedVector3Array() vertices.push_back(Vector3(0, 1, 0))
vertices.push_back(Vector3(1, 0, 0)) vertices.push_back(Vector3(0, 0,
1))

\# Initialize the ArrayMesh. var arr_mesh = ArrayMesh.new() var arrays =
\[\] arrays.resize(Mesh.ARRAY_MAX) arrays\[Mesh.ARRAY_VERTEX\] =
vertices

\# Create the Mesh.
arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, arrays) var m
= MeshInstance3D.new() m.mesh = arr_mesh
:::

::: code-tab
csharp

Vector3\[\] vertices = \[ new Vector3(0, 1, 0), new Vector3(1, 0, 0),
new Vector3(0, 0, 1), \];

// Initialize the ArrayMesh. var arrMesh = new ArrayMesh();
Godot.Collections.Array arrays = \[\];
arrays.Resize((int)Mesh.ArrayType.Max);
arrays\[(int)Mesh.ArrayType.Vertex\] = vertices;

// Create the Mesh.
arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, arrays); var
m = new MeshInstance3D(); m.Mesh = arrMesh;
:::
:::::

The `MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}
is ready to be added to the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} to be shown.

See also `ImmediateMesh<class_ImmediateMesh>`{.interpreted-text
role="ref"}, `MeshDataTool<class_MeshDataTool>`{.interpreted-text
role="ref"} and `SurfaceTool<class_SurfaceTool>`{.interpreted-text
role="ref"} for procedural geometry generation.

\*\*Note:\*\* Godot uses clockwise [winding
order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front
faces of triangle primitive modes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Procedural geometry using the ArrayMesh <../tutorials/3d/procedural_geometry/arraymesh>`{.interpreted-text
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

:::: {#class_ArrayMesh_property_blend_shape_mode}
::: rst-class
classref-property
:::
::::

`BlendShapeMode<enum_Mesh_BlendShapeMode>`{.interpreted-text role="ref"}
**blend_shape_mode** = `1`
`🔗<class_ArrayMesh_property_blend_shape_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_shape_mode**(value:
  `BlendShapeMode<enum_Mesh_BlendShapeMode>`{.interpreted-text
  role="ref"})
- `BlendShapeMode<enum_Mesh_BlendShapeMode>`{.interpreted-text
  role="ref"} **get_blend_shape_mode**()

The blend shape mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_property_custom_aabb}
::: rst-class
classref-property
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **custom_aabb** =
`AABB(0, 0, 0, 0, 0, 0)`
`🔗<class_ArrayMesh_property_custom_aabb>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_aabb**(value: `AABB<class_AABB>`{.interpreted-text
  role="ref"})
- `AABB<class_AABB>`{.interpreted-text role="ref"} **get_custom_aabb**()

Overrides the `AABB<class_AABB>`{.interpreted-text role="ref"} with one
defined by user for use with frustum culling. Especially useful to avoid
unexpected culling when using a shader to offset vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_property_shadow_mesh}
::: rst-class
classref-property
:::
::::

`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
**shadow_mesh**
`🔗<class_ArrayMesh_property_shadow_mesh>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_mesh**(value:
  `ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"})
- `ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
  **get_shadow_mesh**()

An optional mesh which can be used for rendering shadows and the depth
prepass. Can be used to increase performance by supplying a mesh with
fused vertices and only vertex position data (without normals, UVs,
colors, etc.).

\*\*Note:\*\* This mesh must have exactly the same vertex positions as
the source mesh (including the source mesh\'s LODs, if present). If
vertex positions differ, then the mesh will not draw correctly.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ArrayMesh_method_add_blend_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_blend_shape**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_ArrayMesh_method_add_blend_shape>`{.interpreted-text
role="ref"}

Adds name for a blend shape that will be added with
`add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"}. Must be called before surface is added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_add_surface_from_arrays}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_surface_from_arrays**(primitive:
`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"},
arrays: `Array<class_Array>`{.interpreted-text role="ref"},
blend_shapes: `Array<class_Array>`{.interpreted-text
role="ref"}\[`Array<class_Array>`{.interpreted-text role="ref"}\] =
\[\], lods: `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
= {}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
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

:::: {#class_ArrayMesh_method_clear_blend_shapes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_blend_shapes**()
`🔗<class_ArrayMesh_method_clear_blend_shapes>`{.interpreted-text
role="ref"}

Removes all blend shapes from this **ArrayMesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_clear_surfaces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_surfaces**()
`🔗<class_ArrayMesh_method_clear_surfaces>`{.interpreted-text
role="ref"}

Removes all surfaces from this **ArrayMesh**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_get_blend_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_blend_shape_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_get_blend_shape_count>`{.interpreted-text
role="ref"}

Returns the number of blend shapes that the **ArrayMesh** holds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_get_blend_shape_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_blend_shape_name**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_get_blend_shape_name>`{.interpreted-text
role="ref"}

Returns the name of the blend shape at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_lightmap_unwrap}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**lightmap_unwrap**(transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
texel_size: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_ArrayMesh_method_lightmap_unwrap>`{.interpreted-text
role="ref"}

Performs a UV unwrap on the **ArrayMesh** to prepare the mesh for
lightmapping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_regen_normal_maps}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**regen_normal_maps**()
`🔗<class_ArrayMesh_method_regen_normal_maps>`{.interpreted-text
role="ref"}

Regenerates tangents for each of the **ArrayMesh**\'s surfaces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_set_blend_shape_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_shape_name**(index: `int<class_int>`{.interpreted-text
role="ref"}, name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_ArrayMesh_method_set_blend_shape_name>`{.interpreted-text
role="ref"}

Sets the name of the blend shape at this index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_find_by_name}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**surface_find_by_name**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_surface_find_by_name>`{.interpreted-text
role="ref"}

Returns the index of the first surface with this name held within this
**ArrayMesh**. If none are found, -1 is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_get_array_index_len}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**surface_get_array_index_len**(surf_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_surface_get_array_index_len>`{.interpreted-text
role="ref"}

Returns the length in indices of the index array in the requested
surface (see
`add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_get_array_len}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**surface_get_array_len**(surf_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_surface_get_array_len>`{.interpreted-text
role="ref"}

Returns the length in vertices of the vertex array in the requested
surface (see
`add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_get_format}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text
role="ref"}\] **surface_get_format**(surf_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_surface_get_format>`{.interpreted-text
role="ref"}

Returns the format mask of the requested surface (see
`add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**surface_get_name**(surf_idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_surface_get_name>`{.interpreted-text
role="ref"}

Gets the name assigned to this surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_get_primitive_type}
::: rst-class
classref-method
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**surface_get_primitive_type**(surf_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ArrayMesh_method_surface_get_primitive_type>`{.interpreted-text
role="ref"}

Returns the primitive type of the requested surface (see
`add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_remove}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_remove**(surf_idx: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_ArrayMesh_method_surface_remove>`{.interpreted-text
role="ref"}

Removes the surface at the given index from the Mesh, shifting surfaces
with higher index down by one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_set_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_set_name**(surf_idx: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ArrayMesh_method_surface_set_name>`{.interpreted-text
role="ref"}

Sets a name for a given surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ArrayMesh_method_surface_update_attribute_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_update_attribute_region**(surf_idx:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_ArrayMesh_method_surface_update_attribute_region>`{.interpreted-text
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

:::: {#class_ArrayMesh_method_surface_update_skin_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_update_skin_region**(surf_idx:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_ArrayMesh_method_surface_update_skin_region>`{.interpreted-text
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

:::: {#class_ArrayMesh_method_surface_update_vertex_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_update_vertex_region**(surf_idx:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`int<class_int>`{.interpreted-text role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_ArrayMesh_method_surface_update_vertex_region>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
