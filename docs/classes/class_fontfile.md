github_url
:   hide

# FontFile {#class_FontFile}

**Inherits:** `Font<class_Font>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Holds font source data and prerendered glyph cache, imported from a
dynamic or a bitmap font.

::: rst-class
classref-introduction-group
:::

## Description

**FontFile** contains a set of glyphs to represent Unicode characters
imported from a font file, as well as a cache of rasterized glyphs, and
a set of fallback `Font<class_Font>`{.interpreted-text role="ref"}s to
use.

Use `FontVariation<class_FontVariation>`{.interpreted-text role="ref"}
to access specific OpenType variation of the font, create simulated bold
/ slanted version, and draw lines of text.

For more complex text processing, use
`FontVariation<class_FontVariation>`{.interpreted-text role="ref"} in
conjunction with `TextLine<class_TextLine>`{.interpreted-text
role="ref"} or `TextParagraph<class_TextParagraph>`{.interpreted-text
role="ref"}.

Supported font formats:

- Dynamic font importer: TrueType (.ttf), TrueType collection (.ttc),
  OpenType (.otf), OpenType collection (.otc), WOFF (.woff), WOFF2
  (.woff2), Type 1 (.pfb, .pfm).
- Bitmap font importer: AngelCode BMFont (.fnt, .font), text and binary
  (version 3) format variants.
- Monospace image font importer: All supported image formats.

\*\*Note:\*\* A character is a symbol that represents an item (letter,
digit etc.) in an abstract way.

\*\*Note:\*\* A glyph is a bitmap or a shape used to draw one or more
characters in a context-dependent manner. Glyph indices are bound to the
specific font data source.

\*\*Note:\*\* If none of the font data sources contain glyphs for a
character used in a string, the character in question will be replaced
with a box displaying its hexadecimal code.

::::: tabs
::: code-tab
gdscript

var f = load(\"res://BarlowCondensed-Bold.ttf\")
\$Label.add_theme_font_override(\"font\", f)
\$Label.add_theme_font_size_override(\"font_size\", 64)
:::

::: code-tab
csharp

var f =
ResourceLoader.Load\<FontFile\>(\"res://BarlowCondensed-Bold.ttf\");
GetNode(\"Label\").AddThemeFontOverride(\"font\", f);
GetNode(\"Label\").AddThemeFontSizeOverride(\"font_size\", 64);
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Runtime file loading and saving <../tutorials/io/runtime_file_loading_and_saving>`{.interpreted-text
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

## Property Descriptions

:::: {#class_FontFile_property_allow_system_fallback}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**allow_system_fallback** = `true`
`🔗<class_FontFile_property_allow_system_fallback>`{.interpreted-text
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

:::: {#class_FontFile_property_antialiasing}
::: rst-class
classref-property
:::
::::

`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"} **antialiasing** = `1`
`🔗<class_FontFile_property_antialiasing>`{.interpreted-text role="ref"}

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

:::: {#class_FontFile_property_data}
::: rst-class
classref-property
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**data** = `PackedByteArray()`
`🔗<class_FontFile_property_data>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_data**(value:
  `PackedByteArray<class_PackedByteArray>`{.interpreted-text
  role="ref"})
- `PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
  **get_data**()

Contents of the dynamic font source file.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_disable_embedded_bitmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**disable_embedded_bitmaps** = `true`
`🔗<class_FontFile_property_disable_embedded_bitmaps>`{.interpreted-text
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

:::: {#class_FontFile_property_fixed_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fixed_size** = `0`
`🔗<class_FontFile_property_fixed_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fixed_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_fixed_size**()

Font size, used only for the bitmap fonts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_fixed_size_scale_mode}
::: rst-class
classref-property
:::
::::

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"} **fixed_size_scale_mode** = `0`
`🔗<class_FontFile_property_fixed_size_scale_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fixed_size_scale_mode**(value:
  `FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
  role="ref"})
- `FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
  role="ref"} **get_fixed_size_scale_mode**()

Scaling mode, used only for the bitmap fonts with
`fixed_size<class_FontFile_property_fixed_size>`{.interpreted-text
role="ref"} greater than zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_font_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **font_name** =
`""` `🔗<class_FontFile_property_font_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_name**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_font_name**()

Font family name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_font_stretch}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_stretch** = `100`
`🔗<class_FontFile_property_font_stretch>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_stretch**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_stretch**()

Font stretch amount, compared to a normal width. A percentage value
between `50%` and `200%`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_font_style}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
role="ref"}\] **font_style** = `0`
`🔗<class_FontFile_property_font_style>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_style**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
  role="ref"}\] **get_font_style**()

Font style flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_font_weight}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_weight** = `400`
`🔗<class_FontFile_property_font_weight>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_weight**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_weight**()

Weight (boldness) of the font. A value in the `100...999` range, normal
font weight is `400`, bold font weight is `700`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_force_autohinter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **force_autohinter** =
`false` `🔗<class_FontFile_property_force_autohinter>`{.interpreted-text
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
built-in hinting. Used by dynamic fonts only (MSDF fonts don\'t support
hinting).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_generate_mipmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **generate_mipmaps** =
`false` `🔗<class_FontFile_property_generate_mipmaps>`{.interpreted-text
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

:::: {#class_FontFile_property_hinting}
::: rst-class
classref-property
:::
::::

`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
**hinting** = `1`
`🔗<class_FontFile_property_hinting>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hinting**(value:
  `Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"})
- `Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
  **get_hinting**()

Font hinting mode. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_keep_rounding_remainders}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**keep_rounding_remainders** = `true`
`🔗<class_FontFile_property_keep_rounding_remainders>`{.interpreted-text
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

:::: {#class_FontFile_property_modulate_color_glyphs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**modulate_color_glyphs** = `false`
`🔗<class_FontFile_property_modulate_color_glyphs>`{.interpreted-text
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

:::: {#class_FontFile_property_msdf_pixel_range}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **msdf_pixel_range** =
`16` `🔗<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
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
`msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the size of the largest font
outline. The default
`msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} value of `16` allows outline sizes up to `8` to look
correct.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_msdf_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **msdf_size** = `48`
`🔗<class_FontFile_property_msdf_size>`{.interpreted-text role="ref"}

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

:::: {#class_FontFile_property_multichannel_signed_distance_field}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**multichannel_signed_distance_field** = `false`
`🔗<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
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
multichannel signed distance field (MSDF) generated from the dynamic
font vector data. Since this approach does not rely on rasterizing the
font every time its size changes, this allows for resizing the font in
real-time without any performance penalty. Text will also not look
grainy for `Control<class_Control>`{.interpreted-text role="ref"}s that
are scaled down (or for `Label3D<class_Label3D>`{.interpreted-text
role="ref"}s viewed from a long distance). As a downside, font hinting
is not available with MSDF. The lack of font hinting may result in less
crisp and less readable fonts at small sizes.

\*\*Note:\*\* If using font outlines,
`msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the size of the largest font
outline.

\*\*Note:\*\* MSDF font rendering does not render glyphs with
overlapping shapes correctly. Overlapping shapes are not valid per the
OpenType standard, but are still commonly found in many font files,
especially those converted by Google Fonts. To avoid issues with
overlapping glyphs, consider downloading the font file directly from the
type foundry instead of relying on Google Fonts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_opentype_feature_overrides}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**opentype_feature_overrides** = `{}`
`🔗<class_FontFile_property_opentype_feature_overrides>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_opentype_feature_overrides**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_opentype_feature_overrides**()

Font OpenType feature set override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_oversampling}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **oversampling** =
`0.0` `🔗<class_FontFile_property_oversampling>`{.interpreted-text
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

:::: {#class_FontFile_property_style_name}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **style_name** =
`""` `🔗<class_FontFile_property_style_name>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_style_name**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_font_style_name**()

Font style name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_property_subpixel_positioning}
::: rst-class
classref-property
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **subpixel_positioning** = `1`
`🔗<class_FontFile_property_subpixel_positioning>`{.interpreted-text
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
higher memory usage and lower font rasterization speed. Use
`TextServer.SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>`{.interpreted-text
role="ref"} to automatically enable it based on the font size.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FontFile_method_clear_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_cache**()
`🔗<class_FontFile_method_clear_cache>`{.interpreted-text role="ref"}

Removes all font cache entries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_clear_glyphs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_glyphs**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}) `🔗<class_FontFile_method_clear_glyphs>`{.interpreted-text
role="ref"}

Removes all rendered glyph information from the cache entry.

\*\*Note:\*\* This function will not remove textures associated with the
glyphs, use
`remove_texture()<class_FontFile_method_remove_texture>`{.interpreted-text
role="ref"} to remove them manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_clear_kerning_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_kerning_map**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_clear_kerning_map>`{.interpreted-text
role="ref"}

Removes all kerning overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_clear_size_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_size_cache**(cache_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_FontFile_method_clear_size_cache>`{.interpreted-text
role="ref"}

Removes all font sizes from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_clear_textures}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_textures**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_FontFile_method_clear_textures>`{.interpreted-text role="ref"}

Removes all textures from font cache entry.

\*\*Note:\*\* This function will not remove glyphs associated with the
texture, use
`remove_glyph()<class_FontFile_method_remove_glyph>`{.interpreted-text
role="ref"} to remove them manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_cache_ascent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_cache_ascent**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_cache_ascent>`{.interpreted-text
role="ref"}

Returns the font ascent (number of pixels above the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_cache_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_cache_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_cache_count>`{.interpreted-text
role="ref"}

Returns number of the font cache entries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_cache_descent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_cache_descent**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_cache_descent>`{.interpreted-text
role="ref"}

Returns the font descent (number of pixels below the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_cache_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_cache_scale**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_cache_scale>`{.interpreted-text
role="ref"}

Returns scaling factor of the color bitmap font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_cache_underline_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_cache_underline_position**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_cache_underline_position>`{.interpreted-text
role="ref"}

Returns pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_cache_underline_thickness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_cache_underline_thickness**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_cache_underline_thickness>`{.interpreted-text
role="ref"}

Returns thickness of the underline in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_char_from_glyph_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_char_from_glyph_index**(size: `int<class_int>`{.interpreted-text
role="ref"}, glyph_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_char_from_glyph_index>`{.interpreted-text
role="ref"}

Returns character code associated with `glyph_index`, or `0` if
`glyph_index` is invalid. See
`get_glyph_index()<class_FontFile_method_get_glyph_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_embolden}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_embolden**(cache_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FontFile_method_get_embolden>`{.interpreted-text
role="ref"}

Returns embolden strength, if is not equal to zero, emboldens the font
outlines. Negative values reduce the outline thickness.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_extra_baseline_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_extra_baseline_offset**(cache_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_extra_baseline_offset>`{.interpreted-text
role="ref"}

Returns extra baseline offset (as a fraction of font height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_extra_spacing}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_extra_spacing**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_extra_spacing>`{.interpreted-text
role="ref"}

Returns spacing for `spacing` in pixels (not relative to the font size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_face_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_face_index**(cache_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_face_index>`{.interpreted-text role="ref"}

Returns an active face index in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_glyph_advance}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_glyph_advance**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_glyph_advance>`{.interpreted-text
role="ref"}

Returns glyph advance (offset of the next glyph).

\*\*Note:\*\* Advance for glyphs outlines is the same as the base glyph
advance and is not saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_glyph_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_glyph_index**(size:
`int<class_int>`{.interpreted-text role="ref"}, char:
`int<class_int>`{.interpreted-text role="ref"}, variation_selector:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_glyph_index>`{.interpreted-text
role="ref"}

Returns the glyph index of a `char`, optionally modified by the
`variation_selector`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_glyph_list}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_glyph_list**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_glyph_list>`{.interpreted-text role="ref"}

Returns list of rendered glyphs in the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_glyph_offset}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_glyph_offset**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_glyph_offset>`{.interpreted-text
role="ref"}

Returns glyph offset from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_glyph_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_glyph_size**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_glyph_size>`{.interpreted-text role="ref"}

Returns glyph size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_glyph_texture_idx}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_glyph_texture_idx**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_glyph_texture_idx>`{.interpreted-text
role="ref"}

Returns index of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_glyph_uv_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_glyph_uv_rect**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_glyph_uv_rect>`{.interpreted-text
role="ref"}

Returns rectangle in the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_kerning}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_kerning**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FontFile_method_get_kerning>`{.interpreted-text
role="ref"}

Returns kerning for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_kerning_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_kerning_list**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_kerning_list>`{.interpreted-text
role="ref"}

Returns list of the kerning overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_language_support_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_language_support_override**(language:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_language_support_override>`{.interpreted-text
role="ref"}

Returns `true` if support override is enabled for the `language`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_language_support_overrides}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_language_support_overrides**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_language_support_overrides>`{.interpreted-text
role="ref"}

Returns list of language support overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_script_support_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_script_support_override**(script:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_script_support_override>`{.interpreted-text
role="ref"}

Returns `true` if support override is enabled for the `script`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_script_support_overrides}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_script_support_overrides**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_script_support_overrides>`{.interpreted-text
role="ref"}

Returns list of script support overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_size_cache_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_size_cache_list**(cache_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_size_cache_list>`{.interpreted-text
role="ref"}

Returns list of the font sizes in the cache. Each size is
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} with font size
and outline size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_texture_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_texture_count**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_texture_count>`{.interpreted-text
role="ref"}

Returns number of textures used by font cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_texture_image}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**get_texture_image**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_texture_image>`{.interpreted-text
role="ref"}

Returns a copy of the font cache texture image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_texture_offsets}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_texture_offsets**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_texture_offsets>`{.interpreted-text
role="ref"}

Returns a copy of the array containing glyph packing data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_transform**(cache_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_FontFile_method_get_transform>`{.interpreted-text
role="ref"}

Returns 2D transform, applied to the font outlines, can be used for
slanting, flipping and rotating glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_get_variation_coordinates}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_variation_coordinates**(cache_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FontFile_method_get_variation_coordinates>`{.interpreted-text
role="ref"}

Returns variation coordinates for the specified font cache entry. See
`Font.get_supported_variation_list()<class_Font_method_get_supported_variation_list>`{.interpreted-text
role="ref"} for more info.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_load_bitmap_font}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_bitmap_font**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FontFile_method_load_bitmap_font>`{.interpreted-text
role="ref"}

Loads an AngelCode BMFont (.fnt, .font) bitmap font from file `path`.

\*\*Warning:\*\* This method should only be used in the editor or in
cases when you need to load external fonts at run-time, such as fonts
located at the `user://` directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_load_dynamic_font}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_dynamic_font**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FontFile_method_load_dynamic_font>`{.interpreted-text
role="ref"}

Loads a TrueType (.ttf), OpenType (.otf), WOFF (.woff), WOFF2 (.woff2)
or Type 1 (.pfb, .pfm) dynamic font from file `path`.

\*\*Warning:\*\* This method should only be used in the editor or in
cases when you need to load external fonts at run-time, such as fonts
located at the `user://` directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_remove_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_cache**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_FontFile_method_remove_cache>`{.interpreted-text
role="ref"}

Removes specified font cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_remove_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_glyph**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_remove_glyph>`{.interpreted-text role="ref"}

Removes specified rendered glyph information from the cache entry.

\*\*Note:\*\* This function will not remove textures associated with the
glyphs, use
`remove_texture()<class_FontFile_method_remove_texture>`{.interpreted-text
role="ref"} to remove them manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_remove_kerning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_kerning**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_remove_kerning>`{.interpreted-text role="ref"}

Removes kerning override for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_remove_language_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_language_support_override**(language:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_remove_language_support_override>`{.interpreted-text
role="ref"}

Remove language support override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_remove_script_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_script_support_override**(script:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_remove_script_support_override>`{.interpreted-text
role="ref"}

Removes script support override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_remove_size_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_size_cache**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_FontFile_method_remove_size_cache>`{.interpreted-text
role="ref"}

Removes specified font size from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_remove_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_texture**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_FontFile_method_remove_texture>`{.interpreted-text role="ref"}

Removes specified texture from the cache entry.

\*\*Note:\*\* This function will not remove glyphs associated with the
texture. Remove them manually using
`remove_glyph()<class_FontFile_method_remove_glyph>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_render_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**render_glyph**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_render_glyph>`{.interpreted-text role="ref"}

Renders specified glyph to the font cache texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_render_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**render_range**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, start: `int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_render_range>`{.interpreted-text role="ref"}

Renders the range of characters to the font cache texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_cache_ascent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cache_ascent**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
ascent: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_cache_ascent>`{.interpreted-text
role="ref"}

Sets the font ascent (number of pixels above the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_cache_descent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cache_descent**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
descent: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_cache_descent>`{.interpreted-text
role="ref"}

Sets the font descent (number of pixels below the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_cache_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cache_scale**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
scale: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_cache_scale>`{.interpreted-text
role="ref"}

Sets scaling factor of the color bitmap font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_cache_underline_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cache_underline_position**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, underline_position:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_cache_underline_position>`{.interpreted-text
role="ref"}

Sets pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_cache_underline_thickness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cache_underline_thickness**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, underline_thickness:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_cache_underline_thickness>`{.interpreted-text
role="ref"}

Sets thickness of the underline in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_embolden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_embolden**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, strength: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_FontFile_method_set_embolden>`{.interpreted-text
role="ref"}

Sets embolden strength, if is not equal to zero, emboldens the font
outlines. Negative values reduce the outline thickness.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_extra_baseline_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_extra_baseline_offset**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, baseline_offset:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_extra_baseline_offset>`{.interpreted-text
role="ref"}

Sets extra baseline offset (as a fraction of font height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_extra_spacing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_extra_spacing**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_extra_spacing>`{.interpreted-text
role="ref"}

Sets the spacing for `spacing` to `value` in pixels (not relative to the
font size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_face_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_face_index**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, face_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_face_index>`{.interpreted-text role="ref"}

Sets an active face index in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_glyph_advance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_glyph_advance**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph: `int<class_int>`{.interpreted-text role="ref"}, advance:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_glyph_advance>`{.interpreted-text
role="ref"}

Sets glyph advance (offset of the next glyph).

\*\*Note:\*\* Advance for glyphs outlines is the same as the base glyph
advance and is not saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_glyph_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_glyph_offset**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
offset: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_glyph_offset>`{.interpreted-text
role="ref"}

Sets glyph offset from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_glyph_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_glyph_size**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
gl_size: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_glyph_size>`{.interpreted-text role="ref"}

Sets glyph size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_glyph_texture_idx}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_glyph_texture_idx**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"}, texture_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_glyph_texture_idx>`{.interpreted-text
role="ref"}

Sets index of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_glyph_uv_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_glyph_uv_rect**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
uv_rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_glyph_uv_rect>`{.interpreted-text
role="ref"}

Sets rectangle in the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_kerning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_kerning**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
kerning: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_kerning>`{.interpreted-text role="ref"}

Sets kerning for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_language_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_language_support_override**(language:
`String<class_String>`{.interpreted-text role="ref"}, supported:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_language_support_override>`{.interpreted-text
role="ref"}

Adds override for
`Font.is_language_supported()<class_Font_method_is_language_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_script_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_script_support_override**(script:
`String<class_String>`{.interpreted-text role="ref"}, supported:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_script_support_override>`{.interpreted-text
role="ref"}

Adds override for
`Font.is_script_supported()<class_Font_method_is_script_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_texture_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_texture_image**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"}, image: `Image<class_Image>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_texture_image>`{.interpreted-text
role="ref"}

Sets font cache texture image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_texture_offsets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_texture_offsets**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"}, offset:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_FontFile_method_set_texture_offsets>`{.interpreted-text
role="ref"}

Sets array containing glyph packing data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_transform**(cache_index: `int<class_int>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_transform>`{.interpreted-text role="ref"}

Sets 2D transform, applied to the font outlines, can be used for
slanting, flipping, and rotating glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontFile_method_set_variation_coordinates}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_variation_coordinates**(cache_index:
`int<class_int>`{.interpreted-text role="ref"}, variation_coordinates:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_FontFile_method_set_variation_coordinates>`{.interpreted-text
role="ref"}

Sets variation coordinates for the specified font cache entry. See
`Font.get_supported_variation_list()<class_Font_method_get_supported_variation_list>`{.interpreted-text
role="ref"} for more info.
