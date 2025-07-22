github_url
:   hide

# XRInterface {#class_XRInterface}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`MobileVRInterface<class_MobileVRInterface>`{.interpreted-text
role="ref"}, `OpenXRInterface<class_OpenXRInterface>`{.interpreted-text
role="ref"}, `WebXRInterface<class_WebXRInterface>`{.interpreted-text
role="ref"},
`XRInterfaceExtension<class_XRInterfaceExtension>`{.interpreted-text
role="ref"}

Base class for an XR interface implementation.

::: rst-class
classref-introduction-group
:::

## Description

This class needs to be implemented to make an AR or VR platform
available to Godot and these should be implemented as C++ modules or
GDExtension modules. Part of the interface is exposed to GDScript so you
can detect, enable and configure an AR or VR platform.

Interfaces should be written in such a way that simply enabling them
will give us a working setup. You can query the available interfaces
through `XRServer<class_XRServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `XR documentation index <../tutorials/xr/index>`{.interpreted-text
  role="doc"}

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

## Signals

:::: {#class_XRInterface_signal_play_area_changed}
::: rst-class
classref-signal
:::
::::

**play_area_changed**(mode: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_XRInterface_signal_play_area_changed>`{.interpreted-text
role="ref"}

Emitted when the play area is changed. This can be a result of the
player resetting the boundary or entering a new play area, the player
changing the play area mode, the world scale changing or the player
resetting their headset orientation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_XRInterface_Capabilities}
::: rst-class
classref-enumeration
:::
::::

enum **Capabilities**:
`🔗<enum_XRInterface_Capabilities>`{.interpreted-text role="ref"}

:::: {#class_XRInterface_constant_XR_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} **XR_NONE** = `0`

No XR capabilities.

:::: {#class_XRInterface_constant_XR_MONO}
::: rst-class
classref-enumeration-constant
:::
::::

`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} **XR_MONO** = `1`

This interface can work with normal rendering output (non-HMD based AR).

:::: {#class_XRInterface_constant_XR_STEREO}
::: rst-class
classref-enumeration-constant
:::
::::

`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} **XR_STEREO** = `2`

This interface supports stereoscopic rendering.

:::: {#class_XRInterface_constant_XR_QUAD}
::: rst-class
classref-enumeration-constant
:::
::::

`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} **XR_QUAD** = `4`

This interface supports quad rendering (not yet supported by Godot).

:::: {#class_XRInterface_constant_XR_VR}
::: rst-class
classref-enumeration-constant
:::
::::

`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} **XR_VR** = `8`

This interface supports VR.

:::: {#class_XRInterface_constant_XR_AR}
::: rst-class
classref-enumeration-constant
:::
::::

`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} **XR_AR** = `16`

This interface supports AR (video background and real world tracking).

:::: {#class_XRInterface_constant_XR_EXTERNAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} **XR_EXTERNAL** = `32`

This interface outputs to an external device. If the main viewport is
used, the on screen output is an unmodified buffer of either the left or
right eye (stretched if the viewport size is not changed to the same
aspect ratio of
`get_render_target_size()<class_XRInterface_method_get_render_target_size>`{.interpreted-text
role="ref"}). Using a separate viewport node frees up the main viewport
for other purposes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRInterface_TrackingStatus}
::: rst-class
classref-enumeration
:::
::::

enum **TrackingStatus**:
`🔗<enum_XRInterface_TrackingStatus>`{.interpreted-text role="ref"}

:::: {#class_XRInterface_constant_XR_NORMAL_TRACKING}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} **XR_NORMAL_TRACKING** = `0`

Tracking is behaving as expected.

:::: {#class_XRInterface_constant_XR_EXCESSIVE_MOTION}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} **XR_EXCESSIVE_MOTION** = `1`

Tracking is hindered by excessive motion (the player is moving faster
than tracking can keep up).

:::: {#class_XRInterface_constant_XR_INSUFFICIENT_FEATURES}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} **XR_INSUFFICIENT_FEATURES** = `2`

Tracking is hindered by insufficient features, it\'s too dark (for
camera-based tracking), player is blocked, etc.

:::: {#class_XRInterface_constant_XR_UNKNOWN_TRACKING}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} **XR_UNKNOWN_TRACKING** = `3`

We don\'t know the status of the tracking or this interface does not
provide feedback.

:::: {#class_XRInterface_constant_XR_NOT_TRACKING}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} **XR_NOT_TRACKING** = `4`

Tracking is not functional (camera not plugged in or obscured,
lighthouses turned off, etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRInterface_PlayAreaMode}
::: rst-class
classref-enumeration
:::
::::

enum **PlayAreaMode**:
`🔗<enum_XRInterface_PlayAreaMode>`{.interpreted-text role="ref"}

:::: {#class_XRInterface_constant_XR_PLAY_AREA_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **XR_PLAY_AREA_UNKNOWN** = `0`

Play area mode not set or not available.

:::: {#class_XRInterface_constant_XR_PLAY_AREA_3DOF}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **XR_PLAY_AREA_3DOF** = `1`

Play area only supports orientation tracking, no positional tracking,
area will center around player.

:::: {#class_XRInterface_constant_XR_PLAY_AREA_SITTING}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **XR_PLAY_AREA_SITTING** = `2`

Player is in seated position, limited positional tracking, fixed
guardian around player.

:::: {#class_XRInterface_constant_XR_PLAY_AREA_ROOMSCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **XR_PLAY_AREA_ROOMSCALE** = `3`

Player is free to move around, full positional tracking.

:::: {#class_XRInterface_constant_XR_PLAY_AREA_STAGE}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **XR_PLAY_AREA_STAGE** = `4`

Same as
`XR_PLAY_AREA_ROOMSCALE<class_XRInterface_constant_XR_PLAY_AREA_ROOMSCALE>`{.interpreted-text
role="ref"} but origin point is fixed to the center of the physical
space. In this mode, system-level recentering may be disabled, requiring
the use of
`XRServer.center_on_hmd()<class_XRServer_method_center_on_hmd>`{.interpreted-text
role="ref"}.

:::: {#class_XRInterface_constant_XR_PLAY_AREA_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **XR_PLAY_AREA_CUSTOM** = `2147483647`

Custom play area set by a GDExtension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRInterface_EnvironmentBlendMode}
::: rst-class
classref-enumeration
:::
::::

enum **EnvironmentBlendMode**:
`🔗<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
role="ref"}

:::: {#class_XRInterface_constant_XR_ENV_BLEND_MODE_OPAQUE}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
role="ref"} **XR_ENV_BLEND_MODE_OPAQUE** = `0`

Opaque blend mode. This is typically used for VR devices.

:::: {#class_XRInterface_constant_XR_ENV_BLEND_MODE_ADDITIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
role="ref"} **XR_ENV_BLEND_MODE_ADDITIVE** = `1`

Additive blend mode. This is typically used for AR devices or VR devices
with passthrough.

:::: {#class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND}
::: rst-class
classref-enumeration-constant
:::
::::

`EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
role="ref"} **XR_ENV_BLEND_MODE_ALPHA_BLEND** = `2`

Alpha blend mode. This is typically used for AR or VR devices with
passthrough capabilities. The alpha channel controls how much of the
passthrough is visible. Alpha of 0.0 means the passthrough is visible
and this pixel works in ADDITIVE mode. Alpha of 1.0 means that the
passthrough is not visible and this pixel works in OPAQUE mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRInterface_VRSTextureFormat}
::: rst-class
classref-enumeration
:::
::::

enum **VRSTextureFormat**:
`🔗<enum_XRInterface_VRSTextureFormat>`{.interpreted-text role="ref"}

:::: {#class_XRInterface_constant_XR_VRS_TEXTURE_FORMAT_UNIFIED}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSTextureFormat<enum_XRInterface_VRSTextureFormat>`{.interpreted-text
role="ref"} **XR_VRS_TEXTURE_FORMAT_UNIFIED** = `0`

The texture format is the same as returned by
`XRVRS.make_vrs_texture()<class_XRVRS_method_make_vrs_texture>`{.interpreted-text
role="ref"}.

:::: {#class_XRInterface_constant_XR_VRS_TEXTURE_FORMAT_FRAGMENT_SHADING_RATE}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSTextureFormat<enum_XRInterface_VRSTextureFormat>`{.interpreted-text
role="ref"} **XR_VRS_TEXTURE_FORMAT_FRAGMENT_SHADING_RATE** = `1`

The texture format is the same as expected by the Vulkan
`VK_KHR_fragment_shading_rate` extension.

:::: {#class_XRInterface_constant_XR_VRS_TEXTURE_FORMAT_FRAGMENT_DENSITY_MAP}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSTextureFormat<enum_XRInterface_VRSTextureFormat>`{.interpreted-text
role="ref"} **XR_VRS_TEXTURE_FORMAT_FRAGMENT_DENSITY_MAP** = `2`

The texture format is the same as expected by the Vulkan
`VK_EXT_fragment_density_map` extension.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRInterface_property_ar_is_anchor_detection_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**ar_is_anchor_detection_enabled** = `false`
`🔗<class_XRInterface_property_ar_is_anchor_detection_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_anchor_detection_is_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_anchor_detection_is_enabled**()

On an AR interface, `true` if anchor detection is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_property_environment_blend_mode}
::: rst-class
classref-property
:::
::::

`EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
role="ref"} **environment_blend_mode** = `0`
`🔗<class_XRInterface_property_environment_blend_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `bool<class_bool>`{.interpreted-text role="ref"}
  **set_environment_blend_mode**(mode:
  `EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
  role="ref"})
- `EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
  role="ref"} **get_environment_blend_mode**()

Specify how XR should blend in the environment. This is specific to
certain AR and passthrough devices where camera images are blended in by
the XR compositor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_property_interface_is_primary}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface_is_primary** = `false`
`🔗<class_XRInterface_property_interface_is_primary>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_primary**()

`true` if this is the primary interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_property_xr_play_area_mode}
::: rst-class
classref-property
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **xr_play_area_mode** = `0`
`🔗<class_XRInterface_property_xr_play_area_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `bool<class_bool>`{.interpreted-text role="ref"}
  **set_play_area_mode**(mode:
  `PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
  role="ref"})
- `PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
  role="ref"} **get_play_area_mode**()

The play area mode for this interface.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRInterface_method_get_camera_feed_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_camera_feed_id**()
`🔗<class_XRInterface_method_get_camera_feed_id>`{.interpreted-text
role="ref"}

If this is an AR interface that requires displaying a camera feed as the
background, this method returns the feed ID in the
`CameraServer<class_CameraServer>`{.interpreted-text role="ref"} for
this interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_capabilities}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_capabilities**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterface_method_get_capabilities>`{.interpreted-text
role="ref"}

Returns a combination of
`Capabilities<enum_XRInterface_Capabilities>`{.interpreted-text
role="ref"} flags providing information about the capabilities of this
interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_XRInterface_method_get_name>`{.interpreted-text
role="ref"}

Returns the name of this interface (`"OpenXR"`, `"OpenVR"`, `"OpenHMD"`,
`"ARKit"`, etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_play_area}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **get_play_area**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterface_method_get_play_area>`{.interpreted-text
role="ref"}

Returns an array of vectors that represent the physical play area mapped
to the virtual space around the
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"} point. The
points form a convex polygon that can be used to react to or visualize
the play area. This returns an empty array if this feature is not
supported or if the information is not yet available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_projection_for_view}
::: rst-class
classref-method
:::
::::

`Projection<class_Projection>`{.interpreted-text role="ref"}
**get_projection_for_view**(view: `int<class_int>`{.interpreted-text
role="ref"}, aspect: `float<class_float>`{.interpreted-text role="ref"},
near: `float<class_float>`{.interpreted-text role="ref"}, far:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRInterface_method_get_projection_for_view>`{.interpreted-text
role="ref"}

Returns the projection matrix for a view/eye.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_render_target_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_render_target_size**()
`🔗<class_XRInterface_method_get_render_target_size>`{.interpreted-text
role="ref"}

Returns the resolution at which we should render our intermediate
results before things like lens distortion are applied by the VR
platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_supported_environment_blend_modes}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_supported_environment_blend_modes**()
`🔗<class_XRInterface_method_get_supported_environment_blend_modes>`{.interpreted-text
role="ref"}

Returns the an array of supported environment blend modes, see
`EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_system_info}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_system_info**()
`🔗<class_XRInterface_method_get_system_info>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
with extra system info. Interfaces are expected to return
`XRRuntimeName` and `XRRuntimeVersion` providing info about the used XR
runtime. Additional entries may be provided specific to an interface.

\*\*Note:\*\*This information may only be available after
`initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} was successfully called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_tracking_status}
::: rst-class
classref-method
:::
::::

`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} **get_tracking_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterface_method_get_tracking_status>`{.interpreted-text
role="ref"}

If supported, returns the status of our tracking. This will allow you to
provide feedback to the user whether there are issues with positional
tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_transform_for_view}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_transform_for_view**(view: `int<class_int>`{.interpreted-text
role="ref"}, cam_transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`🔗<class_XRInterface_method_get_transform_for_view>`{.interpreted-text
role="ref"}

Returns the transform for a view/eye.

`view` is the view/eye index.

`cam_transform` is the transform that maps device coordinates to scene
coordinates, typically the
`Node3D.global_transform<class_Node3D_property_global_transform>`{.interpreted-text
role="ref"} of the current XROrigin3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_get_view_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_view_count**()
`🔗<class_XRInterface_method_get_view_count>`{.interpreted-text
role="ref"}

Returns the number of views that need to be rendered for this device. 1
for Monoscopic, 2 for Stereoscopic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_initialize}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **initialize**()
`🔗<class_XRInterface_method_initialize>`{.interpreted-text role="ref"}

Call this to initialize this interface. The first interface that is
initialized is identified as the primary interface and it will be used
for rendering output.

After initializing the interface you want to use you then need to enable
the AR/VR mode of a viewport and rendering should commence.

\*\*Note:\*\* You must enable the XR mode on the main viewport for any
device that uses the main output of Godot, such as for mobile VR.

If you do this for a platform that handles its own output (such as
OpenVR) Godot will show just one eye without distortion on screen.
Alternatively, you can add a separate viewport node to your scene and
enable AR/VR on that viewport. It will be used to output to the HMD,
leaving you free to do anything you like in the main window, such as
using a separate camera as a spectator camera or rendering something
completely different.

While currently not used, you can activate additional interfaces. You
may wish to do this if you want to track controllers from other
platforms. However, at this point in time only one interface can render
to an HMD.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_is_initialized}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_initialized**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterface_method_is_initialized>`{.interpreted-text
role="ref"}

Returns `true` if this interface has been initialized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_is_passthrough_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_passthrough_enabled**()
`🔗<class_XRInterface_method_is_passthrough_enabled>`{.interpreted-text
role="ref"}

**Deprecated:** Check if
`environment_blend_mode<class_XRInterface_property_environment_blend_mode>`{.interpreted-text
role="ref"} is
`XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"}, instead.

Returns `true` if passthrough is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_is_passthrough_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_passthrough_supported**()
`🔗<class_XRInterface_method_is_passthrough_supported>`{.interpreted-text
role="ref"}

**Deprecated:** Check that
`XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"} is supported using
`get_supported_environment_blend_modes()<class_XRInterface_method_get_supported_environment_blend_modes>`{.interpreted-text
role="ref"}, instead.

Returns `true` if this interface supports passthrough.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_set_environment_blend_mode}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**set_environment_blend_mode**(mode:
`EnvironmentBlendMode<enum_XRInterface_EnvironmentBlendMode>`{.interpreted-text
role="ref"})
`🔗<class_XRInterface_method_set_environment_blend_mode>`{.interpreted-text
role="ref"}

Sets the active environment blend mode.

`mode` is the environment blend mode starting with the next frame.

\*\*Note:\*\* Not all runtimes support all environment blend modes, so
it is important to check this at startup. For example:

    func _ready():
        var xr_interface = XRServer.find_interface("OpenXR")
        if xr_interface and xr_interface.is_initialized():
            var vp = get_viewport()
            vp.use_xr = true
            var acceptable_modes = [XRInterface.XR_ENV_BLEND_MODE_OPAQUE, XRInterface.XR_ENV_BLEND_MODE_ADDITIVE]
            var modes = xr_interface.get_supported_environment_blend_modes()
            for mode in acceptable_modes:
                if mode in modes:
                    xr_interface.set_environment_blend_mode(mode)
                    break

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_set_play_area_mode}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**set_play_area_mode**(mode:
`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"})
`🔗<class_XRInterface_method_set_play_area_mode>`{.interpreted-text
role="ref"}

Sets the active play area mode, will return `false` if the mode can\'t
be used with this interface.

\*\*Note:\*\* Changing this after the interface has already been
initialized can be jarring for the player, so it\'s recommended to
recenter on the HMD with
`XRServer.center_on_hmd()<class_XRServer_method_center_on_hmd>`{.interpreted-text
role="ref"} (if switching to
`XR_PLAY_AREA_STAGE<class_XRInterface_constant_XR_PLAY_AREA_STAGE>`{.interpreted-text
role="ref"}) or make the switch during a scene change.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_start_passthrough}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **start_passthrough**()
`🔗<class_XRInterface_method_start_passthrough>`{.interpreted-text
role="ref"}

**Deprecated:** Set the
`environment_blend_mode<class_XRInterface_property_environment_blend_mode>`{.interpreted-text
role="ref"} to
`XR_ENV_BLEND_MODE_ALPHA_BLEND<class_XRInterface_constant_XR_ENV_BLEND_MODE_ALPHA_BLEND>`{.interpreted-text
role="ref"}, instead.

Starts passthrough, will return `false` if passthrough couldn\'t be
started.

\*\*Note:\*\* The viewport used for XR must have a transparent
background, otherwise passthrough may not properly render.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_stop_passthrough}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**stop_passthrough**()
`🔗<class_XRInterface_method_stop_passthrough>`{.interpreted-text
role="ref"}

**Deprecated:** Set the
`environment_blend_mode<class_XRInterface_property_environment_blend_mode>`{.interpreted-text
role="ref"} to
`XR_ENV_BLEND_MODE_OPAQUE<class_XRInterface_constant_XR_ENV_BLEND_MODE_OPAQUE>`{.interpreted-text
role="ref"}, instead.

Stops passthrough.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_supports_play_area_mode}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**supports_play_area_mode**(mode:
`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"})
`🔗<class_XRInterface_method_supports_play_area_mode>`{.interpreted-text
role="ref"}

Call this to find out if a given play area mode is supported by this
interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_trigger_haptic_pulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**trigger_haptic_pulse**(action_name:
`String<class_String>`{.interpreted-text role="ref"}, tracker_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, frequency:
`float<class_float>`{.interpreted-text role="ref"}, amplitude:
`float<class_float>`{.interpreted-text role="ref"}, duration_sec:
`float<class_float>`{.interpreted-text role="ref"}, delay_sec:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRInterface_method_trigger_haptic_pulse>`{.interpreted-text
role="ref"}

Triggers a haptic pulse on a device associated with this interface.

`action_name` is the name of the action for this pulse.

`tracker_name` is optional and can be used to direct the pulse to a
specific device provided that device is bound to this haptic.

`frequency` is the frequency of the pulse, set to `0.0` to have the
system use a default frequency.

`amplitude` is the amplitude of the pulse between `0.0` and `1.0`.

`duration_sec` is the duration of the pulse in seconds.

`delay_sec` is a delay in seconds before the pulse is given.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterface_method_uninitialize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**uninitialize**()
`🔗<class_XRInterface_method_uninitialize>`{.interpreted-text
role="ref"}

Turns the interface off.
