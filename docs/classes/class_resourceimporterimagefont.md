github_url
:   hide

# ResourceImporterImageFont {#class_ResourceImporterImageFont}

**Inherits:**
`ResourceImporter<class_ResourceImporter>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Imports a bitmap font where all glyphs have the same width and height.

::: rst-class
classref-introduction-group
:::

## Description

This image-based workflow can be easier to use than
`ResourceImporterBMFont<class_ResourceImporterBMFont>`{.interpreted-text
role="ref"}, but it requires all glyphs to have the same width and
height, glyph advances and drawing offsets can be customized. This makes
**ResourceImporterImageFont** most suited to fixed-width fonts.

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

:::: {#class_ResourceImporterImageFont_property_ascent}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **ascent** = `0`
`🔗<class_ResourceImporterImageFont_property_ascent>`{.interpreted-text
role="ref"}

Font ascent (number of pixels above the baseline). If set to `0`, half
of the character height is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_character_margin}
::: rst-class
classref-property
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**character_margin** = `Rect2i(0, 0, 0, 0)`
`🔗<class_ResourceImporterImageFont_property_character_margin>`{.interpreted-text
role="ref"}

Margin applied around every imported glyph. If your font image contains
guides (in the form of lines between glyphs) or if spacing between
characters appears incorrect, try adjusting
`character_margin<class_ResourceImporterImageFont_property_character_margin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_character_ranges}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **character_ranges** = `PackedStringArray()`
`🔗<class_ResourceImporterImageFont_property_character_ranges>`{.interpreted-text
role="ref"}

The character ranges to import from the font image. This is an array
that maps each position on the image (in tile coordinates, not pixels).
The font atlas is traversed from left to right and top to bottom.
Characters can be specified with decimal numbers (127), hexadecimal
numbers (`0x007f`, or `U+007f`) or between single quotes (`'~'`). Ranges
can be specified with a hyphen between characters.

For example, `0-127` represents the full ASCII range. It can also be
written as `0x0000-0x007f` (or `U+0000-U+007f`). As another example,
`' '-'~'` is equivalent to `32-127` and represents the range of
printable (visible) ASCII characters.

For any range, the character advance and offset can be customized by
appending three space-separated integer values (additional advance, x
offset, y offset) to the end. For example `'a'-'b' 4 5 2` sets the
advance to `char_width + 4` and offset to `Vector2(5, 2)` for both
[a]{.title-ref} and [b]{.title-ref} characters.

\*\*Note:\*\* The overall number of characters must not exceed the
number of
`columns<class_ResourceImporterImageFont_property_columns>`{.interpreted-text
role="ref"} multiplied by
`rows<class_ResourceImporterImageFont_property_rows>`{.interpreted-text
role="ref"}. Otherwise, the font will fail to import.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_columns}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **columns** = `1`
`🔗<class_ResourceImporterImageFont_property_columns>`{.interpreted-text
role="ref"}

Number of columns in the font image. See also
`rows<class_ResourceImporterImageFont_property_rows>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_compress}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **compress** = `true`
`🔗<class_ResourceImporterImageFont_property_compress>`{.interpreted-text
role="ref"}

If `true`, uses lossless compression for the resulting font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_descent}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **descent** = `0`
`🔗<class_ResourceImporterImageFont_property_descent>`{.interpreted-text
role="ref"}

Font descent (number of pixels below the baseline). If set to `0`, half
of the character height is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_fallbacks}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **fallbacks** = `[]`
`🔗<class_ResourceImporterImageFont_property_fallbacks>`{.interpreted-text
role="ref"}

List of font fallbacks to use if a glyph isn\'t found in this bitmap
font. Fonts at the beginning of the array are attempted first.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_image_margin}
::: rst-class
classref-property
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"} **image_margin** =
`Rect2i(0, 0, 0, 0)`
`🔗<class_ResourceImporterImageFont_property_image_margin>`{.interpreted-text
role="ref"}

Margin to cut on the sides of the entire image. This can be used to cut
parts of the image that contain attribution information or similar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_kerning_pairs}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **kerning_pairs** = `PackedStringArray()`
`🔗<class_ResourceImporterImageFont_property_kerning_pairs>`{.interpreted-text
role="ref"}

Kerning pairs for the font. Kerning pair adjust the spacing between two
characters.

Each string consist of three space separated values: \"from\" string,
\"to\" string and integer offset. Each combination form the two string
for a kerning pair, e.g, `ab cd -3` will create kerning pairs `ac`,
`ad`, `bc`, and `bd` with offset `-3`. `\uXXXX` escape sequences can be
used to add Unicode characters.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_rows}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **rows** = `1`
`🔗<class_ResourceImporterImageFont_property_rows>`{.interpreted-text
role="ref"}

Number of rows in the font image. See also
`columns<class_ResourceImporterImageFont_property_columns>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ResourceImporterImageFont_property_scaling_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scaling_mode** = `2`
`🔗<class_ResourceImporterImageFont_property_scaling_mode>`{.interpreted-text
role="ref"}

Font scaling mode.
