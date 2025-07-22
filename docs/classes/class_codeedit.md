github_url
:   hide

# CodeEdit {#class_CodeEdit}

**Inherits:** `TextEdit<class_TextEdit>`{.interpreted-text role="ref"}
**\<** `Control<class_Control>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A multiline text editor designed for editing code.

::: rst-class
classref-introduction-group
:::

## Description

CodeEdit is a specialized `TextEdit<class_TextEdit>`{.interpreted-text
role="ref"} designed for editing plain text code files. It has many
features commonly found in code editors such as line numbers, line
folding, code completion, indent management, and string/comment
management.

\*\*Note:\*\* Regardless of locale, **CodeEdit** will by default always
use left-to-right text direction to correctly display source code.

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

:::: {#class_CodeEdit_signal_breakpoint_toggled}
::: rst-class
classref-signal
:::
::::

**breakpoint_toggled**(line: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_CodeEdit_signal_breakpoint_toggled>`{.interpreted-text
role="ref"}

Emitted when a breakpoint is added or removed from a line. If the line
is removed via backspace, a signal is emitted at the old line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_signal_code_completion_requested}
::: rst-class
classref-signal
:::
::::

**code_completion_requested**()
`🔗<class_CodeEdit_signal_code_completion_requested>`{.interpreted-text
role="ref"}

Emitted when the user requests code completion. This signal will not be
sent if
`_request_code_completion()<class_CodeEdit_private_method__request_code_completion>`{.interpreted-text
role="ref"} is overridden or
`code_completion_enabled<class_CodeEdit_property_code_completion_enabled>`{.interpreted-text
role="ref"} is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_signal_symbol_hovered}
::: rst-class
classref-signal
:::
::::

**symbol_hovered**(symbol: `String<class_String>`{.interpreted-text
role="ref"}, line: `int<class_int>`{.interpreted-text role="ref"},
column: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_signal_symbol_hovered>`{.interpreted-text role="ref"}

Emitted when the user hovers over a symbol. Unlike
`Control.mouse_entered<class_Control_signal_mouse_entered>`{.interpreted-text
role="ref"}, this signal is not emitted immediately, but when the cursor
is over the symbol for
`ProjectSettings.gui/timers/tooltip_delay_sec<class_ProjectSettings_property_gui/timers/tooltip_delay_sec>`{.interpreted-text
role="ref"} seconds.

\*\*Note:\*\*
`symbol_tooltip_on_hover<class_CodeEdit_property_symbol_tooltip_on_hover>`{.interpreted-text
role="ref"} must be `true` for this signal to be emitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_signal_symbol_lookup}
::: rst-class
classref-signal
:::
::::

**symbol_lookup**(symbol: `String<class_String>`{.interpreted-text
role="ref"}, line: `int<class_int>`{.interpreted-text role="ref"},
column: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_signal_symbol_lookup>`{.interpreted-text role="ref"}

Emitted when the user has clicked on a valid symbol.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_signal_symbol_validate}
::: rst-class
classref-signal
:::
::::

**symbol_validate**(symbol: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_CodeEdit_signal_symbol_validate>`{.interpreted-text
role="ref"}

Emitted when the user hovers over a symbol. The symbol should be
validated and responded to, by calling
`set_symbol_lookup_word_as_valid()<class_CodeEdit_method_set_symbol_lookup_word_as_valid>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`symbol_lookup_on_click<class_CodeEdit_property_symbol_lookup_on_click>`{.interpreted-text
role="ref"} must be `true` for this signal to be emitted.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_CodeEdit_CodeCompletionKind}
::: rst-class
classref-enumeration
:::
::::

enum **CodeCompletionKind**:
`🔗<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text role="ref"}

:::: {#class_CodeEdit_constant_KIND_CLASS}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_CLASS** = `0`

Marks the option as a class.

:::: {#class_CodeEdit_constant_KIND_FUNCTION}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_FUNCTION** = `1`

Marks the option as a function.

:::: {#class_CodeEdit_constant_KIND_SIGNAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_SIGNAL** = `2`

Marks the option as a Godot signal.

:::: {#class_CodeEdit_constant_KIND_VARIABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_VARIABLE** = `3`

Marks the option as a variable.

:::: {#class_CodeEdit_constant_KIND_MEMBER}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_MEMBER** = `4`

Marks the option as a member.

:::: {#class_CodeEdit_constant_KIND_ENUM}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_ENUM** = `5`

Marks the option as an enum entry.

:::: {#class_CodeEdit_constant_KIND_CONSTANT}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_CONSTANT** = `6`

Marks the option as a constant.

:::: {#class_CodeEdit_constant_KIND_NODE_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_NODE_PATH** = `7`

Marks the option as a Godot node path.

:::: {#class_CodeEdit_constant_KIND_FILE_PATH}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_FILE_PATH** = `8`

Marks the option as a file path.

:::: {#class_CodeEdit_constant_KIND_PLAIN_TEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"} **KIND_PLAIN_TEXT** = `9`

Marks the option as unclassified or plain text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CodeEdit_CodeCompletionLocation}
::: rst-class
classref-enumeration
:::
::::

enum **CodeCompletionLocation**:
`🔗<enum_CodeEdit_CodeCompletionLocation>`{.interpreted-text role="ref"}

:::: {#class_CodeEdit_constant_LOCATION_LOCAL}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>`{.interpreted-text
role="ref"} **LOCATION_LOCAL** = `0`

The option is local to the location of the code completion query - e.g.
a local variable. Subsequent value of location represent options from
the outer class, the exact value represent how far they are (in terms of
inner classes).

:::: {#class_CodeEdit_constant_LOCATION_PARENT_MASK}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>`{.interpreted-text
role="ref"} **LOCATION_PARENT_MASK** = `256`

The option is from the containing class or a parent class, relative to
the location of the code completion query. Perform a bitwise OR with the
class depth (e.g. `0` for the local class, `1` for the parent, `2` for
the grandparent, etc.) to store the depth of an option in the class or a
parent class.

:::: {#class_CodeEdit_constant_LOCATION_OTHER_USER_CODE}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>`{.interpreted-text
role="ref"} **LOCATION_OTHER_USER_CODE** = `512`

The option is from user code which is not local and not in a derived
class (e.g. Autoload Singletons).

:::: {#class_CodeEdit_constant_LOCATION_OTHER}
::: rst-class
classref-enumeration-constant
:::
::::

`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>`{.interpreted-text
role="ref"} **LOCATION_OTHER** = `1024`

The option is from other engine code, not covered by the other enum
constants - e.g. built-in classes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CodeEdit_property_auto_brace_completion_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**auto_brace_completion_enabled** = `false`
`🔗<class_CodeEdit_property_auto_brace_completion_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_brace_completion_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_auto_brace_completion_enabled**()

If `true`, uses
`auto_brace_completion_pairs<class_CodeEdit_property_auto_brace_completion_pairs>`{.interpreted-text
role="ref"} to automatically insert the closing brace when the opening
brace is inserted by typing or autocompletion. Also automatically
removes the closing brace when using backspace on the opening brace.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_auto_brace_completion_highlight_matching}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**auto_brace_completion_highlight_matching** = `false`
`🔗<class_CodeEdit_property_auto_brace_completion_highlight_matching>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_highlight_matching_braces_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_highlight_matching_braces_enabled**()

If `true`, highlights brace pairs when the caret is on either one, using
`auto_brace_completion_pairs<class_CodeEdit_property_auto_brace_completion_pairs>`{.interpreted-text
role="ref"}. If matching, the pairs will be underlined. If a brace is
unmatched, it is colored with
`brace_mismatch_color<class_CodeEdit_theme_color_brace_mismatch_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_auto_brace_completion_pairs}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**auto_brace_completion_pairs** =
`{ "\"": "\"", "'": "'", "(": ")", "[": "]", "{": "}" }`
`🔗<class_CodeEdit_property_auto_brace_completion_pairs>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_brace_completion_pairs**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_auto_brace_completion_pairs**()

Sets the brace pairs to be autocompleted. For each entry in the
dictionary, the key is the opening brace and the value is the closing
brace that matches it. A brace is a
`String<class_String>`{.interpreted-text role="ref"} made of symbols.
See
`auto_brace_completion_enabled<class_CodeEdit_property_auto_brace_completion_enabled>`{.interpreted-text
role="ref"} and
`auto_brace_completion_highlight_matching<class_CodeEdit_property_auto_brace_completion_highlight_matching>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_code_completion_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**code_completion_enabled** = `false`
`🔗<class_CodeEdit_property_code_completion_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_code_completion_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_code_completion_enabled**()

If `true`, the
`ProjectSettings.input/ui_text_completion_query<class_ProjectSettings_property_input/ui_text_completion_query>`{.interpreted-text
role="ref"} action requests code completion. To handle it, see
`_request_code_completion()<class_CodeEdit_private_method__request_code_completion>`{.interpreted-text
role="ref"} or
`code_completion_requested<class_CodeEdit_signal_code_completion_requested>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_code_completion_prefixes}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**code_completion_prefixes** = `[]`
`🔗<class_CodeEdit_property_code_completion_prefixes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_code_completion_prefixes**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
  **get_code_completion_prefixes**()

Sets prefixes that will trigger code completion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_delimiter_comments}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**delimiter_comments** = `[]`
`🔗<class_CodeEdit_property_delimiter_comments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_comment_delimiters**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
  **get_comment_delimiters**()

Sets the comment delimiters. All existing comment delimiters will be
removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_delimiter_strings}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**delimiter_strings** = `["' '", "\" \""]`
`🔗<class_CodeEdit_property_delimiter_strings>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_string_delimiters**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
  **get_string_delimiters**()

Sets the string delimiters. All existing string delimiters will be
removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_gutters_draw_bookmarks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gutters_draw_bookmarks** = `false`
`🔗<class_CodeEdit_property_gutters_draw_bookmarks>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_bookmarks_gutter**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drawing_bookmarks_gutter**()

If `true`, bookmarks are drawn in the gutter. This gutter is shared with
breakpoints and executing lines. See
`set_line_as_bookmarked()<class_CodeEdit_method_set_line_as_bookmarked>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_gutters_draw_breakpoints_gutter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gutters_draw_breakpoints_gutter** = `false`
`🔗<class_CodeEdit_property_gutters_draw_breakpoints_gutter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_breakpoints_gutter**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drawing_breakpoints_gutter**()

If `true`, breakpoints are drawn in the gutter. This gutter is shared
with bookmarks and executing lines. Clicking the gutter will toggle the
breakpoint for the line, see
`set_line_as_breakpoint()<class_CodeEdit_method_set_line_as_breakpoint>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_gutters_draw_executing_lines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gutters_draw_executing_lines** = `false`
`🔗<class_CodeEdit_property_gutters_draw_executing_lines>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_executing_lines_gutter**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drawing_executing_lines_gutter**()

If `true`, executing lines are marked in the gutter. This gutter is
shared with breakpoints and bookmarks. See
`set_line_as_executing()<class_CodeEdit_method_set_line_as_executing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_gutters_draw_fold_gutter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gutters_draw_fold_gutter** = `false`
`🔗<class_CodeEdit_property_gutters_draw_fold_gutter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_fold_gutter**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_drawing_fold_gutter**()

If `true`, the fold gutter is drawn. In this gutter, the
`can_fold_code_region<class_CodeEdit_theme_icon_can_fold_code_region>`{.interpreted-text
role="ref"} icon is drawn for each foldable line (see
`can_fold_line()<class_CodeEdit_method_can_fold_line>`{.interpreted-text
role="ref"}) and the
`folded_code_region<class_CodeEdit_theme_icon_folded_code_region>`{.interpreted-text
role="ref"} icon is drawn for each folded line (see
`is_line_folded()<class_CodeEdit_method_is_line_folded>`{.interpreted-text
role="ref"}). These icons can be clicked to toggle the fold state, see
`toggle_foldable_line()<class_CodeEdit_method_toggle_foldable_line>`{.interpreted-text
role="ref"}.
`line_folding<class_CodeEdit_property_line_folding>`{.interpreted-text
role="ref"} must be `true` to show icons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_gutters_draw_line_numbers}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gutters_draw_line_numbers** = `false`
`🔗<class_CodeEdit_property_gutters_draw_line_numbers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_line_numbers**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_draw_line_numbers_enabled**()

If `true`, the line number gutter is drawn. Line numbers start at `1`
and are incremented for each line of text. Clicking and dragging in the
line number gutter will select entire lines of text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_gutters_zero_pad_line_numbers}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gutters_zero_pad_line_numbers** = `false`
`🔗<class_CodeEdit_property_gutters_zero_pad_line_numbers>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_numbers_zero_padded**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_line_numbers_zero_padded**()

If `true`, line numbers drawn in the gutter are zero padded based on the
total line count. Requires
`gutters_draw_line_numbers<class_CodeEdit_property_gutters_draw_line_numbers>`{.interpreted-text
role="ref"} to be set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_indent_automatic}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **indent_automatic** =
`false` `🔗<class_CodeEdit_property_indent_automatic>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_indent_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_auto_indent_enabled**()

If `true`, an extra indent is automatically inserted when a new line is
added and a prefix in
`indent_automatic_prefixes<class_CodeEdit_property_indent_automatic_prefixes>`{.interpreted-text
role="ref"} is found. If a brace pair opening key is found, the matching
closing brace will be moved to another new line (see
`auto_brace_completion_pairs<class_CodeEdit_property_auto_brace_completion_pairs>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_indent_automatic_prefixes}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
**indent_automatic_prefixes** = `[":", "{", "[", "("]`
`🔗<class_CodeEdit_property_indent_automatic_prefixes>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_indent_prefixes**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`String<class_String>`{.interpreted-text role="ref"}\]
  **get_auto_indent_prefixes**()

Prefixes to trigger an automatic indent. Used when
`indent_automatic<class_CodeEdit_property_indent_automatic>`{.interpreted-text
role="ref"} is set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_indent_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **indent_size** = `4`
`🔗<class_CodeEdit_property_indent_size>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_indent_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_indent_size**()

Size of the tabulation indent (one `Tab`{.interpreted-text role="kbd"}
press) in characters. If
`indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`{.interpreted-text
role="ref"} is enabled the number of spaces to use.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_indent_use_spaces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **indent_use_spaces** =
`false`
`🔗<class_CodeEdit_property_indent_use_spaces>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_indent_using_spaces**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_indent_using_spaces**()

Use spaces instead of tabs for indentation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_line_folding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **line_folding** =
`false` `🔗<class_CodeEdit_property_line_folding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_folding_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_line_folding_enabled**()

If `true`, lines can be folded. Otherwise, line folding methods like
`fold_line()<class_CodeEdit_method_fold_line>`{.interpreted-text
role="ref"} will not work and
`can_fold_line()<class_CodeEdit_method_can_fold_line>`{.interpreted-text
role="ref"} will always return `false`. See
`gutters_draw_fold_gutter<class_CodeEdit_property_gutters_draw_fold_gutter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_line_length_guidelines}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
**line_length_guidelines** = `[]`
`🔗<class_CodeEdit_property_line_length_guidelines>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_length_guidelines**(value:
  `Array<class_Array>`{.interpreted-text
  role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
  **get_line_length_guidelines**()

Draws vertical lines at the provided columns. The first entry is
considered a main hard guideline and is drawn more prominently.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_symbol_lookup_on_click}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**symbol_lookup_on_click** = `false`
`🔗<class_CodeEdit_property_symbol_lookup_on_click>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_symbol_lookup_on_click_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_symbol_lookup_on_click_enabled**()

Set when a validated word from
`symbol_validate<class_CodeEdit_signal_symbol_validate>`{.interpreted-text
role="ref"} is clicked, the
`symbol_lookup<class_CodeEdit_signal_symbol_lookup>`{.interpreted-text
role="ref"} should be emitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_property_symbol_tooltip_on_hover}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**symbol_tooltip_on_hover** = `false`
`🔗<class_CodeEdit_property_symbol_tooltip_on_hover>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_symbol_tooltip_on_hover_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_symbol_tooltip_on_hover_enabled**()

If `true`, the
`symbol_hovered<class_CodeEdit_signal_symbol_hovered>`{.interpreted-text
role="ref"} signal is emitted when hovering over a word.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CodeEdit_private_method__confirm_code_completion}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_confirm_code_completion**(replace:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_private_method__confirm_code_completion>`{.interpreted-text
role="ref"}

Override this method to define how the selected entry should be
inserted. If `replace` is `true`, any existing text should be replaced.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_private_method__filter_code_completion_candidates}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **\_filter_code_completion_candidates**(candidates:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\])
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_private_method__filter_code_completion_candidates>`{.interpreted-text
role="ref"}

Override this method to define what items in `candidates` should be
displayed.

Both `candidates` and the return is an
`Array<class_Array>`{.interpreted-text role="ref"} of
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}, see
`get_code_completion_option()<class_CodeEdit_method_get_code_completion_option>`{.interpreted-text
role="ref"} for `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_private_method__request_code_completion}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_request_code_completion**(force:
`bool<class_bool>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_private_method__request_code_completion>`{.interpreted-text
role="ref"}

Override this method to define what happens when the user requests code
completion. If `force` is `true`, any checks should be bypassed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_add_auto_brace_completion_pair}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_auto_brace_completion_pair**(start_key:
`String<class_String>`{.interpreted-text role="ref"}, end_key:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_add_auto_brace_completion_pair>`{.interpreted-text
role="ref"}

Adds a brace pair.

Both the start and end keys must be symbols. Only the start key has to
be unique.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_add_code_completion_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_code_completion_option**(type:
`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"}, display_text: `String<class_String>`{.interpreted-text
role="ref"}, insert_text: `String<class_String>`{.interpreted-text
role="ref"}, text_color: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(1, 1, 1, 1), icon:
`Resource<class_Resource>`{.interpreted-text role="ref"} = null, value:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null, location:
`int<class_int>`{.interpreted-text role="ref"} = 1024)
`🔗<class_CodeEdit_method_add_code_completion_option>`{.interpreted-text
role="ref"}

Submits an item to the queue of potential candidates for the
autocomplete menu. Call
`update_code_completion_options()<class_CodeEdit_method_update_code_completion_options>`{.interpreted-text
role="ref"} to update the list.

`location` indicates location of the option relative to the location of
the code completion query. See
`CodeCompletionLocation<enum_CodeEdit_CodeCompletionLocation>`{.interpreted-text
role="ref"} for how to set this value.

\*\*Note:\*\* This list will replace all current candidates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_add_comment_delimiter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_comment_delimiter**(start_key:
`String<class_String>`{.interpreted-text role="ref"}, end_key:
`String<class_String>`{.interpreted-text role="ref"}, line_only:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CodeEdit_method_add_comment_delimiter>`{.interpreted-text
role="ref"}

Adds a comment delimiter from `start_key` to `end_key`. Both keys should
be symbols, and `start_key` must not be shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty
`String<class_String>`{.interpreted-text role="ref"}, the region does
not carry over to the next line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_add_string_delimiter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_string_delimiter**(start_key:
`String<class_String>`{.interpreted-text role="ref"}, end_key:
`String<class_String>`{.interpreted-text role="ref"}, line_only:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CodeEdit_method_add_string_delimiter>`{.interpreted-text
role="ref"}

Defines a string delimiter from `start_key` to `end_key`. Both keys
should be symbols, and `start_key` must not be shared with other
delimiters.

If `line_only` is `true` or `end_key` is an empty
`String<class_String>`{.interpreted-text role="ref"}, the region does
not carry over to the next line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_can_fold_line}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_fold_line**(line:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CodeEdit_method_can_fold_line>`{.interpreted-text
role="ref"}

Returns `true` if the given line is foldable. A line is foldable if it
is the start of a valid code region (see
`get_code_region_start_tag()<class_CodeEdit_method_get_code_region_start_tag>`{.interpreted-text
role="ref"}), if it is the start of a comment or string block, or if the
next non-empty line is more indented (see
`TextEdit.get_indent_level()<class_TextEdit_method_get_indent_level>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_cancel_code_completion}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cancel_code_completion**()
`🔗<class_CodeEdit_method_cancel_code_completion>`{.interpreted-text
role="ref"}

Cancels the autocomplete menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_clear_bookmarked_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_bookmarked_lines**()
`🔗<class_CodeEdit_method_clear_bookmarked_lines>`{.interpreted-text
role="ref"}

Clears all bookmarked lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_clear_breakpointed_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_breakpointed_lines**()
`🔗<class_CodeEdit_method_clear_breakpointed_lines>`{.interpreted-text
role="ref"}

Clears all breakpointed lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_clear_comment_delimiters}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_comment_delimiters**()
`🔗<class_CodeEdit_method_clear_comment_delimiters>`{.interpreted-text
role="ref"}

Removes all comment delimiters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_clear_executing_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_executing_lines**()
`🔗<class_CodeEdit_method_clear_executing_lines>`{.interpreted-text
role="ref"}

Clears all executed lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_clear_string_delimiters}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_string_delimiters**()
`🔗<class_CodeEdit_method_clear_string_delimiters>`{.interpreted-text
role="ref"}

Removes all string delimiters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_confirm_code_completion}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**confirm_code_completion**(replace:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CodeEdit_method_confirm_code_completion>`{.interpreted-text
role="ref"}

Inserts the selected entry into the text. If `replace` is `true`, any
existing text is replaced rather than merged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_convert_indent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**convert_indent**(from_line: `int<class_int>`{.interpreted-text
role="ref"} = -1, to_line: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_CodeEdit_method_convert_indent>`{.interpreted-text role="ref"}

Converts the indents of lines between `from_line` and `to_line` to tabs
or spaces as set by
`indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`{.interpreted-text
role="ref"}.

Values of `-1` convert the entire text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_create_code_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_code_region**()
`🔗<class_CodeEdit_method_create_code_region>`{.interpreted-text
role="ref"}

Creates a new code region with the selection. At least one single line
comment delimiter have to be defined (see
`add_comment_delimiter()<class_CodeEdit_method_add_comment_delimiter>`{.interpreted-text
role="ref"}).

A code region is a part of code that is highlighted when folded and can
help organize your script.

Code region start and end tags can be customized (see
`set_code_region_tags()<class_CodeEdit_method_set_code_region_tags>`{.interpreted-text
role="ref"}).

Code regions are delimited using start and end tags (respectively
`region` and `endregion` by default) preceded by one line comment
delimiter. (eg. `#region` and `#endregion`)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_delete_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**delete_lines**()
`🔗<class_CodeEdit_method_delete_lines>`{.interpreted-text role="ref"}

Deletes all lines that are selected or have a caret on them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_do_indent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **do_indent**()
`🔗<class_CodeEdit_method_do_indent>`{.interpreted-text role="ref"}

If there is no selection, indentation is inserted at the caret.
Otherwise, the selected lines are indented like
`indent_lines()<class_CodeEdit_method_indent_lines>`{.interpreted-text
role="ref"}. Equivalent to the
`ProjectSettings.input/ui_text_indent<class_ProjectSettings_property_input/ui_text_indent>`{.interpreted-text
role="ref"} action. The indentation characters used depend on
`indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`{.interpreted-text
role="ref"} and
`indent_size<class_CodeEdit_property_indent_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_duplicate_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**duplicate_lines**()
`🔗<class_CodeEdit_method_duplicate_lines>`{.interpreted-text
role="ref"}

Duplicates all lines currently selected with any caret. Duplicates the
entire line beneath the current one no matter where the caret is within
the line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_duplicate_selection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**duplicate_selection**()
`🔗<class_CodeEdit_method_duplicate_selection>`{.interpreted-text
role="ref"}

Duplicates all selected text and duplicates all lines with a caret on
them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_fold_all_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fold_all_lines**()
`🔗<class_CodeEdit_method_fold_all_lines>`{.interpreted-text role="ref"}

Folds all lines that are possible to be folded (see
`can_fold_line()<class_CodeEdit_method_can_fold_line>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_fold_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**fold_line**(line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_fold_line>`{.interpreted-text role="ref"}

Folds the given line, if possible (see
`can_fold_line()<class_CodeEdit_method_can_fold_line>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_auto_brace_completion_close_key}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_auto_brace_completion_close_key**(open_key:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_auto_brace_completion_close_key>`{.interpreted-text
role="ref"}

Gets the matching auto brace close key for `open_key`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_bookmarked_lines}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_bookmarked_lines**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_bookmarked_lines>`{.interpreted-text
role="ref"}

Gets all bookmarked lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_breakpointed_lines}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_breakpointed_lines**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_breakpointed_lines>`{.interpreted-text
role="ref"}

Gets all breakpointed lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_code_completion_option}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_code_completion_option**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_code_completion_option>`{.interpreted-text
role="ref"}

Gets the completion option at `index`. The return
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} has the
following key-values:

`kind`:
`CodeCompletionKind<enum_CodeEdit_CodeCompletionKind>`{.interpreted-text
role="ref"}

`display_text`: Text that is shown on the autocomplete menu.

`insert_text`: Text that is to be inserted when this item is selected.

`font_color`: Color of the text on the autocomplete menu.

`icon`: Icon to draw on the autocomplete menu.

`default_value`: Value of the symbol.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_code_completion_options}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Dictionary<class_Dictionary>`{.interpreted-text
role="ref"}\] **get_code_completion_options**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_code_completion_options>`{.interpreted-text
role="ref"}

Gets all completion options, see
`get_code_completion_option()<class_CodeEdit_method_get_code_completion_option>`{.interpreted-text
role="ref"} for return content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_code_completion_selected_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_code_completion_selected_index**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_code_completion_selected_index>`{.interpreted-text
role="ref"}

Gets the index of the current selected completion option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_code_region_end_tag}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_code_region_end_tag**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_code_region_end_tag>`{.interpreted-text
role="ref"}

Returns the code region end tag (without comment delimiter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_code_region_start_tag}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_code_region_start_tag**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_code_region_start_tag>`{.interpreted-text
role="ref"}

Returns the code region start tag (without comment delimiter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_delimiter_end_key}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_delimiter_end_key**(delimiter_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_delimiter_end_key>`{.interpreted-text
role="ref"}

Gets the end key for a string or comment region index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_delimiter_end_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_delimiter_end_position**(line: `int<class_int>`{.interpreted-text
role="ref"}, column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_delimiter_end_position>`{.interpreted-text
role="ref"}

If `line` `column` is in a string or comment, returns the end position
of the region. If not or no end could be found, both
`Vector2<class_Vector2>`{.interpreted-text role="ref"} values will be
`-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_delimiter_start_key}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_delimiter_start_key**(delimiter_index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_delimiter_start_key>`{.interpreted-text
role="ref"}

Gets the start key for a string or comment region index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_delimiter_start_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_delimiter_start_position**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_delimiter_start_position>`{.interpreted-text
role="ref"}

If `line` `column` is in a string or comment, returns the start position
of the region. If not or no start could be found, both
`Vector2<class_Vector2>`{.interpreted-text role="ref"} values will be
`-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_executing_lines}
::: rst-class
classref-method
:::
::::

`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
**get_executing_lines**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_executing_lines>`{.interpreted-text
role="ref"}

Gets all executing lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_folded_lines}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
**get_folded_lines**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_folded_lines>`{.interpreted-text
role="ref"}

Returns all lines that are currently folded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_text_for_code_completion}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_text_for_code_completion**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_text_for_code_completion>`{.interpreted-text
role="ref"}

Returns the full text with char `0xFFFF` at the caret location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_text_for_symbol_lookup}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_text_for_symbol_lookup**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_text_for_symbol_lookup>`{.interpreted-text
role="ref"}

Returns the full text with char `0xFFFF` at the cursor location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_get_text_with_cursor_char}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_text_with_cursor_char**(line: `int<class_int>`{.interpreted-text
role="ref"}, column: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_get_text_with_cursor_char>`{.interpreted-text
role="ref"}

Returns the full text with char `0xFFFF` at the specified location.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_has_auto_brace_completion_close_key}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_auto_brace_completion_close_key**(close_key:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_has_auto_brace_completion_close_key>`{.interpreted-text
role="ref"}

Returns `true` if close key `close_key` exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_has_auto_brace_completion_open_key}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_auto_brace_completion_open_key**(open_key:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_has_auto_brace_completion_open_key>`{.interpreted-text
role="ref"}

Returns `true` if open key `open_key` exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_has_comment_delimiter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_comment_delimiter**(start_key:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_has_comment_delimiter>`{.interpreted-text
role="ref"}

Returns `true` if comment `start_key` exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_has_string_delimiter}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_string_delimiter**(start_key:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_has_string_delimiter>`{.interpreted-text
role="ref"}

Returns `true` if string `start_key` exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_indent_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**indent_lines**()
`🔗<class_CodeEdit_method_indent_lines>`{.interpreted-text role="ref"}

Indents all lines that are selected or have a caret on them. Uses spaces
or a tab depending on
`indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`{.interpreted-text
role="ref"}. See
`unindent_lines()<class_CodeEdit_method_unindent_lines>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_in_comment}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **is_in_comment**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CodeEdit_method_is_in_comment>`{.interpreted-text
role="ref"}

Returns delimiter index if `line` `column` is in a comment. If `column`
is not provided, will return delimiter index if the entire `line` is a
comment. Otherwise `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_in_string}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **is_in_string**(line:
`int<class_int>`{.interpreted-text role="ref"}, column:
`int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_CodeEdit_method_is_in_string>`{.interpreted-text
role="ref"}

Returns the delimiter index if `line` `column` is in a string. If
`column` is not provided, will return the delimiter index if the entire
`line` is a string. Otherwise `-1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_line_bookmarked}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_bookmarked**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_is_line_bookmarked>`{.interpreted-text
role="ref"}

Returns `true` if the given line is bookmarked. See
`set_line_as_bookmarked()<class_CodeEdit_method_set_line_as_bookmarked>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_line_breakpointed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_breakpointed**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_is_line_breakpointed>`{.interpreted-text
role="ref"}

Returns `true` if the given line is breakpointed. See
`set_line_as_breakpoint()<class_CodeEdit_method_set_line_as_breakpoint>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_line_code_region_end}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_code_region_end**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_is_line_code_region_end>`{.interpreted-text
role="ref"}

Returns `true` if the given line is a code region end. See
`set_code_region_tags()<class_CodeEdit_method_set_code_region_tags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_line_code_region_start}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_code_region_start**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_is_line_code_region_start>`{.interpreted-text
role="ref"}

Returns `true` if the given line is a code region start. See
`set_code_region_tags()<class_CodeEdit_method_set_code_region_tags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_line_executing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_executing**(line: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_is_line_executing>`{.interpreted-text
role="ref"}

Returns `true` if the given line is marked as executing. See
`set_line_as_executing()<class_CodeEdit_method_set_line_as_executing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_is_line_folded}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_line_folded**(line: `int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeEdit_method_is_line_folded>`{.interpreted-text role="ref"}

Returns `true` if the given line is folded. See
`fold_line()<class_CodeEdit_method_fold_line>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_move_lines_down}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_lines_down**()
`🔗<class_CodeEdit_method_move_lines_down>`{.interpreted-text
role="ref"}

Moves all lines down that are selected or have a caret on them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_move_lines_up}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_lines_up**()
`🔗<class_CodeEdit_method_move_lines_up>`{.interpreted-text role="ref"}

Moves all lines up that are selected or have a caret on them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_remove_comment_delimiter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_comment_delimiter**(start_key:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_remove_comment_delimiter>`{.interpreted-text
role="ref"}

Removes the comment delimiter with `start_key`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_remove_string_delimiter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_string_delimiter**(start_key:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_remove_string_delimiter>`{.interpreted-text
role="ref"}

Removes the string delimiter with `start_key`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_request_code_completion}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_code_completion**(force: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_CodeEdit_method_request_code_completion>`{.interpreted-text
role="ref"}

Emits
`code_completion_requested<class_CodeEdit_signal_code_completion_requested>`{.interpreted-text
role="ref"}, if `force` is `true` will bypass all checks. Otherwise will
check that the caret is in a word or in front of a prefix. Will ignore
the request if all current options are of type file path, node path, or
signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_code_completion_selected_index}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_code_completion_selected_index**(index:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_set_code_completion_selected_index>`{.interpreted-text
role="ref"}

Sets the current selected completion option.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_code_hint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_code_hint**(code_hint: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_CodeEdit_method_set_code_hint>`{.interpreted-text
role="ref"}

Sets the code hint text. Pass an empty string to clear.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_code_hint_draw_below}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_code_hint_draw_below**(draw_below:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_set_code_hint_draw_below>`{.interpreted-text
role="ref"}

If `true`, the code hint will draw below the main caret. If `false`, the
code hint will draw above the main caret. See
`set_code_hint()<class_CodeEdit_method_set_code_hint>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_code_region_tags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_code_region_tags**(start: `String<class_String>`{.interpreted-text
role="ref"} = \"region\", end: `String<class_String>`{.interpreted-text
role="ref"} = \"endregion\")
`🔗<class_CodeEdit_method_set_code_region_tags>`{.interpreted-text
role="ref"}

Sets the code region start and end tags (without comment delimiter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_line_as_bookmarked}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_as_bookmarked**(line: `int<class_int>`{.interpreted-text
role="ref"}, bookmarked: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_CodeEdit_method_set_line_as_bookmarked>`{.interpreted-text
role="ref"}

Sets the given line as bookmarked. If `true` and
`gutters_draw_bookmarks<class_CodeEdit_property_gutters_draw_bookmarks>`{.interpreted-text
role="ref"} is `true`, draws the
`bookmark<class_CodeEdit_theme_icon_bookmark>`{.interpreted-text
role="ref"} icon in the gutter for this line. See
`get_bookmarked_lines()<class_CodeEdit_method_get_bookmarked_lines>`{.interpreted-text
role="ref"} and
`is_line_bookmarked()<class_CodeEdit_method_is_line_bookmarked>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_line_as_breakpoint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_as_breakpoint**(line: `int<class_int>`{.interpreted-text
role="ref"}, breakpointed: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_CodeEdit_method_set_line_as_breakpoint>`{.interpreted-text
role="ref"}

Sets the given line as a breakpoint. If `true` and
`gutters_draw_breakpoints_gutter<class_CodeEdit_property_gutters_draw_breakpoints_gutter>`{.interpreted-text
role="ref"} is `true`, draws the
`breakpoint<class_CodeEdit_theme_icon_breakpoint>`{.interpreted-text
role="ref"} icon in the gutter for this line. See
`get_breakpointed_lines()<class_CodeEdit_method_get_breakpointed_lines>`{.interpreted-text
role="ref"} and
`is_line_breakpointed()<class_CodeEdit_method_is_line_breakpointed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_line_as_executing}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_line_as_executing**(line: `int<class_int>`{.interpreted-text
role="ref"}, executing: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_CodeEdit_method_set_line_as_executing>`{.interpreted-text
role="ref"}

Sets the given line as executing. If `true` and
`gutters_draw_executing_lines<class_CodeEdit_property_gutters_draw_executing_lines>`{.interpreted-text
role="ref"} is `true`, draws the
`executing_line<class_CodeEdit_theme_icon_executing_line>`{.interpreted-text
role="ref"} icon in the gutter for this line. See
`get_executing_lines()<class_CodeEdit_method_get_executing_lines>`{.interpreted-text
role="ref"} and
`is_line_executing()<class_CodeEdit_method_is_line_executing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_set_symbol_lookup_word_as_valid}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_symbol_lookup_word_as_valid**(valid:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_set_symbol_lookup_word_as_valid>`{.interpreted-text
role="ref"}

Sets the symbol emitted by
`symbol_validate<class_CodeEdit_signal_symbol_validate>`{.interpreted-text
role="ref"} as a valid lookup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_toggle_foldable_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**toggle_foldable_line**(line: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_CodeEdit_method_toggle_foldable_line>`{.interpreted-text
role="ref"}

Toggle the folding of the code block at the given line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_toggle_foldable_lines_at_carets}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**toggle_foldable_lines_at_carets**()
`🔗<class_CodeEdit_method_toggle_foldable_lines_at_carets>`{.interpreted-text
role="ref"}

Toggle the folding of the code block on all lines with a caret on them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_unfold_all_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unfold_all_lines**()
`🔗<class_CodeEdit_method_unfold_all_lines>`{.interpreted-text
role="ref"}

Unfolds all lines that are folded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_unfold_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unfold_line**(line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_unfold_line>`{.interpreted-text role="ref"}

Unfolds the given line if it is folded or if it is hidden under a folded
line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_unindent_lines}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unindent_lines**()
`🔗<class_CodeEdit_method_unindent_lines>`{.interpreted-text role="ref"}

Unindents all lines that are selected or have a caret on them. Uses
spaces or a tab depending on
`indent_use_spaces<class_CodeEdit_property_indent_use_spaces>`{.interpreted-text
role="ref"}. Equivalent to the
`ProjectSettings.input/ui_text_dedent<class_ProjectSettings_property_input/ui_text_dedent>`{.interpreted-text
role="ref"} action. See
`indent_lines()<class_CodeEdit_method_indent_lines>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_method_update_code_completion_options}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_code_completion_options**(force:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CodeEdit_method_update_code_completion_options>`{.interpreted-text
role="ref"}

Submits all completion options added with
`add_code_completion_option()<class_CodeEdit_method_add_code_completion_option>`{.interpreted-text
role="ref"}. Will try to force the autocomplete menu to popup, if
`force` is `true`.

\*\*Note:\*\* This will replace all current candidates.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_CodeEdit_theme_color_bookmark_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **bookmark_color** =
`Color(0.5, 0.64, 1, 0.8)`
`🔗<class_CodeEdit_theme_color_bookmark_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the bookmark icon
for bookmarked lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_brace_mismatch_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**brace_mismatch_color** = `Color(1, 0.2, 0.2, 1)`
`🔗<class_CodeEdit_theme_color_brace_mismatch_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the text to
highlight mismatched braces.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_breakpoint_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **breakpoint_color**
= `Color(0.9, 0.29, 0.3, 1)`
`🔗<class_CodeEdit_theme_color_breakpoint_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the breakpoint
icon for bookmarked lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_code_folding_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**code_folding_color** = `Color(0.8, 0.8, 0.8, 0.8)`
`🔗<class_CodeEdit_theme_color_code_folding_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} for all icons related
to line folding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_completion_background_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**completion_background_color** = `Color(0.17, 0.16, 0.2, 1)`
`🔗<class_CodeEdit_theme_color_completion_background_color>`{.interpreted-text
role="ref"}

Sets the background `Color<class_Color>`{.interpreted-text role="ref"}
for the code completion popup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_completion_existing_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**completion_existing_color** = `Color(0.87, 0.87, 0.87, 0.13)`
`🔗<class_CodeEdit_theme_color_completion_existing_color>`{.interpreted-text
role="ref"}

Background highlight `Color<class_Color>`{.interpreted-text role="ref"}
for matching text in code completion options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_completion_scroll_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**completion_scroll_color** = `Color(1, 1, 1, 0.29)`
`🔗<class_CodeEdit_theme_color_completion_scroll_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the scrollbar in
the code completion popup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_completion_scroll_hovered_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**completion_scroll_hovered_color** = `Color(1, 1, 1, 0.4)`
`🔗<class_CodeEdit_theme_color_completion_scroll_hovered_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the scrollbar in
the code completion popup when hovered.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_completion_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**completion_selected_color** = `Color(0.26, 0.26, 0.27, 1)`
`🔗<class_CodeEdit_theme_color_completion_selected_color>`{.interpreted-text
role="ref"}

Background highlight `Color<class_Color>`{.interpreted-text role="ref"}
for the current selected option item in the code completion popup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_executing_line_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**executing_line_color** = `Color(0.98, 0.89, 0.27, 1)`
`🔗<class_CodeEdit_theme_color_executing_line_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the executing icon
for executing lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_folded_code_region_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**folded_code_region_color** = `Color(0.68, 0.46, 0.77, 0.2)`
`🔗<class_CodeEdit_theme_color_folded_code_region_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of background line
highlight for folded code region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_line_length_guideline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**line_length_guideline_color** = `Color(0.3, 0.5, 0.8, 0.1)`
`🔗<class_CodeEdit_theme_color_line_length_guideline_color>`{.interpreted-text
role="ref"}

`Color<class_Color>`{.interpreted-text role="ref"} of the main line
length guideline, secondary guidelines will have 50% alpha applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_color_line_number_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **line_number_color**
= `Color(0.67, 0.67, 0.67, 0.4)`
`🔗<class_CodeEdit_theme_color_line_number_color>`{.interpreted-text
role="ref"}

Sets the `Color<class_Color>`{.interpreted-text role="ref"} of line
numbers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_constant_completion_lines}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **completion_lines** =
`7`
`🔗<class_CodeEdit_theme_constant_completion_lines>`{.interpreted-text
role="ref"}

Max number of options to display in the code completion popup at any one
time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_constant_completion_max_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **completion_max_width**
= `50`
`🔗<class_CodeEdit_theme_constant_completion_max_width>`{.interpreted-text
role="ref"}

Max width of options in the code completion popup. Options longer than
this will be cut off.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_constant_completion_scroll_width}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**completion_scroll_width** = `6`
`🔗<class_CodeEdit_theme_constant_completion_scroll_width>`{.interpreted-text
role="ref"}

Width of the scrollbar in the code completion popup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_bookmark}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **bookmark**
`🔗<class_CodeEdit_theme_icon_bookmark>`{.interpreted-text role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
to draw in the bookmark gutter for bookmarked lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_breakpoint}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**breakpoint**
`🔗<class_CodeEdit_theme_icon_breakpoint>`{.interpreted-text role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
to draw in the breakpoint gutter for breakpointed lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_can_fold}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **can_fold**
`🔗<class_CodeEdit_theme_icon_can_fold>`{.interpreted-text role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
to draw in the line folding gutter when a line can be folded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_can_fold_code_region}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**can_fold_code_region**
`🔗<class_CodeEdit_theme_icon_can_fold_code_region>`{.interpreted-text
role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
to draw in the line folding gutter when a code region can be folded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_completion_color_bg}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**completion_color_bg**
`🔗<class_CodeEdit_theme_icon_completion_color_bg>`{.interpreted-text
role="ref"}

Background panel for the color preview box in autocompletion (visible
when the color is translucent).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_executing_line}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**executing_line**
`🔗<class_CodeEdit_theme_icon_executing_line>`{.interpreted-text
role="ref"}

Icon to draw in the executing gutter for executing lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_folded}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **folded**
`🔗<class_CodeEdit_theme_icon_folded>`{.interpreted-text role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
to draw in the line folding gutter when a line is folded and can be
unfolded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_folded_code_region}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**folded_code_region**
`🔗<class_CodeEdit_theme_icon_folded_code_region>`{.interpreted-text
role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
to draw in the line folding gutter when a code region is folded and can
be unfolded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_icon_folded_eol_icon}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**folded_eol_icon**
`🔗<class_CodeEdit_theme_icon_folded_eol_icon>`{.interpreted-text
role="ref"}

Sets a custom `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
to draw at the end of a folded line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeEdit_theme_style_completion}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **completion**
`🔗<class_CodeEdit_theme_style_completion>`{.interpreted-text
role="ref"}

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} for the code
completion popup.
