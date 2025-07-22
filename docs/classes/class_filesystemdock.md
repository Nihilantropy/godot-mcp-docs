github_url
:   hide

# FileSystemDock {#class_FileSystemDock}

**Inherits:** `VBoxContainer<class_VBoxContainer>`{.interpreted-text
role="ref"} **\<** `BoxContainer<class_BoxContainer>`{.interpreted-text
role="ref"} **\<** `Container<class_Container>`{.interpreted-text
role="ref"} **\<** `Control<class_Control>`{.interpreted-text
role="ref"} **\<** `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} **\<** `Node<class_Node>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Godot editor\'s dock for managing files in the project.

::: rst-class
classref-introduction-group
:::

## Description

This class is available only in
`EditorPlugin<class_EditorPlugin>`{.interpreted-text role="ref"}s and
can\'t be instantiated. You can access it using
`EditorInterface.get_file_system_dock()<class_EditorInterface_method_get_file_system_dock>`{.interpreted-text
role="ref"}.

While **FileSystemDock** doesn\'t expose any methods for file
manipulation, it can listen for various file-related signals.

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

:::: {#class_FileSystemDock_signal_display_mode_changed}
::: rst-class
classref-signal
:::
::::

**display_mode_changed**()
`🔗<class_FileSystemDock_signal_display_mode_changed>`{.interpreted-text
role="ref"}

Emitted when the user switches file display mode or split mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_file_removed}
::: rst-class
classref-signal
:::
::::

**file_removed**(file: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_signal_file_removed>`{.interpreted-text
role="ref"}

Emitted when the given `file` was removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_files_moved}
::: rst-class
classref-signal
:::
::::

**files_moved**(old_file: `String<class_String>`{.interpreted-text
role="ref"}, new_file: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_signal_files_moved>`{.interpreted-text
role="ref"}

Emitted when a file is moved from `old_file` path to `new_file` path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_folder_color_changed}
::: rst-class
classref-signal
:::
::::

**folder_color_changed**()
`🔗<class_FileSystemDock_signal_folder_color_changed>`{.interpreted-text
role="ref"}

Emitted when folders change color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_folder_moved}
::: rst-class
classref-signal
:::
::::

**folder_moved**(old_folder: `String<class_String>`{.interpreted-text
role="ref"}, new_folder: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_signal_folder_moved>`{.interpreted-text
role="ref"}

Emitted when a folder is moved from `old_folder` path to `new_folder`
path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_folder_removed}
::: rst-class
classref-signal
:::
::::

**folder_removed**(folder: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_signal_folder_removed>`{.interpreted-text
role="ref"}

Emitted when the given `folder` was removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_inherit}
::: rst-class
classref-signal
:::
::::

**inherit**(file: `String<class_String>`{.interpreted-text role="ref"})
`🔗<class_FileSystemDock_signal_inherit>`{.interpreted-text role="ref"}

Emitted when a new scene is created that inherits the scene at `file`
path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_instantiate}
::: rst-class
classref-signal
:::
::::

**instantiate**(files:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_signal_instantiate>`{.interpreted-text
role="ref"}

Emitted when the given scenes are being instantiated in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_signal_resource_removed}
::: rst-class
classref-signal
:::
::::

**resource_removed**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_FileSystemDock_signal_resource_removed>`{.interpreted-text
role="ref"}

Emitted when an external `resource` had its file removed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_FileSystemDock_method_add_resource_tooltip_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_resource_tooltip_plugin**(plugin:
`EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_method_add_resource_tooltip_plugin>`{.interpreted-text
role="ref"}

Registers a new
`EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_method_navigate_to_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**navigate_to_path**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_method_navigate_to_path>`{.interpreted-text
role="ref"}

Sets the given `path` as currently selected, ensuring that the selected
file/directory is visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_FileSystemDock_method_remove_resource_tooltip_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_resource_tooltip_plugin**(plugin:
`EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`{.interpreted-text
role="ref"})
`🔗<class_FileSystemDock_method_remove_resource_tooltip_plugin>`{.interpreted-text
role="ref"}

Removes an
`EditorResourceTooltipPlugin<class_EditorResourceTooltipPlugin>`{.interpreted-text
role="ref"}. Fails if the plugin wasn\'t previously added.
