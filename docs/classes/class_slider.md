github_url
:   hide

# Slider {#class_Slider}

**Inherits:** `Range<class_Range>`{.interpreted-text role="ref"} **\<**
`Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `HSlider<class_HSlider>`{.interpreted-text
role="ref"}, `VSlider<class_VSlider>`{.interpreted-text role="ref"}

Abstract base class for sliders.

::: rst-class
classref-introduction-group
:::

## Description

Abstract base class for sliders, used to adjust a value by moving a
grabber along a horizontal or vertical axis. Sliders are
`Range<class_Range>`{.interpreted-text role="ref"}-based controls.

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

:::: {#class_Slider_signal_drag_ended}
::: rst-class
classref-signal
:::
::::

**drag_ended**(value_changed: `bool<class_bool>`{.interpreted-text
role="ref"}) `🔗<class_Slider_signal_drag_ended>`{.interpreted-text
role="ref"}

Emitted when the grabber stops being dragged. If `value_changed` is
`true`, `Range.value<class_Range_property_value>`{.interpreted-text
role="ref"} is different from the value when the dragging was started.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_signal_drag_started}
::: rst-class
classref-signal
:::
::::

**drag_started**()
`🔗<class_Slider_signal_drag_started>`{.interpreted-text role="ref"}

Emitted when the grabber starts being dragged. This is emitted before
the corresponding
`Range.value_changed<class_Range_signal_value_changed>`{.interpreted-text
role="ref"} signal.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Slider_TickPosition}
::: rst-class
classref-enumeration
:::
::::

enum **TickPosition**: `🔗<enum_Slider_TickPosition>`{.interpreted-text
role="ref"}

:::: {#class_Slider_constant_TICK_POSITION_BOTTOM_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`TickPosition<enum_Slider_TickPosition>`{.interpreted-text role="ref"}
**TICK_POSITION_BOTTOM_RIGHT** = `0`

Places the ticks at the bottom of the
`HSlider<class_HSlider>`{.interpreted-text role="ref"}, or right of the
`VSlider<class_VSlider>`{.interpreted-text role="ref"}.

:::: {#class_Slider_constant_TICK_POSITION_TOP_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`TickPosition<enum_Slider_TickPosition>`{.interpreted-text role="ref"}
**TICK_POSITION_TOP_LEFT** = `1`

Places the ticks at the top of the
`HSlider<class_HSlider>`{.interpreted-text role="ref"}, or left of the
`VSlider<class_VSlider>`{.interpreted-text role="ref"}.

:::: {#class_Slider_constant_TICK_POSITION_BOTH}
::: rst-class
classref-enumeration-constant
:::
::::

`TickPosition<enum_Slider_TickPosition>`{.interpreted-text role="ref"}
**TICK_POSITION_BOTH** = `2`

Places the ticks at the both sides of the slider.

:::: {#class_Slider_constant_TICK_POSITION_CENTER}
::: rst-class
classref-enumeration-constant
:::
::::

`TickPosition<enum_Slider_TickPosition>`{.interpreted-text role="ref"}
**TICK_POSITION_CENTER** = `3`

Places the ticks at the center of the slider.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Slider_property_editable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editable** = `true`
`🔗<class_Slider_property_editable>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_editable**()

If `true`, the slider can be interacted with. If `false`, the value can
be changed only by code.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_property_scrollable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **scrollable** = `true`
`🔗<class_Slider_property_scrollable>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scrollable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_scrollable**()

If `true`, the value can be changed using the mouse wheel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_property_tick_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tick_count** = `0`
`🔗<class_Slider_property_tick_count>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ticks**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_ticks**()

Number of ticks displayed on the slider, including border ticks. Ticks
are uniformly-distributed value markers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_property_ticks_on_borders}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ticks_on_borders** =
`false` `🔗<class_Slider_property_ticks_on_borders>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ticks_on_borders**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_ticks_on_borders**()

If `true`, the slider will display ticks for minimum and maximum values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_property_ticks_position}
::: rst-class
classref-property
:::
::::

`TickPosition<enum_Slider_TickPosition>`{.interpreted-text role="ref"}
**ticks_position** = `0`
`🔗<class_Slider_property_ticks_position>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ticks_position**(value:
  `TickPosition<enum_Slider_TickPosition>`{.interpreted-text
  role="ref"})
- `TickPosition<enum_Slider_TickPosition>`{.interpreted-text role="ref"}
  **get_ticks_position**()

Sets the position of the ticks. See
`TickPosition<enum_Slider_TickPosition>`{.interpreted-text role="ref"}
for details.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_Slider_theme_constant_center_grabber}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **center_grabber** = `0`
`🔗<class_Slider_theme_constant_center_grabber>`{.interpreted-text
role="ref"}

Boolean constant. If `1`, the grabber texture size will be ignored and
it will fit within slider\'s bounds based only on its center position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_constant_grabber_offset}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **grabber_offset** = `0`
`🔗<class_Slider_theme_constant_grabber_offset>`{.interpreted-text
role="ref"}

Vertical or horizontal offset of the grabber.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_constant_tick_offset}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tick_offset** = `0`
`🔗<class_Slider_theme_constant_tick_offset>`{.interpreted-text
role="ref"}

Vertical or horizontal offset of the ticks. The offset is reversed for
top or left ticks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_icon_grabber}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **grabber**
`🔗<class_Slider_theme_icon_grabber>`{.interpreted-text role="ref"}

The texture for the grabber (the draggable element).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_icon_grabber_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**grabber_disabled**
`🔗<class_Slider_theme_icon_grabber_disabled>`{.interpreted-text
role="ref"}

The texture for the grabber when it\'s disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_icon_grabber_highlight}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**grabber_highlight**
`🔗<class_Slider_theme_icon_grabber_highlight>`{.interpreted-text
role="ref"}

The texture for the grabber when it\'s focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_icon_tick}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **tick**
`🔗<class_Slider_theme_icon_tick>`{.interpreted-text role="ref"}

The texture for the ticks, visible when
`tick_count<class_Slider_property_tick_count>`{.interpreted-text
role="ref"} is greater than 0.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_style_grabber_area}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**grabber_area**
`🔗<class_Slider_theme_style_grabber_area>`{.interpreted-text
role="ref"}

The background of the area to the left or bottom of the grabber.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_style_grabber_area_highlight}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**grabber_area_highlight**
`🔗<class_Slider_theme_style_grabber_area_highlight>`{.interpreted-text
role="ref"}

The background of the area to the left or bottom of the grabber that
displays when it\'s being hovered or focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Slider_theme_style_slider}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **slider**
`🔗<class_Slider_theme_style_slider>`{.interpreted-text role="ref"}

The background for the whole slider. Affects the height or width of the
`grabber_area<class_Slider_theme_style_grabber_area>`{.interpreted-text
role="ref"}.
