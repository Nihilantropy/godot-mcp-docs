github_url
:   hide

# EditorFileDialog {#class_EditorFileDialog}

**Inherits:**
`ConfirmationDialog<class_ConfirmationDialog>`{.interpreted-text
role="ref"} **\<** `AcceptDialog<class_AcceptDialog>`{.interpreted-text
role="ref"} **\<** `Window<class_Window>`{.interpreted-text role="ref"}
**\<** `Viewport<class_Viewport>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A modified version of `FileDialog<class_FileDialog>`{.interpreted-text
role="ref"} used by the editor.

::: rst-class
classref-introduction-group
:::

## Description

**EditorFileDialog** is an enhanced version of
`FileDialog<class_FileDialog>`{.interpreted-text role="ref"} available
only to editor plugins. Additional features include list of
favorited/recent files and the ability to see files as thumbnails grid
instead of list.

Unlike `FileDialog<class_FileDialog>`{.interpreted-text role="ref"},
**EditorFileDialog** does not have a property for using native dialogs.
Instead, native dialogs can be enabled globally via the
`EditorSettings.interface/editor/use_native_file_dialogs<class_EditorSettings_property_interface/editor/use_native_file_dialogs>`{.interpreted-text
role="ref"} editor setting. They are also enabled automatically when
running in sandbox (e.g. on macOS).

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

## Signals

:::: {#class_EditorFileDialog_signal_dir_selected}
::: rst-class
classref-signal
:::
::::

**dir_selected**(dir: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileDialog_signal_dir_selected>`{.interpreted-text
role="ref"}

Emitted when a directory is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_signal_file_selected}
::: rst-class
classref-signal
:::
::::

**file_selected**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileDialog_signal_file_selected>`{.interpreted-text
role="ref"}

Emitted when a file is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_signal_filename_filter_changed}
::: rst-class
classref-signal
:::
::::

**filename_filter_changed**(filter:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorFileDialog_signal_filename_filter_changed>`{.interpreted-text
role="ref"}

Emitted when the filter for file names changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_signal_files_selected}
::: rst-class
classref-signal
:::
::::

**files_selected**(paths:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileDialog_signal_files_selected>`{.interpreted-text
role="ref"}

Emitted when multiple files are selected.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_EditorFileDialog_FileMode}
::: rst-class
classref-enumeration
:::
::::

enum **FileMode**:
`🔗<enum_EditorFileDialog_FileMode>`{.interpreted-text role="ref"}

:::: {#class_EditorFileDialog_constant_FILE_MODE_OPEN_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_FILE** = `0`

The **EditorFileDialog** can select only one file. Accepting the window
will open the file.

:::: {#class_EditorFileDialog_constant_FILE_MODE_OPEN_FILES}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_FILES** = `1`

The **EditorFileDialog** can select multiple files. Accepting the window
will open all files.

:::: {#class_EditorFileDialog_constant_FILE_MODE_OPEN_DIR}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_DIR** = `2`

The **EditorFileDialog** can select only one directory. Accepting the
window will open the directory.

:::: {#class_EditorFileDialog_constant_FILE_MODE_OPEN_ANY}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_OPEN_ANY** = `3`

The **EditorFileDialog** can select a file or directory. Accepting the
window will open it.

:::: {#class_EditorFileDialog_constant_FILE_MODE_SAVE_FILE}
::: rst-class
classref-enumeration-constant
:::
::::

`FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text role="ref"}
**FILE_MODE_SAVE_FILE** = `4`

The **EditorFileDialog** can select only one file. Accepting the window
will save the file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorFileDialog_Access}
::: rst-class
classref-enumeration
:::
::::

enum **Access**: `🔗<enum_EditorFileDialog_Access>`{.interpreted-text
role="ref"}

:::: {#class_EditorFileDialog_constant_ACCESS_RESOURCES}
::: rst-class
classref-enumeration-constant
:::
::::

`Access<enum_EditorFileDialog_Access>`{.interpreted-text role="ref"}
**ACCESS_RESOURCES** = `0`

The **EditorFileDialog** can only view `res://` directory contents.

:::: {#class_EditorFileDialog_constant_ACCESS_USERDATA}
::: rst-class
classref-enumeration-constant
:::
::::

`Access<enum_EditorFileDialog_Access>`{.interpreted-text role="ref"}
**ACCESS_USERDATA** = `1`

The **EditorFileDialog** can only view `user://` directory contents.

:::: {#class_EditorFileDialog_constant_ACCESS_FILESYSTEM}
::: rst-class
classref-enumeration-constant
:::
::::

`Access<enum_EditorFileDialog_Access>`{.interpreted-text role="ref"}
**ACCESS_FILESYSTEM** = `2`

The **EditorFileDialog** can view the entire local file system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorFileDialog_DisplayMode}
::: rst-class
classref-enumeration
:::
::::

enum **DisplayMode**:
`🔗<enum_EditorFileDialog_DisplayMode>`{.interpreted-text role="ref"}

:::: {#class_EditorFileDialog_constant_DISPLAY_THUMBNAILS}
::: rst-class
classref-enumeration-constant
:::
::::

`DisplayMode<enum_EditorFileDialog_DisplayMode>`{.interpreted-text
role="ref"} **DISPLAY_THUMBNAILS** = `0`

The **EditorFileDialog** displays resources as thumbnails.

:::: {#class_EditorFileDialog_constant_DISPLAY_LIST}
::: rst-class
classref-enumeration-constant
:::
::::

`DisplayMode<enum_EditorFileDialog_DisplayMode>`{.interpreted-text
role="ref"} **DISPLAY_LIST** = `1`

The **EditorFileDialog** displays resources as a list of filenames.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EditorFileDialog_property_access}
::: rst-class
classref-property
:::
::::

`Access<enum_EditorFileDialog_Access>`{.interpreted-text role="ref"}
**access** = `0`
`🔗<class_EditorFileDialog_property_access>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_access**(value:
  `Access<enum_EditorFileDialog_Access>`{.interpreted-text role="ref"})
- `Access<enum_EditorFileDialog_Access>`{.interpreted-text role="ref"}
  **get_access**()

The location from which the user may select a file, including `res://`,
`user://`, and the local file system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_current_dir}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **current_dir**
`🔗<class_EditorFileDialog_property_current_dir>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_dir**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_current_dir**()

The currently occupied directory.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_current_file}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **current_file**
`🔗<class_EditorFileDialog_property_current_file>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_file**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_current_file**()

The currently selected file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_current_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **current_path**
`🔗<class_EditorFileDialog_property_current_path>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_path**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_current_path**()

The file system path in the address bar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_disable_overwrite_warning}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**disable_overwrite_warning** = `false`
`🔗<class_EditorFileDialog_property_disable_overwrite_warning>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disable_overwrite_warning**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_overwrite_warning_disabled**()

If `true`, the **EditorFileDialog** will not warn the user before
overwriting files.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_display_mode}
::: rst-class
classref-property
:::
::::

`DisplayMode<enum_EditorFileDialog_DisplayMode>`{.interpreted-text
role="ref"} **display_mode** = `0`
`🔗<class_EditorFileDialog_property_display_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_display_mode**(value:
  `DisplayMode<enum_EditorFileDialog_DisplayMode>`{.interpreted-text
  role="ref"})
- `DisplayMode<enum_EditorFileDialog_DisplayMode>`{.interpreted-text
  role="ref"} **get_display_mode**()

The view format in which the **EditorFileDialog** displays resources to
the user.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_file_mode}
::: rst-class
classref-property
:::
::::

`FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text role="ref"}
**file_mode** = `4`
`🔗<class_EditorFileDialog_property_file_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_file_mode**(value:
  `FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text
  role="ref"})
- `FileMode<enum_EditorFileDialog_FileMode>`{.interpreted-text
  role="ref"} **get_file_mode**()

The dialog\'s open or save mode, which affects the selection behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_filters}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **filters** = `PackedStringArray()`
`🔗<class_EditorFileDialog_property_filters>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_filters**(value:
  `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"})
- `PackedStringArray<class_PackedStringArray>`{.interpreted-text
  role="ref"} **get_filters**()

The available file type filters. For example, this shows only `.png` and
`.gd` files:
`set_filters(PackedStringArray(["*.png ; PNG Images","*.gd ; GDScript Files"]))`.
Multiple file types can also be specified in a single filter.
`"*.png, *.jpg, *.jpeg ; Supported Images"` will show both PNG and JPEG
files when selected.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_property_option_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **option_count** = `0`
`🔗<class_EditorFileDialog_property_option_count>`{.interpreted-text
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

:::: {#class_EditorFileDialog_property_show_hidden_files}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **show_hidden_files** =
`false`
`🔗<class_EditorFileDialog_property_show_hidden_files>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_show_hidden_files**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_showing_hidden_files**()

If `true`, hidden files and directories will be visible in the
**EditorFileDialog**. This property is synchronized with
`EditorSettings.filesystem/file_dialog/show_hidden_files<class_EditorSettings_property_filesystem/file_dialog/show_hidden_files>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorFileDialog_method_add_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_filter**(filter: `String<class_String>`{.interpreted-text
role="ref"}, description: `String<class_String>`{.interpreted-text
role="ref"} = \"\")
`🔗<class_EditorFileDialog_method_add_filter>`{.interpreted-text
role="ref"}

Adds a comma-separated file name `filter` option to the
**EditorFileDialog** with an optional `description`, which restricts
what files can be picked.

A `filter` should be of the form `"filename.extension"`, where filename
and extension can be `*` to match any string. Filters starting with `.`
(i.e. empty filenames) are not allowed.

For example, a `filter` of `"*.tscn, *.scn"` and a `description` of
`"Scenes"` results in filter text \"Scenes (\*.tscn, \*.scn)\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_add_option}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_option**(name: `String<class_String>`{.interpreted-text
role="ref"}, values:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"}, default_value_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileDialog_method_add_option>`{.interpreted-text
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

:::: {#class_EditorFileDialog_method_add_side_menu}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_side_menu**(menu: `Control<class_Control>`{.interpreted-text
role="ref"}, title: `String<class_String>`{.interpreted-text role="ref"}
= \"\")
`🔗<class_EditorFileDialog_method_add_side_menu>`{.interpreted-text
role="ref"}

Adds the given `menu` to the side of the file dialog with the given
`title` text on top. Only one side menu is allowed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_clear_filename_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_filename_filter**()
`🔗<class_EditorFileDialog_method_clear_filename_filter>`{.interpreted-text
role="ref"}

Clear the filter for file names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_clear_filters}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_filters**()
`🔗<class_EditorFileDialog_method_clear_filters>`{.interpreted-text
role="ref"}

Removes all filters except for \"All Files (\*.\*)\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_get_filename_filter}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_filename_filter**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileDialog_method_get_filename_filter>`{.interpreted-text
role="ref"}

Returns the value of the filter for file names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_get_line_edit}
::: rst-class
classref-method
:::
::::

`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}
**get_line_edit**()
`🔗<class_EditorFileDialog_method_get_line_edit>`{.interpreted-text
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

:::: {#class_EditorFileDialog_method_get_option_default}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_option_default**(option: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileDialog_method_get_option_default>`{.interpreted-text
role="ref"}

Returns the default value index of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_get_option_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_option_name**(option: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileDialog_method_get_option_name>`{.interpreted-text
role="ref"}

Returns the name of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_get_option_values}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_option_values**(option:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileDialog_method_get_option_values>`{.interpreted-text
role="ref"}

Returns an array of values of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} with
index `option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_get_selected_options}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**get_selected_options**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileDialog_method_get_selected_options>`{.interpreted-text
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

:::: {#class_EditorFileDialog_method_get_vbox}
::: rst-class
classref-method
:::
::::

`VBoxContainer<class_VBoxContainer>`{.interpreted-text role="ref"}
**get_vbox**()
`🔗<class_EditorFileDialog_method_get_vbox>`{.interpreted-text
role="ref"}

Returns the `VBoxContainer<class_VBoxContainer>`{.interpreted-text
role="ref"} used to display the file system.

\*\*Warning:\*\* This is a required internal node, removing and freeing
it may cause a crash. If you wish to hide it or any of its children, use
their
`CanvasItem.visible<class_CanvasItem_property_visible>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_invalidate}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**invalidate**()
`🔗<class_EditorFileDialog_method_invalidate>`{.interpreted-text
role="ref"}

Notify the **EditorFileDialog** that its view of the data is no longer
accurate. Updates the view contents on next view update.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_popup_file_dialog}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_file_dialog**()
`🔗<class_EditorFileDialog_method_popup_file_dialog>`{.interpreted-text
role="ref"}

Shows the **EditorFileDialog** at the default size and position for file
dialogs in the editor, and selects the file name if there is a current
file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_set_filename_filter}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_filename_filter**(filter: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileDialog_method_set_filename_filter>`{.interpreted-text
role="ref"}

Sets the value of the filter for file names.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_set_option_default}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_option_default**(option: `int<class_int>`{.interpreted-text
role="ref"}, default_value_index: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileDialog_method_set_option_default>`{.interpreted-text
role="ref"}

Sets the default value index of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_set_option_name}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_option_name**(option: `int<class_int>`{.interpreted-text
role="ref"}, name: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorFileDialog_method_set_option_name>`{.interpreted-text
role="ref"}

Sets the name of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} or
`CheckBox<class_CheckBox>`{.interpreted-text role="ref"} with index
`option`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileDialog_method_set_option_values}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_option_values**(option: `int<class_int>`{.interpreted-text
role="ref"}, values:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileDialog_method_set_option_values>`{.interpreted-text
role="ref"}

Sets the option values of the
`OptionButton<class_OptionButton>`{.interpreted-text role="ref"} with
index `option`.
