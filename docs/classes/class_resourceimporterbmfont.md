github_url
:   hide

# ResourceImporterBMFont {#class_ResourceImporterBMFont}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports a bitmap font in the BMFont (`.fnt`) format.

::: rst-class
classref-introduction-group
:::

## Description

The BMFont format is a format created by the
[BMFont](https://www.angelcode.com/products/bmfont/) program. Many
BMFont-compatible programs also exist, like
[BMGlyph](https://www.bmglyph.com/).

Compared to
`ResourceImporterImageFont<class_ResourceImporterImageFont>`{.interpreted-text
role="ref"}, **ResourceImporterBMFont** supports bitmap fonts with
varying glyph widths/heights.

See also
`ResourceImporterDynamicFont<class_ResourceImporterDynamicFont>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Bitmap fonts - Using
  fonts](../tutorials/ui/gui_using_fonts.html#bitmap-fonts)

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

:::: {#class_ResourceImporterBMFont_property_compress}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **compress** = `true`
`🔗<class_ResourceImporterBMFont_property_compress>`{.interpreted-text
role="ref"}

If `true`, uses lossless compression for the resulting font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterBMFont_property_fallbacks}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **fallbacks** = `[]`
`🔗<class_ResourceImporterBMFont_property_fallbacks>`{.interpreted-text
role="ref"}

List of font fallbacks to use if a glyph isn\'t found in this bitmap
font. Fonts at the beginning of the array are attempted first.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterBMFont_property_scaling_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scaling_mode** = `2`
`🔗<class_ResourceImporterBMFont_property_scaling_mode>`{.interpreted-text
role="ref"}

Font scaling mode.
