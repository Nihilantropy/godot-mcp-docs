github_url
:   hide

# XRPositionalTracker {#class_XRPositionalTracker}

**Inherits:** `XRTracker<class_XRTracker>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `XRBodyTracker<class_XRBodyTracker>`{.interpreted-text
role="ref"},
`XRControllerTracker<class_XRControllerTracker>`{.interpreted-text
role="ref"}, `XRHandTracker<class_XRHandTracker>`{.interpreted-text
role="ref"}

A tracked object.

::: rst-class
classref-introduction-group
:::

## Description

An instance of this object represents a device that is tracked, such as
a controller or anchor point. HMDs aren\'t represented here as they are
handled internally.

As controllers are turned on and the
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"} detects
them, instances of this object are automatically added to this list of
active tracking objects accessible through the
`XRServer<class_XRServer>`{.interpreted-text role="ref"}.

The `XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"} and
`XRAnchor3D<class_XRAnchor3D>`{.interpreted-text role="ref"} both
consume objects of this type and should be used in your project. The
positional trackers are just under-the-hood objects that make this all
work. These are mostly exposed so that GDExtension-based interfaces can
interact with them.

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

:::: {#class_XRPositionalTracker_signal_button_pressed}
::: rst-class
classref-signal
:::
::::

**button_pressed**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_signal_button_pressed>`{.interpreted-text
role="ref"}

Emitted when a button on this tracker is pressed. Note that many XR
runtimes allow other inputs to be mapped to buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_signal_button_released}
::: rst-class
classref-signal
:::
::::

**button_released**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_signal_button_released>`{.interpreted-text
role="ref"}

Emitted when a button on this tracker is released.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_signal_input_float_changed}
::: rst-class
classref-signal
:::
::::

**input_float_changed**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRPositionalTracker_signal_input_float_changed>`{.interpreted-text
role="ref"}

Emitted when a trigger or similar input on this tracker changes value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_signal_input_vector2_changed}
::: rst-class
classref-signal
:::
::::

**input_vector2_changed**(name: `String<class_String>`{.interpreted-text
role="ref"}, vector: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_signal_input_vector2_changed>`{.interpreted-text
role="ref"}

Emitted when a thumbstick or thumbpad on this tracker moves.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_signal_pose_changed}
::: rst-class
classref-signal
:::
::::

**pose_changed**(pose: `XRPose<class_XRPose>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_signal_pose_changed>`{.interpreted-text
role="ref"}

Emitted when the state of a pose tracked by this tracker changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_signal_pose_lost_tracking}
::: rst-class
classref-signal
:::
::::

**pose_lost_tracking**(pose: `XRPose<class_XRPose>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_signal_pose_lost_tracking>`{.interpreted-text
role="ref"}

Emitted when a pose tracked by this tracker stops getting updated
tracking data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_signal_profile_changed}
::: rst-class
classref-signal
:::
::::

**profile_changed**(role: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_signal_profile_changed>`{.interpreted-text
role="ref"}

Emitted when the profile of our tracker changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_XRPositionalTracker_TrackerHand}
::: rst-class
classref-enumeration
:::
::::

enum **TrackerHand**:
`🔗<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text role="ref"}

:::: {#class_XRPositionalTracker_constant_TRACKER_HAND_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
role="ref"} **TRACKER_HAND_UNKNOWN** = `0`

The hand this tracker is held in is unknown or not applicable.

:::: {#class_XRPositionalTracker_constant_TRACKER_HAND_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
role="ref"} **TRACKER_HAND_LEFT** = `1`

This tracker is the left hand controller.

:::: {#class_XRPositionalTracker_constant_TRACKER_HAND_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
role="ref"} **TRACKER_HAND_RIGHT** = `2`

This tracker is the right hand controller.

:::: {#class_XRPositionalTracker_constant_TRACKER_HAND_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
role="ref"} **TRACKER_HAND_MAX** = `3`

Represents the size of the
`TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRPositionalTracker_property_hand}
::: rst-class
classref-property
:::
::::

`TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
role="ref"} **hand** = `0`
`🔗<class_XRPositionalTracker_property_hand>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracker_hand**(value:
  `TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
  role="ref"})
- `TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
  role="ref"} **get_tracker_hand**()

Defines which hand this tracker relates to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_property_profile}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **profile** = `""`
`🔗<class_XRPositionalTracker_property_profile>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracker_profile**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_tracker_profile**()

The profile associated with this tracker, interface dependent but will
indicate the type of controller being tracked.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRPositionalTracker_method_get_input}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_input**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRPositionalTracker_method_get_input>`{.interpreted-text
role="ref"}

**Deprecated:** Use through
`XRControllerTracker<class_XRControllerTracker>`{.interpreted-text
role="ref"}.

Returns an input for this tracker. It can return a boolean, float or
`Vector2<class_Vector2>`{.interpreted-text role="ref"} value depending
on whether the input is a button, trigger or thumbstick/thumbpad.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_method_get_pose}
::: rst-class
classref-method
:::
::::

`XRPose<class_XRPose>`{.interpreted-text role="ref"} **get_pose**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRPositionalTracker_method_get_pose>`{.interpreted-text
role="ref"}

Returns the current `XRPose<class_XRPose>`{.interpreted-text role="ref"}
state object for the bound `name` pose.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_method_has_pose}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_pose**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRPositionalTracker_method_has_pose>`{.interpreted-text
role="ref"}

Returns `true` if the tracker is available and is currently tracking the
bound `name` pose.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_method_invalidate_pose}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**invalidate_pose**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_XRPositionalTracker_method_invalidate_pose>`{.interpreted-text
role="ref"}

Marks this pose as invalid, we don\'t clear the last reported state but
it allows users to decide if trackers need to be hidden if we lose
tracking or just remain at their last known position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_method_set_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_method_set_input>`{.interpreted-text
role="ref"}

**Deprecated:** Use through
`XRControllerTracker<class_XRControllerTracker>`{.interpreted-text
role="ref"}.

Changes the value for the given input. This method is called by an
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}
implementation and should not be used directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPositionalTracker_method_set_pose}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_pose**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, transform:
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"},
linear_velocity: `Vector3<class_Vector3>`{.interpreted-text role="ref"},
angular_velocity: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, tracking_confidence:
`TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
role="ref"})
`🔗<class_XRPositionalTracker_method_set_pose>`{.interpreted-text
role="ref"}

Sets the transform, linear velocity, angular velocity and tracking
confidence for the given pose. This method is called by an
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}
implementation and should not be used directly.
