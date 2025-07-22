github_url
:   hide

# InputEvent {#class_InputEvent}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"},
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"},
`InputEventJoypadButton<class_InputEventJoypadButton>`{.interpreted-text
role="ref"},
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"}, `InputEventMIDI<class_InputEventMIDI>`{.interpreted-text
role="ref"},
`InputEventShortcut<class_InputEventShortcut>`{.interpreted-text
role="ref"}

Abstract base class for input events.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class of all types of input events. See
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`{.interpreted-text
  role="doc"}
- `Viewport and canvas transforms <../tutorials/2d/2d_transforms>`{.interpreted-text
  role="doc"}
- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

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

## Constants

:::: {#class_InputEvent_constant_DEVICE_ID_EMULATION}
::: rst-class
classref-constant
:::
::::

**DEVICE_ID_EMULATION** = `-1`
`🔗<class_InputEvent_constant_DEVICE_ID_EMULATION>`{.interpreted-text
role="ref"}

Device ID used for emulated mouse input from a touchscreen, or for
emulated touch input from a mouse. This can be used to distinguish
emulated mouse input from physical mouse input, or emulated touch input
from physical touch input.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_InputEvent_property_device}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **device** = `0`
`🔗<class_InputEvent_property_device>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_device**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_device**()

The event\'s device ID.

\*\*Note:\*\*
`device<class_InputEvent_property_device>`{.interpreted-text role="ref"}
can be negative for special use cases that don\'t refer to devices
physically present on the system. See
`DEVICE_ID_EMULATION<class_InputEvent_constant_DEVICE_ID_EMULATION>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_InputEvent_method_accumulate}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**accumulate**(with_event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`🔗<class_InputEvent_method_accumulate>`{.interpreted-text role="ref"}

Returns `true` if the given input event and this input event can be
added together (only for events of type
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"}).

The given input event\'s position, global position and speed will be
copied. The resulting `relative` is a sum of both events. Both events\'
modifiers have to be identical.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_as_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **as_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_as_text>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"}
representation of the event.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_get_action_strength}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_action_strength**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEvent_method_get_action_strength>`{.interpreted-text
role="ref"}

Returns a value between 0.0 and 1.0 depending on the given actions\'
state. Useful for getting the value of events of type
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"}.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_action}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_action**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_is_action>`{.interpreted-text
role="ref"}

Returns `true` if this input event matches a pre-defined action of any
type.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_action_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_action_pressed**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
allow_echo: `bool<class_bool>`{.interpreted-text role="ref"} = false,
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEvent_method_is_action_pressed>`{.interpreted-text
role="ref"}

Returns `true` if the given action matches this event and is being
pressed (and is not an echo event for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"}
events, unless `allow_echo` is `true`). Not relevant for events of type
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} or
`InputEventScreenDrag<class_InputEventScreenDrag>`{.interpreted-text
role="ref"}.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

\*\*Note:\*\* Due to keyboard ghosting,
`is_action_pressed()<class_InputEvent_method_is_action_pressed>`{.interpreted-text
role="ref"} may return `false` even if one of the action\'s keys is
pressed. See [Input
examples](../tutorials/inputs/input_examples.html#keyboard-events) in
the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_action_released}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_action_released**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEvent_method_is_action_released>`{.interpreted-text
role="ref"}

Returns `true` if the given action matches this event and is released
(i.e. not pressed). Not relevant for events of type
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} or
`InputEventScreenDrag<class_InputEventScreenDrag>`{.interpreted-text
role="ref"}.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_action_type}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_action_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputEvent_method_is_action_type>`{.interpreted-text
role="ref"}

Returns `true` if this input event\'s type is one that can be assigned
to an input action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_canceled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_canceled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_is_canceled>`{.interpreted-text
role="ref"}

Returns `true` if this input event has been canceled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_echo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_echo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_is_echo>`{.interpreted-text
role="ref"}

Returns `true` if this input event is an echo event (only for events of
type `InputEventKey<class_InputEventKey>`{.interpreted-text
role="ref"}). An echo event is a repeated key event sent when the user
is holding down the key. Any other event type returns `false`.

\*\*Note:\*\* The rate at which echo events are sent is typically around
20 events per second (after holding down the key for roughly half a
second). However, the key repeat delay/speed can be changed by the user
or disabled entirely in the operating system settings. To ensure your
project works correctly on all configurations, do not assume the user
has a specific key repeat configuration in your project\'s behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_match}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_match**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_is_match>`{.interpreted-text
role="ref"}

Returns `true` if the specified `event` matches this event. Only valid
for action events, which include key
(`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"}),
button
(`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} or
`InputEventJoypadButton<class_InputEventJoypadButton>`{.interpreted-text
role="ref"}), axis
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"}, and action
(`InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"}) events.

If `exact_match` is `false`, the check ignores additional input
modifiers for `InputEventKey<class_InputEventKey>`{.interpreted-text
role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

\*\*Note:\*\* This method only considers the event configuration (such
as the keyboard key or the joypad axis), not state information like
`is_pressed()<class_InputEvent_method_is_pressed>`{.interpreted-text
role="ref"},
`is_released()<class_InputEvent_method_is_released>`{.interpreted-text
role="ref"},
`is_echo()<class_InputEvent_method_is_echo>`{.interpreted-text
role="ref"}, or
`is_canceled()<class_InputEvent_method_is_canceled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_is_pressed>`{.interpreted-text
role="ref"}

Returns `true` if this input event is pressed. Not relevant for events
of type
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} or
`InputEventScreenDrag<class_InputEventScreenDrag>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Due to keyboard ghosting,
`is_pressed()<class_InputEvent_method_is_pressed>`{.interpreted-text
role="ref"} may return `false` even if one of the action\'s keys is
pressed. See [Input
examples](../tutorials/inputs/input_examples.html#keyboard-events) in
the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_is_released}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_released**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_is_released>`{.interpreted-text
role="ref"}

Returns `true` if this input event is released. Not relevant for events
of type
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} or
`InputEventScreenDrag<class_InputEventScreenDrag>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEvent_method_xformed_by}
::: rst-class
classref-method
:::
::::

`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}
**xformed_by**(xform: `Transform2D<class_Transform2D>`{.interpreted-text
role="ref"}, local_ofs: `Vector2<class_Vector2>`{.interpreted-text
role="ref"} = Vector2(0, 0))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputEvent_method_xformed_by>`{.interpreted-text
role="ref"}

Returns a copy of the given input event which has been offset by
`local_ofs` and transformed by `xform`. Relevant for events of type
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"},
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"},
`InputEventScreenTouch<class_InputEventScreenTouch>`{.interpreted-text
role="ref"},
`InputEventScreenDrag<class_InputEventScreenDrag>`{.interpreted-text
role="ref"},
`InputEventMagnifyGesture<class_InputEventMagnifyGesture>`{.interpreted-text
role="ref"} and
`InputEventPanGesture<class_InputEventPanGesture>`{.interpreted-text
role="ref"}.
