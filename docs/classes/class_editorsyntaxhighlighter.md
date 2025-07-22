github_url
:   hide

# EditorSyntaxHighlighter {#class_EditorSyntaxHighlighter}

**Inherits:**
`SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`GDScriptSyntaxHighlighter<class_GDScriptSyntaxHighlighter>`{.interpreted-text
role="ref"}

Base class for
`SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
role="ref"} used by the
`ScriptEditor<class_ScriptEditor>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Base class that all
`SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
role="ref"}s used by the
`ScriptEditor<class_ScriptEditor>`{.interpreted-text role="ref"} extend
from.

Add a syntax highlighter to an individual script by calling
`ScriptEditorBase.add_syntax_highlighter()<class_ScriptEditorBase_method_add_syntax_highlighter>`{.interpreted-text
role="ref"}. To apply to all scripts on open, call
`ScriptEditor.register_syntax_highlighter()<class_ScriptEditor_method_register_syntax_highlighter>`{.interpreted-text
role="ref"}.

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

:::: {#class_EditorSyntaxHighlighter_private_method__create}
::: rst-class
classref-method
:::
::::

`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"} **\_create**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSyntaxHighlighter_private_method__create>`{.interpreted-text
role="ref"}

Virtual method which creates a new instance of the syntax highlighter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSyntaxHighlighter_private_method__get_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **\_get_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSyntaxHighlighter_private_method__get_name>`{.interpreted-text
role="ref"}

Virtual method which can be overridden to return the syntax highlighter
name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSyntaxHighlighter_private_method__get_supported_languages}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_supported_languages**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSyntaxHighlighter_private_method__get_supported_languages>`{.interpreted-text
role="ref"}

Virtual method which can be overridden to return the supported language
names.
