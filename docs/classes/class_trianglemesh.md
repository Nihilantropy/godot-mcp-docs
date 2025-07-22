github_url
:   hide

# TriangleMesh {#class_TriangleMesh}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Triangle geometry for efficient, physicsless intersection queries.

::: rst-class
classref-introduction-group
:::

## Description

Creates a bounding volume hierarchy (BVH) tree structure around triangle
geometry.

The triangle BVH tree can be used for efficient intersection queries
without involving a physics engine.

For example, this can be used in editor tools to select objects with
complex shapes based on the mouse cursor position.

\*\*Performance:\*\* Creating the BVH tree for complex geometry is a
slow process and best done in a background thread.

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

:::: {#class_TriangleMesh_method_create_from_faces}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**create_from_faces**(faces:
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"})
`🔗<class_TriangleMesh_method_create_from_faces>`{.interpreted-text
role="ref"}

Creates the BVH tree from an array of faces. Each 3 vertices of the
input `faces` array represent one triangle (face).

Returns `true` if the tree is successfully built, `false` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TriangleMesh_method_get_faces}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_faces**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TriangleMesh_method_get_faces>`{.interpreted-text
role="ref"}

Returns a copy of the geometry faces. Each 3 vertices of the array
represent one triangle (face).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TriangleMesh_method_intersect_ray}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**intersect_ray**(begin: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, dir: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TriangleMesh_method_intersect_ray>`{.interpreted-text
role="ref"}

Tests for intersection with a ray starting at `begin` and facing `dir`
and extending toward infinity.

If an intersection with a triangle happens, returns a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following fields:

`position`: The position on the intersected triangle.

`normal`: The normal of the intersected triangle.

`face_index`: The index of the intersected triangle.

Returns an empty `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} if no intersection happens.

See also
`intersect_segment()<class_TriangleMesh_method_intersect_segment>`{.interpreted-text
role="ref"}, which is similar but uses a finite-length segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TriangleMesh_method_intersect_segment}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**intersect_segment**(begin: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, end: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TriangleMesh_method_intersect_segment>`{.interpreted-text
role="ref"}

Tests for intersection with a segment going from `begin` to `end`.

If an intersection with a triangle happens returns a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following fields:

`position`: The position on the intersected triangle.

`normal`: The normal of the intersected triangle.

`face_index`: The index of the intersected triangle.

Returns an empty `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} if no intersection happens.

See also
`intersect_ray()<class_TriangleMesh_method_intersect_ray>`{.interpreted-text
role="ref"}, which is similar but uses an infinite-length ray.
