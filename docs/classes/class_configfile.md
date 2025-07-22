github_url
:   hide

# ConfigFile {#class_ConfigFile}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Helper class to handle INI-style files.

::: rst-class
classref-introduction-group
:::

## Description

This helper class can be used to store
`Variant<class_Variant>`{.interpreted-text role="ref"} values on the
filesystem using INI-style formatting. The stored values are identified
by a section and a key:

``` text
[section]
some_key=42
string_example="Hello World3D!"
a_vector=Vector3(1, 0, 2)
```

The stored data can be saved to or parsed from a file, though ConfigFile
objects can also be used directly without accessing the filesystem.

The following example shows how to create a simple **ConfigFile** and
save it on disc:

::::: tabs
::: code-tab
gdscript

\# Create new ConfigFile object. var config = ConfigFile.new()

\# Store some values. config.set_value(\"Player1\", \"player_name\",
\"Steve\") config.set_value(\"Player1\", \"best_score\", 10)
config.set_value(\"Player2\", \"player_name\", \"V3geta\")
config.set_value(\"Player2\", \"best_score\", 9001)

\# Save it to a file (overwrite if already exists).
config.save(\"user://scores.cfg\")
:::

::: code-tab
csharp

// Create new ConfigFile object. var config = new ConfigFile();

// Store some values. config.SetValue(\"Player1\", \"player_name\",
\"Steve\"); config.SetValue(\"Player1\", \"best_score\", 10);
config.SetValue(\"Player2\", \"player_name\", \"V3geta\");
config.SetValue(\"Player2\", \"best_score\", 9001);

// Save it to a file (overwrite if already exists).
config.Save(\"user://scores.cfg\");
:::
:::::

This example shows how the above file could be loaded:

::::: tabs
::: code-tab
gdscript

var score_data = {} var config = ConfigFile.new()

\# Load data from a file. var err = config.load(\"user://scores.cfg\")

\# If the file didn\'t load, ignore it. if err != OK: return

\# Iterate over all sections. for player in config.get_sections(): \#
Fetch the data for each section. var player_name =
config.get_value(player, \"player_name\") var player_score =
config.get_value(player, \"best_score\") score_data\[player_name\] =
player_score
:::

::: code-tab
csharp

var score_data = new Godot.Collections.Dictionary(); var config = new
ConfigFile();

// Load data from a file. Error err =
config.Load(\"user://scores.cfg\");

// If the file didn\'t load, ignore it. if (err != Error.Ok) { return; }

// Iterate over all sections. foreach (String player in
config.GetSections()) { // Fetch the data for each section. var
player_name = (String)config.GetValue(player, \"player_name\"); var
player_score = (int)config.GetValue(player, \"best_score\");
score_data\[player_name\] = player_score; }
:::
:::::

Any operation that mutates the ConfigFile such as
`set_value()<class_ConfigFile_method_set_value>`{.interpreted-text
role="ref"}, `clear()<class_ConfigFile_method_clear>`{.interpreted-text
role="ref"}, or
`erase_section()<class_ConfigFile_method_erase_section>`{.interpreted-text
role="ref"}, only changes what is loaded in memory. If you want to write
the change to a file, you have to save the changes with
`save()<class_ConfigFile_method_save>`{.interpreted-text role="ref"},
`save_encrypted()<class_ConfigFile_method_save_encrypted>`{.interpreted-text
role="ref"}, or
`save_encrypted_pass()<class_ConfigFile_method_save_encrypted_pass>`{.interpreted-text
role="ref"}.

Keep in mind that section and property names can\'t contain spaces.
Anything after a space will be ignored on save and on load.

ConfigFiles can also contain manually written comment lines starting
with a semicolon (`;`). Those lines will be ignored when parsing the
file. Note that comments will be lost when saving the ConfigFile. This
can still be useful for dedicated server configuration files, which are
typically never overwritten without explicit user action.

\*\*Note:\*\* The file extension given to a ConfigFile does not have any
impact on its formatting or behavior. By convention, the `.cfg`
extension is used here, but any other extension such as `.ini` is also
valid. Since neither `.cfg` nor `.ini` are standardized, Godot\'s
ConfigFile formatting may differ from files written by other programs.

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

:::: {#class_ConfigFile_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**()
`🔗<class_ConfigFile_method_clear>`{.interpreted-text role="ref"}

Removes the entire contents of the config.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_encode_to_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**encode_to_text**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConfigFile_method_encode_to_text>`{.interpreted-text
role="ref"}

Obtain the text version of this config file (the same text that would be
written to a file).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_erase_section}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_section**(section: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ConfigFile_method_erase_section>`{.interpreted-text
role="ref"}

Deletes the specified section along with all the key-value pairs inside.
Raises an error if the section does not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_erase_section_key}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_section_key**(section: `String<class_String>`{.interpreted-text
role="ref"}, key: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ConfigFile_method_erase_section_key>`{.interpreted-text
role="ref"}

Deletes the specified key in a section. Raises an error if either the
section or the key do not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_get_section_keys}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_section_keys**(section:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConfigFile_method_get_section_keys>`{.interpreted-text
role="ref"}

Returns an array of all defined key identifiers in the specified
section. Raises an error and returns an empty array if the section does
not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_get_sections}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_sections**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConfigFile_method_get_sections>`{.interpreted-text role="ref"}

Returns an array of all defined section identifiers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_get_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_value**(section: `String<class_String>`{.interpreted-text
role="ref"}, key: `String<class_String>`{.interpreted-text role="ref"},
default: `Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ConfigFile_method_get_value>`{.interpreted-text
role="ref"}

Returns the current value for the specified section and key. If either
the section or the key do not exist, the method returns the fallback
`default` value. If `default` is not specified or set to `null`, an
error is also raised.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_has_section}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_section**(section: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_ConfigFile_method_has_section>`{.interpreted-text
role="ref"}

Returns `true` if the specified section exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_has_section_key}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_section_key**(section: `String<class_String>`{.interpreted-text
role="ref"}, key: `String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ConfigFile_method_has_section_key>`{.interpreted-text
role="ref"}

Returns `true` if the specified section-key pair exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_load}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ConfigFile_method_load>`{.interpreted-text role="ref"}

Loads the config file specified as a parameter. The file\'s contents are
parsed and loaded in the **ConfigFile** object which the method was
called on.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} values if
the operation failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_load_encrypted}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_encrypted**(path: `String<class_String>`{.interpreted-text
role="ref"}, key:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_ConfigFile_method_load_encrypted>`{.interpreted-text
role="ref"}

Loads the encrypted config file specified as a parameter, using the
provided `key` to decrypt it. The file\'s contents are parsed and loaded
in the **ConfigFile** object which the method was called on.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} values if
the operation failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_load_encrypted_pass}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**load_encrypted_pass**(path: `String<class_String>`{.interpreted-text
role="ref"}, password: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ConfigFile_method_load_encrypted_pass>`{.interpreted-text
role="ref"}

Loads the encrypted config file specified as a parameter, using the
provided `password` to decrypt it. The file\'s contents are parsed and
loaded in the **ConfigFile** object which the method was called on.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} values if
the operation failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_parse}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**parse**(data: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ConfigFile_method_parse>`{.interpreted-text role="ref"}

Parses the passed string as the contents of a config file. The string is
parsed and loaded in the ConfigFile object which the method was called
on.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} values if
the operation failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_save}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save**(path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_ConfigFile_method_save>`{.interpreted-text role="ref"}

Saves the contents of the **ConfigFile** object to the file specified as
a parameter. The output file uses an INI-style structure.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} values if
the operation failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_save_encrypted}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_encrypted**(path: `String<class_String>`{.interpreted-text
role="ref"}, key:
`PackedByteArray<class_PackedByteArray>`{.interpreted-text role="ref"})
`🔗<class_ConfigFile_method_save_encrypted>`{.interpreted-text
role="ref"}

Saves the contents of the **ConfigFile** object to the AES-256 encrypted
file specified as a parameter, using the provided `key` to encrypt it.
The output file uses an INI-style structure.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} values if
the operation failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_save_encrypted_pass}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_encrypted_pass**(path: `String<class_String>`{.interpreted-text
role="ref"}, password: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_ConfigFile_method_save_encrypted_pass>`{.interpreted-text
role="ref"}

Saves the contents of the **ConfigFile** object to the AES-256 encrypted
file specified as a parameter, using the provided `password` to encrypt
it. The output file uses an INI-style structure.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or one of the other
`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"} values if
the operation failed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ConfigFile_method_set_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_value**(section: `String<class_String>`{.interpreted-text
role="ref"}, key: `String<class_String>`{.interpreted-text role="ref"},
value: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_ConfigFile_method_set_value>`{.interpreted-text role="ref"}

Assigns a value to the specified key of the specified section. If either
the section or the key do not exist, they are created. Passing a `null`
value deletes the specified key if it exists, and deletes the section if
it ends up empty once the key has been removed.
