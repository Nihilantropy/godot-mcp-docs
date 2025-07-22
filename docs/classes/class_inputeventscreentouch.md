github_url
:   hide

# InputEventScreenTouch {#class_InputEventScreenTouch}

**Inherits:**
`InputEventFromWindow<class_InputEventFromWindow>`{.interpreted-text
role="ref"} **\<** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Represents a screen touch event.

::: rst-class
classref-introduction-group
:::

## Description

Stores information about multi-touch press/release input events.
Supports touch press, touch release and
`index<class_InputEventScreenTouch_property_index>`{.interpreted-text
role="ref"} for multi-touch count and order.

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

:::: {#class_InputEventScreenTouch_property_canceled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **canceled** = `false`
`🔗<class_InputEventScreenTouch_property_canceled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_canceled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_canceled**()

If `true`, the touch event has been canceled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenTouch_property_double_tap}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **double_tap** =
`false`
`🔗<class_InputEventScreenTouch_property_double_tap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_double_tap**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_double_tap**()

If `true`, the touch\'s state is a double tap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenTouch_property_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **index** = `0`
`🔗<class_InputEventScreenTouch_property_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_index**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_index**()

The touch index in the case of a multi-touch event. One index = one
finger.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenTouch_property_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **position** =
`Vector2(0, 0)`
`🔗<class_InputEventScreenTouch_property_position>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_position**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_position**()

The touch position in the viewport the node is in, using the coordinate
system of this viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventScreenTouch_property_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pressed** = `false`
`🔗<class_InputEventScreenTouch_property_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()

If `true`, the touch\'s state is pressed. If `false`, the touch\'s state
is released.
