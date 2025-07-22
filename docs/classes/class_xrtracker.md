github_url
:   hide

# XRTracker {#class_XRTracker}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `XRFaceTracker<class_XRFaceTracker>`{.interpreted-text
role="ref"},
`XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
role="ref"}

A tracked object.

::: rst-class
classref-introduction-group
:::

## Description

This object is the base of all XR trackers.

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
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRTracker_property_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **description** =
`""` `🔗<class_XRTracker_property_description>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracker_desc**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_tracker_desc**()

The description of this tracker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRTracker_property_name}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **name** =
`&"Unknown"` `🔗<class_XRTracker_property_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracker_name**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_tracker_name**()

The unique name of this tracker. The trackers that are available differ
between various XR runtimes and can often be configured by the user.
Godot maintains a number of reserved names that it expects the
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"} to
implement if applicable:

- `"head"` identifies the
  `XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
  role="ref"} of the player\'s head
- `"left_hand"` identifies the
  `XRControllerTracker<class_XRControllerTracker>`{.interpreted-text
  role="ref"} in the player\'s left hand
- `"right_hand"` identifies the
  `XRControllerTracker<class_XRControllerTracker>`{.interpreted-text
  role="ref"} in the player\'s right hand
- `"/user/hand_tracker/left"` identifies the
  `XRHandTracker<class_XRHandTracker>`{.interpreted-text role="ref"} for
  the player\'s left hand
- `"/user/hand_tracker/right"` identifies the
  `XRHandTracker<class_XRHandTracker>`{.interpreted-text role="ref"} for
  the player\'s right hand
- `"/user/body_tracker"` identifies the
  `XRBodyTracker<class_XRBodyTracker>`{.interpreted-text role="ref"} for
  the player\'s body
- `"/user/face_tracker"` identifies the
  `XRFaceTracker<class_XRFaceTracker>`{.interpreted-text role="ref"} for
  the player\'s face

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRTracker_property_type}
::: rst-class
classref-property
:::
::::

`TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
**type** = `128` `🔗<class_XRTracker_property_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracker_type**(value:
  `TrackerType<enum_XRServer_TrackerType>`{.interpreted-text
  role="ref"})
- `TrackerType<enum_XRServer_TrackerType>`{.interpreted-text role="ref"}
  **get_tracker_type**()

The type of tracker.
