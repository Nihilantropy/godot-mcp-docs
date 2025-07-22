github_url
:   hide

::: {.meta keywords="environment, envmap"}
:::

# ReflectionProbe {#class_ReflectionProbe}

**Inherits:**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Captures its surroundings to create fast, accurate reflections from a
given point.

::: rst-class
classref-introduction-group
:::

## Description

Captures its surroundings as a cubemap, and stores versions of it with
increasing levels of blur to simulate different material roughnesses.

The **ReflectionProbe** is used to create high-quality reflections at a
low performance cost (when
`update_mode<class_ReflectionProbe_property_update_mode>`{.interpreted-text
role="ref"} is
`UPDATE_ONCE<class_ReflectionProbe_constant_UPDATE_ONCE>`{.interpreted-text
role="ref"}). **ReflectionProbe**s can be blended together and with the
rest of the scene smoothly. **ReflectionProbe**s can also be combined
with `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}, SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) and screen-space reflections
(`Environment.ssr_enabled<class_Environment_property_ssr_enabled>`{.interpreted-text
role="ref"}) to get more accurate reflections in specific areas.
**ReflectionProbe**s render all objects within their
`cull_mask<class_ReflectionProbe_property_cull_mask>`{.interpreted-text
role="ref"}, so updating them can be quite expensive. It is best to
update them once with the important static objects and then leave them
as-is.

\*\*Note:\*\* Unlike `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} and SDFGI, **ReflectionProbe**s only source their
environment from a
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text role="ref"}
node. If you specify an
`Environment<class_Environment>`{.interpreted-text role="ref"} resource
within a `Camera3D<class_Camera3D>`{.interpreted-text role="ref"} node,
it will be ignored by the **ReflectionProbe**. This can lead to
incorrect lighting within the **ReflectionProbe**.

\*\*Note:\*\* Reflection probes are only supported in the Forward+ and
Mobile rendering methods, not Compatibility. When using the Mobile
rendering method, only 8 reflection probes can be displayed on each mesh
resource. Attempting to display more than 8 reflection probes on a
single mesh resource will result in reflection probes flickering in and
out as the camera moves.

\*\*Note:\*\* When using the Mobile rendering method, reflection probes
will only correctly affect meshes whose visibility AABB intersects with
the reflection probe\'s AABB. If using a shader to deform the mesh in a
way that makes it go outside its AABB,
`GeometryInstance3D.extra_cull_margin<class_GeometryInstance3D_property_extra_cull_margin>`{.interpreted-text
role="ref"} must be increased on the mesh. Otherwise, the reflection
probe may not be visible on the mesh.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Reflection probes <../tutorials/3d/global_illumination/reflection_probes>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_ReflectionProbe_UpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **UpdateMode**:
`🔗<enum_ReflectionProbe_UpdateMode>`{.interpreted-text role="ref"}

:::: {#class_ReflectionProbe_constant_UPDATE_ONCE}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_ReflectionProbe_UpdateMode>`{.interpreted-text
role="ref"} **UPDATE_ONCE** = `0`

Update the probe once on the next frame (recommended for most objects).
The corresponding radiance map will be generated over the following six
frames. This takes more time to update than
`UPDATE_ALWAYS<class_ReflectionProbe_constant_UPDATE_ALWAYS>`{.interpreted-text
role="ref"}, but it has a lower performance cost and can result in
higher-quality reflections. The ReflectionProbe is updated when its
transform changes, but not when nearby geometry changes. You can force a
**ReflectionProbe** update by moving the **ReflectionProbe** slightly in
any direction.

:::: {#class_ReflectionProbe_constant_UPDATE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_ReflectionProbe_UpdateMode>`{.interpreted-text
role="ref"} **UPDATE_ALWAYS** = `1`

Update the probe every frame. This provides better results for
fast-moving dynamic objects (such as cars). However, it has a
significant performance cost. Due to the cost, it\'s recommended to only
use one ReflectionProbe with
`UPDATE_ALWAYS<class_ReflectionProbe_constant_UPDATE_ALWAYS>`{.interpreted-text
role="ref"} at most per scene. For all other use cases, use
`UPDATE_ONCE<class_ReflectionProbe_constant_UPDATE_ONCE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ReflectionProbe_AmbientMode}
::: rst-class
classref-enumeration
:::
::::

enum **AmbientMode**:
`🔗<enum_ReflectionProbe_AmbientMode>`{.interpreted-text role="ref"}

:::: {#class_ReflectionProbe_constant_AMBIENT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AmbientMode<enum_ReflectionProbe_AmbientMode>`{.interpreted-text
role="ref"} **AMBIENT_DISABLED** = `0`

Do not apply any ambient lighting inside the **ReflectionProbe**\'s box
defined by its
`size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}.

:::: {#class_ReflectionProbe_constant_AMBIENT_ENVIRONMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`AmbientMode<enum_ReflectionProbe_AmbientMode>`{.interpreted-text
role="ref"} **AMBIENT_ENVIRONMENT** = `1`

Apply automatically-sourced environment lighting inside the
**ReflectionProbe**\'s box defined by its
`size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}.

:::: {#class_ReflectionProbe_constant_AMBIENT_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`AmbientMode<enum_ReflectionProbe_AmbientMode>`{.interpreted-text
role="ref"} **AMBIENT_COLOR** = `2`

Apply custom ambient lighting inside the **ReflectionProbe**\'s box
defined by its
`size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}. See
`ambient_color<class_ReflectionProbe_property_ambient_color>`{.interpreted-text
role="ref"} and
`ambient_color_energy<class_ReflectionProbe_property_ambient_color_energy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ReflectionProbe_property_ambient_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **ambient_color** =
`Color(0, 0, 0, 1)`
`🔗<class_ReflectionProbe_property_ambient_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ambient_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_ambient_color**()

The custom ambient color to use within the **ReflectionProbe**\'s box
defined by its
`size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}. Only effective if
`ambient_mode<class_ReflectionProbe_property_ambient_mode>`{.interpreted-text
role="ref"} is
`AMBIENT_COLOR<class_ReflectionProbe_constant_AMBIENT_COLOR>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_ambient_color_energy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**ambient_color_energy** = `1.0`
`🔗<class_ReflectionProbe_property_ambient_color_energy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ambient_color_energy**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_ambient_color_energy**()

The custom ambient color energy to use within the **ReflectionProbe**\'s
box defined by its
`size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}. Only effective if
`ambient_mode<class_ReflectionProbe_property_ambient_mode>`{.interpreted-text
role="ref"} is
`AMBIENT_COLOR<class_ReflectionProbe_constant_AMBIENT_COLOR>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_ambient_mode}
::: rst-class
classref-property
:::
::::

`AmbientMode<enum_ReflectionProbe_AmbientMode>`{.interpreted-text
role="ref"} **ambient_mode** = `1`
`🔗<class_ReflectionProbe_property_ambient_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ambient_mode**(value:
  `AmbientMode<enum_ReflectionProbe_AmbientMode>`{.interpreted-text
  role="ref"})
- `AmbientMode<enum_ReflectionProbe_AmbientMode>`{.interpreted-text
  role="ref"} **get_ambient_mode**()

The ambient color to use within the **ReflectionProbe**\'s box defined
by its `size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}. The ambient color will smoothly blend with other
**ReflectionProbe**s and the rest of the scene (outside the
**ReflectionProbe**\'s box defined by its
`size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_blend_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **blend_distance** =
`1.0`
`🔗<class_ReflectionProbe_property_blend_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_blend_distance**()

Defines the distance in meters over which a probe blends into the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_box_projection}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **box_projection** =
`false`
`🔗<class_ReflectionProbe_property_box_projection>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_box_projection**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_box_projection_enabled**()

If `true`, enables box projection. This makes reflections look more
correct in rectangle-shaped rooms by offsetting the reflection center
depending on the camera\'s location.

\*\*Note:\*\* To better fit rectangle-shaped rooms that are not aligned
to the grid, you can rotate the **ReflectionProbe** node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **cull_mask** = `1048575`
`🔗<class_ReflectionProbe_property_cull_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cull_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_cull_mask**()

Sets the cull mask which determines what objects are drawn by this
probe. Every
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
with a layer included in this cull mask will be rendered by the probe.
It is best to only include large objects which are likely to take up a
lot of space in the reflection in order to save on rendering cost.

This can also be used to prevent an object from reflecting upon itself
(for instance, a **ReflectionProbe** centered on a vehicle).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_enable_shadows}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_shadows** =
`false`
`🔗<class_ReflectionProbe_property_enable_shadows>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_shadows**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **are_shadows_enabled**()

If `true`, computes shadows in the reflection probe. This makes the
reflection probe slower to render; you may want to disable this if using
the
`UPDATE_ALWAYS<class_ReflectionProbe_constant_UPDATE_ALWAYS>`{.interpreted-text
role="ref"}
`update_mode<class_ReflectionProbe_property_update_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_intensity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **intensity** = `1.0`
`🔗<class_ReflectionProbe_property_intensity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_intensity**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_intensity**()

Defines the reflection intensity. Intensity modulates the strength of
the reflection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_interior}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **interior** = `false`
`🔗<class_ReflectionProbe_property_interior>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_interior**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_set_as_interior**()

If `true`, reflections will ignore sky contribution.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_max_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **max_distance** =
`0.0`
`🔗<class_ReflectionProbe_property_max_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_max_distance**()

The maximum distance away from the **ReflectionProbe** an object can be
before it is culled. Decrease this to improve performance, especially
when using the
`UPDATE_ALWAYS<class_ReflectionProbe_constant_UPDATE_ALWAYS>`{.interpreted-text
role="ref"}
`update_mode<class_ReflectionProbe_property_update_mode>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The maximum reflection distance is always at least equal
to the probe\'s extents. This means that decreasing
`max_distance<class_ReflectionProbe_property_max_distance>`{.interpreted-text
role="ref"} will not always cull objects from reflections, especially if
the reflection probe\'s box defined by its
`size<class_ReflectionProbe_property_size>`{.interpreted-text
role="ref"} is already large.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_mesh_lod_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**mesh_lod_threshold** = `1.0`
`🔗<class_ReflectionProbe_property_mesh_lod_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh_lod_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_mesh_lod_threshold**()

The automatic LOD bias to use for meshes rendered within the
**ReflectionProbe** (this is analog to
`Viewport.mesh_lod_threshold<class_Viewport_property_mesh_lod_threshold>`{.interpreted-text
role="ref"}). Higher values will use less detailed versions of meshes
that have LOD variations generated. If set to `0.0`, automatic LOD is
disabled. Increase
`mesh_lod_threshold<class_ReflectionProbe_property_mesh_lod_threshold>`{.interpreted-text
role="ref"} to improve performance at the cost of geometry detail,
especially when using the
`UPDATE_ALWAYS<class_ReflectionProbe_constant_UPDATE_ALWAYS>`{.interpreted-text
role="ref"}
`update_mode<class_ReflectionProbe_property_update_mode>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`mesh_lod_threshold<class_ReflectionProbe_property_mesh_lod_threshold>`{.interpreted-text
role="ref"} does not affect
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} visibility ranges (also known as \"manual\" LOD or
hierarchical LOD).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_origin_offset}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **origin_offset**
= `Vector3(0, 0, 0)`
`🔗<class_ReflectionProbe_property_origin_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_origin_offset**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_origin_offset**()

Sets the origin offset to be used when this **ReflectionProbe** is in
`box_projection<class_ReflectionProbe_property_box_projection>`{.interpreted-text
role="ref"} mode. This can be set to a non-zero value to ensure a
reflection fits a rectangle-shaped room, while reducing the number of
objects that \"get in the way\" of the reflection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_reflection_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **reflection_mask** =
`1048575`
`🔗<class_ReflectionProbe_property_reflection_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_reflection_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_reflection_mask**()

Sets the reflection mask which determines what objects have reflections
applied from this probe. Every
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
with a layer included in this reflection mask will have reflections
applied from this probe. See also
`cull_mask<class_ReflectionProbe_property_cull_mask>`{.interpreted-text
role="ref"}, which can be used to exclude objects from appearing in the
reflection while still making them affected by the **ReflectionProbe**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(20, 20, 20)`
`🔗<class_ReflectionProbe_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The size of the reflection probe. The larger the size, the more space
covered by the probe, which will lower the perceived resolution. It is
best to keep the size only as large as you need it.

\*\*Note:\*\* To better fit areas that are not aligned to the grid, you
can rotate the **ReflectionProbe** node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ReflectionProbe_property_update_mode}
::: rst-class
classref-property
:::
::::

`UpdateMode<enum_ReflectionProbe_UpdateMode>`{.interpreted-text
role="ref"} **update_mode** = `0`
`🔗<class_ReflectionProbe_property_update_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_update_mode**(value:
  `UpdateMode<enum_ReflectionProbe_UpdateMode>`{.interpreted-text
  role="ref"})
- `UpdateMode<enum_ReflectionProbe_UpdateMode>`{.interpreted-text
  role="ref"} **get_update_mode**()

Sets how frequently the **ReflectionProbe** is updated. Can be
`UPDATE_ONCE<class_ReflectionProbe_constant_UPDATE_ONCE>`{.interpreted-text
role="ref"} or
`UPDATE_ALWAYS<class_ReflectionProbe_constant_UPDATE_ALWAYS>`{.interpreted-text
role="ref"}.
