github_url
:   hide

# RichTextLabel {#class_RichTextLabel}

**Inherits:** `Control<class_Control>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A control for displaying text that can contain different font styles,
images, and basic formatting.

::: rst-class
classref-introduction-group
:::

## Description

A control for displaying text that can contain custom fonts, images, and
basic formatting. **RichTextLabel** manages these as an internal tag
stack. It also adapts itself to given width/heights.

\*\*Note:\*\*
`newline()<class_RichTextLabel_method_newline>`{.interpreted-text
role="ref"},
`push_paragraph()<class_RichTextLabel_method_push_paragraph>`{.interpreted-text
role="ref"}, `"\n"`, `"\r\n"`, `p` tag, and alignment tags start a new
paragraph. Each paragraph is processed independently, in its own BiDi
context. If you want to force line wrapping within paragraph, any other
line breaking character can be used, for example, Form Feed (U+000C),
Next Line (U+0085), Line Separator (U+2028).

\*\*Note:\*\* Assignments to
`text<class_RichTextLabel_property_text>`{.interpreted-text role="ref"}
clear the tag stack and reconstruct it from the property\'s contents.
Any edits made to
`text<class_RichTextLabel_property_text>`{.interpreted-text role="ref"}
will erase previous edits made from other manual sources such as
`append_text()<class_RichTextLabel_method_append_text>`{.interpreted-text
role="ref"} and the `push_*` /
`pop()<class_RichTextLabel_method_pop>`{.interpreted-text role="ref"}
methods.

\*\*Note:\*\* RichTextLabel doesn\'t support entangled BBCode tags. For
example, instead of using `[b]bold[i]bold italic[/b]italic[/i]`, use
`[b]bold[i]bold italic[/i][/b][i]italic[/i]`.

\*\*Note:\*\* `push_*/pop_*` functions won\'t affect BBCode.

\*\*Note:\*\* While
`bbcode_enabled<class_RichTextLabel_property_bbcode_enabled>`{.interpreted-text
role="ref"} is enabled, alignment tags such as `[center]` will take
priority over the
`horizontal_alignment<class_RichTextLabel_property_horizontal_alignment>`{.interpreted-text
role="ref"} setting which determines the default text alignment.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `BBCode in RichTextLabel <../tutorials/ui/bbcode_in_richtextlabel>`{.interpreted-text
  role="doc"}
- [Rich Text Label with BBCode
  Demo](https://godotengine.org/asset-library/asset/2774)
- [Operating System Testing
  Demo](https://godotengine.org/asset-library/asset/2789)

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

:::: {#class_RichTextLabel_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**()
`🔗<class_RichTextLabel_signal_finished>`{.interpreted-text role="ref"}

Triggered when the document is fully loaded.

\*\*Note:\*\* This can happen before the text is processed for drawing.
Scrolling values may not be valid until the document is drawn for the
first time after this signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_signal_meta_clicked}
::: rst-class
classref-signal
:::
::::

**meta_clicked**(meta: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_signal_meta_clicked>`{.interpreted-text
role="ref"}

Triggered when the user clicks on content between meta (URL) tags. If
the meta is defined in BBCode, e.g. `[url={"key": "value"}]Text[/url]`,
then the parameter for this signal will always be a
`String<class_String>`{.interpreted-text role="ref"} type. If a
particular type or an object is desired, the
`push_meta()<class_RichTextLabel_method_push_meta>`{.interpreted-text
role="ref"} method must be used to manually insert the data into the tag
stack. Alternatively, you can convert the
`String<class_String>`{.interpreted-text role="ref"} input to the
desired type based on its contents (such as calling
`JSON.parse()<class_JSON_method_parse>`{.interpreted-text role="ref"} on
it).

For example, the following method can be connected to
`meta_clicked<class_RichTextLabel_signal_meta_clicked>`{.interpreted-text
role="ref"} to open clicked URLs using the user\'s default web browser:

:::: tabs
::: code-tab
gdscript

\# This assumes RichTextLabel\'s [meta_clicked]{.title-ref} signal was
connected to \# the function below using the signal connection dialog.
func
[richtextlabel_on_meta_clicked]{#richtextlabel_on_meta_clicked}(meta):
\# [meta]{.title-ref} is of Variant type, so convert it to a String to
avoid script errors at run-time. OS.shell_open(str(meta))
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_signal_meta_hover_ended}
::: rst-class
classref-signal
:::
::::

**meta_hover_ended**(meta: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_signal_meta_hover_ended>`{.interpreted-text
role="ref"}

Triggers when the mouse exits a meta tag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_signal_meta_hover_started}
::: rst-class
classref-signal
:::
::::

**meta_hover_started**(meta: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_signal_meta_hover_started>`{.interpreted-text
role="ref"}

Triggers when the mouse enters a meta tag.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_RichTextLabel_ListType}
::: rst-class
classref-enumeration
:::
::::

enum **ListType**: `🔗<enum_RichTextLabel_ListType>`{.interpreted-text
role="ref"}

:::: {#class_RichTextLabel_constant_LIST_NUMBERS}
::: rst-class
classref-enumeration-constant
:::
::::

`ListType<enum_RichTextLabel_ListType>`{.interpreted-text role="ref"}
**LIST_NUMBERS** = `0`

Each list item has a number marker.

:::: {#class_RichTextLabel_constant_LIST_LETTERS}
::: rst-class
classref-enumeration-constant
:::
::::

`ListType<enum_RichTextLabel_ListType>`{.interpreted-text role="ref"}
**LIST_LETTERS** = `1`

Each list item has a letter marker.

:::: {#class_RichTextLabel_constant_LIST_ROMAN}
::: rst-class
classref-enumeration-constant
:::
::::

`ListType<enum_RichTextLabel_ListType>`{.interpreted-text role="ref"}
**LIST_ROMAN** = `2`

Each list item has a roman number marker.

:::: {#class_RichTextLabel_constant_LIST_DOTS}
::: rst-class
classref-enumeration-constant
:::
::::

`ListType<enum_RichTextLabel_ListType>`{.interpreted-text role="ref"}
**LIST_DOTS** = `3`

Each list item has a filled circle marker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RichTextLabel_MenuItems}
::: rst-class
classref-enumeration
:::
::::

enum **MenuItems**: `🔗<enum_RichTextLabel_MenuItems>`{.interpreted-text
role="ref"}

:::: {#class_RichTextLabel_constant_MENU_COPY}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_RichTextLabel_MenuItems>`{.interpreted-text role="ref"}
**MENU_COPY** = `0`

Copies the selected text.

:::: {#class_RichTextLabel_constant_MENU_SELECT_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_RichTextLabel_MenuItems>`{.interpreted-text role="ref"}
**MENU_SELECT_ALL** = `1`

Selects the whole **RichTextLabel** text.

:::: {#class_RichTextLabel_constant_MENU_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`MenuItems<enum_RichTextLabel_MenuItems>`{.interpreted-text role="ref"}
**MENU_MAX** = `2`

Represents the size of the
`MenuItems<enum_RichTextLabel_MenuItems>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RichTextLabel_MetaUnderline}
::: rst-class
classref-enumeration
:::
::::

enum **MetaUnderline**:
`🔗<enum_RichTextLabel_MetaUnderline>`{.interpreted-text role="ref"}

:::: {#class_RichTextLabel_constant_META_UNDERLINE_NEVER}
::: rst-class
classref-enumeration-constant
:::
::::

`MetaUnderline<enum_RichTextLabel_MetaUnderline>`{.interpreted-text
role="ref"} **META_UNDERLINE_NEVER** = `0`

Meta tag does not display an underline, even if
`meta_underlined<class_RichTextLabel_property_meta_underlined>`{.interpreted-text
role="ref"} is `true`.

:::: {#class_RichTextLabel_constant_META_UNDERLINE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`MetaUnderline<enum_RichTextLabel_MetaUnderline>`{.interpreted-text
role="ref"} **META_UNDERLINE_ALWAYS** = `1`

If
`meta_underlined<class_RichTextLabel_property_meta_underlined>`{.interpreted-text
role="ref"} is `true`, meta tag always display an underline.

:::: {#class_RichTextLabel_constant_META_UNDERLINE_ON_HOVER}
::: rst-class
classref-enumeration-constant
:::
::::

`MetaUnderline<enum_RichTextLabel_MetaUnderline>`{.interpreted-text
role="ref"} **META_UNDERLINE_ON_HOVER** = `2`

If
`meta_underlined<class_RichTextLabel_property_meta_underlined>`{.interpreted-text
role="ref"} is `true`, meta tag display an underline when the mouse
cursor is over it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_RichTextLabel_ImageUpdateMask}
::: rst-class
classref-enumeration
:::
::::

flags **ImageUpdateMask**:
`🔗<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text role="ref"}

:::: {#class_RichTextLabel_constant_UPDATE_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_TEXTURE** = `1`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image texture.

:::: {#class_RichTextLabel_constant_UPDATE_SIZE}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_SIZE** = `2`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image size.

:::: {#class_RichTextLabel_constant_UPDATE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_COLOR** = `4`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image color.

:::: {#class_RichTextLabel_constant_UPDATE_ALIGNMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_ALIGNMENT** = `8`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image inline alignment.

:::: {#class_RichTextLabel_constant_UPDATE_REGION}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_REGION** = `16`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image texture region.

:::: {#class_RichTextLabel_constant_UPDATE_PAD}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_PAD** = `32`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image padding.

:::: {#class_RichTextLabel_constant_UPDATE_TOOLTIP}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_TOOLTIP** = `64`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image tooltip.

:::: {#class_RichTextLabel_constant_UPDATE_WIDTH_IN_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"} **UPDATE_WIDTH_IN_PERCENT** = `128`

If this bit is set,
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"} changes image width from/to percents.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_RichTextLabel_property_autowrap_mode}
::: rst-class
classref-property
:::
::::

`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"} **autowrap_mode** = `3`
`🔗<class_RichTextLabel_property_autowrap_mode>`{.interpreted-text
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
rectangle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_autowrap_trim_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
role="ref"}\] **autowrap_trim_flags** = `192`
`🔗<class_RichTextLabel_property_autowrap_trim_flags>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autowrap_trim_flags**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`LineBreakFlag<enum_TextServer_LineBreakFlag>`{.interpreted-text
  role="ref"}\] **get_autowrap_trim_flags**()

Autowrap space trimming flags. See
`TextServer.BREAK_TRIM_START_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_START_EDGE_SPACES>`{.interpreted-text
role="ref"} and
`TextServer.BREAK_TRIM_END_EDGE_SPACES<class_TextServer_constant_BREAK_TRIM_END_EDGE_SPACES>`{.interpreted-text
role="ref"} for more info.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_bbcode_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **bbcode_enabled** =
`false`
`🔗<class_RichTextLabel_property_bbcode_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_bbcode**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_bbcode**()

If `true`, the label uses BBCode formatting.

\*\*Note:\*\* This only affects the contents of
`text<class_RichTextLabel_property_text>`{.interpreted-text role="ref"},
not the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_context_menu_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**context_menu_enabled** = `false`
`🔗<class_RichTextLabel_property_context_menu_enabled>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_custom_effects}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"} **custom_effects** =
`[]` `🔗<class_RichTextLabel_property_custom_effects>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_effects**(value: `Array<class_Array>`{.interpreted-text
  role="ref"})
- `Array<class_Array>`{.interpreted-text role="ref"} **get_effects**()

The currently installed custom effects. This is an array of
`RichTextEffect<class_RichTextEffect>`{.interpreted-text role="ref"}s.

To add a custom effect, it\'s more convenient to use
`install_effect()<class_RichTextLabel_method_install_effect>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_deselect_on_focus_loss_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**deselect_on_focus_loss_enabled** = `true`
`🔗<class_RichTextLabel_property_deselect_on_focus_loss_enabled>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_drag_and_drop_selection_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**drag_and_drop_selection_enabled** = `true`
`🔗<class_RichTextLabel_property_drag_and_drop_selection_enabled>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_fit_content}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **fit_content** =
`false` `🔗<class_RichTextLabel_property_fit_content>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fit_content**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_fit_content_enabled**()

If `true`, the label\'s minimum size will be automatically updated to
fit its content, matching the behavior of
`Label<class_Label>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_hint_underlined}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **hint_underlined** =
`true`
`🔗<class_RichTextLabel_property_hint_underlined>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_hint_underline**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_hint_underlined**()

If `true`, the label underlines hint tags such as
`[hint=description]{text}[/hint]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_horizontal_alignment}
::: rst-class
classref-property
:::
::::

`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} **horizontal_alignment** = `0`
`🔗<class_RichTextLabel_property_horizontal_alignment>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_justification_flags}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] **justification_flags** = `163`
`🔗<class_RichTextLabel_property_justification_flags>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **language** = `""`
`🔗<class_RichTextLabel_property_language>`{.interpreted-text
role="ref"}

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

:::: {#class_RichTextLabel_property_meta_underlined}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **meta_underlined** =
`true`
`🔗<class_RichTextLabel_property_meta_underlined>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_meta_underline**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_meta_underlined**()

If `true`, the label underlines meta tags such as `[url]{text}[/url]`.
These tags can call a function when clicked if
`meta_clicked<class_RichTextLabel_signal_meta_clicked>`{.interpreted-text
role="ref"} is connected to a function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_progress_bar_delay}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **progress_bar_delay** =
`1000`
`🔗<class_RichTextLabel_property_progress_bar_delay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_progress_bar_delay**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_progress_bar_delay**()

The delay after which the loading progress bar is displayed, in
milliseconds. Set to `-1` to disable progress bar entirely.

\*\*Note:\*\* Progress bar is displayed only if
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_scroll_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **scroll_active** =
`true`
`🔗<class_RichTextLabel_property_scroll_active>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_scroll_active**()

If `true`, the scrollbar is visible. Setting this to `false` does not
block scrolling completely. See
`scroll_to_line()<class_RichTextLabel_method_scroll_to_line>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_scroll_following}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **scroll_following** =
`false`
`🔗<class_RichTextLabel_property_scroll_following>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_follow**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_scroll_following**()

If `true`, the window scrolls down to display new content automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_scroll_following_visible_characters}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**scroll_following_visible_characters** = `false`
`🔗<class_RichTextLabel_property_scroll_following_visible_characters>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scroll_follow_visible_characters**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_scroll_following_visible_characters**()

If `true`, the window scrolls to display the last visible line when
`visible_characters<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"} or
`visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} is changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_selection_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **selection_enabled** =
`false`
`🔗<class_RichTextLabel_property_selection_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_selection_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_selection_enabled**()

If `true`, the label allows text selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_shortcut_keys_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**shortcut_keys_enabled** = `true`
`🔗<class_RichTextLabel_property_shortcut_keys_enabled>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_structured_text_bidi_override}
::: rst-class
classref-property
:::
::::

`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} **structured_text_bidi_override** = `0`
`🔗<class_RichTextLabel_property_structured_text_bidi_override>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_structured_text_bidi_override_options}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**structured_text_bidi_override_options** = `[]`
`🔗<class_RichTextLabel_property_structured_text_bidi_override_options>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_tab_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **tab_size** = `4`
`🔗<class_RichTextLabel_property_tab_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_size**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_tab_size**()

The number of spaces associated with a single tab length. Does not
affect `\t` in text tags, only indent tags.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_tab_stops}
::: rst-class
classref-property
:::
::::

`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} **tab_stops** = `PackedFloat32Array()`
`🔗<class_RichTextLabel_property_tab_stops>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_tab_stops**(value:
  `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"})
- `PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
  role="ref"} **get_tab_stops**()

Aligns text to the given tab-stops.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_text}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **text** = `""`
`🔗<class_RichTextLabel_property_text>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_text**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"} **get_text**()

The label\'s text in BBCode format. Is not representative of manual
modifications to the internal tag stack. Erases changes made by other
methods when edited.

\*\*Note:\*\* If
`bbcode_enabled<class_RichTextLabel_property_bbcode_enabled>`{.interpreted-text
role="ref"} is `true`, it is unadvised to use the `+=` operator with
`text<class_RichTextLabel_property_text>`{.interpreted-text role="ref"}
(e.g. `text += "some string"`) as it replaces the whole text and can
cause slowdowns. It will also erase all BBCode that was added to stack
using `push_*` methods. Use
`append_text()<class_RichTextLabel_method_append_text>`{.interpreted-text
role="ref"} for adding text instead, unless you absolutely need to close
a tag that was opened in an earlier method call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_text_direction}
::: rst-class
classref-property
:::
::::

`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} **text_direction** = `0`
`🔗<class_RichTextLabel_property_text_direction>`{.interpreted-text
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

:::: {#class_RichTextLabel_property_threaded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **threaded** = `false`
`🔗<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_threaded**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_threaded**()

If `true`, text processing is done in a background thread.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_vertical_alignment}
::: rst-class
classref-property
:::
::::

`VerticalAlignment<enum_@GlobalScope_VerticalAlignment>`{.interpreted-text
role="ref"} **vertical_alignment** = `0`
`🔗<class_RichTextLabel_property_vertical_alignment>`{.interpreted-text
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

Controls the text\'s vertical alignment. Supports top, center, bottom,
and fill.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_visible_characters}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **visible_characters** =
`-1`
`🔗<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible_characters**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_visible_characters**()

The number of characters to display. If set to `-1`, all characters are
displayed. This can be useful when animating the text appearing in a
dialog box.

\*\*Note:\*\* Setting this property updates
`visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} accordingly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_visible_characters_behavior}
::: rst-class
classref-property
:::
::::

`VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
role="ref"} **visible_characters_behavior** = `0`
`🔗<class_RichTextLabel_property_visible_characters_behavior>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible_characters_behavior**(value:
  `VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
  role="ref"})
- `VisibleCharactersBehavior<enum_TextServer_VisibleCharactersBehavior>`{.interpreted-text
  role="ref"} **get_visible_characters_behavior**()

The clipping behavior when
`visible_characters<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"} or
`visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} is set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_property_visible_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **visible_ratio** =
`1.0` `🔗<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visible_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_visible_ratio**()

The fraction of characters to display, relative to the total number of
characters (see
`get_total_character_count()<class_RichTextLabel_method_get_total_character_count>`{.interpreted-text
role="ref"}). If set to `1.0`, all characters are displayed. If set to
`0.5`, only half of the characters will be displayed. This can be useful
when animating the text appearing in a dialog box.

\*\*Note:\*\* Setting this property updates
`visible_characters<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"} accordingly.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RichTextLabel_method_add_hr}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_hr**(width: `int<class_int>`{.interpreted-text role="ref"} = 90,
height: `int<class_int>`{.interpreted-text role="ref"} = 2, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"} = 1, width_in_percent: `bool<class_bool>`{.interpreted-text
role="ref"} = true, height_in_percent:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_RichTextLabel_method_add_hr>`{.interpreted-text role="ref"}

Adds a horizontal rule that can be used to separate content.

If `width_in_percent` is set, `width` values are percentages of the
control width instead of pixels.

If `height_in_percent` is set, `height` values are percentages of the
control width instead of pixels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_add_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_image**(image: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"} = 0,
height: `int<class_int>`{.interpreted-text role="ref"} = 0, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} = 5, region: `Rect2<class_Rect2>`{.interpreted-text
role="ref"} = Rect2(0, 0, 0, 0), key:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null, pad:
`bool<class_bool>`{.interpreted-text role="ref"} = false, tooltip:
`String<class_String>`{.interpreted-text role="ref"} = \"\",
width_in_percent: `bool<class_bool>`{.interpreted-text role="ref"} =
false, height_in_percent: `bool<class_bool>`{.interpreted-text
role="ref"} = false, alt_text: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`🔗<class_RichTextLabel_method_add_image>`{.interpreted-text role="ref"}

Adds an image\'s opening and closing tags to the tag stack, optionally
providing a `width` and `height` to resize the image, a `color` to tint
the image and a `region` to only use parts of the image.

If `width` or `height` is set to 0, the image size will be adjusted in
order to keep the original aspect ratio.

If `width` and `height` are not set, but `region` is, the region\'s rect
will be used.

`key` is an optional identifier, that can be used to modify the image
via
`update_image()<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"}.

If `pad` is set, and the image is smaller than the size specified by
`width` and `height`, the image padding is added to match the size
instead of upscaling.

If `width_in_percent` is set, `width` values are percentages of the
control width instead of pixels.

If `height_in_percent` is set, `height` values are percentages of the
control width instead of pixels.

`alt_text` is used as the image description for assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_add_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_text**(text: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_add_text>`{.interpreted-text role="ref"}

Adds raw non-BBCode-parsed text to the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_append_text}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**append_text**(bbcode: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_append_text>`{.interpreted-text
role="ref"}

Parses `bbcode` and adds tags to the tag stack as needed.

\*\*Note:\*\* Using this method, you can\'t close a tag that was opened
in a previous
`append_text()<class_RichTextLabel_method_append_text>`{.interpreted-text
role="ref"} call. This is done to improve performance, especially when
updating large RichTextLabels since rebuilding the whole BBCode every
time would be slower. If you absolutely need to close a tag in a future
method call, append the
`text<class_RichTextLabel_property_text>`{.interpreted-text role="ref"}
instead of using
`append_text()<class_RichTextLabel_method_append_text>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_RichTextLabel_method_clear>`{.interpreted-text role="ref"}

Clears the tag stack, causing the label to display nothing.

\*\*Note:\*\* This method does not affect
`text<class_RichTextLabel_property_text>`{.interpreted-text role="ref"},
and its contents will show again if the label is redrawn. However,
setting `text<class_RichTextLabel_property_text>`{.interpreted-text
role="ref"} to an empty `String<class_String>`{.interpreted-text
role="ref"} also clears the stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_deselect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **deselect**()
`🔗<class_RichTextLabel_method_deselect>`{.interpreted-text role="ref"}

Clears the current selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_character_line}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_character_line**(character: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_get_character_line>`{.interpreted-text
role="ref"}

Returns the line number of the character position provided. Line and
character numbers are both zero-indexed.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_character_paragraph}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_character_paragraph**(character:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_get_character_paragraph>`{.interpreted-text
role="ref"}

Returns the paragraph number of the character position provided.
Paragraph and character numbers are both zero-indexed.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_content_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_content_height**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_content_height>`{.interpreted-text
role="ref"}

Returns the height of the content.

\*\*Note:\*\* This method always returns the full content size, and is
not affected by
`visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} and
`visible_characters<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"}. To get the visible content size, use
`get_visible_content_rect()<class_RichTextLabel_method_get_visible_content_rect>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_content_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_content_width**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_content_width>`{.interpreted-text
role="ref"}

Returns the width of the content.

\*\*Note:\*\* This method always returns the full content size, and is
not affected by
`visible_ratio<class_RichTextLabel_property_visible_ratio>`{.interpreted-text
role="ref"} and
`visible_characters<class_RichTextLabel_property_visible_characters>`{.interpreted-text
role="ref"}. To get the visible content size, use
`get_visible_content_rect()<class_RichTextLabel_method_get_visible_content_rect>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_line_count>`{.interpreted-text
role="ref"}

Returns the total number of lines in the text. Wrapped text is counted
as multiple lines.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_line_height}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_height**(line:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_line_height>`{.interpreted-text
role="ref"}

Returns the height of the line found at the provided index.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether the document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_line_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_line_offset**(line: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_get_line_offset>`{.interpreted-text
role="ref"}

Returns the vertical offset of the line found at the provided index.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_line_range}
::: rst-class
classref-method
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**get_line_range**(line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_get_line_range>`{.interpreted-text
role="ref"}

Returns the indexes of the first and last visible characters for the
given `line`, as a `Vector2i<class_Vector2i>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* If
`visible_characters_behavior<class_RichTextLabel_property_visible_characters_behavior>`{.interpreted-text
role="ref"} is set to
`TextServer.VC_CHARS_BEFORE_SHAPING<class_TextServer_constant_VC_CHARS_BEFORE_SHAPING>`{.interpreted-text
role="ref"} only visible wrapped lines are counted.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_line_width}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_line_width**(line:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_line_width>`{.interpreted-text
role="ref"}

Returns the width of the line found at the provided index.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether the document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_menu}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_menu**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RichTextLabel_method_get_menu>`{.interpreted-text
role="ref"}

Returns the `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
of this **RichTextLabel**. By default, this menu is displayed when
right-clicking on the **RichTextLabel**.

You can add custom menu items or remove standard ones. Make sure your
IDs don\'t conflict with the standard ones (see
`MenuItems<enum_RichTextLabel_MenuItems>`{.interpreted-text
role="ref"}). For example:

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var menu = get_menu() \# Remove \"Select All\" item.
    menu.remove_item(MENU_SELECT_ALL) \# Add custom items.
    menu.add_separator() menu.add_item(\"Duplicate Text\", MENU_MAX + 1)
    \# Connect callback.
    menu.id_pressed.connect([on_item_pressed]{#on_item_pressed})

func [on_item_pressed]{#on_item_pressed}(id):

:   

    if id == MENU_MAX + 1:

    :   add_text(\"n\" + get_parsed_text())
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { var menu = GetMenu(); // Remove
\"Select All\" item. menu.RemoveItem(RichTextLabel.MenuItems.SelectAll);
// Add custom items. menu.AddSeparator(); menu.AddItem(\"Duplicate
Text\", RichTextLabel.MenuItems.Max + 1); // Add event handler.
menu.IdPressed += OnItemPressed; }

public void OnItemPressed(int id) { if (id ==
TextEdit.MenuItems.Max + 1) { AddText(\"n\" + GetParsedText()); } }
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

:::: {#class_RichTextLabel_method_get_paragraph_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_paragraph_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_paragraph_count>`{.interpreted-text
role="ref"}

Returns the total number of paragraphs (newlines or `p` tags in the tag
stack\'s text tags). Considers wrapped text as one paragraph.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_paragraph_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_paragraph_offset**(paragraph: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_get_paragraph_offset>`{.interpreted-text
role="ref"}

Returns the vertical offset of the paragraph found at the provided
index.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_parsed_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_parsed_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_parsed_text>`{.interpreted-text
role="ref"}

Returns the text without BBCode mark-up.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_selected_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_selected_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_selected_text>`{.interpreted-text
role="ref"}

Returns the current selection text. Does not include BBCodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_selection_from}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_selection_from**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_selection_from>`{.interpreted-text
role="ref"}

Returns the current selection first character index if a selection is
active, `-1` otherwise. Does not include BBCodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_selection_line_offset}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_selection_line_offset**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_selection_line_offset>`{.interpreted-text
role="ref"}

Returns the current selection vertical line offset if a selection is
active, `-1.0` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_selection_to}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_selection_to**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_selection_to>`{.interpreted-text
role="ref"}

Returns the current selection last character index if a selection is
active, `-1` otherwise. Does not include BBCodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_total_character_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_total_character_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_total_character_count>`{.interpreted-text
role="ref"}

Returns the total number of characters from text tags. Does not include
BBCodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_v_scroll_bar}
::: rst-class
classref-method
:::
::::

`VScrollBar<class_VScrollBar>`{.interpreted-text role="ref"}
**get_v_scroll_bar**()
`🔗<class_RichTextLabel_method_get_v_scroll_bar>`{.interpreted-text
role="ref"}

Returns the vertical scrollbar.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_visible_content_rect}
::: rst-class
classref-method
:::
::::

`Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
**get_visible_content_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_visible_content_rect>`{.interpreted-text
role="ref"}

Returns the bounding rectangle of the visible content.

\*\*Note:\*\* This method returns a correct value only after the label
has been drawn.

::::: tabs
::: code-tab
gdscript

extends RichTextLabel

\@export var background_panel: Panel

func [ready]{#ready}():

:   await draw background_panel.position =
    get_visible_content_rect().position background_panel.size =
    get_visible_content_rect().size
:::

::: code-tab
csharp

public partial class TestLabel : RichTextLabel { \[Export\] public Panel
BackgroundPanel { get; set; }

> public override async void [Ready]{#ready}() { await ToSignal(this,
> Control.SignalName.Draw); BackgroundGPanel.Position =
> GetVisibleContentRect().Position; BackgroundPanel.Size =
> GetVisibleContentRect().Size; }

}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_visible_line_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_visible_line_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_visible_line_count>`{.interpreted-text
role="ref"}

Returns the number of visible lines.

\*\*Note:\*\* This method returns a correct value only after the label
has been drawn.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_get_visible_paragraph_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_visible_paragraph_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_get_visible_paragraph_count>`{.interpreted-text
role="ref"}

Returns the number of visible paragraphs. A paragraph is considered
visible if at least one of its lines is visible.

\*\*Note:\*\* This method returns a correct value only after the label
has been drawn.

\*\*Note:\*\* If
`threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, this method returns a value for the loaded part
of the document. Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} or
`finished<class_RichTextLabel_signal_finished>`{.interpreted-text
role="ref"} to determine whether document is fully loaded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_install_effect}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**install_effect**(effect: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_install_effect>`{.interpreted-text
role="ref"}

Installs a custom effect. This can also be done in the Inspector through
the
`custom_effects<class_RichTextLabel_property_custom_effects>`{.interpreted-text
role="ref"} property. `effect` should be a valid
`RichTextEffect<class_RichTextEffect>`{.interpreted-text role="ref"}.

\*\*Example:\*\* With the following script extending from
`RichTextEffect<class_RichTextEffect>`{.interpreted-text role="ref"}:

    # effect.gd
    class_name MyCustomEffect
    extends RichTextEffect

    var bbcode = "my_custom_effect"

    # ...

The above effect can be installed in **RichTextLabel** from a script:

    # rich_text_label.gd
    extends RichTextLabel

    func _ready():
        install_effect(MyCustomEffect.new())

        # Alternatively, if not using `class_name` in the script that extends RichTextEffect:
        install_effect(preload("res://effect.gd").new())

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_invalidate_paragraph}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**invalidate_paragraph**(paragraph: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_invalidate_paragraph>`{.interpreted-text
role="ref"}

Invalidates `paragraph` and all subsequent paragraphs cache.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_is_finished}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_finished**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"}

If `threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, returns `true` if the background thread has
finished text processing, otherwise always return `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_is_menu_visible}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_menu_visible**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_RichTextLabel_method_is_menu_visible>`{.interpreted-text
role="ref"}

Returns whether the menu is visible. Use this instead of
`get_menu().visible` to improve performance (so the creation of the menu
is avoided).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_is_ready}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_ready**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_RichTextLabel_method_is_ready>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`is_finished()<class_RichTextLabel_method_is_finished>`{.interpreted-text
role="ref"} instead.

If `threaded<class_RichTextLabel_property_threaded>`{.interpreted-text
role="ref"} is enabled, returns `true` if the background thread has
finished text processing, otherwise always return `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_menu_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**menu_option**(option: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_menu_option>`{.interpreted-text
role="ref"}

Executes a given action as defined in the
`MenuItems<enum_RichTextLabel_MenuItems>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_newline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **newline**()
`🔗<class_RichTextLabel_method_newline>`{.interpreted-text role="ref"}

Adds a newline tag to the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_parse_bbcode}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**parse_bbcode**(bbcode: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_parse_bbcode>`{.interpreted-text
role="ref"}

The assignment version of
`append_text()<class_RichTextLabel_method_append_text>`{.interpreted-text
role="ref"}. Clears the tag stack and inserts the new content.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_parse_expressions_for_values}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**parse_expressions_for_values**(expressions:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_parse_expressions_for_values>`{.interpreted-text
role="ref"}

Parses BBCode parameter `expressions` into a dictionary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_pop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **pop**()
`🔗<class_RichTextLabel_method_pop>`{.interpreted-text role="ref"}

Terminates the current tag. Use after `push_*` methods to close BBCodes
manually. Does not need to follow `add_*` methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_pop_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **pop_all**()
`🔗<class_RichTextLabel_method_pop_all>`{.interpreted-text role="ref"}

Terminates all tags opened by `push_*` methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_pop_context}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**pop_context**()
`🔗<class_RichTextLabel_method_pop_context>`{.interpreted-text
role="ref"}

Terminates tags opened after the last
`push_context()<class_RichTextLabel_method_push_context>`{.interpreted-text
role="ref"} call (including context marker), or all tags if there\'s no
context marker on the stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_bgcolor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_bgcolor**(bgcolor: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_bgcolor>`{.interpreted-text
role="ref"}

Adds a `[bgcolor]` tag to the tag stack.

\*\*Note:\*\* The background color has padding applied by default, which
is controlled using
`text_highlight_h_padding<class_RichTextLabel_theme_constant_text_highlight_h_padding>`{.interpreted-text
role="ref"} and
`text_highlight_v_padding<class_RichTextLabel_theme_constant_text_highlight_v_padding>`{.interpreted-text
role="ref"}. This can lead to overlapping highlights if background
colors are placed on neighboring lines/columns, so consider setting
those theme items to `0` if you want to avoid this.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_bold}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **push_bold**()
`🔗<class_RichTextLabel_method_push_bold>`{.interpreted-text role="ref"}

Adds a `[font]` tag with a bold font to the tag stack. This is the same
as adding a `[b]` tag if not currently in a `[i]` tag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_bold_italics}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_bold_italics**()
`🔗<class_RichTextLabel_method_push_bold_italics>`{.interpreted-text
role="ref"}

Adds a `[font]` tag with a bold italics font to the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_cell}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **push_cell**()
`🔗<class_RichTextLabel_method_push_cell>`{.interpreted-text role="ref"}

Adds a `[cell]` tag to the tag stack. Must be inside a `[table]` tag.
See
`push_table()<class_RichTextLabel_method_push_table>`{.interpreted-text
role="ref"} for details. Use
`set_table_column_expand()<class_RichTextLabel_method_set_table_column_expand>`{.interpreted-text
role="ref"} to set column expansion ratio,
`set_cell_border_color()<class_RichTextLabel_method_set_cell_border_color>`{.interpreted-text
role="ref"} to set cell border,
`set_cell_row_background_color()<class_RichTextLabel_method_set_cell_row_background_color>`{.interpreted-text
role="ref"} to set cell background,
`set_cell_size_override()<class_RichTextLabel_method_set_cell_size_override>`{.interpreted-text
role="ref"} to override cell size, and
`set_cell_padding()<class_RichTextLabel_method_set_cell_padding>`{.interpreted-text
role="ref"} to set padding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_color**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_color>`{.interpreted-text
role="ref"}

Adds a `[color]` tag to the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_context}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_context**()
`🔗<class_RichTextLabel_method_push_context>`{.interpreted-text
role="ref"}

Adds a context marker to the tag stack. See
`pop_context()<class_RichTextLabel_method_pop_context>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_customfx}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_customfx**(effect:
`RichTextEffect<class_RichTextEffect>`{.interpreted-text role="ref"},
env: `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_push_customfx>`{.interpreted-text
role="ref"}

Adds a custom effect tag to the tag stack. The effect does not need to
be in
`custom_effects<class_RichTextLabel_property_custom_effects>`{.interpreted-text
role="ref"}. The environment is directly passed to the effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_dropcap}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_dropcap**(string: `String<class_String>`{.interpreted-text
role="ref"}, font: `Font<class_Font>`{.interpreted-text role="ref"},
size: `int<class_int>`{.interpreted-text role="ref"}, dropcap_margins:
`Rect2<class_Rect2>`{.interpreted-text role="ref"} = Rect2(0, 0, 0, 0),
color: `Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1,
1, 1), outline_size: `int<class_int>`{.interpreted-text role="ref"} = 0,
outline_color: `Color<class_Color>`{.interpreted-text role="ref"} =
Color(0, 0, 0, 0))
`🔗<class_RichTextLabel_method_push_dropcap>`{.interpreted-text
role="ref"}

Adds a `[dropcap]` tag to the tag stack. Drop cap (dropped capital) is a
decorative element at the beginning of a paragraph that is larger than
the rest of the text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_fgcolor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_fgcolor**(fgcolor: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_fgcolor>`{.interpreted-text
role="ref"}

Adds a `[fgcolor]` tag to the tag stack.

\*\*Note:\*\* The foreground color has padding applied by default, which
is controlled using
`text_highlight_h_padding<class_RichTextLabel_theme_constant_text_highlight_h_padding>`{.interpreted-text
role="ref"} and
`text_highlight_v_padding<class_RichTextLabel_theme_constant_text_highlight_v_padding>`{.interpreted-text
role="ref"}. This can lead to overlapping highlights if foreground
colors are placed on neighboring lines/columns, so consider setting
those theme items to `0` if you want to avoid this.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_font}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_font**(font: `Font<class_Font>`{.interpreted-text role="ref"},
font_size: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_RichTextLabel_method_push_font>`{.interpreted-text role="ref"}

Adds a `[font]` tag to the tag stack. Overrides default fonts for its
duration.

Passing `0` to `font_size` will use the existing default font size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_font_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_font_size**(font_size: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_font_size>`{.interpreted-text
role="ref"}

Adds a `[font_size]` tag to the tag stack. Overrides default font size
for its duration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_hint}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_hint**(description: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_hint>`{.interpreted-text role="ref"}

Adds a `[hint]` tag to the tag stack. Same as BBCode
`[hint=something]{text}[/hint]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_indent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_indent**(level: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_push_indent>`{.interpreted-text
role="ref"}

Adds an `[indent]` tag to the tag stack. Multiplies `level` by current
`tab_size<class_RichTextLabel_property_tab_size>`{.interpreted-text
role="ref"} to determine new margin length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_italics}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_italics**()
`🔗<class_RichTextLabel_method_push_italics>`{.interpreted-text
role="ref"}

Adds a `[font]` tag with an italics font to the tag stack. This is the
same as adding an `[i]` tag if not currently in a `[b]` tag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_language}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_language**(language: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_language>`{.interpreted-text
role="ref"}

Adds language code used for text shaping algorithm and Open-Type font
features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_list}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_list**(level: `int<class_int>`{.interpreted-text role="ref"},
type: `ListType<enum_RichTextLabel_ListType>`{.interpreted-text
role="ref"}, capitalize: `bool<class_bool>`{.interpreted-text
role="ref"}, bullet: `String<class_String>`{.interpreted-text
role="ref"} = \"•\")
`🔗<class_RichTextLabel_method_push_list>`{.interpreted-text role="ref"}

Adds `[ol]` or `[ul]` tag to the tag stack. Multiplies `level` by
current
`tab_size<class_RichTextLabel_property_tab_size>`{.interpreted-text
role="ref"} to determine new margin length.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_meta}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_meta**(data: `Variant<class_Variant>`{.interpreted-text
role="ref"}, underline_mode:
`MetaUnderline<enum_RichTextLabel_MetaUnderline>`{.interpreted-text
role="ref"} = 1, tooltip: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`🔗<class_RichTextLabel_method_push_meta>`{.interpreted-text role="ref"}

Adds a meta tag to the tag stack. Similar to the BBCode
`[url=something]{text}[/url]`, but supports
non-`String<class_String>`{.interpreted-text role="ref"} metadata types.

If
`meta_underlined<class_RichTextLabel_property_meta_underlined>`{.interpreted-text
role="ref"} is `true`, meta tags display an underline. This behavior can
be customized with `underline_mode`.

\*\*Note:\*\* Meta tags do nothing by default when clicked. To assign
behavior when clicked, connect
`meta_clicked<class_RichTextLabel_signal_meta_clicked>`{.interpreted-text
role="ref"} to a function that is called when the meta tag is clicked.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_mono}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **push_mono**()
`🔗<class_RichTextLabel_method_push_mono>`{.interpreted-text role="ref"}

Adds a `[font]` tag with a monospace font to the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_normal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_normal**()
`🔗<class_RichTextLabel_method_push_normal>`{.interpreted-text
role="ref"}

Adds a `[font]` tag with a normal font to the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_outline_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_outline_color**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_outline_color>`{.interpreted-text
role="ref"}

Adds a `[outline_color]` tag to the tag stack. Adds text outline for its
duration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_outline_size}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_outline_size**(outline_size: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_push_outline_size>`{.interpreted-text
role="ref"}

Adds a `[outline_size]` tag to the tag stack. Overrides default text
outline size for its duration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_paragraph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_paragraph**(alignment:
`HorizontalAlignment<enum_@GlobalScope_HorizontalAlignment>`{.interpreted-text
role="ref"}, base_direction:
`TextDirection<enum_Control_TextDirection>`{.interpreted-text
role="ref"} = 0, language: `String<class_String>`{.interpreted-text
role="ref"} = \"\", st_parser:
`StructuredTextParser<enum_TextServer_StructuredTextParser>`{.interpreted-text
role="ref"} = 0, justification_flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`JustificationFlag<enum_TextServer_JustificationFlag>`{.interpreted-text
role="ref"}\] = 163, tab_stops:
`PackedFloat32Array<class_PackedFloat32Array>`{.interpreted-text
role="ref"} = PackedFloat32Array())
`🔗<class_RichTextLabel_method_push_paragraph>`{.interpreted-text
role="ref"}

Adds a `[p]` tag to the tag stack.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_strikethrough}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_strikethrough**(color: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(0, 0, 0, 0))
`🔗<class_RichTextLabel_method_push_strikethrough>`{.interpreted-text
role="ref"}

Adds a `[s]` tag to the tag stack. If `color` alpha value is zero,
current font color with alpha multiplied by
`strikethrough_alpha<class_RichTextLabel_theme_constant_strikethrough_alpha>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_table}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_table**(columns: `int<class_int>`{.interpreted-text role="ref"},
inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} = 0, align_to_row: `int<class_int>`{.interpreted-text
role="ref"} = -1, name: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`🔗<class_RichTextLabel_method_push_table>`{.interpreted-text
role="ref"}

Adds a `[table=columns,inline_align]` tag to the tag stack. Use
`set_table_column_expand()<class_RichTextLabel_method_set_table_column_expand>`{.interpreted-text
role="ref"} to set column expansion ratio. Use
`push_cell()<class_RichTextLabel_method_push_cell>`{.interpreted-text
role="ref"} to add cells. `name` is used as the table name for assistive
apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_push_underline}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_underline**(color: `Color<class_Color>`{.interpreted-text
role="ref"} = Color(0, 0, 0, 0))
`🔗<class_RichTextLabel_method_push_underline>`{.interpreted-text
role="ref"}

Adds a `[u]` tag to the tag stack. If `color` alpha value is zero,
current font color with alpha multiplied by
`underline_alpha<class_RichTextLabel_theme_constant_underline_alpha>`{.interpreted-text
role="ref"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_reload_effects}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reload_effects**()
`🔗<class_RichTextLabel_method_reload_effects>`{.interpreted-text
role="ref"}

Reloads custom effects. Useful when
`custom_effects<class_RichTextLabel_property_custom_effects>`{.interpreted-text
role="ref"} is modified manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_remove_paragraph}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**remove_paragraph**(paragraph: `int<class_int>`{.interpreted-text
role="ref"}, no_invalidate: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_RichTextLabel_method_remove_paragraph>`{.interpreted-text
role="ref"}

Removes a paragraph of content from the label. Returns `true` if the
paragraph exists.

The `paragraph` argument is the index of the paragraph to remove, it can
take values in the interval `[0, get_paragraph_count() - 1]`.

If `no_invalidate` is set to `true`, cache for the subsequent paragraphs
is not invalidated. Use it for faster updates if deleted paragraph is
fully self-contained (have no unclosed tags), or this call is part of
the complex edit operation and
`invalidate_paragraph()<class_RichTextLabel_method_invalidate_paragraph>`{.interpreted-text
role="ref"} will be called at the end of operation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_scroll_to_line}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scroll_to_line**(line: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_scroll_to_line>`{.interpreted-text
role="ref"}

Scrolls the window\'s top line to match `line`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_scroll_to_paragraph}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scroll_to_paragraph**(paragraph: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_scroll_to_paragraph>`{.interpreted-text
role="ref"}

Scrolls the window\'s top line to match first line of the `paragraph`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_scroll_to_selection}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scroll_to_selection**()
`🔗<class_RichTextLabel_method_scroll_to_selection>`{.interpreted-text
role="ref"}

Scrolls to the beginning of the current selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_select_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select_all**()
`🔗<class_RichTextLabel_method_select_all>`{.interpreted-text
role="ref"}

Select all the text.

If
`selection_enabled<class_RichTextLabel_property_selection_enabled>`{.interpreted-text
role="ref"} is `false`, no selection will occur.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_set_cell_border_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell_border_color**(color: `Color<class_Color>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_set_cell_border_color>`{.interpreted-text
role="ref"}

Sets color of a table cell border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_set_cell_padding}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell_padding**(padding: `Rect2<class_Rect2>`{.interpreted-text
role="ref"})
`🔗<class_RichTextLabel_method_set_cell_padding>`{.interpreted-text
role="ref"}

Sets inner padding of a table cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_set_cell_row_background_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell_row_background_color**(odd_row_bg:
`Color<class_Color>`{.interpreted-text role="ref"}, even_row_bg:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_set_cell_row_background_color>`{.interpreted-text
role="ref"}

Sets color of a table cell. Separate colors for alternating rows can be
specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_set_cell_size_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_cell_size_override**(min_size:
`Vector2<class_Vector2>`{.interpreted-text role="ref"}, max_size:
`Vector2<class_Vector2>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_set_cell_size_override>`{.interpreted-text
role="ref"}

Sets minimum and maximum size overrides for a table cell.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_set_table_column_expand}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_table_column_expand**(column: `int<class_int>`{.interpreted-text
role="ref"}, expand: `bool<class_bool>`{.interpreted-text role="ref"},
ratio: `int<class_int>`{.interpreted-text role="ref"} = 1, shrink:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_RichTextLabel_method_set_table_column_expand>`{.interpreted-text
role="ref"}

Edits the selected column\'s expansion options. If `expand` is `true`,
the column expands in proportion to its expansion ratio versus the other
columns\' ratios.

For example, 2 columns with ratios 3 and 4 plus 70 pixels in available
width would expand 30 and 40 pixels, respectively.

If `expand` is `false`, the column will not contribute to the total
ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_set_table_column_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_table_column_name**(column: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_RichTextLabel_method_set_table_column_name>`{.interpreted-text
role="ref"}

Sets table column name for assistive apps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_method_update_image}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_image**(key: `Variant<class_Variant>`{.interpreted-text
role="ref"}, mask:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ImageUpdateMask<enum_RichTextLabel_ImageUpdateMask>`{.interpreted-text
role="ref"}\], image: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}, width: `int<class_int>`{.interpreted-text role="ref"} = 0,
height: `int<class_int>`{.interpreted-text role="ref"} = 0, color:
`Color<class_Color>`{.interpreted-text role="ref"} = Color(1, 1, 1, 1),
inline_align:
`InlineAlignment<enum_@GlobalScope_InlineAlignment>`{.interpreted-text
role="ref"} = 5, region: `Rect2<class_Rect2>`{.interpreted-text
role="ref"} = Rect2(0, 0, 0, 0), pad:
`bool<class_bool>`{.interpreted-text role="ref"} = false, tooltip:
`String<class_String>`{.interpreted-text role="ref"} = \"\",
width_in_percent: `bool<class_bool>`{.interpreted-text role="ref"} =
false, height_in_percent: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_RichTextLabel_method_update_image>`{.interpreted-text
role="ref"}

Updates the existing images with the key `key`. Only properties
specified by `mask` bits are updated. See
`add_image()<class_RichTextLabel_method_add_image>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_RichTextLabel_theme_color_default_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **default_color** =
`Color(1, 1, 1, 1)`
`🔗<class_RichTextLabel_theme_color_default_color>`{.interpreted-text
role="ref"}

The default text color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_color_font_outline_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_outline_color** = `Color(0, 0, 0, 1)`
`🔗<class_RichTextLabel_theme_color_font_outline_color>`{.interpreted-text
role="ref"}

The default tint of text outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_color_font_selected_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**font_selected_color** = `Color(0, 0, 0, 0)`
`🔗<class_RichTextLabel_theme_color_font_selected_color>`{.interpreted-text
role="ref"}

The color of selected text, used when
`selection_enabled<class_RichTextLabel_property_selection_enabled>`{.interpreted-text
role="ref"} is `true`. If equal to `Color(0, 0, 0, 0)`, it will be
ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_color_font_shadow_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **font_shadow_color**
= `Color(0, 0, 0, 0)`
`🔗<class_RichTextLabel_theme_color_font_shadow_color>`{.interpreted-text
role="ref"}

The color of the font\'s shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_color_selection_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **selection_color** =
`Color(0.1, 0.1, 1, 0.8)`
`🔗<class_RichTextLabel_theme_color_selection_color>`{.interpreted-text
role="ref"}

The color of the selection box.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_color_table_border}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **table_border** =
`Color(0, 0, 0, 0)`
`🔗<class_RichTextLabel_theme_color_table_border>`{.interpreted-text
role="ref"}

The default cell border color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_color_table_even_row_bg}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **table_even_row_bg**
= `Color(0, 0, 0, 0)`
`🔗<class_RichTextLabel_theme_color_table_even_row_bg>`{.interpreted-text
role="ref"}

The default background color for even rows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_color_table_odd_row_bg}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **table_odd_row_bg**
= `Color(0, 0, 0, 0)`
`🔗<class_RichTextLabel_theme_color_table_odd_row_bg>`{.interpreted-text
role="ref"}

The default background color for odd rows.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_line_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **line_separation** = `0`
`🔗<class_RichTextLabel_theme_constant_line_separation>`{.interpreted-text
role="ref"}

Additional vertical spacing between lines (in pixels), spacing is added
to line descent. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **outline_size** = `0`
`🔗<class_RichTextLabel_theme_constant_outline_size>`{.interpreted-text
role="ref"}

The size of the text outline.

\*\*Note:\*\* If using a font with
`FontFile.multichannel_signed_distance_field<class_FontFile_property_multichannel_signed_distance_field>`{.interpreted-text
role="ref"} enabled, its
`FontFile.msdf_pixel_range<class_FontFile_property_msdf_pixel_range>`{.interpreted-text
role="ref"} must be set to at least *twice* the value of
`outline_size<class_RichTextLabel_theme_constant_outline_size>`{.interpreted-text
role="ref"} for outline rendering to look correct. Otherwise, the
outline may appear to be cut off earlier than intended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_paragraph_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **paragraph_separation**
= `0`
`🔗<class_RichTextLabel_theme_constant_paragraph_separation>`{.interpreted-text
role="ref"}

Additional vertical spacing between paragraphs (in pixels). Spacing is
added after the last line. This value can be negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_shadow_offset_x}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_offset_x** = `1`
`🔗<class_RichTextLabel_theme_constant_shadow_offset_x>`{.interpreted-text
role="ref"}

The horizontal offset of the font\'s shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_shadow_offset_y}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_offset_y** = `1`
`🔗<class_RichTextLabel_theme_constant_shadow_offset_y>`{.interpreted-text
role="ref"}

The vertical offset of the font\'s shadow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_shadow_outline_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **shadow_outline_size** =
`1`
`🔗<class_RichTextLabel_theme_constant_shadow_outline_size>`{.interpreted-text
role="ref"}

The size of the shadow outline.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_strikethrough_alpha}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **strikethrough_alpha** =
`50`
`🔗<class_RichTextLabel_theme_constant_strikethrough_alpha>`{.interpreted-text
role="ref"}

The default strikethrough color transparency (percent). For
strikethroughs with a custom color, this theme item is only used if the
custom color\'s alpha is `0.0` (fully transparent).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_table_h_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **table_h_separation** =
`3`
`🔗<class_RichTextLabel_theme_constant_table_h_separation>`{.interpreted-text
role="ref"}

The horizontal separation of elements in a table.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_table_v_separation}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **table_v_separation** =
`3`
`🔗<class_RichTextLabel_theme_constant_table_v_separation>`{.interpreted-text
role="ref"}

The vertical separation of elements in a table.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_text_highlight_h_padding}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_highlight_h_padding** = `3`
`🔗<class_RichTextLabel_theme_constant_text_highlight_h_padding>`{.interpreted-text
role="ref"}

The horizontal padding around boxes drawn by the `[fgcolor]` and
`[bgcolor]` tags. This does not affect the appearance of text selection.
To avoid any risk of neighboring highlights overlapping each other, set
this to `0` to disable padding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_text_highlight_v_padding}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_highlight_v_padding** = `3`
`🔗<class_RichTextLabel_theme_constant_text_highlight_v_padding>`{.interpreted-text
role="ref"}

The vertical padding around boxes drawn by the `[fgcolor]` and
`[bgcolor]` tags. This does not affect the appearance of text selection.
To avoid any risk of neighboring highlights overlapping each other, set
this to `0` to disable padding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_constant_underline_alpha}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **underline_alpha** =
`50`
`🔗<class_RichTextLabel_theme_constant_underline_alpha>`{.interpreted-text
role="ref"}

The default underline color transparency (percent). For underlines with
a custom color, this theme item is only used if the custom color\'s
alpha is `0.0` (fully transparent).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_bold_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **bold_font**
`🔗<class_RichTextLabel_theme_font_bold_font>`{.interpreted-text
role="ref"}

The font used for bold text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_bold_italics_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **bold_italics_font**
`🔗<class_RichTextLabel_theme_font_bold_italics_font>`{.interpreted-text
role="ref"}

The font used for bold italics text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_italics_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **italics_font**
`🔗<class_RichTextLabel_theme_font_italics_font>`{.interpreted-text
role="ref"}

The font used for italics text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_mono_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **mono_font**
`🔗<class_RichTextLabel_theme_font_mono_font>`{.interpreted-text
role="ref"}

The font used for monospace text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_normal_font}
::: rst-class
classref-themeproperty
:::
::::

`Font<class_Font>`{.interpreted-text role="ref"} **normal_font**
`🔗<class_RichTextLabel_theme_font_normal_font>`{.interpreted-text
role="ref"}

The default text font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_size_bold_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **bold_font_size**
`🔗<class_RichTextLabel_theme_font_size_bold_font_size>`{.interpreted-text
role="ref"}

The font size used for bold text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_size_bold_italics_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**bold_italics_font_size**
`🔗<class_RichTextLabel_theme_font_size_bold_italics_font_size>`{.interpreted-text
role="ref"}

The font size used for bold italics text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_size_italics_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **italics_font_size**
`🔗<class_RichTextLabel_theme_font_size_italics_font_size>`{.interpreted-text
role="ref"}

The font size used for italics text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_size_mono_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **mono_font_size**
`🔗<class_RichTextLabel_theme_font_size_mono_font_size>`{.interpreted-text
role="ref"}

The font size used for monospace text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_font_size_normal_font_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **normal_font_size**
`🔗<class_RichTextLabel_theme_font_size_normal_font_size>`{.interpreted-text
role="ref"}

The default text font size.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_icon_horizontal_rule}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**horizontal_rule**
`🔗<class_RichTextLabel_theme_icon_horizontal_rule>`{.interpreted-text
role="ref"}

The horizontal rule texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RichTextLabel_theme_style_focus}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **focus**
`🔗<class_RichTextLabel_theme_style_focus>`{.interpreted-text
role="ref"}

The background used when the **RichTextLabel** is focused. The
`focus<class_RichTextLabel_theme_style_focus>`{.interpreted-text
role="ref"} `StyleBox<class_StyleBox>`{.interpreted-text role="ref"} is
displayed *over* the base `StyleBox<class_StyleBox>`{.interpreted-text
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

:::: {#class_RichTextLabel_theme_style_normal}
::: rst-class
classref-themeproperty
:::
::::

`StyleBox<class_StyleBox>`{.interpreted-text role="ref"} **normal**
`🔗<class_RichTextLabel_theme_style_normal>`{.interpreted-text
role="ref"}

The normal background for the **RichTextLabel**.
