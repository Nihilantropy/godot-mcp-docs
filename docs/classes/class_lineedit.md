github_url
:   hide

::: {.meta keywords="text, input"}
:::

# LineEdit {#class_LineEdit}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An input field for single-line text.

::: rst-class
classref-introduction-group
:::

## Description

**LineEdit** provides an input field for editing a single line of text.

- When the **LineEdit** control is focused using the keyboard arrow
  keys, it will only gain focus and not enter edit mode.
- To enter edit mode, click on the control with the mouse, see also
  `keep_editing_on_text_submit<class_LineEdit_property_keep_editing_on_text_submit>`{.interpreted-text
  role="ref"}.
- To exit edit mode, press `ui_text_submit` or `ui_cancel` (by default
  `Escape`{.interpreted-text role="kbd"}) actions.
- Check `edit()<class_LineEdit_method_edit>`{.interpreted-text
  role="ref"},
  `unedit()<class_LineEdit_method_unedit>`{.interpreted-text
  role="ref"},
  `is_editing()<class_LineEdit_method_is_editing>`{.interpreted-text
  role="ref"}, and
  `editing_toggled<class_LineEdit_signal_editing_toggled>`{.interpreted-text
  role="ref"} for more information.

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

\*\*Important:\*\*

- Focusing the **LineEdit** with `ui_focus_next` (by default
  `Tab`{.interpreted-text role="kbd"}) or `ui_focus_prev` (by default
  `Shift + Tab`{.interpreted-text role="kbd"}) or
  `Control.grab_focus()<class_Control_method_grab_focus>`{.interpreted-text
  role="ref"} still enters edit mode (for compatibility).

\*\*LineEdit\*\* features many built-in shortcuts that are always
available (`Ctrl`{.interpreted-text role="kbd"} here maps to
`Cmd`{.interpreted-text role="kbd"} on macOS):

- `Ctrl + C`{.interpreted-text role="kbd"}: Copy
- `Ctrl + X`{.interpreted-text role="kbd"}: Cut
- `Ctrl + V`{.interpreted-text role="kbd"} or
  `Ctrl + Y`{.interpreted-text role="kbd"}: Paste/\"yank\"
- `Ctrl + Z`{.interpreted-text role="kbd"}: Undo
- `Ctrl + ~`{.interpreted-text role="kbd"}: Swap input direction.
- `Ctrl + Shift + Z`{.interpreted-text role="kbd"}: Redo
- `Ctrl + U`{.interpreted-text role="kbd"}: Delete text from the caret
  position to the beginning of the line
- `Ctrl + K`{.interpreted-text role="kbd"}: Delete text from the caret
  position to the end of the line
- `Ctrl + A`{.interpreted-text role="kbd"}: Select all text
- `Up Arrow`{.interpreted-text
  role="kbd"}/`Down Arrow`{.interpreted-text role="kbd"}: Move the caret
  to the beginning/end of the line

On macOS, some extra keyboard shortcuts are available:

- `Cmd + F`{.interpreted-text role="kbd"}: Same as
  `Right Arrow`{.interpreted-text role="kbd"}, move the caret one
  character right
- `Cmd + B`{.interpreted-text role="kbd"}: Same as
  `Left Arrow`{.interpreted-text role="kbd"}, move the caret one
  character left
- `Cmd + P`{.interpreted-text role="kbd"}: Same as
  `Up Arrow`{.interpreted-text role="kbd"}, move the caret to the
  previous line
- `Cmd + N`{.interpreted-text role="kbd"}: Same as
  `Down Arrow`{.interpreted-text role="kbd"}, move the caret to the next
  line
- `Cmd + D`{.interpreted-text role="kbd"}: Same as
  `Delete`{.interpreted-text role="kbd"}, delete the character on the
  right side of caret
- `Cmd + H`{.interpreted-text role="kbd"}: Same as
  `Backspace`{.interpreted-text role="kbd"}, delete the character on the
  left side of the caret
- `Cmd + A`{.interpreted-text role="kbd"}: Same as
  `Home`{.interpreted-text role="kbd"}, move the caret to the beginning
  of the line
- `Cmd + E`{.interpreted-text role="kbd"}: Same as
  `End`{.interpreted-text role="kbd"}, move the caret to the end of the
  line
- `Cmd + Left Arrow`{.interpreted-text role="kbd"}: Same as
  `Home`{.interpreted-text role="kbd"}, move the caret to the beginning
  of the line
- `Cmd + Right Arrow`{.interpreted-text role="kbd"}: Same as
  `End`{.interpreted-text role="kbd"}, move the caret to the end of the
  line

\*\*Note:\*\* Caret movement shortcuts listed above are not affected by
`shortcut_keys_enabled<class_LineEdit_property_shortcut_keys_enabled>`{.interpreted-text
role="ref"}.

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

:::: {#class_LineEdit_signal_editing_toggled}
::: rst-class
classref-signal
:::
::::

**editing_toggled**(toggled_on: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_LineEdit_signal_editing_toggled>`{.interpreted-text
role="ref"}

Emitted when the **LineEdit** switches in or out of edit mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_signal_text_change_rejected}
::: rst-class
classref-signal
:::
::::

**text_change_rejected**(rejected_substring:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_LineEdit_signal_text_change_rejected>`{.interpreted-text
role="ref"}

Emitted when appending text that overflows the
`max_length<class_LineEdit_property_max_length>`{.interpreted-text
role="ref"}. The appended text is truncated to fit
`max_length<class_LineEdit_property_max_length>`{.interpreted-text
role="ref"}, and the part that couldn\'t fit is passed as the
`rejected_substring` argument.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_signal_text_changed}
::: rst-class
classref-signal
:::
::::

**text_changed**(new_text: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_LineEdit_signal_text_changed>`{.interpreted-text
role="ref"}

Emitted when the text changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_signal_text_submitted}
::: rst-class
classref-signal
:::
::::

**text_submitted**(new_text: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_LineEdit_signal_text_submitted>`{.interpreted-text role="ref"}

Emitted when the user presses the `ui_text_submit` action (by default:
`Enter`{.interpreted-text role="kbd"} or `Kp Enter`{.interpreted-text
role="kbd"}) while the **LineEdit** has focus.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_LineEdit_MenuItems}
::: rst-class
classref-enumeration
:::
::::

enum **MenuItems**: `🔗<enum_LineEdit_MenuItems>`{.interpreted-text
role="ref"}

:::: {#class_LineEdit_constant_MENU_CUT}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_CUT** = `0`

Cuts (copies and clears) the selected text.

:::: {#class_LineEdit_constant_MENU_COPY}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_COPY** = `1`

Copies the selected text.

:::: {#class_LineEdit_constant_MENU_PASTE}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_PASTE** = `2`

Pastes the clipboard text over the selected text (or at the caret\'s
position).

Non-printable escape characters are automatically stripped from the OS
clipboard via
`String.strip_escapes()<class_String_method_strip_escapes>`{.interpreted-text
role="ref"}.

:::: {#class_LineEdit_constant_MENU_CLEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_CLEAR** = `3`

Erases the whole **LineEdit** text.

:::: {#class_LineEdit_constant_MENU_SELECT_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_SELECT_ALL** = `4`

Selects the whole **LineEdit** text.

:::: {#class_LineEdit_constant_MENU_UNDO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_UNDO** = `5`

Undoes the previous action.

:::: {#class_LineEdit_constant_MENU_REDO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_REDO** = `6`

Reverse the last undo action.

:::: {#class_LineEdit_constant_MENU_SUBMENU_TEXT_DIR}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_SUBMENU_TEXT_DIR** = `7`

ID of \"Text Writing Direction\" submenu.

:::: {#class_LineEdit_constant_MENU_DIR_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_INHERITED** = `8`

Sets text direction to inherited.

:::: {#class_LineEdit_constant_MENU_DIR_AUTO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_AUTO** = `9`

Sets text direction to automatic.

:::: {#class_LineEdit_constant_MENU_DIR_LTR}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_LTR** = `10`

Sets text direction to left-to-right.

:::: {#class_LineEdit_constant_MENU_DIR_RTL}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DIR_RTL** = `11`

Sets text direction to right-to-left.

:::: {#class_LineEdit_constant_MENU_DISPLAY_UCC}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_DISPLAY_UCC** = `12`

Toggles control character display.

:::: {#class_LineEdit_constant_MENU_SUBMENU_INSERT_UCC}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_SUBMENU_INSERT_UCC** = `13`

ID of \"Insert Control Character\" submenu.

:::: {#class_LineEdit_constant_MENU_INSERT_LRM}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRM** = `14`

Inserts left-to-right mark (LRM) character.

:::: {#class_LineEdit_constant_MENU_INSERT_RLM}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLM** = `15`

Inserts right-to-left mark (RLM) character.

:::: {#class_LineEdit_constant_MENU_INSERT_LRE}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRE** = `16`

Inserts start of left-to-right embedding (LRE) character.

:::: {#class_LineEdit_constant_MENU_INSERT_RLE}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLE** = `17`

Inserts start of right-to-left embedding (RLE) character.

:::: {#class_LineEdit_constant_MENU_INSERT_LRO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRO** = `18`

Inserts start of left-to-right override (LRO) character.

:::: {#class_LineEdit_constant_MENU_INSERT_RLO}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLO** = `19`

Inserts start of right-to-left override (RLO) character.

:::: {#class_LineEdit_constant_MENU_INSERT_PDF}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_PDF** = `20`

Inserts pop direction formatting (PDF) character.

:::: {#class_LineEdit_constant_MENU_INSERT_ALM}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_ALM** = `21`

Inserts Arabic letter mark (ALM) character.

:::: {#class_LineEdit_constant_MENU_INSERT_LRI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_LRI** = `22`

Inserts left-to-right isolate (LRI) character.

:::: {#class_LineEdit_constant_MENU_INSERT_RLI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_RLI** = `23`

Inserts right-to-left isolate (RLI) character.

:::: {#class_LineEdit_constant_MENU_INSERT_FSI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_FSI** = `24`

Inserts first strong isolate (FSI) character.

:::: {#class_LineEdit_constant_MENU_INSERT_PDI}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_PDI** = `25`

Inserts pop direction isolate (PDI) character.

:::: {#class_LineEdit_constant_MENU_INSERT_ZWJ}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_ZWJ** = `26`

Inserts zero width joiner (ZWJ) character.

:::: {#class_LineEdit_constant_MENU_INSERT_ZWNJ}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_ZWNJ** = `27`

Inserts zero width non-joiner (ZWNJ) character.

:::: {#class_LineEdit_constant_MENU_INSERT_WJ}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_WJ** = `28`

Inserts word joiner (WJ) character.

:::: {#class_LineEdit_constant_MENU_INSERT_SHY}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_INSERT_SHY** = `29`

Inserts soft hyphen (SHY) character.

:::: {#class_LineEdit_constant_MENU_EMOJI_AND_SYMBOL}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_EMOJI_AND_SYMBOL** = `30`

Opens system emoji and symbol picker.

:::: {#class_LineEdit_constant_MENU_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}
**MENU_MAX** = `31`

Represents the size of the
`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_LineEdit_VirtualKeyboardType}
::: rst-class
classref-enumeration
:::
::::

enum **VirtualKeyboardType**:
`🔗<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text role="ref"}

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_DEFAULT** = `0`

Default text virtual keyboard.

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_MULTILINE}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_MULTILINE** = `1`

Multiline virtual keyboard.

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_NUMBER}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_NUMBER** = `2`

Virtual number keypad, useful for PIN entry.

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_NUMBER_DECIMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_NUMBER_DECIMAL** = `3`

Virtual number keypad, useful for entering fractional numbers.

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_PHONE}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_PHONE** = `4`

Virtual phone number keypad.

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_EMAIL_ADDRESS}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_EMAIL_ADDRESS** = `5`

Virtual keyboard with additional keys to assist with typing email
addresses.

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_PASSWORD}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_PASSWORD** = `6`

Virtual keyboard for entering a password. On most platforms, this should
disable autocomplete and autocapitalization.

\*\*Note:\*\* This is not supported on Web. Instead, this behaves
identically to
`KEYBOARD_TYPE_DEFAULT<class_LineEdit_constant_KEYBOARD_TYPE_DEFAULT>`{.interpreted-text
role="ref"}.

:::: {#class_LineEdit_constant_KEYBOARD_TYPE_URL}
::: rst-class
classref-enumeration-constant
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **KEYBOARD_TYPE_URL** = `7`

Virtual keyboard with additional keys to assist with typing URLs.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_LineEdit_property_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **alignment** = `0`
`🔗<class_LineEdit_property_alignment>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_alignment**(value:
  `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"})
- `HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
  role="ref"} **get_horizontal_alignment**()

Text alignment as defined in the
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_backspace_deletes_composite_character_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**backspace_deletes_composite_character_enabled** = `false`
`🔗<class_LineEdit_property_backspace_deletes_composite_character_enabled>`{.interpreted-text
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
`caret_mid_grapheme<class_LineEdit_property_caret_mid_grapheme>`{.interpreted-text
role="ref"} is `false`, backspace deletes an entire composite character
such as ❤️‍🩹, instead of deleting part of the composite character.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_caret_blink}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **caret_blink** =
`false` `🔗<class_LineEdit_property_caret_blink>`{.interpreted-text
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

:::: {#class_LineEdit_property_caret_blink_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**caret_blink_interval** = `0.65`
`🔗<class_LineEdit_property_caret_blink_interval>`{.interpreted-text
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

:::: {#class_LineEdit_property_caret_column}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **caret_column** = `0`
`🔗<class_LineEdit_property_caret_column>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_caret_column**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_caret_column**()

The caret\'s column position inside the **LineEdit**. When set, the text
may scroll to accommodate it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_caret_force_displayed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**caret_force_displayed** = `false`
`🔗<class_LineEdit_property_caret_force_displayed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_caret_force_displayed**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_caret_force_displayed**()

If `true`, the **LineEdit** will always show the caret, even if not
editing or focus is lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_caret_mid_grapheme}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **caret_mid_grapheme**
= `false`
`🔗<class_LineEdit_property_caret_mid_grapheme>`{.interpreted-text
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

:::: {#class_LineEdit_property_clear_button_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**clear_button_enabled** = `false`
`🔗<class_LineEdit_property_clear_button_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_clear_button_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_clear_button_enabled**()

If `true`, the **LineEdit** will show a clear button if
`text<class_LineEdit_property_text>`{.interpreted-text role="ref"} is
not empty, which can be used to clear the text quickly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_context_menu_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**context_menu_enabled** = `true`
`🔗<class_LineEdit_property_context_menu_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_context_menu_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_context_menu_enabled**()

If `true`, the context menu will appear when right-clicked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_deselect_on_focus_loss_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**deselect_on_focus_loss_enabled** = `true`
`🔗<class_LineEdit_property_deselect_on_focus_loss_enabled>`{.interpreted-text
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

:::: {#class_LineEdit_property_drag_and_drop_selection_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**drag_and_drop_selection_enabled** = `true`
`🔗<class_LineEdit_property_drag_and_drop_selection_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_drag_and_drop_selection_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drag_and_drop_selection_enabled**()

If `true`, allow drag and drop of selected text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_draw_control_chars}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **draw_control_chars**
= `false`
`🔗<class_LineEdit_property_draw_control_chars>`{.interpreted-text
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

:::: {#class_LineEdit_property_editable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **editable** = `true`
`🔗<class_LineEdit_property_editable>`{.interpreted-text role="ref"}

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

:::: {#class_LineEdit_property_emoji_menu_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **emoji_menu_enabled**
= `true`
`🔗<class_LineEdit_property_emoji_menu_enabled>`{.interpreted-text
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

:::: {#class_LineEdit_property_expand_to_text_length}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**expand_to_text_length** = `false`
`🔗<class_LineEdit_property_expand_to_text_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expand_to_text_length_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_expand_to_text_length_enabled**()

If `true`, the **LineEdit** width will increase to stay longer than the
`text<class_LineEdit_property_text>`{.interpreted-text role="ref"}. It
will **not** compress if the
`text<class_LineEdit_property_text>`{.interpreted-text role="ref"} is
shortened.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_flat}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **flat** = `false`
`🔗<class_LineEdit_property_flat>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flat**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_flat**()

If `true`, the **LineEdit** doesn\'t display decoration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_keep_editing_on_text_submit}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**keep_editing_on_text_submit** = `false`
`🔗<class_LineEdit_property_keep_editing_on_text_submit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_editing_on_text_submit**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_editing_kept_on_text_submit**()

If `true`, the **LineEdit** will not exit edit mode when text is
submitted by pressing `ui_text_submit` action (by default:
`Enter`{.interpreted-text role="kbd"} or `Kp Enter`{.interpreted-text
role="kbd"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_LineEdit_property_language>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_language**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_language**()

Language code used for line-breaking and text shaping algorithms. If
left empty, current locale is used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_max_length}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_length** = `0`
`🔗<class_LineEdit_property_max_length>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_length**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_length**()

Maximum number of characters that can be entered inside the
**LineEdit**. If `0`, there is no limit.

When a limit is defined, characters that would exceed
`max_length<class_LineEdit_property_max_length>`{.interpreted-text
role="ref"} are truncated. This happens both for existing
`text<class_LineEdit_property_text>`{.interpreted-text role="ref"}
contents when setting the max length, or for new text inserted in the
**LineEdit**, including pasting.

If any input text is truncated, the
`text_change_rejected<class_LineEdit_signal_text_change_rejected>`{.interpreted-text
role="ref"} signal is emitted with the truncated substring as a
parameter:

::::: tabs
::: code-tab
gdscript

text = \"Hello world\" max_length = 5 \# [text]{.title-ref} becomes
\"Hello\". max_length = 10 text += \" goodbye\" \# [text]{.title-ref}
becomes \"Hello good\". \# [text_change_rejected]{.title-ref} is emitted
with \"bye\" as a parameter.
:::

::: code-tab
csharp

Text = \"Hello world\"; MaxLength = 5; // [Text]{.title-ref} becomes
\"Hello\". MaxLength = 10; Text += \" goodbye\"; // [Text]{.title-ref}
becomes \"Hello good\". // [text_change_rejected]{.title-ref} is emitted
with \"bye\" as a parameter.
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_middle_mouse_paste_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**middle_mouse_paste_enabled** = `true`
`🔗<class_LineEdit_property_middle_mouse_paste_enabled>`{.interpreted-text
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

:::: {#class_LineEdit_property_placeholder_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**placeholder_text** = `""`
`🔗<class_LineEdit_property_placeholder_text>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_placeholder**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_placeholder**()

Text shown when the **LineEdit** is empty. It is **not** the
**LineEdit**\'s default value (see
`text<class_LineEdit_property_text>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_right_icon}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**right_icon**
`🔗<class_LineEdit_property_right_icon>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_right_icon**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_right_icon**()

Sets the icon that will appear in the right end of the **LineEdit** if
there\'s no `text<class_LineEdit_property_text>`{.interpreted-text
role="ref"}, or always, if
`clear_button_enabled<class_LineEdit_property_clear_button_enabled>`{.interpreted-text
role="ref"} is set to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_secret}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **secret** = `false`
`🔗<class_LineEdit_property_secret>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secret**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_secret**()

If `true`, every character is replaced with the secret character (see
`secret_character<class_LineEdit_property_secret_character>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_secret_character}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**secret_character** = `"•"`
`🔗<class_LineEdit_property_secret_character>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_secret_character**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_secret_character**()

The character to use to mask secret input. Only a single character can
be used as the secret character. If it is longer than one character,
only the first one will be used. If it is empty, a space will be used
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_select_all_on_focus}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **select_all_on_focus**
= `false`
`🔗<class_LineEdit_property_select_all_on_focus>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_select_all_on_focus**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_select_all_on_focus**()

If `true`, the **LineEdit** will select the whole text when it gains
focus.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_selecting_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **selecting_enabled** =
`true` `🔗<class_LineEdit_property_selecting_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_selecting_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_selecting_enabled**()

If `false`, it\'s impossible to select the text using mouse nor
keyboard.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_shortcut_keys_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shortcut_keys_enabled** = `true`
`🔗<class_LineEdit_property_shortcut_keys_enabled>`{.interpreted-text
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

:::: {#class_LineEdit_property_structured_text_bidi_override}
::: rst-class
classref-property
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **structured_text_bidi_override** = `0`
`🔗<class_LineEdit_property_structured_text_bidi_override>`{.interpreted-text
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

:::: {#class_LineEdit_property_structured_text_bidi_override_options}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**structured_text_bidi_override_options** = `[]`
`🔗<class_LineEdit_property_structured_text_bidi_override_options>`{.interpreted-text
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

:::: {#class_LineEdit_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_LineEdit_property_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_text**()

String value of the **LineEdit**.

\*\*Note:\*\* Changing text using this property won\'t emit the
`text_changed<class_LineEdit_signal_text_changed>`{.interpreted-text
role="ref"} signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_property_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **text_direction** = `0`
`🔗<class_LineEdit_property_text_direction>`{.interpreted-text
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

:::: {#class_LineEdit_property_virtual_keyboard_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**virtual_keyboard_enabled** = `true`
`🔗<class_LineEdit_property_virtual_keyboard_enabled>`{.interpreted-text
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

:::: {#class_LineEdit_property_virtual_keyboard_show_on_focus}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**virtual_keyboard_show_on_focus** = `true`
`🔗<class_LineEdit_property_virtual_keyboard_show_on_focus>`{.interpreted-text
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

:::: {#class_LineEdit_property_virtual_keyboard_type}
::: rst-class
classref-property
:::
::::

`VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
role="ref"} **virtual_keyboard_type** = `0`
`🔗<class_LineEdit_property_virtual_keyboard_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_virtual_keyboard_type**(value:
  `VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
  role="ref"})
- `VirtualKeyboardType<enum_LineEdit_VirtualKeyboardType>`{.interpreted-text
  role="ref"} **get_virtual_keyboard_type**()

Specifies the type of virtual keyboard to show.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_LineEdit_method_apply_ime}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **apply_ime**()
`🔗<class_LineEdit_method_apply_ime>`{.interpreted-text role="ref"}

Applies text from the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) (IME) and closes the
IME if it is open.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_cancel_ime}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cancel_ime**()
`🔗<class_LineEdit_method_cancel_ime>`{.interpreted-text role="ref"}

Closes the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) (IME) if it is open.
Any text in the IME will be lost.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_LineEdit_method_clear>`{.interpreted-text role="ref"}

Erases the **LineEdit**\'s
`text<class_LineEdit_property_text>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_delete_char_at_caret}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delete_char_at_caret**()
`🔗<class_LineEdit_method_delete_char_at_caret>`{.interpreted-text
role="ref"}

Deletes one character at the caret\'s current position (equivalent to
pressing `Delete`{.interpreted-text role="kbd"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_delete_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delete_text**(from_column: `int<class_int>`{.interpreted-text
role="ref"}, to_column: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_LineEdit_method_delete_text>`{.interpreted-text role="ref"}

Deletes a section of the
`text<class_LineEdit_property_text>`{.interpreted-text role="ref"} going
from position `from_column` to `to_column`. Both parameters should be
within the text\'s length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_deselect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **deselect**()
`🔗<class_LineEdit_method_deselect>`{.interpreted-text role="ref"}

Clears the current selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_edit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **edit**()
`🔗<class_LineEdit_method_edit>`{.interpreted-text role="ref"}

Allows entering edit mode whether the **LineEdit** is focused or not.

See also
`keep_editing_on_text_submit<class_LineEdit_property_keep_editing_on_text_submit>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_get_menu}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_menu**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_LineEdit_method_get_menu>`{.interpreted-text
role="ref"}

Returns the `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
of this **LineEdit**. By default, this menu is displayed when
right-clicking on the **LineEdit**.

You can add custom menu items or remove standard ones. Make sure your
IDs don\'t conflict with the standard ones (see
`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"}). For
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
menu.GetItemIndex(LineEdit.MenuItems.Redo) + 1; // Add custom items.
menu.AddSeparator(); menu.AddItem(\"Insert Date\",
LineEdit.MenuItems.Max + 1); // Add event handler. menu.IdPressed +=
OnItemPressed; }

public void OnItemPressed(int id) { if (id ==
LineEdit.MenuItems.Max + 1) {
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

:::: {#class_LineEdit_method_get_next_composite_character_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_next_composite_character_column**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LineEdit_method_get_next_composite_character_column>`{.interpreted-text
role="ref"}

Returns the correct column at the end of a composite character like ❤️‍🩹
(mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is
comprised of more than one Unicode code point, if the caret is at the
start of the composite character. Also returns the correct column with
the caret at mid grapheme and for non-composite characters.

\*\*Note:\*\* To check at caret location use
`get_next_composite_character_column(get_caret_column())`

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_get_previous_composite_character_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_previous_composite_character_column**(column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LineEdit_method_get_previous_composite_character_column>`{.interpreted-text
role="ref"}

Returns the correct column at the start of a composite character like ❤️‍🩹
(mending heart; Unicode: `U+2764 U+FE0F U+200D U+1FA79`) which is
comprised of more than one Unicode code point, if the caret is at the
end of the composite character. Also returns the correct column with the
caret at mid grapheme and for non-composite characters.

\*\*Note:\*\* To check at caret location use
`get_previous_composite_character_column(get_caret_column())`

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_get_scroll_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_scroll_offset**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LineEdit_method_get_scroll_offset>`{.interpreted-text
role="ref"}

Returns the scroll offset due to
`caret_column<class_LineEdit_property_caret_column>`{.interpreted-text
role="ref"}, as a number of characters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_get_selected_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_selected_text**()
`🔗<class_LineEdit_method_get_selected_text>`{.interpreted-text
role="ref"}

Returns the text inside the selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_get_selection_from_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_from_column**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LineEdit_method_get_selection_from_column>`{.interpreted-text
role="ref"}

Returns the selection begin column.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_get_selection_to_column}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_selection_to_column**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LineEdit_method_get_selection_to_column>`{.interpreted-text
role="ref"}

Returns the selection end column.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_has_ime_text}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_ime_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_LineEdit_method_has_ime_text>`{.interpreted-text
role="ref"}

Returns `true` if the user has text in the [Input Method
Editor](https://en.wikipedia.org/wiki/Input_method) (IME).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_has_redo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_redo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_LineEdit_method_has_redo>`{.interpreted-text
role="ref"}

Returns `true` if a \"redo\" action is available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_has_selection}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_selection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_LineEdit_method_has_selection>`{.interpreted-text
role="ref"}

Returns `true` if the user has selected text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_has_undo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_undo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_LineEdit_method_has_undo>`{.interpreted-text
role="ref"}

Returns `true` if an \"undo\" action is available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_insert_text_at_caret}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**insert_text_at_caret**(text: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_LineEdit_method_insert_text_at_caret>`{.interpreted-text
role="ref"}

Inserts `text` at the caret. If the resulting value is longer than
`max_length<class_LineEdit_property_max_length>`{.interpreted-text
role="ref"}, nothing happens.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_is_editing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_editing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_LineEdit_method_is_editing>`{.interpreted-text
role="ref"}

Returns whether the **LineEdit** is being edited.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_is_menu_visible}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_menu_visible**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_LineEdit_method_is_menu_visible>`{.interpreted-text
role="ref"}

Returns whether the menu is visible. Use this instead of
`get_menu().visible` to improve performance (so the creation of the menu
is avoided).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_menu_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**menu_option**(option: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_LineEdit_method_menu_option>`{.interpreted-text role="ref"}

Executes a given action as defined in the
`MenuItems<enum_LineEdit_MenuItems>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_select}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select**(from: `int<class_int>`{.interpreted-text role="ref"} = 0, to:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`🔗<class_LineEdit_method_select>`{.interpreted-text role="ref"}

Selects characters inside **LineEdit** between `from` and `to`. By
default, `from` is at the beginning and `to` at the end.

::::: tabs
::: code-tab
gdscript

text = \"Welcome\" select() \# Will select \"Welcome\". select(4) \#
Will select \"ome\". select(2, 5) \# Will select \"lco\".
:::

::: code-tab
csharp

Text = \"Welcome\"; Select(); // Will select \"Welcome\". Select(4); //
Will select \"ome\". Select(2, 5); // Will select \"lco\".
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_select_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select_all**()
`🔗<class_LineEdit_method_select_all>`{.interpreted-text role="ref"}

Selects the whole `String<class_String>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_method_unedit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **unedit**()
`🔗<class_LineEdit_method_unedit>`{.interpreted-text role="ref"}

Allows exiting edit mode while preserving focus.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_LineEdit_theme_color_caret_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **caret_color** =
`Color(0.95, 0.95, 0.95, 1)`
`🔗<class_LineEdit_theme_color_caret_color>`{.interpreted-text
role="ref"}

Color of the **LineEdit**\'s caret (text cursor). This can be set to a
fully transparent color to hide the caret entirely.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_clear_button_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**clear_button_color** = `Color(0.875, 0.875, 0.875, 1)`
`🔗<class_LineEdit_theme_color_clear_button_color>`{.interpreted-text
role="ref"}

Color used as default tint for the clear button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_clear_button_color_pressed}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**clear_button_color_pressed** = `Color(1, 1, 1, 1)`
`🔗<class_LineEdit_theme_color_clear_button_color_pressed>`{.interpreted-text
role="ref"}

Color used for the clear button when it\'s pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_font_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_color** =
`Color(0.875, 0.875, 0.875, 1)`
`🔗<class_LineEdit_theme_color_font_color>`{.interpreted-text
role="ref"}

Default font color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_LineEdit_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The tint of text outline of the **LineEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_font_placeholder_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_placeholder_color** = `Color(0.875, 0.875, 0.875, 0.6)`
`🔗<class_LineEdit_theme_color_font_placeholder_color>`{.interpreted-text
role="ref"}

Font color for
`placeholder_text<class_LineEdit_property_placeholder_text>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_font_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_selected_color** = `Color(1, 1, 1, 1)`
`🔗<class_LineEdit_theme_color_font_selected_color>`{.interpreted-text
role="ref"}

Font color for selected text (inside the selection rectangle).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_font_uneditable_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_uneditable_color** = `Color(0.875, 0.875, 0.875, 0.5)`
`🔗<class_LineEdit_theme_color_font_uneditable_color>`{.interpreted-text
role="ref"}

Font color when editing is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_color_selection_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **selection_color** =
`Color(0.5, 0.5, 0.5, 1)`
`🔗<class_LineEdit_theme_color_selection_color>`{.interpreted-text
role="ref"}

Color of the selection rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_constant_caret_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **caret_width** = `1`
`🔗<class_LineEdit_theme_constant_caret_width>`{.interpreted-text
role="ref"}

The caret\'s width in pixels. Greater values can be used to improve
accessibility by ensuring the caret is easily visible, or to ensure
consistency with a large font size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_constant_minimum_character_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**minimum_character_width** = `4`
`🔗<class_LineEdit_theme_constant_minimum_character_width>`{.interpreted-text
role="ref"}

Minimum horizontal space for the text (not counting the clear button and
content margins). This value is measured in count of \'M\' characters
(i.e. this number of \'M\' characters can be displayed without
scrolling).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_LineEdit_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_LineEdit_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_font_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **font**
`🔗<class_LineEdit_theme_font_font>`{.interpreted-text role="ref"}

Font used for the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_font_size_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **font_size**
`🔗<class_LineEdit_theme_font_size_font_size>`{.interpreted-text
role="ref"}

Font size of the **LineEdit**\'s text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_icon_clear}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **clear**
`🔗<class_LineEdit_theme_icon_clear>`{.interpreted-text role="ref"}

Texture for the clear button. See
`clear_button_enabled<class_LineEdit_property_clear_button_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_LineEdit_theme_style_focus>`{.interpreted-text role="ref"}

Background used when **LineEdit** has GUI focus. The
`focus<class_LineEdit_theme_style_focus>`{.interpreted-text role="ref"}
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

:::: {#class_LineEdit_theme_style_normal}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **normal**
`🔗<class_LineEdit_theme_style_normal>`{.interpreted-text role="ref"}

Default background for the **LineEdit**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_LineEdit_theme_style_read_only}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **read_only**
`🔗<class_LineEdit_theme_style_read_only>`{.interpreted-text role="ref"}

Background used when **LineEdit** is in read-only mode
(`editable<class_LineEdit_property_editable>`{.interpreted-text
role="ref"} is set to `false`).
