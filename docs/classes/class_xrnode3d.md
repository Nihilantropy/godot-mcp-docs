github_url
:   hide

# XRNode3D {#class_XRNode3D}

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `XRAnchor3D<class_XRAnchor3D>`{.interpreted-text
role="ref"}, `XRController3D<class_XRController3D>`{.interpreted-text
role="ref"}

A 3D node that has its position automatically updated by the
`XRServer<class_XRServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

This node can be bound to a specific pose of an
`XRPositionalTracker<class_XRPositionalTracker>`{.interpreted-text
role="ref"} and will automatically have its
`Node3D.transform<class_Node3D_property_transform>`{.interpreted-text
role="ref"} updated by the `XRServer<class_XRServer>`{.interpreted-text
role="ref"}. Nodes of this type must be added as children of the
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"} node.

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

:::: {#class_XRNode3D_signal_tracking_changed}
::: rst-class
classref-signal
:::
::::

**tracking_changed**(tracking: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_XRNode3D_signal_tracking_changed>`{.interpreted-text
role="ref"}

Emitted when the
`tracker<class_XRNode3D_property_tracker>`{.interpreted-text role="ref"}
starts or stops receiving updated tracking data for the
`pose<class_XRNode3D_property_pose>`{.interpreted-text role="ref"} being
tracked. The `tracking` argument indicates whether the tracker is
getting updated tracking data.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_XRNode3D_property_pose}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **pose** =
`&"default"` `🔗<class_XRNode3D_property_pose>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pose_name**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_pose_name**()

The name of the pose we\'re bound to. Which poses a tracker supports is
not known during design time.

Godot defines number of standard pose names such as `aim` and `grip` but
other may be configured within a given
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRNode3D_property_show_when_tracked}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_when_tracked** =
`false`
`🔗<class_XRNode3D_property_show_when_tracked>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_when_tracked**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_show_when_tracked**()

Enables showing the node when tracking starts, and hiding the node when
tracking is lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRNode3D_property_tracker}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **tracker**
= `&""` `🔗<class_XRNode3D_property_tracker>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tracker**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_tracker**()

The name of the tracker we\'re bound to. Which trackers are available is
not known during design time.

Godot defines a number of standard trackers such as `left_hand` and
`right_hand` but others may be configured within a given
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRNode3D_method_get_has_tracking_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_has_tracking_data**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRNode3D_method_get_has_tracking_data>`{.interpreted-text
role="ref"}

Returns `true` if the
`tracker<class_XRNode3D_property_tracker>`{.interpreted-text role="ref"}
has current tracking data for the
`pose<class_XRNode3D_property_pose>`{.interpreted-text role="ref"} being
tracked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRNode3D_method_get_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_is_active**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_XRNode3D_method_get_is_active>`{.interpreted-text
role="ref"}

Returns `true` if the
`tracker<class_XRNode3D_property_tracker>`{.interpreted-text role="ref"}
has been registered and the
`pose<class_XRNode3D_property_pose>`{.interpreted-text role="ref"} is
being tracked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRNode3D_method_get_pose}
::: rst-class
classref-method
:::
::::

`XRPose<class_XRPose>`{.interpreted-text role="ref"} **get_pose**()
`🔗<class_XRNode3D_method_get_pose>`{.interpreted-text role="ref"}

Returns the `XRPose<class_XRPose>`{.interpreted-text role="ref"}
containing the current state of the pose being tracked. This gives
access to additional properties of this pose.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRNode3D_method_trigger_haptic_pulse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**trigger_haptic_pulse**(action_name:
`String<class_String>`{.interpreted-text role="ref"}, frequency:
`float<class_float>`{.interpreted-text role="ref"}, amplitude:
`float<class_float>`{.interpreted-text role="ref"}, duration_sec:
`float<class_float>`{.interpreted-text role="ref"}, delay_sec:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRNode3D_method_trigger_haptic_pulse>`{.interpreted-text
role="ref"}

Triggers a haptic pulse on a device associated with this interface.

`action_name` is the name of the action for this pulse.

`frequency` is the frequency of the pulse, set to `0.0` to have the
system use a default frequency.

`amplitude` is the amplitude of the pulse between `0.0` and `1.0`.

`duration_sec` is the duration of the pulse in seconds.

`delay_sec` is a delay in seconds before the pulse is given.
