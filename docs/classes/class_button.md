github_url
:   hide

# Button {#class_Button}

**Inherits:** `BaseButton<class_BaseButton>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `CheckBox<class_CheckBox>`{.interpreted-text
role="ref"}, `CheckButton<class_CheckButton>`{.interpreted-text
role="ref"},
`ColorPickerButton<class_ColorPickerButton>`{.interpreted-text
role="ref"}, `MenuButton<class_MenuButton>`{.interpreted-text
role="ref"}, `OptionButton<class_OptionButton>`{.interpreted-text
role="ref"}

A themed button that can contain text and an icon.

::: rst-class
classref-introduction-group
:::

## Description

**Button** is the standard themed button. It can contain text and an
icon, and it will display them according to the current
`Theme<class_Theme>`{.interpreted-text role="ref"}.

\*\*Example:\*\* Create a button and connect a method that will be
called when the button is pressed:

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var button = Button.new() button.text = \"Click me\"
    button.pressed.connect([button_pressed]{#button_pressed})
    add_child(button)

func [button_pressed]{#button_pressed}():

:   print(\"Hello world!\")
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { var button = new Button();
button.Text = \"Click me\"; button.Pressed += ButtonPressed;
AddChild(button); }

private void ButtonPressed() { GD.Print(\"Hello world!\"); }
:::
:::::

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

\*\*Note:\*\* Buttons do not detect touch input and therefore don\'t
support multitouch, since mouse emulation can only press one button at a
given time. Use
`TouchScreenButton<class_TouchScreenButton>`{.interpreted-text
role="ref"} for buttons that trigger gameplay movement or actions.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)
- [Operating System Testing
  Demo](https://godotengine.org/asset-library/asset/2789)

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

## Property Descriptions

:::: {#class_Button_property_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **alignment** = `1`
`🔗<class_Button_property_alignment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_text_alignment**()

Text alignment policy for the button\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_autowrap_mode}
::: rst-class
classref-property
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **autowrap_mode** = `0`
`🔗<class_Button_property_autowrap_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autowrap_mode**(value:
  `AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
  role="ref"})
- `AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
  role="ref"} **get_autowrap_mode**()

If set to something other than
`TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>`{.interpreted-text
role="ref"}, the text gets wrapped inside the node\'s bounding
rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_autowrap_trim_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] **autowrap_trim_flags** = `128`
`🔗<class_Button_property_autowrap_trim_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autowrap_trim_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
  role="ref"}\] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See
`TextServer.BREAK_TRIM_START_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES>`{.interpreted-text
role="ref"} and
`TextServer.BREAK_TRIM_END_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES>`{.interpreted-text
role="ref"} for more info.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_clip_text}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **clip_text** = `false`
`🔗<class_Button_property_clip_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clip_text**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_clip_text**()

If `true`, text that is too large to fit the button is clipped
horizontally. If `false`, the button will always be wide enough to hold
the text. The text is not vertically clipped, and the button\'s height
is not affected by this property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_expand_icon}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **expand_icon** =
`false` `🔗<class_Button_property_expand_icon>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand_icon**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_expand_icon**()

When enabled, the button\'s icon will expand/shrink to fit the button\'s
size while keeping its aspect. See also
`icon_max_width<class_Button_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_flat}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flat** = `false`
`🔗<class_Button_property_flat>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flat**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flat**()

Flat buttons don\'t display decoration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_icon}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **icon**
`🔗<class_Button_property_icon>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_button_icon**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_button_icon**()

Button\'s icon, if text is present the icon will be placed before the
text.

To edit margin and spacing of the icon, use
`h_separation<class_Button_theme_constant_h_separation>`{.interpreted-text
role="ref"} theme property and `content_margin_*` properties of the used
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}es.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_icon_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **icon_alignment** = `0`
`🔗<class_Button_property_icon_alignment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_icon_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_icon_alignment**()

Specifies if the icon should be aligned horizontally to the left, right,
or center of a button. Uses the same
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} constants as the text alignment. If centered horizontally
and vertically, text will draw on top of the icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_Button_property_language>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_language**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_language**()

Language code used for line-breaking and text shaping algorithms, if
left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_Button_property_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_text**()

The button\'s text that will be displayed inside the button\'s area.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **text_direction** = `0`
`🔗<class_Button_property_text_direction>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_direction**(value:
  `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"})
- `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"} **get_text_direction**()

Base text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_text_overrun_behavior}
::: rst-class
classref-property
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **text_overrun_behavior** = `0`
`🔗<class_Button_property_text_overrun_behavior>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_overrun_behavior**(value:
  `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"})
- `OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
  role="ref"} **get_text_overrun_behavior**()

Sets the clipping behavior when the text exceeds the node\'s bounding
rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_property_vertical_icon_alignment}
::: rst-class
classref-property
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **vertical_icon_alignment** = `1`
`🔗<class_Button_property_vertical_icon_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical_icon_alignment**(value:
  `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
  role="ref"})
- `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
  role="ref"} **get_vertical_icon_alignment**()

Specifies if the icon should be aligned vertically to the top, bottom,
or center of a button. Uses the same
`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} constants as the text alignment. If centered horizontally
and vertically, text will draw on top of the icon.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_Button_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_Button_theme_color_font_color>`{.interpreted-text role="ref"}

Default text `Color<class_Color>`{.interpreted-text role="ref"} of the
**Button**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_font_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_Button_theme_color_font_disabled_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**Button** is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_font_focus_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_focus_color**
= `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_Button_theme_color_font_focus_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**Button** is focused. Only replaces the normal text color of the
button. Disabled, hovered, and pressed states take precedence over this
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_font_hover_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_hover_color**
= `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_Button_theme_color_font_hover_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**Button** is being hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_font_hover_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hover_pressed_color** = `Color(1, 1, 1, 1)`
`🔗<class_Button_theme_color_font_hover_pressed_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**Button** is being hovered and pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_Button_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the **Button**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_font_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_pressed_color** = `Color(1, 1, 1, 1)`
`🔗<class_Button_theme_color_font_pressed_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**Button** is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_icon_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**icon_disabled_color** = `Color(1, 1, 1, 0.4)`
`🔗<class_Button_theme_color_icon_disabled_color>`{.interpreted-text
role="ref"}

Icon modulate `Color<class_Color>`{.interpreted-text role="ref"} used
when the **Button** is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_icon_focus_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **icon_focus_color**
= `Color(1, 1, 1, 1)`
`🔗<class_Button_theme_color_icon_focus_color>`{.interpreted-text
role="ref"}

Icon modulate `Color<class_Color>`{.interpreted-text role="ref"} used
when the **Button** is focused. Only replaces the normal modulate color
of the button. Disabled, hovered, and pressed states take precedence
over this color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_icon_hover_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **icon_hover_color**
= `Color(1, 1, 1, 1)`
`🔗<class_Button_theme_color_icon_hover_color>`{.interpreted-text
role="ref"}

Icon modulate `Color<class_Color>`{.interpreted-text role="ref"} used
when the **Button** is being hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_icon_hover_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**icon_hover_pressed_color** = `Color(1, 1, 1, 1)`
`🔗<class_Button_theme_color_icon_hover_pressed_color>`{.interpreted-text
role="ref"}

Icon modulate `Color<class_Color>`{.interpreted-text role="ref"} used
when the **Button** is being hovered and pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_icon_normal_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **icon_normal_color**
= `Color(1, 1, 1, 1)`
`🔗<class_Button_theme_color_icon_normal_color>`{.interpreted-text
role="ref"}

Default icon modulate `Color<class_Color>`{.interpreted-text role="ref"}
of the **Button**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_color_icon_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**icon_pressed_color** = `Color(1, 1, 1, 1)`
`🔗<class_Button_theme_color_icon_pressed_color>`{.interpreted-text
role="ref"}

Icon modulate `Color<class_Color>`{.interpreted-text role="ref"} used
when the **Button** is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_constant_align_to_largest_stylebox}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**align_to_largest_stylebox** = `0`
`🔗<class_Button_theme_constant_align_to_largest_stylebox>`{.interpreted-text
role="ref"}

This constant acts as a boolean. If `true`, the minimum size of the
button and text/icon alignment is always based on the largest stylebox
margins, otherwise it\'s based on the current button state stylebox
margins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_Button_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal space between **Button**\'s icon and text. Negative
values will be treated as `0` when used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_constant_icon_max_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **icon_max_width** = `0`
`🔗<class_Button_theme_constant_icon_max_width>`{.interpreted-text
role="ref"}

The maximum allowed width of the **Button**\'s icon. This limit is
applied on top of the default size of the icon, or its expanded size if
`expand_icon<class_Button_property_expand_icon>`{.interpreted-text
role="ref"} is `true`. The height is adjusted according to the icon\'s
ratio. If the button has additional icons (e.g.
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"}), they will
also be limited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_constant_line_spacing}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **line_spacing** = `0`
`🔗<class_Button_theme_constant_line_spacing>`{.interpreted-text
role="ref"}

Additional vertical spacing between lines (in pixels), spacing is added
to line descent. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_Button_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_Button_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_Button_theme_font_font>`{.interpreted-text role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} of the **Button**\'s
text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_Button_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the **Button**\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_icon_icon}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **icon**
`🔗<class_Button_theme_icon_icon>`{.interpreted-text role="ref"}

Default icon for the **Button**. Appears only if
`icon<class_Button_property_icon>`{.interpreted-text role="ref"} is not
assigned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_disabled}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **disabled**
`🔗<class_Button_theme_style_disabled>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_disabled_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**disabled_mirrored**
`🔗<class_Button_theme_style_disabled_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is disabled (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_Button_theme_style_focus>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is focused. The
`focus<class_Button_theme_style_focus>`{.interpreted-text role="ref"}
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} is displayed
*over* the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}, so a partially transparent
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} should be used
to ensure the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} remains visible. A
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

:::: {#class_Button_theme_style_hover}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **hover**
`🔗<class_Button_theme_style_hover>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is being hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_hover_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hover_mirrored**
`🔗<class_Button_theme_style_hover_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is being hovered (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_hover_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hover_pressed**
`🔗<class_Button_theme_style_hover_pressed>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is being pressed and hovered at the same time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_hover_pressed_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hover_pressed_mirrored**
`🔗<class_Button_theme_style_hover_pressed_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is being pressed and hovered at the same time (for
right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_normal}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **normal**
`🔗<class_Button_theme_style_normal>`{.interpreted-text role="ref"}

Default `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
**Button**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_normal_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**normal_mirrored**
`🔗<class_Button_theme_style_normal_mirrored>`{.interpreted-text
role="ref"}

Default `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
**Button** (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **pressed**
`🔗<class_Button_theme_style_pressed>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Button_theme_style_pressed_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**pressed_mirrored**
`🔗<class_Button_theme_style_pressed_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**Button** is being pressed (for right-to-left layouts).
