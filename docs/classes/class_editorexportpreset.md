github_url
:   hide

# EditorExportPreset {#class_EditorExportPreset}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Export preset configuration.

::: rst-class
classref-introduction-group
:::

## Description

Represents the configuration of an export preset, as created by the
editor\'s export dialog. An **EditorExportPreset** instance is intended
to be used a read-only configuration passed to the
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"} methods when exporting the project.

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

## Enumerations

:::: {#enum_EditorExportPreset_ExportFilter}
::: rst-class
classref-enumeration
:::
::::

enum **ExportFilter**:
`🔗<enum_EditorExportPreset_ExportFilter>`{.interpreted-text role="ref"}

:::: {#class_EditorExportPreset_constant_EXPORT_ALL_RESOURCES}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportFilter<enum_EditorExportPreset_ExportFilter>`{.interpreted-text
role="ref"} **EXPORT_ALL_RESOURCES** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_EXPORT_SELECTED_SCENES}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportFilter<enum_EditorExportPreset_ExportFilter>`{.interpreted-text
role="ref"} **EXPORT_SELECTED_SCENES** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_EXPORT_SELECTED_RESOURCES}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportFilter<enum_EditorExportPreset_ExportFilter>`{.interpreted-text
role="ref"} **EXPORT_SELECTED_RESOURCES** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_EXCLUDE_SELECTED_RESOURCES}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportFilter<enum_EditorExportPreset_ExportFilter>`{.interpreted-text
role="ref"} **EXCLUDE_SELECTED_RESOURCES** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_EXPORT_CUSTOMIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportFilter<enum_EditorExportPreset_ExportFilter>`{.interpreted-text
role="ref"} **EXPORT_CUSTOMIZED** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorExportPreset_FileExportMode}
::: rst-class
classref-enumeration
:::
::::

enum **FileExportMode**:
`🔗<enum_EditorExportPreset_FileExportMode>`{.interpreted-text
role="ref"}

:::: {#class_EditorExportPreset_constant_MODE_FILE_NOT_CUSTOMIZED}
::: rst-class
classref-enumeration-constant
:::
::::

`FileExportMode<enum_EditorExportPreset_FileExportMode>`{.interpreted-text
role="ref"} **MODE_FILE_NOT_CUSTOMIZED** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_MODE_FILE_STRIP}
::: rst-class
classref-enumeration-constant
:::
::::

`FileExportMode<enum_EditorExportPreset_FileExportMode>`{.interpreted-text
role="ref"} **MODE_FILE_STRIP** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_MODE_FILE_KEEP}
::: rst-class
classref-enumeration-constant
:::
::::

`FileExportMode<enum_EditorExportPreset_FileExportMode>`{.interpreted-text
role="ref"} **MODE_FILE_KEEP** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_MODE_FILE_REMOVE}
::: rst-class
classref-enumeration-constant
:::
::::

`FileExportMode<enum_EditorExportPreset_FileExportMode>`{.interpreted-text
role="ref"} **MODE_FILE_REMOVE** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorExportPreset_ScriptExportMode}
::: rst-class
classref-enumeration
:::
::::

enum **ScriptExportMode**:
`🔗<enum_EditorExportPreset_ScriptExportMode>`{.interpreted-text
role="ref"}

:::: {#class_EditorExportPreset_constant_MODE_SCRIPT_TEXT}
::: rst-class
classref-enumeration-constant
:::
::::

`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>`{.interpreted-text
role="ref"} **MODE_SCRIPT_TEXT** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_MODE_SCRIPT_BINARY_TOKENS}
::: rst-class
classref-enumeration-constant
:::
::::

`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>`{.interpreted-text
role="ref"} **MODE_SCRIPT_BINARY_TOKENS** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_EditorExportPreset_constant_MODE_SCRIPT_BINARY_TOKENS_COMPRESSED}
::: rst-class
classref-enumeration-constant
:::
::::

`ScriptExportMode<enum_EditorExportPreset_ScriptExportMode>`{.interpreted-text
role="ref"} **MODE_SCRIPT_BINARY_TOKENS_COMPRESSED** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorExportPreset_method_are_advanced_options_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**are_advanced_options_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_are_advanced_options_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the \"Advanced\" toggle is enabled in the export
dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_custom_features}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_custom_features**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_custom_features>`{.interpreted-text
role="ref"}

Returns a comma-separated list of custom features added to this preset,
as a string. See
`Feature tags <../tutorials/export/feature_tags>`{.interpreted-text
role="doc"} in the documentation for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_customized_files}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_customized_files**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_customized_files>`{.interpreted-text
role="ref"}

Returns a dictionary of files selected in the \"Resources\" tab of the
export dialog. The dictionary\'s keys are file paths, and its values are
the corresponding export modes: `"strip"`, `"keep"`, or `"remove"`. See
also
`get_file_export_mode()<class_EditorExportPreset_method_get_file_export_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_customized_files_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_customized_files_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_customized_files_count>`{.interpreted-text
role="ref"}

Returns the number of files selected in the \"Resources\" tab of the
export dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_encrypt_directory}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_encrypt_directory**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_encrypt_directory>`{.interpreted-text
role="ref"}

Returns `true` if PCK directory encryption is enabled in the export
dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_encrypt_pck}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **get_encrypt_pck**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_encrypt_pck>`{.interpreted-text
role="ref"}

Returns `true` if PCK encryption is enabled in the export dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_encryption_ex_filter}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_encryption_ex_filter**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_encryption_ex_filter>`{.interpreted-text
role="ref"}

Returns file filters to exclude during PCK encryption.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_encryption_in_filter}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_encryption_in_filter**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_encryption_in_filter>`{.interpreted-text
role="ref"}

Returns file filters to include during PCK encryption.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_encryption_key}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_encryption_key**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_encryption_key>`{.interpreted-text
role="ref"}

Returns PCK encryption key.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_exclude_filter}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_exclude_filter**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_exclude_filter>`{.interpreted-text
role="ref"}

Returns file filters to exclude during export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_export_filter}
::: rst-class
classref-method
:::
::::

`ExportFilter<enum_EditorExportPreset_ExportFilter>`{.interpreted-text
role="ref"} **get_export_filter**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_export_filter>`{.interpreted-text
role="ref"}

Returns export file filter mode selected in the \"Resources\" tab of the
export dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_export_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_export_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_export_path>`{.interpreted-text
role="ref"}

Returns export target path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_file_export_mode}
::: rst-class
classref-method
:::
::::

`FileExportMode<enum_EditorExportPreset_FileExportMode>`{.interpreted-text
role="ref"} **get_file_export_mode**(path:
`String<class_String>`{.interpreted-text role="ref"}, default:
`FileExportMode<enum_EditorExportPreset_FileExportMode>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_file_export_mode>`{.interpreted-text
role="ref"}

Returns file export mode for the specified file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_files_to_export}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_files_to_export**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_files_to_export>`{.interpreted-text
role="ref"}

Returns array of files to export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_include_filter}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_include_filter**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_include_filter>`{.interpreted-text
role="ref"}

Returns file filters to include during export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_or_env}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_or_env**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, env_var: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_or_env>`{.interpreted-text
role="ref"}

Returns export option value or value of environment variable if it is
set.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_patches}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_patches**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_patches>`{.interpreted-text
role="ref"}

Returns the list of packs on which to base a patch export on.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_preset_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_preset_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_preset_name>`{.interpreted-text
role="ref"}

Returns this export preset\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_project_setting}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_project_setting**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPreset_method_get_project_setting>`{.interpreted-text
role="ref"}

Returns the value of the setting identified by `name` using export
preset feature tag overrides instead of current OS features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_script_export_mode}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_script_export_mode**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_script_export_mode>`{.interpreted-text
role="ref"}

Returns the export mode used by GDScript files. `0` for \"Text\", `1`
for \"Binary tokens\", and `2` for \"Compressed binary tokens (smaller
files)\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_get_version}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_version**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, windows_version: `bool<class_bool>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_get_version>`{.interpreted-text
role="ref"}

Returns the preset\'s version number, or fall back to the
`ProjectSettings.application/config/version<class_ProjectSettings_property_application/config/version>`{.interpreted-text
role="ref"} project setting if set to an empty string.

If `windows_version` is `true`, formats the returned version number to
be compatible with Windows executable metadata.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_has}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_EditorExportPreset_method_has>`{.interpreted-text
role="ref"}

Returns `true` if the preset has the property named `property`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_has_export_file}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_export_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPreset_method_has_export_file>`{.interpreted-text
role="ref"}

Returns `true` if the file at the specified `path` will be exported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_is_dedicated_server}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_dedicated_server**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_is_dedicated_server>`{.interpreted-text
role="ref"}

Returns `true` if the dedicated server export mode is selected in the
export dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPreset_method_is_runnable}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_runnable**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPreset_method_is_runnable>`{.interpreted-text
role="ref"}

Returns `true` if the \"Runnable\" toggle is enabled in the export
dialog.
