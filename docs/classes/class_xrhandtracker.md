github_url
:   hide

# XRHandTracker {#class_XRHandTracker}

**Inherits:**
`XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
role="ref"} **\<** `XRTracker<class_XRTracker>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A tracked hand in XR.

::: rst-class
classref-introduction-group
:::

## Description

A hand tracking system will create an instance of this object and add it
to the `XRServer<class_XRServer>`{.interpreted-text role="ref"}. This
tracking system will then obtain skeleton data, convert it to the Godot
Humanoid hand skeleton and store this data on the **XRHandTracker**
object.

Use `XRHandModifier3D<class_XRHandModifier3D>`{.interpreted-text
role="ref"} to animate a hand mesh using hand tracking data.

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

## Enumerations

:::: {#enum_XRHandTracker_HandTrackingSource}
::: rst-class
classref-enumeration
:::
::::

enum **HandTrackingSource**:
`🔗<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"}

:::: {#class_XRHandTracker_constant_HAND_TRACKING_SOURCE_UNKNOWN}
::: rst-class
classref-enumeration-constant
:::
::::

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"} **HAND_TRACKING_SOURCE_UNKNOWN** = `0`

The source of hand tracking data is unknown.

:::: {#class_XRHandTracker_constant_HAND_TRACKING_SOURCE_UNOBSTRUCTED}
::: rst-class
classref-enumeration-constant
:::
::::

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"} **HAND_TRACKING_SOURCE_UNOBSTRUCTED** = `1`

The source of hand tracking data is unobstructed, meaning that an
accurate method of hand tracking is used. These include optical hand
tracking, data gloves, etc.

:::: {#class_XRHandTracker_constant_HAND_TRACKING_SOURCE_CONTROLLER}
::: rst-class
classref-enumeration-constant
:::
::::

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"} **HAND_TRACKING_SOURCE_CONTROLLER** = `2`

The source of hand tracking data is a controller, meaning that joint
positions are inferred from controller inputs.

:::: {#class_XRHandTracker_constant_HAND_TRACKING_SOURCE_NOT_TRACKED}
::: rst-class
classref-enumeration-constant
:::
::::

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"} **HAND_TRACKING_SOURCE_NOT_TRACKED** = `3`

No hand tracking data is tracked, this either means the hand is
obscured, the controller is turned off, or tracking is not supported for
the current input type.

:::: {#class_XRHandTracker_constant_HAND_TRACKING_SOURCE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"} **HAND_TRACKING_SOURCE_MAX** = `4`

Represents the size of the
`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRHandTracker_HandJoint}
::: rst-class
classref-enumeration
:::
::::

enum **HandJoint**: `🔗<enum_XRHandTracker_HandJoint>`{.interpreted-text
role="ref"}

:::: {#class_XRHandTracker_constant_HAND_JOINT_PALM}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_PALM** = `0`

Palm joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_WRIST}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_WRIST** = `1`

Wrist joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_THUMB_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_THUMB_METACARPAL** = `2`

Thumb metacarpal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_THUMB_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_THUMB_PHALANX_PROXIMAL** = `3`

Thumb phalanx proximal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_THUMB_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_THUMB_PHALANX_DISTAL** = `4`

Thumb phalanx distal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_THUMB_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_THUMB_TIP** = `5`

Thumb tip joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_INDEX_FINGER_METACARPAL** = `6`

Index finger metacarpal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_INDEX_FINGER_PHALANX_PROXIMAL** = `7`

Index finger phalanx proximal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_INDEX_FINGER_PHALANX_INTERMEDIATE** = `8`

Index finger phalanx intermediate joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_INDEX_FINGER_PHALANX_DISTAL** = `9`

Index finger phalanx distal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_INDEX_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_INDEX_FINGER_TIP** = `10`

Index finger tip joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_MIDDLE_FINGER_METACARPAL** = `11`

Middle finger metacarpal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_MIDDLE_FINGER_PHALANX_PROXIMAL** = `12`

Middle finger phalanx proximal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_MIDDLE_FINGER_PHALANX_INTERMEDIATE** = `13`

Middle finger phalanx intermediate joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_MIDDLE_FINGER_PHALANX_DISTAL** = `14`

Middle finger phalanx distal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_MIDDLE_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_MIDDLE_FINGER_TIP** = `15`

Middle finger tip joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_RING_FINGER_METACARPAL** = `16`

Ring finger metacarpal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_RING_FINGER_PHALANX_PROXIMAL** = `17`

Ring finger phalanx proximal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_RING_FINGER_PHALANX_INTERMEDIATE** = `18`

Ring finger phalanx intermediate joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_RING_FINGER_PHALANX_DISTAL** = `19`

Ring finger phalanx distal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_RING_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_RING_FINGER_TIP** = `20`

Ring finger tip joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_METACARPAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_PINKY_FINGER_METACARPAL** = `21`

Pinky finger metacarpal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_PINKY_FINGER_PHALANX_PROXIMAL** = `22`

Pinky finger phalanx proximal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_PINKY_FINGER_PHALANX_INTERMEDIATE** = `23`

Pinky finger phalanx intermediate joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_PINKY_FINGER_PHALANX_DISTAL** = `24`

Pinky finger phalanx distal joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_PINKY_FINGER_TIP}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_PINKY_FINGER_TIP** = `25`

Pinky finger tip joint.

:::: {#class_XRHandTracker_constant_HAND_JOINT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
**HAND_JOINT_MAX** = `26`

Represents the size of the
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_XRHandTracker_HandJointFlags}
::: rst-class
classref-enumeration
:::
::::

flags **HandJointFlags**:
`🔗<enum_XRHandTracker_HandJointFlags>`{.interpreted-text role="ref"}

:::: {#class_XRHandTracker_constant_HAND_JOINT_FLAG_ORIENTATION_VALID}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_FLAG_ORIENTATION_VALID** = `1`

The hand joint\'s orientation data is valid.

:::: {#class_XRHandTracker_constant_HAND_JOINT_FLAG_ORIENTATION_TRACKED}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_FLAG_ORIENTATION_TRACKED** = `2`

The hand joint\'s orientation is actively tracked. May not be set if
tracking has been temporarily lost.

:::: {#class_XRHandTracker_constant_HAND_JOINT_FLAG_POSITION_VALID}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_FLAG_POSITION_VALID** = `4`

The hand joint\'s position data is valid.

:::: {#class_XRHandTracker_constant_HAND_JOINT_FLAG_POSITION_TRACKED}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_FLAG_POSITION_TRACKED** = `8`

The hand joint\'s position is actively tracked. May not be set if
tracking has been temporarily lost.

:::: {#class_XRHandTracker_constant_HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_FLAG_LINEAR_VELOCITY_VALID** = `16`

The hand joint\'s linear velocity data is valid.

:::: {#class_XRHandTracker_constant_HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID}
::: rst-class
classref-enumeration-constant
:::
::::

`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"} **HAND_JOINT_FLAG_ANGULAR_VELOCITY_VALID** = `32`

The hand joint\'s angular velocity data is valid.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRHandTracker_property_hand_tracking_source}
::: rst-class
classref-property
:::
::::

`HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
role="ref"} **hand_tracking_source** = `0`
`🔗<class_XRHandTracker_property_hand_tracking_source>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hand_tracking_source**(value:
  `HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
  role="ref"})
- `HandTrackingSource<enum_XRHandTracker_HandTrackingSource>`{.interpreted-text
  role="ref"} **get_hand_tracking_source**()

The source of the hand tracking data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_property_has_tracking_data}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_tracking_data** =
`false`
`🔗<class_XRHandTracker_property_has_tracking_data>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_has_tracking_data**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_has_tracking_data**()

If `true`, the hand tracking data is valid.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRHandTracker_method_get_hand_joint_angular_velocity}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_hand_joint_angular_velocity**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRHandTracker_method_get_hand_joint_angular_velocity>`{.interpreted-text
role="ref"}

Returns the angular velocity for the given hand joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_get_hand_joint_flags}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"}\] **get_hand_joint_flags**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRHandTracker_method_get_hand_joint_flags>`{.interpreted-text
role="ref"}

Returns flags about the validity of the tracking data for the given hand
joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_get_hand_joint_linear_velocity}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_hand_joint_linear_velocity**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRHandTracker_method_get_hand_joint_linear_velocity>`{.interpreted-text
role="ref"}

Returns the linear velocity for the given hand joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_get_hand_joint_radius}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_hand_joint_radius**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRHandTracker_method_get_hand_joint_radius>`{.interpreted-text
role="ref"}

Returns the radius of the given hand joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_get_hand_joint_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_hand_joint_transform**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRHandTracker_method_get_hand_joint_transform>`{.interpreted-text
role="ref"}

Returns the transform for the given hand joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_set_hand_joint_angular_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_hand_joint_angular_velocity**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"},
angular_velocity: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_XRHandTracker_method_set_hand_joint_angular_velocity>`{.interpreted-text
role="ref"}

Sets the angular velocity for the given hand joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_set_hand_joint_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_hand_joint_flags**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"},
flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`HandJointFlags<enum_XRHandTracker_HandJointFlags>`{.interpreted-text
role="ref"}\])
`🔗<class_XRHandTracker_method_set_hand_joint_flags>`{.interpreted-text
role="ref"}

Sets flags about the validity of the tracking data for the given hand
joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_set_hand_joint_linear_velocity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_hand_joint_linear_velocity**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"},
linear_velocity: `Vector3<class_Vector3>`{.interpreted-text role="ref"})
`🔗<class_XRHandTracker_method_set_hand_joint_linear_velocity>`{.interpreted-text
role="ref"}

Sets the linear velocity for the given hand joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_set_hand_joint_radius}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_hand_joint_radius**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"},
radius: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRHandTracker_method_set_hand_joint_radius>`{.interpreted-text
role="ref"}

Sets the radius of the given hand joint.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRHandTracker_method_set_hand_joint_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_hand_joint_transform**(joint:
`HandJoint<enum_XRHandTracker_HandJoint>`{.interpreted-text role="ref"},
transform: `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"})
`🔗<class_XRHandTracker_method_set_hand_joint_transform>`{.interpreted-text
role="ref"}

Sets the transform for the given hand joint.
