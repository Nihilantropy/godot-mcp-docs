github_url
:   hide

# TextServer {#class_TextServer}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`TextServerExtension<class_TextServerExtension>`{.interpreted-text
role="ref"}

A server interface for font management and text rendering.

::: rst-class
classref-introduction-group
:::

## Description

**TextServer** is the API backend for managing fonts and rendering text.

\*\*Note:\*\* This is a low-level API, consider using
`TextLine<class_TextLine>`{.interpreted-text role="ref"},
`TextParagraph<class_TextParagraph>`{.interpreted-text role="ref"}, and
`Font<class_Font>`{.interpreted-text role="ref"} classes instead.

This is an abstract class, so to get the currently active **TextServer**
instance, use the following code:

::::: tabs
::: code-tab
gdscript

var ts = TextServerManager.get_primary_interface()
:::

::: code-tab
csharp

var ts = TextServerManager.GetPrimaryInterface();
:::
:::::

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

:::: {#enum_TextServer_FontAntialiasing}
::: rst-class
classref-enumeration
:::
::::

enum **FontAntialiasing**:
`🔗<enum_TextServer_FontAntialiasing>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_FONT_ANTIALIASING_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"} **FONT_ANTIALIASING_NONE** = `0`

Font glyphs are rasterized as 1-bit bitmaps.

:::: {#class_TextServer_constant_FONT_ANTIALIASING_GRAY}
::: rst-class
classref-enumeration-constant
:::
::::

`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"} **FONT_ANTIALIASING_GRAY** = `1`

Font glyphs are rasterized as 8-bit grayscale anti-aliased bitmaps.

:::: {#class_TextServer_constant_FONT_ANTIALIASING_LCD}
::: rst-class
classref-enumeration-constant
:::
::::

`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"} **FONT_ANTIALIASING_LCD** = `2`

Font glyphs are rasterized for LCD screens.

LCD subpixel layout is determined by the value of the
`ProjectSettings.gui/theme/lcd_subpixel_layout<class_ProjectSettings_property_gui/theme/lcd_subpixel_layout>`{.interpreted-text
role="ref"} setting.

LCD subpixel anti-aliasing mode is suitable only for rendering
horizontal, unscaled text in 2D.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_FontLCDSubpixelLayout}
::: rst-class
classref-enumeration
:::
::::

enum **FontLCDSubpixelLayout**:
`🔗<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"}

:::: {#class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"} **FONT_LCD_SUBPIXEL_LAYOUT_NONE** = `0`

Unknown or unsupported subpixel layout, LCD subpixel antialiasing is
disabled.

:::: {#class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_HRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"} **FONT_LCD_SUBPIXEL_LAYOUT_HRGB** = `1`

Horizontal RGB subpixel layout.

:::: {#class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_HBGR}
::: rst-class
classref-enumeration-constant
:::
::::

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"} **FONT_LCD_SUBPIXEL_LAYOUT_HBGR** = `2`

Horizontal BGR subpixel layout.

:::: {#class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_VRGB}
::: rst-class
classref-enumeration-constant
:::
::::

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"} **FONT_LCD_SUBPIXEL_LAYOUT_VRGB** = `3`

Vertical RGB subpixel layout.

:::: {#class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_VBGR}
::: rst-class
classref-enumeration-constant
:::
::::

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"} **FONT_LCD_SUBPIXEL_LAYOUT_VBGR** = `4`

Vertical BGR subpixel layout.

:::: {#class_TextServer_constant_FONT_LCD_SUBPIXEL_LAYOUT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"} **FONT_LCD_SUBPIXEL_LAYOUT_MAX** = `5`

Represents the size of the
`FontLCDSubpixelLayout<enum_TextServer_FontLCDSubpixelLayout>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_Direction}
::: rst-class
classref-enumeration
:::
::::

enum **Direction**: `🔗<enum_TextServer_Direction>`{.interpreted-text
role="ref"}

:::: {#class_TextServer_constant_DIRECTION_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**DIRECTION_AUTO** = `0`

Text direction is determined based on contents and current locale.

:::: {#class_TextServer_constant_DIRECTION_LTR}
::: rst-class
classref-enumeration-constant
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**DIRECTION_LTR** = `1`

Text is written from left to right.

:::: {#class_TextServer_constant_DIRECTION_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**DIRECTION_RTL** = `2`

Text is written from right to left.

:::: {#class_TextServer_constant_DIRECTION_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**DIRECTION_INHERITED** = `3`

Text writing direction is the same as base string writing direction.
Used for BiDi override only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_Orientation}
::: rst-class
classref-enumeration
:::
::::

enum **Orientation**:
`🔗<enum_TextServer_Orientation>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_ORIENTATION_HORIZONTAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
**ORIENTATION_HORIZONTAL** = `0`

Text is written horizontally.

:::: {#class_TextServer_constant_ORIENTATION_VERTICAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
**ORIENTATION_VERTICAL** = `1`

Left to right text is written vertically from top to bottom.

Right to left text is written vertically from bottom to top.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_JustificationFlag}
::: rst-class
classref-enumeration
:::
::::

flags **JustificationFlag**:
`🔗<enum_TextServer_JustificationFlag>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_JUSTIFICATION_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_NONE** = `0`

Do not justify text.

:::: {#class_TextServer_constant_JUSTIFICATION_KASHIDA}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_KASHIDA** = `1`

Justify text by adding and removing kashidas.

:::: {#class_TextServer_constant_JUSTIFICATION_WORD_BOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_WORD_BOUND** = `2`

Justify text by changing width of the spaces between the words.

:::: {#class_TextServer_constant_JUSTIFICATION_TRIM_EDGE_SPACES}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_TRIM_EDGE_SPACES** = `4`

Remove trailing and leading spaces from the justified text.

:::: {#class_TextServer_constant_JUSTIFICATION_AFTER_LAST_TAB}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_AFTER_LAST_TAB** = `8`

Only apply justification to the part of the text after the last tab.

:::: {#class_TextServer_constant_JUSTIFICATION_CONSTRAIN_ELLIPSIS}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_CONSTRAIN_ELLIPSIS** = `16`

Apply justification to the trimmed line with ellipsis.

:::: {#class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_SKIP_LAST_LINE** = `32`

Do not apply justification to the last line of the paragraph.

:::: {#class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS** = `64`

Do not apply justification to the last line of the paragraph with
visible characters (takes precedence over
`JUSTIFICATION_SKIP_LAST_LINE<class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE>`{.interpreted-text
role="ref"}).

:::: {#class_TextServer_constant_JUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE}
::: rst-class
classref-enumeration-constant
:::
::::

`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"} **JUSTIFICATION_DO_NOT_SKIP_SINGLE_LINE** = `128`

Always apply justification to the paragraphs with a single line
(`JUSTIFICATION_SKIP_LAST_LINE<class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE>`{.interpreted-text
role="ref"} and
`JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS<class_TextServer_constant_JUSTIFICATION_SKIP_LAST_LINE_WITH_VISIBLE_CHARS>`{.interpreted-text
role="ref"} are ignored).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_AutowrapMode}
::: rst-class
classref-enumeration
:::
::::

enum **AutowrapMode**:
`🔗<enum_TextServer_AutowrapMode>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_AUTOWRAP_OFF}
::: rst-class
classref-enumeration-constant
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **AUTOWRAP_OFF** = `0`

Autowrap is disabled.

:::: {#class_TextServer_constant_AUTOWRAP_ARBITRARY}
::: rst-class
classref-enumeration-constant
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **AUTOWRAP_ARBITRARY** = `1`

Wraps the text inside the node\'s bounding rectangle by allowing to
break lines at arbitrary positions, which is useful when very limited
space is available.

:::: {#class_TextServer_constant_AUTOWRAP_WORD}
::: rst-class
classref-enumeration-constant
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **AUTOWRAP_WORD** = `2`

Wraps the text inside the node\'s bounding rectangle by soft-breaking
between words.

:::: {#class_TextServer_constant_AUTOWRAP_WORD_SMART}
::: rst-class
classref-enumeration-constant
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **AUTOWRAP_WORD_SMART** = `3`

Behaves similarly to
`AUTOWRAP_WORD<class_TextServer_constant_AUTOWRAP_WORD>`{.interpreted-text
role="ref"}, but force-breaks a word if that single word does not fit in
one line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_LineBreakFlag}
::: rst-class
classref-enumeration
:::
::::

flags **LineBreakFlag**:
`🔗<enum_TextServer_LineBreakFlag>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_BREAK_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_NONE** = `0`

Do not break the line.

:::: {#class_TextServer_constant_BREAK_MANDATORY}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_MANDATORY** = `1`

Break the line at the line mandatory break characters (e.g. `"\n"`).

:::: {#class_TextServer_constant_BREAK_WORD_BOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_WORD_BOUND** = `2`

Break the line between the words.

:::: {#class_TextServer_constant_BREAK_GRAPHEME_BOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_GRAPHEME_BOUND** = `4`

Break the line between any unconnected graphemes.

:::: {#class_TextServer_constant_BREAK_ADAPTIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_ADAPTIVE** = `8`

Should be used only in conjunction with
`BREAK_WORD_BOUND<class_TextServer_constant_BREAK_WORD_BOUND>`{.interpreted-text
role="ref"}, break the line between any unconnected graphemes, if it\'s
impossible to break it between the words.

:::: {#class_TextServer_constant_BREAK_TRIM_EDGE_SPACES}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_TRIM_EDGE_SPACES** = `16`

**Deprecated:** Use
`BREAK_TRIM_START_EDGE_SPACES | BREAK_TRIM_END_EDGE_SPACES` instead.

Remove edge spaces from the broken line segments.

:::: {#class_TextServer_constant_BREAK_TRIM_INDENT}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_TRIM_INDENT** = `32`

Subtract first line indentation width from all lines after the first
one.

:::: {#class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_TRIM_START_EDGE_SPACES** = `64`

Remove spaces and line break characters from the start of broken line
segments.

E.g, after line breaking, the second segment of the following text
`test  \n  next`, is `next` if the flag is set, and `next` if it is not.

:::: {#class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES}
::: rst-class
classref-enumeration-constant
:::
::::

`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"} **BREAK_TRIM_END_EDGE_SPACES** = `128`

Remove spaces and line break characters from the end of broken line
segments.

E.g, after line breaking, the first segment of the following text
`test  \n  next`, is `test` if the flag is set, and `test  \n` if it is
not.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_VisibleCharactersBehavior}
::: rst-class
classref-enumeration
:::
::::

enum **VisibleCharactersBehavior**:
`🔗<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"}

:::: {#class_TextServer_constant_VC_CHARS_BEFORE_SHAPING}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"} **VC_CHARS_BEFORE_SHAPING** = `0`

Trims text before the shaping. e.g, increasing
`Label.visible_characters<class_Label_property_visible_characters>`{.interpreted-text
role="ref"} or
`RichTextLabel.visible_characters<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"} value is visually identical to typing the text.

\*\*Note:\*\* In this mode, trimmed text is not processed at all. It is
not accounted for in line breaking and size calculations.

:::: {#class_TextServer_constant_VC_CHARS_AFTER_SHAPING}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"} **VC_CHARS_AFTER_SHAPING** = `1`

Displays glyphs that are mapped to the first
`Label.visible_characters<class_Label_property_visible_characters>`{.interpreted-text
role="ref"} or
`RichTextLabel.visible_characters<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"} characters from the beginning of the text.

:::: {#class_TextServer_constant_VC_GLYPHS_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"} **VC_GLYPHS_AUTO** = `2`

Displays
`Label.visible_ratio<class_Label_property_visible_ratio>`{.interpreted-text
role="ref"} or
`RichTextLabel.visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} glyphs, starting from the left or from the right, depending
on
`Control.layout_direction<class_Control_property_layout_direction>`{.interpreted-text
role="ref"} value.

:::: {#class_TextServer_constant_VC_GLYPHS_LTR}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"} **VC_GLYPHS_LTR** = `3`

Displays
`Label.visible_ratio<class_Label_property_visible_ratio>`{.interpreted-text
role="ref"} or
`RichTextLabel.visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} glyphs, starting from the left.

:::: {#class_TextServer_constant_VC_GLYPHS_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"} **VC_GLYPHS_RTL** = `4`

Displays
`Label.visible_ratio<class_Label_property_visible_ratio>`{.interpreted-text
role="ref"} or
`RichTextLabel.visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} glyphs, starting from the right.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_OverrunBehavior}
::: rst-class
classref-enumeration
:::
::::

enum **OverrunBehavior**:
`🔗<enum_TextServer_OverrunBehavior>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_OVERRUN_NO_TRIMMING}
::: rst-class
classref-enumeration-constant
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **OVERRUN_NO_TRIMMING** = `0`

No text trimming is performed.

:::: {#class_TextServer_constant_OVERRUN_TRIM_CHAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **OVERRUN_TRIM_CHAR** = `1`

Trims the text per character.

:::: {#class_TextServer_constant_OVERRUN_TRIM_WORD}
::: rst-class
classref-enumeration-constant
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **OVERRUN_TRIM_WORD** = `2`

Trims the text per word.

:::: {#class_TextServer_constant_OVERRUN_TRIM_ELLIPSIS}
::: rst-class
classref-enumeration-constant
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **OVERRUN_TRIM_ELLIPSIS** = `3`

Trims the text per character and adds an ellipsis to indicate that parts
are hidden if trimmed text is 6 characters or longer.

:::: {#class_TextServer_constant_OVERRUN_TRIM_WORD_ELLIPSIS}
::: rst-class
classref-enumeration-constant
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **OVERRUN_TRIM_WORD_ELLIPSIS** = `4`

Trims the text per word and adds an ellipsis to indicate that parts are
hidden if trimmed text is 6 characters or longer.

:::: {#class_TextServer_constant_OVERRUN_TRIM_ELLIPSIS_FORCE}
::: rst-class
classref-enumeration-constant
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **OVERRUN_TRIM_ELLIPSIS_FORCE** = `5`

Trims the text per character and adds an ellipsis to indicate that parts
are hidden regardless of trimmed text length.

:::: {#class_TextServer_constant_OVERRUN_TRIM_WORD_ELLIPSIS_FORCE}
::: rst-class
classref-enumeration-constant
:::
::::

`OverrunBehavior<enum_TextServer_OverrunBehavior>`{.interpreted-text
role="ref"} **OVERRUN_TRIM_WORD_ELLIPSIS_FORCE** = `6`

Trims the text per word and adds an ellipsis to indicate that parts are
hidden regardless of trimmed text length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_TextOverrunFlag}
::: rst-class
classref-enumeration
:::
::::

flags **TextOverrunFlag**:
`🔗<enum_TextServer_TextOverrunFlag>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_OVERRUN_NO_TRIM}
::: rst-class
classref-enumeration-constant
:::
::::

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"} **OVERRUN_NO_TRIM** = `0`

No trimming is performed.

:::: {#class_TextServer_constant_OVERRUN_TRIM}
::: rst-class
classref-enumeration-constant
:::
::::

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"} **OVERRUN_TRIM** = `1`

Trims the text when it exceeds the given width.

:::: {#class_TextServer_constant_OVERRUN_TRIM_WORD_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"} **OVERRUN_TRIM_WORD_ONLY** = `2`

Trims the text per word instead of per grapheme.

:::: {#class_TextServer_constant_OVERRUN_ADD_ELLIPSIS}
::: rst-class
classref-enumeration-constant
:::
::::

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"} **OVERRUN_ADD_ELLIPSIS** = `4`

Determines whether an ellipsis should be added at the end of the text.

:::: {#class_TextServer_constant_OVERRUN_ENFORCE_ELLIPSIS}
::: rst-class
classref-enumeration-constant
:::
::::

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"} **OVERRUN_ENFORCE_ELLIPSIS** = `8`

Determines whether the ellipsis at the end of the text is enforced and
may not be hidden.

:::: {#class_TextServer_constant_OVERRUN_JUSTIFICATION_AWARE}
::: rst-class
classref-enumeration-constant
:::
::::

`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"} **OVERRUN_JUSTIFICATION_AWARE** = `16`

Accounts for the text being justified before attempting to trim it (see
`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_GraphemeFlag}
::: rst-class
classref-enumeration
:::
::::

flags **GraphemeFlag**:
`🔗<enum_TextServer_GraphemeFlag>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_GRAPHEME_IS_VALID}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_VALID** = `1`

Grapheme is supported by the font, and can be drawn.

:::: {#class_TextServer_constant_GRAPHEME_IS_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_RTL** = `2`

Grapheme is part of right-to-left or bottom-to-top run.

:::: {#class_TextServer_constant_GRAPHEME_IS_VIRTUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_VIRTUAL** = `4`

Grapheme is not part of source text, it was added by justification
process.

:::: {#class_TextServer_constant_GRAPHEME_IS_SPACE}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_SPACE** = `8`

Grapheme is whitespace.

:::: {#class_TextServer_constant_GRAPHEME_IS_BREAK_HARD}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_BREAK_HARD** = `16`

Grapheme is mandatory break point (e.g. `"\n"`).

:::: {#class_TextServer_constant_GRAPHEME_IS_BREAK_SOFT}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_BREAK_SOFT** = `32`

Grapheme is optional break point (e.g. space).

:::: {#class_TextServer_constant_GRAPHEME_IS_TAB}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_TAB** = `64`

Grapheme is the tabulation character.

:::: {#class_TextServer_constant_GRAPHEME_IS_ELONGATION}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_ELONGATION** = `128`

Grapheme is kashida.

:::: {#class_TextServer_constant_GRAPHEME_IS_PUNCTUATION}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_PUNCTUATION** = `256`

Grapheme is punctuation character.

:::: {#class_TextServer_constant_GRAPHEME_IS_UNDERSCORE}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_UNDERSCORE** = `512`

Grapheme is underscore character.

:::: {#class_TextServer_constant_GRAPHEME_IS_CONNECTED}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_CONNECTED** = `1024`

Grapheme is connected to the previous grapheme. Breaking line before
this grapheme is not safe.

:::: {#class_TextServer_constant_GRAPHEME_IS_SAFE_TO_INSERT_TATWEEL}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_SAFE_TO_INSERT_TATWEEL** = `2048`

It is safe to insert a U+0640 before this grapheme for elongation.

:::: {#class_TextServer_constant_GRAPHEME_IS_EMBEDDED_OBJECT}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_EMBEDDED_OBJECT** = `4096`

Grapheme is an object replacement character for the embedded object.

:::: {#class_TextServer_constant_GRAPHEME_IS_SOFT_HYPHEN}
::: rst-class
classref-enumeration-constant
:::
::::

`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"} **GRAPHEME_IS_SOFT_HYPHEN** = `8192`

Grapheme is a soft hyphen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_Hinting}
::: rst-class
classref-enumeration
:::
::::

enum **Hinting**: `🔗<enum_TextServer_Hinting>`{.interpreted-text
role="ref"}

:::: {#class_TextServer_constant_HINTING_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
**HINTING_NONE** = `0`

Disables font hinting (smoother but less crisp).

:::: {#class_TextServer_constant_HINTING_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
**HINTING_LIGHT** = `1`

Use the light font hinting mode.

:::: {#class_TextServer_constant_HINTING_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
**HINTING_NORMAL** = `2`

Use the default font hinting mode (crisper but less smooth).

\*\*Note:\*\* This hinting mode changes both horizontal and vertical
glyph metrics. If applied to monospace font, some glyphs might have
different width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_SubpixelPositioning}
::: rst-class
classref-enumeration
:::
::::

enum **SubpixelPositioning**:
`🔗<enum_TextServer_SubpixelPositioning>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_SUBPIXEL_POSITIONING_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **SUBPIXEL_POSITIONING_DISABLED** = `0`

Glyph horizontal position is rounded to the whole pixel size, each glyph
is rasterized once.

:::: {#class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **SUBPIXEL_POSITIONING_AUTO** = `1`

Glyph horizontal position is rounded based on font size.

- To one quarter of the pixel size if font size is smaller or equal to
  `SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE<class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE>`{.interpreted-text
  role="ref"}.
- To one half of the pixel size if font size is smaller or equal to
  `SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE<class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE>`{.interpreted-text
  role="ref"}.
- To the whole pixel size for larger fonts.

:::: {#class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_HALF}
::: rst-class
classref-enumeration-constant
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **SUBPIXEL_POSITIONING_ONE_HALF** = `2`

Glyph horizontal position is rounded to one half of the pixel size, each
glyph is rasterized up to two times.

:::: {#class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_QUARTER}
::: rst-class
classref-enumeration-constant
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **SUBPIXEL_POSITIONING_ONE_QUARTER** = `3`

Glyph horizontal position is rounded to one quarter of the pixel size,
each glyph is rasterized up to four times.

:::: {#class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **SUBPIXEL_POSITIONING_ONE_HALF_MAX_SIZE** = `20`

Maximum font size which will use \"one half of the pixel\" subpixel
positioning in
`SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>`{.interpreted-text
role="ref"} mode.

:::: {#class_TextServer_constant_SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **SUBPIXEL_POSITIONING_ONE_QUARTER_MAX_SIZE** = `16`

Maximum font size which will use \"one quarter of the pixel\" subpixel
positioning in
`SUBPIXEL_POSITIONING_AUTO<class_TextServer_constant_SUBPIXEL_POSITIONING_AUTO>`{.interpreted-text
role="ref"} mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_Feature}
::: rst-class
classref-enumeration
:::
::::

enum **Feature**: `🔗<enum_TextServer_Feature>`{.interpreted-text
role="ref"}

:::: {#class_TextServer_constant_FEATURE_SIMPLE_LAYOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_SIMPLE_LAYOUT** = `1`

TextServer supports simple text layouts.

:::: {#class_TextServer_constant_FEATURE_BIDI_LAYOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_BIDI_LAYOUT** = `2`

TextServer supports bidirectional text layouts.

:::: {#class_TextServer_constant_FEATURE_VERTICAL_LAYOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_VERTICAL_LAYOUT** = `4`

TextServer supports vertical layouts.

:::: {#class_TextServer_constant_FEATURE_SHAPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_SHAPING** = `8`

TextServer supports complex text shaping.

:::: {#class_TextServer_constant_FEATURE_KASHIDA_JUSTIFICATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_KASHIDA_JUSTIFICATION** = `16`

TextServer supports justification using kashidas.

:::: {#class_TextServer_constant_FEATURE_BREAK_ITERATORS}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_BREAK_ITERATORS** = `32`

TextServer supports complex line/word breaking rules (e.g. dictionary
based).

:::: {#class_TextServer_constant_FEATURE_FONT_BITMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_FONT_BITMAP** = `64`

TextServer supports loading bitmap fonts.

:::: {#class_TextServer_constant_FEATURE_FONT_DYNAMIC}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_FONT_DYNAMIC** = `128`

TextServer supports loading dynamic (TrueType, OpeType, etc.) fonts.

:::: {#class_TextServer_constant_FEATURE_FONT_MSDF}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_FONT_MSDF** = `256`

TextServer supports multichannel signed distance field dynamic font
rendering.

:::: {#class_TextServer_constant_FEATURE_FONT_SYSTEM}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_FONT_SYSTEM** = `512`

TextServer supports loading system fonts.

:::: {#class_TextServer_constant_FEATURE_FONT_VARIABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_FONT_VARIABLE** = `1024`

TextServer supports variable fonts.

:::: {#class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION** = `2048`

TextServer supports locale dependent and context sensitive case
conversion.

:::: {#class_TextServer_constant_FEATURE_USE_SUPPORT_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_USE_SUPPORT_DATA** = `4096`

TextServer require external data file for some features, see
`load_support_data()<class_TextServer_method_load_support_data>`{.interpreted-text
role="ref"}.

:::: {#class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_UNICODE_IDENTIFIERS** = `8192`

TextServer supports UAX #31 identifier validation, see
`is_valid_identifier()<class_TextServer_method_is_valid_identifier>`{.interpreted-text
role="ref"}.

:::: {#class_TextServer_constant_FEATURE_UNICODE_SECURITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}
**FEATURE_UNICODE_SECURITY** = `16384`

TextServer supports [Unicode Technical Report
#36](https://unicode.org/reports/tr36/) and [Unicode Technical Standard
#39](https://unicode.org/reports/tr39/) based spoof detection features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_ContourPointTag}
::: rst-class
classref-enumeration
:::
::::

enum **ContourPointTag**:
`🔗<enum_TextServer_ContourPointTag>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_CONTOUR_CURVE_TAG_ON}
::: rst-class
classref-enumeration-constant
:::
::::

`ContourPointTag<enum_TextServer_ContourPointTag>`{.interpreted-text
role="ref"} **CONTOUR_CURVE_TAG_ON** = `1`

Contour point is on the curve.

:::: {#class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC}
::: rst-class
classref-enumeration-constant
:::
::::

`ContourPointTag<enum_TextServer_ContourPointTag>`{.interpreted-text
role="ref"} **CONTOUR_CURVE_TAG_OFF_CONIC** = `0`

Contour point isn\'t on the curve, but serves as a control point for a
conic (quadratic) Bézier arc.

:::: {#class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CUBIC}
::: rst-class
classref-enumeration-constant
:::
::::

`ContourPointTag<enum_TextServer_ContourPointTag>`{.interpreted-text
role="ref"} **CONTOUR_CURVE_TAG_OFF_CUBIC** = `2`

Contour point isn\'t on the curve, but serves as a control point for a
cubic Bézier arc.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_SpacingType}
::: rst-class
classref-enumeration
:::
::::

enum **SpacingType**:
`🔗<enum_TextServer_SpacingType>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_SPACING_GLYPH}
::: rst-class
classref-enumeration-constant
:::
::::

`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text role="ref"}
**SPACING_GLYPH** = `0`

Spacing for each glyph.

:::: {#class_TextServer_constant_SPACING_SPACE}
::: rst-class
classref-enumeration-constant
:::
::::

`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text role="ref"}
**SPACING_SPACE** = `1`

Spacing for the space character.

:::: {#class_TextServer_constant_SPACING_TOP}
::: rst-class
classref-enumeration-constant
:::
::::

`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text role="ref"}
**SPACING_TOP** = `2`

Spacing at the top of the line.

:::: {#class_TextServer_constant_SPACING_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text role="ref"}
**SPACING_BOTTOM** = `3`

Spacing at the bottom of the line.

:::: {#class_TextServer_constant_SPACING_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text role="ref"}
**SPACING_MAX** = `4`

Represents the size of the
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_FontStyle}
::: rst-class
classref-enumeration
:::
::::

flags **FontStyle**: `🔗<enum_TextServer_FontStyle>`{.interpreted-text
role="ref"}

:::: {#class_TextServer_constant_FONT_BOLD}
::: rst-class
classref-enumeration-constant
:::
::::

`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text role="ref"}
**FONT_BOLD** = `1`

Font is bold.

:::: {#class_TextServer_constant_FONT_ITALIC}
::: rst-class
classref-enumeration-constant
:::
::::

`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text role="ref"}
**FONT_ITALIC** = `2`

Font is italic or oblique.

:::: {#class_TextServer_constant_FONT_FIXED_WIDTH}
::: rst-class
classref-enumeration-constant
:::
::::

`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text role="ref"}
**FONT_FIXED_WIDTH** = `4`

Font has fixed-width characters (also known as monospace).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_StructuredTextParser}
::: rst-class
classref-enumeration
:::
::::

enum **StructuredTextParser**:
`🔗<enum_TextServer_StructuredTextParser>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_STRUCTURED_TEXT_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **STRUCTURED_TEXT_DEFAULT** = `0`

Use default Unicode BiDi algorithm.

:::: {#class_TextServer_constant_STRUCTURED_TEXT_URI}
::: rst-class
classref-enumeration-constant
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **STRUCTURED_TEXT_URI** = `1`

BiDi override for URI.

:::: {#class_TextServer_constant_STRUCTURED_TEXT_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **STRUCTURED_TEXT_FILE** = `2`

BiDi override for file path.

:::: {#class_TextServer_constant_STRUCTURED_TEXT_EMAIL}
::: rst-class
classref-enumeration-constant
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **STRUCTURED_TEXT_EMAIL** = `3`

BiDi override for email.

:::: {#class_TextServer_constant_STRUCTURED_TEXT_LIST}
::: rst-class
classref-enumeration-constant
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **STRUCTURED_TEXT_LIST** = `4`

BiDi override for lists. Structured text options: list separator
`String<class_String>`{.interpreted-text role="ref"}.

:::: {#class_TextServer_constant_STRUCTURED_TEXT_GDSCRIPT}
::: rst-class
classref-enumeration-constant
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **STRUCTURED_TEXT_GDSCRIPT** = `5`

BiDi override for GDScript.

:::: {#class_TextServer_constant_STRUCTURED_TEXT_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **STRUCTURED_TEXT_CUSTOM** = `6`

User defined structured text BiDi override function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextServer_FixedSizeScaleMode}
::: rst-class
classref-enumeration
:::
::::

enum **FixedSizeScaleMode**:
`🔗<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text role="ref"}

:::: {#class_TextServer_constant_FIXED_SIZE_SCALE_DISABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"} **FIXED_SIZE_SCALE_DISABLE** = `0`

Bitmap font is not scaled.

:::: {#class_TextServer_constant_FIXED_SIZE_SCALE_INTEGER_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"} **FIXED_SIZE_SCALE_INTEGER_ONLY** = `1`

Bitmap font is scaled to the closest integer multiple of the font\'s
fixed size. This is the recommended option for pixel art fonts.

:::: {#class_TextServer_constant_FIXED_SIZE_SCALE_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"} **FIXED_SIZE_SCALE_ENABLED** = `2`

Bitmap font is scaled to an arbitrary (fractional) size. This is the
recommended option for non-pixel art fonts.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TextServer_method_create_font}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **create_font**()
`🔗<class_TextServer_method_create_font>`{.interpreted-text role="ref"}

Creates a new, empty font cache entry resource. To free the resulting
resource, use the
`free_rid()<class_TextServer_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_create_font_linked_variation}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**create_font_linked_variation**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_create_font_linked_variation>`{.interpreted-text
role="ref"}

Creates a new variation existing font which is reusing the same glyph
cache and font data. To free the resulting resource, use the
`free_rid()<class_TextServer_method_free_rid>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_create_shaped_text}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**create_shaped_text**(direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0) `🔗<class_TextServer_method_create_shaped_text>`{.interpreted-text
role="ref"}

Creates a new buffer for complex text layout, with the given `direction`
and `orientation`. To free the resulting buffer, use
`free_rid()<class_TextServer_method_free_rid>`{.interpreted-text
role="ref"} method.

\*\*Note:\*\* Direction is ignored if server does not support
`FEATURE_BIDI_LAYOUT<class_TextServer_constant_FEATURE_BIDI_LAYOUT>`{.interpreted-text
role="ref"} feature (supported by
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* Orientation is ignored if server does not support
`FEATURE_VERTICAL_LAYOUT<class_TextServer_constant_FEATURE_VERTICAL_LAYOUT>`{.interpreted-text
role="ref"} feature (supported by
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_draw_hex_code_box}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**draw_hex_code_box**(canvas: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_draw_hex_code_box>`{.interpreted-text
role="ref"}

Draws box displaying character hexadecimal code. Used for replacing
missing characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_clear_glyphs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_clear_glyphs**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_clear_glyphs>`{.interpreted-text
role="ref"}

Removes all rendered glyph information from the cache entry.

\*\*Note:\*\* This function will not remove textures associated with the
glyphs, use
`font_remove_texture()<class_TextServer_method_font_remove_texture>`{.interpreted-text
role="ref"} to remove them manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_clear_kerning_map}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_clear_kerning_map**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_clear_kerning_map>`{.interpreted-text
role="ref"}

Removes all kerning overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_clear_size_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_clear_size_cache**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_clear_size_cache>`{.interpreted-text
role="ref"}

Removes all font sizes from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_clear_system_fallback_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_clear_system_fallback_cache**()
`🔗<class_TextServer_method_font_clear_system_fallback_cache>`{.interpreted-text
role="ref"}

Frees all automatically loaded system fonts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_clear_textures}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_clear_textures**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_clear_textures>`{.interpreted-text
role="ref"}

Removes all textures from font cache entry.

\*\*Note:\*\* This function will not remove glyphs associated with the
texture, use
`font_remove_glyph()<class_TextServer_method_font_remove_glyph>`{.interpreted-text
role="ref"} to remove them manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_draw_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_draw_glyph**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"},
size: `int<class_int>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_draw_glyph>`{.interpreted-text
role="ref"}

Draws single glyph into a canvas item at the position, using `font_rid`
at the size `size`. If `oversampling` is greater than zero, it is used
as font oversampling factor, otherwise viewport oversampling settings
are used.

\*\*Note:\*\* Glyph index is specific to the font, use glyphs indices
returned by
`shaped_text_get_glyphs()<class_TextServer_method_shaped_text_get_glyphs>`{.interpreted-text
role="ref"} or
`font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If there are pending glyphs to render, calling this
function might trigger the texture cache update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_draw_glyph_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_draw_glyph_outline**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"},
size: `int<class_int>`{.interpreted-text role="ref"}, outline_size:
`int<class_int>`{.interpreted-text role="ref"}, pos:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_draw_glyph_outline>`{.interpreted-text
role="ref"}

Draws single glyph outline of size `outline_size` into a canvas item at
the position, using `font_rid` at the size `size`. If `oversampling` is
greater than zero, it is used as font oversampling factor, otherwise
viewport oversampling settings are used.

\*\*Note:\*\* Glyph index is specific to the font, use glyphs indices
returned by
`shaped_text_get_glyphs()<class_TextServer_method_shaped_text_get_glyphs>`{.interpreted-text
role="ref"} or
`font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If there are pending glyphs to render, calling this
function might trigger the texture cache update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_antialiasing}
::: rst-class
classref-method
:::
::::

`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"} **font_get_antialiasing**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_antialiasing>`{.interpreted-text
role="ref"}

Returns font anti-aliasing mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_ascent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_ascent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_ascent>`{.interpreted-text
role="ref"}

Returns the font ascent (number of pixels above the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_baseline_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_baseline_offset**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_baseline_offset>`{.interpreted-text
role="ref"}

Returns extra baseline offset (as a fraction of font height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_char_from_glyph_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_char_from_glyph_index**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, glyph_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_char_from_glyph_index>`{.interpreted-text
role="ref"}

Returns character code associated with `glyph_index`, or `0` if
`glyph_index` is invalid. See
`font_get_glyph_index()<class_TextServer_method_font_get_glyph_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_descent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_descent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_descent>`{.interpreted-text
role="ref"}

Returns the font descent (number of pixels below the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_disable_embedded_bitmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_get_disable_embedded_bitmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_disable_embedded_bitmaps>`{.interpreted-text
role="ref"}

Returns whether the font\'s embedded bitmap loading is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_embolden}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_embolden**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_embolden>`{.interpreted-text
role="ref"}

Returns font embolden strength.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_face_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_face_count**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_face_count>`{.interpreted-text
role="ref"}

Returns number of faces in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_face_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_face_index**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_face_index>`{.interpreted-text
role="ref"}

Returns an active face index in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_fixed_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_fixed_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_fixed_size>`{.interpreted-text
role="ref"}

Returns bitmap font fixed size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_fixed_size_scale_mode}
::: rst-class
classref-method
:::
::::

`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"} **font_get_fixed_size_scale_mode**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_fixed_size_scale_mode>`{.interpreted-text
role="ref"}

Returns bitmap font scaling mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_generate_mipmaps}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_get_generate_mipmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_generate_mipmaps>`{.interpreted-text
role="ref"}

Returns `true` if font texture mipmap generation is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_global_oversampling}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_global_oversampling**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_global_oversampling>`{.interpreted-text
role="ref"}

**Deprecated:** Use `Viewport<class_Viewport>`{.interpreted-text
role="ref"} oversampling, or the `oversampling` argument of the `draw_*`
methods instead.

Deprecated. This method always returns `1.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_advance}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**font_get_glyph_advance**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_advance>`{.interpreted-text
role="ref"}

Returns glyph advance (offset of the next glyph).

\*\*Note:\*\* Advance for glyphs outlines is the same as the base glyph
advance and is not saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_contours}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**font_get_glyph_contours**(font: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_contours>`{.interpreted-text
role="ref"}

Returns outline contours of the glyph as a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following contents:

`points` -
`PackedVector3Array<class_PackedVector3Array>`{.interpreted-text
role="ref"}, containing outline points. `x` and `y` are point
coordinates. `z` is the type of the point, using the
`ContourPointTag<enum_TextServer_ContourPointTag>`{.interpreted-text
role="ref"} values.

`contours` -
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"}, containing indices the end points of each contour.

`orientation` - `bool<class_bool>`{.interpreted-text role="ref"},
contour orientation. If `true`, clockwise contours must be filled.

- Two successive
  `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>`{.interpreted-text
  role="ref"} points indicate a line segment.
- One
  `CONTOUR_CURVE_TAG_OFF_CONIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC>`{.interpreted-text
  role="ref"} point between two
  `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>`{.interpreted-text
  role="ref"} points indicates a single conic (quadratic) Bézier arc.
- Two
  `CONTOUR_CURVE_TAG_OFF_CUBIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CUBIC>`{.interpreted-text
  role="ref"} points between two
  `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>`{.interpreted-text
  role="ref"} points indicate a single cubic Bézier arc.
- Two successive
  `CONTOUR_CURVE_TAG_OFF_CONIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC>`{.interpreted-text
  role="ref"} points indicate two successive conic (quadratic) Bézier
  arcs with a virtual
  `CONTOUR_CURVE_TAG_ON<class_TextServer_constant_CONTOUR_CURVE_TAG_ON>`{.interpreted-text
  role="ref"} point at their middle.
- Each contour is closed. The last point of a contour uses the first
  point of a contour as its next point, and vice versa. The first point
  can be
  `CONTOUR_CURVE_TAG_OFF_CONIC<class_TextServer_constant_CONTOUR_CURVE_TAG_OFF_CONIC>`{.interpreted-text
  role="ref"} point.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_glyph_index**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"}, char:
`int<class_int>`{.interpreted-text role="ref"}, variation_selector:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_index>`{.interpreted-text
role="ref"}

Returns the glyph index of a `char`, optionally modified by the
`variation_selector`. See
`font_get_char_from_glyph_index()<class_TextServer_method_font_get_char_from_glyph_index>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_list}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**font_get_glyph_list**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_list>`{.interpreted-text
role="ref"}

Returns list of rendered glyphs in the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_offset}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**font_get_glyph_offset**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_offset>`{.interpreted-text
role="ref"}

Returns glyph offset from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**font_get_glyph_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_size>`{.interpreted-text
role="ref"}

Returns size of the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_texture_idx}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_glyph_texture_idx**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_texture_idx>`{.interpreted-text
role="ref"}

Returns index of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_texture_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**font_get_glyph_texture_rid**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_texture_rid>`{.interpreted-text
role="ref"}

Returns resource ID of the cache texture containing the glyph.

\*\*Note:\*\* If there are pending glyphs to render, calling this
function might trigger the texture cache update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_texture_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**font_get_glyph_texture_size**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_texture_size>`{.interpreted-text
role="ref"}

Returns size of the cache texture containing the glyph.

\*\*Note:\*\* If there are pending glyphs to render, calling this
function might trigger the texture cache update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_glyph_uv_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**font_get_glyph_uv_rect**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_glyph_uv_rect>`{.interpreted-text
role="ref"}

Returns rectangle in the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_hinting}
::: rst-class
classref-method
:::
::::

`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"}
**font_get_hinting**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_hinting>`{.interpreted-text
role="ref"}

Returns the font hinting mode. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_keep_rounding_remainders}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_get_keep_rounding_remainders**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_keep_rounding_remainders>`{.interpreted-text
role="ref"}

Returns glyph position rounding behavior. If set to `true`, when
aligning glyphs to the pixel boundaries rounding remainders are
accumulated to ensure more uniform glyph distribution. This setting has
no effect if subpixel positioning is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_kerning}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**font_get_kerning**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_kerning>`{.interpreted-text
role="ref"}

Returns kerning for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_kerning_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**font_get_kerning_list**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_kerning_list>`{.interpreted-text
role="ref"}

Returns list of the kerning overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_language_support_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_get_language_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_get_language_support_override>`{.interpreted-text
role="ref"}

Returns `true` if support override is enabled for the `language`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_language_support_overrides}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **font_get_language_support_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_get_language_support_overrides>`{.interpreted-text
role="ref"}

Returns list of language support overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_msdf_pixel_range}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_msdf_pixel_range**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_msdf_pixel_range>`{.interpreted-text
role="ref"}

Returns the width of the range around the shape between the minimum and
maximum representable signed distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_msdf_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_msdf_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_msdf_size>`{.interpreted-text
role="ref"}

Returns source font size used to generate MSDF textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**font_get_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_name>`{.interpreted-text
role="ref"}

Returns font family name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_opentype_feature_overrides}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**font_get_opentype_feature_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_opentype_feature_overrides>`{.interpreted-text
role="ref"}

Returns font OpenType feature set override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_ot_name_strings}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**font_get_ot_name_strings**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_ot_name_strings>`{.interpreted-text
role="ref"}

Returns `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
with OpenType font name strings (localized font names, version,
description, license information, sample text, etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_oversampling}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_oversampling**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_oversampling>`{.interpreted-text
role="ref"}

Returns oversampling factor override. If set to a positive value,
overrides the oversampling factor of the viewport this font is used in.
See
`Viewport.oversampling<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"}. This value doesn\'t override the `oversampling` parameter
of `draw_*` methods. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_scale**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_scale>`{.interpreted-text
role="ref"}

Returns scaling factor of the color bitmap font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_script_support_override}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_get_script_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_get_script_support_override>`{.interpreted-text
role="ref"}

Returns `true` if support override is enabled for the `script`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_script_support_overrides}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **font_get_script_support_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_get_script_support_overrides>`{.interpreted-text
role="ref"}

Returns list of script support overrides.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_size_cache_info}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **font_get_size_cache_info**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_size_cache_info>`{.interpreted-text
role="ref"}

Returns font cache information, each entry contains the following
fields: `Vector2i size_px` - font size in pixels,
`float viewport_oversampling` - viewport oversampling factor,
`int glyphs` - number of rendered glyphs, `int textures` - number of
used textures, `int textures_size` - size of texture data in bytes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_size_cache_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**font_get_size_cache_list**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_size_cache_list>`{.interpreted-text
role="ref"}

Returns list of the font sizes in the cache. Each size is
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} with font size
and outline size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_spacing}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_spacing**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_spacing>`{.interpreted-text
role="ref"}

Returns the spacing for `spacing` in pixels (not relative to the font
size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_stretch}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_stretch**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_stretch>`{.interpreted-text
role="ref"}

Returns font stretch amount, compared to a normal width. A percentage
value between `50%` and `200%`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_style}
::: rst-class
classref-method
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
role="ref"}\] **font_get_style**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_style>`{.interpreted-text
role="ref"}

Returns font style flags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_style_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**font_get_style_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_style_name>`{.interpreted-text
role="ref"}

Returns font style name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_subpixel_positioning}
::: rst-class
classref-method
:::
::::

`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"} **font_get_subpixel_positioning**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_subpixel_positioning>`{.interpreted-text
role="ref"}

Returns font subpixel glyph positioning mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_supported_chars}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**font_get_supported_chars**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_supported_chars>`{.interpreted-text
role="ref"}

Returns a string containing all the characters available in the font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_supported_glyphs}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**font_get_supported_glyphs**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_supported_glyphs>`{.interpreted-text
role="ref"}

Returns an array containing all glyph indices in the font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_texture_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_texture_count**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_texture_count>`{.interpreted-text
role="ref"}

Returns number of textures used by font cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_texture_image}
::: rst-class
classref-method
:::
::::

`Image<class_Image>`{.interpreted-text role="ref"}
**font_get_texture_image**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_texture_image>`{.interpreted-text
role="ref"}

Returns font cache texture image data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_texture_offsets}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**font_get_texture_offsets**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, texture_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_texture_offsets>`{.interpreted-text
role="ref"}

Returns array containing glyph packing data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**font_get_transform**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_transform>`{.interpreted-text
role="ref"}

Returns 2D transform applied to the font outlines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_underline_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_underline_position**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_underline_position>`{.interpreted-text
role="ref"}

Returns pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_underline_thickness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**font_get_underline_thickness**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_underline_thickness>`{.interpreted-text
role="ref"}

Returns thickness of the underline in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_variation_coordinates}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**font_get_variation_coordinates**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_variation_coordinates>`{.interpreted-text
role="ref"}

Returns variation coordinates for the specified font cache entry. See
`font_supported_variation_list()<class_TextServer_method_font_supported_variation_list>`{.interpreted-text
role="ref"} for more info.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_get_weight}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**font_get_weight**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_get_weight>`{.interpreted-text
role="ref"}

Returns weight (boldness) of the font. A value in the `100...999` range,
normal font weight is `400`, bold font weight is `700`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_has_char}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_has_char**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, char: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_has_char>`{.interpreted-text
role="ref"}

Returns `true` if a Unicode `char` is available in the font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_is_allow_system_fallback}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_is_allow_system_fallback**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_is_allow_system_fallback>`{.interpreted-text
role="ref"}

Returns `true` if system fonts can be automatically used as fallbacks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_is_force_autohinter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_is_force_autohinter**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_is_force_autohinter>`{.interpreted-text
role="ref"}

Returns `true` if auto-hinting is supported and preferred over font
built-in hinting. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_is_language_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_is_language_supported**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_is_language_supported>`{.interpreted-text
role="ref"}

Returns `true`, if font supports given language ([ISO
639](https://en.wikipedia.org/wiki/ISO_639-1) code).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_is_modulate_color_glyphs}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_is_modulate_color_glyphs**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_is_modulate_color_glyphs>`{.interpreted-text
role="ref"}

Returns `true`, if color modulation is applied when drawing colored
glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_is_multichannel_signed_distance_field}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_is_multichannel_signed_distance_field**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_is_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}

Returns `true` if glyphs of all sizes are rendered using single
multichannel signed distance field generated from the dynamic font
vector data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_is_script_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**font_is_script_supported**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_is_script_supported>`{.interpreted-text
role="ref"}

Returns `true`, if font supports given script (ISO 15924 code).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_remove_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_remove_glyph**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_remove_glyph>`{.interpreted-text
role="ref"}

Removes specified rendered glyph information from the cache entry.

\*\*Note:\*\* This function will not remove textures associated with the
glyphs, use
`font_remove_texture()<class_TextServer_method_font_remove_texture>`{.interpreted-text
role="ref"} to remove them manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_remove_kerning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_remove_kerning**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_remove_kerning>`{.interpreted-text
role="ref"}

Removes kerning override for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_remove_language_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_remove_language_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_remove_language_support_override>`{.interpreted-text
role="ref"}

Remove language support override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_remove_script_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_remove_script_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_remove_script_support_override>`{.interpreted-text
role="ref"}

Removes script support override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_remove_size_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_remove_size_cache**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_remove_size_cache>`{.interpreted-text
role="ref"}

Removes specified font size from the cache entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_remove_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_remove_texture**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_remove_texture>`{.interpreted-text
role="ref"}

Removes specified texture from the cache entry.

\*\*Note:\*\* This function will not remove glyphs associated with the
texture, remove them manually, using
`font_remove_glyph()<class_TextServer_method_font_remove_glyph>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_render_glyph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_render_glyph**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_render_glyph>`{.interpreted-text
role="ref"}

Renders specified glyph to the font cache texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_render_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_render_range**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, start: `int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_render_range>`{.interpreted-text
role="ref"}

Renders the range of characters to the font cache texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_allow_system_fallback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_allow_system_fallback**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, allow_system_fallback:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_allow_system_fallback>`{.interpreted-text
role="ref"}

If set to `true`, system fonts can be automatically used as fallbacks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_antialiasing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_antialiasing**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, antialiasing:
`FontAntialiasing<enum_TextServer_FontAntialiasing>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_antialiasing>`{.interpreted-text
role="ref"}

Sets font anti-aliasing mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_ascent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_ascent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
ascent: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_ascent>`{.interpreted-text
role="ref"}

Sets the font ascent (number of pixels above the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_baseline_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_baseline_offset**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, baseline_offset:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_baseline_offset>`{.interpreted-text
role="ref"}

Sets extra baseline offset (as a fraction of font height).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_data**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, data:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_data>`{.interpreted-text
role="ref"}

Sets font source data, e.g contents of the dynamic font source file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_descent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_descent**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
descent: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_descent>`{.interpreted-text
role="ref"}

Sets the font descent (number of pixels below the baseline).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_disable_embedded_bitmaps}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_disable_embedded_bitmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"},
disable_embedded_bitmaps: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_disable_embedded_bitmaps>`{.interpreted-text
role="ref"}

If set to `true`, embedded font bitmap loading is disabled (bitmap-only
and color fonts ignore this property).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_embolden}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_embolden**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, strength: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_embolden>`{.interpreted-text
role="ref"}

Sets font embolden strength. If `strength` is not equal to zero,
emboldens the font outlines. Negative values reduce the outline
thickness.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_face_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_face_index**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, face_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_face_index>`{.interpreted-text
role="ref"}

Sets an active face index in the TrueType / OpenType collection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_fixed_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_fixed_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, fixed_size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_fixed_size>`{.interpreted-text
role="ref"}

Sets bitmap font fixed size. If set to value greater than zero, same
cache entry will be used for all font sizes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_fixed_size_scale_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_fixed_size_scale_mode**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, fixed_size_scale_mode:
`FixedSizeScaleMode<enum_TextServer_FixedSizeScaleMode>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_fixed_size_scale_mode>`{.interpreted-text
role="ref"}

Sets bitmap font scaling mode. This property is used only if
`fixed_size` is greater than zero.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_force_autohinter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_force_autohinter**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, force_autohinter:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_force_autohinter>`{.interpreted-text
role="ref"}

If set to `true` auto-hinting is preferred over font built-in hinting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_generate_mipmaps}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_generate_mipmaps**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, generate_mipmaps:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_generate_mipmaps>`{.interpreted-text
role="ref"}

If set to `true` font texture mipmap generation is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_global_oversampling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_global_oversampling**(oversampling:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_global_oversampling>`{.interpreted-text
role="ref"}

**Deprecated:** Use `Viewport<class_Viewport>`{.interpreted-text
role="ref"} oversampling, or the `oversampling` argument of the `draw_*`
methods instead.

Deprecated. This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_glyph_advance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_glyph_advance**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph: `int<class_int>`{.interpreted-text role="ref"}, advance:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_glyph_advance>`{.interpreted-text
role="ref"}

Sets glyph advance (offset of the next glyph).

\*\*Note:\*\* Advance for glyphs outlines is the same as the base glyph
advance and is not saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_glyph_offset}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_glyph_offset**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
offset: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_glyph_offset>`{.interpreted-text
role="ref"}

Sets glyph offset from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_glyph_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_glyph_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
gl_size: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_glyph_size>`{.interpreted-text
role="ref"}

Sets size of the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_glyph_texture_idx}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_glyph_texture_idx**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, glyph:
`int<class_int>`{.interpreted-text role="ref"}, texture_idx:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_glyph_texture_idx>`{.interpreted-text
role="ref"}

Sets index of the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_glyph_uv_rect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_glyph_uv_rect**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, glyph: `int<class_int>`{.interpreted-text role="ref"},
uv_rect: `Rect2<class_Rect2>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_glyph_uv_rect>`{.interpreted-text
role="ref"}

Sets rectangle in the cache texture containing the glyph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_hinting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_hinting**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, hinting:
`Hinting<enum_TextServer_Hinting>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_hinting>`{.interpreted-text
role="ref"}

Sets font hinting mode. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_keep_rounding_remainders}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_keep_rounding_remainders**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"},
keep_rounding_remainders: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_keep_rounding_remainders>`{.interpreted-text
role="ref"}

Sets glyph position rounding behavior. If set to `true`, when aligning
glyphs to the pixel boundaries rounding remainders are accumulated to
ensure more uniform glyph distribution. This setting has no effect if
subpixel positioning is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_kerning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_kerning**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
glyph_pair: `Vector2i<class_Vector2i>`{.interpreted-text role="ref"},
kerning: `Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_kerning>`{.interpreted-text
role="ref"}

Sets kerning for the pair of glyphs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_language_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_language_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"}, supported:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_language_support_override>`{.interpreted-text
role="ref"}

Adds override for
`font_is_language_supported()<class_TextServer_method_font_is_language_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_modulate_color_glyphs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_modulate_color_glyphs**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, force_autohinter:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_modulate_color_glyphs>`{.interpreted-text
role="ref"}

If set to `true`, color modulation is applied when drawing colored
glyphs, otherwise it\'s applied to the monochrome glyphs only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_msdf_pixel_range}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_msdf_pixel_range**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, msdf_pixel_range:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_msdf_pixel_range>`{.interpreted-text
role="ref"}

Sets the width of the range around the shape between the minimum and
maximum representable signed distance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_msdf_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_msdf_size**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, msdf_size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_msdf_size>`{.interpreted-text
role="ref"}

Sets source font size used to generate MSDF textures.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_multichannel_signed_distance_field}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_multichannel_signed_distance_field**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, msdf:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_multichannel_signed_distance_field>`{.interpreted-text
role="ref"}

If set to `true`, glyphs of all sizes are rendered using single
multichannel signed distance field generated from the dynamic font
vector data. MSDF rendering allows displaying the font at any scaling
factor without blurriness, and without incurring a CPU cost when the
font size changes (since the font no longer needs to be rasterized on
the CPU). As a downside, font hinting is not available with MSDF. The
lack of font hinting may result in less crisp and less readable fonts at
small sizes.

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

:::: {#class_TextServer_method_font_set_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_name>`{.interpreted-text
role="ref"}

Sets the font family name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_opentype_feature_overrides}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_opentype_feature_overrides**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, overrides:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_opentype_feature_overrides>`{.interpreted-text
role="ref"}

Sets font OpenType feature set override.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_oversampling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_oversampling**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, oversampling: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_oversampling>`{.interpreted-text
role="ref"}

If set to a positive value, overrides the oversampling factor of the
viewport this font is used in. See
`Viewport.oversampling<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"}. This value doesn\'t override the `oversampling` parameter
of `draw_*` methods. Used by dynamic fonts only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_scale}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_scale**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `int<class_int>`{.interpreted-text role="ref"},
scale: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_scale>`{.interpreted-text
role="ref"}

Sets scaling factor of the color bitmap font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_script_support_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_script_support_override**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, script:
`String<class_String>`{.interpreted-text role="ref"}, supported:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_script_support_override>`{.interpreted-text
role="ref"}

Adds override for
`font_is_script_supported()<class_TextServer_method_font_is_script_supported>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_spacing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_spacing**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_spacing>`{.interpreted-text
role="ref"}

Sets the spacing for `spacing` to `value` in pixels (not relative to the
font size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_stretch}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_stretch**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, weight: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_stretch>`{.interpreted-text
role="ref"}

Sets font stretch amount, compared to a normal width. A percentage value
between `50%` and `200%`.

\*\*Note:\*\* This value is used for font matching only and will not
affect font rendering. Use
`font_set_face_index()<class_TextServer_method_font_set_face_index>`{.interpreted-text
role="ref"},
`font_set_variation_coordinates()<class_TextServer_method_font_set_variation_coordinates>`{.interpreted-text
role="ref"}, or
`font_set_transform()<class_TextServer_method_font_set_transform>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_style}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_style**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, style:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`FontStyle<enum_TextServer_FontStyle>`{.interpreted-text
role="ref"}\])
`🔗<class_TextServer_method_font_set_style>`{.interpreted-text
role="ref"}

Sets the font style flags.

\*\*Note:\*\* This value is used for font matching only and will not
affect font rendering. Use
`font_set_face_index()<class_TextServer_method_font_set_face_index>`{.interpreted-text
role="ref"},
`font_set_variation_coordinates()<class_TextServer_method_font_set_variation_coordinates>`{.interpreted-text
role="ref"},
`font_set_embolden()<class_TextServer_method_font_set_embolden>`{.interpreted-text
role="ref"}, or
`font_set_transform()<class_TextServer_method_font_set_transform>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_style_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_style_name**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_style_name>`{.interpreted-text
role="ref"}

Sets the font style name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_subpixel_positioning}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_subpixel_positioning**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, subpixel_positioning:
`SubpixelPositioning<enum_TextServer_SubpixelPositioning>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_subpixel_positioning>`{.interpreted-text
role="ref"}

Sets font subpixel glyph positioning mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_texture_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_texture_image**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, size: `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}, texture_index: `int<class_int>`{.interpreted-text
role="ref"}, image: `Image<class_Image>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_texture_image>`{.interpreted-text
role="ref"}

Sets font cache texture image data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_texture_offsets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_texture_offsets**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, texture_index:
`int<class_int>`{.interpreted-text role="ref"}, offset:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_font_set_texture_offsets>`{.interpreted-text
role="ref"}

Sets array containing glyph packing data.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_transform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_transform**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, transform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_transform>`{.interpreted-text
role="ref"}

Sets 2D transform, applied to the font outlines, can be used for
slanting, flipping, and rotating glyphs.

For example, to simulate italic typeface by slanting, apply the
following transform `Transform2D(1.0, slant, 0.0, 1.0, 0.0, 0.0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_underline_position}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_underline_position**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, underline_position:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_underline_position>`{.interpreted-text
role="ref"}

Sets pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_underline_thickness}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_underline_thickness**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, size:
`int<class_int>`{.interpreted-text role="ref"}, underline_thickness:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_underline_thickness>`{.interpreted-text
role="ref"}

Sets thickness of the underline in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_variation_coordinates}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_variation_coordinates**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"}, variation_coordinates:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_variation_coordinates>`{.interpreted-text
role="ref"}

Sets variation coordinates for the specified font cache entry. See
`font_supported_variation_list()<class_TextServer_method_font_supported_variation_list>`{.interpreted-text
role="ref"} for more info.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_set_weight}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**font_set_weight**(font_rid: `RID<class_RID>`{.interpreted-text
role="ref"}, weight: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_font_set_weight>`{.interpreted-text
role="ref"}

Sets weight (boldness) of the font. A value in the `100...999` range,
normal font weight is `400`, bold font weight is `700`.

\*\*Note:\*\* This value is used for font matching only and will not
affect font rendering. Use
`font_set_face_index()<class_TextServer_method_font_set_face_index>`{.interpreted-text
role="ref"},
`font_set_variation_coordinates()<class_TextServer_method_font_set_variation_coordinates>`{.interpreted-text
role="ref"}, or
`font_set_embolden()<class_TextServer_method_font_set_embolden>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_supported_feature_list}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**font_supported_feature_list**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_supported_feature_list>`{.interpreted-text
role="ref"}

Returns the dictionary of the supported OpenType features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_font_supported_variation_list}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**font_supported_variation_list**(font_rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_font_supported_variation_list>`{.interpreted-text
role="ref"}

Returns the dictionary of the supported OpenType variation coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_format_number}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**format_number**(number: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_format_number>`{.interpreted-text
role="ref"}

Converts a number from the Western Arabic (0..9) to the numeral systems
used in `language`.

If `language` is omitted, the active locale will be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_free_rid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**free_rid**(rid: `RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_free_rid>`{.interpreted-text role="ref"}

Frees an object created by this **TextServer**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_get_features}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_features**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_get_features>`{.interpreted-text role="ref"}

Returns text server features, see
`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_get_hex_code_box_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_hex_code_box_size**(size: `int<class_int>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_get_hex_code_box_size>`{.interpreted-text
role="ref"}

Returns size of the replacement character (box with character
hexadecimal code that is drawn in place of invalid characters).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextServer_method_get_name>`{.interpreted-text
role="ref"}

Returns the name of the server interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_get_support_data}
::: rst-class
classref-method
:::
::::

`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"}
**get_support_data**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_get_support_data>`{.interpreted-text
role="ref"}

Returns default TextServer database (e.g. ICU break iterators and
dictionaries).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_get_support_data_filename}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_support_data_filename**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_get_support_data_filename>`{.interpreted-text
role="ref"}

Returns default TextServer database (e.g. ICU break iterators and
dictionaries) filename.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_get_support_data_info}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_support_data_info**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_get_support_data_info>`{.interpreted-text
role="ref"}

Returns TextServer database (e.g. ICU break iterators and dictionaries)
description.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(rid:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_has>`{.interpreted-text role="ref"}

Returns `true` if `rid` is valid resource owned by this text server.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_has_feature}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_feature**(feature:
`Feature<enum_TextServer_Feature>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextServer_method_has_feature>`{.interpreted-text
role="ref"}

Returns `true` if the server supports a feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_is_confusable}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **is_confusable**(string:
`String<class_String>`{.interpreted-text role="ref"}, dict:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_is_confusable>`{.interpreted-text
role="ref"}

Returns index of the first string in `dict` which is visually confusable
with the `string`, or `-1` if none is found.

\*\*Note:\*\* This method doesn\'t detect invisible characters, for
spoof detection use it in combination with
`spoof_check()<class_TextServer_method_spoof_check>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Always returns `-1` if the server does not support the
`FEATURE_UNICODE_SECURITY<class_TextServer_constant_FEATURE_UNICODE_SECURITY>`{.interpreted-text
role="ref"} feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_is_locale_right_to_left}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_locale_right_to_left**(locale:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_is_locale_right_to_left>`{.interpreted-text
role="ref"}

Returns `true` if locale is right-to-left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_is_valid_identifier}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_identifier**(string: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_is_valid_identifier>`{.interpreted-text
role="ref"}

Returns `true` if `string` is a valid identifier.

If the text server supports the
`FEATURE_UNICODE_IDENTIFIERS<class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS>`{.interpreted-text
role="ref"} feature, a valid identifier must:

- Conform to normalization form C.
- Begin with a Unicode character of class XID_Start or `"_"`.
- May contain Unicode characters of class XID_Continue in the other
  positions.
- Use UAX #31 recommended scripts only (mixed scripts are allowed).

If the
`FEATURE_UNICODE_IDENTIFIERS<class_TextServer_constant_FEATURE_UNICODE_IDENTIFIERS>`{.interpreted-text
role="ref"} feature is not supported, a valid identifier must:

- Begin with a Unicode character of class XID_Start or `"_"`.
- May contain Unicode characters of class XID_Continue in the other
  positions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_is_valid_letter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_valid_letter**(unicode: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_is_valid_letter>`{.interpreted-text
role="ref"}

Returns `true` if the given code point is a valid letter, i.e. it
belongs to the Unicode category \"L\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_load_support_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**load_support_data**(filename: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_load_support_data>`{.interpreted-text
role="ref"}

Loads optional TextServer database (e.g. ICU break iterators and
dictionaries).

\*\*Note:\*\* This function should be called before any other TextServer
functions used, otherwise it won\'t have any effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_name_to_tag}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **name_to_tag**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextServer_method_name_to_tag>`{.interpreted-text
role="ref"}

Converts readable feature, variation, script, or language name to
OpenType tag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_parse_number}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**parse_number**(number: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_parse_number>`{.interpreted-text role="ref"}

Converts `number` from the numeral systems used in `language` to Western
Arabic (0..9).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_parse_structured_text}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector3i<class_Vector3i>`{.interpreted-text role="ref"}\]
**parse_structured_text**(parser_type:
`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"}, args: `Array<class_Array>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_parse_structured_text>`{.interpreted-text
role="ref"}

Default implementation of the BiDi algorithm override function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_percent_sign}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**percent_sign**(language: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_percent_sign>`{.interpreted-text role="ref"}

Returns percent sign used in the `language`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_save_support_data}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**save_support_data**(filename: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_save_support_data>`{.interpreted-text
role="ref"}

Saves optional TextServer database (e.g. ICU break iterators and
dictionaries) to the file.

\*\*Note:\*\* This function is used by during project export, to include
TextServer database.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_get_run_count**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_count>`{.interpreted-text
role="ref"}

Returns the number of uniform text runs in the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_direction}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**shaped_get_run_direction**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_direction>`{.interpreted-text
role="ref"}

Returns the direction of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_font_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**shaped_get_run_font_rid**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_font_rid>`{.interpreted-text
role="ref"}

Returns the font RID of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_font_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_get_run_font_size**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_font_size>`{.interpreted-text
role="ref"}

Returns the font size of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_language}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**shaped_get_run_language**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_language>`{.interpreted-text
role="ref"}

Returns the language of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_object}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**shaped_get_run_object**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_object>`{.interpreted-text
role="ref"}

Returns the embedded object of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_range}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**shaped_get_run_range**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_range>`{.interpreted-text
role="ref"}

Returns the source text range of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_run_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**shaped_get_run_text**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_run_text>`{.interpreted-text
role="ref"}

Returns the source text of the `index` text run (in visual order).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_span_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_get_span_count**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_span_count>`{.interpreted-text
role="ref"}

Returns number of text spans added using
`shaped_text_add_string()<class_TextServer_method_shaped_text_add_string>`{.interpreted-text
role="ref"} or
`shaped_text_add_object()<class_TextServer_method_shaped_text_add_object>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_span_embedded_object}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**shaped_get_span_embedded_object**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_span_embedded_object>`{.interpreted-text
role="ref"}

Returns text embedded object key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_span_meta}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**shaped_get_span_meta**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_span_meta>`{.interpreted-text
role="ref"}

Returns text span metadata.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_span_object}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**shaped_get_span_object**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_span_object>`{.interpreted-text
role="ref"}

Returns the text span embedded object key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_span_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**shaped_get_span_text**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, index: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_span_text>`{.interpreted-text
role="ref"}

Returns the text span source text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_get_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**shaped_get_text**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_get_text>`{.interpreted-text
role="ref"}

Returns the text buffer source text, including object replacement
characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_set_span_update_font}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_set_span_update_font**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, index:
`int<class_int>`{.interpreted-text role="ref"}, fonts:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\], size:
`int<class_int>`{.interpreted-text role="ref"}, opentype_features:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} = {})
`🔗<class_TextServer_method_shaped_set_span_update_font>`{.interpreted-text
role="ref"}

Changes text span font, font size, and OpenType features, without
changing the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_add_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_add_object**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, key: `Variant<class_Variant>`{.interpreted-text
role="ref"}, size: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} = 5, length: `int<class_int>`{.interpreted-text role="ref"}
= 1, baseline: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`🔗<class_TextServer_method_shaped_text_add_object>`{.interpreted-text
role="ref"}

Adds inline object to the text buffer, `key` must be unique. In the
text, object is represented as `length` object replacement characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_add_string}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_add_string**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, text: `String<class_String>`{.interpreted-text role="ref"},
fonts: `Array<class_Array>`{.interpreted-text
role="ref"}\[`RID<class_RID>`{.interpreted-text role="ref"}\], size:
`int<class_int>`{.interpreted-text role="ref"}, opentype_features:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} = {},
language: `String<class_String>`{.interpreted-text role="ref"} = \"\",
meta: `Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`🔗<class_TextServer_method_shaped_text_add_string>`{.interpreted-text
role="ref"}

Adds text span and font to draw it to the text buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_clear**(rid: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_shaped_text_clear>`{.interpreted-text
role="ref"}

Clears text buffer (removes text and inline objects).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_closest_character_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_closest_character_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_closest_character_pos>`{.interpreted-text
role="ref"}

Returns composite character position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_draw**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"},
pos: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, clip_l:
`float<class_float>`{.interpreted-text role="ref"} = -1, clip_r:
`float<class_float>`{.interpreted-text role="ref"} = -1, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_draw>`{.interpreted-text
role="ref"}

Draw shaped text into a canvas item at a given position, with `color`.
`pos` specifies the leftmost point of the baseline (for horizontal
layout) or topmost point of the baseline (for vertical layout). If
`oversampling` is greater than zero, it is used as font oversampling
factor, otherwise viewport oversampling settings are used.

`clip_l` and `clip_r` are offsets relative to `pos`, going to the right
in horizontal layout and downward in vertical layout. If `clip_l` is not
negative, glyphs starting before the offset are clipped. If `clip_r` is
not negative, glyphs ending after the offset are clipped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_draw_outline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_draw_outline**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, canvas: `RID<class_RID>`{.interpreted-text role="ref"},
pos: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, clip_l:
`float<class_float>`{.interpreted-text role="ref"} = -1, clip_r:
`float<class_float>`{.interpreted-text role="ref"} = -1, outline_size:
`int<class_int>`{.interpreted-text role="ref"} = 1, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
oversampling: `float<class_float>`{.interpreted-text role="ref"} = 0.0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_draw_outline>`{.interpreted-text
role="ref"}

Draw the outline of the shaped text into a canvas item at a given
position, with `color`. `pos` specifies the leftmost point of the
baseline (for horizontal layout) or topmost point of the baseline (for
vertical layout). If `oversampling` is greater than zero, it is used as
font oversampling factor, otherwise viewport oversampling settings are
used.

`clip_l` and `clip_r` are offsets relative to `pos`, going to the right
in horizontal layout and downward in vertical layout. If `clip_l` is not
negative, glyphs starting before the offset are clipped. If `clip_r` is
not negative, glyphs ending after the offset are clipped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_fit_to_width}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shaped_text_fit_to_width**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, width: `float<class_float>`{.interpreted-text role="ref"},
justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 3)
`🔗<class_TextServer_method_shaped_text_fit_to_width>`{.interpreted-text
role="ref"}

Adjusts text width to fit to specified width, returns new text width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_ascent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shaped_text_get_ascent**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_ascent>`{.interpreted-text
role="ref"}

Returns the text ascent (number of pixels above the baseline for
horizontal layout or to the left of baseline for vertical).

\*\*Note:\*\* Overall ascent can be higher than font ascent, if some
glyphs are displaced from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_carets}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**shaped_text_get_carets**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, position: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_carets>`{.interpreted-text
role="ref"}

Returns shapes of the carets corresponding to the character offset
`position` in the text. Returned caret shape is 1 pixel wide rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_character_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**shaped_text_get_character_breaks**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_character_breaks>`{.interpreted-text
role="ref"}

Returns array of the composite character boundaries.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_custom_ellipsis}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_get_custom_ellipsis**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_custom_ellipsis>`{.interpreted-text
role="ref"}

Returns ellipsis character used for text clipping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_custom_punctuation}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**shaped_text_get_custom_punctuation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_custom_punctuation>`{.interpreted-text
role="ref"}

Returns custom punctuation character list, used for word breaking. If
set to empty string, server defaults are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_descent}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shaped_text_get_descent**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_descent>`{.interpreted-text
role="ref"}

Returns the text descent (number of pixels below the baseline for
horizontal layout or to the right of baseline for vertical).

\*\*Note:\*\* Overall descent can be higher than font descent, if some
glyphs are displaced from the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_direction}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**shaped_text_get_direction**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_direction>`{.interpreted-text
role="ref"}

Returns direction of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_dominant_direction_in_range}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**shaped_text_get_dominant_direction_in_range**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, start:
`int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_dominant_direction_in_range>`{.interpreted-text
role="ref"}

Returns dominant direction of in the range of text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_ellipsis_glyph_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_get_ellipsis_glyph_count**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_ellipsis_glyph_count>`{.interpreted-text
role="ref"}

Returns number of glyphs in the ellipsis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_ellipsis_glyphs}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **shaped_text_get_ellipsis_glyphs**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_ellipsis_glyphs>`{.interpreted-text
role="ref"}

Returns array of the glyphs in the ellipsis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_ellipsis_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_get_ellipsis_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_ellipsis_pos>`{.interpreted-text
role="ref"}

Returns position of the ellipsis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_glyph_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_get_glyph_count**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_glyph_count>`{.interpreted-text
role="ref"}

Returns number of glyphs in the buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_glyphs}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **shaped_text_get_glyphs**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_glyphs>`{.interpreted-text
role="ref"}

Returns an array of glyphs in the visual order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_grapheme_bounds}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**shaped_text_get_grapheme_bounds**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_grapheme_bounds>`{.interpreted-text
role="ref"}

Returns composite character\'s bounds as offsets from the start of the
line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_inferred_direction}
::: rst-class
classref-method
:::
::::

`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"}
**shaped_text_get_inferred_direction**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_inferred_direction>`{.interpreted-text
role="ref"}

Returns direction of the text, inferred by the BiDi algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_line_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**shaped_text_get_line_breaks**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"}, start:
`int<class_int>`{.interpreted-text role="ref"} = 0, break_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] = 3)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_line_breaks>`{.interpreted-text
role="ref"}

Breaks text to the lines and returns character ranges for each line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_line_breaks_adv}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**shaped_text_get_line_breaks_adv**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"}, start: `int<class_int>`{.interpreted-text role="ref"} = 0,
once: `bool<class_bool>`{.interpreted-text role="ref"} = true,
break_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] = 3)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_line_breaks_adv>`{.interpreted-text
role="ref"}

Breaks text to the lines and columns. Returns character ranges for each
segment.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_object_glyph}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_get_object_glyph**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_object_glyph>`{.interpreted-text
role="ref"}

Returns the glyph index of the inline object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_object_range}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**shaped_text_get_object_range**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_object_range>`{.interpreted-text
role="ref"}

Returns the character range of the inline object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_object_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**shaped_text_get_object_rect**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, key:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_object_rect>`{.interpreted-text
role="ref"}

Returns bounding rectangle of the inline object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_objects}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**shaped_text_get_objects**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_objects>`{.interpreted-text
role="ref"}

Returns array of inline objects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_orientation}
::: rst-class
classref-method
:::
::::

`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
**shaped_text_get_orientation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_orientation>`{.interpreted-text
role="ref"}

Returns text orientation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_parent}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**shaped_text_get_parent**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_parent>`{.interpreted-text
role="ref"}

Returns the parent buffer from which the substring originates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_preserve_control}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_get_preserve_control**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_preserve_control>`{.interpreted-text
role="ref"}

Returns `true` if text buffer is configured to display control
characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_preserve_invalid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_get_preserve_invalid**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_preserve_invalid>`{.interpreted-text
role="ref"}

Returns `true` if text buffer is configured to display hexadecimal codes
in place of invalid characters.

\*\*Note:\*\* If set to `false`, nothing is displayed in place of
invalid characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_range}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**shaped_text_get_range**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_range>`{.interpreted-text
role="ref"}

Returns substring buffer character range in the parent buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_selection}
::: rst-class
classref-method
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **shaped_text_get_selection**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, start:
`int<class_int>`{.interpreted-text role="ref"}, end:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_selection>`{.interpreted-text
role="ref"}

Returns selection rectangles for the specified character range.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_size}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**shaped_text_get_size**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_size>`{.interpreted-text
role="ref"}

Returns size of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_spacing}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_get_spacing**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_spacing>`{.interpreted-text
role="ref"}

Returns extra spacing added between glyphs or lines in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_trim_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_get_trim_pos**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_trim_pos>`{.interpreted-text
role="ref"}

Returns the position of the overrun trim.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_underline_position}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shaped_text_get_underline_position**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_underline_position>`{.interpreted-text
role="ref"}

Returns pixel offset of the underline below the baseline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_underline_thickness}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shaped_text_get_underline_thickness**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_underline_thickness>`{.interpreted-text
role="ref"}

Returns thickness of the underline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_width}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shaped_text_get_width**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_width>`{.interpreted-text
role="ref"}

Returns width (for horizontal layout) or height (for vertical) of the
text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_get_word_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**shaped_text_get_word_breaks**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, grapheme_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"}\] = 264, skip_grapheme_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`GraphemeFlag<enum_TextServer_GraphemeFlag>`{.interpreted-text
role="ref"}\] = 4)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_get_word_breaks>`{.interpreted-text
role="ref"}

Breaks text into words and returns array of character ranges. Use
`grapheme_flags` to set what characters are used for breaking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_has_visible_chars}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_has_visible_chars**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_has_visible_chars>`{.interpreted-text
role="ref"}

Returns `true` if text buffer contains any visible characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_hit_test_grapheme}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_hit_test_grapheme**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, coords:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_hit_test_grapheme>`{.interpreted-text
role="ref"}

Returns grapheme index at the specified pixel offset at the baseline, or
`-1` if none is found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_hit_test_position}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_hit_test_position**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, coords:
`float<class_float>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_hit_test_position>`{.interpreted-text
role="ref"}

Returns caret character offset at the specified pixel offset at the
baseline. This function always returns a valid position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_is_ready}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_is_ready**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_is_ready>`{.interpreted-text
role="ref"}

Returns `true` if buffer is successfully shaped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_next_character_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_next_character_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_next_character_pos>`{.interpreted-text
role="ref"}

Returns composite character end position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_next_grapheme_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_next_grapheme_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_next_grapheme_pos>`{.interpreted-text
role="ref"}

Returns grapheme end position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_overrun_trim_to_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_overrun_trim_to_width**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, width:
`float<class_float>`{.interpreted-text role="ref"} = 0,
overrun_trim_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`TextOverrunFlag<enum_TextServer_TextOverrunFlag>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_TextServer_method_shaped_text_overrun_trim_to_width>`{.interpreted-text
role="ref"}

Trims text if it exceeds the given width.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_prev_character_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_prev_character_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_prev_character_pos>`{.interpreted-text
role="ref"}

Returns composite character start position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_prev_grapheme_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**shaped_text_prev_grapheme_pos**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, pos:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_prev_grapheme_pos>`{.interpreted-text
role="ref"}

Returns grapheme start position closest to the `pos`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_resize_object}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_resize_object**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, key: `Variant<class_Variant>`{.interpreted-text
role="ref"}, size: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}, inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} = 5, baseline: `float<class_float>`{.interpreted-text
role="ref"} = 0.0)
`🔗<class_TextServer_method_shaped_text_resize_object>`{.interpreted-text
role="ref"}

Sets new size and alignment of embedded object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_bidi_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_bidi_override**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, override:
`Array<class_Array>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_shaped_text_set_bidi_override>`{.interpreted-text
role="ref"}

Overrides BiDi for the structured text.

Override ranges should cover full source text without overlaps. BiDi
algorithm will be used on each range separately.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_custom_ellipsis}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_custom_ellipsis**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, char:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_shaped_text_set_custom_ellipsis>`{.interpreted-text
role="ref"}

Sets ellipsis character used for text clipping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_custom_punctuation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_custom_punctuation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, punct:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_shaped_text_set_custom_punctuation>`{.interpreted-text
role="ref"}

Sets custom punctuation character list, used for word breaking. If set
to empty string, server defaults are used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_direction}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_direction**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, direction:
`Direction<enum_TextServer_Direction>`{.interpreted-text role="ref"} =
0)
`🔗<class_TextServer_method_shaped_text_set_direction>`{.interpreted-text
role="ref"}

Sets desired text direction. If set to
`DIRECTION_AUTO<class_TextServer_constant_DIRECTION_AUTO>`{.interpreted-text
role="ref"}, direction will be detected based on the buffer contents and
current locale.

\*\*Note:\*\* Direction is ignored if server does not support
`FEATURE_BIDI_LAYOUT<class_TextServer_constant_FEATURE_BIDI_LAYOUT>`{.interpreted-text
role="ref"} feature (supported by
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_orientation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_orientation**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, orientation:
`Orientation<enum_TextServer_Orientation>`{.interpreted-text role="ref"}
= 0)
`🔗<class_TextServer_method_shaped_text_set_orientation>`{.interpreted-text
role="ref"}

Sets desired text orientation.

\*\*Note:\*\* Orientation is ignored if server does not support
`FEATURE_VERTICAL_LAYOUT<class_TextServer_constant_FEATURE_VERTICAL_LAYOUT>`{.interpreted-text
role="ref"} feature (supported by
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_preserve_control}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_preserve_control**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_shaped_text_set_preserve_control>`{.interpreted-text
role="ref"}

If set to `true` text buffer will display control characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_preserve_invalid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_preserve_invalid**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"}, enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_shaped_text_set_preserve_invalid>`{.interpreted-text
role="ref"}

If set to `true` text buffer will display invalid characters as
hexadecimal codes, otherwise nothing is displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_set_spacing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**shaped_text_set_spacing**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, spacing:
`SpacingType<enum_TextServer_SpacingType>`{.interpreted-text
role="ref"}, value: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_shaped_text_set_spacing>`{.interpreted-text
role="ref"}

Sets extra spacing added between glyphs or lines in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_shape}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shaped_text_shape**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_shaped_text_shape>`{.interpreted-text
role="ref"}

Shapes buffer if it\'s not shaped. Returns `true` if the string is
shaped successfully.

\*\*Note:\*\* It is not necessary to call this function manually, buffer
will be shaped automatically as soon as any of its output data is
requested.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_sort_logical}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **shaped_text_sort_logical**(shaped:
`RID<class_RID>`{.interpreted-text role="ref"})
`🔗<class_TextServer_method_shaped_text_sort_logical>`{.interpreted-text
role="ref"}

Returns text glyphs in the logical order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_substr}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**shaped_text_substr**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, start: `int<class_int>`{.interpreted-text role="ref"},
length: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_shaped_text_substr>`{.interpreted-text
role="ref"}

Returns text buffer for the substring of the text in the `shaped` text
buffer (including inline objects).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_shaped_text_tab_align}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**shaped_text_tab_align**(shaped: `RID<class_RID>`{.interpreted-text
role="ref"}, tab_stops:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"})
`🔗<class_TextServer_method_shaped_text_tab_align>`{.interpreted-text
role="ref"}

Aligns shaped text to the given tab-stops.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_spoof_check}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **spoof_check**(string:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextServer_method_spoof_check>`{.interpreted-text
role="ref"}

Returns `true` if `string` is likely to be an attempt at confusing the
reader.

\*\*Note:\*\* Always returns `false` if the server does not support the
`FEATURE_UNICODE_SECURITY<class_TextServer_constant_FEATURE_UNICODE_SECURITY>`{.interpreted-text
role="ref"} feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_string_get_character_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**string_get_character_breaks**(string:
`String<class_String>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_string_get_character_breaks>`{.interpreted-text
role="ref"}

Returns array of the composite character boundaries.

    var ts = TextServerManager.get_primary_interface()
    print(ts.string_get_character_breaks("Test ❤️‍🔥 Test")) # Prints [1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14]

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_string_get_word_breaks}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**string_get_word_breaks**(string:
`String<class_String>`{.interpreted-text role="ref"}, language:
`String<class_String>`{.interpreted-text role="ref"} = \"\",
chars_per_line: `int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_string_get_word_breaks>`{.interpreted-text
role="ref"}

Returns an array of the word break boundaries. Elements in the returned
array are the offsets of the start and end of words. Therefore the
length of the array is always even.

When `chars_per_line` is greater than zero, line break boundaries are
returned instead.

    var ts = TextServerManager.get_primary_interface()
    # Corresponds to the substrings "The", "Godot", "Engine", and "4".
    print(ts.string_get_word_breaks("The Godot Engine, 4")) # Prints [0, 3, 4, 9, 10, 16, 18, 19]
    # Corresponds to the substrings "The", "Godot", "Engin", and "e, 4".
    print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 5)) # Prints [0, 3, 4, 9, 10, 15, 15, 19]
    # Corresponds to the substrings "The Godot" and "Engine, 4".
    print(ts.string_get_word_breaks("The Godot Engine, 4", "en", 10)) # Prints [0, 9, 10, 19]

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_string_to_lower}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**string_to_lower**(string: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_string_to_lower>`{.interpreted-text
role="ref"}

Returns the string converted to lowercase.

\*\*Note:\*\* Casing is locale dependent and context sensitive if server
support
`FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION<class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION>`{.interpreted-text
role="ref"} feature (supported by
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* The result may be longer or shorter than the original.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_string_to_title}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**string_to_title**(string: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_string_to_title>`{.interpreted-text
role="ref"}

Returns the string converted to title case.

\*\*Note:\*\* Casing is locale dependent and context sensitive if server
support
`FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION<class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION>`{.interpreted-text
role="ref"} feature (supported by
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* The result may be longer or shorter than the original.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_string_to_upper}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**string_to_upper**(string: `String<class_String>`{.interpreted-text
role="ref"}, language: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_string_to_upper>`{.interpreted-text
role="ref"}

Returns the string converted to uppercase.

\*\*Note:\*\* Casing is locale dependent and context sensitive if server
support
`FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION<class_TextServer_constant_FEATURE_CONTEXT_SENSITIVE_CASE_CONVERSION>`{.interpreted-text
role="ref"} feature (supported by
`TextServerAdvanced<class_TextServerAdvanced>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* The result may be longer or shorter than the original.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_strip_diacritics}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**strip_diacritics**(string: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextServer_method_strip_diacritics>`{.interpreted-text
role="ref"}

Strips diacritics from the string.

\*\*Note:\*\* The result may be longer or shorter than the original.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextServer_method_tag_to_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**tag_to_name**(tag: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextServer_method_tag_to_name>`{.interpreted-text
role="ref"}

Converts OpenType tag to readable feature, variation, script, or
language name.
