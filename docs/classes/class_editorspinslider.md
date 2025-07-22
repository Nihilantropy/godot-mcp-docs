github_url
:   hide

# EditorSpinSlider {#class_EditorSpinSlider}

**Inherits:** `Range<class_Range>`{.interpreted-text role="ref"} **\<**
`Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Godot editor\'s control for editing numeric values.

::: rst-class
classref-introduction-group
:::

## Description

This `Control<class_Control>`{.interpreted-text role="ref"} node is used
in the editor\'s Inspector dock to allow editing of numeric values. Can
be used with
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"} to recreate the same behavior.

If the `Range.step<class_Range_property_step>`{.interpreted-text
role="ref"} value is `1`, the **EditorSpinSlider** will display up/down
arrows, similar to `SpinBox<class_SpinBox>`{.interpreted-text
role="ref"}. If the
`Range.step<class_Range_property_step>`{.interpreted-text role="ref"}
value is not `1`, a slider will be displayed instead.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_EditorSpinSlider_signal_grabbed}
::: rst-class
classref-signal
:::
::::

**grabbed**()
`🔗<class_EditorSpinSlider_signal_grabbed>`{.interpreted-text
role="ref"}

Emitted when the spinner/slider is grabbed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_signal_ungrabbed}
::: rst-class
classref-signal
:::
::::

**ungrabbed**()
`🔗<class_EditorSpinSlider_signal_ungrabbed>`{.interpreted-text
role="ref"}

Emitted when the spinner/slider is ungrabbed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_signal_updown_pressed}
::: rst-class
classref-signal
:::
::::

**updown_pressed**()
`🔗<class_EditorSpinSlider_signal_updown_pressed>`{.interpreted-text
role="ref"}

Emitted when the updown button is pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_signal_value_focus_entered}
::: rst-class
classref-signal
:::
::::

**value_focus_entered**()
`🔗<class_EditorSpinSlider_signal_value_focus_entered>`{.interpreted-text
role="ref"}

Emitted when the value form gains focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_signal_value_focus_exited}
::: rst-class
classref-signal
:::
::::

**value_focus_exited**()
`🔗<class_EditorSpinSlider_signal_value_focus_exited>`{.interpreted-text
role="ref"}

Emitted when the value form loses focus.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EditorSpinSlider_property_editing_integer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editing_integer** =
`false`
`🔗<class_EditorSpinSlider_property_editing_integer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editing_integer**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_editing_integer**()

If `true`, the **EditorSpinSlider** is considered to be editing an
integer value. If `false`, the **EditorSpinSlider** is considered to be
editing a floating-point value. This is used to determine whether a
slider should be drawn. The slider is only drawn for floats; integers
use up-down arrows similar to `SpinBox<class_SpinBox>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_property_flat}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flat** = `false`
`🔗<class_EditorSpinSlider_property_flat>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flat**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flat**()

If `true`, the slider will not draw background.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_property_hide_slider}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hide_slider** =
`false`
`🔗<class_EditorSpinSlider_property_hide_slider>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hide_slider**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hiding_slider**()

If `true`, the slider and up/down arrows are hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_property_label}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **label** = `""`
`🔗<class_EditorSpinSlider_property_label>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_label**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_label**()

The text that displays to the left of the value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_property_read_only}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **read_only** = `false`
`🔗<class_EditorSpinSlider_property_read_only>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_read_only**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_read_only**()

If `true`, the slider can\'t be interacted with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_property_suffix}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **suffix** = `""`
`🔗<class_EditorSpinSlider_property_suffix>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_suffix**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_suffix**()

The suffix to display after the value (in a faded color). This should
generally be a plural word. You may have to use an abbreviation if the
suffix is too long to be displayed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_EditorSpinSlider_theme_icon_updown}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **updown**
`🔗<class_EditorSpinSlider_theme_icon_updown>`{.interpreted-text
role="ref"}

Single texture representing both the up and down buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSpinSlider_theme_icon_updown_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**updown_disabled**
`🔗<class_EditorSpinSlider_theme_icon_updown_disabled>`{.interpreted-text
role="ref"}

Single texture representing both the up and down buttons, when the
control is readonly or disabled.
