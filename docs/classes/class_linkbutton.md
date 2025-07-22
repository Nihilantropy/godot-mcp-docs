github_url
:   hide

# LinkButton {#class_LinkButton}

**Inherits:** `BaseButton<class_BaseButton>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A button that represents a link.

::: rst-class
classref-introduction-group
:::

## Description

A button that represents a link. This type of button is primarily used
for interactions that cause a context change (like linking to a web
page).

See also `BaseButton<class_BaseButton>`{.interpreted-text role="ref"}
which contains common properties and methods associated with this node.

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

## Enumerations

:::: {#enum_LinkButton_UnderlineMode}
::: rst-class
classref-enumeration
:::
::::

enum **UnderlineMode**:
`🔗<enum_LinkButton_UnderlineMode>`{.interpreted-text role="ref"}

:::: {#class_LinkButton_constant_UNDERLINE_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`UnderlineMode<enum_LinkButton_UnderlineMode>`{.interpreted-text
role="ref"} **UNDERLINE_MODE_ALWAYS** = `0`

The LinkButton will always show an underline at the bottom of its text.

:::: {#class_LinkButton_constant_UNDERLINE_MODE_ON_HOVER}
::: rst-class
classref-enumeration-constant
:::
::::

`UnderlineMode<enum_LinkButton_UnderlineMode>`{.interpreted-text
role="ref"} **UNDERLINE_MODE_ON_HOVER** = `1`

The LinkButton will show an underline at the bottom of its text when the
mouse cursor is over it.

:::: {#class_LinkButton_constant_UNDERLINE_MODE_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`UnderlineMode<enum_LinkButton_UnderlineMode>`{.interpreted-text
role="ref"} **UNDERLINE_MODE_NEVER** = `2`

The LinkButton will never show an underline at the bottom of its text.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_LinkButton_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_LinkButton_property_language>`{.interpreted-text role="ref"}

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

:::: {#class_LinkButton_property_structured_text_bidi_override}
::: rst-class
classref-property
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **structured_text_bidi_override** = `0`
`🔗<class_LinkButton_property_structured_text_bidi_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_structured_text_bidi_override**(value:
  `StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
  role="ref"})
- `StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
  role="ref"} **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_property_structured_text_bidi_override_options}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**structured_text_bidi_override_options** = `[]`
`🔗<class_LinkButton_property_structured_text_bidi_override_options>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_structured_text_bidi_override_options**(value:
  `Array<class_Array>`{.interpreted-text role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_LinkButton_property_text>`{.interpreted-text role="ref"}

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

:::: {#class_LinkButton_property_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **text_direction** = `0`
`🔗<class_LinkButton_property_text_direction>`{.interpreted-text
role="ref"}

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

:::: {#class_LinkButton_property_underline}
::: rst-class
classref-property
:::
::::

`UnderlineMode<enum_LinkButton_UnderlineMode>`{.interpreted-text
role="ref"} **underline** = `0`
`🔗<class_LinkButton_property_underline>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_underline_mode**(value:
  `UnderlineMode<enum_LinkButton_UnderlineMode>`{.interpreted-text
  role="ref"})
- `UnderlineMode<enum_LinkButton_UnderlineMode>`{.interpreted-text
  role="ref"} **get_underline_mode**()

The underline mode to use for the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_property_uri}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **uri** = `""`
`🔗<class_LinkButton_property_uri>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_uri**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_uri**()

The [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) for
this **LinkButton**. If set to a valid URI, pressing the button opens
the URI using the operating system\'s default program for the protocol
(via `OS.shell_open()<class_OS_method_shell_open>`{.interpreted-text
role="ref"}). HTTP and HTTPS URLs open the default web browser.

::::: tabs
::: code-tab
gdscript

uri = \"https://godotengine.org\" \# Opens the URL in the default web
browser. uri = \"C:SomeFolder\" \# Opens the file explorer at the given
path. uri = \"C:SomeImage.png\" \# Opens the given image in the default
viewing app.
:::

::: code-tab
csharp

Uri = \"https://godotengine.org\"; // Opens the URL in the default web
browser. Uri = \"C:SomeFolder\"; // Opens the file explorer at the given
path. Uri = \"C:SomeImage.png\"; // Opens the given image in the default
viewing app.
:::
:::::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_LinkButton_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_LinkButton_theme_color_font_color>`{.interpreted-text
role="ref"}

Default text `Color<class_Color>`{.interpreted-text role="ref"} of the
**LinkButton**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_color_font_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_disabled_color** = `Color(0, 0, 0, 1)`
`🔗<class_LinkButton_theme_color_font_disabled_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**LinkButton** is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_color_font_focus_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_focus_color**
= `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_LinkButton_theme_color_font_focus_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**LinkButton** is focused. Only replaces the normal text color of the
button. Disabled, hovered, and pressed states take precedence over this
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_color_font_hover_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_hover_color**
= `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_LinkButton_theme_color_font_hover_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**LinkButton** is being hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_color_font_hover_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hover_pressed_color** = `Color(0, 0, 0, 1)`
`🔗<class_LinkButton_theme_color_font_hover_pressed_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**LinkButton** is being hovered and pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_LinkButton_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the **LinkButton**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_color_font_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_pressed_color** = `Color(1, 1, 1, 1)`
`🔗<class_LinkButton_theme_color_font_pressed_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
**LinkButton** is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_LinkButton_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_LinkButton_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_constant_underline_spacing}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **underline_spacing** =
`2`
`🔗<class_LinkButton_theme_constant_underline_spacing>`{.interpreted-text
role="ref"}

The vertical space between the baseline of text and the underline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_LinkButton_theme_font_font>`{.interpreted-text role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} of the
**LinkButton**\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_LinkButton_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the **LinkButton**\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LinkButton_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_LinkButton_theme_style_focus>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
**LinkButton** is focused. The
`focus<class_LinkButton_theme_style_focus>`{.interpreted-text
role="ref"} `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} is
displayed *over* the base `StyleBox<class_StyleBox>`{.interpreted-text
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
