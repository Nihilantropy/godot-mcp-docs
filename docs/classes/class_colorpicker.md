github_url
:   hide

# ColorPicker {#class_ColorPicker}

**Inherits:** `VBoxContainer<class_VBoxContainer>`{.interpreted-text
role="ref"} **\<** `BoxContainer<class_BoxContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A widget that provides an interface for selecting or modifying a color.

::: rst-class
classref-introduction-group
:::

## Description

A widget that provides an interface for selecting or modifying a color.
It can optionally provide functionalities like a color sampler
(eyedropper), color modes, and presets.

\*\*Note:\*\* This control is the color picker widget itself. You can
use a `ColorPickerButton<class_ColorPickerButton>`{.interpreted-text
role="ref"} instead if you need a button that brings up a
**ColorPicker** in a popup.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Tween Interpolation
  Demo](https://godotengine.org/asset-library/asset/2733)

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

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

:::: {#class_ColorPicker_signal_color_changed}
::: rst-class
classref-signal
:::
::::

**color_changed**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ColorPicker_signal_color_changed>`{.interpreted-text
role="ref"}

Emitted when the color is changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_signal_preset_added}
::: rst-class
classref-signal
:::
::::

**preset_added**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ColorPicker_signal_preset_added>`{.interpreted-text
role="ref"}

Emitted when a preset is added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_signal_preset_removed}
::: rst-class
classref-signal
:::
::::

**preset_removed**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ColorPicker_signal_preset_removed>`{.interpreted-text
role="ref"}

Emitted when a preset is removed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_ColorPicker_ColorModeType}
::: rst-class
classref-enumeration
:::
::::

enum **ColorModeType**:
`🔗<enum_ColorPicker_ColorModeType>`{.interpreted-text role="ref"}

:::: {#class_ColorPicker_constant_MODE_RGB}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
role="ref"} **MODE_RGB** = `0`

Allows editing the color with Red/Green/Blue sliders in sRGB color
space.

:::: {#class_ColorPicker_constant_MODE_HSV}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
role="ref"} **MODE_HSV** = `1`

Allows editing the color with Hue/Saturation/Value sliders.

:::: {#class_ColorPicker_constant_MODE_RAW}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
role="ref"} **MODE_RAW** = `2`

**Deprecated:** This is replaced by
`MODE_LINEAR<class_ColorPicker_constant_MODE_LINEAR>`{.interpreted-text
role="ref"}.

:::: {#class_ColorPicker_constant_MODE_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
role="ref"} **MODE_LINEAR** = `2`

Allows editing the color with Red/Green/Blue sliders in linear color
space.

:::: {#class_ColorPicker_constant_MODE_OKHSL}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
role="ref"} **MODE_OKHSL** = `3`

Allows editing the color with Hue/Saturation/Lightness sliders.

OKHSL is a new color space similar to HSL but that better match
perception by leveraging the Oklab color space which is designed to be
simple to use, while doing a good job at predicting perceived lightness,
chroma and hue.

\`Okhsv and Okhsl color spaces
\<https://bottosson.github.io/posts/colorpicker/\>\`\_\_

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ColorPicker_PickerShapeType}
::: rst-class
classref-enumeration
:::
::::

enum **PickerShapeType**:
`🔗<enum_ColorPicker_PickerShapeType>`{.interpreted-text role="ref"}

:::: {#class_ColorPicker_constant_SHAPE_HSV_RECTANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **SHAPE_HSV_RECTANGLE** = `0`

HSV Color Model rectangle color space.

:::: {#class_ColorPicker_constant_SHAPE_HSV_WHEEL}
::: rst-class
classref-enumeration-constant
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **SHAPE_HSV_WHEEL** = `1`

HSV Color Model rectangle color space with a wheel.

:::: {#class_ColorPicker_constant_SHAPE_VHS_CIRCLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **SHAPE_VHS_CIRCLE** = `2`

HSV Color Model circle color space. Use Saturation as a radius.

:::: {#class_ColorPicker_constant_SHAPE_OKHSL_CIRCLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **SHAPE_OKHSL_CIRCLE** = `3`

HSL OK Color Model circle color space.

:::: {#class_ColorPicker_constant_SHAPE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **SHAPE_NONE** = `4`

The color space shape and the shape select button are hidden. Can\'t be
selected from the shapes popup.

:::: {#class_ColorPicker_constant_SHAPE_OK_HS_RECTANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **SHAPE_OK_HS_RECTANGLE** = `5`

OKHSL Color Model rectangle with constant lightness.

:::: {#class_ColorPicker_constant_SHAPE_OK_HL_RECTANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **SHAPE_OK_HL_RECTANGLE** = `6`

OKHSL Color Model rectangle with constant saturation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ColorPicker_property_can_add_swatches}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_add_swatches** =
`true`
`🔗<class_ColorPicker_property_can_add_swatches>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_can_add_swatches**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **are_swatches_enabled**()

If `true`, it\'s possible to add presets under Swatches. If `false`, the
button to add presets is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(1, 1, 1, 1)`
`🔗<class_ColorPicker_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pick_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_pick_color**()

The currently selected color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_color_mode}
::: rst-class
classref-property
:::
::::

`ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
role="ref"} **color_mode** = `0`
`🔗<class_ColorPicker_property_color_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_mode**(value:
  `ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
  role="ref"})
- `ColorModeType<enum_ColorPicker_ColorModeType>`{.interpreted-text
  role="ref"} **get_color_mode**()

The currently selected color mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_color_modes_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **color_modes_visible**
= `true`
`🔗<class_ColorPicker_property_color_modes_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modes_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **are_modes_visible**()

If `true`, the color mode buttons are visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_deferred_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **deferred_mode** =
`false` `🔗<class_ColorPicker_property_deferred_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_deferred_mode**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_deferred_mode**()

If `true`, the color will apply only after the user releases the mouse
button, otherwise it will apply immediately even in mouse motion event
(which can cause performance issues).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_edit_alpha}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **edit_alpha** = `true`
`🔗<class_ColorPicker_property_edit_alpha>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edit_alpha**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_editing_alpha**()

If `true`, shows an alpha channel slider (opacity).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_edit_intensity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **edit_intensity** =
`true` `🔗<class_ColorPicker_property_edit_intensity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edit_intensity**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_editing_intensity**()

If `true`, shows an intensity slider. The intensity is applied as
follows: multiply the color by `2 ** intensity` in linear RGB space, and
then convert it back to sRGB.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_hex_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hex_visible** =
`true` `🔗<class_ColorPicker_property_hex_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hex_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_hex_visible**()

If `true`, the hex color code input field is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_picker_shape}
::: rst-class
classref-property
:::
::::

`PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
role="ref"} **picker_shape** = `0`
`🔗<class_ColorPicker_property_picker_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_picker_shape**(value:
  `PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
  role="ref"})
- `PickerShapeType<enum_ColorPicker_PickerShapeType>`{.interpreted-text
  role="ref"} **get_picker_shape**()

The shape of the color space view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_presets_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **presets_visible** =
`true`
`🔗<class_ColorPicker_property_presets_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_presets_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **are_presets_visible**()

If `true`, the Swatches and Recent Colors presets are visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_sampler_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sampler_visible** =
`true`
`🔗<class_ColorPicker_property_sampler_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sampler_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_sampler_visible**()

If `true`, the color sampler and color preview are visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_property_sliders_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **sliders_visible** =
`true`
`🔗<class_ColorPicker_property_sliders_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sliders_visible**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **are_sliders_visible**()

If `true`, the color sliders are visible.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ColorPicker_method_add_preset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_preset**(color: `Color<class_Color>`{.interpreted-text
role="ref"}) `🔗<class_ColorPicker_method_add_preset>`{.interpreted-text
role="ref"}

Adds the given color to a list of color presets. The presets are
displayed in the color picker and the user will be able to select them.

\*\*Note:\*\* The presets list is only for *this* color picker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_method_add_recent_preset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_recent_preset**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ColorPicker_method_add_recent_preset>`{.interpreted-text
role="ref"}

Adds the given color to a list of color recent presets so that it can be
picked later. Recent presets are the colors that were picked recently, a
new preset is automatically created and added to recent presets when you
pick a new color.

\*\*Note:\*\* The recent presets list is only for *this* color picker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_method_erase_preset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_preset**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ColorPicker_method_erase_preset>`{.interpreted-text
role="ref"}

Removes the given color from the list of color presets of this color
picker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_method_erase_recent_preset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_recent_preset**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ColorPicker_method_erase_recent_preset>`{.interpreted-text
role="ref"}

Removes the given color from the list of color recent presets of this
color picker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_method_get_presets}
::: rst-class
classref-method
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**get_presets**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ColorPicker_method_get_presets>`{.interpreted-text role="ref"}

Returns the list of colors in the presets of the color picker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_method_get_recent_presets}
::: rst-class
classref-method
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**get_recent_presets**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ColorPicker_method_get_recent_presets>`{.interpreted-text
role="ref"}

Returns the list of colors in the recent presets of the color picker.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_ColorPicker_theme_color_focused_not_editing_cursor_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**focused_not_editing_cursor_color** = `Color(1, 1, 1, 0.275)`
`🔗<class_ColorPicker_theme_color_focused_not_editing_cursor_color>`{.interpreted-text
role="ref"}

Color of rectangle or circle drawn when a picker shape part is focused
but not editable via keyboard or joypad. Displayed *over* the picker
shape, so a partially transparent color should be used to ensure the
picker shape remains visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_constant_center_slider_grabbers}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**center_slider_grabbers** = `1`
`🔗<class_ColorPicker_theme_constant_center_slider_grabbers>`{.interpreted-text
role="ref"}

Overrides the
`Slider.center_grabber<class_Slider_theme_constant_center_grabber>`{.interpreted-text
role="ref"} theme property of the sliders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_constant_h_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_width** = `30`
`🔗<class_ColorPicker_theme_constant_h_width>`{.interpreted-text
role="ref"}

The width of the hue selection slider.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_constant_label_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **label_width** = `10`
`🔗<class_ColorPicker_theme_constant_label_width>`{.interpreted-text
role="ref"}

The minimum width of the color labels next to sliders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_constant_margin}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **margin** = `4`
`🔗<class_ColorPicker_theme_constant_margin>`{.interpreted-text
role="ref"}

The margin around the **ColorPicker**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_constant_sv_height}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sv_height** = `256`
`🔗<class_ColorPicker_theme_constant_sv_height>`{.interpreted-text
role="ref"}

The height of the saturation-value selection box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_constant_sv_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sv_width** = `256`
`🔗<class_ColorPicker_theme_constant_sv_width>`{.interpreted-text
role="ref"}

The width of the saturation-value selection box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_add_preset}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**add_preset**
`🔗<class_ColorPicker_theme_icon_add_preset>`{.interpreted-text
role="ref"}

The icon for the \"Add Preset\" button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_bar_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **bar_arrow**
`🔗<class_ColorPicker_theme_icon_bar_arrow>`{.interpreted-text
role="ref"}

The texture for the arrow grabber.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_color_hue}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **color_hue**
`🔗<class_ColorPicker_theme_icon_color_hue>`{.interpreted-text
role="ref"}

Custom texture for the hue selection slider on the right.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_color_script}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**color_script**
`🔗<class_ColorPicker_theme_icon_color_script>`{.interpreted-text
role="ref"}

The icon for the button that switches color text to hexadecimal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_expanded_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**expanded_arrow**
`🔗<class_ColorPicker_theme_icon_expanded_arrow>`{.interpreted-text
role="ref"}

The icon for color preset drop down menu when expanded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_folded_arrow}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**folded_arrow**
`🔗<class_ColorPicker_theme_icon_folded_arrow>`{.interpreted-text
role="ref"}

The icon for color preset drop down menu when folded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_menu_option}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**menu_option**
`🔗<class_ColorPicker_theme_icon_menu_option>`{.interpreted-text
role="ref"}

The icon for color preset option menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_overbright_indicator}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**overbright_indicator**
`🔗<class_ColorPicker_theme_icon_overbright_indicator>`{.interpreted-text
role="ref"}

The indicator used to signalize that the color value is outside the 0-1
range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_picker_cursor}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**picker_cursor**
`🔗<class_ColorPicker_theme_icon_picker_cursor>`{.interpreted-text
role="ref"}

The image displayed over the color box/circle (depending on the
`picker_shape<class_ColorPicker_property_picker_shape>`{.interpreted-text
role="ref"}), marking the currently selected color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_picker_cursor_bg}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**picker_cursor_bg**
`🔗<class_ColorPicker_theme_icon_picker_cursor_bg>`{.interpreted-text
role="ref"}

The fill image displayed behind the picker cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_sample_bg}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **sample_bg**
`🔗<class_ColorPicker_theme_icon_sample_bg>`{.interpreted-text
role="ref"}

Background panel for the color preview box (visible when the color is
translucent).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_sample_revert}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**sample_revert**
`🔗<class_ColorPicker_theme_icon_sample_revert>`{.interpreted-text
role="ref"}

The icon for the revert button (visible on the middle of the \"old\"
color when it differs from the currently selected color). This icon is
modulated with a dark color if the \"old\" color is bright enough, so
the icon should be bright to ensure visibility in both scenarios.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_screen_picker}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**screen_picker**
`🔗<class_ColorPicker_theme_icon_screen_picker>`{.interpreted-text
role="ref"}

The icon for the screen color picker button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_shape_circle}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**shape_circle**
`🔗<class_ColorPicker_theme_icon_shape_circle>`{.interpreted-text
role="ref"}

The icon for circular picker shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_shape_rect}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**shape_rect**
`🔗<class_ColorPicker_theme_icon_shape_rect>`{.interpreted-text
role="ref"}

The icon for rectangular picker shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_icon_shape_rect_wheel}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**shape_rect_wheel**
`🔗<class_ColorPicker_theme_icon_shape_rect_wheel>`{.interpreted-text
role="ref"}

The icon for rectangular wheel picker shapes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_style_picker_focus_circle}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**picker_focus_circle**
`🔗<class_ColorPicker_theme_style_picker_focus_circle>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when
the circle-shaped part of the picker is focused. Displayed *over* the
picker shape, so a partially transparent
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} should be used
to ensure the picker shape remains visible. A
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that represents
an outline or an underline works well for this purpose. To disable the
focus visual effect, assign a
`StyleBoxEmpty<class_StyleBoxEmpty>`{.interpreted-text role="ref"}
resource. Note that disabling the focus visual effect will harm
keyboard/controller navigation usability, so this is not recommended for
accessibility reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_style_picker_focus_rectangle}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**picker_focus_rectangle**
`🔗<class_ColorPicker_theme_style_picker_focus_rectangle>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when
the rectangle-shaped part of the picker is focused. Displayed *over* the
picker shape, so a partially transparent
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} should be used
to ensure the picker shape remains visible. A
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that represents
an outline or an underline works well for this purpose. To disable the
focus visual effect, assign a
`StyleBoxEmpty<class_StyleBoxEmpty>`{.interpreted-text role="ref"}
resource. Note that disabling the focus visual effect will harm
keyboard/controller navigation usability, so this is not recommended for
accessibility reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPicker_theme_style_sample_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**sample_focus**
`🔗<class_ColorPicker_theme_style_sample_focus>`{.interpreted-text
role="ref"}

The `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used for
the old color sample part when it is focused. Displayed *over* the
sample, so a partially transparent
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} should be used
to ensure the picker shape remains visible. A
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that represents
an outline or an underline works well for this purpose. To disable the
focus visual effect, assign a
`StyleBoxEmpty<class_StyleBoxEmpty>`{.interpreted-text role="ref"}
resource. Note that disabling the focus visual effect will harm
keyboard/controller navigation usability, so this is not recommended for
accessibility reasons.
