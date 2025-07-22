github_url
:   hide

# XRServer {#class_XRServer}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Server for AR and VR features.

::: rst-class
classref-introduction-group
:::

## Description

The AR/VR server is the heart of our Advanced and Virtual Reality
solution and handles all the processing.

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

:::: {#class_XRServer_signal_interface_added}
::: rst-class
classref-signal
:::
::::

**interface_added**(interface_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_XRServer_signal_interface_added>`{.interpreted-text
role="ref"}

Emitted when a new interface has been added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_signal_interface_removed}
::: rst-class
classref-signal
:::
::::

**interface_removed**(interface_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_XRServer_signal_interface_removed>`{.interpreted-text
role="ref"}

Emitted when an interface is removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_signal_reference_frame_changed}
::: rst-class
classref-signal
:::
::::

**reference_frame_changed**()
`🔗<class_XRServer_signal_reference_frame_changed>`{.interpreted-text
role="ref"}

Emitted when the reference frame transform changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_signal_tracker_added}
::: rst-class
classref-signal
:::
::::

**tracker_added**(tracker_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_XRServer_signal_tracker_added>`{.interpreted-text role="ref"}

Emitted when a new tracker has been added. If you don\'t use a fixed
number of controllers or if you\'re using
`XRAnchor3D<class_XRAnchor3D>`{.interpreted-text role="ref"}s for an AR
solution, it is important to react to this signal to add the appropriate
`XRController3D<class_XRController3D>`{.interpreted-text role="ref"} or
`XRAnchor3D<class_XRAnchor3D>`{.interpreted-text role="ref"} nodes
related to this new tracker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_signal_tracker_removed}
::: rst-class
classref-signal
:::
::::

**tracker_removed**(tracker_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_XRServer_signal_tracker_removed>`{.interpreted-text
role="ref"}

Emitted when a tracker is removed. You should remove any
`XRController3D<class_XRController3D>`{.interpreted-text role="ref"} or
`XRAnchor3D<class_XRAnchor3D>`{.interpreted-text role="ref"} points if
applicable. This is not mandatory, the nodes simply become inactive and
will be made active again when a new tracker becomes available (i.e. a
new controller is switched on that takes the place of the previous one).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_signal_tracker_updated}
::: rst-class
classref-signal
:::
::::

**tracker_updated**(tracker_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, type:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_XRServer_signal_tracker_updated>`{.interpreted-text
role="ref"}

Emitted when an existing tracker has been updated. This can happen if
the user switches controllers.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_XRServer_TrackerType}
::: rst-class
classref-enumeration
:::
::::

enum **TrackerType**: `🔗<enum_XRServer_TrackerType>`{.interpreted-text
role="ref"}

:::: {#class_XRServer_constant_TRACKER_HEAD}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_HEAD** = `1`

The tracker tracks the location of the player\'s head. This is usually a
location centered between the player\'s eyes. Note that for handheld AR
devices this can be the current location of the device.

:::: {#class_XRServer_constant_TRACKER_CONTROLLER}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_CONTROLLER** = `2`

The tracker tracks the location of a controller.

:::: {#class_XRServer_constant_TRACKER_BASESTATION}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_BASESTATION** = `4`

The tracker tracks the location of a base station.

:::: {#class_XRServer_constant_TRACKER_ANCHOR}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_ANCHOR** = `8`

The tracker tracks the location and size of an AR anchor.

:::: {#class_XRServer_constant_TRACKER_HAND}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_HAND** = `16`

The tracker tracks the location and joints of a hand.

:::: {#class_XRServer_constant_TRACKER_BODY}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_BODY** = `32`

The tracker tracks the location and joints of a body.

:::: {#class_XRServer_constant_TRACKER_FACE}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_FACE** = `64`

The tracker tracks the expressions of a face.

:::: {#class_XRServer_constant_TRACKER_ANY_KNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_ANY_KNOWN** = `127`

Used internally to filter trackers of any known type.

:::: {#class_XRServer_constant_TRACKER_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_UNKNOWN** = `128`

Used internally if we haven\'t set the tracker type yet.

:::: {#class_XRServer_constant_TRACKER_ANY}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**TRACKER_ANY** = `255`

Used internally to select all trackers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRServer_RotationMode}
::: rst-class
classref-enumeration
:::
::::

enum **RotationMode**:
`🔗<enum_XRServer_RotationMode>`{.interpreted-text role="ref"}

:::: {#class_XRServer_constant_RESET_FULL_ROTATION}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_XRServer_RotationMode>`{.interpreted-text role="ref"}
**RESET_FULL_ROTATION** = `0`

Fully reset the orientation of the HMD. Regardless of what direction the
user is looking to in the real world. The user will look dead ahead in
the virtual world.

:::: {#class_XRServer_constant_RESET_BUT_KEEP_TILT}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_XRServer_RotationMode>`{.interpreted-text role="ref"}
**RESET_BUT_KEEP_TILT** = `1`

Resets the orientation but keeps the tilt of the device. So if we\'re
looking down, we keep looking down but heading will be reset.

:::: {#class_XRServer_constant_DONT_RESET_ROTATION}
::: rst-class
classref-enumeration-constant
:::
::::

`RotationMode<enum_XRServer_RotationMode>`{.interpreted-text role="ref"}
**DONT_RESET_ROTATION** = `2`

Does not reset the orientation of the HMD, only the position of the
player gets centered.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRServer_property_camera_locked_to_origin}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**camera_locked_to_origin** = `false`
`🔗<class_XRServer_property_camera_locked_to_origin>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_camera_locked_to_origin**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_camera_locked_to_origin**()

If set to `true`, the scene will be rendered as if the camera is locked
to the `XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This doesn\'t provide a very comfortable experience for
users. This setting exists for doing benchmarking or automated testing,
where you want to control what is rendered via code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_property_primary_interface}
::: rst-class
classref-property
:::
::::

`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}
**primary_interface**
`🔗<class_XRServer_property_primary_interface>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_primary_interface**(value:
  `XRInterface<class_XRInterface>`{.interpreted-text role="ref"})
- `XRInterface<class_XRInterface>`{.interpreted-text role="ref"}
  **get_primary_interface**()

The primary `XRInterface<class_XRInterface>`{.interpreted-text
role="ref"} currently bound to the **XRServer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_property_world_origin}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**world_origin** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_XRServer_property_world_origin>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_world_origin**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_world_origin**()

The current origin of our tracking space in the virtual world. This is
used by the renderer to properly position the camera with new tracking
data.

\*\*Note:\*\* This property is managed by the current
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"} node. It is
exposed for access from GDExtensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_property_world_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **world_scale** =
`1.0` `🔗<class_XRServer_property_world_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_world_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_world_scale**()

The scale of the game world compared to the real world. By default, most
AR/VR platforms assume that 1 game unit corresponds to 1 real world
meter.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRServer_method_add_interface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_interface**(interface:
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"})
`🔗<class_XRServer_method_add_interface>`{.interpreted-text role="ref"}

Registers an `XRInterface<class_XRInterface>`{.interpreted-text
role="ref"} object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_add_tracker}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_tracker**(tracker: `XRTracker<class_XRTracker>`{.interpreted-text
role="ref"}) `🔗<class_XRServer_method_add_tracker>`{.interpreted-text
role="ref"}

Registers a new `XRTracker<class_XRTracker>`{.interpreted-text
role="ref"} that tracks a physical object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_center_on_hmd}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**center_on_hmd**(rotation_mode:
`RotationMode<enum_XRServer_RotationMode>`{.interpreted-text
role="ref"}, keep_height: `bool<class_bool>`{.interpreted-text
role="ref"}) `🔗<class_XRServer_method_center_on_hmd>`{.interpreted-text
role="ref"}

This is an important function to understand correctly. AR and VR
platforms all handle positioning slightly differently.

For platforms that do not offer spatial tracking, our origin point
`(0, 0, 0)` is the location of our HMD, but you have little control over
the direction the player is facing in the real world.

For platforms that do offer spatial tracking, our origin point depends
very much on the system. For OpenVR, our origin point is usually the
center of the tracking space, on the ground. For other platforms, it\'s
often the location of the tracking camera.

This method allows you to center your tracker on the location of the
HMD. It will take the current location of the HMD and use that to adjust
all your tracking data; in essence, realigning the real world to your
player\'s current position in the game world.

For this method to produce usable results, tracking information must be
available. This often takes a few frames after starting your game.

You should call this method after a few seconds have passed. For
example, when the user requests a realignment of the display holding a
designated button on a controller for a short period of time, or when
implementing a teleport mechanism.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_clear_reference_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_reference_frame**()
`🔗<class_XRServer_method_clear_reference_frame>`{.interpreted-text
role="ref"}

Clears the reference frame that was set by previous calls to
`center_on_hmd()<class_XRServer_method_center_on_hmd>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_find_interface}
::: rst-class
classref-method
:::
::::

`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}
**find_interface**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRServer_method_find_interface>`{.interpreted-text role="ref"}

Finds an interface by its `name`. For example, if your project uses
capabilities of an AR/VR platform, you can find the interface for that
platform by name and initialize it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_get_hmd_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_hmd_transform**()
`🔗<class_XRServer_method_get_hmd_transform>`{.interpreted-text
role="ref"}

Returns the primary interface\'s transformation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_get_interface}
::: rst-class
classref-method
:::
::::

`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}
**get_interface**(idx: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_XRServer_method_get_interface>`{.interpreted-text
role="ref"}

Returns the interface registered at the given `idx` index in the list of
interfaces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_get_interface_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_interface_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRServer_method_get_interface_count>`{.interpreted-text
role="ref"}

Returns the number of interfaces currently registered with the AR/VR
server. If your project supports multiple AR/VR platforms, you can look
through the available interface, and either present the user with a
selection or simply try to initialize each interface and use the first
one that returns `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_get_interfaces}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_interfaces**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRServer_method_get_interfaces>`{.interpreted-text role="ref"}

Returns a list of available interfaces the ID and name of each
interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_get_reference_frame}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_reference_frame**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRServer_method_get_reference_frame>`{.interpreted-text
role="ref"}

Returns the reference frame transform. Mostly used internally and
exposed for GDExtension build interfaces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_get_tracker}
::: rst-class
classref-method
:::
::::

`XRTracker<class_XRTracker>`{.interpreted-text role="ref"}
**get_tracker**(tracker_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_XRServer_method_get_tracker>`{.interpreted-text
role="ref"}

Returns the positional tracker with the given `tracker_name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_get_trackers}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_trackers**(tracker_types: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_XRServer_method_get_trackers>`{.interpreted-text
role="ref"}

Returns a dictionary of trackers for `tracker_types`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_remove_interface}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_interface**(interface:
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"})
`🔗<class_XRServer_method_remove_interface>`{.interpreted-text
role="ref"}

Removes this `interface`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRServer_method_remove_tracker}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_tracker**(tracker:
`XRTracker<class_XRTracker>`{.interpreted-text role="ref"})
`🔗<class_XRServer_method_remove_tracker>`{.interpreted-text role="ref"}

Removes this `tracker`.
