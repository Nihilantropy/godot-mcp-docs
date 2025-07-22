github_url
:   hide

# ResourceImporterDynamicFont {#class_ResourceImporterDynamicFont}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports a TTF, TTC, OTF, OTC, WOFF or WOFF2 font file for font rendering
that adapts to any size.

::: rst-class
classref-introduction-group
:::

## Description

Unlike bitmap fonts, dynamic fonts can be resized to any size and still
look crisp. Dynamic fonts also optionally support MSDF font rendering,
which allows for run-time scale changes with no re-rasterization cost.

While WOFF and especially WOFF2 tend to result in smaller file sizes,
there is no universally \"better\" font format. In most situations,
it\'s recommended to use the font format that was shipped on the font
developer\'s website.

See also
`ResourceImporterBMFont<class_ResourceImporterBMFont>`{.interpreted-text
role="ref"} and
`ResourceImporterImageFont<class_ResourceImporterImageFont>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Dynamic fonts - Using
  fonts](../tutorials/ui/gui_using_fonts.html#dynamic-fonts)

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

:::: {#class_ResourceImporterDynamicFont_property_allow_system_fallback}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**allow_system_fallback** = `true`
`🔗<class_ResourceImporterDynamicFont_property_allow_system_fallback>`{.interpreted-text
role="ref"}

If `true`, automatically use system fonts as a fallback if a glyph
isn\'t found in this dynamic font. This makes supporting CJK characters
or emoji more straightforward, as you don\'t need to include a CJK/emoji
font in your project. See also
`fallbacks<class_ResourceImporterDynamicFont_property_fallbacks>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The appearance of system fonts varies across platforms.
Loading system fonts is only supported on Windows, macOS, Linux, Android
and iOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_antialiasing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **antialiasing** = `1`
`🔗<class_ResourceImporterDynamicFont_property_antialiasing>`{.interpreted-text
role="ref"}

The font antialiasing method to use.

\*\*Disabled:\*\* Most suited for pixel art fonts, although you do not
*have* to change the antialiasing from the default **Grayscale** if the
font file was well-created and the font is used at an integer multiple
of its intended size. If pixel art fonts have a bad appearance at their
intended size, try setting
`subpixel_positioning<class_ResourceImporterDynamicFont_property_subpixel_positioning>`{.interpreted-text
role="ref"} to **Disabled** instead.

\*\*Grayscale:\*\* Use grayscale antialiasing. This is the approach used
by the operating system on macOS, Android and iOS.

\*\*LCD Subpixel:\*\* Use antialiasing with subpixel patterns to make
fonts sharper on LCD displays. This is the approach used by the
operating system on Windows and most Linux distributions. The downside
is that this can introduce \"fringing\" on edges, especially on display
technologies that don\'t use standard RGB subpixels (such as OLED
displays). The LCD subpixel layout is globally controlled by
`ProjectSettings.gui/theme/lcd_subpixel_layout<class_ProjectSettings_property_gui/theme/lcd_subpixel_layout>`{.interpreted-text
role="ref"}, which also allows falling back to grayscale antialiasing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_compress}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **compress** = `true`
`🔗<class_ResourceImporterDynamicFont_property_compress>`{.interpreted-text
role="ref"}

If `true`, uses lossless compression for the resulting font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_disable_embedded_bitmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**disable_embedded_bitmaps** = `true`
`🔗<class_ResourceImporterDynamicFont_property_disable_embedded_bitmaps>`{.interpreted-text
role="ref"}

If set to `true`, embedded font bitmap loading is disabled (bitmap-only
and color fonts ignore this property).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_fallbacks}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **fallbacks** = `[]`
`🔗<class_ResourceImporterDynamicFont_property_fallbacks>`{.interpreted-text
role="ref"}

List of font fallbacks to use if a glyph isn\'t found in this dynamic
font. Fonts at the beginning of the array are attempted first, but
fallback fonts that don\'t support the glyph\'s language and script are
attempted last (see
`language_support<class_ResourceImporterDynamicFont_property_language_support>`{.interpreted-text
role="ref"} and
`script_support<class_ResourceImporterDynamicFont_property_script_support>`{.interpreted-text
role="ref"}). See also
`allow_system_fallback<class_ResourceImporterDynamicFont_property_allow_system_fallback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_force_autohinter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **force_autohinter** =
`false`
`🔗<class_ResourceImporterDynamicFont_property_force_autohinter>`{.interpreted-text
role="ref"}

If `true`, forces generation of hinting data for the font using
[FreeType](https://freetype.org/)\'s autohinter. This will make
`hinting<class_ResourceImporterDynamicFont_property_hinting>`{.interpreted-text
role="ref"} effective with fonts that don\'t include hinting data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_generate_mipmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **generate_mipmaps** =
`false`
`🔗<class_ResourceImporterDynamicFont_property_generate_mipmaps>`{.interpreted-text
role="ref"}

If `true`, this font will have mipmaps generated. This prevents text
from looking grainy when a `Control<class_Control>`{.interpreted-text
role="ref"} is scaled down, or when a
`Label3D<class_Label3D>`{.interpreted-text role="ref"} is viewed from a
long distance (if
`Label3D.texture_filter<class_Label3D_property_texture_filter>`{.interpreted-text
role="ref"} is set to a mode that displays mipmaps).

Enabling
`generate_mipmaps<class_ResourceImporterDynamicFont_property_generate_mipmaps>`{.interpreted-text
role="ref"} increases font generation time and memory usage. Only enable
this setting if you actually need it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_hinting}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **hinting** = `1`
`🔗<class_ResourceImporterDynamicFont_property_hinting>`{.interpreted-text
role="ref"}

The hinting mode to use. This controls how aggressively glyph edges
should be snapped to pixels when rasterizing the font. Depending on
personal preference, you may prefer using one hinting mode over the
other. Hinting modes other than **None** are only effective if the font
contains hinting data (see
`force_autohinter<class_ResourceImporterDynamicFont_property_force_autohinter>`{.interpreted-text
role="ref"}).

\*\*None:\*\* Smoothest appearance, which can make the font look blurry
at small sizes.

\*\*Light:\*\* Sharp result by snapping glyph edges to pixels on the Y
axis only.

\*\*Full:\*\* Sharpest by snapping glyph edges to pixels on both X and Y
axes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_keep_rounding_remainders}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**keep_rounding_remainders** = `true`
`🔗<class_ResourceImporterDynamicFont_property_keep_rounding_remainders>`{.interpreted-text
role="ref"}

If set to `true`, when aligning glyphs to the pixel boundaries rounding
remainders are accumulated to ensure more uniform glyph distribution.
This setting has no effect if subpixel positioning is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_language_support}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**language_support** = `{}`
`🔗<class_ResourceImporterDynamicFont_property_language_support>`{.interpreted-text
role="ref"}

Override the list of languages supported by this font. If left empty,
this is supplied by the font metadata. There is usually no need to
change this. See also
`script_support<class_ResourceImporterDynamicFont_property_script_support>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_modulate_color_glyphs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**modulate_color_glyphs** = `false`
`🔗<class_ResourceImporterDynamicFont_property_modulate_color_glyphs>`{.interpreted-text
role="ref"}

If set to `true`, color modulation is applied when drawing colored
glyphs, otherwise it\'s applied to the monochrome glyphs only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_msdf_pixel_range}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **msdf_pixel_range** =
`8`
`🔗<class_ResourceImporterDynamicFont_property_msdf_pixel_range>`{.interpreted-text
role="ref"}

The width of the range around the shape between the minimum and maximum
representable signed distance. If using font outlines,
`msdf_pixel_range<class_ResourceImporterDynamicFont_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the size of the largest font
outline. The default
`msdf_pixel_range<class_ResourceImporterDynamicFont_property_msdf_pixel_range>`{.interpreted-text
role="ref"} value of `8` allows outline sizes up to `4` to look correct.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_msdf_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **msdf_size** = `48`
`🔗<class_ResourceImporterDynamicFont_property_msdf_size>`{.interpreted-text
role="ref"}

Source font size used to generate MSDF textures. Higher values allow for
more precision, but are slower to render and require more memory. Only
increase this value if you notice a visible lack of precision in glyph
rendering. Only effective if
`multichannel_signed_distance_field<class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**multichannel_signed_distance_field** = `false`
`🔗<class_ResourceImporterDynamicFont_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}

If set to `true`, the font will use multichannel signed distance field
(MSDF) for crisp rendering at any size. Since this approach does not
rely on rasterizing the font every time its size changes, this allows
for resizing the font in real-time without any performance penalty. Text
will also not look grainy for `Control<class_Control>`{.interpreted-text
role="ref"}s that are scaled down (or for
`Label3D<class_Label3D>`{.interpreted-text role="ref"}s viewed from a
long distance).

MSDF font rendering can be combined with
`generate_mipmaps<class_ResourceImporterDynamicFont_property_generate_mipmaps>`{.interpreted-text
role="ref"} to further improve font rendering quality when scaled down.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_opentype_features}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**opentype_features** = `{}`
`🔗<class_ResourceImporterDynamicFont_property_opentype_features>`{.interpreted-text
role="ref"}

The OpenType features to enable, disable or set a value for this font.
This can be used to enable optional features provided by the font, such
as ligatures or alternative glyphs. The list of supported OpenType
features varies on a per-font basis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_oversampling}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **oversampling** =
`0.0`
`🔗<class_ResourceImporterDynamicFont_property_oversampling>`{.interpreted-text
role="ref"}

If set to a positive value, overrides the oversampling factor of the
viewport this font is used in. See
`Viewport.oversampling<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"}. This value doesn\'t override the `oversampling` parameter
of `draw_*` methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_preload}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **preload** = `[]`
`🔗<class_ResourceImporterDynamicFont_property_preload>`{.interpreted-text
role="ref"}

The glyph ranges to prerender. This can avoid stuttering during gameplay
when new characters need to be rendered, especially if
`subpixel_positioning<class_ResourceImporterDynamicFont_property_subpixel_positioning>`{.interpreted-text
role="ref"} is enabled. The downside of using preloading is that initial
project load times will increase, as well as memory usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_script_support}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**script_support** = `{}`
`🔗<class_ResourceImporterDynamicFont_property_script_support>`{.interpreted-text
role="ref"}

Override the list of language scripts supported by this font. If left
empty, this is supplied by the font metadata. There is usually no need
to change this. See also
`language_support<class_ResourceImporterDynamicFont_property_language_support>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterDynamicFont_property_subpixel_positioning}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **subpixel_positioning**
= `4`
`🔗<class_ResourceImporterDynamicFont_property_subpixel_positioning>`{.interpreted-text
role="ref"}

Subpixel positioning improves font rendering appearance, especially at
smaller font sizes. The downside is that it takes more time to initially
render the font, which can cause stuttering during gameplay, especially
if used with large font sizes. This should be set to **Disabled** for
fonts with a pixel art appearance.

\*\*Disabled:\*\* No subpixel positioning. Lowest quality, fastest
rendering.

\*\*Auto:\*\* Use subpixel positioning at small font sizes (the chosen
quality varies depending on font size). Large fonts will not use
subpixel positioning. This is a good tradeoff between performance and
quality.

\*\*One Half of a Pixel:\*\* Always perform intermediate subpixel
positioning regardless of font size. High quality, slow rendering.

\*\*One Quarter of a Pixel:\*\* Always perform precise subpixel
positioning regardless of font size. Highest quality, slowest rendering.

\*\*Auto (Except Pixel Fonts):\*\* **Disabled** for the pixel style
fonts (each glyph contours contain only straight horizontal and vertical
lines), **Auto** for the other fonts.
