github_url
:   hide

# SystemFont {#class_SystemFont}

**Inherits:** `Font<class_Font>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A font loaded from a system font. Falls back to a default theme font if
not implemented on the host OS.

::: rst-class
classref-introduction-group
:::

## Description

**SystemFont** loads a font from a system font with the first matching
name from
`font_names<class_SystemFont_property_font_names>`{.interpreted-text
role="ref"}.

It will attempt to match font style, but it\'s not guaranteed.

The returned font might be part of a font collection or be a variable
font with OpenType \"weight\", \"width\" and/or \"italic\" features set.

You can create `FontVariation<class_FontVariation>`{.interpreted-text
role="ref"} of the system font for precise control over its features.

\*\*Note:\*\* This class is implemented on iOS, Linux, macOS and
Windows, on other platforms it will fallback to default theme font.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SystemFont_property_allow_system_fallback}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**allow_system_fallback** = `true`
`🔗<class_SystemFont_property_allow_system_fallback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_allow_system_fallback**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_allow_system_fallback**()

If set to `true`, system fonts can be automatically used as fallbacks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_antialiasing}
::: rst-class
classref-property
:::
::::

`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"} **antialiasing** = `1`
`🔗<class_SystemFont_property_antialiasing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_antialiasing**(value:
  `FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
  role="ref"})
- `FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
  role="ref"} **get_antialiasing**()

Font anti-aliasing mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_disable_embedded_bitmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**disable_embedded_bitmaps** = `true`
`🔗<class_SystemFont_property_disable_embedded_bitmaps>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disable_embedded_bitmaps**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_disable_embedded_bitmaps**()

If set to `true`, embedded font bitmap loading is disabled (bitmap-only
and color fonts ignore this property).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_font_italic}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **font_italic** =
`false` `🔗<class_SystemFont_property_font_italic>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_italic**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_font_italic**()

If set to `true`, italic or oblique font is preferred.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_font_names}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **font_names** = `PackedStringArray()`
`🔗<class_SystemFont_property_font_names>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_names**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_font_names**()

Array of font family names to search, first matching font found is used.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_font_stretch}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_stretch** = `100`
`🔗<class_SystemFont_property_font_stretch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_stretch**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_stretch**()

Preferred font stretch amount, compared to a normal width. A percentage
value between `50%` and `200%`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_font_weight}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_weight** = `400`
`🔗<class_SystemFont_property_font_weight>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_weight**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_weight**()

Preferred weight (boldness) of the font. A value in the `100...999`
range, normal font weight is `400`, bold font weight is `700`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_force_autohinter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **force_autohinter** =
`false`
`🔗<class_SystemFont_property_force_autohinter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_force_autohinter**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_force_autohinter**()

If set to `true`, auto-hinting is supported and preferred over font
built-in hinting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_generate_mipmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **generate_mipmaps** =
`false`
`🔗<class_SystemFont_property_generate_mipmaps>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_generate_mipmaps**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_generate_mipmaps**()

If set to `true`, generate mipmaps for the font textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_hinting}
::: rst-class
classref-property
:::
::::

`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
**hinting** = `1`
`🔗<class_SystemFont_property_hinting>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hinting**(value:
  `Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"})
- `Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
  **get_hinting**()

Font hinting mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_keep_rounding_remainders}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**keep_rounding_remainders** = `true`
`🔗<class_SystemFont_property_keep_rounding_remainders>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_rounding_remainders**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_keep_rounding_remainders**()

If set to `true`, when aligning glyphs to the pixel boundaries rounding
remainders are accumulated to ensure more uniform glyph distribution.
This setting has no effect if subpixel positioning is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_modulate_color_glyphs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**modulate_color_glyphs** = `false`
`🔗<class_SystemFont_property_modulate_color_glyphs>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_modulate_color_glyphs**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_modulate_color_glyphs**()

If set to `true`, color modulation is applied when drawing colored
glyphs, otherwise it\'s applied to the monochrome glyphs only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_msdf_pixel_range}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **msdf_pixel_range** =
`16` `🔗<class_SystemFont_property_msdf_pixel_range>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_msdf_pixel_range**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_msdf_pixel_range**()

The width of the range around the shape between the minimum and maximum
representable signed distance. If using font outlines,
`msdf_pixel_range<class_SystemFont_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the size of the largest font
outline. The default
`msdf_pixel_range<class_SystemFont_property_msdf_pixel_range>`{.interpreted-text
role="ref"} value of `16` allows outline sizes up to `8` to look
correct.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_msdf_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **msdf_size** = `48`
`🔗<class_SystemFont_property_msdf_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_msdf_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_msdf_size**()

Source font size used to generate MSDF textures. Higher values allow for
more precision, but are slower to render and require more memory. Only
increase this value if you notice a visible lack of precision in glyph
rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_multichannel_signed_distance_field}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**multichannel_signed_distance_field** = `false`
`🔗<class_SystemFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_multichannel_signed_distance_field**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_multichannel_signed_distance_field**()

If set to `true`, glyphs of all sizes are rendered using single
multichannel signed distance field generated from the dynamic font
vector data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_oversampling}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **oversampling** =
`0.0` `🔗<class_SystemFont_property_oversampling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_oversampling**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_oversampling**()

If set to a positive value, overrides the oversampling factor of the
viewport this font is used in. See
`Viewport.oversampling<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"}. This value doesn\'t override the `oversampling` parameter
of `draw_*` methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SystemFont_property_subpixel_positioning}
::: rst-class
classref-property
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **subpixel_positioning** = `1`
`🔗<class_SystemFont_property_subpixel_positioning>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_subpixel_positioning**(value:
  `SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
  role="ref"})
- `SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
  role="ref"} **get_subpixel_positioning**()

Font glyph subpixel positioning mode. Subpixel positioning provides
shaper text and better kerning for smaller font sizes, at the cost of
memory usage and font rasterization speed. Use
`TextServer.SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>`{.interpreted-text
role="ref"} to automatically enable it based on the font size.
