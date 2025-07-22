github_url
:   hide

# MeshDataTool {#class_MeshDataTool}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Helper tool to access and edit `Mesh<class_Mesh>`{.interpreted-text
role="ref"} data.

::: rst-class
classref-introduction-group
:::

## Description

MeshDataTool provides access to individual vertices in a
`Mesh<class_Mesh>`{.interpreted-text role="ref"}. It allows users to
read and edit vertex data of meshes. It also creates an array of faces
and edges.

To use MeshDataTool, load a mesh with
`create_from_surface()<class_MeshDataTool_method_create_from_surface>`{.interpreted-text
role="ref"}. When you are finished editing the data commit the data to a
mesh with
`commit_to_surface()<class_MeshDataTool_method_commit_to_surface>`{.interpreted-text
role="ref"}.

Below is an example of how MeshDataTool may be used.

::::: tabs
::: code-tab
gdscript

var mesh = ArrayMesh.new()
mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES,
BoxMesh.new().get_mesh_arrays()) var mdt = MeshDataTool.new()
mdt.create_from_surface(mesh, 0) for i in range(mdt.get_vertex_count()):
var vertex = mdt.get_vertex(i) \# In this example we extend the mesh by
one unit, which results in separated faces as it is flat shaded. vertex
+= mdt.get_vertex_normal(i) \# Save your change. mdt.set_vertex(i,
vertex) mesh.clear_surfaces() mdt.commit_to_surface(mesh) var mi =
MeshInstance.new() mi.mesh = mesh add_child(mi)
:::

::: code-tab
csharp

var mesh = new ArrayMesh();
mesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles, new
BoxMesh().GetMeshArrays()); var mdt = new MeshDataTool();
mdt.CreateFromSurface(mesh, 0); for (var i = 0; i \<
mdt.GetVertexCount(); i++) { Vector3 vertex = mdt.GetVertex(i); // In
this example we extend the mesh by one unit, which results in separated
faces as it is flat shaded. vertex += mdt.GetVertexNormal(i); // Save
your change. mdt.SetVertex(i, vertex); } mesh.ClearSurfaces();
mdt.CommitToSurface(mesh); var mi = new MeshInstance(); mi.Mesh = mesh;
AddChild(mi);
:::
:::::

See also `ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"},
`ImmediateMesh<class_ImmediateMesh>`{.interpreted-text role="ref"} and
`SurfaceTool<class_SurfaceTool>`{.interpreted-text role="ref"} for
procedural geometry generation.

\*\*Note:\*\* Godot uses clockwise [winding
order](https://learnopengl.com/Advanced-OpenGL/Face-culling) for front
faces of triangle primitive modes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using the MeshDataTool <../tutorials/3d/procedural_geometry/meshdatatool>`{.interpreted-text
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

:::: {#class_MeshDataTool_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_MeshDataTool_method_clear>`{.interpreted-text role="ref"}

Clears all data currently in MeshDataTool.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_commit_to_surface}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**commit_to_surface**(mesh:
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"},
compression_flags: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_MeshDataTool_method_commit_to_surface>`{.interpreted-text
role="ref"}

Adds a new surface to specified `Mesh<class_Mesh>`{.interpreted-text
role="ref"} with edited data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_create_from_surface}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**create_from_surface**(mesh:
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}, surface:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_create_from_surface>`{.interpreted-text
role="ref"}

Uses specified surface of given `Mesh<class_Mesh>`{.interpreted-text
role="ref"} to populate data for MeshDataTool.

Requires `Mesh<class_Mesh>`{.interpreted-text role="ref"} with primitive
type
`Mesh.PRIMITIVE_TRIANGLES<class_Mesh_constant_PRIMITIVE_TRIANGLES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_edge_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_edge_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_edge_count>`{.interpreted-text
role="ref"}

Returns the number of edges in this `Mesh<class_Mesh>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_edge_faces}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_edge_faces**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_edge_faces>`{.interpreted-text
role="ref"}

Returns array of faces that touch given edge.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_edge_meta}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_edge_meta**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_edge_meta>`{.interpreted-text
role="ref"}

Returns meta information assigned to given edge.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_edge_vertex}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_edge_vertex**(idx:
`int<class_int>`{.interpreted-text role="ref"}, vertex:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_edge_vertex>`{.interpreted-text
role="ref"}

Returns the index of the specified `vertex` connected to the edge at
index `idx`.

`vertex` can only be `0` or `1`, as edges are composed of two vertices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_face_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_face_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_face_count>`{.interpreted-text
role="ref"}

Returns the number of faces in this `Mesh<class_Mesh>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_face_edge}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_face_edge**(idx:
`int<class_int>`{.interpreted-text role="ref"}, edge:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_face_edge>`{.interpreted-text
role="ref"}

Returns the edge associated with the face at index `idx`.

`edge` argument must be either `0`, `1`, or `2` because a face only has
three edges.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_face_meta}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_face_meta**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_face_meta>`{.interpreted-text
role="ref"}

Returns the metadata associated with the given face.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_face_normal}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_face_normal**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_face_normal>`{.interpreted-text
role="ref"}

Calculates and returns the face normal of the given face.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_face_vertex}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_face_vertex**(idx:
`int<class_int>`{.interpreted-text role="ref"}, vertex:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_face_vertex>`{.interpreted-text
role="ref"}

Returns the specified vertex index of the given face.

`vertex` must be either `0`, `1`, or `2` because faces contain three
vertices.

::::: tabs
::: code-tab
gdscript

var index = mesh_data_tool.get_face_vertex(0, 1) \# Gets the index of
the second vertex of the first face. var position =
mesh_data_tool.get_vertex(index) var normal =
mesh_data_tool.get_vertex_normal(index)
:::

::: code-tab
csharp

int index = meshDataTool.GetFaceVertex(0, 1); // Gets the index of the
second vertex of the first face. Vector3 position =
meshDataTool.GetVertex(index); Vector3 normal =
meshDataTool.GetVertexNormal(index);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_format}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_format**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_format>`{.interpreted-text role="ref"}

Returns the `Mesh<class_Mesh>`{.interpreted-text role="ref"}\'s format
as a combination of the
`ArrayFormat<enum_Mesh_ArrayFormat>`{.interpreted-text role="ref"}
flags. For example, a mesh containing both vertices and normals would
return a format of `3` because
`Mesh.ARRAY_FORMAT_VERTEX<class_Mesh_constant_ARRAY_FORMAT_VERTEX>`{.interpreted-text
role="ref"} is `1` and
`Mesh.ARRAY_FORMAT_NORMAL<class_Mesh_constant_ARRAY_FORMAT_NORMAL>`{.interpreted-text
role="ref"} is `2`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_material}
::: rst-class
classref-method
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**get_material**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_material>`{.interpreted-text
role="ref"}

Returns the material assigned to the
`Mesh<class_Mesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_vertex**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex>`{.interpreted-text role="ref"}

Returns the position of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_bones}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_vertex_bones**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_bones>`{.interpreted-text
role="ref"}

Returns the bones of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_vertex_color**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_color>`{.interpreted-text
role="ref"}

Returns the color of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_vertex_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_count>`{.interpreted-text
role="ref"}

Returns the total number of vertices in
`Mesh<class_Mesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_edges}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_vertex_edges**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_edges>`{.interpreted-text
role="ref"}

Returns an array of edges that share the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_faces}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_vertex_faces**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_faces>`{.interpreted-text
role="ref"}

Returns an array of faces that share the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_meta}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_vertex_meta**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_meta>`{.interpreted-text
role="ref"}

Returns the metadata associated with the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_normal}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_vertex_normal**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_normal>`{.interpreted-text
role="ref"}

Returns the normal of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_tangent}
::: rst-class
classref-method
:::
::::

`Plane<class_Plane>`{.interpreted-text role="ref"}
**get_vertex_tangent**(idx: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_tangent>`{.interpreted-text
role="ref"}

Returns the tangent of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_uv}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_vertex_uv**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_uv>`{.interpreted-text
role="ref"}

Returns the UV of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_uv2}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_vertex_uv2**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_uv2>`{.interpreted-text
role="ref"}

Returns the UV2 of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_get_vertex_weights}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **get_vertex_weights**(idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshDataTool_method_get_vertex_weights>`{.interpreted-text
role="ref"}

Returns bone weights of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_edge_meta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_edge_meta**(idx: `int<class_int>`{.interpreted-text role="ref"},
meta: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_set_edge_meta>`{.interpreted-text
role="ref"}

Sets the metadata of the given edge.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_face_meta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_face_meta**(idx: `int<class_int>`{.interpreted-text role="ref"},
meta: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_set_face_meta>`{.interpreted-text
role="ref"}

Sets the metadata of the given face.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_material**(material: `Material<class_Material>`{.interpreted-text
role="ref"})
`🔗<class_MeshDataTool_method_set_material>`{.interpreted-text
role="ref"}

Sets the material to be used by newly-constructed
`Mesh<class_Mesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex**(idx: `int<class_int>`{.interpreted-text role="ref"},
vertex: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_set_vertex>`{.interpreted-text role="ref"}

Sets the position of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_bones}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_bones**(idx: `int<class_int>`{.interpreted-text
role="ref"}, bones:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_bones>`{.interpreted-text
role="ref"}

Sets the bones of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_color**(idx: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_color>`{.interpreted-text
role="ref"}

Sets the color of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_meta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_meta**(idx: `int<class_int>`{.interpreted-text role="ref"},
meta: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_meta>`{.interpreted-text
role="ref"}

Sets the metadata associated with the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_normal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_normal**(idx: `int<class_int>`{.interpreted-text
role="ref"}, normal: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_normal>`{.interpreted-text
role="ref"}

Sets the normal of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_tangent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_tangent**(idx: `int<class_int>`{.interpreted-text
role="ref"}, tangent: `Plane<class_Plane>`{.interpreted-text
role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_tangent>`{.interpreted-text
role="ref"}

Sets the tangent of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_uv}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_uv**(idx: `int<class_int>`{.interpreted-text role="ref"},
uv: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_uv>`{.interpreted-text
role="ref"}

Sets the UV of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_uv2}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_uv2**(idx: `int<class_int>`{.interpreted-text role="ref"},
uv2: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_uv2>`{.interpreted-text
role="ref"}

Sets the UV2 of the given vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshDataTool_method_set_vertex_weights}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex_weights**(idx: `int<class_int>`{.interpreted-text
role="ref"}, weights:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_MeshDataTool_method_set_vertex_weights>`{.interpreted-text
role="ref"}

Sets the bone weights of the given vertex.
