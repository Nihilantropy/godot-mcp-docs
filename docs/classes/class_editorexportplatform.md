github_url
:   hide

# EditorExportPlatform {#class_EditorExportPlatform}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`EditorExportPlatformAndroid<class_EditorExportPlatformAndroid>`{.interpreted-text
role="ref"},
`EditorExportPlatformAppleEmbedded<class_EditorExportPlatformAppleEmbedded>`{.interpreted-text
role="ref"},
`EditorExportPlatformExtension<class_EditorExportPlatformExtension>`{.interpreted-text
role="ref"},
`EditorExportPlatformMacOS<class_EditorExportPlatformMacOS>`{.interpreted-text
role="ref"},
`EditorExportPlatformPC<class_EditorExportPlatformPC>`{.interpreted-text
role="ref"},
`EditorExportPlatformWeb<class_EditorExportPlatformWeb>`{.interpreted-text
role="ref"}

Identifies a supported export platform, and internally provides the
functionality of exporting to that platform.

::: rst-class
classref-introduction-group
:::

## Description

Base resource that provides the functionality of exporting a release
build of a project to a platform, from the editor. Stores
platform-specific metadata such as the name and supported features of
the platform, and performs the exporting of projects, PCK files, and ZIP
files. Uses an export template for the platform provided at the time of
project exporting.

Used in scripting by
`EditorExportPlugin<class_EditorExportPlugin>`{.interpreted-text
role="ref"} to configure platform-specific customization of scenes and
resources. See
`EditorExportPlugin._begin_customize_scenes()<class_EditorExportPlugin_private_method__begin_customize_scenes>`{.interpreted-text
role="ref"} and
`EditorExportPlugin._begin_customize_resources()<class_EditorExportPlugin_private_method__begin_customize_resources>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Console support in Godot <../tutorials/platform/consoles>`{.interpreted-text
  role="doc"}

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

:::: {#enum_EditorExportPlatform_ExportMessageType}
::: rst-class
classref-enumeration
:::
::::

enum **ExportMessageType**:
`🔗<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"}

:::: {#class_EditorExportPlatform_constant_EXPORT_MESSAGE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"} **EXPORT_MESSAGE_NONE** = `0`

Invalid message type used as the default value when no type is
specified.

:::: {#class_EditorExportPlatform_constant_EXPORT_MESSAGE_INFO}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"} **EXPORT_MESSAGE_INFO** = `1`

Message type for informational messages that have no effect on the
export.

:::: {#class_EditorExportPlatform_constant_EXPORT_MESSAGE_WARNING}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"} **EXPORT_MESSAGE_WARNING** = `2`

Message type for warning messages that should be addressed but still
allow to complete the export.

:::: {#class_EditorExportPlatform_constant_EXPORT_MESSAGE_ERROR}
::: rst-class
classref-enumeration-constant
:::
::::

`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"} **EXPORT_MESSAGE_ERROR** = `3`

Message type for error messages that must be addressed and fail the
export.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorExportPlatform_DebugFlags}
::: rst-class
classref-enumeration
:::
::::

flags **DebugFlags**:
`🔗<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text role="ref"}

:::: {#class_EditorExportPlatform_constant_DEBUG_FLAG_DUMB_CLIENT}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"} **DEBUG_FLAG_DUMB_CLIENT** = `1`

Flag is set if the remotely debugged project is expected to use the
remote file system. If set,
`gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>`{.interpreted-text
role="ref"} will append `--remote-fs` and `--remote-fs-password` (if
`EditorSettings.filesystem/file_server/password<class_EditorSettings_property_filesystem/file_server/password>`{.interpreted-text
role="ref"} is defined) command line arguments to the returned list.

:::: {#class_EditorExportPlatform_constant_DEBUG_FLAG_REMOTE_DEBUG}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"} **DEBUG_FLAG_REMOTE_DEBUG** = `2`

Flag is set if remote debug is enabled. If set,
`gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>`{.interpreted-text
role="ref"} will append `--remote-debug` and `--breakpoints` (if
breakpoints are selected in the script editor or added by the plugin)
command line arguments to the returned list.

:::: {#class_EditorExportPlatform_constant_DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"} **DEBUG_FLAG_REMOTE_DEBUG_LOCALHOST** = `4`

Flag is set if remotely debugged project is running on the localhost. If
set,
`gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>`{.interpreted-text
role="ref"} will use `localhost` instead of
`EditorSettings.network/debug/remote_host<class_EditorSettings_property_network/debug/remote_host>`{.interpreted-text
role="ref"} as remote debugger host.

:::: {#class_EditorExportPlatform_constant_DEBUG_FLAG_VIEW_COLLISIONS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"} **DEBUG_FLAG_VIEW_COLLISIONS** = `8`

Flag is set if the \"Visible Collision Shapes\" remote debug option is
enabled. If set,
`gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>`{.interpreted-text
role="ref"} will append the `--debug-collisions` command line argument
to the returned list.

:::: {#class_EditorExportPlatform_constant_DEBUG_FLAG_VIEW_NAVIGATION}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"} **DEBUG_FLAG_VIEW_NAVIGATION** = `16`

Flag is set if the \"Visible Navigation\" remote debug option is
enabled. If set,
`gen_export_flags()<class_EditorExportPlatform_method_gen_export_flags>`{.interpreted-text
role="ref"} will append the `--debug-navigation` command line argument
to the returned list.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorExportPlatform_method_add_message}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_message**(type:
`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"}, category: `String<class_String>`{.interpreted-text
role="ref"}, message: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorExportPlatform_method_add_message>`{.interpreted-text
role="ref"}

Adds a message to the export log that will be displayed when exporting
ends.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_clear_messages}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_messages**()
`🔗<class_EditorExportPlatform_method_clear_messages>`{.interpreted-text
role="ref"}

Clears the export log.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_create_preset}
::: rst-class
classref-method
:::
::::

`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"} **create_preset**()
`🔗<class_EditorExportPlatform_method_create_preset>`{.interpreted-text
role="ref"}

Create a new preset for this platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_export_pack}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**export_pack**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_EditorExportPlatform_method_export_pack>`{.interpreted-text
role="ref"}

Creates a PCK archive at `path` for the specified `preset`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_export_pack_patch}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**export_pack_patch**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, patches:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} = PackedStringArray(), flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_EditorExportPlatform_method_export_pack_patch>`{.interpreted-text
role="ref"}

Creates a patch PCK archive at `path` for the specified `preset`,
containing only the files that have changed since the last patch.

\*\*Note:\*\* `patches` is an optional override of the set of patches
defined in the export preset. When empty the patches defined in the
export preset will be used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_export_project}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**export_project**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_EditorExportPlatform_method_export_project>`{.interpreted-text
role="ref"}

Creates a full project at `path` for the specified `preset`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_export_project_files}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**export_project_files**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
save_cb: `Callable<class_Callable>`{.interpreted-text role="ref"},
shared_cb: `Callable<class_Callable>`{.interpreted-text role="ref"} =
Callable())
`🔗<class_EditorExportPlatform_method_export_project_files>`{.interpreted-text
role="ref"}

Exports project files for the specified preset. This method can be used
to implement custom export format, other than PCK and ZIP. One of the
callbacks is called for each exported file.

`save_cb` is called for all exported files and have the following
arguments: `file_path: String`, `file_data: PackedByteArray`,
`file_index: int`, `file_count: int`,
`encryption_include_filters: PackedStringArray`,
`encryption_exclude_filters: PackedStringArray`,
`encryption_key: PackedByteArray`.

`shared_cb` is called for exported native shared/static libraries and
have the following arguments: `file_path: String`,
`tags: PackedStringArray`, `target_folder: String`.

\*\*Note:\*\* `file_index` and `file_count` are intended for progress
tracking only and aren\'t necessarily unique and precise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_export_zip}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**export_zip**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_EditorExportPlatform_method_export_zip>`{.interpreted-text
role="ref"}

Create a ZIP archive at `path` for the specified `preset`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_export_zip_patch}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**export_zip_patch**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, patches:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} = PackedStringArray(), flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\] = 0)
`🔗<class_EditorExportPlatform_method_export_zip_patch>`{.interpreted-text
role="ref"}

Create a patch ZIP archive at `path` for the specified `preset`,
containing only the files that have changed since the last patch.

\*\*Note:\*\* `patches` is an optional override of the set of patches
defined in the export preset. When empty the patches defined in the
export preset will be used instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_find_export_template}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**find_export_template**(template_file_name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_find_export_template>`{.interpreted-text
role="ref"}

Locates export template for the platform, and returns
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following keys: `path: String` and `error: String`. This method is
provided for convenience and custom export platforms aren\'t required to
use it or keep export templates stored in the same way official
templates are.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_gen_export_flags}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **gen_export_flags**(flags:
`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`DebugFlags<enum_EditorExportPlatform_DebugFlags>`{.interpreted-text
role="ref"}\])
`🔗<class_EditorExportPlatform_method_gen_export_flags>`{.interpreted-text
role="ref"}

Generates array of command line arguments for the default export
templates for the debug flags and editor settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_current_presets}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_current_presets**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_current_presets>`{.interpreted-text
role="ref"}

Returns array of
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}s for this platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_forced_export_files}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_forced_export_files**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_forced_export_files>`{.interpreted-text
role="ref"}

Returns array of core file names that always should be exported
regardless of preset config.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_internal_export_files}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_internal_export_files**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlatform_method_get_internal_export_files>`{.interpreted-text
role="ref"}

Returns additional files that should always be exported regardless of
preset configuration, and are not part of the project source. The
returned `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
contains filename keys (`String<class_String>`{.interpreted-text
role="ref"}) and their corresponding raw data
(`PackedByteArray<class_PackedByteArray>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_message_category}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_message_category**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_message_category>`{.interpreted-text
role="ref"}

Returns message category, for the message with `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_message_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_message_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_message_count>`{.interpreted-text
role="ref"}

Returns number of messages in the export log.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_message_text}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_message_text**(index: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_message_text>`{.interpreted-text
role="ref"}

Returns message text, for the message with `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_message_type}
::: rst-class
classref-method
:::
::::

`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"} **get_message_type**(index:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_message_type>`{.interpreted-text
role="ref"}

Returns message type, for the message with `index`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_os_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_os_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_os_name>`{.interpreted-text
role="ref"}

Returns the name of the export operating system handled by this
**EditorExportPlatform** class, as a friendly string. Possible return
values are `Windows`, `Linux`, `macOS`, `Android`, `iOS`, and `Web`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_get_worst_message_type}
::: rst-class
classref-method
:::
::::

`ExportMessageType<enum_EditorExportPlatform_ExportMessageType>`{.interpreted-text
role="ref"} **get_worst_message_type**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_get_worst_message_type>`{.interpreted-text
role="ref"}

Returns most severe message type currently present in the export log.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_save_pack}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**save_pack**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"}, embed:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_EditorExportPlatform_method_save_pack>`{.interpreted-text
role="ref"}

Saves PCK archive and returns
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following keys: `result: Error`, `so_files: Array` (array of the
shared/static objects which contains dictionaries with the following
keys: `path: String`, `tags: PackedStringArray`, and
`target_folder: String`).

If `embed` is `true`, PCK content is appended to the end of `path` file
and return `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
additionally include following keys: `embedded_start: int` (embedded PCK
offset) and `embedded_size: int` (embedded PCK size).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_save_pack_patch}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**save_pack_patch**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlatform_method_save_pack_patch>`{.interpreted-text
role="ref"}

Saves patch PCK archive and returns
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following keys: `result: Error`, `so_files: Array` (array of the
shared/static objects which contains dictionaries with the following
keys: `path: String`, `tags: PackedStringArray`, and
`target_folder: String`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_save_zip}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**save_zip**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlatform_method_save_zip>`{.interpreted-text
role="ref"}

Saves ZIP archive and returns
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following keys: `result: Error`, `so_files: Array` (array of the
shared/static objects which contains dictionaries with the following
keys: `path: String`, `tags: PackedStringArray`, and
`target_folder: String`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_save_zip_patch}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**save_zip_patch**(preset:
`EditorExportPreset<class_EditorExportPreset>`{.interpreted-text
role="ref"}, debug: `bool<class_bool>`{.interpreted-text role="ref"},
path: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorExportPlatform_method_save_zip_patch>`{.interpreted-text
role="ref"}

Saves patch ZIP archive and returns
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} with the
following keys: `result: Error`, `so_files: Array` (array of the
shared/static objects which contains dictionaries with the following
keys: `path: String`, `tags: PackedStringArray`, and
`target_folder: String`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_ssh_push_to_remote}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ssh_push_to_remote**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `String<class_String>`{.interpreted-text role="ref"},
scp_args: `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, src_file: `String<class_String>`{.interpreted-text
role="ref"}, dst_file: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_ssh_push_to_remote>`{.interpreted-text
role="ref"}

Uploads specified file over SCP protocol to the remote host.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_ssh_run_on_remote}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**ssh_run_on_remote**(host: `String<class_String>`{.interpreted-text
role="ref"}, port: `String<class_String>`{.interpreted-text role="ref"},
ssh_arg: `PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, cmd_args: `String<class_String>`{.interpreted-text
role="ref"}, output: `Array<class_Array>`{.interpreted-text role="ref"}
= \[\], port_fwd: `int<class_int>`{.interpreted-text role="ref"} = -1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_ssh_run_on_remote>`{.interpreted-text
role="ref"}

Executes specified command on the remote host via SSH protocol and
returns command output in the `output`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorExportPlatform_method_ssh_run_on_remote_no_wait}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**ssh_run_on_remote_no_wait**(host:
`String<class_String>`{.interpreted-text role="ref"}, port:
`String<class_String>`{.interpreted-text role="ref"}, ssh_args:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, cmd_args: `String<class_String>`{.interpreted-text
role="ref"}, port_fwd: `int<class_int>`{.interpreted-text role="ref"} =
-1)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorExportPlatform_method_ssh_run_on_remote_no_wait>`{.interpreted-text
role="ref"}

Executes specified command on the remote host via SSH protocol and
returns process ID (on the remote host) without waiting for command to
finish.
