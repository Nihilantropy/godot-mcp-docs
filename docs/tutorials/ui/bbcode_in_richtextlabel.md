# BBCode in RichTextLabel {#doc_bbcode_in_richtextlabel}

## Introduction

`class_Label`{.interpreted-text role="ref"} nodes are great for
displaying basic text, but they have limitations. If you want to change
the color of the text, or its alignment, you can only do that to the
entire label. You can\'t make a part of the text have another color, or
have a part of the text centered. To get around these limitations, you
would use a `class_RichTextLabel`{.interpreted-text role="ref"}.

`class_RichTextLabel`{.interpreted-text role="ref"} allows for complex
formatting of text using a markup syntax or the built-in API. It uses
BBCodes for the markup syntax, a system of tags that designate
formatting rules for a part of the text. You may be familiar with them
if you ever used forums (also known as [bulletin boards]{.title-ref},
hence the \"BB\" in \"BBCode\").

Unlike Label, RichTextLabel also comes with its own vertical scrollbar.
This scrollbar is automatically displayed if the text does not fit
within the control\'s size. The scrollbar can be disabled by unchecking
the **Scroll Active** property in the RichTextLabel inspector.

Note that the BBCode tags can also be used to some extent for other use
cases:

- BBCode can be used to
  `format comments in the XML source of the class reference <doc_class_reference_bbcode>`{.interpreted-text
  role="ref"}.
- BBCode can be used in
  `GDScript documentation comments <doc_gdscript_documentation_comments_bbcode_and_class_reference>`{.interpreted-text
  role="ref"}.
- BBCode can be used when
  `printing rich text to the Output bottom panel <doc_output_panel_printing_rich_text>`{.interpreted-text
  role="ref"}.

::: seealso
You can see how BBCode in RichTextLabel works in action using the [Rich
Text Label with BBCode demo
project](https://github.com/godotengine/godot-demo-projects/tree/master/gui/rich_text_bbcode).
:::

## Using BBCode

By default, `class_RichTextLabel`{.interpreted-text role="ref"}
functions like a normal `class_Label`{.interpreted-text role="ref"}. It
has the
`property_text <class_RichTextLabel_property_text>`{.interpreted-text
role="ref"} property, which you can edit to have uniformly formatted
text. To be able to use BBCode for rich text formatting, you need to
turn on the BBCode mode by setting
`bbcode_enabled <class_RichTextLabel_property_bbcode_enabled>`{.interpreted-text
role="ref"}. After that, you can edit the
`text <class_RichTextLabel_property_text>`{.interpreted-text role="ref"}
property using available tags. Both properties are located at the top of
the inspector after selecting a RichTextLabel node.

![image](img/bbcode_in_richtextlabel_inspector.webp)

For example, `BBCode [color=green]test[/color]` would render the word
\"test\" with a green color.

![image](img/bbcode_in_richtextlabel_basic_example.webp)

Most BBCodes consist of 3 parts: the opening tag, the content and the
closing tag. The opening tag delimits the start of the formatted part,
and can also carry some configuration options. Some opening tags, like
the `color` one shown above, also require a value to work. Other opening
tags may accept multiple options (separated by spaces within the opening
tag). The closing tag delimits the end of the formatted part. In some
cases, both the closing tag and the content can be omitted.

Unlike BBCode in HTML, leading/trailing whitespace is not removed by a
RichTextLabel upon display. Duplicate spaces are also displayed as-is in
the final output. This means that when displaying a code block in a
RichTextLabel, you don\'t need to use a preformatted text tag.

``` none
[tag]content[/tag]
[tag=value]content[/tag]
[tag option1=value1 option2=value2]content[/tag]
[tag][/tag]
[tag]
```

:::: note
::: title
Note
:::

RichTextLabel doesn\'t support entangled BBCode tags. For example,
instead of using:

    [b]bold[i]bold italic[/b]italic[/i]

Use:

    [b]bold[i]bold italic[/i][/b][i]italic[/i]
::::

## Handling user input safely {#doc_bbcode_in_richtextlabel_handling_user_input_safely}

In a scenario where users may freely input text (such as chat in a
multiplayer game), you should make sure users cannot use arbitrary
BBCode tags that will be parsed by RichTextLabel. This is to avoid
inappropriate use of formatting, which can be problematic if `[url]`
tags are handled by your RichTextLabel (as players may be able to create
clickable links to phishing sites or similar).

Using RichTextLabel\'s `[lb]` and/or `[rb]` tags, we can replace the
opening and/or closing brackets of any BBCode tag in a message with
those escaped tags. This prevents users from using BBCode that will be
parsed as tags -- instead, the BBCode will be displayed as text.

<figure class="align-center">
<img src="img/bbcode_in_richtextlabel_escaping_user_input.webp"
alt="img/bbcode_in_richtextlabel_escaping_user_input.webp" />
<figcaption>Example of unescaped user input resulting in BBCode
injection (2nd line) and escaped user input (3rd line)</figcaption>
</figure>

The above image was created using the following script:

    extends RichTextLabel

    func _ready():
        append_chat_line("Player 1", "Hello world!")
        append_chat_line("Player 2", "Hello [color=red]BBCode injection[/color] (no escaping)!")
        append_chat_line_escaped("Player 2", "Hello [color=red]BBCode injection[/color] (with escaping)!")


    # Returns escaped BBCode that won't be parsed by RichTextLabel as tags.
    func escape_bbcode(bbcode_text):
        # We only need to replace opening brackets to prevent tags from being parsed.
        return bbcode_text.replace("[", "[lb]")


    # Appends the user's message as-is, without escaping. This is dangerous!
    func append_chat_line(username, message):
        append_text("%s: [color=green]%s[/color]\n" % [username, message])


    # Appends the user's message with escaping.
    # Remember to escape both the player name and message contents.
    func append_chat_line_escaped(username, message):
        append_text("%s: [color=green]%s[/color]\n" % [escape_bbcode(username), escape_bbcode(message)])

## Stripping BBCode tags

For certain use cases, it can be desired to remove BBCode tags from the
string. This is useful when displaying the RichTextLabel\'s text in
another Control that does not support BBCode (such as a tooltip):

``` 
extends RichTextLabel

func _ready():
    var regex = RegEx.new()
    regex.compile("\\[.*?\\]")
    var text_without_tags = regex.sub(text, "", true)
    # `text_without_tags` contains the text with all BBCode tags removed.
```

:::: note
::: title
Note
:::

Removing BBCode tags entirely isn\'t advised for user input, as it can
modify the displayed text without users understanding why part of their
message was removed.
`Escaping user input <doc_bbcode_in_richtextlabel_handling_user_input_safely>`{.interpreted-text
role="ref"} should be preferred instead.
::::

## Performance

In most cases, you can use BBCode directly as-is since text formatting
is rarely a heavy task. However, with particularly large RichTextLabels
(such as console logs spanning thousands of lines), you may encounter
stuttering during gameplay when the RichTextLabel\'s text is updated.

There are several ways to alleviate this:

- Use the `append_text()` function instead of appending to the `text`
  property. This function will only parse BBCode for the added text,
  rather than parsing BBCode from the entire `text` property.
- Use `push_[tag]()` and `pop()` functions to add tags to RichTextLabel
  instead of using BBCode.
- Enable the **Threading \> Threaded** property in RichTextLabel. This
  won\'t speed up processing, but it will prevent the main thread from
  blocking, which avoids stuttering during gameplay. Only enable
  threading if it\'s actually needed in your project, as threading has
  some overhead.

## Using [push]()\[tag\]() and pop() functions instead of BBCode {#doc_bbcode_in_richtextlabel_use_functions}

If you don\'t want to use BBCode for performance reasons, you can use
functions provided by RichTextLabel to create formatting tags without
writing BBCode in the text.

Every BBCode tag (including effects) has a `push_[tag]()` function
(where `[tag]` is the tag\'s name). There are also a few convenience
functions available, such as `push_bold_italics()` that combines both
`push_bold()` and `push_italics()` into a single tag. See the
`RichTextLabel class reference <class_RichTextLabel>`{.interpreted-text
role="ref"} for a complete list of `push_[tag]()` functions.

The `pop()` function is used to end *any* tag. Since BBCode is a tag
*stack*, using `pop()` will close the most recently started tags first.

The following script will result in the same visual output as using
`BBCode [color=green]test [i]example[/i][/color]`:

    extends RichTextLabel

    func _ready():
        append_text("BBCode ")  # Trailing space separates words from each other.
        push_color(Color.GREEN)
        append_text("test ")  # Trailing space separates words from each other.
        push_italics()
        append_text("example")
        pop()  # Ends the tag opened by `push_italics()`.
        pop()  # Ends the tag opened by `push_color()`.

:::: warning
::: title
Warning
:::

Do **not** set the `text` property directly when using formatting
functions. Appending to the `text` property will erase all modifications
made to the RichTextLabel using the `append_text()`, `push_[tag]()` and
`pop()` functions.
::::

## Reference

::: seealso
*Some* of these BBCode tags can be used in tooltips for `@export` script
variables as well as in the XML source of the class reference. For more
information, see
`Class reference BBCode <doc_class_reference_bbcode>`{.interpreted-text
role="ref"}.
:::

+------------------------------------------+---------------------------+
| Tag                                      | Example                   |
+------------------------------------------+---------------------------+
| | **b**                                  | `[b]{text}[/b]`           |
| | Makes `{text}` use the bold (or bold   |                           |
|   italics) font of `RichTextLabel`.      |                           |
+------------------------------------------+---------------------------+
| | **i**                                  | `[i]{text}[/i]`           |
| | Makes `{text}` use the italics (or     |                           |
|   bold italics) font of `RichTextLabel`. |                           |
+------------------------------------------+---------------------------+
| | **u**                                  | `[u]{text}[/u]`           |
| | Makes `{text}` underlined.             |                           |
+------------------------------------------+---------------------------+
| | **s**                                  | `[s]{text}[/s]`           |
| | Makes `{text}` strikethrough.          |                           |
+------------------------------------------+---------------------------+
| | **code**                               | `[code]{text}[/code]`     |
| | Makes `{text}` use the mono font of    |                           |
|   `RichTextLabel`.                       |                           |
+------------------------------------------+---------------------------+
| | **char**                               | `[char={codepoint}]`      |
| | Adds Unicode character with            |                           |
|   hexadecimal UTF-32 `{codepoint}`.      |                           |
+------------------------------------------+---------------------------+
| | **p**                                  | | `[p]{text}[/p]`         |
| | Adds new paragraph with `{text}`.      | |                         |
|   Supports configuration options, see    | `[p {options}]{text}[/p]` |
|   `doc_bbcode_in_richtextla              |                           |
| bel_paragraph_options`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **br**                                 | `[br]`                    |
| | Adds line break in a text.             |                           |
+------------------------------------------+---------------------------+
| | **hr**                                 | | `[hr]`                  |
| | Adds new a horizontal rule to separate | | `[hr {options}]`        |
|   content. Supports configuration        |                           |
|   options, see                           |                           |
|   `doc_bbcode_in_ric                     |                           |
| htextlabel_hr_options`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **center**                             | `[center]{text}[/center]` |
| | Makes `{text}` horizontally centered.  |                           |
| | Same as `[p align=center]`.            |                           |
+------------------------------------------+---------------------------+
| | **left**                               | `[left]{text}[/left]`     |
| | Makes `{text}` horizontally            |                           |
|   left-aligned.                          |                           |
| | Same as `[p align=left]`.              |                           |
+------------------------------------------+---------------------------+
| | **right**                              | `[right]{text}[/right]`   |
| | Makes `{text}` horizontally            |                           |
|   right-aligned.                         |                           |
| | Same as `[p align=right]`.             |                           |
+------------------------------------------+---------------------------+
| | **fill**                               | `[fill]{text}[/fill]`     |
| | Makes `{text}` fill the full width of  |                           |
|   `RichTextLabel`.                       |                           |
| | Same as `[p align=fill]`.              |                           |
+------------------------------------------+---------------------------+
| | **indent**                             | `[indent]{text}[/indent]` |
| | Indents `{text}` once. The indentation |                           |
|   width is the same as with `[ul]` or    |                           |
|   `[ol]`, but without a bullet point.    |                           |
+------------------------------------------+---------------------------+
| | **url**                                | | `[url]{link}[/url]`     |
| | Creates a hyperlink (underlined and    | | `                       |
|   clickable text). Can contain optional  | [url={link}]{text}[/url]` |
|   `{text}` or display `{link}` as is.    |                           |
| | **Must be handled with the             |                           |
|   \"meta_clicked\" signal to have an     |                           |
|   effect,** see                          |                           |
|   `doc_bbcode_in_richtextlabel_ha        |                           |
| ndling_url_tag_clicks`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **hint**                               | | `[hint=                 |
| | Creates a tooltip hint that is         | "{tooltip text displayed  |
|   displayed when hovering the text with  | on hover}"]{text}[/hint]` |
|   the mouse. While not required, it\'s   |                           |
|   recommended to put tooltip text        |                           |
|   between double or single quotes. Note  |                           |
|   that it is not possible to escape      |                           |
|   quotes using `\"` or `\'`. To use      |                           |
|   single quotes for apostrophes in the   |                           |
|   hint string, you must use double       |                           |
|   quotes to surround the string.         |                           |
+------------------------------------------+---------------------------+
| | **img**                                | | `[img]{path}[/img]`     |
| | Inserts an image from the `{path}`     | | `[                      |
|   (can be any valid                      | img={width}]{path}[/img]` |
|   `class_Texture2D`{.interpreted-text    | | `[img={widt             |
|   role="ref"} resource).                 | h}x{height}]{path}[/img]` |
| | If `{width}` is provided, the image    | | `[i                     |
|   will try to fit that width maintaining | mg={valign}]{path}[/img]` |
|   the aspect ratio.                      | | `[im                    |
| | If both `{width}` and `{height}` are   | g {options}]{path}[/img]` |
|   provided, the image will be scaled to  |                           |
|   that size.                             |                           |
| | Add `%` to the end of `{width}` or     |                           |
|   `{height}` value to specify it as      |                           |
|   percentages of the control width       |                           |
|   instead of pixels.                     |                           |
| | If `{valign}` configuration is         |                           |
|   provided, the image will try to align  |                           |
|   to the surrounding text, see           |                           |
|   `doc_bbcode_in_richtextlabel_imag      |                           |
| e_and_table_alignment`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
| | Supports configuration options, see    |                           |
|   `doc_bbcode_in_richte                  |                           |
| xtlabel_image_options`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **font**                               | | `[f                     |
| | Makes `{text}` use a font resource     | ont={path}]{text}[/font]` |
|   from the `{path}`.                     | | `[font                  |
| | Supports configuration options, see    |  {options}]{text}[/font]` |
|   `doc_bbcode_in_richt                   |                           |
| extlabel_font_options`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **font_size**                          | `[font_size={             |
| | Use custom font size for `{text}`.     | size}]{text}[/font_size]` |
+------------------------------------------+---------------------------+
| | **dropcap**                            | `[dropcap font={font} fon |
| | Use a different font size and color    | t_size={size} color={colo |
|   for `{text}`, while making the tag\'s  | r} outline_size={size} ou |
|   contents span multiple lines if it\'s  | tline_color={color} margi |
|   large enough.                          | ns={left},{top},{right},{ |
| | A [drop                                | bottom}]{text}[/dropcap]` |
|   cap](https://ww                        |                           |
| w.computerhope.com/jargon/d/dropcap.htm) |                           |
|   is typically one uppercase character,  |                           |
|   but `[dropcap]` supports containing    |                           |
|   multiple characters. `margins` values  |                           |
|   are comma-separated and can be         |                           |
|   positive, zero or negative. Values     |                           |
|   must **not** be separated by spaces;   |                           |
|   otherwise, the values won\'t be parsed |                           |
|   correctly. Negative top and bottom     |                           |
|   margins are particularly useful to     |                           |
|   allow the rest of the paragraph to     |                           |
|   display below the dropcap.             |                           |
+------------------------------------------+---------------------------+
| | **opentype_features**                  | | `[o                     |
| | Enables custom OpenType font features  | pentype_features={list}]` |
|   for `{text}`. Features must be         | | `{text}`                |
|   provided as a comma-separated          | | `[/opentype_features]`  |
|   `{list}`. Values must **not** be       |                           |
|   separated by spaces; otherwise, the    |                           |
|   list won\'t be parsed correctly.       |                           |
+------------------------------------------+---------------------------+
| | **lang**                               | `[l                       |
| | Overrides the language for `{text}`    | ang={code}]{text}[/lang]` |
|   that is set by the **BiDi \>           |                           |
|   Language** property in                 |                           |
|                                          |                           |
|  `class_RichTextLabel`{.interpreted-text |                           |
|   role="ref"}. `{code}` must be an ISO   |                           |
|   `langua                                |                           |
| ge code <doc_locales>`{.interpreted-text |                           |
|   role="ref"}. This can be used to       |                           |
|   enforce the use of a specific script   |                           |
|   for a language without starting a new  |                           |
|   paragraph. Some font files may contain |                           |
|   script-specific substitutes, in which  |                           |
|   case they will be used.                |                           |
+------------------------------------------+---------------------------+
| | **color**                              | `[color={c                |
| | Changes the color of `{text}`. Color   | ode/name}]{text}[/color]` |
|   must be provided by a common name (see |                           |
|   `doc_bbcode_in_richt                   |                           |
| extlabel_named_colors`{.interpreted-text |                           |
|   role="ref"}) or using the HEX format   |                           |
|   (e.g. `#ff00ff`, see                   |                           |
|   `doc_bbcode_in_ric                     |                           |
| htextlabel_hex_colors`{.interpreted-text |                           |
|   role="ref"}).                          |                           |
+------------------------------------------+---------------------------+
| | **bgcolor**                            | `[bgcolor={cod            |
| | Draws the color behind `{text}`. This  | e/name}]{text}[/bgcolor]` |
|   can be used to highlight text. Accepts |                           |
|   same values as the `color` tag. By     |                           |
|   default, there is a slight padding     |                           |
|   which is controlled by the             |                           |
|   `text_highlight_h_padding` and         |                           |
|   `text_highlight_v_padding` theme items |                           |
|   in the RichTextLabel node. Set padding |                           |
|   to `0` to avoid potential overlapping  |                           |
|   issues when there are background       |                           |
|   colors on neighboring lines/columns.   |                           |
+------------------------------------------+---------------------------+
| | **fgcolor**                            | `[fgcolor={cod            |
| | Draws the color in front of `{text}`.  | e/name}]{text}[/fgcolor]` |
|   This can be used to \"redact\" text by |                           |
|   using an opaque foreground color.      |                           |
|   Accepts same values as the `color`     |                           |
|   tag. By default, there is a slight     |                           |
|   padding which is controlled by the     |                           |
|   `text_highlight_h_padding` and         |                           |
|   `text_highlight_v_padding` theme items |                           |
|   in the RichTextLabel node. Set padding |                           |
|   to `0` to avoid potential overlapping  |                           |
|   issues when there are foreground       |                           |
|   colors on neighboring lines/columns.   |                           |
+------------------------------------------+---------------------------+
| | **outline_size**                       | | `[outline_size={size}]` |
| | Use custom font outline size for       | | `{text}`                |
|   `{text}`.                              | | `[/outline_size]`       |
+------------------------------------------+---------------------------+
| | **outline_color**                      | | `[ou                    |
| | Use custom outline color for `{text}`. | tline_color={code/name}]` |
|   Accepts same values as the `color`     | | `{text}`                |
|   tag.                                   | | `[/outline_color]`      |
+------------------------------------------+---------------------------+
| | **table**                              | | `[table=                |
| | Creates a table with the `{number}` of | {number}]{cells}[/table]` |
|   columns. Use the `cell` tag to define  | | `[table={number},       |
|   table cells.                           | {valign}]{cells}[/table]` |
| | If `{valign}` configuration is         | | `[table=                |
|   provided, the table will try to align  | {number},{valign},{alignm |
|   to the surrounding text, see           | ent_row}]{cells}[/table]` |
|   `doc_bbcode_in_richtextlabel_imag      |                           |
| e_and_table_alignment`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
| | If baseline alignment is used, the     |                           |
|   table is aligned to the baseline of    |                           |
|   the row with index `{alignment_row}`   |                           |
|   (zero-based).                          |                           |
+------------------------------------------+---------------------------+
| | **cell**                               | | `[cell]{text}[/cell]`   |
| | Adds a cell with `{text}` to the       | | `[ce                    |
|   table.                                 | ll={ratio}]{text}[/cell]` |
| | If `{ratio}` is provided, the cell     | | `[cell                  |
|   will try to expand to that value       |  {options}]{text}[/cell]` |
|   proportionally to other cells and      |                           |
|   their ratio values.                    |                           |
| | Supports configuration options, see    |                           |
|   `doc_bbcode_in_richt                   |                           |
| extlabel_cell_options`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **ul**                                 | | `[ul]{items}[/ul]`      |
| | Adds an unordered list. List `{items}` | | `[ul bull               |
|   must be provided by putting one item   | et={bullet}]{items}[/ul]` |
|   per line of text.                      |                           |
| | The bullet point can be customized     |                           |
|   using the `{bullet}` parameter, see    |                           |
|   `doc_bbcode_in_richtextlabel_          |                           |
| unordered_list_bullet`{.interpreted-text |                           |
|   role="ref"}.                           |                           |
+------------------------------------------+---------------------------+
| | **ol**                                 | `[ol                      |
| | Adds an ordered (numbered) list of the | type={type}]{items}[/ol]` |
|   given `{type}` (see                    |                           |
|   `doc_bbcode_in_ric                     |                           |
| htextlabel_list_types`{.interpreted-text |                           |
|   role="ref"}). List `{items}` must be   |                           |
|   provided by putting one item per line  |                           |
|   of text.                               |                           |
+------------------------------------------+---------------------------+
| | **lb**, **rb**                         | |                         |
| | Adds `[` and `]` respectively. Allows  | `[lb]b[rb]text[lb]/b[rb]` |
|   escaping BBCode markup.                |   will display as         |
| | These are self-closing tags, which     |   `[b]text[/b]`.          |
|   means you do not need to close them    |                           |
|   (and there is no `[/lb]` or `[/rb]`    |                           |
|   closing tag).                          |                           |
+------------------------------------------+---------------------------+
| | Several Unicode control characters can | | `[lrm]` (left-to-right  |
|   be added using their own self-closing  |   mark), `[rlm]`          |
|   tags.                                  |   (right-to-left mark),   |
| | This can result in easier maintenance  |   `[lre]` (left-to-right  |
|   compared to pasting those              |   embedding),             |
| | control characters directly in the     | | `[rle]` (right-to-left  |
|   text.                                  |   embedding), `[lro]`     |
|                                          |   (left-to-right          |
|                                          |   override), `[rlo]`      |
|                                          |   (right-to-left          |
|                                          |   override),              |
|                                          | | `[pdf]` (pop            |
|                                          |   directional             |
|                                          |   formatting), `[alm]`    |
|                                          |   (Arabic letter mark),   |
|                                          |   `[lri]` (left-to-right  |
|                                          |   isolate),               |
|                                          | | `[rli]` (right-to-left  |
|                                          |   isolate), `[fsi]`       |
|                                          |   (first strong isolate), |
|                                          |   `[pdi]` (pop            |
|                                          |   directional isolate),   |
|                                          | | `[zwj]` (zero-width     |
|                                          |   joiner), `[zwnj]`       |
|                                          |   (zero-width             |
|                                          |   non-joiner), `[wj]`     |
|                                          |   (word joiner),          |
|                                          | | `[shy]` (soft hyphen)   |
+------------------------------------------+---------------------------+

:::: note
::: title
Note
:::

Tags for bold (`[b]`) and italics (`[i]`) formatting work best if the
appropriate custom fonts are set up in the RichTextLabelNode\'s theme
overrides. If no custom bold or italic fonts are defined, [faux bold and
italic
fonts](https://fonts.google.com/knowledge/glossary/faux_fake_pseudo_synthesized)
will be generated by Godot. These fonts rarely look good in comparison
to hand-made bold/italic font variants.

The monospaced (`[code]`) tag **only** works if a custom font is set up
in the RichTextLabel node\'s theme overrides. Otherwise, monospaced text
will use the regular font.

There are no BBCode tags to control vertical centering of text yet.

Options can be skipped for all tags.
::::

### Paragraph options {#doc_bbcode_in_richtextlabel_paragraph_options}

- **align**

    ----------------------- --------------------------------------------------------------
    [Values]{.title-ref}    `left` (or `l`), `center` (or `c`), `right` (or `r`), `fill`
                            (or `f`)

    [Default]{.title-ref}   `left`
    ----------------------- --------------------------------------------------------------

  Text horizontal alignment.

- **bidi_override**, **st**

    ----------------------- ----------------------------------------------------------------
    [Values]{.title-ref}    `default` (of `d`), `uri` (or `u`), `file` (or `f`), `email` (or
                            `e`), `list` (or `l`), `none` (or `n`), `custom` (or `c`)

    [Default]{.title-ref}   `default`
    ----------------------- ----------------------------------------------------------------

  Structured text override.

- **justification_flags**, **jst**

    ----------------------- ---------------------------------------------------------------
    [Values]{.title-ref}    Comma-separated list of the following values (no space after
                            each comma): `kashida` (or `k`), `word` (or `w`), `trim` (or
                            `tr`), `after_last_tab` (or `lt`), `skip_last` (or `sl`),
                            `skip_last_with_chars` (or `sv`), `do_not_skip_single` (or
                            `ns`).

    [Default]{.title-ref}   `word,kashida,skip_last,do_not_skip_single`
    ----------------------- ---------------------------------------------------------------

  Justification (fill alignment) option. See
  `class_TextServer`{.interpreted-text role="ref"} for more details.

- **direction**, **dir**

    ----------------------- ------------------------------------------------------------
    [Values]{.title-ref}    `ltr` (or `l`), `rtl` (or `r`), `auto` (or `a`)

    [Default]{.title-ref}   Inherit
    ----------------------- ------------------------------------------------------------

  Base BiDi direction.

- **language**, **lang**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    ISO language codes. See
                            `doc_locales`{.interpreted-text role="ref"}

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Locale override. Some font files may contain script-specific
  substitutes, in which case they will be used.

- **tab_stops**

    ----------------------- ----------------------------------------------------
    [Values]{.title-ref}    List of floating-point numbers, e.g. `10.0,30.0`

    [Default]{.title-ref}   Width of the space character in the font
    ----------------------- ----------------------------------------------------

  Overrides the horizontal offsets for each tab character. When the end
  of the list is reached, the tab stops will loop over. For example, if
  you set `tab_stops` to `10.0,30.0`, the first tab will be at `10`
  pixels, the second tab will be at `10 + 30 = 40` pixels, and the third
  tab will be at `10 + 30 + 10 = 50` pixels from the origin of the
  RichTextLabel.

### Handling `[url]` tag clicks {#doc_bbcode_in_richtextlabel_handling_url_tag_clicks}

By default, `[url]` tags do nothing when clicked. This is to allow
flexible use of `[url]` tags rather than limiting them to opening URLs
in a web browser.

To handle clicked `[url]` tags, connect the `RichTextLabel` node\'s
`meta_clicked <class_RichTextLabel_signal_meta_clicked>`{.interpreted-text
role="ref"} signal to a script function.

For example, the following method can be connected to `meta_clicked` to
open clicked URLs using the user\'s default web browser:

    # This assumes RichTextLabel's `meta_clicked` signal was connected to
    # the function below using the signal connection dialog.
    func _richtextlabel_on_meta_clicked(meta):
        # `meta` is not guaranteed to be a String, so convert it to a String
        # to avoid script errors at runtime.
        OS.shell_open(str(meta))

For more advanced use cases, it\'s also possible to store JSON in a
`[url]` tag\'s option and parse it in the function that handles the
`meta_clicked` signal. For example:

``` none
[url={"example": "value"}]JSON[/url]
```

### Horizontal rule options {#doc_bbcode_in_richtextlabel_hr_options}

- **color**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Color name or color in HEX format

    [Default]{.title-ref}   `Color(1, 1, 1, 1)`
    ----------------------- --------------------------------------------

  Color tint of the rule (modulation).

- **height**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Integer number

    [Default]{.title-ref}   `2`
    ----------------------- --------------------------------------------

  Target height of the rule in pixels, add `%` to the end of value to
  specify it as percentages of the control width instead of pixels.

- **width**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Integer number

    [Default]{.title-ref}   `90%`
    ----------------------- --------------------------------------------

  Target width of the rule in pixels, add `%` to the end of value to
  specify it as percentages of the control width instead of pixels.

- **align**

    ----------------------- --------------------------------------------------------------
    [Values]{.title-ref}    `left` (or `l`), `center` (or `c`), `right` (or `r`)

    [Default]{.title-ref}   `left`
    ----------------------- --------------------------------------------------------------

  Horizontal alignment.

### Image options {#doc_bbcode_in_richtextlabel_image_options}

- **color**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Color name or color in HEX format

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Color tint of the image (modulation).

- **height**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Integer number

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Target height of the image in pixels, add `%` to the end of value to
  specify it as percentages of the control width instead of pixels.

- **width**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Integer number

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Target width of the image in pixels, add `%` to the end of value to
  specify it as percentages of the control width instead of pixels.

- **region**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    x,y,width,height in pixels

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Region rect of the image. This can be used to display a single image
  from a spritesheet.

- **pad**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    `false`, `true`

    [Default]{.title-ref}   `false`
    ----------------------- --------------------------------------------

  If set to `true`, and the image is smaller than the size specified by
  `width` and `height`, the image padding is added to match the size
  instead of upscaling.

- **tooltip**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    String

    [Default]{.title-ref}   
    ----------------------- --------------------------------------------

  Image tooltip.

### Image and table vertical alignment {#doc_bbcode_in_richtextlabel_image_and_table_alignment}

When a vertical alignment value is provided with the `[img]` or
`[table]` tag the image/table will try to align itself against the
surrounding text. Alignment is performed using a vertical point of the
image and a vertical point of the text. There are 3 possible points on
the image (`top`, `center`, and `bottom`) and 4 possible points on the
text and table (`top`, `center`, `baseline`, and `bottom`), which can be
used in any combination.

To specify both points, use their full or short names as a value of the
image/table tag:

``` none
text [img=top,bottom]...[/img] text
text [img=center,center]...[/img] text
```

![image](img/bbcode_in_richtextlabel_image_align.webp)

``` none
text [table=3,center]...[/table] text  # Center to center.
text [table=3,top,bottom]...[/table] text # Top of the table to the bottom of text.
text [table=3,baseline,baseline,1]...[/table] text # Baseline of the second row (rows use zero-based indexing) to the baseline of text.
```

![image](img/bbcode_in_richtextlabel_table_align.webp)

You can also specify just one value (`top`, `center`, or `bottom`) to
make use of a corresponding preset (`top-top`, `center-center`, and
`bottom-bottom` respectively).

Short names for the values are `t` (`top`), `c` (`center`), `l`
(`baseline`), and `b` (`bottom`).

### Font options {#doc_bbcode_in_richtextlabel_font_options}

- **name**, **n**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    A valid Font resource path.

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Font resource path.

- **size**, **s**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Number in pixels.

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Custom font size.

- **glyph_spacing**, **gl**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Number in pixels.

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Extra spacing for each glyph.

- **space_spacing**, **sp**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Number in pixels.

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Extra spacing for the space character.

- **top_spacing**, **top**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Number in pixels.

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Extra spacing at the top of the line.

- **bottom_spacing**, **bt**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Number in pixels.

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Extra spacing at the bottom of the line.

- **embolden**, **emb**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Floating-point number.

    [Default]{.title-ref}   `0.0`
    ----------------------- --------------------------------------------

  Font embolden strength, if it is not equal to zero, emboldens the font
  outlines. Negative values reduce the outline thickness.

- **face_index**, **fi**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Integer number.

    [Default]{.title-ref}   `0`
    ----------------------- --------------------------------------------

  An active face index in the TrueType / OpenType collection.

- **slant**, **sln**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Floating-point number.

    [Default]{.title-ref}   `0.0`
    ----------------------- --------------------------------------------

  Font slant strength, positive values slant glyphs to the right.
  Negative values to the left.

- **opentype_variation**, **otv**

    ----------------------- --------------------------------------------------------------
    [Values]{.title-ref}    Comma-separated list of the OpenType variation tags (no space
                            after each comma).

    [Default]{.title-ref}   
    ----------------------- --------------------------------------------------------------

  Font OpenType variation coordinates. See [OpenType variation
  tags](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg).

  Note: The value should be enclosed in `"` to allow using `=` inside
  it:

``` none
[font otv="wght=200,wdth=400"] # Sets variable font weight and width.
```

- **opentype_features**, **otf**

    ----------------------- -------------------------------------------------------------
    [Values]{.title-ref}    Comma-separated list of the OpenType feature tags (no space
                            after each comma).

    [Default]{.title-ref}   
    ----------------------- -------------------------------------------------------------

  Font OpenType features. See [OpenType features
  tags](https://docs.microsoft.com/en-us/typography/opentype/spec/featuretags).

  Note: The value should be enclosed in `"` to allow using `=` inside
  it:

``` none
[font otf="calt=0,zero=1"] # Disable contextual alternates, enable slashed zero.
```

### Named colors {#doc_bbcode_in_richtextlabel_named_colors}

For tags that allow specifying a color by name, you can use names of the
constants from the built-in `class_Color`{.interpreted-text role="ref"}
class. Named classes can be specified in a number of styles using
different casings: `DARK_RED`, `DarkRed`, and `darkred` will give the
same exact result.

See this image for a list of color constants:

![image](/img/color_constants.png)

[View at full
size](https://raw.githubusercontent.com/godotengine/godot-docs/master/img/color_constants.png)

### Hexadecimal color codes {#doc_bbcode_in_richtextlabel_hex_colors}

For opaque RGB colors, any valid 6-digit hexadecimal code is supported,
e.g. `[color=#ffffff]white[/color]`. Shorthand RGB color codes such as
`#6f2` (equivalent to `#66ff22`) are also supported.

For transparent RGB colors, any RGBA 8-digit hexadecimal code can be
used, e.g. `[color=#ffffff88]translucent white[/color]`. Note that the
alpha channel is the **last** component of the color code, not the first
one. Short RGBA color codes such as `#6f28` (equivalent to `#66ff2288`)
are supported as well.

### Cell options {#doc_bbcode_in_richtextlabel_cell_options}

- **expand**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Integer number

    [Default]{.title-ref}   1
    ----------------------- --------------------------------------------

  Cell expansion ratio. This defines which cells will try to expand to
  proportionally to other cells and their expansion ratios.

- **border**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Color name or color in HEX format

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Cell border color.

- **bg**

    ----------------------- --------------------------------------------
    [Values]{.title-ref}    Color name or color in HEX format

    [Default]{.title-ref}   Inherit
    ----------------------- --------------------------------------------

  Cell background color. For alternating odd/even row backgrounds, you
  can use `bg=odd_color,even_color`.

- **padding**

    ----------------------- -------------------------------------------------------------
    [Values]{.title-ref}    4 comma-separated floating-point numbers (no space after each
                            comma)

    [Default]{.title-ref}   `0,0,0,0`
    ----------------------- -------------------------------------------------------------

  Left, top, right, and bottom cell padding.

### Unordered list bullet {#doc_bbcode_in_richtextlabel_unordered_list_bullet}

By default, the `[ul]` tag uses the `U+2022` \"Bullet\" Unicode glyph as
the bullet character. This behavior is similar to web browsers. The
bullet character can be customized using `[ul bullet={bullet}]`. If
provided, this `{bullet}` parameter must be a *single* character with no
enclosing quotes (for example, `[bullet=*]`). Additional characters are
ignored. The bullet character\'s width does not affect the list\'s
formatting.

See [Bullet (typography) on
Wikipedia](https://en.wikipedia.org/wiki/Bullet_(typography)) for a list
of common bullet characters that you can paste directly in the `bullet`
parameter.

### Ordered list types {#doc_bbcode_in_richtextlabel_list_types}

Ordered lists can be used to automatically mark items with numbers or
letters in ascending order. This tag supports the following type
options:

- `1` - Numbers, using language specific numbering system if possible.
- `a`, `A` - Lower and upper case Latin letters.
- `i`, `I` - Lower and upper case Roman numerals.

## Text effects

BBCode can also be used to create different text effects that can
optionally be animated. Five customizable effects are provided out of
the box, and you can easily create your own. By default, animated
effects will pause
`when the SceneTree is paused <doc_pausing_games>`{.interpreted-text
role="ref"}. You can change this behavior by adjusting the
RichTextLabel\'s **Process \> Mode** property.

All examples below mention the default values for options in the listed
tag format.

:::: note
::: title
Note
:::

Text effects that move characters\' positions may result in characters
being clipped by the RichTextLabel node bounds.

You can resolve this by disabling **Control \> Layout \> Clip Contents**
in the inspector after selecting the RichTextLabel node, or ensuring
there is enough margin added around the text by using line breaks above
and below the line using the effect.
::::

### Pulse

![image](img/bbcode_in_richtextlabel_effect_pulse.webp)

Pulse creates an animated pulsing effect that multiplies each
character\'s opacity and color. It can be used to bring attention to
specific text. Its tag format is
`[pulse freq=1.0 color=#ffffff40 ease=-2.0]{text}[/pulse]`.

`freq` controls the frequency of the half-pulsing cycle (higher is
faster). A full pulsing cycle takes `2 * (1.0 / freq)` seconds. `color`
is the target color multiplier for blinking. The default mostly fades
out text, but not entirely. `ease` is the easing function exponent to
use. Negative values provide in-out easing, which is why the default is
`-2.0`.

### Wave

![image](img/bbcode_in_richtextlabel_effect_wave.webp)

Wave makes the text go up and down. Its tag format is
`[wave amp=50.0 freq=5.0 connected=1]{text}[/wave]`.

`amp` controls how high and low the effect goes, and `freq` controls how
fast the text goes up and down. A `freq` value of `0` will result in no
visible waves, and negative `freq` values won\'t display any waves
either. If `connected` is `1` (default), glyphs with ligatures will be
moved together. If `connected` is `0`, each glyph is moved individually
even if they are joined by ligatures. This can work around certain
rendering issues with font ligatures.

### Tornado

![image](img/bbcode_in_richtextlabel_effect_tornado.webp)

Tornado makes the text move around in a circle. Its tag format is
`[tornado radius=10.0 freq=1.0 connected=1]{text}[/tornado]`.

`radius` is the radius of the circle that controls the offset, `freq` is
how fast the text moves in a circle. A `freq` value of `0` will pause
the animation, while negative `freq` will play the animation backwards.
If `connected` is `1` (default), glyphs with ligatures will be moved
together. If `connected` is `0`, each glyph is moved individually even
if they are joined by ligatures. This can work around certain rendering
issues with font ligatures.

### Shake

![image](img/bbcode_in_richtextlabel_effect_shake.webp)

Shake makes the text shake. Its tag format is
`[shake rate=20.0 level=5 connected=1]{text}[/shake]`.

`rate` controls how fast the text shakes, `level` controls how far the
text is offset from the origin. If `connected` is `1` (default), glyphs
with ligatures will be moved together. If `connected` is `0`, each glyph
is moved individually even if they are joined by ligatures. This can
work around certain rendering issues with font ligatures.

### Fade

![image](img/bbcode_in_richtextlabel_effect_fade.webp)

Fade creates a static fade effect that multiplies each character\'s
opacity. Its tag format is `[fade start=4 length=14]{text}[/fade]`.

`start` controls the starting position of the falloff relative to where
the fade command is inserted, `length` controls over how many characters
should the fade out take place.

### Rainbow

![image](img/bbcode_in_richtextlabel_effect_rainbow.webp)

Rainbow gives the text a rainbow color that changes over time. Its tag
format is
`[rainbow freq=1.0 sat=0.8 val=0.8 speed=1.0]{text}[/rainbow]`.

`freq` determines how many letters the rainbow extends over before it
repeats itself, `sat` is the saturation of the rainbow, `val` is the
value of the rainbow. `speed` is the number of full rainbow cycles per
second. A positive `speed` value will play the animation forwards, a
value of `0` will pause the animation, and a negative `speed` value will
play the animation backwards.

Font outlines are *not* affected by the rainbow effect (they keep their
original color). Existing font colors are overridden by the rainbow
effect. However, CanvasItem\'s **Modulate** and **Self Modulate**
properties will affect how the rainbow effect looks, as modulation
multiplies its final colors.

## Custom BBCode tags and text effects

You can extend the `class_RichTextEffect`{.interpreted-text role="ref"}
resource type to create your own custom BBCode tags. Create a new script
file that extends the `class_RichTextEffect`{.interpreted-text
role="ref"} resource type and give the script a `class_name` so that the
effect can be selected in the inspector. Add the `@tool` annotation to
your GDScript file if you wish to have these custom effects run within
the editor itself. The RichTextLabel does not need to have a script
attached, nor does it need to be running in `tool` mode. The new effect
can be registered in the Inspector by adding it to the **Markup \>
Custom Effects** array, or in code with the
`install_effect() <class_RichTextLabel_method_install_effect>`{.interpreted-text
role="ref"} method:

<figure class="align-center">
<img
src="img/bbcode_in_richtextlabel_selecting_custom_richtexteffect.webp"
alt="img/bbcode_in_richtextlabel_selecting_custom_richtexteffect.webp" />
<figcaption>Selecting a custom RichTextEffect after saving a script that
extends RichTextEffect with a <code>class_name</code></figcaption>
</figure>

:::: warning
::: title
Warning
:::

If the custom effect is not registered within the RichTextLabel\'s
**Markup \> Custom Effects** property, no effect will be visible and the
original tag will be left as-is.
::::

There is only one function that you need to extend:
`_process_custom_fx(char_fx)`. Optionally, you can also provide a custom
BBCode identifier by adding a member name `bbcode`. The code will check
the `bbcode` property automatically or will use the name of the file to
determine what the BBCode tag should be.

### `_process_custom_fx`

This is where the logic of each effect takes place and is called once
per glyph during the draw phase of text rendering. This passes in a
`class_CharFXTransform`{.interpreted-text role="ref"} object, which
holds a few variables to control how the associated glyph is rendered:

- `identity` specifies which custom effect is being processed. You
  should use that for code flow control.
- `outline` is `true` if effect is called for drawing text outline.
- `range` tells you how far into a given custom effect block you are in
  as an index.
- `elapsed_time` is the total amount of time the text effect has been
  running.
- `visible` will tell you whether the glyph is visible or not and will
  also allow you to hide a given portion of text.
- `offset` is an offset position relative to where the given glyph
  should render under normal circumstances.
- `color` is the color of a given glyph.
- `glyph_index` and `font` is glyph being drawn and font data resource
  used to draw it.
- Finally, `env` is a `class_Dictionary`{.interpreted-text role="ref"}
  of parameters assigned to a given custom effect. You can use
  `get() <class_Dictionary_method_get>`{.interpreted-text role="ref"}
  with an optional default value to retrieve each parameter, if
  specified by the user. For example
  `[custom_fx spread=0.5 color=#FFFF00]test[/custom_fx]` would have a
  float `spread` and Color `color` parameters in its `env` Dictionary.
  See below for more usage examples.

The last thing to note about this function is that it is necessary to
return a boolean `true` value to verify that the effect processed
correctly. This way, if there\'s a problem with rendering a given glyph,
it will back out of rendering custom effects entirely until the user
fixes whatever error cropped up in their custom effect logic.

Here are some examples of custom effects:

### Ghost

    @tool
    extends RichTextEffect
    class_name RichTextGhost

    # Syntax: [ghost freq=5.0 span=10.0][/ghost]

    # Define the tag name.
    var bbcode = "ghost"

    func _process_custom_fx(char_fx):
        # Get parameters, or use the provided default value if missing.
        var speed = char_fx.env.get("freq", 5.0)
        var span = char_fx.env.get("span", 10.0)

        var alpha = sin(char_fx.elapsed_time * speed + (char_fx.range.x / span)) * 0.5 + 0.5
        char_fx.color.a = alpha
        return true

### Matrix

    @tool
    extends RichTextEffect
    class_name RichTextMatrix

    # Syntax: [matrix clean=2.0 dirty=1.0 span=50][/matrix]

    # Define the tag name.
    var bbcode = "matrix"

    # Gets TextServer for retrieving font information.
    func get_text_server():
        return TextServerManager.get_primary_interface()

    func _process_custom_fx(char_fx):
        # Get parameters, or use the provided default value if missing.
        var clear_time = char_fx.env.get("clean", 2.0)
        var dirty_time = char_fx.env.get("dirty", 1.0)
        var text_span = char_fx.env.get("span", 50)

        var value = char_fx.glyph_index

        var matrix_time = fmod(char_fx.elapsed_time + (char_fx.range.x / float(text_span)), \
                               clear_time + dirty_time)

        matrix_time = 0.0 if matrix_time < clear_time else \
                      (matrix_time - clear_time) / dirty_time

        if matrix_time > 0.0:
            value = int(1 * matrix_time * (126 - 65))
            value %= (126 - 65)
            value += 65
        char_fx.glyph_index = get_text_server().font_get_glyph_index(char_fx.font, 1, value, 0)
        return true

This will add a few new BBCode commands, which can be used like so:

``` none
[center][ghost]This is a custom [matrix]effect[/matrix][/ghost] made in
[pulse freq=5.0 height=2.0][pulse color=#00FFAA freq=2.0]GDScript[/pulse][/pulse].[/center]
```
