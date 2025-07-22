github_url
:   hide

# SyntaxHighlighter {#class_SyntaxHighlighter}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CodeHighlighter<class_CodeHighlighter>`{.interpreted-text role="ref"},
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"}

Base class for syntax highlighters. Provides syntax highlighting data to
a `TextEdit<class_TextEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Base class for syntax highlighters. Provides syntax highlighting data to
a `TextEdit<class_TextEdit>`{.interpreted-text role="ref"}. The
associated `TextEdit<class_TextEdit>`{.interpreted-text role="ref"} will
call into the **SyntaxHighlighter** on an as-needed basis.

\*\*Note:\*\* A **SyntaxHighlighter** instance should not be used across
multiple `TextEdit<class_TextEdit>`{.interpreted-text role="ref"} nodes.

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

## Method Descriptions

:::: {#class_SyntaxHighlighter_private_method__clear_highlighting_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_clear_highlighting_cache**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SyntaxHighlighter_private_method__clear_highlighting_cache>`{.interpreted-text
role="ref"}

Virtual method which can be overridden to clear any local caches.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SyntaxHighlighter_private_method__get_line_syntax_highlighting}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_line_syntax_highlighting**(line:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SyntaxHighlighter_private_method__get_line_syntax_highlighting>`{.interpreted-text
role="ref"}

Virtual method which can be overridden to return syntax highlighting
data.

See
`get_line_syntax_highlighting()<class_SyntaxHighlighter_method_get_line_syntax_highlighting>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SyntaxHighlighter_private_method__update_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_update_cache**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_SyntaxHighlighter_private_method__update_cache>`{.interpreted-text
role="ref"}

Virtual method which can be overridden to update any local caches.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SyntaxHighlighter_method_clear_highlighting_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_highlighting_cache**()
`🔗<class_SyntaxHighlighter_method_clear_highlighting_cache>`{.interpreted-text
role="ref"}

Clears all cached syntax highlighting data.

Then calls overridable method
`_clear_highlighting_cache()<class_SyntaxHighlighter_private_method__clear_highlighting_cache>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SyntaxHighlighter_method_get_line_syntax_highlighting}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_line_syntax_highlighting**(line:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SyntaxHighlighter_method_get_line_syntax_highlighting>`{.interpreted-text
role="ref"}

Returns the syntax highlighting data for the line at index `line`. If
the line is not cached, calls
`_get_line_syntax_highlighting()<class_SyntaxHighlighter_private_method__get_line_syntax_highlighting>`{.interpreted-text
role="ref"} first to calculate the data.

Each entry is a column number containing a nested
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}. The column
number denotes the start of a region, the region will end if another
region is found, or at the end of the line. The nested
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} contains
the data for that region. Currently only the key `"color"` is supported.

\*\*Example:\*\* Possible return value. This means columns `0` to `4`
should be red, and columns `5` to the end of the line should be green:

    {
        0: {
            "color": Color(1, 0, 0)
        },
        5: {
            "color": Color(0, 1, 0)
        }
    }

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SyntaxHighlighter_method_get_text_edit}
::: rst-class
classref-method
:::
::::

`TextEdit<class_TextEdit>`{.interpreted-text role="ref"}
**get_text_edit**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SyntaxHighlighter_method_get_text_edit>`{.interpreted-text
role="ref"}

Returns the associated `TextEdit<class_TextEdit>`{.interpreted-text
role="ref"} node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SyntaxHighlighter_method_update_cache}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_cache**()
`🔗<class_SyntaxHighlighter_method_update_cache>`{.interpreted-text
role="ref"}

Clears then updates the **SyntaxHighlighter** caches. Override
`_update_cache()<class_SyntaxHighlighter_private_method__update_cache>`{.interpreted-text
role="ref"} for a callback.

\*\*Note:\*\* This is called automatically when the associated
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"} node, updates
its own cache.
