github_url
:   hide

# MenuBar {#class_MenuBar}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A horizontal menu bar that creates a menu for each
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"} child.

::: rst-class
classref-introduction-group
:::

## Description

A horizontal menu bar that creates a menu for each
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"} child. New
items are created by adding
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}s to this
node. Item title is determined by
`Window.title<class_Window_property_title>`{.interpreted-text
role="ref"}, or node name if
`Window.title<class_Window_property_title>`{.interpreted-text
role="ref"} is empty. Item title can be overridden using
`set_menu_title()<class_MenuBar_method_set_menu_title>`{.interpreted-text
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

:::: {#class_MenuBar_property_flat}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flat** = `false`
`🔗<class_MenuBar_property_flat>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flat**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flat**()

Flat **MenuBar** don\'t display item decoration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_MenuBar_property_language>`{.interpreted-text role="ref"}

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

:::: {#class_MenuBar_property_prefer_global_menu}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **prefer_global_menu**
= `true`
`🔗<class_MenuBar_property_prefer_global_menu>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_prefer_global_menu**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_prefer_global_menu**()

If `true`, **MenuBar** will use system global menu when supported.

\*\*Note:\*\* If `true` and global menu is supported, this node is not
displayed, has zero size, and all its child nodes except
`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}s are
inaccessible.

\*\*Note:\*\* This property overrides the value of the
`PopupMenu.prefer_native_menu<class_PopupMenu_property_prefer_native_menu>`{.interpreted-text
role="ref"} property of the child nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_property_start_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **start_index** = `-1`
`🔗<class_MenuBar_property_start_index>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_start_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_start_index**()

Position order in the global menu to insert **MenuBar** items at. All
menu items in the **MenuBar** are always inserted as a continuous range.
Menus with lower
`start_index<class_MenuBar_property_start_index>`{.interpreted-text
role="ref"} are inserted first. Menus with
`start_index<class_MenuBar_property_start_index>`{.interpreted-text
role="ref"} equal to `-1` are inserted last.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_property_switch_on_hover}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **switch_on_hover** =
`true` `🔗<class_MenuBar_property_switch_on_hover>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_switch_on_hover**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_switch_on_hover**()

If `true`, when the cursor hovers above menu item, it will close the
current `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"} and
open the other one.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_property_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **text_direction** = `0`
`🔗<class_MenuBar_property_text_direction>`{.interpreted-text
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
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_MenuBar_method_get_menu_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_menu_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_MenuBar_method_get_menu_count>`{.interpreted-text
role="ref"}

Returns number of menu items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_get_menu_popup}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_menu_popup**(menu: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_MenuBar_method_get_menu_popup>`{.interpreted-text
role="ref"}

Returns `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
associated with menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_get_menu_title}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_menu_title**(menu: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_MenuBar_method_get_menu_title>`{.interpreted-text
role="ref"}

Returns menu item title.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_get_menu_tooltip}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_menu_tooltip**(menu: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MenuBar_method_get_menu_tooltip>`{.interpreted-text
role="ref"}

Returns menu item tooltip.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_is_menu_disabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_menu_disabled**(menu: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_MenuBar_method_is_menu_disabled>`{.interpreted-text
role="ref"}

Returns `true`, if menu item is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_is_menu_hidden}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_menu_hidden**(menu: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_MenuBar_method_is_menu_hidden>`{.interpreted-text
role="ref"}

Returns `true`, if menu item is hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_is_native_menu}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_native_menu**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_MenuBar_method_is_native_menu>`{.interpreted-text
role="ref"}

Returns `true`, if system global menu is supported and used by this
**MenuBar**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_set_disable_shortcuts}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_disable_shortcuts**(disabled: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_MenuBar_method_set_disable_shortcuts>`{.interpreted-text
role="ref"}

If `true`, shortcuts are disabled and cannot be used to trigger the
button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_set_menu_disabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_menu_disabled**(menu: `int<class_int>`{.interpreted-text
role="ref"}, disabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_MenuBar_method_set_menu_disabled>`{.interpreted-text
role="ref"}

If `true`, menu item is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_set_menu_hidden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_menu_hidden**(menu: `int<class_int>`{.interpreted-text
role="ref"}, hidden: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_MenuBar_method_set_menu_hidden>`{.interpreted-text role="ref"}

If `true`, menu item is hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_set_menu_title}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_menu_title**(menu: `int<class_int>`{.interpreted-text role="ref"},
title: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_MenuBar_method_set_menu_title>`{.interpreted-text role="ref"}

Sets menu item title.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_method_set_menu_tooltip}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_menu_tooltip**(menu: `int<class_int>`{.interpreted-text
role="ref"}, tooltip: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_MenuBar_method_set_menu_tooltip>`{.interpreted-text
role="ref"}

Sets menu item tooltip.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_MenuBar_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_MenuBar_theme_color_font_color>`{.interpreted-text role="ref"}

Default text `Color<class_Color>`{.interpreted-text role="ref"} of the
menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_color_font_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_disabled_color** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_MenuBar_theme_color_font_disabled_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
menu item is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_color_font_focus_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_focus_color**
= `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_MenuBar_theme_color_font_focus_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
menu item is focused. Only replaces the normal text color of the menu
item. Disabled, hovered, and pressed states take precedence over this
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_color_font_hover_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_hover_color**
= `Color(0.95, 0.95, 0.95, 1)`
`🔗<class_MenuBar_theme_color_font_hover_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
menu item is being hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_color_font_hover_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_hover_pressed_color** = `Color(1, 1, 1, 1)`
`🔗<class_MenuBar_theme_color_font_hover_pressed_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
menu item is being hovered and pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_MenuBar_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_color_font_pressed_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_pressed_color** = `Color(1, 1, 1, 1)`
`🔗<class_MenuBar_theme_color_font_pressed_color>`{.interpreted-text
role="ref"}

Text `Color<class_Color>`{.interpreted-text role="ref"} used when the
menu item is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_constant_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **h_separation** = `4`
`🔗<class_MenuBar_theme_constant_h_separation>`{.interpreted-text
role="ref"}

The horizontal space between menu items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_MenuBar_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_MenuBar_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_MenuBar_theme_font_font>`{.interpreted-text role="ref"}

`Font<class_Font>`{.interpreted-text role="ref"} of the menu item\'s
text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_MenuBar_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the menu item\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_disabled}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **disabled**
`🔗<class_MenuBar_theme_style_disabled>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_disabled_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**disabled_mirrored**
`🔗<class_MenuBar_theme_style_disabled_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is disabled (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_hover}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **hover**
`🔗<class_MenuBar_theme_style_hover>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is being hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_hover_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hover_mirrored**
`🔗<class_MenuBar_theme_style_hover_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is being hovered (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_hover_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hover_pressed**
`🔗<class_MenuBar_theme_style_hover_pressed>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is being pressed and hovered at the same time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_hover_pressed_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**hover_pressed_mirrored**
`🔗<class_MenuBar_theme_style_hover_pressed_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is being pressed and hovered at the same time (for
right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_normal}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **normal**
`🔗<class_MenuBar_theme_style_normal>`{.interpreted-text role="ref"}

Default `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
menu item.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_normal_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**normal_mirrored**
`🔗<class_MenuBar_theme_style_normal_mirrored>`{.interpreted-text
role="ref"}

Default `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the
menu item (for right-to-left layouts).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_pressed}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **pressed**
`🔗<class_MenuBar_theme_style_pressed>`{.interpreted-text role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MenuBar_theme_style_pressed_mirrored}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**pressed_mirrored**
`🔗<class_MenuBar_theme_style_pressed_mirrored>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} used when the
menu item is being pressed (for right-to-left layouts).
