github_url
:   hide

# FileDialog {#class_FileDialog}

**Inherits:**
`ConfirmationDialog<class_ConfirmationDialog>`{.interpreted-text
role="ref"} **\<** `AcceptDialog<class_AcceptDialog>`{.interpreted-text
role="ref"} **\<** `Window<class_Window>`{.interpreted-text role="ref"}
**\<** `Viewport<class_Viewport>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A dialog for selecting files or directories in the filesystem.

::: rst-class
classref-introduction-group
:::

## Description

**FileDialog** is a preset dialog used to choose files and directories
in the filesystem. It supports filter masks. **FileDialog**
automatically sets its window title according to the
`file_mode<class_FileDialog_property_file_mode>`{.interpreted-text
role="ref"}. If you want to use a custom title, disable this by setting
`mode_overrides_title<class_FileDialog_property_mode_overrides_title>`{.interpreted-text
role="ref"} to `false`.

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

:::: {#class_FileDialog_signal_dir_selected}
::: rst-class
classref-signal
:::
::::

**dir_selected**(dir: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileDialog_signal_dir_selected>`{.interpreted-text role="ref"}

Emitted when the user selects a directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_signal_file_selected}
::: rst-class
classref-signal
:::
::::

**file_selected**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileDialog_signal_file_selected>`{.interpreted-text
role="ref"}

Emitted when the user selects a file by double-clicking it or pressing
the **OK** button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_signal_filename_filter_changed}
::: rst-class
classref-signal
:::
::::

**filename_filter_changed**(filter:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_FileDialog_signal_filename_filter_changed>`{.interpreted-text
role="ref"}

Emitted when the filter for file names changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_signal_files_selected}
::: rst-class
classref-signal
:::
::::

**files_selected**(paths:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_FileDialog_signal_files_selected>`{.interpreted-text
role="ref"}

Emitted when the user selects multiple files.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_FileDialog_FileMode}
::: rst-class
classref-enumeration
:::
::::

enum **FileMode**: `🔗<enum_FileDialog_FileMode>`{.interpreted-text
role="ref"}

:::: {#class_FileDialog_constant_FILE_MODE_OPEN_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_FILE** = `0`

The dialog allows selecting one, and only one file.

:::: {#class_FileDialog_constant_FILE_MODE_OPEN_FILES}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_FILES** = `1`

The dialog allows selecting multiple files.

:::: {#class_FileDialog_constant_FILE_MODE_OPEN_DIR}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_DIR** = `2`

The dialog only allows selecting a directory, disallowing the selection
of any file.

:::: {#class_FileDialog_constant_FILE_MODE_OPEN_ANY}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_ANY** = `3`

The dialog allows selecting one file or directory.

:::: {#class_FileDialog_constant_FILE_MODE_SAVE_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_SAVE_FILE** = `4`

The dialog will warn when a file exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FileDialog_Access}
::: rst-class
classref-enumeration
:::
::::

enum **Access**: `🔗<enum_FileDialog_Access>`{.interpreted-text
role="ref"}

:::: {#class_FileDialog_constant_ACCESS_RESOURCES}
::: rst-class
classref-enumeration-constant
:::
::::

`Access<enum_FileDialog_Access>`{.interpreted-text role="ref"}
**ACCESS_RESOURCES** = `0`

The dialog only allows accessing files under the
`Resource<class_Resource>`{.interpreted-text role="ref"} path
(`res://`).

:::: {#class_FileDialog_constant_ACCESS_USERDATA}
::: rst-class
classref-enumeration-constant
:::
::::

`Access<enum_FileDialog_Access>`{.interpreted-text role="ref"}
**ACCESS_USERDATA** = `1`

The dialog only allows accessing files under user data path (`user://`).

:::: {#class_FileDialog_constant_ACCESS_FILESYSTEM}
::: rst-class
classref-enumeration-constant
:::
::::

`Access<enum_FileDialog_Access>`{.interpreted-text role="ref"}
**ACCESS_FILESYSTEM** = `2`

The dialog allows accessing files on the whole file system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FileDialog_DisplayMode}
::: rst-class
classref-enumeration
:::
::::

enum **DisplayMode**:
`🔗<enum_FileDialog_DisplayMode>`{.interpreted-text role="ref"}

:::: {#class_FileDialog_constant_DISPLAY_THUMBNAILS}
::: rst-class
classref-enumeration-constant
:::
::::

`DisplayMode<enum_FileDialog_DisplayMode>`{.interpreted-text role="ref"}
**DISPLAY_THUMBNAILS** = `0`

The dialog displays files as a grid of thumbnails. Use
`thumbnail_size<class_FileDialog_theme_constant_thumbnail_size>`{.interpreted-text
role="ref"} to adjust their size.

:::: {#class_FileDialog_constant_DISPLAY_LIST}
::: rst-class
classref-enumeration-constant
:::
::::

`DisplayMode<enum_FileDialog_DisplayMode>`{.interpreted-text role="ref"}
**DISPLAY_LIST** = `1`

The dialog displays files as a list of filenames.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_FileDialog_Customization}
::: rst-class
classref-enumeration
:::
::::

enum **Customization**:
`🔗<enum_FileDialog_Customization>`{.interpreted-text role="ref"}

:::: {#class_FileDialog_constant_CUSTOMIZATION_HIDDEN_FILES}
::: rst-class
classref-enumeration-constant
:::
::::

`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} **CUSTOMIZATION_HIDDEN_FILES** = `0`

Toggles visibility of the favorite button, and the favorite list on the
left side of the dialog.

Equivalent to
`hidden_files_toggle_enabled<class_FileDialog_property_hidden_files_toggle_enabled>`{.interpreted-text
role="ref"}.

:::: {#class_FileDialog_constant_CUSTOMIZATION_CREATE_FOLDER}
::: rst-class
classref-enumeration-constant
:::
::::

`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} **CUSTOMIZATION_CREATE_FOLDER** = `1`

If enabled, shows the button for creating new directories (when using
`FILE_MODE_OPEN_DIR<class_FileDialog_constant_FILE_MODE_OPEN_DIR>`{.interpreted-text
role="ref"},
`FILE_MODE_OPEN_ANY<class_FileDialog_constant_FILE_MODE_OPEN_ANY>`{.interpreted-text
role="ref"}, or
`FILE_MODE_SAVE_FILE<class_FileDialog_constant_FILE_MODE_SAVE_FILE>`{.interpreted-text
role="ref"}).

Equivalent to
`folder_creation_enabled<class_FileDialog_property_folder_creation_enabled>`{.interpreted-text
role="ref"}.

:::: {#class_FileDialog_constant_CUSTOMIZATION_FILE_FILTER}
::: rst-class
classref-enumeration-constant
:::
::::

`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} **CUSTOMIZATION_FILE_FILTER** = `2`

If enabled, shows the toggle file filter button.

Equivalent to
`file_filter_toggle_enabled<class_FileDialog_property_file_filter_toggle_enabled>`{.interpreted-text
role="ref"}.

:::: {#class_FileDialog_constant_CUSTOMIZATION_FILE_SORT}
::: rst-class
classref-enumeration-constant
:::
::::

`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} **CUSTOMIZATION_FILE_SORT** = `3`

If enabled, shows the file sorting options button.

Equivalent to
`file_sort_options_enabled<class_FileDialog_property_file_sort_options_enabled>`{.interpreted-text
role="ref"}.

:::: {#class_FileDialog_constant_CUSTOMIZATION_FAVORITES}
::: rst-class
classref-enumeration-constant
:::
::::

`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} **CUSTOMIZATION_FAVORITES** = `4`

If enabled, shows the toggle favorite button and favorite list on the
left side of the dialog.

Equivalent to
`favorites_enabled<class_FileDialog_property_favorites_enabled>`{.interpreted-text
role="ref"}.

:::: {#class_FileDialog_constant_CUSTOMIZATION_RECENT}
::: rst-class
classref-enumeration-constant
:::
::::

`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} **CUSTOMIZATION_RECENT** = `5`

If enabled, shows the recent directories list on the left side of the
dialog.

Equivalent to
`recent_list_enabled<class_FileDialog_property_recent_list_enabled>`{.interpreted-text
role="ref"}.

:::: {#class_FileDialog_constant_CUSTOMIZATION_LAYOUT}
::: rst-class
classref-enumeration-constant
:::
::::

`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} **CUSTOMIZATION_LAYOUT** = `6`

If enabled, shows the layout switch buttons (list/thumbnails).

Equivalent to
`layout_toggle_enabled<class_FileDialog_property_layout_toggle_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_FileDialog_property_access}
::: rst-class
classref-property
:::
::::

`Access<enum_FileDialog_Access>`{.interpreted-text role="ref"}
**access** = `0`
`🔗<class_FileDialog_property_access>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_access**(value:
  `Access<enum_FileDialog_Access>`{.interpreted-text role="ref"})
- `Access<enum_FileDialog_Access>`{.interpreted-text role="ref"}
  **get_access**()

The file system access scope.

\*\*Warning:\*\* In Web builds, FileDialog cannot access the host file
system. In sandboxed Linux and macOS environments,
`use_native_dialog<class_FileDialog_property_use_native_dialog>`{.interpreted-text
role="ref"} is automatically used to allow limited access to host file
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_current_dir}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **current_dir**
`🔗<class_FileDialog_property_current_dir>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_dir**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_current_dir**()

The current working directory of the file dialog.

\*\*Note:\*\* For native file dialogs, this property is only treated as
a hint and may not be respected by specific OS implementations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_current_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **current_file**
`🔗<class_FileDialog_property_current_file>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_file**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_current_file**()

The currently selected file of the file dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_current_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **current_path**
`🔗<class_FileDialog_property_current_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_path**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_current_path**()

The currently selected file path of the file dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_display_mode}
::: rst-class
classref-property
:::
::::

`DisplayMode<enum_FileDialog_DisplayMode>`{.interpreted-text role="ref"}
**display_mode** = `0`
`🔗<class_FileDialog_property_display_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_display_mode**(value:
  `DisplayMode<enum_FileDialog_DisplayMode>`{.interpreted-text
  role="ref"})
- `DisplayMode<enum_FileDialog_DisplayMode>`{.interpreted-text
  role="ref"} **get_display_mode**()

Display mode of the dialog\'s file list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_favorites_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **favorites_enabled** =
`true`
`🔗<class_FileDialog_property_favorites_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, shows the toggle favorite button and favorite list on the
left side of the dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_file_filter_toggle_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**file_filter_toggle_enabled** = `true`
`🔗<class_FileDialog_property_file_filter_toggle_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, shows the toggle file filter button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_file_mode}
::: rst-class
classref-property
:::
::::

`FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"}
**file_mode** = `4`
`🔗<class_FileDialog_property_file_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_file_mode**(value:
  `FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"})
- `FileMode<enum_FileDialog_FileMode>`{.interpreted-text role="ref"}
  **get_file_mode**()

The dialog\'s open or save mode, which affects the selection behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_file_sort_options_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**file_sort_options_enabled** = `true`
`🔗<class_FileDialog_property_file_sort_options_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, shows the file sorting options button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_filename_filter}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **filename_filter**
= `""` `🔗<class_FileDialog_property_filename_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filename_filter**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_filename_filter**()

The filter for file names (case-insensitive). When set to a non-empty
string, only files that contains the substring will be shown.
`filename_filter<class_FileDialog_property_filename_filter>`{.interpreted-text
role="ref"} can be edited by the user with the filter button at the top
of the file dialog.

See also `filters<class_FileDialog_property_filters>`{.interpreted-text
role="ref"}, which should be used to restrict the file types that can be
selected instead of
`filename_filter<class_FileDialog_property_filename_filter>`{.interpreted-text
role="ref"} which is meant to be set by the user.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_filters}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **filters** = `PackedStringArray()`
`🔗<class_FileDialog_property_filters>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filters**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_filters**()

The available file type filters. Each filter string in the array should
be formatted like this:
`*.png,*.jpg,*.jpeg;Image Files;image/png,image/jpeg`. The description
text of the filter is optional and can be omitted. Both file extensions
and MIME type should be always set.

\*\*Note:\*\* Embedded file dialog and Windows file dialog support only
file extensions, while Android, Linux, and macOS file dialogs also
support MIME types.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_folder_creation_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**folder_creation_enabled** = `true`
`🔗<class_FileDialog_property_folder_creation_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, shows the button for creating new directories (when using
`FILE_MODE_OPEN_DIR<class_FileDialog_constant_FILE_MODE_OPEN_DIR>`{.interpreted-text
role="ref"},
`FILE_MODE_OPEN_ANY<class_FileDialog_constant_FILE_MODE_OPEN_ANY>`{.interpreted-text
role="ref"}, or
`FILE_MODE_SAVE_FILE<class_FileDialog_constant_FILE_MODE_SAVE_FILE>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_hidden_files_toggle_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**hidden_files_toggle_enabled** = `true`
`🔗<class_FileDialog_property_hidden_files_toggle_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, shows the toggle hidden files button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_layout_toggle_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**layout_toggle_enabled** = `true`
`🔗<class_FileDialog_property_layout_toggle_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, shows the layout switch buttons (list/thumbnails).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_mode_overrides_title}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**mode_overrides_title** = `true`
`🔗<class_FileDialog_property_mode_overrides_title>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mode_overrides_title**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_mode_overriding_title**()

If `true`, changing the
`file_mode<class_FileDialog_property_file_mode>`{.interpreted-text
role="ref"} property will set the window title accordingly (e.g. setting
`file_mode<class_FileDialog_property_file_mode>`{.interpreted-text
role="ref"} to
`FILE_MODE_OPEN_FILE<class_FileDialog_constant_FILE_MODE_OPEN_FILE>`{.interpreted-text
role="ref"} will change the window title to \"Open a File\").

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_option_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **option_count** = `0`
`🔗<class_FileDialog_property_option_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_option_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_option_count**()

The number of additional
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"}s and
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"}es in the
dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_recent_list_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **recent_list_enabled**
= `true`
`🔗<class_FileDialog_property_recent_list_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"}, enabled: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_customization_flag_enabled**(flag:
  `Customization<enum_FileDialog_Customization>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, shows the recent directories list on the left side of the
dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_root_subfolder}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **root_subfolder**
= `""` `🔗<class_FileDialog_property_root_subfolder>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_subfolder**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_root_subfolder**()

If non-empty, the given sub-folder will be \"root\" of this
**FileDialog**, i.e. user won\'t be able to go to its parent directory.

\*\*Note:\*\* This property is ignored by native file dialogs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_show_hidden_files}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_hidden_files** =
`false`
`🔗<class_FileDialog_property_show_hidden_files>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_hidden_files**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_showing_hidden_files**()

If `true`, the dialog will show hidden files.

\*\*Note:\*\* This property is ignored by native file dialogs on Android
and Linux.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_property_use_native_dialog}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_native_dialog** =
`false`
`🔗<class_FileDialog_property_use_native_dialog>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_native_dialog**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_native_dialog**()

If `true`, and if supported by the current
`DisplayServer<class_DisplayServer>`{.interpreted-text role="ref"}, OS
native dialog will be used instead of custom one.

\*\*Note:\*\* On Android, it is only supported for Android 10+ devices
and when using
`ACCESS_FILESYSTEM<class_FileDialog_constant_ACCESS_FILESYSTEM>`{.interpreted-text
role="ref"}. For access mode
`ACCESS_RESOURCES<class_FileDialog_constant_ACCESS_RESOURCES>`{.interpreted-text
role="ref"} and
`ACCESS_USERDATA<class_FileDialog_constant_ACCESS_USERDATA>`{.interpreted-text
role="ref"}, the system will fall back to custom FileDialog.

\*\*Note:\*\* On Linux and macOS, sandboxed apps always use native
dialogs to access the host file system.

\*\*Note:\*\* On macOS, sandboxed apps will save security-scoped
bookmarks to retain access to the opened folders across multiple
sessions. Use
`OS.get_granted_permissions()<class_OS_method_get_granted_permissions>`{.interpreted-text
role="ref"} to get a list of saved bookmarks.

\*\*Note:\*\* Native dialogs are isolated from the base process, file
dialog properties can\'t be modified once the dialog is shown.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FileDialog_method_add_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_filter**(filter: `String<class_String>`{.interpreted-text
role="ref"}, description: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`🔗<class_FileDialog_method_add_filter>`{.interpreted-text role="ref"}

Adds a comma-separated file name `filter` option to the **FileDialog**
with an optional `description`, which restricts what files can be
picked.

A `filter` should be of the form `"filename.extension"`, where filename
and extension can be `*` to match any string. Filters starting with `.`
(i.e. empty filenames) are not allowed.

For example, a `filter` of `"*.png, *.jpg"` and a `description` of
`"Images"` results in filter text \"Images (\*.png, \*.jpg)\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_add_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_option**(name: `String<class_String>`{.interpreted-text
role="ref"}, values:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, default_value_index: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_FileDialog_method_add_option>`{.interpreted-text
role="ref"}

Adds an additional `OptionButton<class_OptionButton>`{.interpreted-text
role="ref"} to the file dialog. If `values` is empty, a
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} is added
instead.

`default_value_index` should be an index of the value in the `values`.
If `values` is empty it should be either `1` (checked), or `0`
(unchecked).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_clear_filename_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_filename_filter**()
`🔗<class_FileDialog_method_clear_filename_filter>`{.interpreted-text
role="ref"}

Clear the filter for file names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_clear_filters}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_filters**()
`🔗<class_FileDialog_method_clear_filters>`{.interpreted-text
role="ref"}

Clear all the added filters in the dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_deselect_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**deselect_all**()
`🔗<class_FileDialog_method_deselect_all>`{.interpreted-text role="ref"}

Clear all currently selected items in the dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_get_line_edit}
::: rst-class
classref-method
:::
::::

`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}
**get_line_edit**()
`🔗<class_FileDialog_method_get_line_edit>`{.interpreted-text
role="ref"}

Returns the LineEdit for the selected file.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_get_option_default}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_option_default**(option: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileDialog_method_get_option_default>`{.interpreted-text
role="ref"}

Returns the default value index of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_get_option_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_option_name**(option: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileDialog_method_get_option_name>`{.interpreted-text
role="ref"}

Returns the name of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_get_option_values}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_option_values**(option:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileDialog_method_get_option_values>`{.interpreted-text
role="ref"}

Returns an array of values of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} with
index `option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_get_selected_options}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_selected_options**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileDialog_method_get_selected_options>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
with the selected values of the additional
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"}s and/or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"}es.
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} keys are
names and values are selected value indices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_get_vbox}
::: rst-class
classref-method
:::
::::

`VBoxContainer<class_VBoxContainer>`{.interpreted-text role="ref"}
**get_vbox**() `🔗<class_FileDialog_method_get_vbox>`{.interpreted-text
role="ref"}

Returns the vertical box container of the dialog, custom controls can be
added to it.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

\*\*Note:\*\* Changes to this node are ignored by native file dialogs,
use `add_option()<class_FileDialog_method_add_option>`{.interpreted-text
role="ref"} to add custom elements to the dialog instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_invalidate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**invalidate**()
`🔗<class_FileDialog_method_invalidate>`{.interpreted-text role="ref"}

Invalidate and update the current dialog content list.

\*\*Note:\*\* This method does nothing on native file dialogs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_is_customization_flag_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_customization_flag_enabled**(flag:
`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_FileDialog_method_is_customization_flag_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the provided `flag` is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_set_customization_flag_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_customization_flag_enabled**(flag:
`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_FileDialog_method_set_customization_flag_enabled>`{.interpreted-text
role="ref"}

Toggles the specified customization `flag`, allowing to customize
features available in this **FileDialog**. See
`Customization<enum_FileDialog_Customization>`{.interpreted-text
role="ref"} for options.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_set_option_default}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_option_default**(option: `int<class_int>`{.interpreted-text
role="ref"}, default_value_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_FileDialog_method_set_option_default>`{.interpreted-text
role="ref"}

Sets the default value index of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_set_option_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_option_name**(option: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_FileDialog_method_set_option_name>`{.interpreted-text
role="ref"}

Sets the name of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_method_set_option_values}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_option_values**(option: `int<class_int>`{.interpreted-text
role="ref"}, values:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_FileDialog_method_set_option_values>`{.interpreted-text
role="ref"}

Sets the option values of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} with
index `option`.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Theme Property Descriptions

:::: {#class_FileDialog_theme_color_file_disabled_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**file_disabled_color** = `Color(1, 1, 1, 0.25)`
`🔗<class_FileDialog_theme_color_file_disabled_color>`{.interpreted-text
role="ref"}

The color tint for disabled files (when the **FileDialog** is used in
open folder mode).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_color_file_icon_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **file_icon_color** =
`Color(1, 1, 1, 1)`
`🔗<class_FileDialog_theme_color_file_icon_color>`{.interpreted-text
role="ref"}

The color modulation applied to the file icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_color_folder_icon_color}
::: rst-class
classref-themeproperty
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **folder_icon_color**
= `Color(1, 1, 1, 1)`
`🔗<class_FileDialog_theme_color_folder_icon_color>`{.interpreted-text
role="ref"}

The color modulation applied to the folder icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_constant_thumbnail_size}
::: rst-class
classref-themeproperty
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **thumbnail_size** = `64`
`🔗<class_FileDialog_theme_constant_thumbnail_size>`{.interpreted-text
role="ref"}

The size of thumbnail icons when
`DISPLAY_THUMBNAILS<class_FileDialog_constant_DISPLAY_THUMBNAILS>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_back_folder}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**back_folder**
`🔗<class_FileDialog_theme_icon_back_folder>`{.interpreted-text
role="ref"}

Custom icon for the back arrow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_create_folder}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**create_folder**
`🔗<class_FileDialog_theme_icon_create_folder>`{.interpreted-text
role="ref"}

Custom icon for the create folder button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_favorite}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **favorite**
`🔗<class_FileDialog_theme_icon_favorite>`{.interpreted-text role="ref"}

Custom icon for favorite folder button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_favorite_down}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**favorite_down**
`🔗<class_FileDialog_theme_icon_favorite_down>`{.interpreted-text
role="ref"}

Custom icon for button to move down a favorite entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_favorite_up}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**favorite_up**
`🔗<class_FileDialog_theme_icon_favorite_up>`{.interpreted-text
role="ref"}

Custom icon for button to move up a favorite entry.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_file}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **file**
`🔗<class_FileDialog_theme_icon_file>`{.interpreted-text role="ref"}

Custom icon for files.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_file_thumbnail}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**file_thumbnail**
`🔗<class_FileDialog_theme_icon_file_thumbnail>`{.interpreted-text
role="ref"}

Icon for files when in thumbnail mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_folder}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **folder**
`🔗<class_FileDialog_theme_icon_folder>`{.interpreted-text role="ref"}

Custom icon for folders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_folder_thumbnail}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**folder_thumbnail**
`🔗<class_FileDialog_theme_icon_folder_thumbnail>`{.interpreted-text
role="ref"}

Icon for folders when in thumbnail mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_forward_folder}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**forward_folder**
`🔗<class_FileDialog_theme_icon_forward_folder>`{.interpreted-text
role="ref"}

Custom icon for the forward arrow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_list_mode}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **list_mode**
`🔗<class_FileDialog_theme_icon_list_mode>`{.interpreted-text
role="ref"}

Icon for the button that enables list mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_parent_folder}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**parent_folder**
`🔗<class_FileDialog_theme_icon_parent_folder>`{.interpreted-text
role="ref"}

Custom icon for the parent folder arrow.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_reload}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **reload**
`🔗<class_FileDialog_theme_icon_reload>`{.interpreted-text role="ref"}

Custom icon for the reload button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_sort}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **sort**
`🔗<class_FileDialog_theme_icon_sort>`{.interpreted-text role="ref"}

Custom icon for the sorting options menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_thumbnail_mode}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**thumbnail_mode**
`🔗<class_FileDialog_theme_icon_thumbnail_mode>`{.interpreted-text
role="ref"}

Icon for the button that enables thumbnail mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_toggle_filename_filter}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**toggle_filename_filter**
`🔗<class_FileDialog_theme_icon_toggle_filename_filter>`{.interpreted-text
role="ref"}

Custom icon for the toggle button for the filter for file names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileDialog_theme_icon_toggle_hidden}
::: rst-class
classref-themeproperty
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**toggle_hidden**
`🔗<class_FileDialog_theme_icon_toggle_hidden>`{.interpreted-text
role="ref"}

Custom icon for the toggle hidden button.
