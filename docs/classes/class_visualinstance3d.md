github_url
:   hide

# VisualInstance3D {#class_VisualInstance3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `Decal<class_Decal>`{.interpreted-text role="ref"},
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"},
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"},
`GPUParticlesAttractor3D<class_GPUParticlesAttractor3D>`{.interpreted-text
role="ref"},
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"}, `Light3D<class_Light3D>`{.interpreted-text role="ref"},
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"},
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"},
`OpenXRVisibilityMask<class_OpenXRVisibilityMask>`{.interpreted-text
role="ref"}, `ReflectionProbe<class_ReflectionProbe>`{.interpreted-text
role="ref"}, `RootMotionView<class_RootMotionView>`{.interpreted-text
role="ref"},
`VisibleOnScreenNotifier3D<class_VisibleOnScreenNotifier3D>`{.interpreted-text
role="ref"}, `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}

Parent of all visual 3D nodes.

::: rst-class
classref-introduction-group
:::

## Description

The **VisualInstance3D** is used to connect a resource to a visual
representation. All visual 3D nodes inherit from the
**VisualInstance3D**. In general, you should not access the
**VisualInstance3D** properties directly as they are accessed and
managed by the nodes that inherit from **VisualInstance3D**.
**VisualInstance3D** is the node representation of the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
instance.

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

:::: {#class_VisualInstance3D_property_layers}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **layers** = `1`
`🔗<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_layer_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_layer_mask**()

The render layer(s) this **VisualInstance3D** is drawn on.

This object will only be visible for
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}s whose cull
mask includes any of the render layers this **VisualInstance3D** is set
to.

For `Light3D<class_Light3D>`{.interpreted-text role="ref"}s, this can be
used to control which **VisualInstance3D**s are affected by a specific
light. For `GPUParticles3D<class_GPUParticles3D>`{.interpreted-text
role="ref"}, this can be used to control which particles are effected by
a specific attractor. For `Decal<class_Decal>`{.interpreted-text
role="ref"}s, this can be used to control which **VisualInstance3D**s
are affected by a specific decal.

To adjust
`layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} more easily using a script, use
`get_layer_mask_value()<class_VisualInstance3D_method_get_layer_mask_value>`{.interpreted-text
role="ref"} and
`set_layer_mask_value()<class_VisualInstance3D_method_set_layer_mask_value>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"},
SDFGI and `LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}
will always take all layers into account to determine what contributes
to global illumination. If this is an issue, set
`GeometryInstance3D.gi_mode<class_GeometryInstance3D_property_gi_mode>`{.interpreted-text
role="ref"} to
`GeometryInstance3D.GI_MODE_DISABLED<class_GeometryInstance3D_constant_GI_MODE_DISABLED>`{.interpreted-text
role="ref"} for meshes and
`Light3D.light_bake_mode<class_Light3D_property_light_bake_mode>`{.interpreted-text
role="ref"} to
`Light3D.BAKE_DISABLED<class_Light3D_constant_BAKE_DISABLED>`{.interpreted-text
role="ref"} for lights to exclude them from global illumination.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualInstance3D_property_sorting_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **sorting_offset** =
`0.0`
`🔗<class_VisualInstance3D_property_sorting_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sorting_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sorting_offset**()

The amount by which the depth of this **VisualInstance3D** will be
adjusted when sorting by depth. Uses the same units as the engine (which
are typically meters). Adjusting it to a higher value will make the
**VisualInstance3D** reliably draw on top of other **VisualInstance3D**s
that are otherwise positioned at the same spot. To ensure it always
draws on top of other objects around it (not positioned at the same
spot), set the value to be greater than the distance between this
**VisualInstance3D** and the other nearby **VisualInstance3D**s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualInstance3D_property_sorting_use_aabb_center}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**sorting_use_aabb_center**
`🔗<class_VisualInstance3D_property_sorting_use_aabb_center>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sorting_use_aabb_center**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_sorting_use_aabb_center**()

If `true`, the object is sorted based on the
`AABB<class_AABB>`{.interpreted-text role="ref"} center. The object will
be sorted based on the global position otherwise.

The `AABB<class_AABB>`{.interpreted-text role="ref"} center based
sorting is generally more accurate for 3D models. The position based
sorting instead allows to better control the drawing order when working
with `GPUParticles3D<class_GPUParticles3D>`{.interpreted-text
role="ref"} and `CPUParticles3D<class_CPUParticles3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_VisualInstance3D_private_method__get_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **\_get_aabb**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualInstance3D_private_method__get_aabb>`{.interpreted-text
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

:::: {#class_VisualInstance3D_method_get_aabb}
::: rst-class
classref-method
:::
::::

`AABB<class_AABB>`{.interpreted-text role="ref"} **get_aabb**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualInstance3D_method_get_aabb>`{.interpreted-text
role="ref"}

Returns the `AABB<class_AABB>`{.interpreted-text role="ref"} (also known
as the bounding box) for this **VisualInstance3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualInstance3D_method_get_base}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_base**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualInstance3D_method_get_base>`{.interpreted-text
role="ref"}

Returns the RID of the resource associated with this
**VisualInstance3D**. For example, if the Node is a
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"},
this will return the RID of the associated
`Mesh<class_Mesh>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualInstance3D_method_get_instance}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_instance**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualInstance3D_method_get_instance>`{.interpreted-text
role="ref"}

Returns the RID of this instance. This RID is the same as the RID
returned by
`RenderingServer.instance_create()<class_RenderingServer_method_instance_create>`{.interpreted-text
role="ref"}. This RID is needed if you want to call
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}
functions directly on this **VisualInstance3D**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualInstance3D_method_get_layer_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_layer_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_VisualInstance3D_method_get_layer_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 20.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualInstance3D_method_set_base}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_base**(base: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_VisualInstance3D_method_set_base>`{.interpreted-text
role="ref"}

Sets the resource that is instantiated by this **VisualInstance3D**,
which changes how the engine handles the **VisualInstance3D** under the
hood. Equivalent to
`RenderingServer.instance_set_base()<class_RenderingServer_method_instance_set_base>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualInstance3D_method_set_layer_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_layer_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_VisualInstance3D_method_set_layer_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 20.
