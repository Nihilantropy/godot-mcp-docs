github_url
:   hide

# Theme {#class_Theme}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

A resource used for styling/skinning
`Control<class_Control>`{.interpreted-text role="ref"}s and
`Window<class_Window>`{.interpreted-text role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

A resource used for styling/skinning
`Control<class_Control>`{.interpreted-text role="ref"} and
`Window<class_Window>`{.interpreted-text role="ref"} nodes. While
individual controls can be styled using their local theme overrides (see
`Control.add_theme_color_override()<class_Control_method_add_theme_color_override>`{.interpreted-text
role="ref"}), theme resources allow you to store and apply the same
settings across all controls sharing the same type (e.g. style all
`Button<class_Button>`{.interpreted-text role="ref"}s the same). One
theme resource can be used for the entire project, but you can also set
a separate theme resource to a branch of control nodes. A theme resource
assigned to a control applies to the control itself, as well as all of
its direct and indirect children (as long as a chain of controls is
uninterrupted).

Use
`ProjectSettings.gui/theme/custom<class_ProjectSettings_property_gui/theme/custom>`{.interpreted-text
role="ref"} to set up a project-scope theme that will be available to
every control in your project.

Use `Control.theme<class_Control_property_theme>`{.interpreted-text
role="ref"} of any control node to set up a theme that will be available
to that control and all of its direct and indirect children.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `GUI skinning <../tutorials/ui/gui_skinning>`{.interpreted-text
  role="doc"}
- `Using the theme editor <../tutorials/ui/gui_using_theme_editor>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Theme_DataType}
::: rst-class
classref-enumeration
:::
::::

enum **DataType**: `🔗<enum_Theme_DataType>`{.interpreted-text
role="ref"}

:::: {#class_Theme_constant_DATA_TYPE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}
**DATA_TYPE_COLOR** = `0`

Theme\'s `Color<class_Color>`{.interpreted-text role="ref"} item type.

:::: {#class_Theme_constant_DATA_TYPE_CONSTANT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}
**DATA_TYPE_CONSTANT** = `1`

Theme\'s constant item type.

:::: {#class_Theme_constant_DATA_TYPE_FONT}
::: rst-class
classref-enumeration-constant
:::
::::

`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}
**DATA_TYPE_FONT** = `2`

Theme\'s `Font<class_Font>`{.interpreted-text role="ref"} item type.

:::: {#class_Theme_constant_DATA_TYPE_FONT_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}
**DATA_TYPE_FONT_SIZE** = `3`

Theme\'s font size item type.

:::: {#class_Theme_constant_DATA_TYPE_ICON}
::: rst-class
classref-enumeration-constant
:::
::::

`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}
**DATA_TYPE_ICON** = `4`

Theme\'s icon `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
item type.

:::: {#class_Theme_constant_DATA_TYPE_STYLEBOX}
::: rst-class
classref-enumeration-constant
:::
::::

`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}
**DATA_TYPE_STYLEBOX** = `5`

Theme\'s `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} item
type.

:::: {#class_Theme_constant_DATA_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}
**DATA_TYPE_MAX** = `6`

Maximum value for the DataType enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Theme_property_default_base_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**default_base_scale** = `0.0`
`🔗<class_Theme_property_default_base_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_base_scale**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_default_base_scale**()

The default base scale factor of this theme resource. Used by some
controls to scale their visual properties based on the global scale
factor. If this value is set to `0.0`, the global scale factor is used
(see
`ThemeDB.fallback_base_scale<class_ThemeDB_property_fallback_base_scale>`{.interpreted-text
role="ref"}).

Use
`has_default_base_scale()<class_Theme_method_has_default_base_scale>`{.interpreted-text
role="ref"} to check if this value is valid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_property_default_font}
::: rst-class
classref-property
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **default_font**
`🔗<class_Theme_property_default_font>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_font**(value: `Font<class_Font>`{.interpreted-text
  role="ref"})
- `Font<class_Font>`{.interpreted-text role="ref"}
  **get_default_font**()

The default font of this theme resource. Used as the default value when
trying to fetch a font resource that doesn\'t exist in this theme or is
in invalid state. If the default font is also missing or invalid, the
engine fallback value is used (see
`ThemeDB.fallback_font<class_ThemeDB_property_fallback_font>`{.interpreted-text
role="ref"}).

Use
`has_default_font()<class_Theme_method_has_default_font>`{.interpreted-text
role="ref"} to check if this value is valid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_property_default_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **default_font_size** =
`-1` `🔗<class_Theme_property_default_font_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_font_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_default_font_size**()

The default font size of this theme resource. Used as the default value
when trying to fetch a font size value that doesn\'t exist in this theme
or is in invalid state. If the default font size is also missing or
invalid, the engine fallback value is used (see
`ThemeDB.fallback_font_size<class_ThemeDB_property_fallback_font_size>`{.interpreted-text
role="ref"}).

Values below `1` are invalid and can be used to unset the property. Use
`has_default_font_size()<class_Theme_method_has_default_font_size>`{.interpreted-text
role="ref"} to check if this value is valid.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Theme_method_add_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_type**(theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_add_type>`{.interpreted-text role="ref"}

Adds an empty theme type for every valid data type.

\*\*Note:\*\* Empty types are not saved with the theme. This method only
exists to perform in-memory changes to the resource. Use available
`set_*` methods to add theme items.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_Theme_method_clear>`{.interpreted-text role="ref"}

Removes all the theme properties defined on the theme resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_color**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_clear_color>`{.interpreted-text role="ref"}

Removes the `Color<class_Color>`{.interpreted-text role="ref"} property
defined by `name` and `theme_type`, if it exists.

Fails if it doesn\'t exist. Use
`has_color()<class_Theme_method_has_color>`{.interpreted-text
role="ref"} to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_constant}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_constant**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_clear_constant>`{.interpreted-text
role="ref"}

Removes the constant property defined by `name` and `theme_type`, if it
exists.

Fails if it doesn\'t exist. Use
`has_constant()<class_Theme_method_has_constant>`{.interpreted-text
role="ref"} to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_font}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_font**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_clear_font>`{.interpreted-text role="ref"}

Removes the `Font<class_Font>`{.interpreted-text role="ref"} property
defined by `name` and `theme_type`, if it exists.

Fails if it doesn\'t exist. Use
`has_font()<class_Theme_method_has_font>`{.interpreted-text role="ref"}
to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_font_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_font_size**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_clear_font_size>`{.interpreted-text
role="ref"}

Removes the font size property defined by `name` and `theme_type`, if it
exists.

Fails if it doesn\'t exist. Use
`has_font_size()<class_Theme_method_has_font_size>`{.interpreted-text
role="ref"} to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_icon**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_clear_icon>`{.interpreted-text role="ref"}

Removes the icon property defined by `name` and `theme_type`, if it
exists.

Fails if it doesn\'t exist. Use
`has_icon()<class_Theme_method_has_icon>`{.interpreted-text role="ref"}
to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_stylebox}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_stylebox**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_clear_stylebox>`{.interpreted-text
role="ref"}

Removes the `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
property defined by `name` and `theme_type`, if it exists.

Fails if it doesn\'t exist. Use
`has_stylebox()<class_Theme_method_has_stylebox>`{.interpreted-text
role="ref"} to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_theme_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_theme_item**(data_type:
`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_clear_theme_item>`{.interpreted-text
role="ref"}

Removes the theme property of `data_type` defined by `name` and
`theme_type`, if it exists.

Fails if it doesn\'t exist. Use
`has_theme_item()<class_Theme_method_has_theme_item>`{.interpreted-text
role="ref"} to check for existence.

\*\*Note:\*\* This method is analogous to calling the corresponding data
type specific method, but can be used for more generalized logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_clear_type_variation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_type_variation**(theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_clear_type_variation>`{.interpreted-text
role="ref"}

Unmarks `theme_type` as being a variation of another theme type. See
`set_type_variation()<class_Theme_method_set_type_variation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **get_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_color>`{.interpreted-text
role="ref"}

Returns the `Color<class_Color>`{.interpreted-text role="ref"} property
defined by `name` and `theme_type`, if it exists.

Returns the default color value if the property doesn\'t exist. Use
`has_color()<class_Theme_method_has_color>`{.interpreted-text
role="ref"} to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_color_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_color_list**(theme_type:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_color_list>`{.interpreted-text
role="ref"}

Returns a list of names for `Color<class_Color>`{.interpreted-text
role="ref"} properties defined with `theme_type`. Use
`get_color_type_list()<class_Theme_method_get_color_type_list>`{.interpreted-text
role="ref"} to get a list of possible theme type names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_color_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_color_type_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_color_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names for
`Color<class_Color>`{.interpreted-text role="ref"} properties. Use
`get_type_list()<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"} to get a list of all unique theme types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_constant}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_constant**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_constant>`{.interpreted-text
role="ref"}

Returns the constant property defined by `name` and `theme_type`, if it
exists.

Returns `0` if the property doesn\'t exist. Use
`has_constant()<class_Theme_method_has_constant>`{.interpreted-text
role="ref"} to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_constant_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_constant_list**(theme_type:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_constant_list>`{.interpreted-text role="ref"}

Returns a list of names for constant properties defined with
`theme_type`. Use
`get_constant_type_list()<class_Theme_method_get_constant_type_list>`{.interpreted-text
role="ref"} to get a list of possible theme type names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_constant_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_constant_type_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_constant_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names for constant properties.
Use
`get_type_list()<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"} to get a list of all unique theme types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_font}
::: rst-class
classref-method
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **get_font**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_font>`{.interpreted-text
role="ref"}

Returns the `Font<class_Font>`{.interpreted-text role="ref"} property
defined by `name` and `theme_type`, if it exists.

Returns the default theme font if the property doesn\'t exist and the
default theme font is set up (see
`default_font<class_Theme_property_default_font>`{.interpreted-text
role="ref"}). Use
`has_font()<class_Theme_method_has_font>`{.interpreted-text role="ref"}
to check for existence of the property and
`has_default_font()<class_Theme_method_has_default_font>`{.interpreted-text
role="ref"} to check for existence of the default theme font.

Returns the engine fallback font value, if neither exist (see
`ThemeDB.fallback_font<class_ThemeDB_property_fallback_font>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_font_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_font_list**(theme_type:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_font_list>`{.interpreted-text
role="ref"}

Returns a list of names for `Font<class_Font>`{.interpreted-text
role="ref"} properties defined with `theme_type`. Use
`get_font_type_list()<class_Theme_method_get_font_type_list>`{.interpreted-text
role="ref"} to get a list of possible theme type names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_font_size**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_font_size>`{.interpreted-text
role="ref"}

Returns the font size property defined by `name` and `theme_type`, if it
exists.

Returns the default theme font size if the property doesn\'t exist and
the default theme font size is set up (see
`default_font_size<class_Theme_property_default_font_size>`{.interpreted-text
role="ref"}). Use
`has_font_size()<class_Theme_method_has_font_size>`{.interpreted-text
role="ref"} to check for existence of the property and
`has_default_font_size()<class_Theme_method_has_default_font_size>`{.interpreted-text
role="ref"} to check for existence of the default theme font.

Returns the engine fallback font size value, if neither exist (see
`ThemeDB.fallback_font_size<class_ThemeDB_property_fallback_font_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_font_size_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_font_size_list**(theme_type:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_font_size_list>`{.interpreted-text
role="ref"}

Returns a list of names for font size properties defined with
`theme_type`. Use
`get_font_size_type_list()<class_Theme_method_get_font_size_type_list>`{.interpreted-text
role="ref"} to get a list of possible theme type names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_font_size_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_font_size_type_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_font_size_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names for font size properties.
Use
`get_type_list()<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"} to get a list of all unique theme types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_font_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_font_type_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_font_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names for
`Font<class_Font>`{.interpreted-text role="ref"} properties. Use
`get_type_list()<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"} to get a list of all unique theme types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_icon**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_icon>`{.interpreted-text
role="ref"}

Returns the icon property defined by `name` and `theme_type`, if it
exists.

Returns the engine fallback icon value if the property doesn\'t exist
(see
`ThemeDB.fallback_icon<class_ThemeDB_property_fallback_icon>`{.interpreted-text
role="ref"}). Use
`has_icon()<class_Theme_method_has_icon>`{.interpreted-text role="ref"}
to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_icon_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_icon_list**(theme_type:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_icon_list>`{.interpreted-text
role="ref"}

Returns a list of names for icon properties defined with `theme_type`.
Use
`get_icon_type_list()<class_Theme_method_get_icon_type_list>`{.interpreted-text
role="ref"} to get a list of possible theme type names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_icon_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_icon_type_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_icon_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names for icon properties. Use
`get_type_list()<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"} to get a list of all unique theme types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_stylebox}
::: rst-class
classref-method
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**get_stylebox**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_stylebox>`{.interpreted-text
role="ref"}

Returns the `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
property defined by `name` and `theme_type`, if it exists.

Returns the engine fallback stylebox value if the property doesn\'t
exist (see
`ThemeDB.fallback_stylebox<class_ThemeDB_property_fallback_stylebox>`{.interpreted-text
role="ref"}). Use
`has_stylebox()<class_Theme_method_has_stylebox>`{.interpreted-text
role="ref"} to check for existence.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_stylebox_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_stylebox_list**(theme_type:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_stylebox_list>`{.interpreted-text role="ref"}

Returns a list of names for `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} properties defined with `theme_type`. Use
`get_stylebox_type_list()<class_Theme_method_get_stylebox_type_list>`{.interpreted-text
role="ref"} to get a list of possible theme type names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_stylebox_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_stylebox_type_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_stylebox_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names for
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} properties. Use
`get_type_list()<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"} to get a list of all unique theme types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_theme_item}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_theme_item**(data_type:
`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_theme_item>`{.interpreted-text
role="ref"}

Returns the theme property of `data_type` defined by `name` and
`theme_type`, if it exists.

Returns the engine fallback value if the property doesn\'t exist (see
`ThemeDB<class_ThemeDB>`{.interpreted-text role="ref"}). Use
`has_theme_item()<class_Theme_method_has_theme_item>`{.interpreted-text
role="ref"} to check for existence.

\*\*Note:\*\* This method is analogous to calling the corresponding data
type specific method, but can be used for more generalized logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_theme_item_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_theme_item_list**(data_type:
`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"},
theme_type: `String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_theme_item_list>`{.interpreted-text
role="ref"}

Returns a list of names for properties of `data_type` defined with
`theme_type`. Use
`get_theme_item_type_list()<class_Theme_method_get_theme_item_type_list>`{.interpreted-text
role="ref"} to get a list of possible theme type names.

\*\*Note:\*\* This method is analogous to calling the corresponding data
type specific method, but can be used for more generalized logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_theme_item_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_theme_item_type_list**(data_type:
`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_theme_item_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names for `data_type`
properties. Use
`get_type_list()<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"} to get a list of all unique theme types.

\*\*Note:\*\* This method is analogous to calling the corresponding data
type specific method, but can be used for more generalized logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_type_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_type_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_get_type_list>`{.interpreted-text
role="ref"}

Returns a list of all unique theme type names. Use the appropriate
`get_*_type_list` method to get a list of unique theme types for a
single data type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_type_variation_base}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**get_type_variation_base**(theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_type_variation_base>`{.interpreted-text
role="ref"}

Returns the name of the base theme type if `theme_type` is a valid
variation type. Returns an empty string otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_get_type_variation_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_type_variation_list**(base_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_get_type_variation_list>`{.interpreted-text
role="ref"}

Returns a list of all type variations for the given `base_type`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_color}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_color**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_color>`{.interpreted-text
role="ref"}

Returns `true` if the `Color<class_Color>`{.interpreted-text role="ref"}
property defined by `name` and `theme_type` exists.

Returns `false` if it doesn\'t exist. Use
`set_color()<class_Theme_method_set_color>`{.interpreted-text
role="ref"} to define it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_constant}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_constant**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_constant>`{.interpreted-text
role="ref"}

Returns `true` if the constant property defined by `name` and
`theme_type` exists.

Returns `false` if it doesn\'t exist. Use
`set_constant()<class_Theme_method_set_constant>`{.interpreted-text
role="ref"} to define it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_default_base_scale}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_default_base_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_has_default_base_scale>`{.interpreted-text
role="ref"}

Returns `true` if
`default_base_scale<class_Theme_property_default_base_scale>`{.interpreted-text
role="ref"} has a valid value.

Returns `false` if it doesn\'t. The value must be greater than `0.0` to
be considered valid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_default_font}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_default_font**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_default_font>`{.interpreted-text
role="ref"}

Returns `true` if
`default_font<class_Theme_property_default_font>`{.interpreted-text
role="ref"} has a valid value.

Returns `false` if it doesn\'t.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_default_font_size}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_default_font_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_has_default_font_size>`{.interpreted-text
role="ref"}

Returns `true` if
`default_font_size<class_Theme_property_default_font_size>`{.interpreted-text
role="ref"} has a valid value.

Returns `false` if it doesn\'t. The value must be greater than `0` to be
considered valid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_font}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_font**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_font>`{.interpreted-text
role="ref"}

Returns `true` if the `Font<class_Font>`{.interpreted-text role="ref"}
property defined by `name` and `theme_type` exists, or if the default
theme font is set up (see
`has_default_font()<class_Theme_method_has_default_font>`{.interpreted-text
role="ref"}).

Returns `false` if neither exist. Use
`set_font()<class_Theme_method_set_font>`{.interpreted-text role="ref"}
to define the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_font_size}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_font_size**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_font_size>`{.interpreted-text
role="ref"}

Returns `true` if the font size property defined by `name` and
`theme_type` exists, or if the default theme font size is set up (see
`has_default_font_size()<class_Theme_method_has_default_font_size>`{.interpreted-text
role="ref"}).

Returns `false` if neither exist. Use
`set_font_size()<class_Theme_method_set_font_size>`{.interpreted-text
role="ref"} to define the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_icon}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_icon**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_icon>`{.interpreted-text
role="ref"}

Returns `true` if the icon property defined by `name` and `theme_type`
exists.

Returns `false` if it doesn\'t exist. Use
`set_icon()<class_Theme_method_set_icon>`{.interpreted-text role="ref"}
to define it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_stylebox}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_stylebox**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_stylebox>`{.interpreted-text
role="ref"}

Returns `true` if the `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} property defined by `name` and `theme_type` exists.

Returns `false` if it doesn\'t exist. Use
`set_stylebox()<class_Theme_method_set_stylebox>`{.interpreted-text
role="ref"} to define it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_has_theme_item}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_theme_item**(data_type:
`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Theme_method_has_theme_item>`{.interpreted-text
role="ref"}

Returns `true` if the theme property of `data_type` defined by `name`
and `theme_type` exists.

Returns `false` if it doesn\'t exist. Use
`set_theme_item()<class_Theme_method_set_theme_item>`{.interpreted-text
role="ref"} to define it.

\*\*Note:\*\* This method is analogous to calling the corresponding data
type specific method, but can be used for more generalized logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_is_type_variation}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_type_variation**(theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, base_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Theme_method_is_type_variation>`{.interpreted-text role="ref"}

Returns `true` if `theme_type` is marked as a variation of `base_type`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_merge_with}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**merge_with**(other: `Theme<class_Theme>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_merge_with>`{.interpreted-text
role="ref"}

Adds missing and overrides existing definitions with values from the
`other` theme resource.

\*\*Note:\*\* This modifies the current theme. If you want to merge two
themes together without modifying either one, create a new empty theme
and merge the other two into it one after another.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_remove_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_type**(theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_remove_type>`{.interpreted-text role="ref"}

Removes the theme type, gracefully discarding defined theme items. If
the type is a variation, this information is also erased. If the type is
a base for type variations, those variations lose their base.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_color**(old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_rename_color>`{.interpreted-text
role="ref"}

Renames the `Color<class_Color>`{.interpreted-text role="ref"} property
defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn\'t exist, or if a similar property with the new name
already exists. Use
`has_color()<class_Theme_method_has_color>`{.interpreted-text
role="ref"} to check for existence, and
`clear_color()<class_Theme_method_clear_color>`{.interpreted-text
role="ref"} to remove the existing property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_constant}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_constant**(old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_rename_constant>`{.interpreted-text
role="ref"}

Renames the constant property defined by `old_name` and `theme_type` to
`name`, if it exists.

Fails if it doesn\'t exist, or if a similar property with the new name
already exists. Use
`has_constant()<class_Theme_method_has_constant>`{.interpreted-text
role="ref"} to check for existence, and
`clear_constant()<class_Theme_method_clear_constant>`{.interpreted-text
role="ref"} to remove the existing property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_font}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_font**(old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_rename_font>`{.interpreted-text
role="ref"}

Renames the `Font<class_Font>`{.interpreted-text role="ref"} property
defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn\'t exist, or if a similar property with the new name
already exists. Use
`has_font()<class_Theme_method_has_font>`{.interpreted-text role="ref"}
to check for existence, and
`clear_font()<class_Theme_method_clear_font>`{.interpreted-text
role="ref"} to remove the existing property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_font_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_font_size**(old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_rename_font_size>`{.interpreted-text
role="ref"}

Renames the font size property defined by `old_name` and `theme_type` to
`name`, if it exists.

Fails if it doesn\'t exist, or if a similar property with the new name
already exists. Use
`has_font_size()<class_Theme_method_has_font_size>`{.interpreted-text
role="ref"} to check for existence, and
`clear_font_size()<class_Theme_method_clear_font_size>`{.interpreted-text
role="ref"} to remove the existing property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_icon**(old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_rename_icon>`{.interpreted-text
role="ref"}

Renames the icon property defined by `old_name` and `theme_type` to
`name`, if it exists.

Fails if it doesn\'t exist, or if a similar property with the new name
already exists. Use
`has_icon()<class_Theme_method_has_icon>`{.interpreted-text role="ref"}
to check for existence, and
`clear_icon()<class_Theme_method_clear_icon>`{.interpreted-text
role="ref"} to remove the existing property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_stylebox}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_stylebox**(old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_rename_stylebox>`{.interpreted-text
role="ref"}

Renames the `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
property defined by `old_name` and `theme_type` to `name`, if it exists.

Fails if it doesn\'t exist, or if a similar property with the new name
already exists. Use
`has_stylebox()<class_Theme_method_has_stylebox>`{.interpreted-text
role="ref"} to check for existence, and
`clear_stylebox()<class_Theme_method_clear_stylebox>`{.interpreted-text
role="ref"} to remove the existing property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_theme_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_theme_item**(data_type:
`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}, old_name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_Theme_method_rename_theme_item>`{.interpreted-text role="ref"}

Renames the theme property of `data_type` defined by `old_name` and
`theme_type` to `name`, if it exists.

Fails if it doesn\'t exist, or if a similar property with the new name
already exists. Use
`has_theme_item()<class_Theme_method_has_theme_item>`{.interpreted-text
role="ref"} to check for existence, and
`clear_theme_item()<class_Theme_method_clear_theme_item>`{.interpreted-text
role="ref"} to remove the existing property.

\*\*Note:\*\* This method is analogous to calling the corresponding data
type specific method, but can be used for more generalized logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_rename_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_type**(old_theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_rename_type>`{.interpreted-text
role="ref"}

Renames the theme type `old_theme_type` to `theme_type`, if the old type
exists and the new one doesn\'t exist.

\*\*Note:\*\* Renaming a theme type to an empty name or a variation to a
type associated with a built-in class removes type variation connections
in a way that cannot be undone by reversing the rename alone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_color**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_set_color>`{.interpreted-text role="ref"}

Creates or changes the value of the
`Color<class_Color>`{.interpreted-text role="ref"} property defined by
`name` and `theme_type`. Use
`clear_color()<class_Theme_method_clear_color>`{.interpreted-text
role="ref"} to remove the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_constant}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_constant**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, constant:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_set_constant>`{.interpreted-text role="ref"}

Creates or changes the value of the constant property defined by `name`
and `theme_type`. Use
`clear_constant()<class_Theme_method_clear_constant>`{.interpreted-text
role="ref"} to remove the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_font}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_font**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, font:
`Font<class_Font>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_set_font>`{.interpreted-text role="ref"}

Creates or changes the value of the `Font<class_Font>`{.interpreted-text
role="ref"} property defined by `name` and `theme_type`. Use
`clear_font()<class_Theme_method_clear_font>`{.interpreted-text
role="ref"} to remove the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_font_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_font_size**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, font_size:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_set_font_size>`{.interpreted-text role="ref"}

Creates or changes the value of the font size property defined by `name`
and `theme_type`. Use
`clear_font_size()<class_Theme_method_clear_font_size>`{.interpreted-text
role="ref"} to remove the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_icon**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, texture:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_set_icon>`{.interpreted-text role="ref"}

Creates or changes the value of the icon property defined by `name` and
`theme_type`. Use
`clear_icon()<class_Theme_method_clear_icon>`{.interpreted-text
role="ref"} to remove the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_stylebox}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_stylebox**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, texture:
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_set_stylebox>`{.interpreted-text role="ref"}

Creates or changes the value of the
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} property
defined by `name` and `theme_type`. Use
`clear_stylebox()<class_Theme_method_clear_stylebox>`{.interpreted-text
role="ref"} to remove the property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_theme_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_theme_item**(data_type:
`DataType<enum_Theme_DataType>`{.interpreted-text role="ref"}, name:
`StringName<class_StringName>`{.interpreted-text role="ref"},
theme_type: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Theme_method_set_theme_item>`{.interpreted-text
role="ref"}

Creates or changes the value of the theme property of `data_type`
defined by `name` and `theme_type`. Use
`clear_theme_item()<class_Theme_method_clear_theme_item>`{.interpreted-text
role="ref"} to remove the property.

Fails if the `value` type is not accepted by `data_type`.

\*\*Note:\*\* This method is analogous to calling the corresponding data
type specific method, but can be used for more generalized logic.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Theme_method_set_type_variation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_type_variation**(theme_type:
`StringName<class_StringName>`{.interpreted-text role="ref"}, base_type:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Theme_method_set_type_variation>`{.interpreted-text
role="ref"}

Marks `theme_type` as a variation of `base_type`.

This adds `theme_type` as a suggested option for
`Control.theme_type_variation<class_Control_property_theme_type_variation>`{.interpreted-text
role="ref"} on a `Control<class_Control>`{.interpreted-text role="ref"}
that is of the `base_type` class.

Variations can also be nested, i.e. `base_type` can be another
variation. If a chain of variations ends with a `base_type` matching the
class of the `Control<class_Control>`{.interpreted-text role="ref"}, the
whole chain is going to be suggested as options.

\*\*Note:\*\* Suggestions only show up if this theme resource is set as
the project default theme. See
`ProjectSettings.gui/theme/custom<class_ProjectSettings_property_gui/theme/custom>`{.interpreted-text
role="ref"}.
