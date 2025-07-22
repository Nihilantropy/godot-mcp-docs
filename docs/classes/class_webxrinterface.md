github_url
:   hide

# WebXRInterface {#class_WebXRInterface}

**Inherits:** `XRInterface<class_XRInterface>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

XR interface using WebXR.

::: rst-class
classref-introduction-group
:::

## Description

WebXR is an open standard that allows creating VR and AR applications
that run in the web browser.

As such, this interface is only available when running in Web exports.

WebXR supports a wide range of devices, from the very capable (like
Valve Index, HTC Vive, Oculus Rift and Quest) down to the much less
capable (like Google Cardboard, Oculus Go, GearVR, or plain
smartphones).

Since WebXR is based on JavaScript, it makes extensive use of callbacks,
which means that **WebXRInterface** is forced to use signals, where
other XR interfaces would instead use functions that return a result
immediately. This makes **WebXRInterface** quite a bit more complicated
to initialize than other XR interfaces.

Here\'s the minimum code required to start an immersive VR session:

    extends Node3D

    var webxr_interface
    var vr_supported = false

    func _ready():
        # We assume this node has a button as a child.
        # This button is for the user to consent to entering immersive VR mode.
        $Button.pressed.connect(self._on_button_pressed)

        webxr_interface = XRServer.find_interface("WebXR")
        if webxr_interface:
            # WebXR uses a lot of asynchronous callbacks, so we connect to various
            # signals in order to receive them.
            webxr_interface.session_supported.connect(self._webxr_session_supported)
            webxr_interface.session_started.connect(self._webxr_session_started)
            webxr_interface.session_ended.connect(self._webxr_session_ended)
            webxr_interface.session_failed.connect(self._webxr_session_failed)

            # This returns immediately - our _webxr_session_supported() method
            # (which we connected to the "session_supported" signal above) will
            # be called sometime later to let us know if it's supported or not.
            webxr_interface.is_session_supported("immersive-vr")

    func _webxr_session_supported(session_mode, supported):
        if session_mode == 'immersive-vr':
            vr_supported = supported

    func _on_button_pressed():
        if not vr_supported:
            OS.alert("Your browser doesn't support VR")
            return

        # We want an immersive VR session, as opposed to AR ('immersive-ar') or a
        # simple 3DoF viewer ('viewer').
        webxr_interface.session_mode = 'immersive-vr'
        # 'bounded-floor' is room scale, 'local-floor' is a standing or sitting
        # experience (it puts you 1.6m above the ground if you have 3DoF headset),
        # whereas as 'local' puts you down at the XROrigin.
        # This list means it'll first try to request 'bounded-floor', then
        # fallback on 'local-floor' and ultimately 'local', if nothing else is
        # supported.
        webxr_interface.requested_reference_space_types = 'bounded-floor, local-floor, local'
        # In order to use 'local-floor' or 'bounded-floor' we must also
        # mark the features as required or optional. By including 'hand-tracking'
        # as an optional feature, it will be enabled if supported.
        webxr_interface.required_features = 'local-floor'
        webxr_interface.optional_features = 'bounded-floor, hand-tracking'

        # This will return false if we're unable to even request the session,
        # however, it can still fail asynchronously later in the process, so we
        # only know if it's really succeeded or failed when our
        # _webxr_session_started() or _webxr_session_failed() methods are called.
        if not webxr_interface.initialize():
            OS.alert("Failed to initialize")
            return

    func _webxr_session_started():
        $Button.visible = false
        # This tells Godot to start rendering to the headset.
        get_viewport().use_xr = true
        # This will be the reference space type you ultimately got, out of the
        # types that you requested above. This is useful if you want the game to
        # work a little differently in 'bounded-floor' versus 'local-floor'.
        print("Reference space type: ", webxr_interface.reference_space_type)
        # This will be the list of features that were successfully enabled
        # (except on browsers that don't support this property).
        print("Enabled features: ", webxr_interface.enabled_features)

    func _webxr_session_ended():
        $Button.visible = true
        # If the user exits immersive mode, then we tell Godot to render to the web
        # page again.
        get_viewport().use_xr = false

    func _webxr_session_failed(message):
        OS.alert("Failed to initialize: " + message)

There are a couple ways to handle \"controller\" input:

- Using `XRController3D<class_XRController3D>`{.interpreted-text
  role="ref"} nodes and their
  `XRController3D.button_pressed<class_XRController3D_signal_button_pressed>`{.interpreted-text
  role="ref"} and
  `XRController3D.button_released<class_XRController3D_signal_button_released>`{.interpreted-text
  role="ref"} signals. This is how controllers are typically handled in
  XR apps in Godot, however, this will only work with advanced VR
  controllers like the Oculus Touch or Index controllers, for example.
- Using the
  `select<class_WebXRInterface_signal_select>`{.interpreted-text
  role="ref"},
  `squeeze<class_WebXRInterface_signal_squeeze>`{.interpreted-text
  role="ref"} and related signals. This method will work for both
  advanced VR controllers, and non-traditional input sources like a tap
  on the screen, a spoken voice command or a button press on the device
  itself.

You can use both methods to allow your game or app to support a wider or
narrower set of devices and input methods, or to allow more advanced
interactions with more advanced devices.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [How to make a VR game for WebXR with Godot
  4](https://www.snopekgames.com/tutorial/2023/how-make-vr-game-webxr-godot-4)

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

:::: {#class_WebXRInterface_signal_display_refresh_rate_changed}
::: rst-class
classref-signal
:::
::::

**display_refresh_rate_changed**()
`🔗<class_WebXRInterface_signal_display_refresh_rate_changed>`{.interpreted-text
role="ref"}

Emitted after the display\'s refresh rate has changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_reference_space_reset}
::: rst-class
classref-signal
:::
::::

**reference_space_reset**()
`🔗<class_WebXRInterface_signal_reference_space_reset>`{.interpreted-text
role="ref"}

Emitted to indicate that the reference space has been reset or
reconfigured.

When (or whether) this is emitted depends on the user\'s browser or
device, but may include when the user has changed the dimensions of
their play space (which you may be able to access via
`XRInterface.get_play_area()<class_XRInterface_method_get_play_area>`{.interpreted-text
role="ref"}) or pressed/held a button to recenter their position.

See [WebXR\'s XRReferenceSpace reset
event](https://developer.mozilla.org/en-US/docs/Web/API/XRReferenceSpace/reset_event)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_select}
::: rst-class
classref-signal
:::
::::

**select**(input_source_id: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_WebXRInterface_signal_select>`{.interpreted-text
role="ref"}

Emitted after one of the input sources has finished its \"primary
action\".

Use
`get_input_source_tracker()<class_WebXRInterface_method_get_input_source_tracker>`{.interpreted-text
role="ref"} and
`get_input_source_target_ray_mode()<class_WebXRInterface_method_get_input_source_target_ray_mode>`{.interpreted-text
role="ref"} to get more information about the input source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_selectend}
::: rst-class
classref-signal
:::
::::

**selectend**(input_source_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_WebXRInterface_signal_selectend>`{.interpreted-text
role="ref"}

Emitted when one of the input sources has finished its \"primary
action\".

Use
`get_input_source_tracker()<class_WebXRInterface_method_get_input_source_tracker>`{.interpreted-text
role="ref"} and
`get_input_source_target_ray_mode()<class_WebXRInterface_method_get_input_source_target_ray_mode>`{.interpreted-text
role="ref"} to get more information about the input source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_selectstart}
::: rst-class
classref-signal
:::
::::

**selectstart**(input_source_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_WebXRInterface_signal_selectstart>`{.interpreted-text
role="ref"}

Emitted when one of the input source has started its \"primary action\".

Use
`get_input_source_tracker()<class_WebXRInterface_method_get_input_source_tracker>`{.interpreted-text
role="ref"} and
`get_input_source_target_ray_mode()<class_WebXRInterface_method_get_input_source_target_ray_mode>`{.interpreted-text
role="ref"} to get more information about the input source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_session_ended}
::: rst-class
classref-signal
:::
::::

**session_ended**()
`🔗<class_WebXRInterface_signal_session_ended>`{.interpreted-text
role="ref"}

Emitted when the user ends the WebXR session (which can be done using UI
from the browser or device).

At this point, you should do `get_viewport().use_xr = false` to instruct
Godot to resume rendering to the screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_session_failed}
::: rst-class
classref-signal
:::
::::

**session_failed**(message: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_WebXRInterface_signal_session_failed>`{.interpreted-text
role="ref"}

Emitted by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} if the session fails to start.

`message` may optionally contain an error message from WebXR, or an
empty string if no message is available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_session_started}
::: rst-class
classref-signal
:::
::::

**session_started**()
`🔗<class_WebXRInterface_signal_session_started>`{.interpreted-text
role="ref"}

Emitted by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} if the session is successfully started.

At this point, it\'s safe to do `get_viewport().use_xr = true` to
instruct Godot to start rendering to the XR device.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_session_supported}
::: rst-class
classref-signal
:::
::::

**session_supported**(session_mode:
`String<class_String>`{.interpreted-text role="ref"}, supported:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_WebXRInterface_signal_session_supported>`{.interpreted-text
role="ref"}

Emitted by
`is_session_supported()<class_WebXRInterface_method_is_session_supported>`{.interpreted-text
role="ref"} to indicate if the given `session_mode` is supported or not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_squeeze}
::: rst-class
classref-signal
:::
::::

**squeeze**(input_source_id: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_WebXRInterface_signal_squeeze>`{.interpreted-text
role="ref"}

Emitted after one of the input sources has finished its \"primary
squeeze action\".

Use
`get_input_source_tracker()<class_WebXRInterface_method_get_input_source_tracker>`{.interpreted-text
role="ref"} and
`get_input_source_target_ray_mode()<class_WebXRInterface_method_get_input_source_target_ray_mode>`{.interpreted-text
role="ref"} to get more information about the input source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_squeezeend}
::: rst-class
classref-signal
:::
::::

**squeezeend**(input_source_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_WebXRInterface_signal_squeezeend>`{.interpreted-text
role="ref"}

Emitted when one of the input sources has finished its \"primary squeeze
action\".

Use
`get_input_source_tracker()<class_WebXRInterface_method_get_input_source_tracker>`{.interpreted-text
role="ref"} and
`get_input_source_target_ray_mode()<class_WebXRInterface_method_get_input_source_target_ray_mode>`{.interpreted-text
role="ref"} to get more information about the input source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_squeezestart}
::: rst-class
classref-signal
:::
::::

**squeezestart**(input_source_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_WebXRInterface_signal_squeezestart>`{.interpreted-text
role="ref"}

Emitted when one of the input sources has started its \"primary squeeze
action\".

Use
`get_input_source_tracker()<class_WebXRInterface_method_get_input_source_tracker>`{.interpreted-text
role="ref"} and
`get_input_source_target_ray_mode()<class_WebXRInterface_method_get_input_source_target_ray_mode>`{.interpreted-text
role="ref"} to get more information about the input source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_signal_visibility_state_changed}
::: rst-class
classref-signal
:::
::::

**visibility_state_changed**()
`🔗<class_WebXRInterface_signal_visibility_state_changed>`{.interpreted-text
role="ref"}

Emitted when
`visibility_state<class_WebXRInterface_property_visibility_state>`{.interpreted-text
role="ref"} has changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_WebXRInterface_TargetRayMode}
::: rst-class
classref-enumeration
:::
::::

enum **TargetRayMode**:
`🔗<enum_WebXRInterface_TargetRayMode>`{.interpreted-text role="ref"}

:::: {#class_WebXRInterface_constant_TARGET_RAY_MODE_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`TargetRayMode<enum_WebXRInterface_TargetRayMode>`{.interpreted-text
role="ref"} **TARGET_RAY_MODE_UNKNOWN** = `0`

We don\'t know the target ray mode.

:::: {#class_WebXRInterface_constant_TARGET_RAY_MODE_GAZE}
::: rst-class
classref-enumeration-constant
:::
::::

`TargetRayMode<enum_WebXRInterface_TargetRayMode>`{.interpreted-text
role="ref"} **TARGET_RAY_MODE_GAZE** = `1`

Target ray originates at the viewer\'s eyes and points in the direction
they are looking.

:::: {#class_WebXRInterface_constant_TARGET_RAY_MODE_TRACKED_POINTER}
::: rst-class
classref-enumeration-constant
:::
::::

`TargetRayMode<enum_WebXRInterface_TargetRayMode>`{.interpreted-text
role="ref"} **TARGET_RAY_MODE_TRACKED_POINTER** = `2`

Target ray from a handheld pointer, most likely a VR touch controller.

:::: {#class_WebXRInterface_constant_TARGET_RAY_MODE_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`TargetRayMode<enum_WebXRInterface_TargetRayMode>`{.interpreted-text
role="ref"} **TARGET_RAY_MODE_SCREEN** = `3`

Target ray from touch screen, mouse or other tactile input device.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_WebXRInterface_property_enabled_features}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**enabled_features**
`🔗<class_WebXRInterface_property_enabled_features>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `String<class_String>`{.interpreted-text role="ref"}
  **get_enabled_features**()

A comma-separated list of features that were successfully enabled by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} when setting up the WebXR session.

This may include features requested by setting
`required_features<class_WebXRInterface_property_required_features>`{.interpreted-text
role="ref"} and
`optional_features<class_WebXRInterface_property_optional_features>`{.interpreted-text
role="ref"}, and will only be available after
`session_started<class_WebXRInterface_signal_session_started>`{.interpreted-text
role="ref"} has been emitted.

\*\*Note:\*\* This may not be support by all web browsers, in which case
it will be an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_property_optional_features}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**optional_features**
`🔗<class_WebXRInterface_property_optional_features>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_optional_features**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_optional_features**()

A comma-seperated list of optional features used by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} when setting up the WebXR session.

If a user\'s browser or device doesn\'t support one of the given
features, initialization will continue, but you won\'t be able to use
the requested feature.

This doesn\'t have any effect on the interface when already initialized.

Possible values come from [WebXR\'s
XRReferenceSpaceType](https://developer.mozilla.org/en-US/docs/Web/API/XRReferenceSpaceType),
or include other features like `"hand-tracking"` to enable hand
tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_property_reference_space_type}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**reference_space_type**
`🔗<class_WebXRInterface_property_reference_space_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `String<class_String>`{.interpreted-text role="ref"}
  **get_reference_space_type**()

The reference space type (from the list of requested types set in the
`requested_reference_space_types<class_WebXRInterface_property_requested_reference_space_types>`{.interpreted-text
role="ref"} property), that was ultimately used by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} when setting up the WebXR session.

Possible values come from [WebXR\'s
XRReferenceSpaceType](https://developer.mozilla.org/en-US/docs/Web/API/XRReferenceSpaceType).
If you want to use a particular reference space type, it must be listed
in either
`required_features<class_WebXRInterface_property_required_features>`{.interpreted-text
role="ref"} or
`optional_features<class_WebXRInterface_property_optional_features>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_property_requested_reference_space_types}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**requested_reference_space_types**
`🔗<class_WebXRInterface_property_requested_reference_space_types>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_requested_reference_space_types**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_requested_reference_space_types**()

A comma-seperated list of reference space types used by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} when setting up the WebXR session.

The reference space types are requested in order, and the first one
supported by the user\'s device or browser will be used. The
`reference_space_type<class_WebXRInterface_property_reference_space_type>`{.interpreted-text
role="ref"} property contains the reference space type that was
ultimately selected.

This doesn\'t have any effect on the interface when already initialized.

Possible values come from [WebXR\'s
XRReferenceSpaceType](https://developer.mozilla.org/en-US/docs/Web/API/XRReferenceSpaceType).
If you want to use a particular reference space type, it must be listed
in either
`required_features<class_WebXRInterface_property_required_features>`{.interpreted-text
role="ref"} or
`optional_features<class_WebXRInterface_property_optional_features>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_property_required_features}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**required_features**
`🔗<class_WebXRInterface_property_required_features>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_required_features**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_required_features**()

A comma-seperated list of required features used by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} when setting up the WebXR session.

If a user\'s browser or device doesn\'t support one of the given
features, initialization will fail and
`session_failed<class_WebXRInterface_signal_session_failed>`{.interpreted-text
role="ref"} will be emitted.

This doesn\'t have any effect on the interface when already initialized.

Possible values come from [WebXR\'s
XRReferenceSpaceType](https://developer.mozilla.org/en-US/docs/Web/API/XRReferenceSpaceType),
or include other features like `"hand-tracking"` to enable hand
tracking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_property_session_mode}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **session_mode**
`🔗<class_WebXRInterface_property_session_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_session_mode**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_session_mode**()

The session mode used by
`XRInterface.initialize()<class_XRInterface_method_initialize>`{.interpreted-text
role="ref"} when setting up the WebXR session.

This doesn\'t have any effect on the interface when already initialized.

Possible values come from [WebXR\'s
XRSessionMode](https://developer.mozilla.org/en-US/docs/Web/API/XRSessionMode),
including: `"immersive-vr"`, `"immersive-ar"`, and `"inline"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_property_visibility_state}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**visibility_state**
`🔗<class_WebXRInterface_property_visibility_state>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `String<class_String>`{.interpreted-text role="ref"}
  **get_visibility_state**()

Indicates if the WebXR session\'s imagery is visible to the user.

Possible values come from [WebXR\'s
XRVisibilityState](https://developer.mozilla.org/en-US/docs/Web/API/XRVisibilityState),
including `"hidden"`, `"visible"`, and `"visible-blurred"`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_WebXRInterface_method_get_available_display_refresh_rates}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_available_display_refresh_rates**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebXRInterface_method_get_available_display_refresh_rates>`{.interpreted-text
role="ref"}

Returns display refresh rates supported by the current HMD. Only
returned if this feature is supported by the web browser and after the
interface has been initialized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_method_get_display_refresh_rate}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_display_refresh_rate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebXRInterface_method_get_display_refresh_rate>`{.interpreted-text
role="ref"}

Returns the display refresh rate for the current HMD. Not supported on
all HMDs and browsers. It may not report an accurate value until after
using
`set_display_refresh_rate()<class_WebXRInterface_method_set_display_refresh_rate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_method_get_input_source_target_ray_mode}
::: rst-class
classref-method
:::
::::

`TargetRayMode<enum_WebXRInterface_TargetRayMode>`{.interpreted-text
role="ref"} **get_input_source_target_ray_mode**(input_source_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebXRInterface_method_get_input_source_target_ray_mode>`{.interpreted-text
role="ref"}

Returns the target ray mode for the given `input_source_id`.

This can help interpret the input coming from that input source. See
[XRInputSource.targetRayMode](https://developer.mozilla.org/en-US/docs/Web/API/XRInputSource/targetRayMode)
for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_method_get_input_source_tracker}
::: rst-class
classref-method
:::
::::

`XRControllerTracker<class_XRControllerTracker>`{.interpreted-text
role="ref"} **get_input_source_tracker**(input_source_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebXRInterface_method_get_input_source_tracker>`{.interpreted-text
role="ref"}

Gets an
`XRControllerTracker<class_XRControllerTracker>`{.interpreted-text
role="ref"} for the given `input_source_id`.

In the context of WebXR, an input source can be an advanced VR
controller like the Oculus Touch or Index controllers, or even a tap on
the screen, a spoken voice command or a button press on the device
itself. When a non-traditional input source is used, interpret the
position and orientation of the
`XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
role="ref"} as a ray pointing at the object the user wishes to interact
with.

Use this method to get information about the input source that triggered
one of these signals:

- `selectstart<class_WebXRInterface_signal_selectstart>`{.interpreted-text
  role="ref"}
- `select<class_WebXRInterface_signal_select>`{.interpreted-text
  role="ref"}
- `selectend<class_WebXRInterface_signal_selectend>`{.interpreted-text
  role="ref"}
- `squeezestart<class_WebXRInterface_signal_squeezestart>`{.interpreted-text
  role="ref"}
- `squeeze<class_WebXRInterface_signal_squeeze>`{.interpreted-text
  role="ref"}
- `squeezestart<class_WebXRInterface_signal_squeezestart>`{.interpreted-text
  role="ref"}

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_method_is_input_source_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_input_source_active**(input_source_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WebXRInterface_method_is_input_source_active>`{.interpreted-text
role="ref"}

Returns `true` if there is an active input source with the given
`input_source_id`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_method_is_session_supported}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**is_session_supported**(session_mode:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_WebXRInterface_method_is_session_supported>`{.interpreted-text
role="ref"}

Checks if the given `session_mode` is supported by the user\'s browser.

Possible values come from [WebXR\'s
XRSessionMode](https://developer.mozilla.org/en-US/docs/Web/API/XRSessionMode),
including: `"immersive-vr"`, `"immersive-ar"`, and `"inline"`.

This method returns nothing, instead it emits the
`session_supported<class_WebXRInterface_signal_session_supported>`{.interpreted-text
role="ref"} signal with the result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WebXRInterface_method_set_display_refresh_rate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_display_refresh_rate**(refresh_rate:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_WebXRInterface_method_set_display_refresh_rate>`{.interpreted-text
role="ref"}

Sets the display refresh rate for the current HMD. Not supported on all
HMDs and browsers. It won\'t take effect right away until after
`display_refresh_rate_changed<class_WebXRInterface_signal_display_refresh_rate_changed>`{.interpreted-text
role="ref"} is emitted.
