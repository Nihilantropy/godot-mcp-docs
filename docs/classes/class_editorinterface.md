github_url
:   hide

# EditorInterface {#class_EditorInterface}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Godot editor\'s interface.

::: rst-class
classref-introduction-group
:::

## Description

**EditorInterface** gives you control over Godot editor\'s window. It
allows customizing the window, saving and (re-)loading scenes, rendering
mesh previews, inspecting and editing resources and objects, and
provides access to
`EditorSettings<class_EditorSettings>`{.interpreted-text role="ref"},
`EditorFileSystem<class_EditorFileSystem>`{.interpreted-text
role="ref"},
`EditorResourcePreview<class_EditorResourcePreview>`{.interpreted-text
role="ref"}, `ScriptEditor<class_ScriptEditor>`{.interpreted-text
role="ref"}, the editor viewport, and information about scenes.

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton directly by its name.

::::: tabs
::: code-tab
gdscript

var editor_settings = EditorInterface.get_editor_settings()
:::

::: code-tab
csharp

// In C# you can access it via the static Singleton property.
EditorSettings settings = EditorInterface.Singleton.GetEditorSettings();
:::
:::::

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

## Property Descriptions

:::: {#class_EditorInterface_property_distraction_free_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**distraction_free_mode**
`🔗<class_EditorInterface_property_distraction_free_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_distraction_free_mode**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_distraction_free_mode_enabled**()

If `true`, enables distraction-free mode which hides side docks to
increase the space available for the main view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_property_movie_maker_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **movie_maker_enabled**
`🔗<class_EditorInterface_property_movie_maker_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_movie_maker_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_movie_maker_enabled**()

If `true`, the Movie Maker mode is enabled in the editor. See
`MovieWriter<class_MovieWriter>`{.interpreted-text role="ref"} for more
information.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorInterface_method_close_scene}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**close_scene**()
`🔗<class_EditorInterface_method_close_scene>`{.interpreted-text
role="ref"}

Closes the currently active scene, discarding any pending changes in the
process. Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success or
`@GlobalScope.ERR_DOES_NOT_EXIST<class_@GlobalScope_constant_ERR_DOES_NOT_EXIST>`{.interpreted-text
role="ref"} if there is no scene to close.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_edit_node}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**edit_node**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_EditorInterface_method_edit_node>`{.interpreted-text
role="ref"}

Edits the given `Node<class_Node>`{.interpreted-text role="ref"}. The
node will be also selected if it\'s inside the scene tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_edit_resource}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**edit_resource**(resource: `Resource<class_Resource>`{.interpreted-text
role="ref"})
`🔗<class_EditorInterface_method_edit_resource>`{.interpreted-text
role="ref"}

Edits the given `Resource<class_Resource>`{.interpreted-text
role="ref"}. If the resource is a
`Script<class_Script>`{.interpreted-text role="ref"} you can also edit
it with
`edit_script()<class_EditorInterface_method_edit_script>`{.interpreted-text
role="ref"} to specify the line and column position.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_edit_script}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**edit_script**(script: `Script<class_Script>`{.interpreted-text
role="ref"}, line: `int<class_int>`{.interpreted-text role="ref"} = -1,
column: `int<class_int>`{.interpreted-text role="ref"} = 0, grab_focus:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`🔗<class_EditorInterface_method_edit_script>`{.interpreted-text
role="ref"}

Edits the given `Script<class_Script>`{.interpreted-text role="ref"}.
The line and column on which to open the script can also be specified.
The script will be open with the user-configured editor for the
script\'s language which may be an external editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_base_control}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**get_base_control**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_base_control>`{.interpreted-text
role="ref"}

Returns the main container of Godot editor\'s window. For example, you
can use it to retrieve the size of the container and place your controls
accordingly.

\*\*Warning:\*\* Removing and freeing this node will render the editor
useless and may cause a crash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_command_palette}
::: rst-class
classref-method
:::
::::

`EditorCommandPalette<class_EditorCommandPalette>`{.interpreted-text
role="ref"} **get_command_palette**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_command_palette>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorCommandPalette<class_EditorCommandPalette>`{.interpreted-text
role="ref"} instance.

\*\*Warning:\*\* Removing and freeing this node will render a part of
the editor useless and may cause a crash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_current_directory}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_current_directory**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_current_directory>`{.interpreted-text
role="ref"}

Returns the current directory being viewed in the
`FileSystemDock<class_FileSystemDock>`{.interpreted-text role="ref"}. If
a file is selected, its base directory will be returned using
`String.get_base_dir()<class_String_method_get_base_dir>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_current_feature_profile}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_current_feature_profile**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_current_feature_profile>`{.interpreted-text
role="ref"}

Returns the name of the currently activated feature profile. If the
default profile is currently active, an empty string is returned
instead.

In order to get a reference to the
`EditorFeatureProfile<class_EditorFeatureProfile>`{.interpreted-text
role="ref"}, you must load the feature profile using
`EditorFeatureProfile.load_from_file()<class_EditorFeatureProfile_method_load_from_file>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Feature profiles created via the user interface are loaded
from the `feature_profiles` directory, as a file with the `.profile`
extension. The editor configuration folder can be found by using
`EditorPaths.get_config_dir()<class_EditorPaths_method_get_config_dir>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_current_path}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_current_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_current_path>`{.interpreted-text
role="ref"}

Returns the current path being viewed in the
`FileSystemDock<class_FileSystemDock>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_edited_scene_root}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**get_edited_scene_root**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_edited_scene_root>`{.interpreted-text
role="ref"}

Returns the edited (current) scene\'s root
`Node<class_Node>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_main_screen}
::: rst-class
classref-method
:::
::::

`VBoxContainer<class_VBoxContainer>`{.interpreted-text role="ref"}
**get_editor_main_screen**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_main_screen>`{.interpreted-text
role="ref"}

Returns the editor control responsible for main screen plugins and
tools. Use it with plugins that implement
`EditorPlugin._has_main_screen()<class_EditorPlugin_private_method__has_main_screen>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This node is a
`VBoxContainer<class_VBoxContainer>`{.interpreted-text role="ref"},
which means that if you add a `Control<class_Control>`{.interpreted-text
role="ref"} child to it, you need to set the child\'s
`Control.size_flags_vertical<class_Control_property_size_flags_vertical>`{.interpreted-text
role="ref"} to
`Control.SIZE_EXPAND_FILL<class_Control_constant_SIZE_EXPAND_FILL>`{.interpreted-text
role="ref"} to make it use the full available space.

\*\*Warning:\*\* Removing and freeing this node will render a part of
the editor useless and may cause a crash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_paths}
::: rst-class
classref-method
:::
::::

`EditorPaths<class_EditorPaths>`{.interpreted-text role="ref"}
**get_editor_paths**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_paths>`{.interpreted-text
role="ref"}

Returns the `EditorPaths<class_EditorPaths>`{.interpreted-text
role="ref"} singleton.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_scale}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_editor_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_scale>`{.interpreted-text
role="ref"}

Returns the actual scale of the editor UI (`1.0` being 100% scale). This
can be used to adjust position and dimensions of the UI added by
plugins.

\*\*Note:\*\* This value is set via the
`EditorSettings.interface/editor/display_scale<class_EditorSettings_property_interface/editor/display_scale>`{.interpreted-text
role="ref"} and
`EditorSettings.interface/editor/custom_display_scale<class_EditorSettings_property_interface/editor/custom_display_scale>`{.interpreted-text
role="ref"} settings. The editor must be restarted for changes to be
properly applied.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_settings}
::: rst-class
classref-method
:::
::::

`EditorSettings<class_EditorSettings>`{.interpreted-text role="ref"}
**get_editor_settings**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_settings>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorSettings<class_EditorSettings>`{.interpreted-text role="ref"}
instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_theme}
::: rst-class
classref-method
:::
::::

`Theme<class_Theme>`{.interpreted-text role="ref"}
**get_editor_theme**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_theme>`{.interpreted-text
role="ref"}

Returns the editor\'s `Theme<class_Theme>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When creating custom editor UI, prefer accessing theme
items directly from your GUI nodes using the `get_theme_*` methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_toaster}
::: rst-class
classref-method
:::
::::

`EditorToaster<class_EditorToaster>`{.interpreted-text role="ref"}
**get_editor_toaster**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_toaster>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorToaster<class_EditorToaster>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_undo_redo}
::: rst-class
classref-method
:::
::::

`EditorUndoRedoManager<class_EditorUndoRedoManager>`{.interpreted-text
role="ref"} **get_editor_undo_redo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_undo_redo>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorUndoRedoManager<class_EditorUndoRedoManager>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_viewport_2d}
::: rst-class
classref-method
:::
::::

`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
**get_editor_viewport_2d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_viewport_2d>`{.interpreted-text
role="ref"}

Returns the 2D editor `SubViewport<class_SubViewport>`{.interpreted-text
role="ref"}. It does not have a camera. Instead, the view transforms are
done directly and can be accessed with
`Viewport.global_canvas_transform<class_Viewport_property_global_canvas_transform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_editor_viewport_3d}
::: rst-class
classref-method
:::
::::

`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
**get_editor_viewport_3d**(idx: `int<class_int>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_editor_viewport_3d>`{.interpreted-text
role="ref"}

Returns the specified 3D editor
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}, from `0`
to `3`. The viewport can be used to access the active editor cameras
with
`Viewport.get_camera_3d()<class_Viewport_method_get_camera_3d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_file_system_dock}
::: rst-class
classref-method
:::
::::

`FileSystemDock<class_FileSystemDock>`{.interpreted-text role="ref"}
**get_file_system_dock**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_file_system_dock>`{.interpreted-text
role="ref"}

Returns the editor\'s
`FileSystemDock<class_FileSystemDock>`{.interpreted-text role="ref"}
instance.

\*\*Warning:\*\* Removing and freeing this node will render a part of
the editor useless and may cause a crash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_inspector}
::: rst-class
classref-method
:::
::::

`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}
**get_inspector**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_inspector>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}
instance.

\*\*Warning:\*\* Removing and freeing this node will render a part of
the editor useless and may cause a crash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_open_scene_roots}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node<class_Node>`{.interpreted-text role="ref"}\]
**get_open_scene_roots**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_open_scene_roots>`{.interpreted-text
role="ref"}

Returns an array with references to the root nodes of the currently
opened scenes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_open_scenes}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_open_scenes**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_open_scenes>`{.interpreted-text
role="ref"}

Returns an array with the file paths of the currently opened scenes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_playing_scene}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_playing_scene**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_playing_scene>`{.interpreted-text
role="ref"}

Returns the name of the scene that is being played. If no scene is
currently being played, returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_resource_filesystem}
::: rst-class
classref-method
:::
::::

`EditorFileSystem<class_EditorFileSystem>`{.interpreted-text role="ref"}
**get_resource_filesystem**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_resource_filesystem>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorFileSystem<class_EditorFileSystem>`{.interpreted-text role="ref"}
instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_resource_previewer}
::: rst-class
classref-method
:::
::::

`EditorResourcePreview<class_EditorResourcePreview>`{.interpreted-text
role="ref"} **get_resource_previewer**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_resource_previewer>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorResourcePreview<class_EditorResourcePreview>`{.interpreted-text
role="ref"} instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_script_editor}
::: rst-class
classref-method
:::
::::

`ScriptEditor<class_ScriptEditor>`{.interpreted-text role="ref"}
**get_script_editor**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_script_editor>`{.interpreted-text
role="ref"}

Returns the editor\'s
`ScriptEditor<class_ScriptEditor>`{.interpreted-text role="ref"}
instance.

\*\*Warning:\*\* Removing and freeing this node will render a part of
the editor useless and may cause a crash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_selected_paths}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_selected_paths**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_selected_paths>`{.interpreted-text
role="ref"}

Returns an array containing the paths of the currently selected files
(and directories) in the
`FileSystemDock<class_FileSystemDock>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_get_selection}
::: rst-class
classref-method
:::
::::

`EditorSelection<class_EditorSelection>`{.interpreted-text role="ref"}
**get_selection**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_get_selection>`{.interpreted-text
role="ref"}

Returns the editor\'s
`EditorSelection<class_EditorSelection>`{.interpreted-text role="ref"}
instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_inspect_object}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**inspect_object**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, for_property: `String<class_String>`{.interpreted-text
role="ref"} = \"\", inspector_only: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_EditorInterface_method_inspect_object>`{.interpreted-text
role="ref"}

Shows the given property on the given `object` in the editor\'s
Inspector dock. If `inspector_only` is `true`, plugins will not attempt
to edit `object`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_is_multi_window_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_multi_window_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_is_multi_window_enabled>`{.interpreted-text
role="ref"}

Returns `true` if multiple window support is enabled in the editor.
Multiple window support is enabled if *all* of these statements are
true:

- `EditorSettings.interface/multi_window/enable<class_EditorSettings_property_interface/multi_window/enable>`{.interpreted-text
  role="ref"} is `true`.
- `EditorSettings.interface/editor/single_window_mode<class_EditorSettings_property_interface/editor/single_window_mode>`{.interpreted-text
  role="ref"} is `false`.
- `Viewport.gui_embed_subwindows<class_Viewport_property_gui_embed_subwindows>`{.interpreted-text
  role="ref"} is `false`. This is forced to `true` on platforms that
  don\'t support multiple windows such as Web, or when the
  `--single-window`
  `command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
  role="doc"} is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_is_playing_scene}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_playing_scene**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_is_playing_scene>`{.interpreted-text
role="ref"}

Returns `true` if a scene is currently being played, `false` otherwise.
Paused scenes are considered as being played.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_is_plugin_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_plugin_enabled**(plugin: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorInterface_method_is_plugin_enabled>`{.interpreted-text
role="ref"}

Returns `true` if the specified `plugin` is enabled. The plugin name is
the same as its directory name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_make_mesh_previews}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}\] **make_mesh_previews**(meshes:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`Mesh<class_Mesh>`{.interpreted-text role="ref"}\],
preview_size: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_EditorInterface_method_make_mesh_previews>`{.interpreted-text
role="ref"}

Returns mesh previews rendered at the given size as an
`Array<class_Array>`{.interpreted-text role="ref"} of
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_mark_scene_as_unsaved}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mark_scene_as_unsaved**()
`🔗<class_EditorInterface_method_mark_scene_as_unsaved>`{.interpreted-text
role="ref"}

Marks the current scene tab as unsaved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_open_scene_from_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**open_scene_from_path**(scene_filepath:
`String<class_String>`{.interpreted-text role="ref"}, set_inherited:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_EditorInterface_method_open_scene_from_path>`{.interpreted-text
role="ref"}

Opens the scene at the given path. If `set_inherited` is `true`, creates
a new inherited scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_play_current_scene}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_current_scene**()
`🔗<class_EditorInterface_method_play_current_scene>`{.interpreted-text
role="ref"}

Plays the currently active scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_play_custom_scene}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_custom_scene**(scene_filepath:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorInterface_method_play_custom_scene>`{.interpreted-text
role="ref"}

Plays the scene specified by its filepath.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_play_main_scene}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_main_scene**()
`🔗<class_EditorInterface_method_play_main_scene>`{.interpreted-text
role="ref"}

Plays the main scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_create_dialog}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_create_dialog**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, base_type:
`StringName<class_StringName>`{.interpreted-text role="ref"} = \"\",
current_type: `String<class_String>`{.interpreted-text role="ref"} =
\"\", dialog_title: `String<class_String>`{.interpreted-text role="ref"}
= \"\", type_blocklist: `Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_EditorInterface_method_popup_create_dialog>`{.interpreted-text
role="ref"}

**Experimental:** This method may be changed or removed in future
versions.

Pops up an editor dialog for creating an object.

The `callback` must take a single argument of type
`StringName<class_StringName>`{.interpreted-text role="ref"} which will
contain the type name of the selected object or be empty if no item is
selected.

The `base_type` specifies the base type of objects to display. For
example, if you set this to \"Resource\", all types derived from
`Resource<class_Resource>`{.interpreted-text role="ref"} will display in
the create dialog.

The `current_type` will be passed in the search box of the create
dialog, and the specified type can be immediately selected when the
dialog pops up. If the `current_type` is not derived from `base_type`,
there will be no result of the type in the dialog.

The `dialog_title` allows you to define a custom title for the dialog.
This is useful if you want to accurately hint the usage of the dialog.
If the `dialog_title` is an empty string, the dialog will use \"Create
New \'Base Type\'\" as the default title.

The `type_blocklist` contains a list of type names, and the types in the
blocklist will be hidden from the create dialog.

\*\*Note:\*\* Trying to list the base type in the `type_blocklist` will
hide all types derived from the base type from the create dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_dialog}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_dialog**(dialog: `Window<class_Window>`{.interpreted-text
role="ref"}, rect: `Rect2i<class_Rect2i>`{.interpreted-text role="ref"}
= Rect2i(0, 0, 0, 0))
`🔗<class_EditorInterface_method_popup_dialog>`{.interpreted-text
role="ref"}

Pops up the `dialog` in the editor UI with
`Window.popup_exclusive()<class_Window_method_popup_exclusive>`{.interpreted-text
role="ref"}. The dialog must have no current parent, otherwise the
method fails.

See also
`Window.set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_dialog_centered}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_dialog_centered**(dialog:
`Window<class_Window>`{.interpreted-text role="ref"}, minsize:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(0,
0))
`🔗<class_EditorInterface_method_popup_dialog_centered>`{.interpreted-text
role="ref"}

Pops up the `dialog` in the editor UI with
`Window.popup_exclusive_centered()<class_Window_method_popup_exclusive_centered>`{.interpreted-text
role="ref"}. The dialog must have no current parent, otherwise the
method fails.

See also
`Window.set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_dialog_centered_clamped}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_dialog_centered_clamped**(dialog:
`Window<class_Window>`{.interpreted-text role="ref"}, minsize:
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} = Vector2i(0,
0), fallback_ratio: `float<class_float>`{.interpreted-text role="ref"} =
0.75)
`🔗<class_EditorInterface_method_popup_dialog_centered_clamped>`{.interpreted-text
role="ref"}

Pops up the `dialog` in the editor UI with
`Window.popup_exclusive_centered_clamped()<class_Window_method_popup_exclusive_centered_clamped>`{.interpreted-text
role="ref"}. The dialog must have no current parent, otherwise the
method fails.

See also
`Window.set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_dialog_centered_ratio}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_dialog_centered_ratio**(dialog:
`Window<class_Window>`{.interpreted-text role="ref"}, ratio:
`float<class_float>`{.interpreted-text role="ref"} = 0.8)
`🔗<class_EditorInterface_method_popup_dialog_centered_ratio>`{.interpreted-text
role="ref"}

Pops up the `dialog` in the editor UI with
`Window.popup_exclusive_centered_ratio()<class_Window_method_popup_exclusive_centered_ratio>`{.interpreted-text
role="ref"}. The dialog must have no current parent, otherwise the
method fails.

See also
`Window.set_unparent_when_invisible()<class_Window_method_set_unparent_when_invisible>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_method_selector}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_method_selector**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, current_value:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_EditorInterface_method_popup_method_selector>`{.interpreted-text
role="ref"}

Pops up an editor dialog for selecting a method from `object`. The
`callback` must take a single argument of type
`String<class_String>`{.interpreted-text role="ref"} which will contain
the name of the selected method or be empty if the dialog is canceled.
If `current_value` is provided, the method will be selected
automatically in the method list, if it exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_node_selector}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_node_selector**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, valid_types:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] = \[\], current_value:
`Node<class_Node>`{.interpreted-text role="ref"} = null)
`🔗<class_EditorInterface_method_popup_node_selector>`{.interpreted-text
role="ref"}

Pops up an editor dialog for selecting a
`Node<class_Node>`{.interpreted-text role="ref"} from the edited scene.
The `callback` must take a single argument of type
`NodePath<class_NodePath>`{.interpreted-text role="ref"}. It is called
on the selected `NodePath<class_NodePath>`{.interpreted-text role="ref"}
or the empty path `^""` if the dialog is canceled. If `valid_types` is
provided, the dialog will only show Nodes that match one of the listed
Node types. If `current_value` is provided, the Node will be
automatically selected in the tree, if it exists.

\*\*Example:\*\* Display the node selection dialog as soon as this node
is added to the tree for the first time:

    func _ready():
        if Engine.is_editor_hint():
            EditorInterface.popup_node_selector(_on_node_selected, ["Button"])

    func _on_node_selected(node_path):
        if node_path.is_empty():
            print("node selection canceled")
        else:
            print("selected ", node_path)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_property_selector}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_property_selector**(object:
`Object<class_Object>`{.interpreted-text role="ref"}, callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, type_filter:
`PackedInt32Array<class_PackedInt32Array>`{.interpreted-text role="ref"}
= PackedInt32Array(), current_value:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_EditorInterface_method_popup_property_selector>`{.interpreted-text
role="ref"}

Pops up an editor dialog for selecting properties from `object`. The
`callback` must take a single argument of type
`NodePath<class_NodePath>`{.interpreted-text role="ref"}. It is called
on the selected property path (see
`NodePath.get_as_property_path()<class_NodePath_method_get_as_property_path>`{.interpreted-text
role="ref"}) or the empty path `^""` if the dialog is canceled. If
`type_filter` is provided, the dialog will only show properties that
match one of the listed
`Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
role="ref"} values. If `current_value` is provided, the property will be
selected automatically in the property list, if it exists.

    func _ready():
        if Engine.is_editor_hint():
            EditorInterface.popup_property_selector(this, _on_property_selected, [TYPE_INT])

    func _on_property_selected(property_path):
        if property_path.is_empty():
            print("property selection canceled")
        else:
            print("selected ", property_path)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_popup_quick_open}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**popup_quick_open**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"}, base_types:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] = \[\])
`🔗<class_EditorInterface_method_popup_quick_open>`{.interpreted-text
role="ref"}

Pops up an editor dialog for quick selecting a resource file. The
`callback` must take a single argument of type
`String<class_String>`{.interpreted-text role="ref"} which will contain
the path of the selected resource or be empty if the dialog is canceled.
If `base_types` is provided, the dialog will only show resources that
match these types. Only types deriving from
`Resource<class_Resource>`{.interpreted-text role="ref"} are supported.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_reload_scene_from_path}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reload_scene_from_path**(scene_filepath:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorInterface_method_reload_scene_from_path>`{.interpreted-text
role="ref"}

Reloads the scene at the given path.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_restart_editor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**restart_editor**(save: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_EditorInterface_method_restart_editor>`{.interpreted-text
role="ref"}

Restarts the editor. This closes the editor and then opens the same
project. If `save` is `true`, the project will be saved before
restarting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_save_all_scenes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**save_all_scenes**()
`🔗<class_EditorInterface_method_save_all_scenes>`{.interpreted-text
role="ref"}

Saves all opened scenes in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_save_scene}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**save_scene**()
`🔗<class_EditorInterface_method_save_scene>`{.interpreted-text
role="ref"}

Saves the currently active scene. Returns either
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} or
`@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_save_scene_as}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**save_scene_as**(path: `String<class_String>`{.interpreted-text
role="ref"}, with_preview: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_EditorInterface_method_save_scene_as>`{.interpreted-text
role="ref"}

Saves the currently active scene as a file at `path`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_select_file}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**select_file**(file: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorInterface_method_select_file>`{.interpreted-text
role="ref"}

Selects the file, with the path provided by `file`, in the FileSystem
dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_set_current_feature_profile}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_current_feature_profile**(profile_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorInterface_method_set_current_feature_profile>`{.interpreted-text
role="ref"}

Selects and activates the specified feature profile with the given
`profile_name`. Set `profile_name` to an empty string to reset to the
default feature profile.

A feature profile can be created programmatically using the
`EditorFeatureProfile<class_EditorFeatureProfile>`{.interpreted-text
role="ref"} class.

\*\*Note:\*\* The feature profile that gets activated must be located in
the `feature_profiles` directory, as a file with the `.profile`
extension. If a profile could not be found, an error occurs. The editor
configuration folder can be found by using
`EditorPaths.get_config_dir()<class_EditorPaths_method_get_config_dir>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_set_main_screen_editor}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_main_screen_editor**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorInterface_method_set_main_screen_editor>`{.interpreted-text
role="ref"}

Sets the editor\'s current main screen to the one specified in `name`.
`name` must match the title of the tab in question exactly (e.g. `2D`,
`3D`, `Script`, `Game`, or `AssetLib` for default tabs).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_set_plugin_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_plugin_enabled**(plugin: `String<class_String>`{.interpreted-text
role="ref"}, enabled: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorInterface_method_set_plugin_enabled>`{.interpreted-text
role="ref"}

Sets the enabled status of a plugin. The plugin name is the same as its
directory name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorInterface_method_stop_playing_scene}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**stop_playing_scene**()
`🔗<class_EditorInterface_method_stop_playing_scene>`{.interpreted-text
role="ref"}

Stops the scene that is currently playing.
