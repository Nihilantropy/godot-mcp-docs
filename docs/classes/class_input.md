github_url
:   hide

# Input {#class_Input}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton for handling inputs.

::: rst-class
classref-introduction-group
:::

## Description

The **Input** singleton handles key presses, mouse buttons and movement,
gamepads, and input actions. Actions and their events can be set in the
**Input Map** tab in **Project \> Project Settings**, or with the
`InputMap<class_InputMap>`{.interpreted-text role="ref"} class.

\*\*Note:\*\* **Input**\'s methods reflect the global input state and
are not affected by
`Control.accept_event()<class_Control_method_accept_event>`{.interpreted-text
role="ref"} or
`Viewport.set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"}, as those methods only deal with the way input is propagated
in the `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Inputs documentation index <../tutorials/inputs/index>`{.interpreted-text
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

## Signals

:::: {#class_Input_signal_joy_connection_changed}
::: rst-class
classref-signal
:::
::::

**joy_connection_changed**(device: `int<class_int>`{.interpreted-text
role="ref"}, connected: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Input_signal_joy_connection_changed>`{.interpreted-text
role="ref"}

Emitted when a joypad device has been connected or disconnected.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Input_MouseMode}
::: rst-class
classref-enumeration
:::
::::

enum **MouseMode**: `🔗<enum_Input_MouseMode>`{.interpreted-text
role="ref"}

:::: {#class_Input_constant_MOUSE_MODE_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_VISIBLE** = `0`

Makes the mouse cursor visible if it is hidden.

:::: {#class_Input_constant_MOUSE_MODE_HIDDEN}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_HIDDEN** = `1`

Makes the mouse cursor hidden if it is visible.

:::: {#class_Input_constant_MOUSE_MODE_CAPTURED}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_CAPTURED** = `2`

Captures the mouse. The mouse will be hidden and its position locked at
the center of the window manager\'s window.

\*\*Note:\*\* If you want to process the mouse\'s movement in this mode,
you need to use
`InputEventMouseMotion.relative<class_InputEventMouseMotion_property_relative>`{.interpreted-text
role="ref"}.

:::: {#class_Input_constant_MOUSE_MODE_CONFINED}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_CONFINED** = `3`

Confines the mouse cursor to the game window, and make it visible.

:::: {#class_Input_constant_MOUSE_MODE_CONFINED_HIDDEN}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_CONFINED_HIDDEN** = `4`

Confines the mouse cursor to the game window, and make it hidden.

:::: {#class_Input_constant_MOUSE_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
**MOUSE_MODE_MAX** = `5`

Max value of the `MouseMode<enum_Input_MouseMode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Input_CursorShape}
::: rst-class
classref-enumeration
:::
::::

enum **CursorShape**: `🔗<enum_Input_CursorShape>`{.interpreted-text
role="ref"}

:::: {#class_Input_constant_CURSOR_ARROW}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_ARROW** = `0`

Arrow cursor. Standard, default pointing cursor.

:::: {#class_Input_constant_CURSOR_IBEAM}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_IBEAM** = `1`

I-beam cursor. Usually used to show where the text cursor will appear
when the mouse is clicked.

:::: {#class_Input_constant_CURSOR_POINTING_HAND}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_POINTING_HAND** = `2`

Pointing hand cursor. Usually used to indicate the pointer is over a
link or other interactable item.

:::: {#class_Input_constant_CURSOR_CROSS}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_CROSS** = `3`

Cross cursor. Typically appears over regions in which a drawing
operation can be performed or for selections.

:::: {#class_Input_constant_CURSOR_WAIT}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_WAIT** = `4`

Wait cursor. Indicates that the application is busy performing an
operation, and that it cannot be used during the operation (e.g.
something is blocking its main thread).

:::: {#class_Input_constant_CURSOR_BUSY}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_BUSY** = `5`

Busy cursor. Indicates that the application is busy performing an
operation, and that it is still usable during the operation.

:::: {#class_Input_constant_CURSOR_DRAG}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_DRAG** = `6`

Drag cursor. Usually displayed when dragging something.

\*\*Note:\*\* Windows lacks a dragging cursor, so
`CURSOR_DRAG<class_Input_constant_CURSOR_DRAG>`{.interpreted-text
role="ref"} is the same as
`CURSOR_MOVE<class_Input_constant_CURSOR_MOVE>`{.interpreted-text
role="ref"} for this platform.

:::: {#class_Input_constant_CURSOR_CAN_DROP}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_CAN_DROP** = `7`

Can drop cursor. Usually displayed when dragging something to indicate
that it can be dropped at the current position.

:::: {#class_Input_constant_CURSOR_FORBIDDEN}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_FORBIDDEN** = `8`

Forbidden cursor. Indicates that the current action is forbidden (for
example, when dragging something) or that the control at a position is
disabled.

:::: {#class_Input_constant_CURSOR_VSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_VSIZE** = `9`

Vertical resize mouse cursor. A double-headed vertical arrow. It tells
the user they can resize the window or the panel vertically.

:::: {#class_Input_constant_CURSOR_HSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_HSIZE** = `10`

Horizontal resize mouse cursor. A double-headed horizontal arrow. It
tells the user they can resize the window or the panel horizontally.

:::: {#class_Input_constant_CURSOR_BDIAGSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_BDIAGSIZE** = `11`

Window resize mouse cursor. The cursor is a double-headed arrow that
goes from the bottom left to the top right. It tells the user they can
resize the window or the panel both horizontally and vertically.

:::: {#class_Input_constant_CURSOR_FDIAGSIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_FDIAGSIZE** = `12`

Window resize mouse cursor. The cursor is a double-headed arrow that
goes from the top left to the bottom right, the opposite of
`CURSOR_BDIAGSIZE<class_Input_constant_CURSOR_BDIAGSIZE>`{.interpreted-text
role="ref"}. It tells the user they can resize the window or the panel
both horizontally and vertically.

:::: {#class_Input_constant_CURSOR_MOVE}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_MOVE** = `13`

Move cursor. Indicates that something can be moved.

:::: {#class_Input_constant_CURSOR_VSPLIT}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_VSPLIT** = `14`

Vertical split mouse cursor. On Windows, it\'s the same as
`CURSOR_VSIZE<class_Input_constant_CURSOR_VSIZE>`{.interpreted-text
role="ref"}.

:::: {#class_Input_constant_CURSOR_HSPLIT}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_HSPLIT** = `15`

Horizontal split mouse cursor. On Windows, it\'s the same as
`CURSOR_HSIZE<class_Input_constant_CURSOR_HSIZE>`{.interpreted-text
role="ref"}.

:::: {#class_Input_constant_CURSOR_HELP}
::: rst-class
classref-enumeration-constant
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**CURSOR_HELP** = `16`

Help cursor. Usually a question mark.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Input_property_emulate_mouse_from_touch}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**emulate_mouse_from_touch**
`🔗<class_Input_property_emulate_mouse_from_touch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emulate_mouse_from_touch**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_emulating_mouse_from_touch**()

If `true`, sends mouse input events when tapping or swiping on the
touchscreen. See also
`ProjectSettings.input_devices/pointing/emulate_mouse_from_touch<class_ProjectSettings_property_input_devices/pointing/emulate_mouse_from_touch>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_property_emulate_touch_from_mouse}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**emulate_touch_from_mouse**
`🔗<class_Input_property_emulate_touch_from_mouse>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emulate_touch_from_mouse**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_emulating_touch_from_mouse**()

If `true`, sends touch input events when clicking or dragging the mouse.
See also
`ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_property_mouse_mode}
::: rst-class
classref-property
:::
::::

`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
**mouse_mode** `🔗<class_Input_property_mouse_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mouse_mode**(value:
  `MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"})
- `MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"}
  **get_mouse_mode**()

Controls the mouse mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_property_use_accumulated_input}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_accumulated_input**
`🔗<class_Input_property_use_accumulated_input>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_accumulated_input**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_accumulated_input**()

If `true`, similar input events sent by the operating system are
accumulated. When input accumulation is enabled, all input events
generated during a frame will be merged and emitted when the frame is
done rendering. Therefore, this limits the number of input method calls
per second to the rendering FPS.

Input accumulation can be disabled to get slightly more precise/reactive
input at the cost of increased CPU usage. In applications where drawing
freehand lines is required, input accumulation should generally be
disabled while the user is drawing the line to get results that closely
follow the actual input.

\*\*Note:\*\* Input accumulation is *enabled* by default.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Input_method_action_press}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**action_press**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"}, strength:
`float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_Input_method_action_press>`{.interpreted-text role="ref"}

This will simulate pressing the specified action.

The strength can be used for non-boolean actions, it\'s ranged between 0
and 1 representing the intensity of the given action.

\*\*Note:\*\* This method will not cause any
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} calls. It is intended to be used with
`is_action_pressed()<class_Input_method_is_action_pressed>`{.interpreted-text
role="ref"} and
`is_action_just_pressed()<class_Input_method_is_action_just_pressed>`{.interpreted-text
role="ref"}. If you want to simulate `_input`, use
`parse_input_event()<class_Input_method_parse_input_event>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_action_release}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**action_release**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Input_method_action_release>`{.interpreted-text role="ref"}

If the specified action is already pressed, this will release it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_add_joy_mapping}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_joy_mapping**(mapping: `String<class_String>`{.interpreted-text
role="ref"}, update_existing: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Input_method_add_joy_mapping>`{.interpreted-text role="ref"}

Adds a new mapping entry (in SDL2 format) to the mapping database.
Optionally update already connected devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_flush_buffered_events}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**flush_buffered_events**()
`🔗<class_Input_method_flush_buffered_events>`{.interpreted-text
role="ref"}

Sends all input events which are in the current buffer to the game loop.
These events may have been buffered as a result of accumulated input
(`use_accumulated_input<class_Input_property_use_accumulated_input>`{.interpreted-text
role="ref"}) or agile input flushing
(`ProjectSettings.input_devices/buffering/agile_event_flushing<class_ProjectSettings_property_input_devices/buffering/agile_event_flushing>`{.interpreted-text
role="ref"}).

The engine will already do this itself at key execution points (at least
once per frame). However, this can be useful in advanced cases where you
want precise control over the timing of event handling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_accelerometer}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_accelerometer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_get_accelerometer>`{.interpreted-text role="ref"}

Returns the acceleration in m/s² of the device\'s accelerometer sensor,
if the device has one. Otherwise, the method returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

Note this method returns an empty
`Vector3<class_Vector3>`{.interpreted-text role="ref"} when running from
the editor even when your device has an accelerometer. You must export
your project to a supported device to read values from the
accelerometer.

\*\*Note:\*\* This method only works on Android and iOS. On other
platforms, it always returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For Android,
`ProjectSettings.input_devices/sensors/enable_accelerometer<class_ProjectSettings_property_input_devices/sensors/enable_accelerometer>`{.interpreted-text
role="ref"} must be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_action_raw_strength}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_action_raw_strength**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_get_action_raw_strength>`{.interpreted-text
role="ref"}

Returns a value between 0 and 1 representing the raw intensity of the
given action, ignoring the action\'s deadzone. In most cases, you should
use
`get_action_strength()<class_Input_method_get_action_strength>`{.interpreted-text
role="ref"} instead.

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

:::: {#class_Input_method_get_action_strength}
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
`🔗<class_Input_method_get_action_strength>`{.interpreted-text
role="ref"}

Returns a value between 0 and 1 representing the intensity of the given
action. In a joypad, for example, the further away the axis (analog
sticks or L2, R2 triggers) is from the dead zone, the closer the value
will be to 1. If the action is mapped to a control that has no axis such
as the keyboard, the value returned will be 0 or 1.

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

:::: {#class_Input_method_get_axis}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_axis**(negative_action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
positive_action: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_axis>`{.interpreted-text
role="ref"}

Get axis input by specifying two actions, one negative and one positive.

This is a shorthand for writing
`Input.get_action_strength("positive_action") - Input.get_action_strength("negative_action")`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_connected_joypads}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
**get_connected_joypads**()
`🔗<class_Input_method_get_connected_joypads>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} containing
the device IDs of all currently connected joypads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_current_cursor_shape}
::: rst-class
classref-method
:::
::::

`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"}
**get_current_cursor_shape**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_get_current_cursor_shape>`{.interpreted-text
role="ref"}

Returns the currently assigned cursor shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_gravity}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **get_gravity**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_gravity>`{.interpreted-text
role="ref"}

Returns the gravity in m/s² of the device\'s accelerometer sensor, if
the device has one. Otherwise, the method returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method only works on Android and iOS. On other
platforms, it always returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For Android,
`ProjectSettings.input_devices/sensors/enable_gravity<class_ProjectSettings_property_input_devices/sensors/enable_gravity>`{.interpreted-text
role="ref"} must be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_gyroscope}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_gyroscope**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_gyroscope>`{.interpreted-text
role="ref"}

Returns the rotation rate in rad/s around a device\'s X, Y, and Z axes
of the gyroscope sensor, if the device has one. Otherwise, the method
returns `Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method only works on Android and iOS. On other
platforms, it always returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For Android,
`ProjectSettings.input_devices/sensors/enable_gyroscope<class_ProjectSettings_property_input_devices/sensors/enable_gyroscope>`{.interpreted-text
role="ref"} must be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_joy_axis}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_joy_axis**(device: `int<class_int>`{.interpreted-text role="ref"},
axis: `JoyAxis<enum_@GlobalScope_JoyAxis>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_joy_axis>`{.interpreted-text
role="ref"}

Returns the current value of the joypad axis at index `axis`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_joy_guid}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_joy_guid**(device: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_joy_guid>`{.interpreted-text
role="ref"}

Returns an SDL2-compatible device GUID on platforms that use gamepad
remapping, e.g. `030000004c050000c405000000010000`. Returns an empty
string if it cannot be found. Godot uses the [SDL2 game controller
database](https://github.com/gabomdq/SDL_GameControllerDB) to determine
gamepad names and mappings based on this GUID.

On Windows, all XInput joypad GUIDs will be overridden by Godot to
`__XINPUT_DEVICE__`, because their mappings are the same.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_joy_info}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_joy_info**(device: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_joy_info>`{.interpreted-text
role="ref"}

Returns a dictionary with extra platform-specific information about the
device, e.g. the raw gamepad name from the OS or the Steam Input index.

On Windows, the dictionary contains the following fields:

`xinput_index`: The index of the controller in the XInput system.
Undefined for DirectInput devices.

`vendor_id`: The USB vendor ID of the device.

`product_id`: The USB product ID of the device.

On Linux:

`raw_name`: The name of the controller as it came from the OS, before
getting renamed by the godot controller database.

`vendor_id`: The USB vendor ID of the device.

`product_id`: The USB product ID of the device.

`steam_input_index`: The Steam Input gamepad index, if the device is not
a Steam Input device this key won\'t be present.

\*\*Note:\*\* The returned dictionary is always empty on Web, iOS,
Android, and macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_joy_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_joy_name**(device: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Input_method_get_joy_name>`{.interpreted-text role="ref"}

Returns the name of the joypad at the specified device index, e.g.
`PS4 Controller`. Godot uses the [SDL2 game controller
database](https://github.com/gabomdq/SDL_GameControllerDB) to determine
gamepad names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_joy_vibration_duration}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_joy_vibration_duration**(device:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Input_method_get_joy_vibration_duration>`{.interpreted-text
role="ref"}

Returns the duration of the current vibration effect in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_joy_vibration_strength}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_joy_vibration_strength**(device:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Input_method_get_joy_vibration_strength>`{.interpreted-text
role="ref"}

Returns the strength of the joypad vibration: x is the strength of the
weak motor, and y is the strength of the strong motor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_last_mouse_screen_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_last_mouse_screen_velocity**()
`🔗<class_Input_method_get_last_mouse_screen_velocity>`{.interpreted-text
role="ref"}

Returns the last mouse velocity in screen coordinates. To provide a
precise and jitter-free velocity, mouse velocity is only calculated
every 0.1s. Therefore, mouse velocity will lag mouse movements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_last_mouse_velocity}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_last_mouse_velocity**()
`🔗<class_Input_method_get_last_mouse_velocity>`{.interpreted-text
role="ref"}

Returns the last mouse velocity. To provide a precise and jitter-free
velocity, mouse velocity is only calculated every 0.1s. Therefore, mouse
velocity will lag mouse movements.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_magnetometer}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_magnetometer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_magnetometer>`{.interpreted-text
role="ref"}

Returns the magnetic field strength in micro-Tesla for all axes of the
device\'s magnetometer sensor, if the device has one. Otherwise, the
method returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method only works on Android and iOS. On other
platforms, it always returns
`Vector3.ZERO<class_Vector3_constant_ZERO>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* For Android,
`ProjectSettings.input_devices/sensors/enable_magnetometer<class_ProjectSettings_property_input_devices/sensors/enable_magnetometer>`{.interpreted-text
role="ref"} must be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_mouse_button_mask}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`MouseButtonMask<enum_@GlobalScope_MouseButtonMask>`{.interpreted-text
role="ref"}\] **get_mouse_button_mask**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_get_mouse_button_mask>`{.interpreted-text
role="ref"}

Returns mouse buttons as a bitmask. If multiple mouse buttons are
pressed at the same time, the bits are added together. Equivalent to
`DisplayServer.mouse_get_button_state()<class_DisplayServer_method_mouse_get_button_state>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_get_vector}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_vector**(negative_x:
`StringName<class_StringName>`{.interpreted-text role="ref"},
positive_x: `StringName<class_StringName>`{.interpreted-text
role="ref"}, negative_y:
`StringName<class_StringName>`{.interpreted-text role="ref"},
positive_y: `StringName<class_StringName>`{.interpreted-text
role="ref"}, deadzone: `float<class_float>`{.interpreted-text
role="ref"} = -1.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_get_vector>`{.interpreted-text
role="ref"}

Gets an input vector by specifying four actions for the positive and
negative X and Y axes.

This method is useful when getting vector input, such as from a
joystick, directional pad, arrows, or WASD. The vector has its length
limited to 1 and has a circular deadzone, which is useful for using
vector input as movement.

By default, the deadzone is automatically calculated from the average of
the action deadzones. However, you can override the deadzone to be
whatever you want (on the range of 0 to 1).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_action_just_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_action_just_pressed**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_action_just_pressed>`{.interpreted-text
role="ref"}

Returns `true` when the user has *started* pressing the action event in
the current frame or physics tick. It will only return `true` on the
frame or tick that the user pressed down the button.

This is useful for code that needs to run only once when an action is
pressed, instead of every frame while it\'s pressed.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

\*\*Note:\*\* Returning `true` does not imply that the action is *still*
pressed. An action can be pressed and released again rapidly, and `true`
will still be returned so as not to miss input.

\*\*Note:\*\* Due to keyboard ghosting,
`is_action_just_pressed()<class_Input_method_is_action_just_pressed>`{.interpreted-text
role="ref"} may return `false` even if one of the action\'s keys is
pressed. See [Input
examples](../tutorials/inputs/input_examples.html#keyboard-events) in
the documentation for more information.

\*\*Note:\*\* During input handling (e.g.
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}), use
`InputEvent.is_action_pressed()<class_InputEvent_method_is_action_pressed>`{.interpreted-text
role="ref"} instead to query the action state of the current event.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_action_just_released}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_action_just_released**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_action_just_released>`{.interpreted-text
role="ref"}

Returns `true` when the user *stops* pressing the action event in the
current frame or physics tick. It will only return `true` on the frame
or tick that the user releases the button.

\*\*Note:\*\* Returning `true` does not imply that the action is *still*
not pressed. An action can be released and pressed again rapidly, and
`true` will still be returned so as not to miss input.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

\*\*Note:\*\* During input handling (e.g.
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}), use
`InputEvent.is_action_released()<class_InputEvent_method_is_action_released>`{.interpreted-text
role="ref"} instead to query the action state of the current event.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_action_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_action_pressed**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_action_pressed>`{.interpreted-text role="ref"}

Returns `true` if you are pressing the action event.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

\*\*Note:\*\* Due to keyboard ghosting,
`is_action_pressed()<class_Input_method_is_action_pressed>`{.interpreted-text
role="ref"} may return `false` even if one of the action\'s keys is
pressed. See [Input
examples](../tutorials/inputs/input_examples.html#keyboard-events) in
the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_anything_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_anything_pressed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_anything_pressed>`{.interpreted-text
role="ref"}

Returns `true` if any action, key, joypad button, or mouse button is
being pressed. This will also return `true` if any action is simulated
via code by calling
`action_press()<class_Input_method_action_press>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_joy_button_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_joy_button_pressed**(device: `int<class_int>`{.interpreted-text
role="ref"}, button:
`JoyButton<enum_@GlobalScope_JoyButton>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_joy_button_pressed>`{.interpreted-text
role="ref"}

Returns `true` if you are pressing the joypad button at index `button`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_joy_known}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_joy_known**(device: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Input_method_is_joy_known>`{.interpreted-text role="ref"}

Returns `true` if the system knows the specified device. This means that
it sets all button and axis indices. Unknown joypads are not expected to
match these constants, but you can still retrieve events from them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_key_label_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_key_label_pressed**(keycode:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_key_label_pressed>`{.interpreted-text
role="ref"}

Returns `true` if you are pressing the key with the `keycode` printed on
it. You can pass a `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} constant or any Unicode character code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_key_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_key_pressed**(keycode:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Input_method_is_key_pressed>`{.interpreted-text
role="ref"}

Returns `true` if you are pressing the Latin key in the current keyboard
layout. You can pass a `Key<enum_@GlobalScope_Key>`{.interpreted-text
role="ref"} constant.

`is_key_pressed()<class_Input_method_is_key_pressed>`{.interpreted-text
role="ref"} is only recommended over
`is_physical_key_pressed()<class_Input_method_is_physical_key_pressed>`{.interpreted-text
role="ref"} in non-game applications. This ensures that shortcut keys
behave as expected depending on the user\'s keyboard layout, as keyboard
shortcuts are generally dependent on the keyboard layout in non-game
applications. If in doubt, use
`is_physical_key_pressed()<class_Input_method_is_physical_key_pressed>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Due to keyboard ghosting,
`is_key_pressed()<class_Input_method_is_key_pressed>`{.interpreted-text
role="ref"} may return `false` even if one of the action\'s keys is
pressed. See [Input
examples](../tutorials/inputs/input_examples.html#keyboard-events) in
the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_mouse_button_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_mouse_button_pressed**(button:
`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_mouse_button_pressed>`{.interpreted-text
role="ref"}

Returns `true` if you are pressing the mouse button specified with
`MouseButton<enum_@GlobalScope_MouseButton>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_is_physical_key_pressed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_physical_key_pressed**(keycode:
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_is_physical_key_pressed>`{.interpreted-text
role="ref"}

Returns `true` if you are pressing the key in the physical location on
the 101/102-key US QWERTY keyboard. You can pass a
`Key<enum_@GlobalScope_Key>`{.interpreted-text role="ref"} constant.

`is_physical_key_pressed()<class_Input_method_is_physical_key_pressed>`{.interpreted-text
role="ref"} is recommended over
`is_key_pressed()<class_Input_method_is_key_pressed>`{.interpreted-text
role="ref"} for in-game actions, as it will make `W`{.interpreted-text
role="kbd"}/`A`{.interpreted-text role="kbd"}/`S`{.interpreted-text
role="kbd"}/`D`{.interpreted-text role="kbd"} layouts work regardless of
the user\'s keyboard layout.
`is_physical_key_pressed()<class_Input_method_is_physical_key_pressed>`{.interpreted-text
role="ref"} will also ensure that the top row number keys work on any
keyboard layout. If in doubt, use
`is_physical_key_pressed()<class_Input_method_is_physical_key_pressed>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Due to keyboard ghosting,
`is_physical_key_pressed()<class_Input_method_is_physical_key_pressed>`{.interpreted-text
role="ref"} may return `false` even if one of the action\'s keys is
pressed. See [Input
examples](../tutorials/inputs/input_examples.html#keyboard-events) in
the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_parse_input_event}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**parse_input_event**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`🔗<class_Input_method_parse_input_event>`{.interpreted-text role="ref"}

Feeds an `InputEvent<class_InputEvent>`{.interpreted-text role="ref"} to
the game. Can be used to artificially trigger input events from code.
Also generates
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} calls.

::::: tabs
::: code-tab
gdscript

var cancel_event = InputEventAction.new() cancel_event.action =
\"ui_cancel\" cancel_event.pressed = true
Input.parse_input_event(cancel_event)
:::

::: code-tab
csharp

var cancelEvent = new InputEventAction(); cancelEvent.Action =
\"ui_cancel\"; cancelEvent.Pressed = true;
Input.ParseInputEvent(cancelEvent);
:::
:::::

\*\*Note:\*\* Calling this function has no influence on the operating
system. So for example sending an
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} will not move the OS mouse cursor to the specified position
(use `warp_mouse()<class_Input_method_warp_mouse>`{.interpreted-text
role="ref"} instead) and sending `Alt/Cmd + Tab`{.interpreted-text
role="kbd"} as `InputEventKey<class_InputEventKey>`{.interpreted-text
role="ref"} won\'t toggle between active windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_remove_joy_mapping}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_joy_mapping**(guid: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_Input_method_remove_joy_mapping>`{.interpreted-text
role="ref"}

Removes all mappings from the internal database that match the given
GUID. All currently connected joypads that use this GUID will become
unmapped.

On Android, Godot will map to an internal fallback mapping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_set_accelerometer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_accelerometer**(value: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`🔗<class_Input_method_set_accelerometer>`{.interpreted-text role="ref"}

Sets the acceleration value of the accelerometer sensor. Can be used for
debugging on devices without a hardware sensor, for example in an editor
on a PC.

\*\*Note:\*\* This value can be immediately overwritten by the hardware
sensor value on Android and iOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_set_custom_mouse_cursor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_custom_mouse_cursor**(image:
`Resource<class_Resource>`{.interpreted-text role="ref"}, shape:
`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"} = 0,
hotspot: `Vector2<class_Vector2>`{.interpreted-text role="ref"} =
Vector2(0, 0))
`🔗<class_Input_method_set_custom_mouse_cursor>`{.interpreted-text
role="ref"}

Sets a custom mouse cursor image, which is only visible inside the game
window, for the given mouse `shape`. The hotspot can also be specified.
Passing `null` to the image parameter resets to the system cursor.

`image` can be either `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"} or `Image<class_Image>`{.interpreted-text role="ref"} and
its size must be lower than or equal to 256×256. To avoid rendering
issues, sizes lower than or equal to 128×128 are recommended.

`hotspot` must be within `image`\'s size.

\*\*Note:\*\* `AnimatedTexture<class_AnimatedTexture>`{.interpreted-text
role="ref"}s aren\'t supported as custom mouse cursors. If using an
`AnimatedTexture<class_AnimatedTexture>`{.interpreted-text role="ref"},
only the first frame will be displayed.

\*\*Note:\*\* The **Lossless**, **Lossy** or **Uncompressed**
compression modes are recommended. The **Video RAM** compression mode
can be used, but it will be decompressed on the CPU, which means loading
times are slowed down and no memory is saved compared to lossless modes.

\*\*Note:\*\* On the web platform, the maximum allowed cursor image size
is 128×128. Cursor images larger than 32×32 will also only be displayed
if the mouse cursor image is entirely located within the page for
[security reasons](https://chromestatus.com/feature/5825971391299584).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_set_default_cursor_shape}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_default_cursor_shape**(shape:
`CursorShape<enum_Input_CursorShape>`{.interpreted-text role="ref"} = 0)
`🔗<class_Input_method_set_default_cursor_shape>`{.interpreted-text
role="ref"}

Sets the default cursor shape to be used in the viewport instead of
`CURSOR_ARROW<class_Input_constant_CURSOR_ARROW>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If you want to change the default cursor shape for
`Control<class_Control>`{.interpreted-text role="ref"}\'s nodes, use
`Control.mouse_default_cursor_shape<class_Control_property_mouse_default_cursor_shape>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* This method generates an
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} to update cursor immediately.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_set_gravity}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gravity**(value: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Input_method_set_gravity>`{.interpreted-text
role="ref"}

Sets the gravity value of the accelerometer sensor. Can be used for
debugging on devices without a hardware sensor, for example in an editor
on a PC.

\*\*Note:\*\* This value can be immediately overwritten by the hardware
sensor value on Android and iOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_set_gyroscope}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gyroscope**(value: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Input_method_set_gyroscope>`{.interpreted-text
role="ref"}

Sets the value of the rotation rate of the gyroscope sensor. Can be used
for debugging on devices without a hardware sensor, for example in an
editor on a PC.

\*\*Note:\*\* This value can be immediately overwritten by the hardware
sensor value on Android and iOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_set_magnetometer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_magnetometer**(value: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}) `🔗<class_Input_method_set_magnetometer>`{.interpreted-text
role="ref"}

Sets the value of the magnetic field of the magnetometer sensor. Can be
used for debugging on devices without a hardware sensor, for example in
an editor on a PC.

\*\*Note:\*\* This value can be immediately overwritten by the hardware
sensor value on Android and iOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_should_ignore_device}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**should_ignore_device**(vendor_id: `int<class_int>`{.interpreted-text
role="ref"}, product_id: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Input_method_should_ignore_device>`{.interpreted-text
role="ref"}

Queries whether an input device should be ignored or not. Devices can be
ignored by setting the environment variable
`SDL_GAMECONTROLLER_IGNORE_DEVICES`. Read the [SDL
documentation](https://wiki.libsdl.org/SDL2) for more information.

\*\*Note:\*\* Some 3rd party tools can contribute to the list of ignored
devices. For example, *SteamInput* creates virtual devices from physical
devices for remapping purposes. To avoid handling the same input device
twice, the original device is added to the ignore list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_start_joy_vibration}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start_joy_vibration**(device: `int<class_int>`{.interpreted-text
role="ref"}, weak_magnitude: `float<class_float>`{.interpreted-text
role="ref"}, strong_magnitude: `float<class_float>`{.interpreted-text
role="ref"}, duration: `float<class_float>`{.interpreted-text
role="ref"} = 0)
`🔗<class_Input_method_start_joy_vibration>`{.interpreted-text
role="ref"}

Starts to vibrate the joypad. Joypads usually come with two rumble
motors, a strong and a weak one. `weak_magnitude` is the strength of the
weak motor (between 0 and 1) and `strong_magnitude` is the strength of
the strong motor (between 0 and 1). `duration` is the duration of the
effect in seconds (a duration of 0 will try to play the vibration
indefinitely). The vibration can be stopped early by calling
`stop_joy_vibration()<class_Input_method_stop_joy_vibration>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Not every hardware is compatible with long effect
durations; it is recommended to restart an effect if it has to be played
for more than a few seconds.

\*\*Note:\*\* For macOS, vibration is only supported in macOS 11 and
later.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_stop_joy_vibration}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**stop_joy_vibration**(device: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Input_method_stop_joy_vibration>`{.interpreted-text
role="ref"}

Stops the vibration of the joypad started with
`start_joy_vibration()<class_Input_method_start_joy_vibration>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_vibrate_handheld}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**vibrate_handheld**(duration_ms: `int<class_int>`{.interpreted-text
role="ref"} = 500, amplitude: `float<class_float>`{.interpreted-text
role="ref"} = -1.0)
`🔗<class_Input_method_vibrate_handheld>`{.interpreted-text role="ref"}

Vibrate the handheld device for the specified duration in milliseconds.

`amplitude` is the strength of the vibration, as a value between `0.0`
and `1.0`. If set to `-1.0`, the default vibration strength of the
device is used.

\*\*Note:\*\* This method is implemented on Android, iOS, and Web. It
has no effect on other platforms.

\*\*Note:\*\* For Android,
`vibrate_handheld()<class_Input_method_vibrate_handheld>`{.interpreted-text
role="ref"} requires enabling the `VIBRATE` permission in the export
preset. Otherwise,
`vibrate_handheld()<class_Input_method_vibrate_handheld>`{.interpreted-text
role="ref"} will have no effect.

\*\*Note:\*\* For iOS, specifying the duration is only supported in iOS
13 and later.

\*\*Note:\*\* For Web, the amplitude cannot be changed.

\*\*Note:\*\* Some web browsers such as Safari and Firefox for Android
do not support
`vibrate_handheld()<class_Input_method_vibrate_handheld>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Input_method_warp_mouse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**warp_mouse**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Input_method_warp_mouse>`{.interpreted-text
role="ref"}

Sets the mouse position to the specified vector, provided in pixels and
relative to an origin at the upper left corner of the currently focused
Window Manager game window.

Mouse position is clipped to the limits of the screen resolution, or to
the limits of the game window if
`MouseMode<enum_Input_MouseMode>`{.interpreted-text role="ref"} is set
to
`MOUSE_MODE_CONFINED<class_Input_constant_MOUSE_MODE_CONFINED>`{.interpreted-text
role="ref"} or
`MOUSE_MODE_CONFINED_HIDDEN<class_Input_constant_MOUSE_MODE_CONFINED_HIDDEN>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`warp_mouse()<class_Input_method_warp_mouse>`{.interpreted-text
role="ref"} is only supported on Windows, macOS and Linux. It has no
effect on Android, iOS and Web.
