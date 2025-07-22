github_url
:   hide

# ColorPickerButton {#class_ColorPickerButton}

**Inherits:** `Button<class_Button>`{.interpreted-text role="ref"}
**\<** `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A button that brings up a
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"} when
pressed.

::: rst-class
classref-introduction-group
:::

## Description

Encapsulates a `ColorPicker<class_ColorPicker>`{.interpreted-text
role="ref"}, making it accessible by pressing a button. Pressing the
button will toggle the
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}\'s
visibility.

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

\*\*Note:\*\* By default, the button may not be wide enough for the
color preview swatch to be visible. Make sure to set
`Control.custom_minimum_size<class_Control_property_custom_minimum_size>`{.interpreted-text
role="ref"} to a big enough value to give the button enough space.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D GD Paint Demo](https://godotengine.org/asset-library/asset/2768)
- [GUI Drag And Drop
  Demo](https://godotengine.org/asset-library/asset/2767)

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

:::: {#class_ColorPickerButton_signal_color_changed}
::: rst-class
classref-signal
:::
::::

**color_changed**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_ColorPickerButton_signal_color_changed>`{.interpreted-text
role="ref"}

Emitted when the color changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPickerButton_signal_picker_created}
::: rst-class
classref-signal
:::
::::

**picker_created**()
`🔗<class_ColorPickerButton_signal_picker_created>`{.interpreted-text
role="ref"}

Emitted when the `ColorPicker<class_ColorPicker>`{.interpreted-text
role="ref"} is created (the button is pressed for the first time).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPickerButton_signal_popup_closed}
::: rst-class
classref-signal
:::
::::

**popup_closed**()
`🔗<class_ColorPickerButton_signal_popup_closed>`{.interpreted-text
role="ref"}

Emitted when the `ColorPicker<class_ColorPicker>`{.interpreted-text
role="ref"} is closed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ColorPickerButton_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(0, 0, 0, 1)`
`🔗<class_ColorPickerButton_property_color>`{.interpreted-text
role="ref"}

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

:::: {#class_ColorPickerButton_property_edit_alpha}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **edit_alpha** = `true`
`🔗<class_ColorPickerButton_property_edit_alpha>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edit_alpha**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_editing_alpha**()

If `true`, the alpha channel in the displayed
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"} will be
visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPickerButton_property_edit_intensity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **edit_intensity** =
`true`
`🔗<class_ColorPickerButton_property_edit_intensity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edit_intensity**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_editing_intensity**()

If `true`, the intensity slider in the displayed
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"} will be
visible.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ColorPickerButton_method_get_picker}
::: rst-class
classref-method
:::
::::

`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}
**get_picker**()
`🔗<class_ColorPickerButton_method_get_picker>`{.interpreted-text
role="ref"}

Returns the `ColorPicker<class_ColorPicker>`{.interpreted-text
role="ref"} that this node toggles.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ColorPickerButton_method_get_popup}
::: rst-class
classref-method
:::
::::

`PopupPanel<class_PopupPanel>`{.interpreted-text role="ref"}
**get_popup**()
`🔗<class_ColorPickerButton_method_get_popup>`{.interpreted-text
role="ref"}

Returns the control\'s `PopupPanel<class_PopupPanel>`{.interpreted-text
role="ref"} which allows you to connect to popup signals. This allows
you to handle events when the ColorPicker is shown or hidden.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their `Window.visible<class_Window_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_ColorPickerButton_theme_icon_bg}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **bg**
`🔗<class_ColorPickerButton_theme_icon_bg>`{.interpreted-text
role="ref"}

The background of the color preview rect on the button.
