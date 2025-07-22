github_url
:   hide

# XRController3D {#class_XRController3D}

**Inherits:** `XRNode3D<class_XRNode3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 3D node representing a spatially-tracked controller.

::: rst-class
classref-introduction-group
:::

## Description

This is a helper 3D node that is linked to the tracking of controllers.
It also offers several handy passthroughs to the state of buttons and
such on the controllers.

Controllers are linked by their ID. You can create controller nodes
before the controllers are available. If your game always uses two
controllers (one for each hand), you can predefine the controllers with
ID 1 and 2; they will become active as soon as the controllers are
identified. If you expect additional controllers to be used, you should
react to the signals and add XRController3D nodes to your scene.

The position of the controller node is automatically updated by the
`XRServer<class_XRServer>`{.interpreted-text role="ref"}. This makes
this node ideal to add child nodes to visualize the controller.

The current `XRInterface<class_XRInterface>`{.interpreted-text
role="ref"} defines the names of inputs. In the case of OpenXR, these
are the names of actions in the current action set from the OpenXR
action map.

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

## Signals

:::: {#class_XRController3D_signal_button_pressed}
::: rst-class
classref-signal
:::
::::

**button_pressed**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_XRController3D_signal_button_pressed>`{.interpreted-text
role="ref"}

Emitted when a button on this controller is pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_signal_button_released}
::: rst-class
classref-signal
:::
::::

**button_released**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_XRController3D_signal_button_released>`{.interpreted-text
role="ref"}

Emitted when a button on this controller is released.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_signal_input_float_changed}
::: rst-class
classref-signal
:::
::::

**input_float_changed**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_XRController3D_signal_input_float_changed>`{.interpreted-text
role="ref"}

Emitted when a trigger or similar input on this controller changes
value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_signal_input_vector2_changed}
::: rst-class
classref-signal
:::
::::

**input_vector2_changed**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_XRController3D_signal_input_vector2_changed>`{.interpreted-text
role="ref"}

Emitted when a thumbstick or thumbpad on this controller is moved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_signal_profile_changed}
::: rst-class
classref-signal
:::
::::

**profile_changed**(role: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_XRController3D_signal_profile_changed>`{.interpreted-text
role="ref"}

Emitted when the interaction profile on this controller is changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_XRController3D_method_get_float}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_float**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRController3D_method_get_float>`{.interpreted-text
role="ref"}

Returns a numeric value for the input with the given `name`. This is
used for triggers and grip sensors.

\*\*Note:\*\* The current
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"} defines
the `name` for each input. In the case of OpenXR, these are the names of
actions in the current action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_method_get_input}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_input**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRController3D_method_get_input>`{.interpreted-text
role="ref"}

Returns a `Variant<class_Variant>`{.interpreted-text role="ref"} for the
input with the given `name`. This works for any input type, the variant
will be typed according to the actions configuration.

\*\*Note:\*\* The current
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"} defines
the `name` for each input. In the case of OpenXR, these are the names of
actions in the current action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_method_get_tracker_hand}
::: rst-class
classref-method
:::
::::

`TrackerHand<enum_XRPositionalTracker_TrackerHand>`{.interpreted-text
role="ref"} **get_tracker_hand**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRController3D_method_get_tracker_hand>`{.interpreted-text
role="ref"}

Returns the hand holding this controller, if known.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_method_get_vector2}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_vector2**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRController3D_method_get_vector2>`{.interpreted-text
role="ref"}

Returns a `Vector2<class_Vector2>`{.interpreted-text role="ref"} for the
input with the given `name`. This is used for thumbsticks and thumbpads
found on many controllers.

\*\*Note:\*\* The current
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"} defines
the `name` for each input. In the case of OpenXR, these are the names of
actions in the current action set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_XRController3D_method_is_button_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_button_pressed**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_XRController3D_method_is_button_pressed>`{.interpreted-text
role="ref"}

Returns `true` if the button with the given `name` is pressed.

\*\*Note:\*\* The current
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"} defines
the `name` for each input. In the case of OpenXR, these are the names of
actions in the current action set.
