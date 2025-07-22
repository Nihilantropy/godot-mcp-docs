github_url
:   hide

::: {.meta keywords="number, numeric, input"}
:::

# SpinBox {#class_SpinBox}

**Inherits:** `Range<class_Range>`{.interpreted-text role="ref"} **\<**
`Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An input field for numbers.

::: rst-class
classref-introduction-group
:::

## Description

**SpinBox** is a numerical input text field. It allows entering integers
and floating-point numbers. The **SpinBox** also has up and down buttons
that can be clicked increase or decrease the value. The value can also
be changed by dragging the mouse up or down over the **SpinBox**\'s
arrows.

Additionally, mathematical expressions can be entered. These are
evaluated when the user presses `Enter`{.interpreted-text role="kbd"}
while editing the **SpinBox**\'s text field. This uses the
`Expression<class_Expression>`{.interpreted-text role="ref"} class to
parse and evaluate the expression. The result of the expression is then
set as the value of the **SpinBox**. Some examples of valid expressions
are `5 + 2 * 3`, `pow(2, 4)`, and `PI + sin(0.5)`. Expressions are
case-sensitive.

\*\*Example:\*\* Create a **SpinBox**, disable its context menu and set
its text alignment to right.

::::: tabs
::: code-tab
gdscript

var spin_box = SpinBox.new() add_child(spin_box) var line_edit =
spin_box.get_line_edit() line_edit.context_menu_enabled = false
spin_box.horizontal_alignment = LineEdit.HORIZONTAL_ALIGNMENT_RIGHT
:::

::: code-tab
csharp

var spinBox = new SpinBox(); AddChild(spinBox); var lineEdit =
spinBox.GetLineEdit(); lineEdit.ContextMenuEnabled = false;
spinBox.AlignHorizontal = LineEdit.HorizontalAlignEnum.Right;
:::
:::::

See `Range<class_Range>`{.interpreted-text role="ref"} class for more
options over the **SpinBox**.

\*\*Note:\*\* With the **SpinBox**\'s context menu disabled, you can
right-click the bottom half of the spinbox to set the value to its
minimum, while right-clicking the top half sets the value to its
maximum.

\*\*Note:\*\* **SpinBox** relies on an underlying
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} node. To theme
a **SpinBox**\'s background, add theme items for
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} and customize
them. The `LineEdit<class_LineEdit>`{.interpreted-text role="ref"} has
the `SpinBoxInnerLineEdit` theme variation, so that you can give it a
distinct appearance from regular
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}s.

\*\*Note:\*\* If you want to implement drag and drop for the underlying
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}, you can use
`Control.set_drag_forwarding()<class_Control_method_set_drag_forwarding>`{.interpreted-text
role="ref"} on the node returned by
`get_line_edit()<class_SpinBox_method_get_line_edit>`{.interpreted-text
role="ref"}.

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

## Property Descriptions

:::: {#class_SpinBox_property_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **alignment** = `0`
`🔗<class_SpinBox_property_alignment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_horizontal_alignment**()

Changes the alignment of the underlying
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_property_custom_arrow_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **custom_arrow_step**
= `0.0` `🔗<class_SpinBox_property_custom_arrow_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_arrow_step**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_custom_arrow_step**()

If not `0`, sets the step when interacting with the arrow buttons of the
**SpinBox**.

\*\*Note:\*\*
`Range.value<class_Range_property_value>`{.interpreted-text role="ref"}
will still be rounded to a multiple of
`step<class_SpinBox_property_step>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_property_editable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editable** = `true`
`🔗<class_SpinBox_property_editable>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_editable**()

If `true`, the **SpinBox** will be editable. Otherwise, it will be read
only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_property_prefix}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **prefix** = `""`
`🔗<class_SpinBox_property_prefix>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_prefix**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_prefix**()

Adds the specified prefix string before the numerical value of the
**SpinBox**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_property_select_all_on_focus}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **select_all_on_focus**
= `false`
`🔗<class_SpinBox_property_select_all_on_focus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_select_all_on_focus**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_select_all_on_focus**()

If `true`, the **SpinBox** will select the whole text when the
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} gains focus.
Clicking the up and down arrows won\'t trigger this behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_property_suffix}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **suffix** = `""`
`🔗<class_SpinBox_property_suffix>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_suffix**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_suffix**()

Adds the specified suffix string after the numerical value of the
**SpinBox**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_property_update_on_text_changed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**update_on_text_changed** = `false`
`🔗<class_SpinBox_property_update_on_text_changed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_update_on_text_changed**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_update_on_text_changed**()

Sets the value of the `Range<class_Range>`{.interpreted-text role="ref"}
for this **SpinBox** when the
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} text is
*changed* instead of *submitted*. See
`LineEdit.text_changed<class_LineEdit_signal_text_changed>`{.interpreted-text
role="ref"} and
`LineEdit.text_submitted<class_LineEdit_signal_text_submitted>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If set to `true`, this will interfere with entering
mathematical expressions in the **SpinBox**. The **SpinBox** will try to
evaluate the expression as you type, which means symbols like a trailing
`+` are removed immediately by the expression being evaluated.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SpinBox_method_apply}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **apply**()
`🔗<class_SpinBox_method_apply>`{.interpreted-text role="ref"}

Applies the current value of this **SpinBox**. This is equivalent to
pressing `Enter`{.interpreted-text role="kbd"} while editing the
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"} used by the
**SpinBox**. This will cause
`LineEdit.text_submitted<class_LineEdit_signal_text_submitted>`{.interpreted-text
role="ref"} to be emitted and its currently contained expression to be
evaluated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_method_get_line_edit}
::: rst-class
classref-method
:::
::::

`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}
**get_line_edit**()
`🔗<class_SpinBox_method_get_line_edit>`{.interpreted-text role="ref"}

Returns the `LineEdit<class_LineEdit>`{.interpreted-text role="ref"}
instance from this **SpinBox**. You can use it to access properties and
methods of `LineEdit<class_LineEdit>`{.interpreted-text role="ref"}.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_SpinBox_theme_color_down_disabled_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**down_disabled_icon_modulate** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_SpinBox_theme_color_down_disabled_icon_modulate>`{.interpreted-text
role="ref"}

Down button icon modulation color, when the button is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_color_down_hover_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**down_hover_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_SpinBox_theme_color_down_hover_icon_modulate>`{.interpreted-text
role="ref"}

Down button icon modulation color, when the button is hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_color_down_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**down_icon_modulate** = `Color(0.875, 0.875, 0.875, 1)`
`🔗<class_SpinBox_theme_color_down_icon_modulate>`{.interpreted-text
role="ref"}

Down button icon modulation color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_color_down_pressed_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**down_pressed_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_SpinBox_theme_color_down_pressed_icon_modulate>`{.interpreted-text
role="ref"}

Down button icon modulation color, when the button is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_color_up_disabled_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**up_disabled_icon_modulate** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_SpinBox_theme_color_up_disabled_icon_modulate>`{.interpreted-text
role="ref"}

Up button icon modulation color, when the button is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_color_up_hover_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**up_hover_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_SpinBox_theme_color_up_hover_icon_modulate>`{.interpreted-text
role="ref"}

Up button icon modulation color, when the button is hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_color_up_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **up_icon_modulate**
= `Color(0.875, 0.875, 0.875, 1)`
`🔗<class_SpinBox_theme_color_up_icon_modulate>`{.interpreted-text
role="ref"}

Up button icon modulation color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_color_up_pressed_icon_modulate}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**up_pressed_icon_modulate** = `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_SpinBox_theme_color_up_pressed_icon_modulate>`{.interpreted-text
role="ref"}

Up button icon modulation color, when the button is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_constant_buttons_vertical_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**buttons_vertical_separation** = `0`
`🔗<class_SpinBox_theme_constant_buttons_vertical_separation>`{.interpreted-text
role="ref"}

Vertical separation between the up and down buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_constant_buttons_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **buttons_width** = `16`
`🔗<class_SpinBox_theme_constant_buttons_width>`{.interpreted-text
role="ref"}

Width of the up and down buttons. If smaller than any icon set on the
buttons, the respective icon may overlap neighboring elements. If
smaller than `0`, the width is automatically adjusted from the icon
size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_constant_field_and_buttons_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**field_and_buttons_separation** = `2`
`🔗<class_SpinBox_theme_constant_field_and_buttons_separation>`{.interpreted-text
role="ref"}

Width of the horizontal separation between the text input field
(`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}) and the
buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_constant_set_min_buttons_width_from_icons}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**set_min_buttons_width_from_icons** = `1`
`🔗<class_SpinBox_theme_constant_set_min_buttons_width_from_icons>`{.interpreted-text
role="ref"}

If not `0`, the minimum button width corresponds to the widest of all
icons set on those buttons, even if
`buttons_width<class_SpinBox_theme_constant_buttons_width>`{.interpreted-text
role="ref"} is smaller.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_down}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **down**
`🔗<class_SpinBox_theme_icon_down>`{.interpreted-text role="ref"}

Down button icon, displayed in the middle of the down (value-decreasing)
button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_down_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**down_disabled**
`🔗<class_SpinBox_theme_icon_down_disabled>`{.interpreted-text
role="ref"}

Down button icon when the button is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_down_hover}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**down_hover**
`🔗<class_SpinBox_theme_icon_down_hover>`{.interpreted-text role="ref"}

Down button icon when the button is hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_down_pressed}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**down_pressed**
`🔗<class_SpinBox_theme_icon_down_pressed>`{.interpreted-text
role="ref"}

Down button icon when the button is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_up}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **up**
`🔗<class_SpinBox_theme_icon_up>`{.interpreted-text role="ref"}

Up button icon, displayed in the middle of the up (value-increasing)
button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_up_disabled}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**up_disabled**
`🔗<class_SpinBox_theme_icon_up_disabled>`{.interpreted-text role="ref"}

Up button icon when the button is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_up_hover}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **up_hover**
`🔗<class_SpinBox_theme_icon_up_hover>`{.interpreted-text role="ref"}

Up button icon when the button is hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_up_pressed}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**up_pressed**
`🔗<class_SpinBox_theme_icon_up_pressed>`{.interpreted-text role="ref"}

Up button icon when the button is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_icon_updown}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **updown**
`🔗<class_SpinBox_theme_icon_updown>`{.interpreted-text role="ref"}

Single texture representing both the up and down buttons icons. It is
displayed in the middle of the buttons and does not change upon
interaction. It is recommended to use individual
`up<class_SpinBox_theme_icon_up>`{.interpreted-text role="ref"} and
`down<class_SpinBox_theme_icon_down>`{.interpreted-text role="ref"}
graphics for better usability. This can also be used as additional
decoration between the two buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_down_background}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**down_background**
`🔗<class_SpinBox_theme_style_down_background>`{.interpreted-text
role="ref"}

Background style of the down button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_down_background_disabled}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**down_background_disabled**
`🔗<class_SpinBox_theme_style_down_background_disabled>`{.interpreted-text
role="ref"}

Background style of the down button when disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_down_background_hovered}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**down_background_hovered**
`🔗<class_SpinBox_theme_style_down_background_hovered>`{.interpreted-text
role="ref"}

Background style of the down button when hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_down_background_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**down_background_pressed**
`🔗<class_SpinBox_theme_style_down_background_pressed>`{.interpreted-text
role="ref"}

Background style of the down button when being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_field_and_buttons_separator}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**field_and_buttons_separator**
`🔗<class_SpinBox_theme_style_field_and_buttons_separator>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} drawn in the
space occupied by the separation between the input field and the
buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_up_background}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**up_background**
`🔗<class_SpinBox_theme_style_up_background>`{.interpreted-text
role="ref"}

Background style of the up button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_up_background_disabled}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**up_background_disabled**
`🔗<class_SpinBox_theme_style_up_background_disabled>`{.interpreted-text
role="ref"}

Background style of the up button when disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_up_background_hovered}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**up_background_hovered**
`🔗<class_SpinBox_theme_style_up_background_hovered>`{.interpreted-text
role="ref"}

Background style of the up button when hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_up_background_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**up_background_pressed**
`🔗<class_SpinBox_theme_style_up_background_pressed>`{.interpreted-text
role="ref"}

Background style of the up button when being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpinBox_theme_style_up_down_buttons_separator}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**up_down_buttons_separator**
`🔗<class_SpinBox_theme_style_up_down_buttons_separator>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} drawn in the
space occupied by the separation between the up and down buttons.
