github_url
:   hide

# CodeHighlighter {#class_CodeHighlighter}

**Inherits:**
`SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A syntax highlighter intended for code.

::: rst-class
classref-introduction-group
:::

## Description

By adjusting various properties of this resource, you can change the
colors of strings, comments, numbers, and other text patterns inside a
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"} control.

::: rst-class
classref-reftable-group
:::

## Properties

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

## Property Descriptions

:::: {#class_CodeHighlighter_property_color_regions}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**color_regions** = `{}`
`🔗<class_CodeHighlighter_property_color_regions>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_regions**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_color_regions**()

Sets the color regions. All existing regions will be removed. The
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} key is the
region start and end key, separated by a space. The value is the region
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_property_function_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **function_color** =
`Color(0, 0, 0, 1)`
`🔗<class_CodeHighlighter_property_function_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_function_color**()

Sets color for functions. A function is a non-keyword string followed by
a \'(\'.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_property_keyword_colors}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**keyword_colors** = `{}`
`🔗<class_CodeHighlighter_property_keyword_colors>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keyword_colors**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_keyword_colors**()

Sets the keyword colors. All existing keywords will be removed. The
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} key is the
keyword. The value is the keyword color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_property_member_keyword_colors}
::: rst-class
classref-property
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**member_keyword_colors** = `{}`
`🔗<class_CodeHighlighter_property_member_keyword_colors>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_member_keyword_colors**(value:
  `Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
- `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
  **get_member_keyword_colors**()

Sets the member keyword colors. All existing member keyword will be
removed. The `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"} key is the member keyword. The value is the member keyword
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_property_member_variable_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**member_variable_color** = `Color(0, 0, 0, 1)`
`🔗<class_CodeHighlighter_property_member_variable_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_member_variable_color**(value:
  `Color<class_Color>`{.interpreted-text role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_member_variable_color**()

Sets color for member variables. A member variable is non-keyword,
non-function string proceeded with a \'.\'.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_property_number_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **number_color** =
`Color(0, 0, 0, 1)`
`🔗<class_CodeHighlighter_property_number_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_number_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_number_color**()

Sets the color for numbers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_property_symbol_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **symbol_color** =
`Color(0, 0, 0, 1)`
`🔗<class_CodeHighlighter_property_symbol_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_symbol_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_symbol_color**()

Sets the color for symbols.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CodeHighlighter_method_add_color_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_color_region**(start_key: `String<class_String>`{.interpreted-text
role="ref"}, end_key: `String<class_String>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"},
line_only: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_CodeHighlighter_method_add_color_region>`{.interpreted-text
role="ref"}

Adds a color region (such as for comments or strings) from `start_key`
to `end_key`. Both keys should be symbols, and `start_key` must not be
shared with other delimiters.

If `line_only` is `true` or `end_key` is an empty
`String<class_String>`{.interpreted-text role="ref"}, the region does
not carry over to the next line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_add_keyword_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_keyword_color**(keyword: `String<class_String>`{.interpreted-text
role="ref"}, color: `Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_CodeHighlighter_method_add_keyword_color>`{.interpreted-text
role="ref"}

Sets the color for a keyword.

The keyword cannot contain any symbols except \'\_\'.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_add_member_keyword_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_member_keyword_color**(member_keyword:
`String<class_String>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"})
`🔗<class_CodeHighlighter_method_add_member_keyword_color>`{.interpreted-text
role="ref"}

Sets the color for a member keyword.

The member keyword cannot contain any symbols except \'\_\'.

It will not be highlighted if preceded by a \'.\'.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_clear_color_regions}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_color_regions**()
`🔗<class_CodeHighlighter_method_clear_color_regions>`{.interpreted-text
role="ref"}

Removes all color regions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_clear_keyword_colors}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_keyword_colors**()
`🔗<class_CodeHighlighter_method_clear_keyword_colors>`{.interpreted-text
role="ref"}

Removes all keywords.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_clear_member_keyword_colors}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_member_keyword_colors**()
`🔗<class_CodeHighlighter_method_clear_member_keyword_colors>`{.interpreted-text
role="ref"}

Removes all member keywords.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_get_keyword_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_keyword_color**(keyword: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeHighlighter_method_get_keyword_color>`{.interpreted-text
role="ref"}

Returns the color for a keyword.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_get_member_keyword_color}
::: rst-class
classref-method
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**get_member_keyword_color**(member_keyword:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeHighlighter_method_get_member_keyword_color>`{.interpreted-text
role="ref"}

Returns the color for a member keyword.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_has_color_region}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_color_region**(start_key: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeHighlighter_method_has_color_region>`{.interpreted-text
role="ref"}

Returns `true` if the start key exists, else `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_has_keyword_color}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_keyword_color**(keyword: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeHighlighter_method_has_keyword_color>`{.interpreted-text
role="ref"}

Returns `true` if the keyword exists, else `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_has_member_keyword_color}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_member_keyword_color**(member_keyword:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CodeHighlighter_method_has_member_keyword_color>`{.interpreted-text
role="ref"}

Returns `true` if the member keyword exists, else `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_remove_color_region}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_color_region**(start_key:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CodeHighlighter_method_remove_color_region>`{.interpreted-text
role="ref"}

Removes the color region that uses that start key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_remove_keyword_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_keyword_color**(keyword:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CodeHighlighter_method_remove_keyword_color>`{.interpreted-text
role="ref"}

Removes the keyword.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CodeHighlighter_method_remove_member_keyword_color}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_member_keyword_color**(member_keyword:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_CodeHighlighter_method_remove_member_keyword_color>`{.interpreted-text
role="ref"}

Removes the member keyword.
