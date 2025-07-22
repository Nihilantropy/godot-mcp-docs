github_url
:   hide

# PrimitiveMesh {#class_PrimitiveMesh}

**Inherits:** `Mesh<class_Mesh>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `BoxMesh<class_BoxMesh>`{.interpreted-text
role="ref"}, `CapsuleMesh<class_CapsuleMesh>`{.interpreted-text
role="ref"}, `CylinderMesh<class_CylinderMesh>`{.interpreted-text
role="ref"}, `PlaneMesh<class_PlaneMesh>`{.interpreted-text role="ref"},
`PointMesh<class_PointMesh>`{.interpreted-text role="ref"},
`PrismMesh<class_PrismMesh>`{.interpreted-text role="ref"},
`RibbonTrailMesh<class_RibbonTrailMesh>`{.interpreted-text role="ref"},
`SphereMesh<class_SphereMesh>`{.interpreted-text role="ref"},
`TextMesh<class_TextMesh>`{.interpreted-text role="ref"},
`TorusMesh<class_TorusMesh>`{.interpreted-text role="ref"},
`TubeTrailMesh<class_TubeTrailMesh>`{.interpreted-text role="ref"}

Base class for all primitive meshes. Handles applying a
`Material<class_Material>`{.interpreted-text role="ref"} to a primitive
mesh.

::: rst-class
classref-introduction-group
:::

## Description

Base class for all primitive meshes. Handles applying a
`Material<class_Material>`{.interpreted-text role="ref"} to a primitive
mesh. Examples include `BoxMesh<class_BoxMesh>`{.interpreted-text
role="ref"}, `CapsuleMesh<class_CapsuleMesh>`{.interpreted-text
role="ref"}, `CylinderMesh<class_CylinderMesh>`{.interpreted-text
role="ref"}, `PlaneMesh<class_PlaneMesh>`{.interpreted-text role="ref"},
`PrismMesh<class_PrismMesh>`{.interpreted-text role="ref"}, and
`SphereMesh<class_SphereMesh>`{.interpreted-text role="ref"}.

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

:::: {#class_PrimitiveMesh_property_add_uv2}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **add_uv2** = `false`
`🔗<class_PrimitiveMesh_property_add_uv2>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_add_uv2**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_add_uv2**()

If set, generates UV2 UV coordinates applying a padding using the
`uv2_padding<class_PrimitiveMesh_property_uv2_padding>`{.interpreted-text
role="ref"} setting. UV2 is needed for lightmapping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrimitiveMesh_property_custom_aabb}
::: rst-class
classref-property
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **custom_aabb** =
`AABB(0, 0, 0, 0, 0, 0)`
`🔗<class_PrimitiveMesh_property_custom_aabb>`{.interpreted-text
role="ref"}

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

:::: {#class_PrimitiveMesh_property_flip_faces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flip_faces** =
`false` `🔗<class_PrimitiveMesh_property_flip_faces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flip_faces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_flip_faces**()

If `true`, the order of the vertices in each triangle is reversed,
resulting in the backside of the mesh being drawn.

This gives the same result as using
`BaseMaterial3D.CULL_FRONT<class_BaseMaterial3D_constant_CULL_FRONT>`{.interpreted-text
role="ref"} in
`BaseMaterial3D.cull_mode<class_BaseMaterial3D_property_cull_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrimitiveMesh_property_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"} **material**
`🔗<class_PrimitiveMesh_property_material>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_material**(value: `Material<class_Material>`{.interpreted-text
  role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_material**()

The current `Material<class_Material>`{.interpreted-text role="ref"} of
the primitive mesh.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrimitiveMesh_property_uv2_padding}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **uv2_padding** =
`2.0` `🔗<class_PrimitiveMesh_property_uv2_padding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_uv2_padding**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_uv2_padding**()

If `add_uv2<class_PrimitiveMesh_property_add_uv2>`{.interpreted-text
role="ref"} is set, specifies the padding in pixels applied along seams
of the mesh. Lower padding values allow making better use of the
lightmap texture (resulting in higher texel density), but may introduce
visible lightmap bleeding along edges.

If the size of the lightmap texture can\'t be determined when generating
the mesh, UV2 is calculated assuming a texture size of 1024x1024.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PrimitiveMesh_private_method__create_mesh_array}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**\_create_mesh_array**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PrimitiveMesh_private_method__create_mesh_array>`{.interpreted-text
role="ref"}

Override this method to customize how this primitive mesh should be
generated. Should return an `Array<class_Array>`{.interpreted-text
role="ref"} where each element is another Array of values required for
the mesh (see the `ArrayType<enum_Mesh_ArrayType>`{.interpreted-text
role="ref"} constants).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrimitiveMesh_method_get_mesh_arrays}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **get_mesh_arrays**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PrimitiveMesh_method_get_mesh_arrays>`{.interpreted-text
role="ref"}

Returns the mesh arrays used to make up the surface of this primitive
mesh.

\*\*Example:\*\* Pass the result to
`ArrayMesh.add_surface_from_arrays()<class_ArrayMesh_method_add_surface_from_arrays>`{.interpreted-text
role="ref"} to create a new surface:

::::: tabs
::: code-tab
gdscript

var c = CylinderMesh.new() var arr_mesh = ArrayMesh.new()
arr_mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES,
c.get_mesh_arrays())
:::

::: code-tab
csharp

var c = new CylinderMesh(); var arrMesh = new ArrayMesh();
arrMesh.AddSurfaceFromArrays(Mesh.PrimitiveType.Triangles,
c.GetMeshArrays());
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PrimitiveMesh_method_request_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_update**()
`🔗<class_PrimitiveMesh_method_request_update>`{.interpreted-text
role="ref"}

Request an update of this primitive mesh based on its properties.
