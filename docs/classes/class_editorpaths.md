github_url
:   hide

# EditorPaths {#class_EditorPaths}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Editor-only singleton that returns paths to various OS-specific data
folders and files.

::: rst-class
classref-introduction-group
:::

## Description

This editor-only singleton returns OS-specific paths to various data
folders and files. It can be used in editor plugins to ensure files are
saved in the correct location on each operating system.

\*\*Note:\*\* This singleton is not accessible in exported projects.
Attempting to access it in an exported project will result in a script
error as the singleton won\'t be declared. To prevent script errors in
exported projects, use
`Engine.has_singleton()<class_Engine_method_has_singleton>`{.interpreted-text
role="ref"} to check whether the singleton is available before using it.

\*\*Note:\*\* On the Linux/BSD platform, Godot complies with the [XDG
Base Directory
Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).
You can override environment variables following the specification to
change the editor and project data paths.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `File paths in Godot projects <../tutorials/io/data_paths>`{.interpreted-text
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

## Method Descriptions

:::: {#class_EditorPaths_method_get_cache_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_cache_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPaths_method_get_cache_dir>`{.interpreted-text
role="ref"}

Returns the absolute path to the user\'s cache folder. This folder
should be used for temporary data that can be removed safely whenever
the editor is closed (such as generated resource thumbnails).

\*\*Default paths per platform:\*\*

``` text
- Windows: %LOCALAPPDATA%\Godot\
- macOS: ~/Library/Caches/Godot/
- Linux: ~/.cache/godot/
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPaths_method_get_config_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_config_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPaths_method_get_config_dir>`{.interpreted-text
role="ref"}

Returns the absolute path to the user\'s configuration folder. This
folder should be used for *persistent* user configuration files.

\*\*Default paths per platform:\*\*

``` text
- Windows: %APPDATA%\Godot\                    (same as `get_data_dir()`)
- macOS: ~/Library/Application Support/Godot/  (same as `get_data_dir()`)
- Linux: ~/.config/godot/
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPaths_method_get_data_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_data_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPaths_method_get_data_dir>`{.interpreted-text
role="ref"}

Returns the absolute path to the user\'s data folder. This folder should
be used for *persistent* user data files such as installed export
templates.

\*\*Default paths per platform:\*\*

``` text
- Windows: %APPDATA%\Godot\                    (same as `get_config_dir()`)
- macOS: ~/Library/Application Support/Godot/  (same as `get_config_dir()`)
- Linux: ~/.local/share/godot/
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPaths_method_get_project_settings_dir}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_project_settings_dir**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPaths_method_get_project_settings_dir>`{.interpreted-text
role="ref"}

Returns the project-specific editor settings path. Projects all have a
unique subdirectory inside the settings path where project-specific
editor settings are saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPaths_method_get_self_contained_file}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_self_contained_file**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPaths_method_get_self_contained_file>`{.interpreted-text
role="ref"}

Returns the absolute path to the self-contained file that makes the
current Godot editor instance be considered as self-contained. Returns
an empty string if the current Godot editor instance isn\'t
self-contained. See also
`is_self_contained()<class_EditorPaths_method_is_self_contained>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPaths_method_is_self_contained}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_self_contained**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPaths_method_is_self_contained>`{.interpreted-text
role="ref"}

Returns `true` if the editor is marked as self-contained, `false`
otherwise. When self-contained mode is enabled, user configuration, data
and cache files are saved in an `editor_data/` folder next to the editor
binary. This makes portable usage easier and ensures the Godot editor
minimizes file writes outside its own folder. Self-contained mode is not
available for exported projects.

Self-contained mode can be enabled by creating a file named `._sc_` or
`_sc_` in the same folder as the editor binary or macOS .app bundle
while the editor is not running. See also
`get_self_contained_file()<class_EditorPaths_method_get_self_contained_file>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* On macOS, quarantine flag should be manually removed
before using self-contained mode, see [Running on
macOS](https://docs.godotengine.org/en/stable/tutorials/export/running_on_macos.html).

\*\*Note:\*\* On macOS, placing `_sc_` or any other file inside .app
bundle will break digital signature and make it non-portable, consider
placing it in the same folder as the .app bundle instead.

\*\*Note:\*\* The Steam release of Godot uses self-contained mode by
default.
