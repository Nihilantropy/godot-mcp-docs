github_url
:   hide

# EditorFileSystem {#class_EditorFileSystem}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Resource filesystem, as the editor sees it.

::: rst-class
classref-introduction-group
:::

## Description

This object holds information of all resources in the filesystem, their
types, etc.

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton using
`EditorInterface.get_resource_filesystem()<class_EditorInterface_method_get_resource_filesystem>`{.interpreted-text
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

## Signals

:::: {#class_EditorFileSystem_signal_filesystem_changed}
::: rst-class
classref-signal
:::
::::

**filesystem_changed**()
`🔗<class_EditorFileSystem_signal_filesystem_changed>`{.interpreted-text
role="ref"}

Emitted if the filesystem changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_signal_resources_reimported}
::: rst-class
classref-signal
:::
::::

**resources_reimported**(resources:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileSystem_signal_resources_reimported>`{.interpreted-text
role="ref"}

Emitted if a resource is reimported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_signal_resources_reimporting}
::: rst-class
classref-signal
:::
::::

**resources_reimporting**(resources:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileSystem_signal_resources_reimporting>`{.interpreted-text
role="ref"}

Emitted before a resource is reimported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_signal_resources_reload}
::: rst-class
classref-signal
:::
::::

**resources_reload**(resources:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileSystem_signal_resources_reload>`{.interpreted-text
role="ref"}

Emitted if at least one resource is reloaded when the filesystem is
scanned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_signal_script_classes_updated}
::: rst-class
classref-signal
:::
::::

**script_classes_updated**()
`🔗<class_EditorFileSystem_signal_script_classes_updated>`{.interpreted-text
role="ref"}

Emitted when the list of global script classes gets updated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_signal_sources_changed}
::: rst-class
classref-signal
:::
::::

**sources_changed**(exist: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileSystem_signal_sources_changed>`{.interpreted-text
role="ref"}

Emitted if the source of any imported file changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorFileSystem_method_get_file_type}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_file_type**(path: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystem_method_get_file_type>`{.interpreted-text
role="ref"}

Returns the resource type of the file, given the full path. This returns
a string such as `"Resource"` or `"GDScript"`, *not* a file extension
such as `".gd"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_get_filesystem}
::: rst-class
classref-method
:::
::::

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>`{.interpreted-text
role="ref"} **get_filesystem**()
`🔗<class_EditorFileSystem_method_get_filesystem>`{.interpreted-text
role="ref"}

Gets the root directory object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_get_filesystem_path}
::: rst-class
classref-method
:::
::::

`EditorFileSystemDirectory<class_EditorFileSystemDirectory>`{.interpreted-text
role="ref"} **get_filesystem_path**(path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorFileSystem_method_get_filesystem_path>`{.interpreted-text
role="ref"}

Returns a view into the filesystem at `path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_get_scanning_progress}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_scanning_progress**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystem_method_get_scanning_progress>`{.interpreted-text
role="ref"}

Returns the scan progress for 0 to 1 if the FS is being scanned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_is_scanning}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_scanning**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorFileSystem_method_is_scanning>`{.interpreted-text
role="ref"}

Returns `true` if the filesystem is being scanned.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_reimport_files}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reimport_files**(files:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileSystem_method_reimport_files>`{.interpreted-text
role="ref"}

Reimports a set of files. Call this if these files or their `.import`
files were directly edited by script or an external program.

If the file type changed or the file was newly created, use
`update_file()<class_EditorFileSystem_method_update_file>`{.interpreted-text
role="ref"} or
`scan()<class_EditorFileSystem_method_scan>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This function blocks until the import is finished.
However, the main loop iteration, including timers and
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, will occur during the import process due to progress bar
updates. Avoid calls to
`reimport_files()<class_EditorFileSystem_method_reimport_files>`{.interpreted-text
role="ref"} or
`scan()<class_EditorFileSystem_method_scan>`{.interpreted-text
role="ref"} while an import is in progress.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_scan}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **scan**()
`🔗<class_EditorFileSystem_method_scan>`{.interpreted-text role="ref"}

Scan the filesystem for changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_scan_sources}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**scan_sources**()
`🔗<class_EditorFileSystem_method_scan_sources>`{.interpreted-text
role="ref"}

Check if the source of any imported resource changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorFileSystem_method_update_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorFileSystem_method_update_file>`{.interpreted-text
role="ref"}

Add a file in an existing directory, or schedule file information to be
updated on editor restart. Can be used to update text files saved by an
external program.

This will not import the file. To reimport, call
`reimport_files()<class_EditorFileSystem_method_reimport_files>`{.interpreted-text
role="ref"} or
`scan()<class_EditorFileSystem_method_scan>`{.interpreted-text
role="ref"} methods.
