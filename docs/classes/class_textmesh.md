github_url
:   hide

# TextMesh {#class_TextMesh}

**Inherits:** `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} **\<** `Mesh<class_Mesh>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Generate a `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} from the text.

::: rst-class
classref-introduction-group
:::

## Description

Generate a `PrimitiveMesh<class_PrimitiveMesh>`{.interpreted-text
role="ref"} from the text.

TextMesh can be generated only when using dynamic fonts with vector
glyph contours. Bitmap fonts (including bitmap data in the
TrueType/OpenType containers, like color emoji fonts) are not supported.

The UV layout is arranged in 4 horizontal strips, top to bottom: 40% of
the height for the front face, 40% for the back face, 10% for the outer
edges and 10% for the inner edges.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `3D text <../tutorials/3d/3d_text>`{.interpreted-text role="doc"}

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

:::: {#class_TextMesh_property_autowrap_mode}
::: rst-class
classref-property
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **autowrap_mode** = `0`
`🔗<class_TextMesh_property_autowrap_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autowrap_mode**(value:
  `AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
  role="ref"})
- `AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
  role="ref"} **get_autowrap_mode**()

If set to something other than
`TextServer.AUTOWRAP_OFF<class_TextServer_constant_AUTOWRAP_OFF>`{.interpreted-text
role="ref"}, the text gets wrapped inside the node\'s bounding
rectangle. If you resize the node, it will change its height
automatically to show all the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_curve_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **curve_step** =
`0.5` `🔗<class_TextMesh_property_curve_step>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_curve_step**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_curve_step**()

Step (in pixels) used to approximate Bézier curves.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_depth}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth** = `0.05`
`🔗<class_TextMesh_property_depth>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_depth**()

Depths of the mesh, if set to `0.0` only front surface, is generated,
and UV layout is changed to use full texture for the front face only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_font}
::: rst-class
classref-property
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_TextMesh_property_font>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font**(value: `Font<class_Font>`{.interpreted-text role="ref"})
- `Font<class_Font>`{.interpreted-text role="ref"} **get_font**()

Font configuration used to display text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size** = `16`
`🔗<class_TextMesh_property_font_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_font_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_font_size**()

Font size of the **TextMesh**\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_horizontal_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **horizontal_alignment** = `1`
`🔗<class_TextMesh_property_horizontal_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_horizontal_alignment**()

Controls the text\'s horizontal alignment. Supports left, center, right,
and fill, or justify.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_justification_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] **justification_flags** = `163`
`🔗<class_TextMesh_property_justification_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_justification_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
  role="ref"}\] **get_justification_flags**()

Line fill alignment rules.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_TextMesh_property_language>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_language**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_language**()

Language code used for text shaping algorithms, if left empty current
locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_line_spacing}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **line_spacing** =
`0.0` `🔗<class_TextMesh_property_line_spacing>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_spacing**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_line_spacing**()

Additional vertical spacing between lines (in pixels), spacing is added
to line descent. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)` `🔗<class_TextMesh_property_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_offset**()

The text drawing offset (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_pixel_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **pixel_size** =
`0.01` `🔗<class_TextMesh_property_pixel_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pixel_size**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pixel_size**()

The size of one pixel\'s width on the text to scale it in 3D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_structured_text_bidi_override}
::: rst-class
classref-property
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **structured_text_bidi_override** = `0`
`🔗<class_TextMesh_property_structured_text_bidi_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_structured_text_bidi_override**(value:
  `StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
  role="ref"})
- `StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
  role="ref"} **get_structured_text_bidi_override**()

Set BiDi algorithm override for the structured text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_structured_text_bidi_override_options}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**structured_text_bidi_override_options** = `[]`
`🔗<class_TextMesh_property_structured_text_bidi_override_options>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_structured_text_bidi_override_options**(value:
  `Array<class_Array>`{.interpreted-text role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"}
  **get_structured_text_bidi_override_options**()

Set additional options for BiDi override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_TextMesh_property_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_text**()

The text to generate mesh from.

\*\*Note:\*\* Due to being a
`Resource<class_Resource>`{.interpreted-text role="ref"}, it doesn\'t
follow the rules of
`Node.auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"}. If disabling translation is desired, it should be done
manually with
`Object.set_message_translation()<class_Object_method_set_message_translation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_text_direction}
::: rst-class
classref-property
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**text_direction** = `0`
`🔗<class_TextMesh_property_text_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_direction**(value:
  `Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"})
- `Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
  **get_text_direction**()

Base text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_uppercase}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **uppercase** = `false`
`🔗<class_TextMesh_property_uppercase>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_uppercase**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_uppercase**()

If `true`, all the text displays as UPPERCASE.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_vertical_alignment}
::: rst-class
classref-property
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **vertical_alignment** = `1`
`🔗<class_TextMesh_property_vertical_alignment>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical_alignment**(value:
  `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
  role="ref"})
- `VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
  role="ref"} **get_vertical_alignment**()

Controls the text\'s vertical alignment. Supports top, center, and
bottom.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextMesh_property_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **width** = `500.0`
`🔗<class_TextMesh_property_width>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_width**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_width**()

Text width (in pixels), used for fill alignment.
