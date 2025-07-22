github_url
:   hide

# ThemeDB {#class_ThemeDB}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton that provides access to static information about
`Theme<class_Theme>`{.interpreted-text role="ref"} resources used by the
engine and by your project.

::: rst-class
classref-introduction-group
:::

## Description

This singleton provides access to static information about
`Theme<class_Theme>`{.interpreted-text role="ref"} resources used by the
engine and by your projects. You can fetch the default engine theme, as
well as your project configured theme.

\*\*ThemeDB\*\* also contains fallback values for theme properties.

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

## Signals

:::: {#class_ThemeDB_signal_fallback_changed}
::: rst-class
classref-signal
:::
::::

**fallback_changed**()
`🔗<class_ThemeDB_signal_fallback_changed>`{.interpreted-text
role="ref"}

Emitted when one of the fallback values had been changed. Use it to
refresh the look of controls that may rely on the fallback theme items.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ThemeDB_property_fallback_base_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**fallback_base_scale** = `1.0`
`🔗<class_ThemeDB_property_fallback_base_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallback_base_scale**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fallback_base_scale**()

The fallback base scale factor of every
`Control<class_Control>`{.interpreted-text role="ref"} node and
`Theme<class_Theme>`{.interpreted-text role="ref"} resource. Used when
no other value is available to the control.

See also
`Theme.default_base_scale<class_Theme_property_default_base_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ThemeDB_property_fallback_font}
::: rst-class
classref-property
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **fallback_font**
`🔗<class_ThemeDB_property_fallback_font>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallback_font**(value: `Font<class_Font>`{.interpreted-text
  role="ref"})
- `Font<class_Font>`{.interpreted-text role="ref"}
  **get_fallback_font**()

The fallback font of every `Control<class_Control>`{.interpreted-text
role="ref"} node and `Theme<class_Theme>`{.interpreted-text role="ref"}
resource. Used when no other value is available to the control.

See also
`Theme.default_font<class_Theme_property_default_font>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ThemeDB_property_fallback_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fallback_font_size** =
`16` `🔗<class_ThemeDB_property_fallback_font_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallback_font_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_fallback_font_size**()

The fallback font size of every
`Control<class_Control>`{.interpreted-text role="ref"} node and
`Theme<class_Theme>`{.interpreted-text role="ref"} resource. Used when
no other value is available to the control.

See also
`Theme.default_font_size<class_Theme_property_default_font_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ThemeDB_property_fallback_icon}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**fallback_icon**
`🔗<class_ThemeDB_property_fallback_icon>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallback_icon**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_fallback_icon**()

The fallback icon of every `Control<class_Control>`{.interpreted-text
role="ref"} node and `Theme<class_Theme>`{.interpreted-text role="ref"}
resource. Used when no other value is available to the control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ThemeDB_property_fallback_stylebox}
::: rst-class
classref-property
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
**fallback_stylebox**
`🔗<class_ThemeDB_property_fallback_stylebox>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fallback_stylebox**(value:
  `StyleBox<class_StyleBox>`{.interpreted-text role="ref"})
- `StyleBox<class_StyleBox>`{.interpreted-text role="ref"}
  **get_fallback_stylebox**()

The fallback stylebox of every
`Control<class_Control>`{.interpreted-text role="ref"} node and
`Theme<class_Theme>`{.interpreted-text role="ref"} resource. Used when
no other value is available to the control.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ThemeDB_method_get_default_theme}
::: rst-class
classref-method
:::
::::

`Theme<class_Theme>`{.interpreted-text role="ref"}
**get_default_theme**()
`🔗<class_ThemeDB_method_get_default_theme>`{.interpreted-text
role="ref"}

Returns a reference to the default engine
`Theme<class_Theme>`{.interpreted-text role="ref"}. This theme resource
is responsible for the out-of-the-box look of
`Control<class_Control>`{.interpreted-text role="ref"} nodes and cannot
be overridden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ThemeDB_method_get_project_theme}
::: rst-class
classref-method
:::
::::

`Theme<class_Theme>`{.interpreted-text role="ref"}
**get_project_theme**()
`🔗<class_ThemeDB_method_get_project_theme>`{.interpreted-text
role="ref"}

Returns a reference to the custom project
`Theme<class_Theme>`{.interpreted-text role="ref"}. This theme resources
allows to override the default engine theme for every control node in
the project.

To set the project theme, see
`ProjectSettings.gui/theme/custom<class_ProjectSettings_property_gui/theme/custom>`{.interpreted-text
role="ref"}.
