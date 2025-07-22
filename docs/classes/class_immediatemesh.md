github_url
:   hide

# ImmediateMesh {#class_ImmediateMesh}

**Inherits:** `Mesh<class_Mesh>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Mesh optimized for creating geometry manually.

::: rst-class
classref-introduction-group
:::

## Description

A mesh type optimized for creating geometry manually, similar to OpenGL
1.x immediate mode.

Here\'s a sample on how to generate a triangular face:

::::: tabs
::: code-tab
gdscript

var mesh = ImmediateMesh.new()
mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)
mesh.surface_add_vertex(Vector3.LEFT)
mesh.surface_add_vertex(Vector3.FORWARD)
mesh.surface_add_vertex(Vector3.ZERO) mesh.surface_end()
:::

::: code-tab
csharp

var mesh = new ImmediateMesh();
mesh.SurfaceBegin(Mesh.PrimitiveType.Triangles);
mesh.SurfaceAddVertex(Vector3.Left);
mesh.SurfaceAddVertex(Vector3.Forward);
mesh.SurfaceAddVertex(Vector3.Zero); mesh.SurfaceEnd();
:::
:::::

\*\*Note:\*\* Generating complex geometries with **ImmediateMesh** is
highly inefficient. Instead, it is designed to generate simple geometry
that changes often.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using ImmediateMesh <../tutorials/3d/procedural_geometry/immediatemesh>`{.interpreted-text
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

:::: {#class_ImmediateMesh_method_clear_surfaces}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_surfaces**()
`🔗<class_ImmediateMesh_method_clear_surfaces>`{.interpreted-text
role="ref"}

Clear all surfaces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_add_vertex}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_add_vertex**(vertex:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_ImmediateMesh_method_surface_add_vertex>`{.interpreted-text
role="ref"}

Add a 3D vertex using the current attributes previously set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_add_vertex_2d}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_add_vertex_2d**(vertex:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_ImmediateMesh_method_surface_add_vertex_2d>`{.interpreted-text
role="ref"}

Add a 2D vertex using the current attributes previously set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_begin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_begin**(primitive:
`PrimitiveType<enum_Mesh_PrimitiveType>`{.interpreted-text role="ref"},
material: `Material<class_Material>`{.interpreted-text role="ref"} =
null) `🔗<class_ImmediateMesh_method_surface_begin>`{.interpreted-text
role="ref"}

Begin a new surface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_end}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_end**()
`🔗<class_ImmediateMesh_method_surface_end>`{.interpreted-text
role="ref"}

End and commit current surface. Note that surface being created will not
be visible until this function is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_set_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_set_color**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ImmediateMesh_method_surface_set_color>`{.interpreted-text
role="ref"}

Set the color attribute that will be pushed with the next vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_set_normal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_set_normal**(normal:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_ImmediateMesh_method_surface_set_normal>`{.interpreted-text
role="ref"}

Set the normal attribute that will be pushed with the next vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_set_tangent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_set_tangent**(tangent: `Plane<class_Plane>`{.interpreted-text
role="ref"})
`🔗<class_ImmediateMesh_method_surface_set_tangent>`{.interpreted-text
role="ref"}

Set the tangent attribute that will be pushed with the next vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_set_uv}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_set_uv**(uv: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_ImmediateMesh_method_surface_set_uv>`{.interpreted-text
role="ref"}

Set the UV attribute that will be pushed with the next vertex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ImmediateMesh_method_surface_set_uv2}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**surface_set_uv2**(uv2: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_ImmediateMesh_method_surface_set_uv2>`{.interpreted-text
role="ref"}

Set the UV2 attribute that will be pushed with the next vertex.
