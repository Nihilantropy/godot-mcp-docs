github_url
:   hide

# NavigationMeshSourceGeometryData3D {#class_NavigationMeshSourceGeometryData3D}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Container for parsed source geometry data used in navigation mesh
baking.

::: rst-class
classref-introduction-group
:::

## Description

Container for parsed source geometry data used in navigation mesh
baking.

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

:::: {#class_NavigationMeshSourceGeometryData3D_method_add_faces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_faces**(faces:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, xform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_add_faces>`{.interpreted-text
role="ref"}

Adds an array of vertex positions to the geometry data for navigation
mesh baking to form triangulated faces. For each face the array must
have three vertex positions in clockwise winding order. Since
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
resources have no transform, all vertex positions need to be offset by
the node\'s transform using `xform`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_add_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_mesh**(mesh: `Mesh<class_Mesh>`{.interpreted-text role="ref"},
xform: `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_add_mesh>`{.interpreted-text
role="ref"}

Adds the geometry data of a `Mesh<class_Mesh>`{.interpreted-text
role="ref"} resource to the navigation mesh baking data. The mesh must
have valid triangulated mesh data to be considered. Since
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
resources have no transform, all vertex positions need to be offset by
the node\'s transform using `xform`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_add_mesh_array}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_mesh_array**(mesh_array: `Array<class_Array>`{.interpreted-text
role="ref"}, xform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_add_mesh_array>`{.interpreted-text
role="ref"}

Adds an `Array<class_Array>`{.interpreted-text role="ref"} the size of
`Mesh.ARRAY_MAX<class_Mesh_constant_ARRAY_MAX>`{.interpreted-text
role="ref"} and with vertices at index
`Mesh.ARRAY_VERTEX<class_Mesh_constant_ARRAY_VERTEX>`{.interpreted-text
role="ref"} and indices at index
`Mesh.ARRAY_INDEX<class_Mesh_constant_ARRAY_INDEX>`{.interpreted-text
role="ref"} to the navigation mesh baking data. The array must have
valid triangulated mesh data to be considered. Since
`NavigationMesh<class_NavigationMesh>`{.interpreted-text role="ref"}
resources have no transform, all vertex positions need to be offset by
the node\'s transform using `xform`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_projected_obstruction**(vertices:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, elevation: `float<class_float>`{.interpreted-text
role="ref"}, height: `float<class_float>`{.interpreted-text role="ref"},
carve: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_add_projected_obstruction>`{.interpreted-text
role="ref"}

Adds a projected obstruction shape to the source geometry. The
`vertices` are considered projected on an xz-axes plane, placed at the
global y-axis `elevation` and extruded by `height`. If `carve` is `true`
the carved shape will not be affected by additional offsets (e.g. agent
radius) of the navigation mesh baking process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_append_arrays}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_arrays**(vertices:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, indices:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_append_arrays>`{.interpreted-text
role="ref"}

Appends arrays of `vertices` and `indices` at the end of the existing
arrays. Adds the existing index as an offset to the appended indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_NavigationMeshSourceGeometryData3D_method_clear>`{.interpreted-text
role="ref"}

Clears the internal data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_projected_obstructions**()
`🔗<class_NavigationMeshSourceGeometryData3D_method_clear_projected_obstructions>`{.interpreted-text
role="ref"}

Clears all projected obstructions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_get_bounds}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **get_bounds**()
`🔗<class_NavigationMeshSourceGeometryData3D_method_get_bounds>`{.interpreted-text
role="ref"}

Returns an axis-aligned bounding box that covers all the stored geometry
data. The bounds are calculated when calling this function with the
result cached until further geometry changes are made.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_get_indices}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_indices**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMeshSourceGeometryData3D_method_get_indices>`{.interpreted-text
role="ref"}

Returns the parsed source geometry data indices array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_projected_obstructions**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMeshSourceGeometryData3D_method_get_projected_obstructions>`{.interpreted-text
role="ref"}

Returns the projected obstructions as an
`Array<class_Array>`{.interpreted-text role="ref"} of dictionaries. Each
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} contains
the following entries:

- `vertices` - A
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} that defines the outline points of the projected shape.
- `elevation` - A `float<class_float>`{.interpreted-text role="ref"}
  that defines the projected shape placement on the y-axis.
- `height` - A `float<class_float>`{.interpreted-text role="ref"} that
  defines how much the projected shape is extruded along the y-axis.
- `carve` - A `bool<class_bool>`{.interpreted-text role="ref"} that
  defines how the obstacle affects the navigation mesh baking. If `true`
  the projected shape will not be affected by addition offsets, e.g.
  agent radius.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_get_vertices}
::: rst-class
classref-method
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **get_vertices**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_NavigationMeshSourceGeometryData3D_method_get_vertices>`{.interpreted-text
role="ref"}

Returns the parsed source geometry data vertices array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_has_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_data**()
`🔗<class_NavigationMeshSourceGeometryData3D_method_has_data>`{.interpreted-text
role="ref"}

Returns `true` when parsed source geometry data exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_merge}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**merge**(other_geometry:
`NavigationMeshSourceGeometryData3D<class_NavigationMeshSourceGeometryData3D>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_merge>`{.interpreted-text
role="ref"}

Adds the geometry data of another **NavigationMeshSourceGeometryData3D**
to the navigation mesh baking data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_set_indices}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_indices**(indices:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_set_indices>`{.interpreted-text
role="ref"}

Sets the parsed source geometry data indices. The indices need to be
matched with appropriated vertices.

\*\*Warning:\*\* Inappropriate data can crash the baking process of the
involved third-party libraries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_projected_obstructions**(projected_obstructions:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_set_projected_obstructions>`{.interpreted-text
role="ref"}

Sets the projected obstructions with an Array of Dictionaries with the
following key value pairs:

:::: tabs
::: code-tab
gdscript

\"vertices\" : PackedFloat32Array \"elevation\" : float \"height\" :
float \"carve\" : bool
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_NavigationMeshSourceGeometryData3D_method_set_vertices}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertices**(vertices:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_NavigationMeshSourceGeometryData3D_method_set_vertices>`{.interpreted-text
role="ref"}

Sets the parsed source geometry data vertices. The vertices need to be
matched with appropriated indices.

\*\*Warning:\*\* Inappropriate data can crash the baking process of the
involved third-party libraries.
