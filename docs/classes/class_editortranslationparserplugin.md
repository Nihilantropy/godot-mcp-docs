github_url
:   hide

# EditorTranslationParserPlugin {#class_EditorTranslationParserPlugin}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Plugin for adding custom parsers to extract strings that are to be
translated from custom files (.csv, .json etc.).

::: rst-class
classref-introduction-group
:::

## Description

**EditorTranslationParserPlugin** is invoked when a file is being parsed
to extract strings that require translation. To define the parsing and
string extraction logic, override the
`_parse_file()<class_EditorTranslationParserPlugin_private_method__parse_file>`{.interpreted-text
role="ref"} method in script.

The return value should be an `Array<class_Array>`{.interpreted-text
role="ref"} of
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}s, one for each extracted translatable string. Each entry
should contain `[msgid, msgctxt, msgid_plural, comment]`, where all
except `msgid` are optional. Empty strings will be ignored.

The extracted strings will be written into a POT file selected by user
under \"POT Generation\" in \"Localization\" tab in \"Project Settings\"
menu.

Below shows an example of a custom parser that extracts strings from a
CSV file to write into a POT.

::::: tabs
::: code-tab
gdscript

\@tool extends EditorTranslationParserPlugin

func [parse_file]{#parse_file}(path):

:   var ret: Array\[PackedStringArray\] = \[\] var file =
    FileAccess.open(path, FileAccess.READ) var text = file.get_as_text()
    var split_strs = text.split(\",\", false) for s in split_strs:
    ret.append(PackedStringArray(\[s\])) #print(\"Extracted string: \" +
    s)

    return ret

func [get_recognized_extensions]{#get_recognized_extensions}():

:   return \[\"csv\"\]
:::

::: code-tab
csharp

using Godot;

\[Tool\] public partial class CustomParser :
EditorTranslationParserPlugin { public override
Godot.Collections.Array\<string\[\]\> [ParseFile]{#parsefile}(string
path) { Godot.Collections.Array\<string\[\]\> ret; using var file =
FileAccess.Open(path, FileAccess.ModeFlags.Read); string text =
file.GetAsText(); string\[\] splitStrs = text.Split(\",\", allowEmpty:
false); foreach (string s in splitStrs) { ret.Add(\[s\]);
//GD.Print(\$\"Extracted string: {s}\"); } return ret; }

> public override string\[\]
> [GetRecognizedExtensions]{#getrecognizedextensions}() { return
> \[\"csv\"\]; }

}
:::
:::::

To add a translatable string associated with a context, plural, or
comment:

::::: tabs
::: code-tab
gdscript

\# This will add a message with msgid \"Test 1\", msgctxt \"context\",
msgid_plural \"test 1 plurals\", and comment \"test 1 comment\".
ret.append(PackedStringArray(\[\"Test 1\", \"context\", \"test 1
plurals\", \"test 1 comment\"\])) \# This will add a message with msgid
\"A test without context\" and msgid_plural \"plurals\".
ret.append(PackedStringArray(\[\"A test without context\", \"\",
\"plurals\"\])) \# This will add a message with msgid \"Only with
context\" and msgctxt \"a friendly context\".
ret.append(PackedStringArray(\[\"Only with context\", \"a friendly
context\"\]))
:::

::: code-tab
csharp

// This will add a message with msgid \"Test 1\", msgctxt \"context\",
msgid_plural \"test 1 plurals\", and comment \"test 1 comment\".
ret.Add(\[\"Test 1\", \"context\", \"test 1 plurals\", \"test 1
comment\"\]); // This will add a message with msgid \"A test without
context\" and msgid_plural \"plurals\". ret.Add(\[\"A test without
context\", \"\", \"plurals\"\]); // This will add a message with msgid
\"Only with context\" and msgctxt \"a friendly context\".
ret.Add(\[\"Only with context\", \"a friendly context\"\]);
:::
:::::

\*\*Note:\*\* If you override parsing logic for standard script types
(GDScript, C#, etc.), it would be better to load the `path` argument
using
`ResourceLoader.load()<class_ResourceLoader_method_load>`{.interpreted-text
role="ref"}. This is because built-in scripts are loaded as
`Resource<class_Resource>`{.interpreted-text role="ref"} type, not
`FileAccess<class_FileAccess>`{.interpreted-text role="ref"} type. For
example:

::::: tabs
::: code-tab
gdscript

func [parse_file]{#parse_file}(path):

:   var res = ResourceLoader.load(path, \"Script\") var text =
    res.source_code \# Parsing logic.

func [get_recognized_extensions]{#get_recognized_extensions}():

:   return \[\"gd\"\]
:::

::: code-tab
csharp

public override Godot.Collections.Array\<string\[\]\>
[ParseFile]{#parsefile}(string path) { var res =
ResourceLoader.Load\<Script\>(path, \"Script\"); string text =
res.SourceCode; // Parsing logic. }

public override string\[\]
[GetRecognizedExtensions]{#getrecognizedextensions}() { return
\[\"gd\"\]; }
:::
:::::

To use **EditorTranslationParserPlugin**, register it using the
`EditorPlugin.add_translation_parser_plugin()<class_EditorPlugin_method_add_translation_parser_plugin>`{.interpreted-text
role="ref"} method first.

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

:::: {#class_EditorTranslationParserPlugin_private_method__get_recognized_extensions}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_recognized_extensions**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorTranslationParserPlugin_private_method__get_recognized_extensions>`{.interpreted-text
role="ref"}

Gets the list of file extensions to associate with this parser, e.g.
`["csv"]`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorTranslationParserPlugin_private_method__parse_file}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}\] **\_parse_file**(path:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorTranslationParserPlugin_private_method__parse_file>`{.interpreted-text
role="ref"}

Override this method to define a custom parsing logic to extract the
translatable strings.
