github_url
:   hide

# XRInterfaceExtension {#class_XRInterfaceExtension}

**Inherits:** `XRInterface<class_XRInterface>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base class for XR interface extensions (plugins).

::: rst-class
classref-introduction-group
:::

## Description

External XR interface plugins should inherit from this class.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `XR documentation index <../tutorials/xr/index>`{.interpreted-text
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

:::: {#class_XRInterfaceExtension_private_method__end_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_end_frame**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__end_frame>`{.interpreted-text
role="ref"}

Called if interface is active and queues have been submitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_anchor_detection_is_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_get_anchor_detection_is_enabled**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_anchor_detection_is_enabled>`{.interpreted-text
role="ref"}

Return `true` if anchor detection is enabled for this interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_camera_feed_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_get_camera_feed_id**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_camera_feed_id>`{.interpreted-text
role="ref"}

Returns the camera feed ID for the
`CameraFeed<class_CameraFeed>`{.interpreted-text role="ref"} registered
with the `CameraServer<class_CameraServer>`{.interpreted-text
role="ref"} that should be presented as the background on an AR capable
device (if applicable).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_camera_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_get_camera_transform**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_camera_transform>`{.interpreted-text
role="ref"}

Returns the `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} that positions the
`XRCamera3D<class_XRCamera3D>`{.interpreted-text role="ref"} in the
world.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_capabilities}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_capabilities**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_capabilities>`{.interpreted-text
role="ref"}

Returns the capabilities of this interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_color_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_get_color_texture**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_color_texture>`{.interpreted-text
role="ref"}

Return color texture into which to render (if applicable).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_depth_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_get_depth_texture**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_depth_texture>`{.interpreted-text
role="ref"}

Return depth texture into which to render (if applicable).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_name}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**\_get_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_name>`{.interpreted-text
role="ref"}

Returns the name of this interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_play_area}
::: rst-class
classref-method
:::
::::

`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} **\_get_play_area**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_play_area>`{.interpreted-text
role="ref"}

Returns a
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"} that represents the play areas boundaries (if applicable).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_play_area_mode}
::: rst-class
classref-method
:::
::::

`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"} **\_get_play_area_mode**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_play_area_mode>`{.interpreted-text
role="ref"}

Returns the play area mode that sets up our play area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_projection_for_view}
::: rst-class
classref-method
:::
::::

`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"} **\_get_projection_for_view**(view:
`int<class_int>`{.interpreted-text role="ref"}, aspect:
`float<class_float>`{.interpreted-text role="ref"}, z_near:
`float<class_float>`{.interpreted-text role="ref"}, z_far:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_projection_for_view>`{.interpreted-text
role="ref"}

Returns the projection matrix for the given view as a
`PackedFloat64Array<class_PackedFloat64Array>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_render_target_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**\_get_render_target_size**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_render_target_size>`{.interpreted-text
role="ref"}

Returns the size of our render target for this interface, this overrides
the size of the `Viewport<class_Viewport>`{.interpreted-text role="ref"}
marked as the xr viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_suggested_pose_names}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_suggested_pose_names**(tracker_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_suggested_pose_names>`{.interpreted-text
role="ref"}

Returns a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} with pose names configured by this interface. Note that user
configuration can override this list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_suggested_tracker_names}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_suggested_tracker_names**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_suggested_tracker_names>`{.interpreted-text
role="ref"}

Returns a `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} with tracker names configured by this interface. Note that
user configuration can override this list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_system_info}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_system_info**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_system_info>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
with system information related to this interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_tracking_status}
::: rst-class
classref-method
:::
::::

`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} **\_get_tracking_status**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_tracking_status>`{.interpreted-text
role="ref"}

Returns an
`TrackingStatus<enum_XRInterface_TrackingStatus>`{.interpreted-text
role="ref"} specifying the current status of our tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_transform_for_view}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**\_get_transform_for_view**(view: `int<class_int>`{.interpreted-text
role="ref"}, cam_transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_transform_for_view>`{.interpreted-text
role="ref"}

Returns a `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
for a given view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_velocity_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_get_velocity_texture**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_velocity_texture>`{.interpreted-text
role="ref"}

Return velocity texture into which to render (if applicable).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_view_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **\_get_view_count**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_view_count>`{.interpreted-text
role="ref"}

Returns the number of views this interface requires, 1 for mono, 2 for
stereoscopic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__get_vrs_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **\_get_vrs_texture**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_vrs_texture>`{.interpreted-text
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

:::: {#class_XRInterfaceExtension_private_method__get_vrs_texture_format}
::: rst-class
classref-method
:::
::::

`VRSTextureFormat<enum_XRInterface_VRSTextureFormat>`{.interpreted-text
role="ref"} **\_get_vrs_texture_format**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__get_vrs_texture_format>`{.interpreted-text
role="ref"}

Returns the format of the texture returned by
`_get_vrs_texture()<class_XRInterfaceExtension_private_method__get_vrs_texture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__initialize}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_initialize**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__initialize>`{.interpreted-text
role="ref"}

Initializes the interface, returns `true` on success.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__is_initialized}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_is_initialized**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__is_initialized>`{.interpreted-text
role="ref"}

Returns `true` if this interface has been initialized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__post_draw_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_post_draw_viewport**(render_target:
`RID<class_RID>`{.interpreted-text role="ref"}, screen_rect:
`Rect2<class_Rect2>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__post_draw_viewport>`{.interpreted-text
role="ref"}

Called after the XR `Viewport<class_Viewport>`{.interpreted-text
role="ref"} draw logic has completed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__pre_draw_viewport}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_pre_draw_viewport**(render_target:
`RID<class_RID>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__pre_draw_viewport>`{.interpreted-text
role="ref"}

Called if this is our primary **XRInterfaceExtension** before we start
processing a `Viewport<class_Viewport>`{.interpreted-text role="ref"}
for every active XR `Viewport<class_Viewport>`{.interpreted-text
role="ref"}, returns `true` if that viewport should be rendered. An XR
interface may return `false` if the user has taken off their headset and
we can pause rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__pre_render}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_pre_render**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__pre_render>`{.interpreted-text
role="ref"}

Called if this **XRInterfaceExtension** is active before rendering
starts. Most XR interfaces will sync tracking at this point in time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_process**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__process>`{.interpreted-text
role="ref"}

Called if this **XRInterfaceExtension** is active before our physics and
game process is called. Most XR interfaces will update its
`XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
role="ref"}s at this point in time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__set_anchor_detection_is_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_anchor_detection_is_enabled**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__set_anchor_detection_is_enabled>`{.interpreted-text
role="ref"}

Enables anchor detection on this interface if supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__set_play_area_mode}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_set_play_area_mode**(mode:
`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__set_play_area_mode>`{.interpreted-text
role="ref"}

Set the play area mode for this interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__supports_play_area_mode}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_supports_play_area_mode**(mode:
`PlayAreaMode<enum_XRInterface_PlayAreaMode>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__supports_play_area_mode>`{.interpreted-text
role="ref"}

Returns `true` if this interface supports this play area mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__trigger_haptic_pulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_trigger_haptic_pulse**(action_name:
`String<class_String>`{.interpreted-text role="ref"}, tracker_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, frequency:
`float<class_float>`{.interpreted-text role="ref"}, amplitude:
`float<class_float>`{.interpreted-text role="ref"}, duration_sec:
`float<class_float>`{.interpreted-text role="ref"}, delay_sec:
`float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__trigger_haptic_pulse>`{.interpreted-text
role="ref"}

Triggers a haptic pulse to be emitted on the specified tracker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_private_method__uninitialize}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_uninitialize**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_XRInterfaceExtension_private_method__uninitialize>`{.interpreted-text
role="ref"}

Uninitialize the interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_method_add_blit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_blit**(render_target: `RID<class_RID>`{.interpreted-text
role="ref"}, src_rect: `Rect2<class_Rect2>`{.interpreted-text
role="ref"}, dst_rect: `Rect2i<class_Rect2i>`{.interpreted-text
role="ref"}, use_layer: `bool<class_bool>`{.interpreted-text
role="ref"}, layer: `int<class_int>`{.interpreted-text role="ref"},
apply_lens_distortion: `bool<class_bool>`{.interpreted-text role="ref"},
eye_center: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, k1:
`float<class_float>`{.interpreted-text role="ref"}, k2:
`float<class_float>`{.interpreted-text role="ref"}, upscale:
`float<class_float>`{.interpreted-text role="ref"}, aspect_ratio:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRInterfaceExtension_method_add_blit>`{.interpreted-text
role="ref"}

Blits our render results to screen optionally applying lens distortion.
This can only be called while processing `_commit_views`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_method_get_color_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_color_texture**()
`🔗<class_XRInterfaceExtension_method_get_color_texture>`{.interpreted-text
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

:::: {#class_XRInterfaceExtension_method_get_depth_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_depth_texture**()
`🔗<class_XRInterfaceExtension_method_get_depth_texture>`{.interpreted-text
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

:::: {#class_XRInterfaceExtension_method_get_render_target_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_render_target_texture**(render_target:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_XRInterfaceExtension_method_get_render_target_texture>`{.interpreted-text
role="ref"}

Returns a valid `RID<class_RID>`{.interpreted-text role="ref"} for a
texture to which we should render the current frame if supported by the
interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRInterfaceExtension_method_get_velocity_texture}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_velocity_texture**()
`🔗<class_XRInterfaceExtension_method_get_velocity_texture>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this method. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::
