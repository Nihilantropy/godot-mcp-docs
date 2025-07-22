github_url
:   hide

::: {.meta keywords="textarea"}
:::

# TextEdit {#class_TextEdit}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `CodeEdit<class_CodeEdit>`{.interpreted-text
role="ref"}

A multiline text editor.

::: rst-class
classref-introduction-group
:::

## Description

A multiline text editor. It also has limited facilities for editing
code, such as syntax highlighting support. For more advanced facilities
for editing code, see `CodeEdit<class_CodeEdit>`{.interpreted-text
role="ref"}.

While entering text, it is possible to insert special characters using
Unicode, OEM or Windows alt codes:

- To enter Unicode codepoints, hold `Alt`{.interpreted-text role="kbd"}
  and type the codepoint on the numpad. For example, to enter the
  character `á` (U+00E1), hold `Alt`{.interpreted-text role="kbd"} and
  type `+E1`{.interpreted-text role="kbd"} on the numpad (the leading
  zeroes can be omitted).
- To enter OEM codepoints, hold `Alt`{.interpreted-text role="kbd"} and
  type the code on the numpad. For example, to enter the character `á`
  (OEM 160), hold `Alt`{.interpreted-text role="kbd"} and type `160` on
  the numpad.
- To enter Windows codepoints, hold `Alt`{.interpreted-text role="kbd"}
  and type the code on the numpad. For example, to enter the character
  `á` (Windows 0225), hold `Alt`{.interpreted-text role="kbd"} and type
  `0`{.interpreted-text role="kbd"}, `2`{.interpreted-text role="kbd"},
  `2`{.interpreted-text role="kbd"}, `5`{.interpreted-text role="kbd"}
  on the numpad. The leading zero here must **not** be omitted, as this
  is how Windows codepoints are distinguished from OEM codepoints.

\*\*Note:\*\* Most viewport, caret, and edit methods contain a
`caret_index` argument for
`caret_multiple<class_TextEdit_property_caret_multiple>`{.interpreted-text
role="ref"} support. The argument should be one of the following: `-1`
for all carets, `0` for the main caret, or greater than `0` for
secondary carets in the order they were created.

\*\*Note:\*\* When holding down `Alt`{.interpreted-text role="kbd"}, the
vertical scroll wheel will scroll 5 times as fast as it would normally
do. This also works in the Godot script editor.

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-reftable-group
:::

## Methods

::: rst-class
classref-reftable-group
:::

## Theme Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_TextEdit_signal_caret_changed}
::: rst-class
classref-signal
:::
::::

**caret_changed**()
`🔗<class_TextEdit_signal_caret_changed>`{.interpreted-text role="ref"}

Emitted when any caret changes position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_signal_gutter_added}
::: rst-class
classref-signal
:::
::::

**gutter_added**()
`🔗<class_TextEdit_signal_gutter_added>`{.interpreted-text role="ref"}

Emitted when a gutter is added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_signal_gutter_clicked}
::: rst-class
classref-signal
:::
::::

**gutter_clicked**(line: `int<class_int>`{.interpreted-text role="ref"},
gutter: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_signal_gutter_clicked>`{.interpreted-text role="ref"}

Emitted when a gutter is clicked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_signal_gutter_removed}
::: rst-class
classref-signal
:::
::::

**gutter_removed**()
`🔗<class_TextEdit_signal_gutter_removed>`{.interpreted-text role="ref"}

Emitted when a gutter is removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_signal_lines_edited_from}
::: rst-class
classref-signal
:::
::::

**lines_edited_from**(from_line: `int<class_int>`{.interpreted-text
role="ref"}, to_line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_signal_lines_edited_from>`{.interpreted-text
role="ref"}

Emitted immediately when the text changes.

When text is added `from_line` will be less than `to_line`. On a remove
`to_line` will be less than `from_line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_signal_text_changed}
::: rst-class
classref-signal
:::
::::

**text_changed**()
`🔗<class_TextEdit_signal_text_changed>`{.interpreted-text role="ref"}

Emitted when the text changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_signal_text_set}
::: rst-class
classref-signal
:::
::::

**text_set**() `🔗<class_TextEdit_signal_text_set>`{.interpreted-text
role="ref"}

Emitted when `clear()<class_TextEdit_method_clear>`{.interpreted-text
role="ref"} is called or
`text<class_TextEdit_property_text>`{.interpreted-text role="ref"} is
set.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_TextEdit_MenuItems}
::: rst-class
classref-enumeration
:::
::::

enum **MenuItems**: `🔗<enum_TextEdit_MenuItems>`{.interpreted-text
role="ref"}

:::: {#class_TextEdit_constant_MENU_CUT}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

:::: {#class_TextEdit_constant_MENU_COPY}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_COPY** = `1`

Copies the selected text.

:::: {#class_TextEdit_constant_MENU_PASTE}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the cursor\'s
position).

:::: {#class_TextEdit_constant_MENU_CLEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_CLEAR** = `3`

Erases the whole **TextEdit** text.

:::: {#class_TextEdit_constant_MENU_SELECT_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_SELECT_ALL** = `4`

Selects the whole **TextEdit** text.

:::: {#class_TextEdit_constant_MENU_UNDO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_UNDO** = `5`

Undoes the previous action.

:::: {#class_TextEdit_constant_MENU_REDO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_REDO** = `6`

Redoes the previous action.

:::: {#class_TextEdit_constant_MENU_SUBMENU_TEXT_DIR}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_SUBMENU_TEXT_DIR** = `7`

ID of \"Text Writing Direction\" submenu.

:::: {#class_TextEdit_constant_MENU_DIR_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

:::: {#class_TextEdit_constant_MENU_DIR_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

:::: {#class_TextEdit_constant_MENU_DIR_LTR}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

:::: {#class_TextEdit_constant_MENU_DIR_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

:::: {#class_TextEdit_constant_MENU_DISPLAY_UCC}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DISPLAY_UCC** = `12`

Toggles control character display.

:::: {#class_TextEdit_constant_MENU_SUBMENU_INSERT_UCC}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_SUBMENU_INSERT_UCC** = `13`

ID of \"Insert Control Character\" submenu.

:::: {#class_TextEdit_constant_MENU_INSERT_LRM}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

:::: {#class_TextEdit_constant_MENU_INSERT_RLM}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

:::: {#class_TextEdit_constant_MENU_INSERT_LRE}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

:::: {#class_TextEdit_constant_MENU_INSERT_RLE}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

:::: {#class_TextEdit_constant_MENU_INSERT_LRO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

:::: {#class_TextEdit_constant_MENU_INSERT_RLO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

:::: {#class_TextEdit_constant_MENU_INSERT_PDF}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

:::: {#class_TextEdit_constant_MENU_INSERT_ALM}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

:::: {#class_TextEdit_constant_MENU_INSERT_LRI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

:::: {#class_TextEdit_constant_MENU_INSERT_RLI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

:::: {#class_TextEdit_constant_MENU_INSERT_FSI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

:::: {#class_TextEdit_constant_MENU_INSERT_PDI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

:::: {#class_TextEdit_constant_MENU_INSERT_ZWJ}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

:::: {#class_TextEdit_constant_MENU_INSERT_ZWNJ}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

:::: {#class_TextEdit_constant_MENU_INSERT_WJ}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

:::: {#class_TextEdit_constant_MENU_INSERT_SHY}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

:::: {#class_TextEdit_constant_MENU_EMOJI_AND_SYMBOL}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

:::: {#class_TextEdit_constant_MENU_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_MAX** = `31`

Represents the size of the
`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextEdit_EditAction}
::: rst-class
classref-enumeration
:::
::::

enum **EditAction**: `🔗<enum_TextEdit_EditAction>`{.interpreted-text
role="ref"}

:::: {#class_TextEdit_constant_ACTION_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`EditAction<enum_TextEdit_EditAction>`{.interpreted-text role="ref"}
**ACTION_NONE** = `0`

No current action.

:::: {#class_TextEdit_constant_ACTION_TYPING}
::: rst-class
classref-enumeration-constant
:::
::::

`EditAction<enum_TextEdit_EditAction>`{.interpreted-text role="ref"}
**ACTION_TYPING** = `1`

A typing action.

:::: {#class_TextEdit_constant_ACTION_BACKSPACE}
::: rst-class
classref-enumeration-constant
:::
::::

`EditAction<enum_TextEdit_EditAction>`{.interpreted-text role="ref"}
**ACTION_BACKSPACE** = `2`

A backwards delete action.

:::: {#class_TextEdit_constant_ACTION_DELETE}
::: rst-class
classref-enumeration-constant
:::
::::

`EditAction<enum_TextEdit_EditAction>`{.interpreted-text role="ref"}
**ACTION_DELETE** = `3`

A forward delete action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextEdit_SearchFlags}
::: rst-class
classref-enumeration
:::
::::

enum **SearchFlags**: `🔗<enum_TextEdit_SearchFlags>`{.interpreted-text
role="ref"}

:::: {#class_TextEdit_constant_SEARCH_MATCH_CASE}
::: rst-class
classref-enumeration-constant
:::
::::

`SearchFlags<enum_TextEdit_SearchFlags>`{.interpreted-text role="ref"}
**SEARCH_MATCH_CASE** = `1`

Match case when searching.

:::: {#class_TextEdit_constant_SEARCH_WHOLE_WORDS}
::: rst-class
classref-enumeration-constant
:::
::::

`SearchFlags<enum_TextEdit_SearchFlags>`{.interpreted-text role="ref"}
**SEARCH_WHOLE_WORDS** = `2`

Match whole words when searching.

:::: {#class_TextEdit_constant_SEARCH_BACKWARDS}
::: rst-class
classref-enumeration-constant
:::
::::

`SearchFlags<enum_TextEdit_SearchFlags>`{.interpreted-text role="ref"}
**SEARCH_BACKWARDS** = `4`

Search from end to beginning.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextEdit_CaretType}
::: rst-class
classref-enumeration
:::
::::

enum **CaretType**: `🔗<enum_TextEdit_CaretType>`{.interpreted-text
role="ref"}

:::: {#class_TextEdit_constant_CARET_TYPE_LINE}
::: rst-class
classref-enumeration-constant
:::
::::

`CaretType<enum_TextEdit_CaretType>`{.interpreted-text role="ref"}
**CARET_TYPE_LINE** = `0`

Vertical line caret.

:::: {#class_TextEdit_constant_CARET_TYPE_BLOCK}
::: rst-class
classref-enumeration-constant
:::
::::

`CaretType<enum_TextEdit_CaretType>`{.interpreted-text role="ref"}
**CARET_TYPE_BLOCK** = `1`

Block caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextEdit_SelectionMode}
::: rst-class
classref-enumeration
:::
::::

enum **SelectionMode**:
`🔗<enum_TextEdit_SelectionMode>`{.interpreted-text role="ref"}

:::: {#class_TextEdit_constant_SELECTION_MODE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectionMode<enum_TextEdit_SelectionMode>`{.interpreted-text
role="ref"} **SELECTION_MODE_NONE** = `0`

Not selecting.

:::: {#class_TextEdit_constant_SELECTION_MODE_SHIFT}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectionMode<enum_TextEdit_SelectionMode>`{.interpreted-text
role="ref"} **SELECTION_MODE_SHIFT** = `1`

Select as if `shift` is pressed.

:::: {#class_TextEdit_constant_SELECTION_MODE_POINTER}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectionMode<enum_TextEdit_SelectionMode>`{.interpreted-text
role="ref"} **SELECTION_MODE_POINTER** = `2`

Select single characters as if the user single clicked.

:::: {#class_TextEdit_constant_SELECTION_MODE_WORD}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectionMode<enum_TextEdit_SelectionMode>`{.interpreted-text
role="ref"} **SELECTION_MODE_WORD** = `3`

Select whole words as if the user double clicked.

:::: {#class_TextEdit_constant_SELECTION_MODE_LINE}
::: rst-class
classref-enumeration-constant
:::
::::

`SelectionMode<enum_TextEdit_SelectionMode>`{.interpreted-text
role="ref"} **SELECTION_MODE_LINE** = `4`

Select whole lines as if the user triple clicked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextEdit_LineWrappingMode}
::: rst-class
classref-enumeration
:::
::::

enum **LineWrappingMode**:
`🔗<enum_TextEdit_LineWrappingMode>`{.interpreted-text role="ref"}

:::: {#class_TextEdit_constant_LINE_WRAPPING_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`LineWrappingMode<enum_TextEdit_LineWrappingMode>`{.interpreted-text
role="ref"} **LINE_WRAPPING_NONE** = `0`

Line wrapping is disabled.

:::: {#class_TextEdit_constant_LINE_WRAPPING_BOUNDARY}
::: rst-class
classref-enumeration-constant
:::
::::

`LineWrappingMode<enum_TextEdit_LineWrappingMode>`{.interpreted-text
role="ref"} **LINE_WRAPPING_BOUNDARY** = `1`

Line wrapping occurs at the control boundary, beyond what would normally
be visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_TextEdit_GutterType}
::: rst-class
classref-enumeration
:::
::::

enum **GutterType**: `🔗<enum_TextEdit_GutterType>`{.interpreted-text
role="ref"}

:::: {#class_TextEdit_constant_GUTTER_TYPE_STRING}
::: rst-class
classref-enumeration-constant
:::
::::

`GutterType<enum_TextEdit_GutterType>`{.interpreted-text role="ref"}
**GUTTER_TYPE_STRING** = `0`

When a gutter is set to string using
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}, it is used to contain text set via the
`set_line_gutter_text()<class_TextEdit_method_set_line_gutter_text>`{.interpreted-text
role="ref"} method.

:::: {#class_TextEdit_constant_GUTTER_TYPE_ICON}
::: rst-class
classref-enumeration-constant
:::
::::

`GutterType<enum_TextEdit_GutterType>`{.interpreted-text role="ref"}
**GUTTER_TYPE_ICON** = `1`

When a gutter is set to icon using
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}, it is used to contain an icon set via the
`set_line_gutter_icon()<class_TextEdit_method_set_line_gutter_icon>`{.interpreted-text
role="ref"} method.

:::: {#class_TextEdit_constant_GUTTER_TYPE_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`GutterType<enum_TextEdit_GutterType>`{.interpreted-text role="ref"}
**GUTTER_TYPE_CUSTOM** = `2`

When a gutter is set to custom using
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}, it is used to contain custom visuals controlled by a
callback method set via the
`set_gutter_custom_draw()<class_TextEdit_method_set_gutter_custom_draw>`{.interpreted-text
role="ref"} method.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_TextEdit_property_autowrap_mode}
::: rst-class
classref-property
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **autowrap_mode** = `3`
`🔗<class_TextEdit_property_autowrap_mode>`{.interpreted-text
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

If `wrap_mode<class_TextEdit_property_wrap_mode>`{.interpreted-text
role="ref"} is set to
`LINE_WRAPPING_BOUNDARY<class_TextEdit_constant_LINE_WRAPPING_BOUNDARY>`{.interpreted-text
role="ref"}, sets text wrapping mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_backspace_deletes_composite_character_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**backspace_deletes_composite_character_enabled** = `false`
`🔗<class_TextEdit_property_backspace_deletes_composite_character_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_backspace_deletes_composite_character_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_backspace_deletes_composite_character_enabled**()

If `true` and
`caret_mid_grapheme<class_TextEdit_property_caret_mid_grapheme>`{.interpreted-text
role="ref"} is `false`, backspace deletes an entire composite character
such as ❤️‍🩹, instead of deleting part of the composite character.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_caret_blink}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **caret_blink** =
`false` `🔗<class_TextEdit_property_caret_blink>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_caret_blink_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_caret_blink_enabled**()

If `true`, makes the caret blink.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_caret_blink_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**caret_blink_interval** = `0.65`
`🔗<class_TextEdit_property_caret_blink_interval>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_caret_blink_interval**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_caret_blink_interval**()

The interval at which the caret blinks (in seconds).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_caret_draw_when_editable_disabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**caret_draw_when_editable_disabled** = `false`
`🔗<class_TextEdit_property_caret_draw_when_editable_disabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_caret_when_editable_disabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drawing_caret_when_editable_disabled**()

If `true`, caret will be visible when
`editable<class_TextEdit_property_editable>`{.interpreted-text
role="ref"} is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_caret_mid_grapheme}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **caret_mid_grapheme**
= `false`
`🔗<class_TextEdit_property_caret_mid_grapheme>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_caret_mid_grapheme_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_caret_mid_grapheme_enabled**()

Allow moving caret, selecting and removing the individual composite
character components.

\*\*Note:\*\* `Backspace`{.interpreted-text role="kbd"} is always
removing individual composite character components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_caret_move_on_right_click}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**caret_move_on_right_click** = `true`
`🔗<class_TextEdit_property_caret_move_on_right_click>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_move_caret_on_right_click_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_move_caret_on_right_click_enabled**()

If `true`, a right-click moves the caret at the mouse position before
displaying the context menu.

If `false`, the context menu ignores mouse location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_caret_multiple}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **caret_multiple** =
`true` `🔗<class_TextEdit_property_caret_multiple>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_multiple_carets_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_multiple_carets_enabled**()

If `true`, multiple carets are allowed. Left-clicking with
`Alt`{.interpreted-text role="kbd"} adds a new caret. See
`add_caret()<class_TextEdit_method_add_caret>`{.interpreted-text
role="ref"} and
`get_caret_count()<class_TextEdit_method_get_caret_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_caret_type}
::: rst-class
classref-property
:::
::::

`CaretType<enum_TextEdit_CaretType>`{.interpreted-text role="ref"}
**caret_type** = `0`
`🔗<class_TextEdit_property_caret_type>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_caret_type**(value:
  `CaretType<enum_TextEdit_CaretType>`{.interpreted-text role="ref"})
- `CaretType<enum_TextEdit_CaretType>`{.interpreted-text role="ref"}
  **get_caret_type**()

Set the type of caret to draw.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_context_menu_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**context_menu_enabled** = `true`
`🔗<class_TextEdit_property_context_menu_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_context_menu_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_context_menu_enabled**()

If `true`, a right-click displays the context menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_custom_word_separators}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**custom_word_separators** = `""`
`🔗<class_TextEdit_property_custom_word_separators>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_custom_word_separators**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_custom_word_separators**()

The characters to consider as word delimiters if
`use_custom_word_separators<class_TextEdit_property_use_custom_word_separators>`{.interpreted-text
role="ref"} is `true`. The characters should be defined without
separation, for example `#_!`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_deselect_on_focus_loss_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**deselect_on_focus_loss_enabled** = `true`
`🔗<class_TextEdit_property_deselect_on_focus_loss_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_deselect_on_focus_loss_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_deselect_on_focus_loss_enabled**()

If `true`, the selected text will be deselected when focus is lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_drag_and_drop_selection_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**drag_and_drop_selection_enabled** = `true`
`🔗<class_TextEdit_property_drag_and_drop_selection_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_and_drop_selection_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drag_and_drop_selection_enabled**()

If `true`, allow drag and drop of selected text. Text can still be
dropped from other sources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_draw_control_chars}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_control_chars**
= `false`
`🔗<class_TextEdit_property_draw_control_chars>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_control_chars**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_draw_control_chars**()

If `true`, control characters are displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_draw_spaces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_spaces** =
`false` `🔗<class_TextEdit_property_draw_spaces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_spaces**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drawing_spaces**()

If `true`, the \"space\" character will have a visible representation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_draw_tabs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_tabs** = `false`
`🔗<class_TextEdit_property_draw_tabs>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_tabs**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_drawing_tabs**()

If `true`, the \"tab\" character will have a visible representation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_editable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editable** = `true`
`🔗<class_TextEdit_property_editable>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editable**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_editable**()

If `false`, existing text cannot be modified and new text cannot be
added.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_emoji_menu_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **emoji_menu_enabled**
= `true`
`🔗<class_TextEdit_property_emoji_menu_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emoji_menu_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_emoji_menu_enabled**()

If `true`, \"Emoji and Symbols\" menu is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_empty_selection_clipboard_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**empty_selection_clipboard_enabled** = `true`
`🔗<class_TextEdit_property_empty_selection_clipboard_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_empty_selection_clipboard_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_empty_selection_clipboard_enabled**()

If `true`, copying or cutting without a selection is performed on all
lines with a caret. Otherwise, copy and cut require a selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_highlight_all_occurrences}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**highlight_all_occurrences** = `false`
`🔗<class_TextEdit_property_highlight_all_occurrences>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_highlight_all_occurrences**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_highlight_all_occurrences_enabled**()

If `true`, all occurrences of the selected text will be highlighted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_highlight_current_line}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**highlight_current_line** = `false`
`🔗<class_TextEdit_property_highlight_current_line>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_highlight_current_line**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_highlight_current_line_enabled**()

If `true`, the line containing the cursor is highlighted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_indent_wrapped_lines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**indent_wrapped_lines** = `false`
`🔗<class_TextEdit_property_indent_wrapped_lines>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_indent_wrapped_lines**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_indent_wrapped_lines**()

If `true`, all wrapped lines are indented to the same amount as the
unwrapped line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_TextEdit_property_language>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_language**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_language**()

Language code used for line-breaking and text shaping algorithms, if
left empty current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_middle_mouse_paste_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**middle_mouse_paste_enabled** = `true`
`🔗<class_TextEdit_property_middle_mouse_paste_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_middle_mouse_paste_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_middle_mouse_paste_enabled**()

If `false`, using middle mouse button to paste clipboard will be
disabled.

\*\*Note:\*\* This method is only implemented on Linux.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_minimap_draw}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **minimap_draw** =
`false` `🔗<class_TextEdit_property_minimap_draw>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_minimap**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drawing_minimap**()

If `true`, a minimap is shown, providing an outline of your source code.
The minimap uses a fixed-width text size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_minimap_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **minimap_width** = `80`
`🔗<class_TextEdit_property_minimap_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_minimap_width**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_minimap_width**()

The width, in pixels, of the minimap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_placeholder_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**placeholder_text** = `""`
`🔗<class_TextEdit_property_placeholder_text>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_placeholder**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_placeholder**()

Text shown when the **TextEdit** is empty. It is **not** the
**TextEdit**\'s default value (see
`text<class_TextEdit_property_text>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_scroll_fit_content_height}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**scroll_fit_content_height** = `false`
`🔗<class_TextEdit_property_scroll_fit_content_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fit_content_height_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_fit_content_height_enabled**()

If `true`, **TextEdit** will disable vertical scroll and fit minimum
height to the number of visible lines. When both this property and
`scroll_fit_content_width<class_TextEdit_property_scroll_fit_content_width>`{.interpreted-text
role="ref"} are `true`, no scrollbars will be displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_scroll_fit_content_width}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**scroll_fit_content_width** = `false`
`🔗<class_TextEdit_property_scroll_fit_content_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fit_content_width_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_fit_content_width_enabled**()

If `true`, **TextEdit** will disable horizontal scroll and fit minimum
width to the widest line in the text. When both this property and
`scroll_fit_content_height<class_TextEdit_property_scroll_fit_content_height>`{.interpreted-text
role="ref"} are `true`, no scrollbars will be displayed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_scroll_horizontal}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **scroll_horizontal** =
`0` `🔗<class_TextEdit_property_scroll_horizontal>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_h_scroll**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_h_scroll**()

If there is a horizontal scrollbar, this determines the current
horizontal scroll value in pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_scroll_past_end_of_file}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**scroll_past_end_of_file** = `false`
`🔗<class_TextEdit_property_scroll_past_end_of_file>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_past_end_of_file_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_scroll_past_end_of_file_enabled**()

Allow scrolling past the last line into \"virtual\" space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_scroll_smooth}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **scroll_smooth** =
`false` `🔗<class_TextEdit_property_scroll_smooth>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_smooth_scroll_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_smooth_scroll_enabled**()

Scroll smoothly over the text rather than jumping to the next location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_scroll_v_scroll_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**scroll_v_scroll_speed** = `80.0`
`🔗<class_TextEdit_property_scroll_v_scroll_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_scroll_speed**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_v_scroll_speed**()

Sets the scroll speed with the minimap or when
`scroll_smooth<class_TextEdit_property_scroll_smooth>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_scroll_vertical}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **scroll_vertical** =
`0.0` `🔗<class_TextEdit_property_scroll_vertical>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_v_scroll**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_v_scroll**()

If there is a vertical scrollbar, this determines the current vertical
scroll value in line numbers, starting at 0 for the top line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_selecting_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **selecting_enabled** =
`true` `🔗<class_TextEdit_property_selecting_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_selecting_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_selecting_enabled**()

If `true`, text can be selected.

If `false`, text can not be selected by the user or by the
`select()<class_TextEdit_method_select>`{.interpreted-text role="ref"}
or `select_all()<class_TextEdit_method_select_all>`{.interpreted-text
role="ref"} methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_shortcut_keys_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shortcut_keys_enabled** = `true`
`🔗<class_TextEdit_property_shortcut_keys_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shortcut_keys_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_shortcut_keys_enabled**()

If `true`, shortcut keys for context menu items are enabled, even if the
context menu is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_structured_text_bidi_override}
::: rst-class
classref-property
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **structured_text_bidi_override** = `0`
`🔗<class_TextEdit_property_structured_text_bidi_override>`{.interpreted-text
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

:::: {#class_TextEdit_property_structured_text_bidi_override_options}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**structured_text_bidi_override_options** = `[]`
`🔗<class_TextEdit_property_structured_text_bidi_override_options>`{.interpreted-text
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

:::: {#class_TextEdit_property_syntax_highlighter}
::: rst-class
classref-property
:::
::::

`SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
role="ref"} **syntax_highlighter**
`🔗<class_TextEdit_property_syntax_highlighter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_syntax_highlighter**(value:
  `SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
  role="ref"})
- `SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
  role="ref"} **get_syntax_highlighter**()

The syntax highlighter to use.

\*\*Note:\*\* A
`SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
role="ref"} instance should not be used across multiple **TextEdit**
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_tab_input_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **tab_input_mode** =
`true` `🔗<class_TextEdit_property_tab_input_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_input_mode**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_tab_input_mode**()

If `true`,
`ProjectSettings.input/ui_text_indent<class_ProjectSettings_property_input/ui_text_indent>`{.interpreted-text
role="ref"} input `Tab` character, otherwise it moves keyboard focus to
the next `Control<class_Control>`{.interpreted-text role="ref"} in the
scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_TextEdit_property_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_text**()

String value of the **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **text_direction** = `0`
`🔗<class_TextEdit_property_text_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text_direction**(value:
  `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"})
- `TextDirection<enum_Control_TextDirection>`{.interpreted-text
  role="ref"} **get_text_direction**()

Base text writing direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_use_custom_word_separators}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_custom_word_separators** = `false`
`🔗<class_TextEdit_property_use_custom_word_separators>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_custom_word_separators**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_custom_word_separators_enabled**()

If `false`, using `Ctrl + Left`{.interpreted-text role="kbd"} or
`Ctrl + Right`{.interpreted-text role="kbd"}
(`Cmd + Left`{.interpreted-text role="kbd"} or
`Cmd + Right`{.interpreted-text role="kbd"} on macOS) bindings will use
the behavior of
`use_default_word_separators<class_TextEdit_property_use_default_word_separators>`{.interpreted-text
role="ref"}. If `true`, it will also stop the caret if a character
within
`custom_word_separators<class_TextEdit_property_custom_word_separators>`{.interpreted-text
role="ref"} is detected. Useful for subword moving. This behavior also
will be applied to the behavior of text selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_use_default_word_separators}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_default_word_separators** = `true`
`🔗<class_TextEdit_property_use_default_word_separators>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_default_word_separators**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_default_word_separators_enabled**()

If `false`, using `Ctrl + Left`{.interpreted-text role="kbd"} or
`Ctrl + Right`{.interpreted-text role="kbd"}
(`Cmd + Left`{.interpreted-text role="kbd"} or
`Cmd + Right`{.interpreted-text role="kbd"} on macOS) bindings will stop
moving caret only if a space or punctuation is detected. If `true`, it
will also stop the caret if a character is part of
`` !"#$%&'()*+,-./:;<=>?@[\]^`{|}~ ``, the Unicode General Punctuation
table, or the Unicode CJK Punctuation table. Useful for subword moving.
This behavior also will be applied to the behavior of text selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_virtual_keyboard_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**virtual_keyboard_enabled** = `true`
`🔗<class_TextEdit_property_virtual_keyboard_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_virtual_keyboard_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_virtual_keyboard_enabled**()

If `true`, the native virtual keyboard is enabled on platforms that
support it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_virtual_keyboard_show_on_focus}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**virtual_keyboard_show_on_focus** = `true`
`🔗<class_TextEdit_property_virtual_keyboard_show_on_focus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_virtual_keyboard_show_on_focus**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_virtual_keyboard_show_on_focus**()

If `true`, the native virtual keyboard is shown on focus events on
platforms that support it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_property_wrap_mode}
::: rst-class
classref-property
:::
::::

`LineWrappingMode<enum_TextEdit_LineWrappingMode>`{.interpreted-text
role="ref"} **wrap_mode** = `0`
`🔗<class_TextEdit_property_wrap_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_wrapping_mode**(value:
  `LineWrappingMode<enum_TextEdit_LineWrappingMode>`{.interpreted-text
  role="ref"})
- `LineWrappingMode<enum_TextEdit_LineWrappingMode>`{.interpreted-text
  role="ref"} **get_line_wrapping_mode**()

Sets the line wrapping mode to use.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_TextEdit_private_method__backspace}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_backspace**(caret_index: `int<class_int>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_private_method__backspace>`{.interpreted-text
role="ref"}

Override this method to define what happens when the user presses the
backspace key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_private_method__copy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_copy**(caret_index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_private_method__copy>`{.interpreted-text
role="ref"}

Override this method to define what happens when the user performs a
copy operation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_private_method__cut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_cut**(caret_index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_private_method__cut>`{.interpreted-text
role="ref"}

Override this method to define what happens when the user performs a cut
operation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_private_method__handle_unicode_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_handle_unicode_input**(unicode_char:
`int<class_int>`{.interpreted-text role="ref"}, caret_index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_private_method__handle_unicode_input>`{.interpreted-text
role="ref"}

Override this method to define what happens when the user types in the
provided key `unicode_char`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_private_method__paste}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_paste**(caret_index: `int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_private_method__paste>`{.interpreted-text role="ref"}

Override this method to define what happens when the user performs a
paste operation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_private_method__paste_primary_clipboard}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_paste_primary_clipboard**(caret_index:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_private_method__paste_primary_clipboard>`{.interpreted-text
role="ref"}

Override this method to define what happens when the user performs a
paste operation with middle mouse button.

\*\*Note:\*\* This method is only implemented on Linux.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_add_caret}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_caret**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_add_caret>`{.interpreted-text role="ref"}

Adds a new caret at the given location. Returns the index of the new
caret, or `-1` if the location is invalid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_add_caret_at_carets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_caret_at_carets**(below: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TextEdit_method_add_caret_at_carets>`{.interpreted-text
role="ref"}

Adds an additional caret above or below every caret. If `below` is
`true` the new caret will be added below and above otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_add_gutter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_gutter**(at: `int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TextEdit_method_add_gutter>`{.interpreted-text role="ref"}

Register a new gutter to this **TextEdit**. Use `at` to have a specific
gutter order. A value of `-1` appends the gutter to the right.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_add_selection_for_next_occurrence}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_selection_for_next_occurrence**()
`🔗<class_TextEdit_method_add_selection_for_next_occurrence>`{.interpreted-text
role="ref"}

Adds a selection and a caret for the next occurrence of the current
selection. If there is no active selection, selects word under caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_adjust_carets_after_edit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**adjust_carets_after_edit**(caret: `int<class_int>`{.interpreted-text
role="ref"}, from_line: `int<class_int>`{.interpreted-text role="ref"},
from_col: `int<class_int>`{.interpreted-text role="ref"}, to_line:
`int<class_int>`{.interpreted-text role="ref"}, to_col:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_adjust_carets_after_edit>`{.interpreted-text
role="ref"}

**Deprecated:** No longer necessary since methods now adjust carets
themselves.

This method does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_adjust_viewport_to_caret}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**adjust_viewport_to_caret**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_TextEdit_method_adjust_viewport_to_caret>`{.interpreted-text
role="ref"}

Adjust the viewport so the caret is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_apply_ime}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **apply_ime**()
`🔗<class_TextEdit_method_apply_ime>`{.interpreted-text role="ref"}

Applies text from the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) (IME) to each caret
and closes the IME if it is open.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_backspace}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**backspace**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_TextEdit_method_backspace>`{.interpreted-text role="ref"}

Called when the user presses the backspace key. Can be overridden with
`_backspace()<class_TextEdit_private_method__backspace>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_begin_complex_operation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**begin_complex_operation**()
`🔗<class_TextEdit_method_begin_complex_operation>`{.interpreted-text
role="ref"}

Starts a multipart edit. All edits will be treated as one action until
`end_complex_operation()<class_TextEdit_method_end_complex_operation>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_begin_multicaret_edit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**begin_multicaret_edit**()
`🔗<class_TextEdit_method_begin_multicaret_edit>`{.interpreted-text
role="ref"}

Starts an edit for multiple carets. The edit must be ended with
`end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"}. Multicaret edits can be used to edit text at multiple
carets and delay merging the carets until the end, so the caret indexes
aren\'t affected immediately.
`begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>`{.interpreted-text
role="ref"} and
`end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"} can be nested, and the merge will happen at the last
`end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"}.

    begin_complex_operation()
    begin_multicaret_edit()
    for i in range(get_caret_count()):
        if multicaret_edit_ignore_caret(i):
            continue
        # Logic here.
    end_multicaret_edit()
    end_complex_operation()

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_cancel_ime}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cancel_ime**()
`🔗<class_TextEdit_method_cancel_ime>`{.interpreted-text role="ref"}

Closes the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) (IME) if it is open.
Any text in the IME will be lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_center_viewport_to_caret}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**center_viewport_to_caret**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_TextEdit_method_center_viewport_to_caret>`{.interpreted-text
role="ref"}

Centers the viewport on the line the editing caret is at. This also
resets the
`scroll_horizontal<class_TextEdit_property_scroll_horizontal>`{.interpreted-text
role="ref"} value to `0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_TextEdit_method_clear>`{.interpreted-text role="ref"}

Performs a full reset of **TextEdit**, including undo history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_clear_undo_history}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_undo_history**()
`🔗<class_TextEdit_method_clear_undo_history>`{.interpreted-text
role="ref"}

Clears the undo history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_collapse_carets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**collapse_carets**(from_line: `int<class_int>`{.interpreted-text
role="ref"}, from_column: `int<class_int>`{.interpreted-text
role="ref"}, to_line: `int<class_int>`{.interpreted-text role="ref"},
to_column: `int<class_int>`{.interpreted-text role="ref"}, inclusive:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_TextEdit_method_collapse_carets>`{.interpreted-text
role="ref"}

Collapse all carets in the given range to the `from_line` and
`from_column` position.

`inclusive` applies to both ends.

If
`is_in_mulitcaret_edit()<class_TextEdit_method_is_in_mulitcaret_edit>`{.interpreted-text
role="ref"} is `true`, carets that are collapsed will be `true` for
`multicaret_edit_ignore_caret()<class_TextEdit_method_multicaret_edit_ignore_caret>`{.interpreted-text
role="ref"}.

`merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`{.interpreted-text
role="ref"} will be called if any carets were collapsed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_copy}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**copy**(caret_index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_TextEdit_method_copy>`{.interpreted-text role="ref"}

Copies the current text selection. Can be overridden with
`_copy()<class_TextEdit_private_method__copy>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_cut}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cut**(caret_index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_TextEdit_method_cut>`{.interpreted-text role="ref"}

Cut\'s the current selection. Can be overridden with
`_cut()<class_TextEdit_private_method__cut>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_delete_selection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delete_selection**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_TextEdit_method_delete_selection>`{.interpreted-text
role="ref"}

Deletes the selected text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_deselect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**deselect**(caret_index: `int<class_int>`{.interpreted-text role="ref"}
= -1) `🔗<class_TextEdit_method_deselect>`{.interpreted-text role="ref"}

Deselects the current selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_end_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**end_action**()
`🔗<class_TextEdit_method_end_action>`{.interpreted-text role="ref"}

Marks the end of steps in the current action started with
`start_action()<class_TextEdit_method_start_action>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_end_complex_operation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**end_complex_operation**()
`🔗<class_TextEdit_method_end_complex_operation>`{.interpreted-text
role="ref"}

Ends a multipart edit, started with
`begin_complex_operation()<class_TextEdit_method_begin_complex_operation>`{.interpreted-text
role="ref"}. If called outside a complex operation, the current
operation is pushed onto the undo/redo stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_end_multicaret_edit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**end_multicaret_edit**()
`🔗<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"}

Ends an edit for multiple carets, that was started with
`begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>`{.interpreted-text
role="ref"}. If this was the last
`end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"} and
`merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`{.interpreted-text
role="ref"} was called, carets will be merged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_caret_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_caret_column**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_caret_column>`{.interpreted-text
role="ref"}

Returns the column the editing caret is at.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_caret_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_caret_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_caret_count>`{.interpreted-text
role="ref"}

Returns the number of carets in this **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_caret_draw_pos}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_caret_draw_pos**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_caret_draw_pos>`{.interpreted-text
role="ref"}

Returns the caret pixel draw position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_caret_index_edit_order}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_caret_index_edit_order**()
`🔗<class_TextEdit_method_get_caret_index_edit_order>`{.interpreted-text
role="ref"}

**Deprecated:** Carets no longer need to be edited in any specific
order. If the carets need to be sorted, use
`get_sorted_carets()<class_TextEdit_method_get_sorted_carets>`{.interpreted-text
role="ref"} instead.

Returns a list of caret indexes in their edit order, this done from
bottom to top. Edit order refers to the way actions such as
`insert_text_at_caret()<class_TextEdit_method_insert_text_at_caret>`{.interpreted-text
role="ref"} are applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_caret_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_caret_line**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_caret_line>`{.interpreted-text role="ref"}

Returns the line the editing caret is on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_caret_wrap_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_caret_wrap_index**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_caret_wrap_index>`{.interpreted-text
role="ref"}

Returns the wrap index the editing caret is on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_first_non_whitespace_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_first_non_whitespace_column**(line:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_first_non_whitespace_column>`{.interpreted-text
role="ref"}

Returns the first column containing a non-whitespace character on the
given line. If there is only whitespace, returns the number of
characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_first_visible_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_first_visible_line**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_first_visible_line>`{.interpreted-text
role="ref"}

Returns the first visible line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_gutter_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_gutter_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_gutter_count>`{.interpreted-text
role="ref"}

Returns the number of gutters registered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_gutter_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_gutter_name**(gutter: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_gutter_name>`{.interpreted-text
role="ref"}

Returns the name of the gutter at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_gutter_type}
::: rst-class
classref-method
:::
::::

`GutterType<enum_TextEdit_GutterType>`{.interpreted-text role="ref"}
**get_gutter_type**(gutter: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_gutter_type>`{.interpreted-text
role="ref"}

Returns the type of the gutter at the given index. Gutters can contain
icons, text, or custom visuals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_gutter_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_gutter_width**(gutter: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_gutter_width>`{.interpreted-text
role="ref"}

Returns the width of the gutter at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_h_scroll_bar}
::: rst-class
classref-method
:::
::::

`HScrollBar<class_HScrollBar>`{.interpreted-text role="ref"}
**get_h_scroll_bar**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_h_scroll_bar>`{.interpreted-text
role="ref"}

Returns the `HScrollBar<class_HScrollBar>`{.interpreted-text role="ref"}
used by **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_indent_level}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_indent_level**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_indent_level>`{.interpreted-text
role="ref"}

Returns the indent level of the given line. This is the number of spaces
and tabs at the beginning of the line, with the tabs taking the tab size
into account (see
`get_tab_size()<class_TextEdit_method_get_tab_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_last_full_visible_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_last_full_visible_line**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_last_full_visible_line>`{.interpreted-text
role="ref"}

Returns the last visible line. Use
`get_last_full_visible_line_wrap_index()<class_TextEdit_method_get_last_full_visible_line_wrap_index>`{.interpreted-text
role="ref"} for the wrap index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_last_full_visible_line_wrap_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_last_full_visible_line_wrap_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_last_full_visible_line_wrap_index>`{.interpreted-text
role="ref"}

Returns the last visible wrap index of the last visible line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_last_unhidden_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_last_unhidden_line**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_last_unhidden_line>`{.interpreted-text
role="ref"}

Returns the last unhidden line in the entire **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_line**(line:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_get_line>`{.interpreted-text
role="ref"}

Returns the text of a specific line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_background_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_line_background_color**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_background_color>`{.interpreted-text
role="ref"}

Returns the custom background color of the given line. If no color is
set, returns `Color(0, 0, 0, 0)`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_column_at_pos}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_line_column_at_pos**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}, clamp_line:
`bool<class_bool>`{.interpreted-text role="ref"} = true, clamp_column:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_column_at_pos>`{.interpreted-text
role="ref"}

Returns the line and column at the given position. In the returned
vector, `x` is the column and `y` is the line.

If `clamp_line` is `false` and `position` is below the last line,
`Vector2i(-1, -1)` is returned.

If `clamp_column` is `false` and `position` is outside the column range
of the line, `Vector2i(-1, -1)` is returned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_count>`{.interpreted-text role="ref"}

Returns the number of lines in the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_gutter_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_line_gutter_icon**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_gutter_icon>`{.interpreted-text
role="ref"}

Returns the icon currently in `gutter` at `line`. This only works when
the gutter type is
`GUTTER_TYPE_ICON<class_TextEdit_constant_GUTTER_TYPE_ICON>`{.interpreted-text
role="ref"} (see
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_gutter_item_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_line_gutter_item_color**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_gutter_item_color>`{.interpreted-text
role="ref"}

Returns the color currently in `gutter` at `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_gutter_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_line_gutter_metadata**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_gutter_metadata>`{.interpreted-text
role="ref"}

Returns the metadata currently in `gutter` at `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_gutter_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_line_gutter_text**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_gutter_text>`{.interpreted-text
role="ref"}

Returns the text currently in `gutter` at `line`. This only works when
the gutter type is
`GUTTER_TYPE_STRING<class_TextEdit_constant_GUTTER_TYPE_STRING>`{.interpreted-text
role="ref"} (see
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_height>`{.interpreted-text
role="ref"}

Returns the maximum value of the line height among all lines.

\*\*Note:\*\* The return value is influenced by
`line_spacing<class_TextEdit_theme_constant_line_spacing>`{.interpreted-text
role="ref"} and
`font_size<class_TextEdit_theme_font_size_font_size>`{.interpreted-text
role="ref"}. And it will not be less than `1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_ranges_from_carets}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}\]
**get_line_ranges_from_carets**(only_selections:
`bool<class_bool>`{.interpreted-text role="ref"} = false,
merge_adjacent: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_ranges_from_carets>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of line
ranges where `x` is the first line and `y` is the last line. All lines
within these ranges will have a caret on them or be part of a selection.
Each line will only be part of one line range, even if it has multiple
carets on it.

If a selection\'s end column
(`get_selection_to_column()<class_TextEdit_method_get_selection_to_column>`{.interpreted-text
role="ref"}) is at column `0`, that line will not be included. If a
selection begins on the line after another selection ends and
`merge_adjacent` is `true`, or they begin and end on the same line, one
line range will include both selections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_width**(line:
`int<class_int>`{.interpreted-text role="ref"}, wrap_index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_width>`{.interpreted-text role="ref"}

Returns the width in pixels of the `wrap_index` on `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_with_ime}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_line_with_ime**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_with_ime>`{.interpreted-text
role="ref"}

Returns line text as it is currently displayed, including IME
composition string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_wrap_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_line_wrap_count**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_wrap_count>`{.interpreted-text
role="ref"}

Returns the number of times the given line is wrapped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_wrap_index_at_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_line_wrap_index_at_column**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_wrap_index_at_column>`{.interpreted-text
role="ref"}

Returns the wrap index of the given column on the given line. This
ranges from `0` to
`get_line_wrap_count()<class_TextEdit_method_get_line_wrap_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_line_wrapped_text}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_line_wrapped_text**(line:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_line_wrapped_text>`{.interpreted-text
role="ref"}

Returns an array of `String<class_String>`{.interpreted-text
role="ref"}s representing each wrapped index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_local_mouse_pos}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_local_mouse_pos**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_local_mouse_pos>`{.interpreted-text
role="ref"}

Returns the local mouse position adjusted for the text direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_menu}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_menu**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_get_menu>`{.interpreted-text
role="ref"}

Returns the `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
of this **TextEdit**. By default, this menu is displayed when
right-clicking on the **TextEdit**.

You can add custom menu items or remove standard ones. Make sure your
IDs don\'t conflict with the standard ones (see
`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"}). For
example:

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var menu = get_menu() \# Remove all items after \"Redo\".
    menu.item_count = menu.get_item_index(MENU_REDO) + 1 \# Add custom
    items. menu.add_separator() menu.add_item(\"Insert Date\",
    MENU_MAX + 1) \# Connect callback.
    menu.id_pressed.connect([on_item_pressed]{#on_item_pressed})

func [on_item_pressed]{#on_item_pressed}(id):

:   

    if id == MENU_MAX + 1:

    :   insert_text_at_caret(Time.get_date_string_from_system())
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { var menu = GetMenu(); // Remove
all items after \"Redo\". menu.ItemCount =
menu.GetItemIndex(TextEdit.MenuItems.Redo) + 1; // Add custom items.
menu.AddSeparator(); menu.AddItem(\"Insert Date\",
TextEdit.MenuItems.Max + 1); // Add event handler. menu.IdPressed +=
OnItemPressed; }

public void OnItemPressed(int id) { if (id ==
TextEdit.MenuItems.Max + 1) {
InsertTextAtCaret(Time.GetDateStringFromSystem()); } }
:::
:::::

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their `Window.visible<class_Window_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_minimap_line_at_pos}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_minimap_line_at_pos**(position:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_minimap_line_at_pos>`{.interpreted-text
role="ref"}

Returns the equivalent minimap line at `position`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_minimap_visible_lines}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_minimap_visible_lines**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_minimap_visible_lines>`{.interpreted-text
role="ref"}

Returns the number of lines that may be drawn on the minimap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_next_composite_character_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_next_composite_character_column**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_next_composite_character_column>`{.interpreted-text
role="ref"}

Returns the correct column at the end of a composite character like ❤️‍🩹
(mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is
comprised of more than one Unicode code point, if the caret is at the
start of the composite character. Also returns the correct column with
the caret at mid grapheme and for non-composite characters.

\*\*Note:\*\* To check at caret location use
`get_next_composite_character_column(get_caret_line(), get_caret_column())`

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_next_visible_line_index_offset_from}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_next_visible_line_index_offset_from**(line:
`int<class_int>`{.interpreted-text role="ref"}, wrap_index:
`int<class_int>`{.interpreted-text role="ref"}, visible_amount:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_next_visible_line_index_offset_from>`{.interpreted-text
role="ref"}

Similar to
`get_next_visible_line_offset_from()<class_TextEdit_method_get_next_visible_line_offset_from>`{.interpreted-text
role="ref"}, but takes into account the line wrap indexes. In the
returned vector, `x` is the line, `y` is the wrap index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_next_visible_line_offset_from}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_next_visible_line_offset_from**(line:
`int<class_int>`{.interpreted-text role="ref"}, visible_amount:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_next_visible_line_offset_from>`{.interpreted-text
role="ref"}

Returns the count to the next visible line from `line` to
`line + visible_amount`. Can also count backwards. For example if a
**TextEdit** has 5 lines with lines 2 and 3 hidden, calling this with
`line = 1, visible_amount = 1` would return 3.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_pos_at_line_column}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_pos_at_line_column**(line: `int<class_int>`{.interpreted-text
role="ref"}, column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_pos_at_line_column>`{.interpreted-text
role="ref"}

Returns the local position for the given `line` and `column`. If `x` or
`y` of the returned vector equal `-1`, the position is outside of the
viewable area of the control.

\*\*Note:\*\* The Y position corresponds to the bottom side of the line.
Use
`get_rect_at_line_column()<class_TextEdit_method_get_rect_at_line_column>`{.interpreted-text
role="ref"} to get the top side position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_previous_composite_character_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_previous_composite_character_column**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_previous_composite_character_column>`{.interpreted-text
role="ref"}

Returns the correct column at the start of a composite character like ❤️‍🩹
(mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is
comprised of more than one Unicode code point, if the caret is at the
end of the composite character. Also returns the correct column with the
caret at mid grapheme and for non-composite characters.

\*\*Note:\*\* To check at caret location use
`get_previous_composite_character_column(get_caret_line(), get_caret_column())`

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_rect_at_line_column}
::: rst-class
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**get_rect_at_line_column**(line: `int<class_int>`{.interpreted-text
role="ref"}, column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_rect_at_line_column>`{.interpreted-text
role="ref"}

Returns the local position and size for the grapheme at the given `line`
and `column`. If `x` or `y` position of the returned rect equal `-1`,
the position is outside of the viewable area of the control.

\*\*Note:\*\* The Y position of the returned rect corresponds to the top
side of the line, unlike
`get_pos_at_line_column()<class_TextEdit_method_get_pos_at_line_column>`{.interpreted-text
role="ref"} which returns the bottom side.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_saved_version}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_saved_version**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_saved_version>`{.interpreted-text
role="ref"}

Returns the last tagged saved version from
`tag_saved_version()<class_TextEdit_method_tag_saved_version>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_scroll_pos_for_line}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_scroll_pos_for_line**(line: `int<class_int>`{.interpreted-text
role="ref"}, wrap_index: `int<class_int>`{.interpreted-text role="ref"}
= 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_scroll_pos_for_line>`{.interpreted-text
role="ref"}

Returns the scroll position for `wrap_index` of `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selected_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_selected_text**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_TextEdit_method_get_selected_text>`{.interpreted-text
role="ref"}

Returns the text inside the selection of a caret, or all the carets if
`caret_index` is its default value `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_at_line_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_at_line_column**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"}, include_edges:
`bool<class_bool>`{.interpreted-text role="ref"} = true,
only_selections: `bool<class_bool>`{.interpreted-text role="ref"} =
true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_at_line_column>`{.interpreted-text
role="ref"}

Returns the caret index of the selection at the given `line` and
`column`, or `-1` if there is none.

If `include_edges` is `false`, the position must be inside the selection
and not at either end. If `only_selections` is `false`, carets without a
selection will also be considered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_column**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_column>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`get_selection_origin_column()<class_TextEdit_method_get_selection_origin_column>`{.interpreted-text
role="ref"} instead.

Returns the original start column of the selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_from_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_from_column**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_from_column>`{.interpreted-text
role="ref"}

Returns the selection begin column. Returns the caret column if there is
no selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_from_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_from_line**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_from_line>`{.interpreted-text
role="ref"}

Returns the selection begin line. Returns the caret line if there is no
selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_line**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_line>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`get_selection_origin_line()<class_TextEdit_method_get_selection_origin_line>`{.interpreted-text
role="ref"} instead.

Returns the original start line of the selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_mode}
::: rst-class
classref-method
:::
::::

`SelectionMode<enum_TextEdit_SelectionMode>`{.interpreted-text
role="ref"} **get_selection_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_mode>`{.interpreted-text
role="ref"}

Returns the current selection mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_origin_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_origin_column**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_origin_column>`{.interpreted-text
role="ref"}

Returns the origin column of the selection. This is the opposite end
from the caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_origin_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_origin_line**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_origin_line>`{.interpreted-text
role="ref"}

Returns the origin line of the selection. This is the opposite end from
the caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_to_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_to_column**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_to_column>`{.interpreted-text
role="ref"}

Returns the selection end column. Returns the caret column if there is
no selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_selection_to_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_to_line**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_selection_to_line>`{.interpreted-text
role="ref"}

Returns the selection end line. Returns the caret line if there is no
selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_sorted_carets}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_sorted_carets**(include_ignored_carets:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_sorted_carets>`{.interpreted-text
role="ref"}

Returns the carets sorted by selection beginning from lowest line and
column to highest (from top to bottom of text).

If `include_ignored_carets` is `false`, carets from
`multicaret_edit_ignore_caret()<class_TextEdit_method_multicaret_edit_ignore_caret>`{.interpreted-text
role="ref"} will be ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_tab_size}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_tab_size**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_get_tab_size>`{.interpreted-text
role="ref"}

Returns the **TextEdit**\'s\' tab size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_total_gutter_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_total_gutter_width**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_total_gutter_width>`{.interpreted-text
role="ref"}

Returns the total width of all gutters and internal padding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_total_visible_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_total_visible_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_total_visible_line_count>`{.interpreted-text
role="ref"}

Returns the total number of lines in the text. This includes wrapped
lines and excludes folded lines. If
`wrap_mode<class_TextEdit_property_wrap_mode>`{.interpreted-text
role="ref"} is set to
`LINE_WRAPPING_NONE<class_TextEdit_constant_LINE_WRAPPING_NONE>`{.interpreted-text
role="ref"} and no lines are folded (see
`CodeEdit.is_line_folded()<class_CodeEdit_method_is_line_folded>`{.interpreted-text
role="ref"}) then this is equivalent to
`get_line_count()<class_TextEdit_method_get_line_count>`{.interpreted-text
role="ref"}. See
`get_visible_line_count_in_range()<class_TextEdit_method_get_visible_line_count_in_range>`{.interpreted-text
role="ref"} for a limited range of lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_v_scroll_bar}
::: rst-class
classref-method
:::
::::

`VScrollBar<class_VScrollBar>`{.interpreted-text role="ref"}
**get_v_scroll_bar**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_v_scroll_bar>`{.interpreted-text
role="ref"}

Returns the `VScrollBar<class_VScrollBar>`{.interpreted-text role="ref"}
of the **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_version}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_version**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_get_version>`{.interpreted-text
role="ref"}

Returns the current version of the **TextEdit**. The version is a count
of recorded operations by the undo/redo history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_visible_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_visible_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_visible_line_count>`{.interpreted-text
role="ref"}

Returns the number of lines that can visually fit, rounded down, based
on this control\'s height.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_visible_line_count_in_range}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_visible_line_count_in_range**(from_line:
`int<class_int>`{.interpreted-text role="ref"}, to_line:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_visible_line_count_in_range>`{.interpreted-text
role="ref"}

Returns the total number of lines between `from_line` and `to_line`
(inclusive) in the text. This includes wrapped lines and excludes folded
lines. If the range covers all lines it is equivalent to
`get_total_visible_line_count()<class_TextEdit_method_get_total_visible_line_count>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_word_at_pos}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_word_at_pos**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_word_at_pos>`{.interpreted-text
role="ref"}

Returns the word at `position`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_get_word_under_caret}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_word_under_caret**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_get_word_under_caret>`{.interpreted-text
role="ref"}

Returns a `String<class_String>`{.interpreted-text role="ref"} text with
the word under the caret\'s location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_has_ime_text}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_ime_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_has_ime_text>`{.interpreted-text
role="ref"}

Returns `true` if the user has text in the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) (IME).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_has_redo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_redo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_has_redo>`{.interpreted-text
role="ref"}

Returns `true` if a \"redo\" action is available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_has_selection}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_selection**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_has_selection>`{.interpreted-text
role="ref"}

Returns `true` if the user has selected text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_has_undo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_undo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_has_undo>`{.interpreted-text
role="ref"}

Returns `true` if an \"undo\" action is available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_insert_line_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**insert_line_at**(line: `int<class_int>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_insert_line_at>`{.interpreted-text role="ref"}

Inserts a new line with `text` at `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_insert_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**insert_text**(text: `String<class_String>`{.interpreted-text
role="ref"}, line: `int<class_int>`{.interpreted-text role="ref"},
column: `int<class_int>`{.interpreted-text role="ref"},
before_selection_begin: `bool<class_bool>`{.interpreted-text role="ref"}
= true, before_selection_end: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_TextEdit_method_insert_text>`{.interpreted-text role="ref"}

Inserts the `text` at `line` and `column`.

If `before_selection_begin` is `true`, carets and selections that begin
at `line` and `column` will moved to the end of the inserted text, along
with all carets after it.

If `before_selection_end` is `true`, selections that end at `line` and
`column` will be extended to the end of the inserted text. These
parameters can be used to insert text inside of or outside of
selections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_insert_text_at_caret}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**insert_text_at_caret**(text: `String<class_String>`{.interpreted-text
role="ref"}, caret_index: `int<class_int>`{.interpreted-text role="ref"}
= -1) `🔗<class_TextEdit_method_insert_text_at_caret>`{.interpreted-text
role="ref"}

Insert the specified text at the caret position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_caret_after_selection_origin}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_caret_after_selection_origin**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_caret_after_selection_origin>`{.interpreted-text
role="ref"}

Returns `true` if the caret of the selection is after the selection
origin. This can be used to determine the direction of the selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_caret_visible}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_caret_visible**(caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_caret_visible>`{.interpreted-text
role="ref"}

Returns `true` if the caret is visible, `false` otherwise. A caret will
be considered hidden if it is outside the scrollable area when scrolling
is enabled.

\*\*Note:\*\*
`is_caret_visible()<class_TextEdit_method_is_caret_visible>`{.interpreted-text
role="ref"} does not account for a caret being off-screen if it is still
within the scrollable area. It will return `true` even if the caret is
off-screen as long as it meets **TextEdit**\'s own conditions for being
visible. This includes uses of
`scroll_fit_content_width<class_TextEdit_property_scroll_fit_content_width>`{.interpreted-text
role="ref"} and
`scroll_fit_content_height<class_TextEdit_property_scroll_fit_content_height>`{.interpreted-text
role="ref"} that cause the **TextEdit** to expand beyond the viewport\'s
bounds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_dragging_cursor}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_dragging_cursor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_dragging_cursor>`{.interpreted-text
role="ref"}

Returns `true` if the user is dragging their mouse for scrolling,
selecting, or text dragging.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_gutter_clickable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_gutter_clickable**(gutter: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_gutter_clickable>`{.interpreted-text
role="ref"}

Returns `true` if the gutter at the given index is clickable. See
`set_gutter_clickable()<class_TextEdit_method_set_gutter_clickable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_gutter_drawn}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_gutter_drawn**(gutter: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_gutter_drawn>`{.interpreted-text
role="ref"}

Returns `true` if the gutter at the given index is currently drawn. See
`set_gutter_draw()<class_TextEdit_method_set_gutter_draw>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_gutter_overwritable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_gutter_overwritable**(gutter: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_gutter_overwritable>`{.interpreted-text
role="ref"}

Returns `true` if the gutter at the given index is overwritable. See
`set_gutter_overwritable()<class_TextEdit_method_set_gutter_overwritable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_in_mulitcaret_edit}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_in_mulitcaret_edit**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_in_mulitcaret_edit>`{.interpreted-text
role="ref"}

Returns `true` if a
`begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>`{.interpreted-text
role="ref"} has been called and
`end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"} has not yet been called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_line_gutter_clickable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_gutter_clickable**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_line_gutter_clickable>`{.interpreted-text
role="ref"}

Returns `true` if the gutter at the given index on the given line is
clickable. See
`set_line_gutter_clickable()<class_TextEdit_method_set_line_gutter_clickable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_line_wrapped}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_wrapped**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_line_wrapped>`{.interpreted-text
role="ref"}

Returns if the given line is wrapped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_menu_visible}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_menu_visible**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_menu_visible>`{.interpreted-text
role="ref"}

Returns `true` if the menu is visible. Use this instead of
`get_menu().visible` to improve performance (so the creation of the menu
is avoided). See
`get_menu()<class_TextEdit_method_get_menu>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_mouse_over_selection}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_mouse_over_selection**(edges: `bool<class_bool>`{.interpreted-text
role="ref"}, caret_index: `int<class_int>`{.interpreted-text role="ref"}
= -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_mouse_over_selection>`{.interpreted-text
role="ref"}

Returns `true` if the mouse is over a selection. If `edges` is `true`,
the edges are considered part of the selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_is_overtype_mode_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_overtype_mode_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_is_overtype_mode_enabled>`{.interpreted-text
role="ref"}

Returns `true` if overtype mode is enabled. See
`set_overtype_mode_enabled()<class_TextEdit_method_set_overtype_mode_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_menu_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**menu_option**(option: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_menu_option>`{.interpreted-text role="ref"}

Executes a given action as defined in the
`MenuItems<enum_TextEdit_MenuItems>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_merge_gutters}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**merge_gutters**(from_line: `int<class_int>`{.interpreted-text
role="ref"}, to_line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_merge_gutters>`{.interpreted-text role="ref"}

Merge the gutters from `from_line` into `to_line`. Only overwritable
gutters will be copied. See
`set_gutter_overwritable()<class_TextEdit_method_set_gutter_overwritable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_merge_overlapping_carets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**merge_overlapping_carets**()
`🔗<class_TextEdit_method_merge_overlapping_carets>`{.interpreted-text
role="ref"}

Merges any overlapping carets. Will favor the newest caret, or the caret
with a selection.

If
`is_in_mulitcaret_edit()<class_TextEdit_method_is_in_mulitcaret_edit>`{.interpreted-text
role="ref"} is `true`, the merge will be queued to happen at the end of
the multicaret edit. See
`begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>`{.interpreted-text
role="ref"} and
`end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This is not called when a caret changes position but after
certain actions, so it is possible to get into a state where carets
overlap.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_multicaret_edit_ignore_caret}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**multicaret_edit_ignore_caret**(caret_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_TextEdit_method_multicaret_edit_ignore_caret>`{.interpreted-text
role="ref"}

Returns `true` if the given `caret_index` should be ignored as part of a
multicaret edit. See
`begin_multicaret_edit()<class_TextEdit_method_begin_multicaret_edit>`{.interpreted-text
role="ref"} and
`end_multicaret_edit()<class_TextEdit_method_end_multicaret_edit>`{.interpreted-text
role="ref"}. Carets that should be ignored are ones that were part of
removed text and will likely be merged at the end of the edit, or carets
that were added during the edit.

It is recommended to `continue` within a loop iterating on multiple
carets if a caret should be ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_paste}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**paste**(caret_index: `int<class_int>`{.interpreted-text role="ref"} =
-1) `🔗<class_TextEdit_method_paste>`{.interpreted-text role="ref"}

Paste at the current location. Can be overridden with
`_paste()<class_TextEdit_private_method__paste>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_paste_primary_clipboard}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**paste_primary_clipboard**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TextEdit_method_paste_primary_clipboard>`{.interpreted-text
role="ref"}

Pastes the primary clipboard.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_redo}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **redo**()
`🔗<class_TextEdit_method_redo>`{.interpreted-text role="ref"}

Perform redo operation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_remove_caret}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_caret**(caret: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_remove_caret>`{.interpreted-text role="ref"}

Removes the given caret index.

\*\*Note:\*\* This can result in adjustment of all other caret indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_remove_gutter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_gutter**(gutter: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_TextEdit_method_remove_gutter>`{.interpreted-text
role="ref"}

Removes the gutter at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_remove_line_at}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_line_at**(line: `int<class_int>`{.interpreted-text role="ref"},
move_carets_down: `bool<class_bool>`{.interpreted-text role="ref"} =
true) `🔗<class_TextEdit_method_remove_line_at>`{.interpreted-text
role="ref"}

Removes the line of text at `line`. Carets on this line will attempt to
match their previous visual x position.

If `move_carets_down` is `true` carets will move to the next line down,
otherwise carets will move up.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_remove_secondary_carets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_secondary_carets**()
`🔗<class_TextEdit_method_remove_secondary_carets>`{.interpreted-text
role="ref"}

Removes all additional carets.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_remove_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_text**(from_line: `int<class_int>`{.interpreted-text
role="ref"}, from_column: `int<class_int>`{.interpreted-text
role="ref"}, to_line: `int<class_int>`{.interpreted-text role="ref"},
to_column: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_remove_text>`{.interpreted-text role="ref"}

Removes text between the given positions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_search}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**search**(text: `String<class_String>`{.interpreted-text role="ref"},
flags: `int<class_int>`{.interpreted-text role="ref"}, from_line:
`int<class_int>`{.interpreted-text role="ref"}, from_column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_TextEdit_method_search>`{.interpreted-text
role="ref"}

Perform a search inside the text. Search flags can be specified in the
`SearchFlags<enum_TextEdit_SearchFlags>`{.interpreted-text role="ref"}
enum.

In the returned vector, `x` is the column, `y` is the line. If no
results are found, both are equal to `-1`.

::::: tabs
::: code-tab
gdscript

var result = search(\"print\", SEARCH_WHOLE_WORDS, 0, 0) if result.x !=
-1: \# Result found. var line_number = result.y var column_number =
result.x
:::

::: code-tab
csharp

Vector2I result = Search(\"print\",
(uint)TextEdit.SearchFlags.WholeWords, 0, 0); if (result.X != -1) { //
Result found. int lineNumber = result.Y; int columnNumber = result.X; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_select}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select**(origin_line: `int<class_int>`{.interpreted-text role="ref"},
origin_column: `int<class_int>`{.interpreted-text role="ref"},
caret_line: `int<class_int>`{.interpreted-text role="ref"},
caret_column: `int<class_int>`{.interpreted-text role="ref"},
caret_index: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_TextEdit_method_select>`{.interpreted-text role="ref"}

Selects text from `origin_line` and `origin_column` to `caret_line` and
`caret_column` for the given `caret_index`. This moves the selection
origin and the caret. If the positions are the same, the selection will
be deselected.

If
`selecting_enabled<class_TextEdit_property_selecting_enabled>`{.interpreted-text
role="ref"} is `false`, no selection will occur.

\*\*Note:\*\* If supporting multiple carets this will not check for any
overlap. See
`merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_select_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select_all**()
`🔗<class_TextEdit_method_select_all>`{.interpreted-text role="ref"}

Select all the text.

If
`selecting_enabled<class_TextEdit_property_selecting_enabled>`{.interpreted-text
role="ref"} is `false`, no selection will occur.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_select_word_under_caret}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select_word_under_caret**(caret_index:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_TextEdit_method_select_word_under_caret>`{.interpreted-text
role="ref"}

Selects the word under the caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_caret_column}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_caret_column**(column: `int<class_int>`{.interpreted-text
role="ref"}, adjust_viewport: `bool<class_bool>`{.interpreted-text
role="ref"} = true, caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_TextEdit_method_set_caret_column>`{.interpreted-text
role="ref"}

Moves the caret to the specified `column` index.

If `adjust_viewport` is `true`, the viewport will center at the caret
position after the move occurs.

\*\*Note:\*\* If supporting multiple carets this will not check for any
overlap. See
`merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_caret_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_caret_line**(line: `int<class_int>`{.interpreted-text role="ref"},
adjust_viewport: `bool<class_bool>`{.interpreted-text role="ref"} =
true, can_be_hidden: `bool<class_bool>`{.interpreted-text role="ref"} =
true, wrap_index: `int<class_int>`{.interpreted-text role="ref"} = 0,
caret_index: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_TextEdit_method_set_caret_line>`{.interpreted-text role="ref"}

Moves the caret to the specified `line` index. The caret column will be
moved to the same visual position it was at the last time
`set_caret_column()<class_TextEdit_method_set_caret_column>`{.interpreted-text
role="ref"} was called, or clamped to the end of the line.

If `adjust_viewport` is `true`, the viewport will center at the caret
position after the move occurs.

If `can_be_hidden` is `true`, the specified `line` can be hidden.

If `wrap_index` is `-1`, the caret column will be clamped to the
`line`\'s length. If `wrap_index` is greater than `-1`, the column will
be moved to attempt to match the visual x position on the line\'s
`wrap_index` to the position from the last time
`set_caret_column()<class_TextEdit_method_set_caret_column>`{.interpreted-text
role="ref"} was called.

\*\*Note:\*\* If supporting multiple carets this will not check for any
overlap. See
`merge_overlapping_carets()<class_TextEdit_method_merge_overlapping_carets>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_gutter_clickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gutter_clickable**(gutter: `int<class_int>`{.interpreted-text
role="ref"}, clickable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TextEdit_method_set_gutter_clickable>`{.interpreted-text
role="ref"}

If `true`, the mouse cursor will change to a pointing hand
(`Control.CURSOR_POINTING_HAND<class_Control_constant_CURSOR_POINTING_HAND>`{.interpreted-text
role="ref"}) when hovering over the gutter at the given index. See
`is_gutter_clickable()<class_TextEdit_method_is_gutter_clickable>`{.interpreted-text
role="ref"} and
`set_line_gutter_clickable()<class_TextEdit_method_set_line_gutter_clickable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_gutter_custom_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gutter_custom_draw**(column: `int<class_int>`{.interpreted-text
role="ref"}, draw_callback: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_TextEdit_method_set_gutter_custom_draw>`{.interpreted-text
role="ref"}

Set a custom draw callback for the gutter at the given index.
`draw_callback` must take the following arguments: A line index
`int<class_int>`{.interpreted-text role="ref"}, a gutter index
`int<class_int>`{.interpreted-text role="ref"}, and an area
`Rect2<class_Rect2>`{.interpreted-text role="ref"}. This callback only
works when the gutter type is
`GUTTER_TYPE_CUSTOM<class_TextEdit_constant_GUTTER_TYPE_CUSTOM>`{.interpreted-text
role="ref"} (see
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_gutter_draw}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gutter_draw**(gutter: `int<class_int>`{.interpreted-text
role="ref"}, draw: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_gutter_draw>`{.interpreted-text
role="ref"}

If `true`, the gutter at the given index is drawn. The gutter type
(`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}) determines how it is drawn. See
`is_gutter_drawn()<class_TextEdit_method_is_gutter_drawn>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_gutter_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gutter_name**(gutter: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_gutter_name>`{.interpreted-text
role="ref"}

Sets the name of the gutter at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_gutter_overwritable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gutter_overwritable**(gutter: `int<class_int>`{.interpreted-text
role="ref"}, overwritable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_TextEdit_method_set_gutter_overwritable>`{.interpreted-text
role="ref"}

If `true`, the line data of the gutter at the given index can be
overridden when using
`merge_gutters()<class_TextEdit_method_merge_gutters>`{.interpreted-text
role="ref"}. See
`is_gutter_overwritable()<class_TextEdit_method_is_gutter_overwritable>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_gutter_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gutter_type**(gutter: `int<class_int>`{.interpreted-text
role="ref"}, type:
`GutterType<enum_TextEdit_GutterType>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}

Sets the type of gutter at the given index. Gutters can contain icons,
text, or custom visuals.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_gutter_width}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_gutter_width**(gutter: `int<class_int>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_gutter_width>`{.interpreted-text
role="ref"}

Set the width of the gutter at the given index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line**(line: `int<class_int>`{.interpreted-text role="ref"},
new_text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_line>`{.interpreted-text role="ref"}

Sets the text for a specific `line`.

Carets on the line will attempt to keep their visual x position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_as_center_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_as_center_visible**(line: `int<class_int>`{.interpreted-text
role="ref"}, wrap_index: `int<class_int>`{.interpreted-text role="ref"}
= 0)
`🔗<class_TextEdit_method_set_line_as_center_visible>`{.interpreted-text
role="ref"}

Positions the `wrap_index` of `line` at the center of the viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_as_first_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_as_first_visible**(line: `int<class_int>`{.interpreted-text
role="ref"}, wrap_index: `int<class_int>`{.interpreted-text role="ref"}
= 0)
`🔗<class_TextEdit_method_set_line_as_first_visible>`{.interpreted-text
role="ref"}

Positions the `wrap_index` of `line` at the top of the viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_as_last_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_as_last_visible**(line: `int<class_int>`{.interpreted-text
role="ref"}, wrap_index: `int<class_int>`{.interpreted-text role="ref"}
= 0)
`🔗<class_TextEdit_method_set_line_as_last_visible>`{.interpreted-text
role="ref"}

Positions the `wrap_index` of `line` at the bottom of the viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_background_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_background_color**(line: `int<class_int>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_line_background_color>`{.interpreted-text
role="ref"}

Sets the custom background color of the given line. If transparent, this
color is applied on top of the default background color (See
`background_color<class_TextEdit_theme_color_background_color>`{.interpreted-text
role="ref"}). If set to `Color(0, 0, 0, 0)`, no additional color is
applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_gutter_clickable}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_gutter_clickable**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"},
clickable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_line_gutter_clickable>`{.interpreted-text
role="ref"}

If `clickable` is `true`, makes the `gutter` on the given `line`
clickable. This is like
`set_gutter_clickable()<class_TextEdit_method_set_gutter_clickable>`{.interpreted-text
role="ref"}, but for a single line. If
`is_gutter_clickable()<class_TextEdit_method_is_gutter_clickable>`{.interpreted-text
role="ref"} is `true`, this will not have any effect. See
`is_line_gutter_clickable()<class_TextEdit_method_is_line_gutter_clickable>`{.interpreted-text
role="ref"} and
`gutter_clicked<class_TextEdit_signal_gutter_clicked>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_gutter_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_gutter_icon**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"},
icon: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_line_gutter_icon>`{.interpreted-text
role="ref"}

Sets the icon for `gutter` on `line` to `icon`. This only works when the
gutter type is
`GUTTER_TYPE_ICON<class_TextEdit_constant_GUTTER_TYPE_ICON>`{.interpreted-text
role="ref"} (see
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_gutter_item_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_gutter_item_color**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"},
color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_line_gutter_item_color>`{.interpreted-text
role="ref"}

Sets the color for `gutter` on `line` to `color`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_gutter_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_gutter_metadata**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"},
metadata: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_line_gutter_metadata>`{.interpreted-text
role="ref"}

Sets the metadata for `gutter` on `line` to `metadata`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_line_gutter_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_gutter_text**(line: `int<class_int>`{.interpreted-text
role="ref"}, gutter: `int<class_int>`{.interpreted-text role="ref"},
text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_line_gutter_text>`{.interpreted-text
role="ref"}

Sets the text for `gutter` on `line` to `text`. This only works when the
gutter type is
`GUTTER_TYPE_STRING<class_TextEdit_constant_GUTTER_TYPE_STRING>`{.interpreted-text
role="ref"} (see
`set_gutter_type()<class_TextEdit_method_set_gutter_type>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_overtype_mode_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_overtype_mode_enabled**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_overtype_mode_enabled>`{.interpreted-text
role="ref"}

If `true`, enables overtype mode. In this mode, typing overrides
existing text instead of inserting text. The
`ProjectSettings.input/ui_text_toggle_insert_mode<class_ProjectSettings_property_input/ui_text_toggle_insert_mode>`{.interpreted-text
role="ref"} action toggles overtype mode. See
`is_overtype_mode_enabled()<class_TextEdit_method_is_overtype_mode_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_search_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_search_flags**(flags: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_TextEdit_method_set_search_flags>`{.interpreted-text
role="ref"}

Sets the search `flags`. This is used with
`set_search_text()<class_TextEdit_method_set_search_text>`{.interpreted-text
role="ref"} to highlight occurrences of the searched text. Search flags
can be specified from the
`SearchFlags<enum_TextEdit_SearchFlags>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_search_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_search_text**(search_text:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_search_text>`{.interpreted-text
role="ref"}

Sets the search text. See
`set_search_flags()<class_TextEdit_method_set_search_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_selection_mode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selection_mode**(mode:
`SelectionMode<enum_TextEdit_SelectionMode>`{.interpreted-text
role="ref"})
`🔗<class_TextEdit_method_set_selection_mode>`{.interpreted-text
role="ref"}

Sets the current selection mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_selection_origin_column}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selection_origin_column**(column:
`int<class_int>`{.interpreted-text role="ref"}, caret_index:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_TextEdit_method_set_selection_origin_column>`{.interpreted-text
role="ref"}

Sets the selection origin column to the `column` for the given
`caret_index`. If the selection origin is moved to the caret position,
the selection will deselect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_selection_origin_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_selection_origin_line**(line: `int<class_int>`{.interpreted-text
role="ref"}, can_be_hidden: `bool<class_bool>`{.interpreted-text
role="ref"} = true, wrap_index: `int<class_int>`{.interpreted-text
role="ref"} = -1, caret_index: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`🔗<class_TextEdit_method_set_selection_origin_line>`{.interpreted-text
role="ref"}

Sets the selection origin line to the `line` for the given
`caret_index`. If the selection origin is moved to the caret position,
the selection will deselect.

If `can_be_hidden` is `false`, The line will be set to the nearest
unhidden line below or above.

If `wrap_index` is `-1`, the selection origin column will be clamped to
the `line`\'s length. If `wrap_index` is greater than `-1`, the column
will be moved to attempt to match the visual x position on the line\'s
`wrap_index` to the position from the last time
`set_selection_origin_column()<class_TextEdit_method_set_selection_origin_column>`{.interpreted-text
role="ref"} or
`select()<class_TextEdit_method_select>`{.interpreted-text role="ref"}
was called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_tab_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tab_size**(size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_tab_size>`{.interpreted-text role="ref"}

Sets the tab size for the **TextEdit** to use.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_set_tooltip_request_func}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_tooltip_request_func**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_set_tooltip_request_func>`{.interpreted-text
role="ref"}

Provide custom tooltip text. The callback method must take the following
args: `hovered_word: String`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_skip_selection_for_next_occurrence}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**skip_selection_for_next_occurrence**()
`🔗<class_TextEdit_method_skip_selection_for_next_occurrence>`{.interpreted-text
role="ref"}

Moves a selection and a caret for the next occurrence of the current
selection. If there is no active selection, moves to the next occurrence
of the word under caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_start_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start_action**(action:
`EditAction<enum_TextEdit_EditAction>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_start_action>`{.interpreted-text role="ref"}

Starts an action, will end the current action if `action` is different.

An action will also end after a call to
`end_action()<class_TextEdit_method_end_action>`{.interpreted-text
role="ref"}, after
`ProjectSettings.gui/timers/text_edit_idle_detect_sec<class_ProjectSettings_property_gui/timers/text_edit_idle_detect_sec>`{.interpreted-text
role="ref"} is triggered or a new undoable step outside the
`start_action()<class_TextEdit_method_start_action>`{.interpreted-text
role="ref"} and
`end_action()<class_TextEdit_method_end_action>`{.interpreted-text
role="ref"} calls.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_swap_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**swap_lines**(from_line: `int<class_int>`{.interpreted-text
role="ref"}, to_line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_TextEdit_method_swap_lines>`{.interpreted-text role="ref"}

Swaps the two lines. Carets will be swapped with the lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_tag_saved_version}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**tag_saved_version**()
`🔗<class_TextEdit_method_tag_saved_version>`{.interpreted-text
role="ref"}

Tag the current version as saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_method_undo}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **undo**()
`🔗<class_TextEdit_method_undo>`{.interpreted-text role="ref"}

Perform undo operation.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_TextEdit_theme_color_background_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **background_color**
= `Color(0, 0, 0, 0)`
`🔗<class_TextEdit_theme_color_background_color>`{.interpreted-text
role="ref"}

Sets the background `Color<class_Color>`{.interpreted-text role="ref"}
of this **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_caret_background_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**caret_background_color** = `Color(0, 0, 0, 1)`
`🔗<class_TextEdit_theme_color_caret_background_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the text behind
the caret when using a block caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_caret_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **caret_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_TextEdit_theme_color_caret_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the caret. This
can be set to a fully transparent color to hide the caret entirely.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_current_line_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**current_line_color** = `Color(0.25, 0.25, 0.26, 0.8)`
`🔗<class_TextEdit_theme_color_current_line_color>`{.interpreted-text
role="ref"}

Background `Color<class_Color>`{.interpreted-text role="ref"} of the
line containing the caret.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_TextEdit_theme_color_font_color>`{.interpreted-text
role="ref"}

Sets the font `Color<class_Color>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_TextEdit_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_font_placeholder_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)`
`🔗<class_TextEdit_theme_color_font_placeholder_color>`{.interpreted-text
role="ref"}

Font color for
`placeholder_text<class_TextEdit_property_placeholder_text>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_font_readonly_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_readonly_color** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_TextEdit_theme_color_font_readonly_color>`{.interpreted-text
role="ref"}

Sets the font `Color<class_Color>`{.interpreted-text role="ref"} when
`editable<class_TextEdit_property_editable>`{.interpreted-text
role="ref"} is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_font_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_selected_color** = `Color(0, 0, 0, 0)`
`🔗<class_TextEdit_theme_color_font_selected_color>`{.interpreted-text
role="ref"}

Sets the `Color<class_Color>`{.interpreted-text role="ref"} of the
selected text. If equal to `Color(0, 0, 0, 0)`, it will be ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_search_result_border_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**search_result_border_color** = `Color(0.3, 0.3, 0.3, 0.4)`
`🔗<class_TextEdit_theme_color_search_result_border_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the border around
text that matches the search query.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_search_result_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**search_result_color** = `Color(0.3, 0.3, 0.3, 1)`
`🔗<class_TextEdit_theme_color_search_result_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} behind the text that
matches the search query.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_selection_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **selection_color** =
`Color(0.5, 0.5, 0.5, 1)`
`🔗<class_TextEdit_theme_color_selection_color>`{.interpreted-text
role="ref"}

Sets the highlight `Color<class_Color>`{.interpreted-text role="ref"} of
text selections.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_color_word_highlighted_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**word_highlighted_color** = `Color(0.5, 0.5, 0.5, 0.25)`
`🔗<class_TextEdit_theme_color_word_highlighted_color>`{.interpreted-text
role="ref"}

Sets the highlight `Color<class_Color>`{.interpreted-text role="ref"} of
multiple occurrences.
`highlight_all_occurrences<class_TextEdit_property_highlight_all_occurrences>`{.interpreted-text
role="ref"} has to be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_constant_caret_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **caret_width** = `1`
`🔗<class_TextEdit_theme_constant_caret_width>`{.interpreted-text
role="ref"}

The caret\'s width in pixels. Greater values can be used to improve
accessibility by ensuring the caret is easily visible, or to ensure
consistency with a large font size. If set to `0` or lower, the caret
width is automatically set to 1 pixel and multiplied by the display
scaling factor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_constant_line_spacing}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **line_spacing** = `4`
`🔗<class_TextEdit_theme_constant_line_spacing>`{.interpreted-text
role="ref"}

Additional vertical spacing between lines (in pixels), spacing is added
to line descent. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_TextEdit_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_TextEdit_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_TextEdit_theme_font_font>`{.interpreted-text role="ref"}

Sets the default `Font<class_Font>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_TextEdit_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Sets default font size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_icon_space}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **space**
`🔗<class_TextEdit_theme_icon_space>`{.interpreted-text role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
for space text characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_icon_tab}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **tab**
`🔗<class_TextEdit_theme_icon_tab>`{.interpreted-text role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
for tab text characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_TextEdit_theme_style_focus>`{.interpreted-text role="ref"}

Sets the `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} when
in focus. The
`focus<class_TextEdit_theme_style_focus>`{.interpreted-text role="ref"}
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} is displayed
*over* the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"}, so a partially transparent
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} should be used
to ensure the base `StyleBox<class_StyleBox>`{.interpreted-text
role="ref"} remains visible. A
`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} that represents
an outline or an underline works well for this purpose. To disable the
focus visual effect, assign a
`StyleBoxEmpty<class_StyleBoxEmpty>`{.interpreted-text role="ref"}
resource. Note that disabling the focus visual effect will harm
keyboard/controller navigation usability, so this is not recommended for
accessibility reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_style_normal}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **normal**
`🔗<class_TextEdit_theme_style_normal>`{.interpreted-text role="ref"}

Sets the `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} of
this **TextEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_TextEdit_theme_style_read_only}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **read_only**
`🔗<class_TextEdit_theme_style_read_only>`{.interpreted-text role="ref"}

Sets the `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} of
this **TextEdit** when
`editable<class_TextEdit_property_editable>`{.interpreted-text
role="ref"} is disabled.
