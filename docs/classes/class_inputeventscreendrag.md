github_url
:   hide

# InputEventScreenDrag {#class_InputEventScreenDrag}

**Inherits:**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a screen drag event.

::: rst-class
classref-introduction-group
:::

## Description

Stores information about screen drag events. See
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using InputEvent <../tutorials/inputs/inputevent>`{.interpreted-text
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

:::: {#class_InputEventScreenDrag_property_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **index** = `0`
`🔗<class_InputEventScreenDrag_property_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_index**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_index**()

The drag event index in the case of a multi-drag event.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenDrag_property_pen_inverted}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pen_inverted** =
`false`
`🔗<class_InputEventScreenDrag_property_pen_inverted>`{.interpreted-text
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

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenDrag_property_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **position** =
`Vector2(0, 0)`
`🔗<class_InputEventScreenDrag_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_position**()

The drag position in the viewport the node is in, using the coordinate
system of this viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenDrag_property_pressure}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pressure** = `0.0`
`🔗<class_InputEventScreenDrag_property_pressure>`{.interpreted-text
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

:::: {#class_InputEventScreenDrag_property_relative}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **relative** =
`Vector2(0, 0)`
`🔗<class_InputEventScreenDrag_property_relative>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_relative**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_relative**()

The drag position relative to the previous position (position at the
last frame).

\*\*Note:\*\*
`relative<class_InputEventScreenDrag_property_relative>`{.interpreted-text
role="ref"} is automatically scaled according to the content scale
factor, which is defined by the project\'s stretch mode settings. This
means touch sensitivity will appear different depending on resolution
when using
`relative<class_InputEventScreenDrag_property_relative>`{.interpreted-text
role="ref"} in a script that handles touch aiming. To avoid this, use
`screen_relative<class_InputEventScreenDrag_property_screen_relative>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenDrag_property_screen_relative}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**screen_relative** = `Vector2(0, 0)`
`🔗<class_InputEventScreenDrag_property_screen_relative>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_relative**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_screen_relative**()

The unscaled drag position relative to the previous position in screen
coordinates (position at the last frame). This position is *not* scaled
according to the content scale factor or calls to
`InputEvent.xformed_by()<class_InputEvent_method_xformed_by>`{.interpreted-text
role="ref"}. This should be preferred over
`relative<class_InputEventScreenDrag_property_relative>`{.interpreted-text
role="ref"} for touch aiming regardless of the project\'s stretch mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenDrag_property_screen_velocity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**screen_velocity** = `Vector2(0, 0)`
`🔗<class_InputEventScreenDrag_property_screen_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_velocity**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_screen_velocity**()

The unscaled drag velocity in pixels per second in screen coordinates.
This velocity is *not* scaled according to the content scale factor or
calls to
`InputEvent.xformed_by()<class_InputEvent_method_xformed_by>`{.interpreted-text
role="ref"}. This should be preferred over
`velocity<class_InputEventScreenDrag_property_velocity>`{.interpreted-text
role="ref"} for touch aiming regardless of the project\'s stretch mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenDrag_property_tilt}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **tilt** =
`Vector2(0, 0)`
`🔗<class_InputEventScreenDrag_property_tilt>`{.interpreted-text
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

:::: {#class_InputEventScreenDrag_property_velocity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **velocity** =
`Vector2(0, 0)`
`🔗<class_InputEventScreenDrag_property_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_velocity**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_velocity**()

The drag velocity.

\*\*Note:\*\*
`velocity<class_InputEventScreenDrag_property_velocity>`{.interpreted-text
role="ref"} is automatically scaled according to the content scale
factor, which is defined by the project\'s stretch mode settings. This
means touch sensitivity will appear different depending on resolution
when using
`velocity<class_InputEventScreenDrag_property_velocity>`{.interpreted-text
role="ref"} in a script that handles touch aiming. To avoid this, use
`screen_velocity<class_InputEventScreenDrag_property_screen_velocity>`{.interpreted-text
role="ref"} instead.
