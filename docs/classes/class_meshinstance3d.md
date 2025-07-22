github_url
:   hide

# MeshInstance3D {#class_MeshInstance3D}

**Inherits:**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `SoftBody3D<class_SoftBody3D>`{.interpreted-text
role="ref"}

Node that instances meshes into a scenario.

::: rst-class
classref-introduction-group
:::

## Description

MeshInstance3D is a node that takes a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resource and adds it to
the current scenario by creating an instance of it. This is the class
most often used to render 3D geometry and can be used to instance a
single `Mesh<class_Mesh>`{.interpreted-text role="ref"} in many places.
This allows reusing geometry, which can save on resources. When a
`Mesh<class_Mesh>`{.interpreted-text role="ref"} has to be instantiated
more than thousands of times at close proximity, consider using a
`MultiMesh<class_MultiMesh>`{.interpreted-text role="ref"} in a
`MultiMeshInstance3D<class_MultiMeshInstance3D>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [3D Material Testers
  Demo](https://godotengine.org/asset-library/asset/2742)
- [3D Kinematic Character
  Demo](https://godotengine.org/asset-library/asset/2739)
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
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

:::: {#class_MeshInstance3D_property_mesh}
::: rst-class
classref-property
:::
::::

`Mesh<class_Mesh>`{.interpreted-text role="ref"} **mesh**
`🔗<class_MeshInstance3D_property_mesh>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh**(value: `Mesh<class_Mesh>`{.interpreted-text role="ref"})
- `Mesh<class_Mesh>`{.interpreted-text role="ref"} **get_mesh**()

The `Mesh<class_Mesh>`{.interpreted-text role="ref"} resource for the
instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_property_skeleton}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **skeleton** =
`NodePath("..")`
`🔗<class_MeshInstance3D_property_skeleton>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skeleton_path**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_skeleton_path**()

`NodePath<class_NodePath>`{.interpreted-text role="ref"} to the
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} associated
with the instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_property_skin}
::: rst-class
classref-property
:::
::::

`Skin<class_Skin>`{.interpreted-text role="ref"} **skin**
`🔗<class_MeshInstance3D_property_skin>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_skin**(value: `Skin<class_Skin>`{.interpreted-text role="ref"})
- `Skin<class_Skin>`{.interpreted-text role="ref"} **get_skin**()

The `Skin<class_Skin>`{.interpreted-text role="ref"} to be used by this
instance.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MeshInstance3D_method_bake_mesh_from_current_blend_shape_mix}
::: rst-class
classref-method
:::
::::

`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
**bake_mesh_from_current_blend_shape_mix**(existing:
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} = null)
`🔗<class_MeshInstance3D_method_bake_mesh_from_current_blend_shape_mix>`{.interpreted-text
role="ref"}

Takes a snapshot from the current
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} with all
blend shapes applied according to their current weights and bakes it to
the provided `existing` mesh. If no `existing` mesh is provided a new
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} is created,
baked and returned. Mesh surface materials are not copied.

\*\*Performance:\*\* `Mesh<class_Mesh>`{.interpreted-text role="ref"}
data needs to be received from the GPU, stalling the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
in the process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_bake_mesh_from_current_skeleton_pose}
::: rst-class
classref-method
:::
::::

`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"}
**bake_mesh_from_current_skeleton_pose**(existing:
`ArrayMesh<class_ArrayMesh>`{.interpreted-text role="ref"} = null)
`🔗<class_MeshInstance3D_method_bake_mesh_from_current_skeleton_pose>`{.interpreted-text
role="ref"}

Takes a snapshot of the current animated skeleton pose of the skinned
mesh and bakes it to the provided `existing` mesh. If no `existing` mesh
is provided a new `ArrayMesh<class_ArrayMesh>`{.interpreted-text
role="ref"} is created, baked, and returned. Requires a skeleton with a
registered skin to work. Blendshapes are ignored. Mesh surface materials
are not copied.

\*\*Performance:\*\* `Mesh<class_Mesh>`{.interpreted-text role="ref"}
data needs to be retrieved from the GPU, stalling the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
in the process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_create_convex_collision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_convex_collision**(clean: `bool<class_bool>`{.interpreted-text
role="ref"} = true, simplify: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_MeshInstance3D_method_create_convex_collision>`{.interpreted-text
role="ref"}

This helper creates a
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} child
node with a
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"} collision shape calculated from the mesh geometry. It\'s
mainly used for testing.

If `clean` is `true` (default), duplicate and interior vertices are
removed automatically. You can set it to `false` to make the process
faster if not needed.

If `simplify` is `true`, the geometry can be further simplified to
reduce the number of vertices. Disabled by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_create_debug_tangents}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_debug_tangents**()
`🔗<class_MeshInstance3D_method_create_debug_tangents>`{.interpreted-text
role="ref"}

This helper creates a **MeshInstance3D** child node with gizmos at every
vertex calculated from the mesh geometry. It\'s mainly used for testing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_create_multiple_convex_collisions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_multiple_convex_collisions**(settings:
`MeshConvexDecompositionSettings<class_MeshConvexDecompositionSettings>`{.interpreted-text
role="ref"} = null)
`🔗<class_MeshInstance3D_method_create_multiple_convex_collisions>`{.interpreted-text
role="ref"}

This helper creates a
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} child
node with multiple
`ConvexPolygonShape3D<class_ConvexPolygonShape3D>`{.interpreted-text
role="ref"} collision shapes calculated from the mesh geometry via
convex decomposition. The convex decomposition operation can be
controlled with parameters from the optional `settings`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_create_trimesh_collision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_trimesh_collision**()
`🔗<class_MeshInstance3D_method_create_trimesh_collision>`{.interpreted-text
role="ref"}

This helper creates a
`StaticBody3D<class_StaticBody3D>`{.interpreted-text role="ref"} child
node with a
`ConcavePolygonShape3D<class_ConcavePolygonShape3D>`{.interpreted-text
role="ref"} collision shape calculated from the mesh geometry. It\'s
mainly used for testing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_find_blend_shape_by_name}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**find_blend_shape_by_name**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_MeshInstance3D_method_find_blend_shape_by_name>`{.interpreted-text
role="ref"}

Returns the index of the blend shape with the given `name`. Returns `-1`
if no blend shape with this name exists, including when
`mesh<class_MeshInstance3D_property_mesh>`{.interpreted-text role="ref"}
is `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_get_active_material}
::: rst-class
classref-method
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**get_active_material**(surface: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshInstance3D_method_get_active_material>`{.interpreted-text
role="ref"}

Returns the `Material<class_Material>`{.interpreted-text role="ref"}
that will be used by the `Mesh<class_Mesh>`{.interpreted-text
role="ref"} when drawing. This can return the
`GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>`{.interpreted-text
role="ref"}, the surface override
`Material<class_Material>`{.interpreted-text role="ref"} defined in this
**MeshInstance3D**, or the surface
`Material<class_Material>`{.interpreted-text role="ref"} defined in the
`mesh<class_MeshInstance3D_property_mesh>`{.interpreted-text
role="ref"}. For example, if
`GeometryInstance3D.material_override<class_GeometryInstance3D_property_material_override>`{.interpreted-text
role="ref"} is used, all surfaces will return the override material.

Returns `null` if no material is active, including when
`mesh<class_MeshInstance3D_property_mesh>`{.interpreted-text role="ref"}
is `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_get_blend_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_blend_shape_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshInstance3D_method_get_blend_shape_count>`{.interpreted-text
role="ref"}

Returns the number of blend shapes available. Produces an error if
`mesh<class_MeshInstance3D_property_mesh>`{.interpreted-text role="ref"}
is `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_get_blend_shape_value}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_blend_shape_value**(blend_shape_idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshInstance3D_method_get_blend_shape_value>`{.interpreted-text
role="ref"}

Returns the value of the blend shape at the given `blend_shape_idx`.
Returns `0.0` and produces an error if
`mesh<class_MeshInstance3D_property_mesh>`{.interpreted-text role="ref"}
is `null` or doesn\'t have a blend shape at that index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_get_skin_reference}
::: rst-class
classref-method
:::
::::

`SkinReference<class_SkinReference>`{.interpreted-text role="ref"}
**get_skin_reference**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshInstance3D_method_get_skin_reference>`{.interpreted-text
role="ref"}

Returns the internal
`SkinReference<class_SkinReference>`{.interpreted-text role="ref"}
containing the skeleton\'s `RID<class_RID>`{.interpreted-text
role="ref"} attached to this RID. See also
`Resource.get_rid()<class_Resource_method_get_rid>`{.interpreted-text
role="ref"},
`SkinReference.get_skeleton()<class_SkinReference_method_get_skeleton>`{.interpreted-text
role="ref"}, and
`RenderingServer.instance_attach_skeleton()<class_RenderingServer_method_instance_attach_skeleton>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_get_surface_override_material}
::: rst-class
classref-method
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**get_surface_override_material**(surface:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshInstance3D_method_get_surface_override_material>`{.interpreted-text
role="ref"}

Returns the override `Material<class_Material>`{.interpreted-text
role="ref"} for the specified `surface` of the
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resource. See also
`get_surface_override_material_count()<class_MeshInstance3D_method_get_surface_override_material_count>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This returns the
`Material<class_Material>`{.interpreted-text role="ref"} associated to
the **MeshInstance3D**\'s Surface Material Override properties, not the
material within the `Mesh<class_Mesh>`{.interpreted-text role="ref"}
resource. To get the material within the
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resource, use
`Mesh.surface_get_material()<class_Mesh_method_surface_get_material>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_get_surface_override_material_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_surface_override_material_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MeshInstance3D_method_get_surface_override_material_count>`{.interpreted-text
role="ref"}

Returns the number of surface override materials. This is equivalent to
`Mesh.get_surface_count()<class_Mesh_method_get_surface_count>`{.interpreted-text
role="ref"}. See also
`get_surface_override_material()<class_MeshInstance3D_method_get_surface_override_material>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_set_blend_shape_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_blend_shape_value**(blend_shape_idx:
`int<class_int>`{.interpreted-text role="ref"}, value:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_MeshInstance3D_method_set_blend_shape_value>`{.interpreted-text
role="ref"}

Sets the value of the blend shape at `blend_shape_idx` to `value`.
Produces an error if
`mesh<class_MeshInstance3D_property_mesh>`{.interpreted-text role="ref"}
is `null` or doesn\'t have a blend shape at that index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MeshInstance3D_method_set_surface_override_material}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_surface_override_material**(surface:
`int<class_int>`{.interpreted-text role="ref"}, material:
`Material<class_Material>`{.interpreted-text role="ref"})
`🔗<class_MeshInstance3D_method_set_surface_override_material>`{.interpreted-text
role="ref"}

Sets the override `material` for the specified `surface` of the
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resource. This material
is associated with this **MeshInstance3D** rather than with
`mesh<class_MeshInstance3D_property_mesh>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This assigns the
`Material<class_Material>`{.interpreted-text role="ref"} associated to
the **MeshInstance3D**\'s Surface Material Override properties, not the
material within the `Mesh<class_Mesh>`{.interpreted-text role="ref"}
resource. To set the material within the
`Mesh<class_Mesh>`{.interpreted-text role="ref"} resource, use
`Mesh.surface_set_material()<class_Mesh_method_surface_set_material>`{.interpreted-text
role="ref"} instead.
