github_url
:   hide

# FontVariation {#class_FontVariation}

**Inherits:** `Font<class_Font>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A variation of a font with additional settings.

::: rst-class
classref-introduction-group
:::

## Description

Provides OpenType variations, simulated bold / slant, and additional
font settings like OpenType features and extra spacing.

To use simulated bold font variant:

::::: tabs
::: code-tab
gdscript

var fv = FontVariation.new() fv.base_font =
load(\"res://BarlowCondensed-Regular.ttf\") fv.variation_embolden = 1.2
\$Label.add_theme_font_override(\"font\", fv)
\$Label.add_theme_font_size_override(\"font_size\", 64)
:::

::: code-tab
csharp

var fv = new FontVariation();
fv.SetBaseFont(ResourceLoader.Load\<FontFile\>(\"res://BarlowCondensed-Regular.ttf\"));
fv.SetVariationEmbolden(1.2);
GetNode(\"Label\").AddThemeFontOverride(\"font\", fv);
GetNode(\"Label\").AddThemeFontSizeOverride(\"font_size\", 64);
:::
:::::

To set the coordinate of multiple variation axes:

    var fv = FontVariation.new();
    var ts = TextServerManager.get_primary_interface()
    fv.base_font = load("res://BarlowCondensed-Regular.ttf")
    fv.variation_opentype = { ts.name_to_tag("wght"): 900, ts.name_to_tag("custom_hght"): 900 }

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

:::: {#class_FontVariation_property_base_font}
::: rst-class
classref-property
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **base_font**
`🔗<class_FontVariation_property_base_font>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_base_font**(value: `Font<class_Font>`{.interpreted-text
  role="ref"})
- `Font<class_Font>`{.interpreted-text role="ref"} **get_base_font**()

Base font used to create a variation. If not set, default
`Theme<class_Theme>`{.interpreted-text role="ref"} font is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_baseline_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **baseline_offset** =
`0.0`
`🔗<class_FontVariation_property_baseline_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_baseline_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_baseline_offset**()

Extra baseline offset (as a fraction of font height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_opentype_features}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**opentype_features** = `{}`
`🔗<class_FontVariation_property_opentype_features>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_opentype_features**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_opentype_features**()

A set of OpenType feature tags. More info: [OpenType feature
tags](https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_spacing_bottom}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **spacing_bottom** = `0`
`🔗<class_FontVariation_property_spacing_bottom>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spacing**(spacing:
  `SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
  role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_spacing**()

Extra spacing at the bottom of the line in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_spacing_glyph}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **spacing_glyph** = `0`
`🔗<class_FontVariation_property_spacing_glyph>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spacing**(spacing:
  `SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
  role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_spacing**()

Extra spacing between graphical glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_spacing_space}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **spacing_space** = `0`
`🔗<class_FontVariation_property_spacing_space>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spacing**(spacing:
  `SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
  role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_spacing**()

Extra width of the space glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_spacing_top}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **spacing_top** = `0`
`🔗<class_FontVariation_property_spacing_top>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spacing**(spacing:
  `SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
  role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_spacing**()

Extra spacing at the top of the line in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_variation_embolden}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**variation_embolden** = `0.0`
`🔗<class_FontVariation_property_variation_embolden>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_variation_embolden**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_variation_embolden**()

If is not equal to zero, emboldens the font outlines. Negative values
reduce the outline thickness.

\*\*Note:\*\* Emboldened fonts might have self-intersecting outlines,
which will prevent MSDF fonts and
`TextMesh<class_TextMesh>`{.interpreted-text role="ref"} from working
correctly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_variation_face_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **variation_face_index**
= `0`
`🔗<class_FontVariation_property_variation_face_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_variation_face_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_variation_face_index**()

Active face index in the TrueType / OpenType collection file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_variation_opentype}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**variation_opentype** = `{}`
`🔗<class_FontVariation_property_variation_opentype>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_variation_opentype**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_variation_opentype**()

Font OpenType variation coordinates. More info: [OpenType variation
tags](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg).

\*\*Note:\*\* This `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} uses OpenType tags as keys. Variation axes can be identified
both by tags (`int<class_int>`{.interpreted-text role="ref"}, e.g.
`0x77678674`) and names (`String<class_String>`{.interpreted-text
role="ref"}, e.g. `wght`). Some axes might be accessible by multiple
names. For example, `wght` refers to the same axis as `weight`. Tags on
the other hand are unique. To convert between names and tags, use
`TextServer.name_to_tag()<class_TextServer_method_name_to_tag>`{.interpreted-text
role="ref"} and
`TextServer.tag_to_name()<class_TextServer_method_tag_to_name>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* To get available variation axes of a font, use
`Font.get_supported_variation_list()<class_Font_method_get_supported_variation_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FontVariation_property_variation_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**variation_transform** = `Transform2D(1, 0, 0, 1, 0, 0)`
`🔗<class_FontVariation_property_variation_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_variation_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_variation_transform**()

2D transform, applied to the font outlines, can be used for slanting,
flipping and rotating glyphs.

For example, to simulate italic typeface by slanting, apply the
following transform `Transform2D(1.0, slant, 0.0, 1.0, 0.0, 0.0)`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FontVariation_method_set_spacing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_spacing**(spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_FontVariation_method_set_spacing>`{.interpreted-text
role="ref"}

Sets the spacing for `spacing` to `value` in pixels (not relative to the
font size).
