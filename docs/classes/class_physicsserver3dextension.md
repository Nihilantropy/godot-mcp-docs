github_url
:   hide

# PhysicsServer3DExtension {#class_PhysicsServer3DExtension}

**Inherits:** `PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides virtual methods that can be overridden to create custom
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
implementations.

::: rst-class
classref-introduction-group
:::

## Description

This class extends
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}
by providing additional virtual methods that can be overridden. When
these methods are overridden, they will be called instead of the
internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
`PhysicsServer3D<class_PhysicsServer3D>`{.interpreted-text role="ref"}.

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

:::: {#class_PhysicsServer3DExtension_private_method__area_add_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_add_shape**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape: `RID<class_RID>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_add_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_attach_object_instance_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_attach_object_instance_id**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_attach_object_instance_id>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_clear_shapes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_clear_shapes**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_clear_shapes>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_area_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_collision_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_area_get_collision_layer**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_collision_layer>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_area_get_collision_mask**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_object_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_area_get_object_instance_id**(area:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_object_instance_id>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_param}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_area_get_param**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_shape}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_area_get_shape**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_area_get_shape_count**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_shape_count>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_shape_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_area_get_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_shape_transform>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_space}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_area_get_space**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_space>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_get_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_area_get_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_get_transform>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_remove_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_remove_shape**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_remove_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_area_monitor_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_area_monitor_callback**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_area_monitor_callback>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_collision_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_collision_layer**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_collision_layer>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_collision_mask**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_monitor_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_monitor_callback**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_monitor_callback>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_monitorable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_monitorable**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, monitorable: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_monitorable>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_param**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`AreaParameter<enum_PhysicsServer3D_AreaParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_ray_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_ray_pickable**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_ray_pickable>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_shape**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
shape: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_shape_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_shape_disabled**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_shape_disabled>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_shape_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_shape_transform>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_space**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, space: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_space>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__area_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__area_set_transform>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_add_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, excepted_body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_add_collision_exception>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_add_constant_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_constant_central_force**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_add_constant_central_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_add_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_add_constant_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_add_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_add_constant_torque>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_add_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape: `RID<class_RID>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_add_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_central_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_apply_central_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_central_impulse**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_apply_central_impulse>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_apply_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_apply_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_apply_impulse>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_apply_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_apply_torque>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_apply_torque_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_torque_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_apply_torque_impulse>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_attach_object_instance_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_attach_object_instance_id**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_attach_object_instance_id>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_clear_shapes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_clear_shapes**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_clear_shapes>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_body_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_collision_exceptions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**\_body_get_collision_exceptions**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_exceptions>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_collision_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_body_get_collision_layer**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_layer>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_body_get_collision_mask**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_collision_priority}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_body_get_collision_priority**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_collision_priority>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_constant_force}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**\_body_get_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_constant_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_constant_torque}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**\_body_get_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_constant_torque>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_contacts_reported_depth_threshold}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_body_get_contacts_reported_depth_threshold**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_contacts_reported_depth_threshold>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_direct_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectBodyState3D<class_PhysicsDirectBodyState3D>`{.interpreted-text
role="ref"} **\_body_get_direct_state**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_direct_state>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_max_contacts_reported}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_body_get_max_contacts_reported**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_max_contacts_reported>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_mode}
::: rst-class
classref-method
:::
::::

`BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text role="ref"}
**\_body_get_mode**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_mode>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_object_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_body_get_object_instance_id**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_object_instance_id>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_param}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_body_get_param**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_shape}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_body_get_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_shape_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_body_get_shape_count**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_shape_count>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_shape_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_body_get_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_shape_transform>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_space}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_body_get_space**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_space>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_state}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_body_get_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_state>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_get_user_flags}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_body_get_user_flags**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_get_user_flags>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_is_axis_locked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_body_is_axis_locked**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis:
`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_is_axis_locked>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_is_continuous_collision_detection_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_body_is_continuous_collision_detection_enabled**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_is_continuous_collision_detection_enabled>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_is_omitting_force_integration}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_body_is_omitting_force_integration**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_is_omitting_force_integration>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_remove_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_remove_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, excepted_body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_remove_collision_exception>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_remove_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_remove_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_remove_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_reset_mass_properties}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_reset_mass_properties**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_reset_mass_properties>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_axis_lock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_axis_lock**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis:
`BodyAxis<enum_PhysicsServer3D_BodyAxis>`{.interpreted-text role="ref"},
lock: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_axis_lock>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_axis_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_axis_velocity**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis_velocity: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_axis_velocity>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_collision_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_collision_layer**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_collision_layer>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_collision_mask**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, mask: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_collision_priority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_collision_priority**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, priority:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_collision_priority>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_constant_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_constant_torque>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_contacts_reported_depth_threshold}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_contacts_reported_depth_threshold**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, threshold:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_contacts_reported_depth_threshold>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_enable_continuous_collision_detection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_enable_continuous_collision_detection**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_enable_continuous_collision_detection>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_force_integration_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_force_integration_callback**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"}, userdata:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_force_integration_callback>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_max_contacts_reported}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_max_contacts_reported**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, amount:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_max_contacts_reported>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_mode**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, mode:
`BodyMode<enum_PhysicsServer3D_BodyMode>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_mode>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_omit_force_integration}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_omit_force_integration**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_omit_force_integration>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_param**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`BodyParameter<enum_PhysicsServer3D_BodyParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_ray_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_ray_pickable**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_ray_pickable>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
shape: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_shape>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_shape_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_shape_disabled**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_shape_disabled>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_shape_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_shape_transform>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_space**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, space: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_space>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_state>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_state_sync_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_state_sync_callback**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_state_sync_callback>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_set_user_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_user_flags**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, flags: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_set_user_flags>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__body_test_motion}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_body_test_motion**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, from: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, motion: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, margin: `float<class_float>`{.interpreted-text role="ref"},
max_collisions: `int<class_int>`{.interpreted-text role="ref"},
collide_separation_ray: `bool<class_bool>`{.interpreted-text
role="ref"}, recovery_as_collision: `bool<class_bool>`{.interpreted-text
role="ref"}, result: `PhysicsServer3DExtensionMotionResult*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__body_test_motion>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__box_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_box_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__box_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__capsule_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_capsule_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__capsule_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__concave_polygon_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_concave_polygon_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__concave_polygon_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__cone_twist_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_cone_twist_joint_get_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, param:
`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__cone_twist_joint_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__cone_twist_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_cone_twist_joint_set_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, param:
`ConeTwistJointParam<enum_PhysicsServer3D_ConeTwistJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__cone_twist_joint_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__convex_polygon_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_convex_polygon_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__convex_polygon_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__custom_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_custom_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__custom_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__cylinder_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_cylinder_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__cylinder_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__end_sync}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_end_sync**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__end_sync>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__finish}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_finish**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__finish>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__flush_queries}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_flush_queries**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__flush_queries>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__free_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__free_rid>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_generic_6dof_joint_get_flag**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, flag:
`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_flag>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_generic_6dof_joint_get_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, param:
`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_generic_6dof_joint_set_flag**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, flag:
`G6DOFJointAxisFlag<enum_PhysicsServer3D_G6DOFJointAxisFlag>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_flag>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_generic_6dof_joint_set_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, axis:
`Axis<enum_Vector3_Axis>`{.interpreted-text role="ref"}, param:
`G6DOFJointAxisParam<enum_PhysicsServer3D_G6DOFJointAxisParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__generic_6dof_joint_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__get_process_info}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_process_info**(process_info:
`ProcessInfo<enum_PhysicsServer3D_ProcessInfo>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__get_process_info>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__heightmap_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_heightmap_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__heightmap_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__hinge_joint_get_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_hinge_joint_get_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_get_flag>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__hinge_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_hinge_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__hinge_joint_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_hinge_joint_set_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`HingeJointFlag<enum_PhysicsServer3D_HingeJointFlag>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_set_flag>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__hinge_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_hinge_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`HingeJointParam<enum_PhysicsServer3D_HingeJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__hinge_joint_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__init}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_init**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__init>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__is_flushing_queries}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_is_flushing_queries**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__is_flushing_queries>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_clear**(joint: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_clear>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_joint_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_disable_collisions_between_bodies}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_disable_collisions_between_bodies**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, disable:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_disable_collisions_between_bodies>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_get_solver_priority}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_joint_get_solver_priority**(joint:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_get_solver_priority>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_get_type}
::: rst-class
classref-method
:::
::::

`JointType<enum_PhysicsServer3D_JointType>`{.interpreted-text
role="ref"} **\_joint_get_type**(joint:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_get_type>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_is_disabled_collisions_between_bodies}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_joint_is_disabled_collisions_between_bodies**(joint:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_is_disabled_collisions_between_bodies>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_make_cone_twist}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_cone_twist**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_A: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, body_B: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_B: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_make_cone_twist>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_make_generic_6dof}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_generic_6dof**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_A: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, body_B: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_B: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_make_generic_6dof>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_make_hinge}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_hinge**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
hinge_A: `Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
body_B: `RID<class_RID>`{.interpreted-text role="ref"}, hinge_B:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_make_hinge>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_make_hinge_simple}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_hinge_simple**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
pivot_A: `Vector3<class_Vector3>`{.interpreted-text role="ref"}, axis_A:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, body_B:
`RID<class_RID>`{.interpreted-text role="ref"}, pivot_B:
`Vector3<class_Vector3>`{.interpreted-text role="ref"}, axis_B:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_make_hinge_simple>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_make_pin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_pin**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_A: `Vector3<class_Vector3>`{.interpreted-text role="ref"}, body_B:
`RID<class_RID>`{.interpreted-text role="ref"}, local_B:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_make_pin>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_make_slider}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_slider**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, body_A: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_A: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"}, body_B: `RID<class_RID>`{.interpreted-text role="ref"},
local_ref_B: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_make_slider>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__joint_set_solver_priority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_set_solver_priority**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, priority:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__joint_set_solver_priority>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__pin_joint_get_local_a}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**\_pin_joint_get_local_a**(joint: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__pin_joint_get_local_a>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__pin_joint_get_local_b}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**\_pin_joint_get_local_b**(joint: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__pin_joint_get_local_b>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__pin_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_pin_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__pin_joint_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__pin_joint_set_local_a}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pin_joint_set_local_a**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, local_A: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__pin_joint_set_local_a>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__pin_joint_set_local_b}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pin_joint_set_local_b**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, local_B: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__pin_joint_set_local_b>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__pin_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pin_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer3D_PinJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__pin_joint_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__separation_ray_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_separation_ray_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__separation_ray_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_active**(active: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__set_active>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__shape_get_custom_solver_bias}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shape_get_custom_solver_bias**(shape:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__shape_get_custom_solver_bias>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__shape_get_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_shape_get_data**(shape: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__shape_get_data>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__shape_get_margin}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_shape_get_margin**(shape: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__shape_get_margin>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__shape_get_type}
::: rst-class
classref-method
:::
::::

`ShapeType<enum_PhysicsServer3D_ShapeType>`{.interpreted-text
role="ref"} **\_shape_get_type**(shape:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__shape_get_type>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__shape_set_custom_solver_bias}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shape_set_custom_solver_bias**(shape:
`RID<class_RID>`{.interpreted-text role="ref"}, bias:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__shape_set_custom_solver_bias>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__shape_set_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shape_set_data**(shape: `RID<class_RID>`{.interpreted-text
role="ref"}, data: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__shape_set_data>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__shape_set_margin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shape_set_margin**(shape: `RID<class_RID>`{.interpreted-text
role="ref"}, margin: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__shape_set_margin>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__slider_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_slider_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__slider_joint_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__slider_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_slider_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SliderJointParam<enum_PhysicsServer3D_SliderJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__slider_joint_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_add_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_add_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, body_b:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_add_collision_exception>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_apply_central_force**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_central_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_apply_central_impulse**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_central_impulse>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_apply_point_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_apply_point_force**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, point_index:
`int<class_int>`{.interpreted-text role="ref"}, force:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_point_force>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_apply_point_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_apply_point_impulse**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, point_index:
`int<class_int>`{.interpreted-text role="ref"}, impulse:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_apply_point_impulse>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_soft_body_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_bounds}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"}
**\_soft_body_get_bounds**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_bounds>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_exceptions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\]
**\_soft_body_get_collision_exceptions**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_collision_exceptions>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_layer}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_soft_body_get_collision_layer**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_collision_layer>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_collision_mask}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_soft_body_get_collision_mask**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_damping_coefficient}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_soft_body_get_damping_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_damping_coefficient>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_drag_coefficient}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_soft_body_get_drag_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_drag_coefficient>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_linear_stiffness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_soft_body_get_linear_stiffness**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_linear_stiffness>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_point_global_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**\_soft_body_get_point_global_position**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, point_index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_point_global_position>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_pressure_coefficient}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_soft_body_get_pressure_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_pressure_coefficient>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_shrinking_factor}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_soft_body_get_shrinking_factor**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_shrinking_factor>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_simulation_precision}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_soft_body_get_simulation_precision**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_simulation_precision>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_space}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_soft_body_get_space**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_space>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_state}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_soft_body_get_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_state>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_get_total_mass}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_soft_body_get_total_mass**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_get_total_mass>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_is_point_pinned}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_soft_body_is_point_pinned**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, point_index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_is_point_pinned>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_move_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_move_point**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, point_index: `int<class_int>`{.interpreted-text
role="ref"}, global_position: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_move_point>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_pin_point}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_pin_point**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, point_index: `int<class_int>`{.interpreted-text
role="ref"}, pin: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_pin_point>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_remove_all_pinned_points}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_remove_all_pinned_points**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_remove_all_pinned_points>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_remove_collision_exception}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_remove_collision_exception**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, body_b:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_remove_collision_exception>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_collision_layer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_collision_layer**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, layer:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_collision_layer>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_collision_mask}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_collision_mask**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, mask:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_collision_mask>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_damping_coefficient}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_damping_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, damping_coefficient:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_damping_coefficient>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_drag_coefficient}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_drag_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, drag_coefficient:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_drag_coefficient>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_linear_stiffness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_linear_stiffness**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, linear_stiffness:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_linear_stiffness>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_mesh}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_mesh**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, mesh: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_mesh>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_pressure_coefficient}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_pressure_coefficient**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, pressure_coefficient:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_pressure_coefficient>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_ray_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_ray_pickable**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_ray_pickable>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_shrinking_factor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_shrinking_factor**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, shrinking_factor:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_shrinking_factor>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_simulation_precision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_simulation_precision**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, simulation_precision:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_simulation_precision>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_space}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_space**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, space: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_space>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer3D_BodyState>`{.interpreted-text
role="ref"}, variant: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_state>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_total_mass}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_total_mass**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, total_mass: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_total_mass>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_set_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_set_transform>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_soft_body_update_rendering_server**(body:
`RID<class_RID>`{.interpreted-text role="ref"},
rendering_server_handler:
`PhysicsServer3DRenderingServerHandler<class_PhysicsServer3DRenderingServerHandler>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__soft_body_update_rendering_server>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_space_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_get_contact_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_space_get_contact_count**(space: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_get_contact_count>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_get_contacts}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **\_space_get_contacts**(space:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_get_contacts>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_get_direct_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectSpaceState3D<class_PhysicsDirectSpaceState3D>`{.interpreted-text
role="ref"} **\_space_get_direct_state**(space:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_get_direct_state>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_space_get_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_get_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_space_is_active**(space: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_is_active>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_set_active}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_space_set_active**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, active: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_set_active>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_set_debug_contacts}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_space_set_debug_contacts**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, max_contacts: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_set_debug_contacts>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__space_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_space_set_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer3D_SpaceParameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__space_set_param>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__sphere_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_sphere_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__sphere_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__step}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_step**(step: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__step>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__sync}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_sync**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__sync>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_private_method__world_boundary_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_world_boundary_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_private_method__world_boundary_shape_create>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_body}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_test_motion_is_excluding_body**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_body>`{.interpreted-text
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

:::: {#class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_test_motion_is_excluding_object**(object:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer3DExtension_method_body_test_motion_is_excluding_object>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
