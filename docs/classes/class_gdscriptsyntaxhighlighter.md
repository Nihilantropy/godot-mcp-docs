github_url
:   hide

# GDScriptSyntaxHighlighter {#class_GDScriptSyntaxHighlighter}

**Inherits:**
`EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>`{.interpreted-text
role="ref"} **\<**
`SyntaxHighlighter<class_SyntaxHighlighter>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A GDScript syntax highlighter that can be used with
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"} and
`CodeEdit<class_CodeEdit>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-introduction-group
:::

## Description

**Note:** This class can only be used for editor plugins because it
relies on editor settings.

::::: tabs
::: code-tab
gdscript

var code_preview = TextEdit.new() var highlighter =
GDScriptSyntaxHighlighter.new() code_preview.syntax_highlighter =
highlighter
:::

::: code-tab
csharp

var codePreview = new TextEdit(); var highlighter = new
GDScriptSyntaxHighlighter(); codePreview.SyntaxHighlighter =
highlighter;
:::
:::::
