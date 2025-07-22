github_url
:   hide

# SurfaceTool {#class_SurfaceTool}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Helper tool to create geometry.

::: rst-class
classref-introduction-group
:::

## Description

The **SurfaceTool** is used to construct a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} by specifying vertex
attributes individually. It can be used to construct a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} from a script. All
properties except indices need to be added before calling
`add_vertex()<class_SurfaceTool_method_add_vertex>`{.interpreted-text
role="ref"}. For example, to add vertex colors and UVs:

::::: tabs
::: code-tab
gdscript

var st = SurfaceTool.new() st.begin(Mesh.PRIMITIVE_TRIANGLES)
st.set_color(Color(1, 0, 0)) st.set_uv(Vector2(0, 0))
st.add_vertex(Vector3(0, 0, 0))
:::

::: code-tab
csharp

var st = new SurfaceTool(); st.Begin(Mesh.PrimitiveType.Triangles);
st.SetColor(new Color(1, 0, 0)); st.SetUV(new Vector2(0, 0));
st.AddVertex(new Vector3(0, 0, 0));
:::
:::::

The above **SurfaceTool** now contains one vertex of a triangle which
has a UV coordinate and a specified
`Color<class_Color>`{.interpreted-text role="ref"}. If another vertex
were added without calling
`set_uv()<class_SurfaceTool_method_set_uv>`{.interpreted-text
role="ref"} or
`set_color()<class_SurfaceTool_method_set_color>`{.interpreted-text
role="ref"}, then the last values would be used.

Vertex attributes must be passed **before** calling
`add_vertex()<class_SurfaceTool_method_add_vertex>`{.interpreted-text
role="ref"}. Failure to do so will result in an error when committing
the vertex information to a mesh.

Additionally, the attributes used before the first vertex is added
determine the format of the mesh. For example, if you only add UVs to
the first vertex, you cannot add color to any of the subsequent
vertices.

See also `ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"},
`ImmediateMesh<class_ImmediateMesh>`{.interpreted-text role="ref"} and
`MeshDataTool<class_MeshDataTool>`{.interpreted-text role="ref"} for
procedural geometry generation.

\*\*Note:\*\* Godot uses clockwise [winding
order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front
faces of triangle primitive modes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using the SurfaceTool <../tutorials/3d/procedural_geometry/surfacetool>`{.interpreted-text
  role="doc"}
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

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

## Enumerations

:::: {#enum_SurfaceTool_CustomFormat}
::: rst-class
classref-enumeration
:::
::::

enum **CustomFormat**:
`🔗<enum_SurfaceTool_CustomFormat>`{.interpreted-text role="ref"}

:::: {#class_SurfaceTool_constant_CUSTOM_RGBA8_UNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_RGBA8_UNORM** = `0`

Limits range of data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} to unsigned normalized 0 to 1 stored in 8 bits per channel.
See
`Mesh.ARRAY_CUSTOM_RGBA8_UNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_UNORM>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_RGBA8_SNORM}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_RGBA8_SNORM** = `1`

Limits range of data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} to signed normalized -1 to 1 stored in 8 bits per channel.
See
`Mesh.ARRAY_CUSTOM_RGBA8_SNORM<class_Mesh_constant_ARRAY_CUSTOM_RGBA8_SNORM>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_RG_HALF}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_RG_HALF** = `2`

Stores data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} as half precision floats, and uses only red and green color
channels. See
`Mesh.ARRAY_CUSTOM_RG_HALF<class_Mesh_constant_ARRAY_CUSTOM_RG_HALF>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_RGBA_HALF}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_RGBA_HALF** = `3`

Stores data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} as half precision floats and uses all color channels. See
`Mesh.ARRAY_CUSTOM_RGBA_HALF<class_Mesh_constant_ARRAY_CUSTOM_RGBA_HALF>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_R_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_R_FLOAT** = `4`

Stores data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} as full precision floats, and uses only red color channel.
See
`Mesh.ARRAY_CUSTOM_R_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_R_FLOAT>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_RG_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_RG_FLOAT** = `5`

Stores data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} as full precision floats, and uses only red and green color
channels. See
`Mesh.ARRAY_CUSTOM_RG_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_RG_FLOAT>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_RGB_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_RGB_FLOAT** = `6`

Stores data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} as full precision floats, and uses only red, green and blue
color channels. See
`Mesh.ARRAY_CUSTOM_RGB_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_RGB_FLOAT>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_RGBA_FLOAT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_RGBA_FLOAT** = `7`

Stores data passed to
`set_custom()<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"} as full precision floats, and uses all color channels. See
`Mesh.ARRAY_CUSTOM_RGBA_FLOAT<class_Mesh_constant_ARRAY_CUSTOM_RGBA_FLOAT>`{.interpreted-text
role="ref"}.

:::: {#class_SurfaceTool_constant_CUSTOM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **CUSTOM_MAX** = `8`

Used to indicate a disabled custom channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_SurfaceTool_SkinWeightCount}
::: rst-class
classref-enumeration
:::
::::

enum **SkinWeightCount**:
`🔗<enum_SurfaceTool_SkinWeightCount>`{.interpreted-text role="ref"}

:::: {#class_SurfaceTool_constant_SKIN_4_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`SkinWeightCount<enum_SurfaceTool_SkinWeightCount>`{.interpreted-text
role="ref"} **SKIN_4_WEIGHTS** = `0`

Each individual vertex can be influenced by only 4 bone weights.

:::: {#class_SurfaceTool_constant_SKIN_8_WEIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`SkinWeightCount<enum_SurfaceTool_SkinWeightCount>`{.interpreted-text
role="ref"} **SKIN_8_WEIGHTS** = `1`

Each individual vertex can be influenced by up to 8 bone weights.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SurfaceTool_method_add_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_index**(index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SurfaceTool_method_add_index>`{.interpreted-text role="ref"}

Adds a vertex to index array if you are using indexed vertices. Does not
need to be called before adding vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_add_triangle_fan}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_triangle_fan**(vertices:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, uvs:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} = PackedVector2Array(), colors:
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
= PackedColorArray(), uv2s:
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} = PackedVector2Array(), normals:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} = PackedVector3Array(), tangents:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\] =
\[\]) `🔗<class_SurfaceTool_method_add_triangle_fan>`{.interpreted-text
role="ref"}

Inserts a triangle fan made of array data into
`Mesh<class_Mesh>`{.interpreted-text role="ref"} being constructed.

Requires the primitive type be set to
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_add_vertex}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_vertex**(vertex: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_SurfaceTool_method_add_vertex>`{.interpreted-text
role="ref"}

Specifies the position of current vertex. Should be called after
specifying other vertex properties (e.g. Color, UV).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_append_from}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_from**(existing: `Mesh<class_Mesh>`{.interpreted-text
role="ref"}, surface: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_SurfaceTool_method_append_from>`{.interpreted-text role="ref"}

Append vertices from a given `Mesh<class_Mesh>`{.interpreted-text
role="ref"} surface onto the current vertex array with specified
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_begin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**begin**(primitive:
`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"})
`🔗<class_SurfaceTool_method_begin>`{.interpreted-text role="ref"}

Called before adding any vertices. Takes the primitive type as an
argument (e.g.
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_SurfaceTool_method_clear>`{.interpreted-text role="ref"}

Clear all information passed into the surface tool so far.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_commit}
::: rst-class
classref-method
:::
::::

`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
**commit**(existing: `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"} = null, flags: `int<class_int>`{.interpreted-text
role="ref"} = 0) `🔗<class_SurfaceTool_method_commit>`{.interpreted-text
role="ref"}

Returns a constructed `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"} from current information passed in. If an existing
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} is passed in
as an argument, will add an extra surface to the existing
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}.

The `flags` argument can be the bitwise OR of
`Mesh.ARRAY_FLAG_USE_DYNAMIC_UPDATE<class_Mesh_constant_ARRAY_FLAG_USE_DYNAMIC_UPDATE>`{.interpreted-text
role="ref"},
`Mesh.ARRAY_FLAG_USE_8_BONE_WEIGHTS<class_Mesh_constant_ARRAY_FLAG_USE_8_BONE_WEIGHTS>`{.interpreted-text
role="ref"}, or
`Mesh.ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY<class_Mesh_constant_ARRAY_FLAG_USES_EMPTY_VERTEX_ARRAY>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_commit_to_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**commit_to_arrays**()
`🔗<class_SurfaceTool_method_commit_to_arrays>`{.interpreted-text
role="ref"}

Commits the data to the same format used by
`ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"},
`ImporterMesh.add_surface()<class_ImporterMesh_method_add_surface>`{.interpreted-text
role="ref"}, and
`create_from_arrays()<class_SurfaceTool_method_create_from_arrays>`{.interpreted-text
role="ref"}. This way you can further process the mesh data using the
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} or
`ImporterMesh<class_ImporterMesh>`{.interpreted-text role="ref"} APIs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_create_from}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_from**(existing: `Mesh<class_Mesh>`{.interpreted-text
role="ref"}, surface: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SurfaceTool_method_create_from>`{.interpreted-text role="ref"}

Creates a vertex array from an existing
`Mesh<class_Mesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_create_from_arrays}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_from_arrays**(arrays: `Array<class_Array>`{.interpreted-text
role="ref"}, primitive_type:
`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"} =
3) `🔗<class_SurfaceTool_method_create_from_arrays>`{.interpreted-text
role="ref"}

Creates this SurfaceTool from existing vertex arrays such as returned by
`commit_to_arrays()<class_SurfaceTool_method_commit_to_arrays>`{.interpreted-text
role="ref"},
`Mesh.surface_get_arrays()<class_Mesh_method_surface_get_arrays>`{.interpreted-text
role="ref"},
`Mesh.surface_get_blend_shape_arrays()<class_Mesh_method_surface_get_blend_shape_arrays>`{.interpreted-text
role="ref"},
`ImporterMesh.get_surface_arrays()<class_ImporterMesh_method_get_surface_arrays>`{.interpreted-text
role="ref"}, and
`ImporterMesh.get_surface_blend_shape_arrays()<class_ImporterMesh_method_get_surface_blend_shape_arrays>`{.interpreted-text
role="ref"}. `primitive_type` controls the type of mesh data, defaulting
to
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_create_from_blend_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_from_blend_shape**(existing:
`Mesh<class_Mesh>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"}, blend_shape:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_SurfaceTool_method_create_from_blend_shape>`{.interpreted-text
role="ref"}

Creates a vertex array from the specified blend shape of an existing
`Mesh<class_Mesh>`{.interpreted-text role="ref"}. This can be used to
extract a specific pose from a blend shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_deindex}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **deindex**()
`🔗<class_SurfaceTool_method_deindex>`{.interpreted-text role="ref"}

Removes the index array by expanding the vertex array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_generate_lod}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**generate_lod**(nd_threshold: `float<class_float>`{.interpreted-text
role="ref"}, target_index_count: `int<class_int>`{.interpreted-text
role="ref"} = 3)
`🔗<class_SurfaceTool_method_generate_lod>`{.interpreted-text
role="ref"}

**Deprecated:** This method is unused internally, as it does not
preserve normals or UVs. Consider using
`ImporterMesh.generate_lods()<class_ImporterMesh_method_generate_lods>`{.interpreted-text
role="ref"} instead.

Generates an LOD for a given `nd_threshold` in linear units (square root
of quadric error metric), using at most `target_index_count` indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_generate_normals}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**generate_normals**(flip: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_SurfaceTool_method_generate_normals>`{.interpreted-text
role="ref"}

Generates normals from vertices so you do not have to do it manually. If
`flip` is `true`, the resulting normals will be inverted.
`generate_normals()<class_SurfaceTool_method_generate_normals>`{.interpreted-text
role="ref"} should be called *after* generating geometry and *before*
committing the mesh using
`commit()<class_SurfaceTool_method_commit>`{.interpreted-text
role="ref"} or
`commit_to_arrays()<class_SurfaceTool_method_commit_to_arrays>`{.interpreted-text
role="ref"}. For correct display of normal-mapped surfaces, you will
also have to generate tangents using
`generate_tangents()<class_SurfaceTool_method_generate_tangents>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`generate_normals()<class_SurfaceTool_method_generate_normals>`{.interpreted-text
role="ref"} only works if the primitive type is set to
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`generate_normals()<class_SurfaceTool_method_generate_normals>`{.interpreted-text
role="ref"} takes smooth groups into account. To generate smooth
normals, set the smooth group to a value greater than or equal to `0`
using
`set_smooth_group()<class_SurfaceTool_method_set_smooth_group>`{.interpreted-text
role="ref"} or leave the smooth group at the default of `0`. To generate
flat normals, set the smooth group to `-1` using
`set_smooth_group()<class_SurfaceTool_method_set_smooth_group>`{.interpreted-text
role="ref"} prior to adding vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_generate_tangents}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**generate_tangents**()
`🔗<class_SurfaceTool_method_generate_tangents>`{.interpreted-text
role="ref"}

Generates a tangent vector for each vertex. Requires that each vertex
already has UVs and normals set (see
`generate_normals()<class_SurfaceTool_method_generate_normals>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_get_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **get_aabb**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_SurfaceTool_method_get_aabb>`{.interpreted-text
role="ref"}

Returns the axis-aligned bounding box of the vertex positions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_get_custom_format}
::: rst-class
classref-method
:::
::::

`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"} **get_custom_format**(channel_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SurfaceTool_method_get_custom_format>`{.interpreted-text
role="ref"}

Returns the format for custom `channel_index` (currently up to 4).
Returns
`CUSTOM_MAX<class_SurfaceTool_constant_CUSTOM_MAX>`{.interpreted-text
role="ref"} if this custom channel is unused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_get_primitive_type}
::: rst-class
classref-method
:::
::::

`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"}
**get_primitive_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SurfaceTool_method_get_primitive_type>`{.interpreted-text
role="ref"}

Returns the type of mesh geometry, such as
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_get_skin_weight_count}
::: rst-class
classref-method
:::
::::

`SkinWeightCount<enum_SurfaceTool_SkinWeightCount>`{.interpreted-text
role="ref"} **get_skin_weight_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SurfaceTool_method_get_skin_weight_count>`{.interpreted-text
role="ref"}

By default, returns
`SKIN_4_WEIGHTS<class_SurfaceTool_constant_SKIN_4_WEIGHTS>`{.interpreted-text
role="ref"} to indicate only 4 bone influences per vertex are used.

Returns
`SKIN_8_WEIGHTS<class_SurfaceTool_constant_SKIN_8_WEIGHTS>`{.interpreted-text
role="ref"} if up to 8 influences are used.

\*\*Note:\*\* This function returns an enum, not the exact number of
weights.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **index**()
`🔗<class_SurfaceTool_method_index>`{.interpreted-text role="ref"}

Shrinks the vertex array by creating an index array. This can improve
performance by avoiding vertex reuse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_optimize_indices_for_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**optimize_indices_for_cache**()
`🔗<class_SurfaceTool_method_optimize_indices_for_cache>`{.interpreted-text
role="ref"}

Optimizes triangle sorting for performance. Requires that
`get_primitive_type()<class_SurfaceTool_method_get_primitive_type>`{.interpreted-text
role="ref"} is
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_bones}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_bones**(bones:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}) `🔗<class_SurfaceTool_method_set_bones>`{.interpreted-text
role="ref"}

Specifies an array of bones to use for the *next* vertex. `bones` must
contain 4 integers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_color**(color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_SurfaceTool_method_set_color>`{.interpreted-text role="ref"}

Specifies a `Color<class_Color>`{.interpreted-text role="ref"} to use
for the *next* vertex. If every vertex needs to have this information
set and you fail to submit it for the first vertex, this information may
not be used at all.

\*\*Note:\*\* The material must have
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} enabled for the vertex color to be visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_custom}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom**(channel_index: `int<class_int>`{.interpreted-text
role="ref"}, custom_color: `Color<class_Color>`{.interpreted-text
role="ref"}) `🔗<class_SurfaceTool_method_set_custom>`{.interpreted-text
role="ref"}

Sets the custom value on this vertex for `channel_index`.

`set_custom_format()<class_SurfaceTool_method_set_custom_format>`{.interpreted-text
role="ref"} must be called first for this `channel_index`. Formats which
are not RGBA will ignore other color channels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_custom_format}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_format**(channel_index: `int<class_int>`{.interpreted-text
role="ref"}, format:
`CustomFormat<enum_SurfaceTool_CustomFormat>`{.interpreted-text
role="ref"})
`🔗<class_SurfaceTool_method_set_custom_format>`{.interpreted-text
role="ref"}

Sets the color format for this custom `channel_index`. Use
`CUSTOM_MAX<class_SurfaceTool_constant_CUSTOM_MAX>`{.interpreted-text
role="ref"} to disable.

Must be invoked after
`begin()<class_SurfaceTool_method_begin>`{.interpreted-text role="ref"}
and should be set before
`commit()<class_SurfaceTool_method_commit>`{.interpreted-text
role="ref"} or
`commit_to_arrays()<class_SurfaceTool_method_commit_to_arrays>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_material**(material: `Material<class_Material>`{.interpreted-text
role="ref"})
`🔗<class_SurfaceTool_method_set_material>`{.interpreted-text
role="ref"}

Sets `Material<class_Material>`{.interpreted-text role="ref"} to be used
by the `Mesh<class_Mesh>`{.interpreted-text role="ref"} you are
constructing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_normal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_normal**(normal: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_SurfaceTool_method_set_normal>`{.interpreted-text
role="ref"}

Specifies a normal to use for the *next* vertex. If every vertex needs
to have this information set and you fail to submit it for the first
vertex, this information may not be used at all.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_skin_weight_count}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_skin_weight_count**(count:
`SkinWeightCount<enum_SurfaceTool_SkinWeightCount>`{.interpreted-text
role="ref"})
`🔗<class_SurfaceTool_method_set_skin_weight_count>`{.interpreted-text
role="ref"}

Set to
`SKIN_8_WEIGHTS<class_SurfaceTool_constant_SKIN_8_WEIGHTS>`{.interpreted-text
role="ref"} to indicate that up to 8 bone influences per vertex may be
used.

By default, only 4 bone influences are used
(`SKIN_4_WEIGHTS<class_SurfaceTool_constant_SKIN_4_WEIGHTS>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* This function takes an enum, not the exact number of
weights.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_smooth_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_smooth_group**(index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SurfaceTool_method_set_smooth_group>`{.interpreted-text
role="ref"}

Specifies the smooth group to use for the *next* vertex. If this is
never called, all vertices will have the default smooth group of `0` and
will be smoothed with adjacent vertices of the same group. To produce a
mesh with flat normals, set the smooth group to `-1`.

\*\*Note:\*\* This function actually takes a `uint32_t`, so C# users
should use `uint32.MaxValue` instead of `-1` to produce a mesh with flat
normals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_tangent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tangent**(tangent: `Plane<class_Plane>`{.interpreted-text
role="ref"})
`🔗<class_SurfaceTool_method_set_tangent>`{.interpreted-text role="ref"}

Specifies a tangent to use for the *next* vertex. If every vertex needs
to have this information set and you fail to submit it for the first
vertex, this information may not be used at all.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_uv}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **set_uv**(uv:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_SurfaceTool_method_set_uv>`{.interpreted-text role="ref"}

Specifies a set of UV coordinates to use for the *next* vertex. If every
vertex needs to have this information set and you fail to submit it for
the first vertex, this information may not be used at all.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_uv2}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_uv2**(uv2: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_SurfaceTool_method_set_uv2>`{.interpreted-text role="ref"}

Specifies an optional second set of UV coordinates to use for the *next*
vertex. If every vertex needs to have this information set and you fail
to submit it for the first vertex, this information may not be used at
all.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SurfaceTool_method_set_weights}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_weights**(weights:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_SurfaceTool_method_set_weights>`{.interpreted-text role="ref"}

Specifies weight values to use for the *next* vertex. `weights` must
contain 4 values. If every vertex needs to have this information set and
you fail to submit it for the first vertex, this information may not be
used at all.
