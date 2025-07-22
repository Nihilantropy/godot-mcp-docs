github_url
:   hide

# XRPose {#class_XRPose}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

This object contains all data related to a pose on a tracked object.

::: rst-class
classref-introduction-group
:::

## Description

XR runtimes often identify multiple locations on devices such as
controllers that are spatially tracked.

Orientation, location, linear velocity and angular velocity are all
provided for each pose by the XR runtime. This object contains this
state of a pose.

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

:::: {#enum_XRPose_TrackingConfidence}
::: rst-class
classref-enumeration
:::
::::

enum **TrackingConfidence**:
`🔗<enum_XRPose_TrackingConfidence>`{.interpreted-text role="ref"}

:::: {#class_XRPose_constant_XR_TRACKING_CONFIDENCE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
role="ref"} **XR_TRACKING_CONFIDENCE_NONE** = `0`

No tracking information is available for this pose.

:::: {#class_XRPose_constant_XR_TRACKING_CONFIDENCE_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
role="ref"} **XR_TRACKING_CONFIDENCE_LOW** = `1`

Tracking information may be inaccurate or estimated. For example, with
inside out tracking this would indicate a controller may be (partially)
obscured.

:::: {#class_XRPose_constant_XR_TRACKING_CONFIDENCE_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
role="ref"} **XR_TRACKING_CONFIDENCE_HIGH** = `2`

Tracking information is considered accurate and up to date.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRPose_property_angular_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**angular_velocity** = `Vector3(0, 0, 0)`
`🔗<class_XRPose_property_angular_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_angular_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_angular_velocity**()

The angular velocity for this pose.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPose_property_has_tracking_data}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_tracking_data** =
`false` `🔗<class_XRPose_property_has_tracking_data>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_has_tracking_data**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_has_tracking_data**()

If `true` our tracking data is up to date. If `false` we\'re no longer
receiving new tracking data and our state is whatever that last valid
state was.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPose_property_linear_velocity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**linear_velocity** = `Vector3(0, 0, 0)`
`🔗<class_XRPose_property_linear_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_linear_velocity**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_linear_velocity**()

The linear velocity of this pose.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPose_property_name}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **name** =
`&""` `🔗<class_XRPose_property_name>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_name**(value: `StringName<class_StringName>`{.interpreted-text
  role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_name**()

The name of this pose. Usually, this name is derived from an action map
set up by the user. Godot also suggests some pose names that
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"} objects
are expected to implement:

- `root` is the root location, often used for tracked objects that do
  not have further nodes.
- `aim` is the tip of a controller with its orientation pointing
  outwards, often used for raycasts.
- `grip` is the location where the user grips the controller.
- `skeleton` is the root location for a hand mesh, when using hand
  tracking and an animated skeleton is supplied by the XR runtime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPose_property_tracking_confidence}
::: rst-class
classref-property
:::
::::

`TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
role="ref"} **tracking_confidence** = `0`
`🔗<class_XRPose_property_tracking_confidence>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracking_confidence**(value:
  `TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
  role="ref"})
- `TrackingConfidence<enum_XRPose_TrackingConfidence>`{.interpreted-text
  role="ref"} **get_tracking_confidence**()

The tracking confidence for this pose, provides insight on how accurate
the spatial positioning of this record is.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRPose_property_transform}
::: rst-class
classref-property
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**transform** = `Transform3D(1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0)`
`🔗<class_XRPose_property_transform>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform3D<class_Transform3D>`{.interpreted-text role="ref"})
- `Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
  **get_transform**()

The transform containing the original and transform as reported by the
XR runtime.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRPose_method_get_adjusted_transform}
::: rst-class
classref-method
:::
::::

`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}
**get_adjusted_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRPose_method_get_adjusted_transform>`{.interpreted-text
role="ref"}

Returns the
`transform<class_XRPose_property_transform>`{.interpreted-text
role="ref"} with world scale and our reference frame applied. This is
the transform used to position
`XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"} objects.
