github_url
:   hide

# PhysicsServer2DExtension {#class_PhysicsServer2DExtension}

**Inherits:** `PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Provides virtual methods that can be overridden to create custom
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}
implementations.

::: rst-class
classref-introduction-group
:::

## Description

This class extends
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}
by providing additional virtual methods that can be overridden. When
these methods are overridden, they will be called instead of the
internal methods of the physics server.

Intended for use with GDExtension to create custom implementations of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text role="ref"}.

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

:::: {#class_PhysicsServer2DExtension_private_method__area_add_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_add_shape**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape: `RID<class_RID>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_add_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_add_shape()<class_PhysicsServer2D_method_area_add_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_attach_canvas_instance_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_attach_canvas_instance_id**(area:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_attach_canvas_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_attach_canvas_instance_id()<class_PhysicsServer2D_method_area_attach_canvas_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_attach_object_instance_id}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_attach_object_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_attach_object_instance_id()<class_PhysicsServer2D_method_area_attach_object_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_clear_shapes}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_clear_shapes>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_clear_shapes()<class_PhysicsServer2D_method_area_clear_shapes>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_area_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_create()<class_PhysicsServer2D_method_area_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_canvas_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_area_get_canvas_instance_id**(area:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_get_canvas_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_canvas_instance_id()<class_PhysicsServer2D_method_area_get_canvas_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_collision_layer}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_get_collision_layer>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_collision_layer()<class_PhysicsServer2D_method_area_get_collision_layer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_collision_mask}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_get_collision_mask>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_collision_mask()<class_PhysicsServer2D_method_area_get_collision_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_object_instance_id}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_get_object_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_object_instance_id()<class_PhysicsServer2D_method_area_get_object_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_param}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_area_get_param**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_get_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_param()<class_PhysicsServer2D_method_area_get_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_shape}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_get_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_shape()<class_PhysicsServer2D_method_area_get_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_shape_count}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_get_shape_count>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_shape_count()<class_PhysicsServer2D_method_area_get_shape_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_shape_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**\_area_get_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_get_shape_transform>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_shape_transform()<class_PhysicsServer2D_method_area_get_shape_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_space}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_get_space>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_space()<class_PhysicsServer2D_method_area_get_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_get_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**\_area_get_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_get_transform>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_get_transform()<class_PhysicsServer2D_method_area_get_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_remove_shape}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_remove_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_remove_shape()<class_PhysicsServer2D_method_area_remove_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_area_monitor_callback}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_area_monitor_callback>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_area_monitor_callback()<class_PhysicsServer2D_method_area_set_area_monitor_callback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_collision_layer}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_collision_layer>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_collision_layer()<class_PhysicsServer2D_method_area_set_collision_layer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_collision_mask}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_collision_mask>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_collision_mask()<class_PhysicsServer2D_method_area_set_collision_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_monitor_callback}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_monitor_callback>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_monitor_callback()<class_PhysicsServer2D_method_area_set_monitor_callback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_monitorable}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_monitorable>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_monitorable()<class_PhysicsServer2D_method_area_set_monitorable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_param**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`AreaParameter<enum_PhysicsServer2D_AreaParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_set_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_param()<class_PhysicsServer2D_method_area_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_pickable**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, pickable: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_set_pickable>`{.interpreted-text
role="ref"}

If set to `true`, allows the area with the given
`RID<class_RID>`{.interpreted-text role="ref"} to detect mouse inputs
when the mouse cursor is hovering on it.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `area_set_pickable` method. Corresponds to
`CollisionObject2D.input_pickable<class_CollisionObject2D_property_input_pickable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_shape}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_shape()<class_PhysicsServer2D_method_area_set_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_shape_disabled}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_shape_disabled>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_shape_disabled()<class_PhysicsServer2D_method_area_set_shape_disabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_shape_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_shape_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_set_shape_transform>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_shape_transform()<class_PhysicsServer2D_method_area_set_shape_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_space}
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
`🔗<class_PhysicsServer2DExtension_private_method__area_set_space>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_space()<class_PhysicsServer2D_method_area_set_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__area_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_area_set_transform**(area: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__area_set_transform>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.area_set_transform()<class_PhysicsServer2D_method_area_set_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_add_collision_exception}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_add_collision_exception>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_add_collision_exception()<class_PhysicsServer2D_method_body_add_collision_exception>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_add_constant_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_constant_central_force**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, force:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_add_constant_central_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_add_constant_central_force()<class_PhysicsServer2D_method_body_add_constant_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_add_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_add_constant_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_add_constant_force()<class_PhysicsServer2D_method_body_add_constant_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_add_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_add_constant_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_add_constant_torque()<class_PhysicsServer2D_method_body_add_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_add_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_add_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape: `RID<class_RID>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_add_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_add_shape()<class_PhysicsServer2D_method_body_add_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_apply_central_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_central_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_apply_central_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_apply_central_force()<class_PhysicsServer2D_method_body_apply_central_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_apply_central_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_central_impulse**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, impulse:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_apply_central_impulse>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_apply_central_impulse()<class_PhysicsServer2D_method_body_apply_central_impulse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_apply_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_apply_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_apply_force()<class_PhysicsServer2D_method_body_apply_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_apply_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_apply_impulse>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_apply_impulse()<class_PhysicsServer2D_method_body_apply_impulse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_apply_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_apply_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_apply_torque()<class_PhysicsServer2D_method_body_apply_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_apply_torque_impulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_apply_torque_impulse**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, impulse: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_apply_torque_impulse>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_apply_torque_impulse()<class_PhysicsServer2D_method_body_apply_torque_impulse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_attach_canvas_instance_id}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_attach_canvas_instance_id**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, id:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_attach_canvas_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_attach_canvas_instance_id()<class_PhysicsServer2D_method_body_attach_canvas_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_attach_object_instance_id}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_attach_object_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_attach_object_instance_id()<class_PhysicsServer2D_method_body_attach_object_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_clear_shapes}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_clear_shapes>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_clear_shapes()<class_PhysicsServer2D_method_body_clear_shapes>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_collide_shape}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_body_collide_shape**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, body_shape: `int<class_int>`{.interpreted-text role="ref"},
shape: `RID<class_RID>`{.interpreted-text role="ref"}, shape_xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}, motion:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, results:
`void*`, result_max: `int<class_int>`{.interpreted-text role="ref"},
result_count: `int32_t*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_collide_shape>`{.interpreted-text
role="ref"}

Given a `body`, a `shape`, and their respective parameters, this method
should return `true` if a collision between the two would occur, with
additional details passed in `results`.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `shape_collide` method. Corresponds to
`PhysicsDirectSpaceState2D.collide_shape()<class_PhysicsDirectSpaceState2D_method_collide_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_body_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_create()<class_PhysicsServer2D_method_body_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_canvas_instance_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_body_get_canvas_instance_id**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_canvas_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_canvas_instance_id()<class_PhysicsServer2D_method_body_get_canvas_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_collision_exceptions}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_collision_exceptions>`{.interpreted-text
role="ref"}

Returns the `RID<class_RID>`{.interpreted-text role="ref"}s of all
bodies added as collision exceptions for the given `body`. See also
`_body_add_collision_exception()<class_PhysicsServer2DExtension_private_method__body_add_collision_exception>`{.interpreted-text
role="ref"} and
`_body_remove_collision_exception()<class_PhysicsServer2DExtension_private_method__body_remove_collision_exception>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `body_get_collision_exceptions` method.
Corresponds to
`PhysicsBody2D.get_collision_exceptions()<class_PhysicsBody2D_method_get_collision_exceptions>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_collision_layer}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_collision_layer>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_collision_layer()<class_PhysicsServer2D_method_body_get_collision_layer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_collision_mask}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_collision_mask>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_collision_mask()<class_PhysicsServer2D_method_body_get_collision_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_collision_priority}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_collision_priority>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_collision_priority()<class_PhysicsServer2D_method_body_get_collision_priority>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_constant_force}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_body_get_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_constant_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_constant_force()<class_PhysicsServer2D_method_body_get_constant_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_constant_torque}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_body_get_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_constant_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_constant_torque()<class_PhysicsServer2D_method_body_get_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_contacts_reported_depth_threshold}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_contacts_reported_depth_threshold>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `body_get_contacts_reported_depth_threshold`
method.

\*\*Note:\*\* This method is currently unused by Godot\'s default
physics implementation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_continuous_collision_detection_mode}
::: rst-class
classref-method
:::
::::

`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"}
**\_body_get_continuous_collision_detection_mode**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_continuous_collision_detection_mode>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_continuous_collision_detection_mode()<class_PhysicsServer2D_method_body_get_continuous_collision_detection_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_direct_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectBodyState2D<class_PhysicsDirectBodyState2D>`{.interpreted-text
role="ref"} **\_body_get_direct_state**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_direct_state>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_direct_state()<class_PhysicsServer2D_method_body_get_direct_state>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_max_contacts_reported}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_max_contacts_reported>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_max_contacts_reported()<class_PhysicsServer2D_method_body_get_max_contacts_reported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_mode}
::: rst-class
classref-method
:::
::::

`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"}
**\_body_get_mode**(body: `RID<class_RID>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_mode>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_mode()<class_PhysicsServer2D_method_body_get_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_object_instance_id}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_object_instance_id>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_object_instance_id()<class_PhysicsServer2D_method_body_get_object_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_param}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_body_get_param**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_param()<class_PhysicsServer2D_method_body_get_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_shape}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_shape()<class_PhysicsServer2D_method_body_get_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_shape_count}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_shape_count>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_shape_count()<class_PhysicsServer2D_method_body_get_shape_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_shape_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**\_body_get_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_shape_transform>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_shape_transform()<class_PhysicsServer2D_method_body_get_shape_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_space}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_get_space>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_space()<class_PhysicsServer2D_method_body_get_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_get_state}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_body_get_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_get_state>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_get_state()<class_PhysicsServer2D_method_body_get_state>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_is_omitting_force_integration}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_is_omitting_force_integration>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_is_omitting_force_integration()<class_PhysicsServer2D_method_body_is_omitting_force_integration>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_remove_collision_exception}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_remove_collision_exception>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_remove_collision_exception()<class_PhysicsServer2D_method_body_remove_collision_exception>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_remove_shape}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_remove_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_remove_shape()<class_PhysicsServer2D_method_body_remove_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_reset_mass_properties}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_reset_mass_properties>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_reset_mass_properties()<class_PhysicsServer2D_method_body_reset_mass_properties>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_axis_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_axis_velocity**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, axis_velocity: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_axis_velocity>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_axis_velocity()<class_PhysicsServer2D_method_body_set_axis_velocity>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_collision_layer}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_collision_layer>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_collision_layer()<class_PhysicsServer2D_method_body_set_collision_layer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_collision_mask}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_collision_mask>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_collision_mask()<class_PhysicsServer2D_method_body_set_collision_mask>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_collision_priority}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_collision_priority>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_collision_priority()<class_PhysicsServer2D_method_body_set_collision_priority>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_constant_force}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_constant_force**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, force: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_constant_force>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_constant_force()<class_PhysicsServer2D_method_body_set_constant_force>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_constant_torque}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_constant_torque**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, torque: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_constant_torque>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_constant_torque()<class_PhysicsServer2D_method_body_set_constant_torque>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_contacts_reported_depth_threshold}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_contacts_reported_depth_threshold>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `body_set_contacts_reported_depth_threshold`
method.

\*\*Note:\*\* This method is currently unused by Godot\'s default
physics implementation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_continuous_collision_detection_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_continuous_collision_detection_mode**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, mode:
`CCDMode<enum_PhysicsServer2D_CCDMode>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_continuous_collision_detection_mode>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_continuous_collision_detection_mode()<class_PhysicsServer2D_method_body_set_continuous_collision_detection_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_force_integration_callback}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_force_integration_callback>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_force_integration_callback()<class_PhysicsServer2D_method_body_set_force_integration_callback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_max_contacts_reported}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_max_contacts_reported>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_max_contacts_reported()<class_PhysicsServer2D_method_body_set_max_contacts_reported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_mode**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, mode:
`BodyMode<enum_PhysicsServer2D_BodyMode>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_mode>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_mode()<class_PhysicsServer2D_method_body_set_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_omit_force_integration}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_omit_force_integration>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_omit_force_integration()<class_PhysicsServer2D_method_body_set_omit_force_integration>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_param**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`BodyParameter<enum_PhysicsServer2D_BodyParameter>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_param()<class_PhysicsServer2D_method_body_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_pickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_pickable**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, pickable: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_pickable>`{.interpreted-text
role="ref"}

If set to `true`, allows the body with the given
`RID<class_RID>`{.interpreted-text role="ref"} to detect mouse inputs
when the mouse cursor is hovering on it.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `body_set_pickable` method. Corresponds to
`CollisionObject2D.input_pickable<class_CollisionObject2D_property_input_pickable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_shape}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_shape>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_shape()<class_PhysicsServer2D_method_body_set_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_shape_as_one_way_collision}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_shape_as_one_way_collision**(body:
`RID<class_RID>`{.interpreted-text role="ref"}, shape_idx:
`int<class_int>`{.interpreted-text role="ref"}, enable:
`bool<class_bool>`{.interpreted-text role="ref"}, margin:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_shape_as_one_way_collision>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_shape_as_one_way_collision()<class_PhysicsServer2D_method_body_set_shape_as_one_way_collision>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_shape_disabled}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_shape_disabled>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_shape_disabled()<class_PhysicsServer2D_method_body_set_shape_disabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_shape_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_shape_transform**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, shape_idx: `int<class_int>`{.interpreted-text role="ref"},
transform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_shape_transform>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_shape_transform()<class_PhysicsServer2D_method_body_set_shape_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_space}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_space>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_space()<class_PhysicsServer2D_method_body_set_space>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_body_set_state**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, state:
`BodyState<enum_PhysicsServer2D_BodyState>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_set_state>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_set_state()<class_PhysicsServer2D_method_body_set_state>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_set_state_sync_callback}
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
`🔗<class_PhysicsServer2DExtension_private_method__body_set_state_sync_callback>`{.interpreted-text
role="ref"}

Assigns the `body` to call the given `callable` during the
synchronization phase of the loop, before
`_step()<class_PhysicsServer2DExtension_private_method__step>`{.interpreted-text
role="ref"} is called. See also
`_sync()<class_PhysicsServer2DExtension_private_method__sync>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D.body_set_state_sync_callback()<class_PhysicsServer2D_method_body_set_state_sync_callback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__body_test_motion}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_body_test_motion**(body: `RID<class_RID>`{.interpreted-text
role="ref"}, from: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, motion: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, margin: `float<class_float>`{.interpreted-text role="ref"},
collide_separation_ray: `bool<class_bool>`{.interpreted-text
role="ref"}, recovery_as_collision: `bool<class_bool>`{.interpreted-text
role="ref"}, result: `PhysicsServer2DExtensionMotionResult*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__body_test_motion>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.body_test_motion()<class_PhysicsServer2D_method_body_test_motion>`{.interpreted-text
role="ref"}. Unlike the exposed implementation, this method does not
receive all of the arguments inside a
`PhysicsTestMotionParameters2D<class_PhysicsTestMotionParameters2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__capsule_shape_create}
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
`🔗<class_PhysicsServer2DExtension_private_method__capsule_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.capsule_shape_create()<class_PhysicsServer2D_method_capsule_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__circle_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_circle_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__circle_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.circle_shape_create()<class_PhysicsServer2D_method_circle_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__concave_polygon_shape_create}
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
`🔗<class_PhysicsServer2DExtension_private_method__concave_polygon_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.concave_polygon_shape_create()<class_PhysicsServer2D_method_concave_polygon_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__convex_polygon_shape_create}
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
`🔗<class_PhysicsServer2DExtension_private_method__convex_polygon_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.convex_polygon_shape_create()<class_PhysicsServer2D_method_convex_polygon_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__damped_spring_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_damped_spring_joint_get_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, param:
`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__damped_spring_joint_get_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.damped_spring_joint_get_param()<class_PhysicsServer2D_method_damped_spring_joint_get_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__damped_spring_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_damped_spring_joint_set_param**(joint:
`RID<class_RID>`{.interpreted-text role="ref"}, param:
`DampedSpringParam<enum_PhysicsServer2D_DampedSpringParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__damped_spring_joint_set_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.damped_spring_joint_set_param()<class_PhysicsServer2D_method_damped_spring_joint_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__end_sync}
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
`🔗<class_PhysicsServer2DExtension_private_method__end_sync>`{.interpreted-text
role="ref"}

Called to indicate that the physics server has stopped synchronizing. It
is in the loop\'s iteration/physics phase, and can access physics
objects even if running on a separate thread. See also
`_sync()<class_PhysicsServer2DExtension_private_method__sync>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `end_sync` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__finish}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_finish**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__finish>`{.interpreted-text
role="ref"}

Called when the main loop finalizes to shut down the physics server. See
also
`MainLoop._finalize()<class_MainLoop_private_method__finalize>`{.interpreted-text
role="ref"} and
`_init()<class_PhysicsServer2DExtension_private_method__init>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `finish` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__flush_queries}
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
`🔗<class_PhysicsServer2DExtension_private_method__flush_queries>`{.interpreted-text
role="ref"}

Called every physics step before
`_step()<class_PhysicsServer2DExtension_private_method__step>`{.interpreted-text
role="ref"} to process all remaining queries.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `flush_queries` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__free_rid}
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
`🔗<class_PhysicsServer2DExtension_private_method__free_rid>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.free_rid()<class_PhysicsServer2D_method_free_rid>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__get_process_info}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_process_info**(process_info:
`ProcessInfo<enum_PhysicsServer2D_ProcessInfo>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__get_process_info>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.get_process_info()<class_PhysicsServer2D_method_get_process_info>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__init}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_init**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__init>`{.interpreted-text
role="ref"}

Called when the main loop is initialized and creates a new instance of
this physics server. See also
`MainLoop._initialize()<class_MainLoop_private_method__initialize>`{.interpreted-text
role="ref"} and
`_finish()<class_PhysicsServer2DExtension_private_method__finish>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `init` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__is_flushing_queries}
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
`🔗<class_PhysicsServer2DExtension_private_method__is_flushing_queries>`{.interpreted-text
role="ref"}

Overridable method that should return `true` when the physics server is
processing queries. See also
`_flush_queries()<class_PhysicsServer2DExtension_private_method__flush_queries>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `is_flushing_queries` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_clear}
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
`🔗<class_PhysicsServer2DExtension_private_method__joint_clear>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_clear()<class_PhysicsServer2D_method_joint_clear>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_joint_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__joint_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_create()<class_PhysicsServer2D_method_joint_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_disable_collisions_between_bodies}
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
`🔗<class_PhysicsServer2DExtension_private_method__joint_disable_collisions_between_bodies>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_disable_collisions_between_bodies()<class_PhysicsServer2D_method_joint_disable_collisions_between_bodies>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__joint_get_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_get_param()<class_PhysicsServer2D_method_joint_get_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_get_type}
::: rst-class
classref-method
:::
::::

`JointType<enum_PhysicsServer2D_JointType>`{.interpreted-text
role="ref"} **\_joint_get_type**(joint:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__joint_get_type>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_get_type()<class_PhysicsServer2D_method_joint_get_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_is_disabled_collisions_between_bodies}
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
`🔗<class_PhysicsServer2DExtension_private_method__joint_is_disabled_collisions_between_bodies>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_is_disabled_collisions_between_bodies()<class_PhysicsServer2D_method_joint_is_disabled_collisions_between_bodies>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_make_damped_spring}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_damped_spring**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, anchor_a: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, anchor_b: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, body_a: `RID<class_RID>`{.interpreted-text role="ref"},
body_b: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__joint_make_damped_spring>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_make_damped_spring()<class_PhysicsServer2D_method_joint_make_damped_spring>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_make_groove}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_groove**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, a_groove1: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, a_groove2: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, b_anchor: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, body_a: `RID<class_RID>`{.interpreted-text role="ref"},
body_b: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__joint_make_groove>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_make_groove()<class_PhysicsServer2D_method_joint_make_groove>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_make_pin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_make_pin**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, anchor: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, body_a: `RID<class_RID>`{.interpreted-text role="ref"},
body_b: `RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__joint_make_pin>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_make_pin()<class_PhysicsServer2D_method_joint_make_pin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`JointParam<enum_PhysicsServer2D_JointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__joint_set_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.joint_set_param()<class_PhysicsServer2D_method_joint_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__pin_joint_get_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_pin_joint_get_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__pin_joint_get_flag>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.pin_joint_get_flag()<class_PhysicsServer2D_method_pin_joint_get_flag>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__pin_joint_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_pin_joint_get_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__pin_joint_get_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.pin_joint_get_param()<class_PhysicsServer2D_method_pin_joint_get_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__pin_joint_set_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pin_joint_set_flag**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, flag:
`PinJointFlag<enum_PhysicsServer2D_PinJointFlag>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__pin_joint_set_flag>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.pin_joint_set_flag()<class_PhysicsServer2D_method_pin_joint_set_flag>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__pin_joint_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pin_joint_set_param**(joint: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`PinJointParam<enum_PhysicsServer2D_PinJointParam>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__pin_joint_set_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.pin_joint_set_param()<class_PhysicsServer2D_method_pin_joint_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__rectangle_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_rectangle_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__rectangle_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.rectangle_shape_create()<class_PhysicsServer2D_method_rectangle_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__segment_shape_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_segment_shape_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__segment_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.segment_shape_create()<class_PhysicsServer2D_method_segment_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__separation_ray_shape_create}
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
`🔗<class_PhysicsServer2DExtension_private_method__separation_ray_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.separation_ray_shape_create()<class_PhysicsServer2D_method_separation_ray_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__set_active}
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
`🔗<class_PhysicsServer2DExtension_private_method__set_active>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.set_active()<class_PhysicsServer2D_method_set_active>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__shape_collide}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_shape_collide**(shape_A: `RID<class_RID>`{.interpreted-text
role="ref"}, xform_A: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, motion_A: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, shape_B: `RID<class_RID>`{.interpreted-text role="ref"},
xform_B: `Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
motion_B: `Vector2<class_Vector2>`{.interpreted-text role="ref"},
results: `void*`, result_max: `int<class_int>`{.interpreted-text
role="ref"}, result_count: `int32_t*`)
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__shape_collide>`{.interpreted-text
role="ref"}

Given two shapes and their parameters, should return `true` if a
collision between the two would occur, with additional details passed in
`results`.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `shape_collide` method. Corresponds to
`PhysicsDirectSpaceState2D.collide_shape()<class_PhysicsDirectSpaceState2D_method_collide_shape>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__shape_get_custom_solver_bias}
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
`🔗<class_PhysicsServer2DExtension_private_method__shape_get_custom_solver_bias>`{.interpreted-text
role="ref"}

Should return the custom solver bias of the given `shape`, which defines
how much bodies are forced to separate on contact when this shape is
involved.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `shape_get_custom_solver_bias` method.
Corresponds to
`Shape2D.custom_solver_bias<class_Shape2D_property_custom_solver_bias>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__shape_get_data}
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
`🔗<class_PhysicsServer2DExtension_private_method__shape_get_data>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.shape_get_data()<class_PhysicsServer2D_method_shape_get_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__shape_get_type}
::: rst-class
classref-method
:::
::::

`ShapeType<enum_PhysicsServer2D_ShapeType>`{.interpreted-text
role="ref"} **\_shape_get_type**(shape:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__shape_get_type>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.shape_get_type()<class_PhysicsServer2D_method_shape_get_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__shape_set_custom_solver_bias}
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
`🔗<class_PhysicsServer2DExtension_private_method__shape_set_custom_solver_bias>`{.interpreted-text
role="ref"}

Should set the custom solver bias for the given `shape`. It defines how
much bodies are forced to separate on contact.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `shape_get_custom_solver_bias` method.
Corresponds to
`Shape2D.custom_solver_bias<class_Shape2D_property_custom_solver_bias>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__shape_set_data}
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
`🔗<class_PhysicsServer2DExtension_private_method__shape_set_data>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.shape_set_data()<class_PhysicsServer2D_method_shape_set_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_create}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_space_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__space_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.space_create()<class_PhysicsServer2D_method_space_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_get_contact_count}
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
`🔗<class_PhysicsServer2DExtension_private_method__space_get_contact_count>`{.interpreted-text
role="ref"}

Should return how many contacts have occurred during the last physics
step in the given `space`. See also
`_space_get_contacts()<class_PhysicsServer2DExtension_private_method__space_get_contacts>`{.interpreted-text
role="ref"} and
`_space_set_debug_contacts()<class_PhysicsServer2DExtension_private_method__space_set_debug_contacts>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `space_get_contact_count` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_get_contacts}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **\_space_get_contacts**(space:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__space_get_contacts>`{.interpreted-text
role="ref"}

Should return the positions of all contacts that have occurred during
the last physics step in the given `space`. See also
`_space_get_contact_count()<class_PhysicsServer2DExtension_private_method__space_get_contact_count>`{.interpreted-text
role="ref"} and
`_space_set_debug_contacts()<class_PhysicsServer2DExtension_private_method__space_set_debug_contacts>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `space_get_contacts` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_get_direct_state}
::: rst-class
classref-method
:::
::::

`PhysicsDirectSpaceState2D<class_PhysicsDirectSpaceState2D>`{.interpreted-text
role="ref"} **\_space_get_direct_state**(space:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__space_get_direct_state>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.space_get_direct_state()<class_PhysicsServer2D_method_space_get_direct_state>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_get_param}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**\_space_get_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__space_get_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.space_get_param()<class_PhysicsServer2D_method_space_get_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_is_active}
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
`🔗<class_PhysicsServer2DExtension_private_method__space_is_active>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.space_is_active()<class_PhysicsServer2D_method_space_is_active>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_set_active}
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
`🔗<class_PhysicsServer2DExtension_private_method__space_set_active>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.space_set_active()<class_PhysicsServer2D_method_space_set_active>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_set_debug_contacts}
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
`🔗<class_PhysicsServer2DExtension_private_method__space_set_debug_contacts>`{.interpreted-text
role="ref"}

Used internally to allow the given `space` to store contact points, up
to `max_contacts`. This is automatically set for the main
`World2D<class_World2D>`{.interpreted-text role="ref"}\'s space when
`SceneTree.debug_collisions_hint<class_SceneTree_property_debug_collisions_hint>`{.interpreted-text
role="ref"} is `true`, or by checking \"Visible Collision Shapes\" in
the editor. Only works in debug builds.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `space_set_debug_contacts` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__space_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_space_set_param**(space: `RID<class_RID>`{.interpreted-text
role="ref"}, param:
`SpaceParameter<enum_PhysicsServer2D_SpaceParameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__space_set_param>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.space_set_param()<class_PhysicsServer2D_method_space_set_param>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__step}
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
`🔗<class_PhysicsServer2DExtension_private_method__step>`{.interpreted-text
role="ref"}

Called every physics step to process the physics simulation. `step` is
the time elapsed since the last physics step, in seconds. It is usually
the same as the value returned by
`Node.get_physics_process_delta_time()<class_Node_method_get_physics_process_delta_time>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `step` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__sync}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_sync**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`required (This method is required to be overridden when extending its base class.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_private_method__sync>`{.interpreted-text
role="ref"}

Called to indicate that the physics server is synchronizing and cannot
access physics states if running on a separate thread. See also
`_end_sync()<class_PhysicsServer2DExtension_private_method__end_sync>`{.interpreted-text
role="ref"}.

Overridable version of
`PhysicsServer2D<class_PhysicsServer2D>`{.interpreted-text
role="ref"}\'s internal `sync` method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_private_method__world_boundary_shape_create}
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
`🔗<class_PhysicsServer2DExtension_private_method__world_boundary_shape_create>`{.interpreted-text
role="ref"}

Overridable version of
`PhysicsServer2D.world_boundary_shape_create()<class_PhysicsServer2D_method_world_boundary_shape_create>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_body}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_test_motion_is_excluding_body**(body:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_body>`{.interpreted-text
role="ref"}

Returns `true` if the body with the given
`RID<class_RID>`{.interpreted-text role="ref"} is being excluded from
`_body_test_motion()<class_PhysicsServer2DExtension_private_method__body_test_motion>`{.interpreted-text
role="ref"}. See also
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**body_test_motion_is_excluding_object**(object:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PhysicsServer2DExtension_method_body_test_motion_is_excluding_object>`{.interpreted-text
role="ref"}

Returns `true` if the object with the given instance ID is being
excluded from
`_body_test_motion()<class_PhysicsServer2DExtension_private_method__body_test_motion>`{.interpreted-text
role="ref"}. See also
`Object.get_instance_id()<class_Object_method_get_instance_id>`{.interpreted-text
role="ref"}.
