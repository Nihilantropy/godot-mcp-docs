github_url
:   hide

# GPUParticlesCollisionHeightField3D {#class_GPUParticlesCollisionHeightField3D}

**Inherits:**
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A real-time heightmap-shaped 3D particle collision shape affecting
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Description

A real-time heightmap-shaped 3D particle collision shape affecting
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

Heightmap shapes allow for efficiently representing collisions for
convex and concave objects with a single \"floor\" (such as terrain).
This is less flexible than
`GPUParticlesCollisionSDF3D<class_GPUParticlesCollisionSDF3D>`{.interpreted-text
role="ref"}, but it doesn\'t require a baking step.

\*\*GPUParticlesCollisionHeightField3D\*\* can also be regenerated in
real-time when it is moved, when the camera moves, or even continuously.
This makes **GPUParticlesCollisionHeightField3D** a good choice for
weather effects such as rain and snow and games with highly dynamic
geometry. However, this class is limited since heightmaps cannot
represent overhangs (e.g. indoors or caves).

\*\*Note:\*\*
`ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"} must be `true` on the
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}\'s
process material for collision to work.

\*\*Note:\*\* Particle collision only affects
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"},
not `CPUParticles3D<class_CPUParticles3D>`{.interpreted-text
role="ref"}.

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

## Enumerations

:::: {#enum_GPUParticlesCollisionHeightField3D_Resolution}
::: rst-class
classref-enumeration
:::
::::

enum **Resolution**:
`🔗<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"}

:::: {#class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_256}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_256** = `0`

Generate a 256×256 heightmap. Intended for small-scale scenes, or larger
scenes with no distant particles.

:::: {#class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_512}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_512** = `1`

Generate a 512×512 heightmap. Intended for medium-scale scenes, or
larger scenes with no distant particles.

:::: {#class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_1024}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_1024** = `2`

Generate a 1024×1024 heightmap. Intended for large scenes with distant
particles.

:::: {#class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_2048}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_2048** = `3`

Generate a 2048×2048 heightmap. Intended for very large scenes with
distant particles.

:::: {#class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_4096}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_4096** = `4`

Generate a 4096×4096 heightmap. Intended for huge scenes with distant
particles.

:::: {#class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_8192}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_8192** = `5`

Generate a 8192×8192 heightmap. Intended for gigantic scenes with
distant particles.

:::: {#class_GPUParticlesCollisionHeightField3D_constant_RESOLUTION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **RESOLUTION_MAX** = `6`

Represents the size of the
`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_GPUParticlesCollisionHeightField3D_UpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **UpdateMode**:
`🔗<enum_GPUParticlesCollisionHeightField3D_UpdateMode>`{.interpreted-text
role="ref"}

:::: {#class_GPUParticlesCollisionHeightField3D_constant_UPDATE_MODE_WHEN_MOVED}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_GPUParticlesCollisionHeightField3D_UpdateMode>`{.interpreted-text
role="ref"} **UPDATE_MODE_WHEN_MOVED** = `0`

Only update the heightmap when the
**GPUParticlesCollisionHeightField3D** node is moved, or when the camera
moves if
`follow_camera_enabled<class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled>`{.interpreted-text
role="ref"} is `true`. An update can be forced by slightly moving the
**GPUParticlesCollisionHeightField3D** in any direction, or by calling
`RenderingServer.particles_collision_height_field_update()<class_RenderingServer_method_particles_collision_height_field_update>`{.interpreted-text
role="ref"}.

:::: {#class_GPUParticlesCollisionHeightField3D_constant_UPDATE_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`UpdateMode<enum_GPUParticlesCollisionHeightField3D_UpdateMode>`{.interpreted-text
role="ref"} **UPDATE_MODE_ALWAYS** = `1`

Update the heightmap every frame. This has a significant performance
cost. This update should only be used when geometry that particles can
collide with changes significantly during gameplay.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**follow_camera_enabled** = `false`
`🔗<class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_follow_camera_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_follow_camera_enabled**()

If `true`, the **GPUParticlesCollisionHeightField3D** will follow the
current camera in global space. The
**GPUParticlesCollisionHeightField3D** does not need to be a child of
the `Camera3D<class_Camera3D>`{.interpreted-text role="ref"} node for
this to work.

Following the camera has a performance cost, as it will force the
heightmap to update whenever the camera moves. Consider lowering
`resolution<class_GPUParticlesCollisionHeightField3D_property_resolution>`{.interpreted-text
role="ref"} to improve performance if
`follow_camera_enabled<class_GPUParticlesCollisionHeightField3D_property_follow_camera_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionHeightField3D_property_heightfield_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **heightfield_mask** =
`1048575`
`🔗<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_heightfield_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_heightfield_mask**()

The visual layers to account for when updating the heightmap. Only
`MeshInstance3D<class_MeshInstance3D>`{.interpreted-text role="ref"}s
whose
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} match with this
`heightfield_mask<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"} will be included in the heightmap collision update. By
default, all 20 user-visible layers are taken into account for updating
the heightmap collision.

\*\*Note:\*\* Since the
`heightfield_mask<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"} allows for 32 layers to be stored in total, there are an
additional 12 layers that are only used internally by the engine and
aren\'t exposed in the editor. Setting
`heightfield_mask<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"} using a script allows you to toggle those reserved layers,
which can be useful for editor plugins.

To adjust
`heightfield_mask<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"} more easily using a script, use
`get_heightfield_mask_value()<class_GPUParticlesCollisionHeightField3D_method_get_heightfield_mask_value>`{.interpreted-text
role="ref"} and
`set_heightfield_mask_value()<class_GPUParticlesCollisionHeightField3D_method_set_heightfield_mask_value>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionHeightField3D_property_resolution}
::: rst-class
classref-property
:::
::::

`Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
role="ref"} **resolution** = `2`
`🔗<class_GPUParticlesCollisionHeightField3D_property_resolution>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_resolution**(value:
  `Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
  role="ref"})
- `Resolution<enum_GPUParticlesCollisionHeightField3D_Resolution>`{.interpreted-text
  role="ref"} **get_resolution**()

Higher resolutions can represent small details more accurately in large
scenes, at the cost of lower performance. If
`update_mode<class_GPUParticlesCollisionHeightField3D_property_update_mode>`{.interpreted-text
role="ref"} is
`UPDATE_MODE_ALWAYS<class_GPUParticlesCollisionHeightField3D_constant_UPDATE_MODE_ALWAYS>`{.interpreted-text
role="ref"}, consider using the lowest resolution possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionHeightField3D_property_size}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **size** =
`Vector3(2, 2, 2)`
`🔗<class_GPUParticlesCollisionHeightField3D_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_size**()

The collision heightmap\'s size in 3D units. To improve heightmap
quality,
`size<class_GPUParticlesCollisionHeightField3D_property_size>`{.interpreted-text
role="ref"} should be set as small as possible while covering the parts
of the scene you need.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionHeightField3D_property_update_mode}
::: rst-class
classref-property
:::
::::

`UpdateMode<enum_GPUParticlesCollisionHeightField3D_UpdateMode>`{.interpreted-text
role="ref"} **update_mode** = `0`
`🔗<class_GPUParticlesCollisionHeightField3D_property_update_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_update_mode**(value:
  `UpdateMode<enum_GPUParticlesCollisionHeightField3D_UpdateMode>`{.interpreted-text
  role="ref"})
- `UpdateMode<enum_GPUParticlesCollisionHeightField3D_UpdateMode>`{.interpreted-text
  role="ref"} **get_update_mode**()

The update policy to use for the generated heightmap.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GPUParticlesCollisionHeightField3D_method_get_heightfield_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_heightfield_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GPUParticlesCollisionHeightField3D_method_get_heightfield_mask_value>`{.interpreted-text
role="ref"}

Returns `true` if the specified layer of the
`heightfield_mask<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between `1` and `20`,
inclusive.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticlesCollisionHeightField3D_method_set_heightfield_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_heightfield_mask_value**(layer_number:
`int<class_int>`{.interpreted-text role="ref"}, value:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_GPUParticlesCollisionHeightField3D_method_set_heightfield_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`heightfield_mask<class_GPUParticlesCollisionHeightField3D_property_heightfield_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between `1` and `20`, inclusive.
