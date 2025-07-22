github_url
:   hide

# InputEventMouseMotion {#class_InputEventMouseMotion}

**Inherits:** `InputEventMouse<class_InputEventMouse>`{.interpreted-text
role="ref"} **\<**
`InputEventWithModifiers<class_InputEventWithModifiers>`{.interpreted-text
role="ref"} **\<**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a mouse or a pen movement.

::: rst-class
classref-introduction-group
:::

## Description

Stores information about a mouse or a pen motion. This includes relative
position, absolute position, and velocity. See
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* By default, this event is only emitted once per frame
rendered at most. If you need more precise input reporting, set
`Input.use_accumulated_input<class_Input_property_use_accumulated_input>`{.interpreted-text
role="ref"} to `false` to make events emitted as often as possible. If
you use InputEventMouseMotion to draw lines, consider using
`Geometry2D.bresenham_line()<class_Geometry2D_method_bresenham_line>`{.interpreted-text
role="ref"} as well to avoid visible gaps in lines if the user is moving
the mouse quickly.

\*\*Note:\*\* This event may be emitted even when the mouse hasn\'t
moved, either by the operating system or by Godot itself. If you really
need to know if the mouse has moved (e.g. to suppress displaying a
tooltip), you should check that `relative.is_zero_approx()` is `false`.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`{.interpreted-text
  role="doc"}
- `Mouse and input coordinates <../tutorials/inputs/mouse_and_input_coordinates>`{.interpreted-text
  role="doc"}
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

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

:::: {#class_InputEventMouseMotion_property_pen_inverted}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pen_inverted** =
`false`
`🔗<class_InputEventMouseMotion_property_pen_inverted>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pen_inverted**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_pen_inverted**()

Returns `true` when using the eraser end of a stylus pen.

\*\*Note:\*\* This property is implemented on Linux, macOS and Windows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseMotion_property_pressure}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pressure** = `0.0`
`🔗<class_InputEventMouseMotion_property_pressure>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressure**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_pressure**()

Represents the pressure the user puts on the pen. Ranges from `0.0` to
`1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseMotion_property_relative}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **relative** =
`Vector2(0, 0)`
`🔗<class_InputEventMouseMotion_property_relative>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_relative**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_relative**()

The mouse position relative to the previous position (position at the
last frame).

\*\*Note:\*\* Since **InputEventMouseMotion** may only be emitted when
the mouse moves, it is not possible to reliably detect when the mouse
has stopped moving by checking this property. A separate, short timer
may be necessary.

\*\*Note:\*\*
`relative<class_InputEventMouseMotion_property_relative>`{.interpreted-text
role="ref"} is automatically scaled according to the content scale
factor, which is defined by the project\'s stretch mode settings. This
means mouse sensitivity will appear different depending on resolution
when using
`relative<class_InputEventMouseMotion_property_relative>`{.interpreted-text
role="ref"} in a script that handles mouse aiming with the
`Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>`{.interpreted-text
role="ref"} mouse mode. To avoid this, use
`screen_relative<class_InputEventMouseMotion_property_screen_relative>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseMotion_property_screen_relative}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**screen_relative** = `Vector2(0, 0)`
`🔗<class_InputEventMouseMotion_property_screen_relative>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_relative**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_screen_relative**()

The unscaled mouse position relative to the previous position in the
coordinate system of the screen (position at the last frame).

\*\*Note:\*\* Since **InputEventMouseMotion** may only be emitted when
the mouse moves, it is not possible to reliably detect when the mouse
has stopped moving by checking this property. A separate, short timer
may be necessary.

\*\*Note:\*\* This coordinate is *not* scaled according to the content
scale factor or calls to
`InputEvent.xformed_by()<class_InputEvent_method_xformed_by>`{.interpreted-text
role="ref"}. This should be preferred over
`relative<class_InputEventMouseMotion_property_relative>`{.interpreted-text
role="ref"} for mouse aiming when using the
`Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>`{.interpreted-text
role="ref"} mouse mode, regardless of the project\'s stretch mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseMotion_property_screen_velocity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**screen_velocity** = `Vector2(0, 0)`
`🔗<class_InputEventMouseMotion_property_screen_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_velocity**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_screen_velocity**()

The unscaled mouse velocity in pixels per second in screen coordinates.
This velocity is *not* scaled according to the content scale factor or
calls to
`InputEvent.xformed_by()<class_InputEvent_method_xformed_by>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Use
`screen_relative<class_InputEventMouseMotion_property_screen_relative>`{.interpreted-text
role="ref"} for mouse aiming using the
`Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>`{.interpreted-text
role="ref"} mouse mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseMotion_property_tilt}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **tilt** =
`Vector2(0, 0)`
`🔗<class_InputEventMouseMotion_property_tilt>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tilt**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_tilt**()

Represents the angles of tilt of the pen. Positive X-coordinate value
indicates a tilt to the right. Positive Y-coordinate value indicates a
tilt toward the user. Ranges from `-1.0` to `1.0` for both axes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventMouseMotion_property_velocity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **velocity** =
`Vector2(0, 0)`
`🔗<class_InputEventMouseMotion_property_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_velocity**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_velocity**()

The mouse velocity in pixels per second.

\*\*Note:\*\*
`velocity<class_InputEventMouseMotion_property_velocity>`{.interpreted-text
role="ref"} is automatically scaled according to the content scale
factor, which is defined by the project\'s stretch mode settings. That
means mouse sensitivity may appear different depending on resolution.

\*\*Note:\*\* Use
`screen_relative<class_InputEventMouseMotion_property_screen_relative>`{.interpreted-text
role="ref"} for mouse aiming using the
`Input.MOUSE_MODE_CAPTURED<class_Input_constant_MOUSE_MODE_CAPTURED>`{.interpreted-text
role="ref"} mouse mode.
