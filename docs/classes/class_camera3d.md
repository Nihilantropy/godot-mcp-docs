github_url
:   hide

# Camera3D {#class_Camera3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `XRCamera3D<class_XRCamera3D>`{.interpreted-text
role="ref"}

Camera node, displays from a point of view.

::: rst-class
classref-introduction-group
:::

## Description

**Camera3D** is a special node that displays what is visible from its
current location. Cameras register themselves in the nearest
`Viewport<class_Viewport>`{.interpreted-text role="ref"} node (when
ascending the tree). Only one camera can be active per viewport. If no
viewport is available ascending the tree, the camera will register in
the global viewport. In other words, a camera just provides 3D display
capabilities to a `Viewport<class_Viewport>`{.interpreted-text
role="ref"}, and, without one, a scene registered in that
`Viewport<class_Viewport>`{.interpreted-text role="ref"} (or higher
viewports) can\'t be displayed.

::: rst-class
classref-introduction-group
:::

## Tutorials

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

## Enumerations

:::: {#enum_Camera3D_ProjectionType}
::: rst-class
classref-enumeration
:::
::::

enum **ProjectionType**:
`🔗<enum_Camera3D_ProjectionType>`{.interpreted-text role="ref"}

:::: {#class_Camera3D_constant_PROJECTION_PERSPECTIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`ProjectionType<enum_Camera3D_ProjectionType>`{.interpreted-text
role="ref"} **PROJECTION_PERSPECTIVE** = `0`

Perspective projection. Objects on the screen becomes smaller when they
are far away.

:::: {#class_Camera3D_constant_PROJECTION_ORTHOGONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ProjectionType<enum_Camera3D_ProjectionType>`{.interpreted-text
role="ref"} **PROJECTION_ORTHOGONAL** = `1`

Orthogonal projection, also known as orthographic projection. Objects
remain the same size on the screen no matter how far away they are.

:::: {#class_Camera3D_constant_PROJECTION_FRUSTUM}
::: rst-class
classref-enumeration-constant
:::
::::

`ProjectionType<enum_Camera3D_ProjectionType>`{.interpreted-text
role="ref"} **PROJECTION_FRUSTUM** = `2`

Frustum projection. This mode allows adjusting
`frustum_offset<class_Camera3D_property_frustum_offset>`{.interpreted-text
role="ref"} to create \"tilted frustum\" effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Camera3D_KeepAspect}
::: rst-class
classref-enumeration
:::
::::

enum **KeepAspect**: `🔗<enum_Camera3D_KeepAspect>`{.interpreted-text
role="ref"}

:::: {#class_Camera3D_constant_KEEP_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`KeepAspect<enum_Camera3D_KeepAspect>`{.interpreted-text role="ref"}
**KEEP_WIDTH** = `0`

Preserves the horizontal aspect ratio; also known as Vert- scaling. This
is usually the best option for projects running in portrait mode, as
taller aspect ratios will benefit from a wider vertical FOV.

:::: {#class_Camera3D_constant_KEEP_HEIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`KeepAspect<enum_Camera3D_KeepAspect>`{.interpreted-text role="ref"}
**KEEP_HEIGHT** = `1`

Preserves the vertical aspect ratio; also known as Hor+ scaling. This is
usually the best option for projects running in landscape mode, as wider
aspect ratios will automatically benefit from a wider horizontal FOV.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Camera3D_DopplerTracking}
::: rst-class
classref-enumeration
:::
::::

enum **DopplerTracking**:
`🔗<enum_Camera3D_DopplerTracking>`{.interpreted-text role="ref"}

:::: {#class_Camera3D_constant_DOPPLER_TRACKING_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`DopplerTracking<enum_Camera3D_DopplerTracking>`{.interpreted-text
role="ref"} **DOPPLER_TRACKING_DISABLED** = `0`

Disables [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect)
simulation (default).

:::: {#class_Camera3D_constant_DOPPLER_TRACKING_IDLE_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`DopplerTracking<enum_Camera3D_DopplerTracking>`{.interpreted-text
role="ref"} **DOPPLER_TRACKING_IDLE_STEP** = `1`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect)
by tracking positions of objects that are changed in `_process`. Changes
in the relative velocity of this camera compared to those objects affect
how audio is perceived (changing the audio\'s
`AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>`{.interpreted-text
role="ref"}).

:::: {#class_Camera3D_constant_DOPPLER_TRACKING_PHYSICS_STEP}
::: rst-class
classref-enumeration-constant
:::
::::

`DopplerTracking<enum_Camera3D_DopplerTracking>`{.interpreted-text
role="ref"} **DOPPLER_TRACKING_PHYSICS_STEP** = `2`

Simulate [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect)
by tracking positions of objects that are changed in `_physics_process`.
Changes in the relative velocity of this camera compared to those
objects affect how audio is perceived (changing the audio\'s
`AudioStreamPlayer3D.pitch_scale<class_AudioStreamPlayer3D_property_pitch_scale>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Camera3D_property_attributes}
::: rst-class
classref-property
:::
::::

`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
**attributes**
`🔗<class_Camera3D_property_attributes>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attributes**(value:
  `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"})
- `CameraAttributes<class_CameraAttributes>`{.interpreted-text
  role="ref"} **get_attributes**()

The `CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"} to use for this camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_compositor}
::: rst-class
classref-property
:::
::::

`Compositor<class_Compositor>`{.interpreted-text role="ref"}
**compositor**
`🔗<class_Camera3D_property_compositor>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_compositor**(value:
  `Compositor<class_Compositor>`{.interpreted-text role="ref"})
- `Compositor<class_Compositor>`{.interpreted-text role="ref"}
  **get_compositor**()

The `Compositor<class_Compositor>`{.interpreted-text role="ref"} to use
for this camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **cull_mask** = `1048575`
`🔗<class_Camera3D_property_cull_mask>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cull_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_cull_mask**()

The culling mask that describes which
`VisualInstance3D.layers<class_VisualInstance3D_property_layers>`{.interpreted-text
role="ref"} are rendered by this camera. By default, all 20 user-visible
layers are rendered.

\*\*Note:\*\* Since the
`cull_mask<class_Camera3D_property_cull_mask>`{.interpreted-text
role="ref"} allows for 32 layers to be stored in total, there are an
additional 12 layers that are only used internally by the engine and
aren\'t exposed in the editor. Setting
`cull_mask<class_Camera3D_property_cull_mask>`{.interpreted-text
role="ref"} using a script allows you to toggle those reserved layers,
which can be useful for editor plugins.

To adjust
`cull_mask<class_Camera3D_property_cull_mask>`{.interpreted-text
role="ref"} more easily using a script, use
`get_cull_mask_value()<class_Camera3D_method_get_cull_mask_value>`{.interpreted-text
role="ref"} and
`set_cull_mask_value()<class_Camera3D_method_set_cull_mask_value>`{.interpreted-text
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

:::: {#class_Camera3D_property_current}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **current** = `false`
`🔗<class_Camera3D_property_current>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_current**()

If `true`, the ancestor `Viewport<class_Viewport>`{.interpreted-text
role="ref"} is currently using this camera.

If multiple cameras are in the scene, one will always be made current.
For example, if two **Camera3D** nodes are present in the scene and only
one is current, setting one camera\'s
`current<class_Camera3D_property_current>`{.interpreted-text role="ref"}
to `false` will cause the other camera to be made current.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_doppler_tracking}
::: rst-class
classref-property
:::
::::

`DopplerTracking<enum_Camera3D_DopplerTracking>`{.interpreted-text
role="ref"} **doppler_tracking** = `0`
`🔗<class_Camera3D_property_doppler_tracking>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_doppler_tracking**(value:
  `DopplerTracking<enum_Camera3D_DopplerTracking>`{.interpreted-text
  role="ref"})
- `DopplerTracking<enum_Camera3D_DopplerTracking>`{.interpreted-text
  role="ref"} **get_doppler_tracking**()

If not
`DOPPLER_TRACKING_DISABLED<class_Camera3D_constant_DOPPLER_TRACKING_DISABLED>`{.interpreted-text
role="ref"}, this camera will simulate the [Doppler
effect](https://en.wikipedia.org/wiki/Doppler_effect) for objects
changed in particular `_process` methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_environment}
::: rst-class
classref-property
:::
::::

`Environment<class_Environment>`{.interpreted-text role="ref"}
**environment**
`🔗<class_Camera3D_property_environment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment**(value:
  `Environment<class_Environment>`{.interpreted-text role="ref"})
- `Environment<class_Environment>`{.interpreted-text role="ref"}
  **get_environment**()

The `Environment<class_Environment>`{.interpreted-text role="ref"} to
use for this camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_far}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **far** = `4000.0`
`🔗<class_Camera3D_property_far>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_far**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_far**()

The distance to the far culling boundary for this camera relative to its
local Z axis. Higher values allow the camera to see further away, while
decreasing `far<class_Camera3D_property_far>`{.interpreted-text
role="ref"} can improve performance if it results in objects being
partially or fully culled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_fov}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fov** = `75.0`
`🔗<class_Camera3D_property_fov>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fov**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_fov**()

The camera\'s field of view angle (in degrees). Only applicable in
perspective mode. Since
`keep_aspect<class_Camera3D_property_keep_aspect>`{.interpreted-text
role="ref"} locks one axis,
`fov<class_Camera3D_property_fov>`{.interpreted-text role="ref"} sets
the other axis\' field of view angle.

For reference, the default vertical field of view value (`75.0`) is
equivalent to a horizontal FOV of:

- \~91.31 degrees in a 4:3 viewport
- \~101.67 degrees in a 16:10 viewport
- \~107.51 degrees in a 16:9 viewport
- \~121.63 degrees in a 21:9 viewport

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_frustum_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**frustum_offset** = `Vector2(0, 0)`
`🔗<class_Camera3D_property_frustum_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frustum_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_frustum_offset**()

The camera\'s frustum offset. This can be changed from the default to
create \"tilted frustum\" effects such as
[Y-shearing](https://zdoom.org/wiki/Y-shearing).

\*\*Note:\*\* Only effective if
`projection<class_Camera3D_property_projection>`{.interpreted-text
role="ref"} is
`PROJECTION_FRUSTUM<class_Camera3D_constant_PROJECTION_FRUSTUM>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_h_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **h_offset** = `0.0`
`🔗<class_Camera3D_property_h_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_h_offset**()

The horizontal (X) offset of the camera viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_keep_aspect}
::: rst-class
classref-property
:::
::::

`KeepAspect<enum_Camera3D_KeepAspect>`{.interpreted-text role="ref"}
**keep_aspect** = `1`
`🔗<class_Camera3D_property_keep_aspect>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_aspect_mode**(value:
  `KeepAspect<enum_Camera3D_KeepAspect>`{.interpreted-text role="ref"})
- `KeepAspect<enum_Camera3D_KeepAspect>`{.interpreted-text role="ref"}
  **get_keep_aspect_mode**()

The axis to lock during
`fov<class_Camera3D_property_fov>`{.interpreted-text
role="ref"}/`size<class_Camera3D_property_size>`{.interpreted-text
role="ref"} adjustments. Can be either
`KEEP_WIDTH<class_Camera3D_constant_KEEP_WIDTH>`{.interpreted-text
role="ref"} or
`KEEP_HEIGHT<class_Camera3D_constant_KEEP_HEIGHT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_near}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **near** = `0.05`
`🔗<class_Camera3D_property_near>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_near**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_near**()

The distance to the near culling boundary for this camera relative to
its local Z axis. Lower values allow the camera to see objects more up
close to its origin, at the cost of lower precision across the *entire*
range. Values lower than the default can lead to increased Z-fighting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_projection}
::: rst-class
classref-property
:::
::::

`ProjectionType<enum_Camera3D_ProjectionType>`{.interpreted-text
role="ref"} **projection** = `0`
`🔗<class_Camera3D_property_projection>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_projection**(value:
  `ProjectionType<enum_Camera3D_ProjectionType>`{.interpreted-text
  role="ref"})
- `ProjectionType<enum_Camera3D_ProjectionType>`{.interpreted-text
  role="ref"} **get_projection**()

The camera\'s projection mode. In
`PROJECTION_PERSPECTIVE<class_Camera3D_constant_PROJECTION_PERSPECTIVE>`{.interpreted-text
role="ref"} mode, objects\' Z distance from the camera\'s local space
scales their perceived size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **size** = `1.0`
`🔗<class_Camera3D_property_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_size**()

The camera\'s size in meters measured as the diameter of the width or
height, depending on
`keep_aspect<class_Camera3D_property_keep_aspect>`{.interpreted-text
role="ref"}. Only applicable in orthogonal and frustum modes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_property_v_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **v_offset** = `0.0`
`🔗<class_Camera3D_property_v_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_v_offset**()

The vertical (Y) offset of the camera viewport.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Camera3D_method_clear_current}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_current**(enable_next: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_Camera3D_method_clear_current>`{.interpreted-text role="ref"}

If this is the current camera, remove it from being current. If
`enable_next` is `true`, request to make the next camera current, if
any.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_get_camera_projection}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**get_camera_projection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_get_camera_projection>`{.interpreted-text
role="ref"}

Returns the projection matrix that this camera uses to render to its
associated viewport. The camera must be part of the scene tree to
function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_get_camera_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_camera_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_get_camera_rid>`{.interpreted-text role="ref"}

Returns the camera\'s RID from the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_get_camera_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_camera_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_get_camera_transform>`{.interpreted-text
role="ref"}

Returns the transform of the camera plus the vertical
(`v_offset<class_Camera3D_property_v_offset>`{.interpreted-text
role="ref"}) and horizontal
(`h_offset<class_Camera3D_property_h_offset>`{.interpreted-text
role="ref"}) offsets; and any other adjustments made to the position and
orientation of the camera by subclassed cameras such as
`XRCamera3D<class_XRCamera3D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_get_cull_mask_value}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_cull_mask_value**(layer_number: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_get_cull_mask_value>`{.interpreted-text
role="ref"}

Returns whether or not the specified layer of the
`cull_mask<class_Camera3D_property_cull_mask>`{.interpreted-text
role="ref"} is enabled, given a `layer_number` between 1 and 20.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_get_frustum}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Plane<class_Plane>`{.interpreted-text role="ref"}\]
**get_frustum**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Camera3D_method_get_frustum>`{.interpreted-text
role="ref"}

Returns the camera\'s frustum planes in world space units as an array of
`Plane<class_Plane>`{.interpreted-text role="ref"}s in the following
order: near, far, left, top, right, bottom. Not to be confused with
`frustum_offset<class_Camera3D_property_frustum_offset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_get_pyramid_shape_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_pyramid_shape_rid**()
`🔗<class_Camera3D_method_get_pyramid_shape_rid>`{.interpreted-text
role="ref"}

Returns the RID of a pyramid shape encompassing the camera\'s view
frustum, ignoring the camera\'s near plane. The tip of the pyramid
represents the position of the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_is_position_behind}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_position_behind**(world_point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_is_position_behind>`{.interpreted-text
role="ref"}

Returns `true` if the given position is behind the camera (the blue part
of the linked diagram). [See this
diagram](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/camera3d_position_frustum.png)
for an overview of position query methods.

\*\*Note:\*\* A position which returns `false` may still be outside the
camera\'s field of view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_is_position_in_frustum}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_position_in_frustum**(world_point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_is_position_in_frustum>`{.interpreted-text
role="ref"}

Returns `true` if the given position is inside the camera\'s frustum
(the green part of the linked diagram). [See this
diagram](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/camera3d_position_frustum.png)
for an overview of position query methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_make_current}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_current**()
`🔗<class_Camera3D_method_make_current>`{.interpreted-text role="ref"}

Makes this camera the current camera for the
`Viewport<class_Viewport>`{.interpreted-text role="ref"} (see class
description). If the camera node is outside the scene tree, it will
attempt to become current once it\'s added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_project_local_ray_normal}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**project_local_ray_normal**(screen_point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_project_local_ray_normal>`{.interpreted-text
role="ref"}

Returns a normal vector from the screen point location directed along
the camera. Orthogonal cameras are normalized. Perspective cameras
account for perspective, screen width/height, etc.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_project_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**project_position**(screen_point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, z_depth:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_project_position>`{.interpreted-text
role="ref"}

Returns the 3D point in world space that maps to the given 2D coordinate
in the `Viewport<class_Viewport>`{.interpreted-text role="ref"}
rectangle on a plane that is the given `z_depth` distance into the scene
away from the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_project_ray_normal}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**project_ray_normal**(screen_point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_project_ray_normal>`{.interpreted-text
role="ref"}

Returns a normal vector in world space, that is the result of projecting
a point on the `Viewport<class_Viewport>`{.interpreted-text role="ref"}
rectangle by the inverse camera projection. This is useful for casting
rays in the form of (origin, normal) for object intersection or picking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_project_ray_origin}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**project_ray_origin**(screen_point:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_project_ray_origin>`{.interpreted-text
role="ref"}

Returns a 3D position in world space, that is the result of projecting a
point on the `Viewport<class_Viewport>`{.interpreted-text role="ref"}
rectangle by the inverse camera projection. This is useful for casting
rays in the form of (origin, normal) for object intersection or picking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_set_cull_mask_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cull_mask_value**(layer_number: `int<class_int>`{.interpreted-text
role="ref"}, value: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Camera3D_method_set_cull_mask_value>`{.interpreted-text
role="ref"}

Based on `value`, enables or disables the specified layer in the
`cull_mask<class_Camera3D_property_cull_mask>`{.interpreted-text
role="ref"}, given a `layer_number` between 1 and 20.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_set_frustum}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_frustum**(size: `float<class_float>`{.interpreted-text
role="ref"}, offset: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, z_near: `float<class_float>`{.interpreted-text role="ref"},
z_far: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Camera3D_method_set_frustum>`{.interpreted-text role="ref"}

Sets the camera projection to frustum mode (see
`PROJECTION_FRUSTUM<class_Camera3D_constant_PROJECTION_FRUSTUM>`{.interpreted-text
role="ref"}), by specifying a `size`, an `offset`, and the `z_near` and
`z_far` clip planes in world space units. See also
`frustum_offset<class_Camera3D_property_frustum_offset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_set_orthogonal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_orthogonal**(size: `float<class_float>`{.interpreted-text
role="ref"}, z_near: `float<class_float>`{.interpreted-text role="ref"},
z_far: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Camera3D_method_set_orthogonal>`{.interpreted-text role="ref"}

Sets the camera projection to orthogonal mode (see
`PROJECTION_ORTHOGONAL<class_Camera3D_constant_PROJECTION_ORTHOGONAL>`{.interpreted-text
role="ref"}), by specifying a `size`, and the `z_near` and `z_far` clip
planes in world space units.

As a hint, 3D games that look 2D often use this projection, with `size`
specified in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_set_perspective}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_perspective**(fov: `float<class_float>`{.interpreted-text
role="ref"}, z_near: `float<class_float>`{.interpreted-text role="ref"},
z_far: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Camera3D_method_set_perspective>`{.interpreted-text
role="ref"}

Sets the camera projection to perspective mode (see
`PROJECTION_PERSPECTIVE<class_Camera3D_constant_PROJECTION_PERSPECTIVE>`{.interpreted-text
role="ref"}), by specifying a `fov` (field of view) angle in degrees,
and the `z_near` and `z_far` clip planes in world space units.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Camera3D_method_unproject_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**unproject_position**(world_point:
`Vector3<class_Vector3>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Camera3D_method_unproject_position>`{.interpreted-text
role="ref"}

Returns the 2D coordinate in the
`Viewport<class_Viewport>`{.interpreted-text role="ref"} rectangle that
maps to the given 3D point in world space.

\*\*Note:\*\* When using this to position GUI elements over a 3D
viewport, use
`is_position_behind()<class_Camera3D_method_is_position_behind>`{.interpreted-text
role="ref"} to prevent them from appearing if the 3D point is behind the
camera:

    # This code block is part of a script that inherits from Node3D.
    # `control` is a reference to a node inheriting from Control.
    control.visible = not get_viewport().get_camera_3d().is_position_behind(global_transform.origin)
    control.position = get_viewport().get_camera_3d().unproject_position(global_transform.origin)
