github_url
:   hide

# CharFXTransform {#class_CharFXTransform}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Controls how an individual character will be displayed in a
`RichTextEffect<class_RichTextEffect>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

By setting various properties on this object, you can control how
individual characters will be displayed in a
`RichTextEffect<class_RichTextEffect>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `BBCode in RichTextLabel <../tutorials/ui/bbcode_in_richtextlabel>`{.interpreted-text
  role="doc"}

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

:::: {#class_CharFXTransform_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(0, 0, 0, 1)`
`🔗<class_CharFXTransform_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

The color the character will be drawn with.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_elapsed_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **elapsed_time** =
`0.0`
`🔗<class_CharFXTransform_property_elapsed_time>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_elapsed_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_elapsed_time**()

The time elapsed since the
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"} was
added to the scene tree (in seconds). Time stops when the
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"} is
paused (see
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"}). Resets when the text in the
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"} is
changed.

\*\*Note:\*\* Time still passes while the
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"} is
hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_env}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} **env** =
`{}` `🔗<class_CharFXTransform_property_env>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_environment**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_environment**()

Contains the arguments passed in the opening BBCode tag. By default,
arguments are strings; if their contents match a type such as
`bool<class_bool>`{.interpreted-text role="ref"},
`int<class_int>`{.interpreted-text role="ref"} or
`float<class_float>`{.interpreted-text role="ref"}, they will be
converted automatically. Color codes in the form `#rrggbb` or `#rgb`
will be converted to an opaque `Color<class_Color>`{.interpreted-text
role="ref"}. String arguments may not contain spaces, even if they\'re
quoted. If present, quotes will also be present in the final string.

For example, the opening BBCode tag
`[example foo=hello bar=true baz=42 color=#ffffff]` will map to the
following `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}:

    {"foo": "hello", "bar": true, "baz": 42, "color": Color(1, 1, 1, 1)}

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_font}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **font** = `RID()`
`🔗<class_CharFXTransform_property_font>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font**(value: `RID<class_RID>`{.interpreted-text role="ref"})
- `RID<class_RID>`{.interpreted-text role="ref"} **get_font**()

`TextServer<class_TextServer>`{.interpreted-text role="ref"} RID of the
font used to render glyph, this value can be used with
`TextServer.font_*` methods to retrieve font information.

\*\*Note:\*\* Read-only. Setting this property won\'t affect drawing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_glyph_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **glyph_count** = `0`
`🔗<class_CharFXTransform_property_glyph_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glyph_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_glyph_count**()

Number of glyphs in the grapheme cluster. This value is set in the first
glyph of a cluster.

\*\*Note:\*\* Read-only. Setting this property won\'t affect drawing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_glyph_flags}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **glyph_flags** = `0`
`🔗<class_CharFXTransform_property_glyph_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glyph_flags**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_glyph_flags**()

Glyph flags. See
`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} for more info.

\*\*Note:\*\* Read-only. Setting this property won\'t affect drawing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_glyph_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **glyph_index** = `0`
`🔗<class_CharFXTransform_property_glyph_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_glyph_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_glyph_index**()

Glyph index specific to the
`font<class_CharFXTransform_property_font>`{.interpreted-text
role="ref"}. If you want to replace this glyph, use
`TextServer.font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>`{.interpreted-text
role="ref"} with
`font<class_CharFXTransform_property_font>`{.interpreted-text
role="ref"} to get a new glyph index for a single character.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)`
`🔗<class_CharFXTransform_property_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The position offset the character will be drawn with (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_outline}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **outline** = `false`
`🔗<class_CharFXTransform_property_outline>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_outline**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_outline**()

If `true`, FX transform is called for outline drawing.

\*\*Note:\*\* Read-only. Setting this property won\'t affect drawing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_range}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **range** =
`Vector2i(0, 0)`
`🔗<class_CharFXTransform_property_range>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_range**(value: `Vector2i<class_Vector2i>`{.interpreted-text
  role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_range**()

Absolute character range in the string, corresponding to the glyph.

\*\*Note:\*\* Read-only. Setting this property won\'t affect drawing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_relative_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **relative_index** = `0`
`🔗<class_CharFXTransform_property_relative_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_relative_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_relative_index**()

The character offset of the glyph, relative to the current
`RichTextEffect<class_RichTextEffect>`{.interpreted-text role="ref"}
custom block.

\*\*Note:\*\* Read-only. Setting this property won\'t affect drawing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**transform** = `Transform2D(1, 0, 0, 1, 0, 0)`
`🔗<class_CharFXTransform_property_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_transform**()

The current transform of the current glyph. It can be overridden (for
example, by driving the position and rotation from a curve). You can
also alter the existing value to apply transforms on top of other
effects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CharFXTransform_property_visible}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **visible** = `true`
`🔗<class_CharFXTransform_property_visible>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_visible**()

If `true`, the character will be drawn. If `false`, the character will
be hidden. Characters around hidden characters will reflow to take the
space of hidden characters. If this is not desired, set their
`color<class_CharFXTransform_property_color>`{.interpreted-text
role="ref"} to `Color(1, 1, 1, 0)` instead.
