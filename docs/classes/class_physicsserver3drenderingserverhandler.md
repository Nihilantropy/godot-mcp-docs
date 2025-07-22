github_url
:   hide

# PhysicsServer3DRenderingServerHandler {#class_PhysicsServer3DRenderingServerHandler}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A class used to provide
`PhysicsServer3DExtension._soft_body_update_rendering_server()<class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server>`{.interpreted-text
role="ref"} with a rendering handler for soft bodies.

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

:::: {#class_PhysicsServer3DRenderingServerHandler_private_method__set_aabb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_aabb**(aabb: `AABB<class_AABB>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DRenderingServerHandler_private_method__set_aabb>`{.interpreted-text
role="ref"}

Called by the `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} to set the bounding box for the
`SoftBody3D<class_SoftBody3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3DRenderingServerHandler_private_method__set_normal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_normal**(vertex_id: `int<class_int>`{.interpreted-text
role="ref"}, normal: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DRenderingServerHandler_private_method__set_normal>`{.interpreted-text
role="ref"}

Called by the `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} to set the normal for the
`SoftBody3D<class_SoftBody3D>`{.interpreted-text role="ref"} vertex at
the index specified by `vertex_id`.

\*\*Note:\*\* The `normal` parameter used to be of type `const void*`
prior to Godot 4.2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3DRenderingServerHandler_private_method__set_vertex}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_vertex**(vertex_id: `int<class_int>`{.interpreted-text
role="ref"}, vertex: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DRenderingServerHandler_private_method__set_vertex>`{.interpreted-text
role="ref"}

Called by the `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} to set the position for the
`SoftBody3D<class_SoftBody3D>`{.interpreted-text role="ref"} vertex at
the index specified by `vertex_id`.

\*\*Note:\*\* The `vertex` parameter used to be of type `const void*`
prior to Godot 4.2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3DRenderingServerHandler_method_set_aabb}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_aabb**(aabb: `AABB<class_AABB>`{.interpreted-text role="ref"})
`🔗<class_PhysicsServer3DRenderingServerHandler_method_set_aabb>`{.interpreted-text
role="ref"}

Sets the bounding box for the
`SoftBody3D<class_SoftBody3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3DRenderingServerHandler_method_set_normal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_normal**(vertex_id: `int<class_int>`{.interpreted-text
role="ref"}, normal: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3DRenderingServerHandler_method_set_normal>`{.interpreted-text
role="ref"}

Sets the normal for the `SoftBody3D<class_SoftBody3D>`{.interpreted-text
role="ref"} vertex at the index specified by `vertex_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer3DRenderingServerHandler_method_set_vertex}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_vertex**(vertex_id: `int<class_int>`{.interpreted-text
role="ref"}, vertex: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_PhysicsServer3DRenderingServerHandler_method_set_vertex>`{.interpreted-text
role="ref"}

Sets the position for the
`SoftBody3D<class_SoftBody3D>`{.interpreted-text role="ref"} vertex at
the index specified by `vertex_id`.
