github_url
:   hide

# EditorSettings {#class_EditorSettings}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Object that holds the project-independent editor settings.

::: rst-class
classref-introduction-group
:::

## Description

Object that holds the project-independent editor settings. These
settings are generally visible in the **Editor \> Editor Settings**
menu.

Property names use slash delimiters to distinguish sections. Setting
values can be of any `Variant<class_Variant>`{.interpreted-text
role="ref"} type. It\'s recommended to use `snake_case` for editor
settings to be consistent with the Godot editor itself.

Accessing the settings can be done using the following methods, such as:

::::: tabs
::: code-tab
gdscript

var settings = EditorInterface.get_editor_settings() \#
[settings.set(\"some/property\", 10)]{.title-ref} also works as this
class overrides [\_set()]{.title-ref} internally.
settings.set_setting(\"some/property\", 10) \#
[settings.get(\"some/property\")]{.title-ref} also works as this class
overrides [\_get()]{.title-ref} internally.
settings.get_setting(\"some/property\") var list_of_settings =
settings.get_property_list()
:::

::: code-tab
csharp

EditorSettings settings = EditorInterface.Singleton.GetEditorSettings();
// [settings.set(\"some/property\", value)]{.title-ref} also works as
this class overrides [\_set()]{.title-ref} internally.
settings.SetSetting(\"some/property\", Value); //
[settings.get(\"some/property\", value)]{.title-ref} also works as this
class overrides [\_get()]{.title-ref} internally.
settings.GetSetting(\"some/property\");
Godot.Collections.Array\<Godot.Collections.Dictionary\> listOfSettings =
settings.GetPropertyList();
:::
:::::

\*\*Note:\*\* This class shouldn\'t be instantiated directly. Instead,
access the singleton using
`EditorInterface.get_editor_settings()<class_EditorInterface_method_get_editor_settings>`{.interpreted-text
role="ref"}.

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

:::: {#class_EditorSettings_signal_settings_changed}
::: rst-class
classref-signal
:::
::::

**settings_changed**()
`🔗<class_EditorSettings_signal_settings_changed>`{.interpreted-text
role="ref"}

Emitted after any editor setting has changed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_EditorSettings_constant_NOTIFICATION_EDITOR_SETTINGS_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_EDITOR_SETTINGS_CHANGED** = `10000`
`🔗<class_EditorSettings_constant_NOTIFICATION_EDITOR_SETTINGS_CHANGED>`{.interpreted-text
role="ref"}

Emitted after any editor setting has changed. It\'s used by various
editor plugins to update their visuals on theme changes or logic on
configuration changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_EditorSettings_property_asset_library/use_threads}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**asset_library/use_threads**
`🔗<class_EditorSettings_property_asset_library/use_threads>`{.interpreted-text
role="ref"}

If `true`, the Asset Library uses multiple threads for its HTTP
requests. This prevents the Asset Library from blocking the main thread
for every loaded asset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/auto_switch_to_remote_scene_tree}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debugger/auto_switch_to_remote_scene_tree**
`🔗<class_EditorSettings_property_debugger/auto_switch_to_remote_scene_tree>`{.interpreted-text
role="ref"}

If `true`, automatically switches to the **Remote** scene tree when
running the project from the editor. If `false`, stays on the **Local**
scene tree when running the project from the editor.

\*\*Warning:\*\* Enabling this setting can cause stuttering when running
a project with a large amount of nodes (typically a few thousands of
nodes or more), even if the editor window isn\'t focused. This is due to
the remote scene tree being updated every second regardless of whether
the editor is focused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/auto_switch_to_stack_trace}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debugger/auto_switch_to_stack_trace**
`🔗<class_EditorSettings_property_debugger/auto_switch_to_stack_trace>`{.interpreted-text
role="ref"}

If `true`, automatically switches to the **Stack Trace** panel when the
debugger hits a breakpoint or steps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/max_node_selection}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debugger/max_node_selection**
`🔗<class_EditorSettings_property_debugger/max_node_selection>`{.interpreted-text
role="ref"}

The limit of how many remote nodes can be selected at once.

\*\*Warning:\*\* Increasing this value is not recommended, as selecting
too many can make the editing and inspection of remote properties
unreliable.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/profile_native_calls}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debugger/profile_native_calls**
`🔗<class_EditorSettings_property_debugger/profile_native_calls>`{.interpreted-text
role="ref"}

If `true`, enables collection of profiling data from non-GDScript Godot
functions, such as engine class methods. Enabling this slows execution
while profiling further.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/profiler_frame_history_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debugger/profiler_frame_history_size**
`🔗<class_EditorSettings_property_debugger/profiler_frame_history_size>`{.interpreted-text
role="ref"}

The size of the profiler\'s frame history. The default value (3600)
allows seeing up to 60 seconds of profiling if the project renders at a
constant 60 FPS. Higher values allow viewing longer periods of profiling
in the graphs, especially when the project is running at high
framerates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/profiler_frame_max_functions}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debugger/profiler_frame_max_functions**
`🔗<class_EditorSettings_property_debugger/profiler_frame_max_functions>`{.interpreted-text
role="ref"}

The maximum number of script functions that can be displayed per frame
in the profiler. If there are more script functions called in a given
profiler frame, these functions will be discarded from the profiling
results entirely.

\*\*Note:\*\* This setting is only read when the profiler is first
started, so changing it during profiling will have no effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/profiler_target_fps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**debugger/profiler_target_fps**
`🔗<class_EditorSettings_property_debugger/profiler_target_fps>`{.interpreted-text
role="ref"}

The target frame rate shown in the visual profiler graph, in frames per
second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/remote_inspect_refresh_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**debugger/remote_inspect_refresh_interval**
`🔗<class_EditorSettings_property_debugger/remote_inspect_refresh_interval>`{.interpreted-text
role="ref"}

The refresh interval for the remote inspector\'s properties (in
seconds). Lower values are more reactive, but may cause stuttering while
the project is running from the editor and the **Remote** scene tree is
selected in the Scene tree dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_debugger/remote_scene_tree_refresh_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**debugger/remote_scene_tree_refresh_interval**
`🔗<class_EditorSettings_property_debugger/remote_scene_tree_refresh_interval>`{.interpreted-text
role="ref"}

The refresh interval for the remote scene tree (in seconds). Lower
values are more reactive, but may cause stuttering while the project is
running from the editor and the **Remote** scene tree is selected in the
Scene tree dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/filesystem/always_show_folders}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/filesystem/always_show_folders**
`🔗<class_EditorSettings_property_docks/filesystem/always_show_folders>`{.interpreted-text
role="ref"}

If `true`, displays folders in the FileSystem dock\'s bottom pane when
split mode is enabled. If `false`, only files will be displayed in the
bottom pane. Split mode can be toggled by pressing the icon next to the
`res://` folder path.

\*\*Note:\*\* This setting has no effect when split mode is disabled
(which is the default).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/filesystem/other_file_extensions}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**docks/filesystem/other_file_extensions**
`🔗<class_EditorSettings_property_docks/filesystem/other_file_extensions>`{.interpreted-text
role="ref"}

A comma separated list of unsupported file extensions to show in the
FileSystem dock, e.g. `"ico,icns"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/filesystem/textfile_extensions}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**docks/filesystem/textfile_extensions**
`🔗<class_EditorSettings_property_docks/filesystem/textfile_extensions>`{.interpreted-text
role="ref"}

A comma separated list of file extensions to consider as editable text
files in the FileSystem dock (by double-clicking on the files), e.g.
`"txt,md,cfg,ini,log,json,yml,yaml,toml,xml"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/filesystem/thumbnail_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**docks/filesystem/thumbnail_size**
`🔗<class_EditorSettings_property_docks/filesystem/thumbnail_size>`{.interpreted-text
role="ref"}

The thumbnail size to use in the FileSystem dock (in pixels). See also
`filesystem/file_dialog/thumbnail_size<class_EditorSettings_property_filesystem/file_dialog/thumbnail_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/property_editor/auto_refresh_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**docks/property_editor/auto_refresh_interval**
`🔗<class_EditorSettings_property_docks/property_editor/auto_refresh_interval>`{.interpreted-text
role="ref"}

The refresh interval to use for the Inspector dock\'s properties. The
effect of this setting is mainly noticeable when adjusting gizmos in the
2D/3D editor and looking at the inspector at the same time. Lower values
make the inspector refresh more often, but take up more CPU time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/property_editor/subresource_hue_tint}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**docks/property_editor/subresource_hue_tint**
`🔗<class_EditorSettings_property_docks/property_editor/subresource_hue_tint>`{.interpreted-text
role="ref"}

The tint intensity to use for the subresources background in the
Inspector dock. The tint is used to distinguish between different
subresources in the inspector. Higher values result in a more noticeable
background color difference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/scene_tree/accessibility_warnings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/scene_tree/accessibility_warnings**
`🔗<class_EditorSettings_property_docks/scene_tree/accessibility_warnings>`{.interpreted-text
role="ref"}

If `true`, accessibility related warnings are displayed alongside other
configuration warnings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/scene_tree/ask_before_deleting_related_animation_tracks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/scene_tree/ask_before_deleting_related_animation_tracks**
`🔗<class_EditorSettings_property_docks/scene_tree/ask_before_deleting_related_animation_tracks>`{.interpreted-text
role="ref"}

If `true`, when a node is deleted with animation tracks referencing it,
a confirmation dialog appears before the tracks are deleted. The dialog
will appear even when using the \"Delete (No Confirm)\" shortcut.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/scene_tree/ask_before_revoking_unique_name}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/scene_tree/ask_before_revoking_unique_name**
`🔗<class_EditorSettings_property_docks/scene_tree/ask_before_revoking_unique_name>`{.interpreted-text
role="ref"}

If `true`, displays a confirmation dialog after left-clicking the
\"percent\" icon next to a node name in the Scene tree dock. When
clicked, this icon revokes the node\'s scene-unique name, which can
impact the behavior of scripts that rely on this scene-unique name due
to identifiers not being found anymore.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/scene_tree/auto_expand_to_selected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/scene_tree/auto_expand_to_selected**
`🔗<class_EditorSettings_property_docks/scene_tree/auto_expand_to_selected>`{.interpreted-text
role="ref"}

If `true`, the scene tree dock will automatically unfold nodes when a
node that has folded parents is selected.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/scene_tree/center_node_on_reparent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/scene_tree/center_node_on_reparent**
`🔗<class_EditorSettings_property_docks/scene_tree/center_node_on_reparent>`{.interpreted-text
role="ref"}

If `true`, new node created when reparenting node(s) will be positioned
at the average position of the selected node(s).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/scene_tree/hide_filtered_out_parents}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/scene_tree/hide_filtered_out_parents**
`🔗<class_EditorSettings_property_docks/scene_tree/hide_filtered_out_parents>`{.interpreted-text
role="ref"}

If `true`, the scene tree dock will only show nodes that match the
filter, without showing parents that don\'t. This settings can also be
changed in the Scene dock\'s top menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_docks/scene_tree/start_create_dialog_fully_expanded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**docks/scene_tree/start_create_dialog_fully_expanded**
`🔗<class_EditorSettings_property_docks/scene_tree/start_create_dialog_fully_expanded>`{.interpreted-text
role="ref"}

If `true`, the Create dialog (Create New Node/Create New Resource) will
start with all its sections expanded. Otherwise, sections will be
collapsed until the user starts searching (which will automatically
expand sections as needed).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/bone_color1}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/bone_color1**
`🔗<class_EditorSettings_property_editors/2d/bone_color1>`{.interpreted-text
role="ref"}

The \"start\" stop of the color gradient to use for bones in the 2D
skeleton editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/bone_color2}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/bone_color2**
`🔗<class_EditorSettings_property_editors/2d/bone_color2>`{.interpreted-text
role="ref"}

The \"end\" stop of the color gradient to use for bones in the 2D
skeleton editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/bone_ik_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/bone_ik_color**
`🔗<class_EditorSettings_property_editors/2d/bone_ik_color>`{.interpreted-text
role="ref"}

The color to use for inverse kinematics-enabled bones in the 2D skeleton
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/bone_outline_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/bone_outline_color**
`🔗<class_EditorSettings_property_editors/2d/bone_outline_color>`{.interpreted-text
role="ref"}

The outline color to use for non-selected bones in the 2D skeleton
editor. See also
`editors/2d/bone_selected_color<class_EditorSettings_property_editors/2d/bone_selected_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/bone_outline_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/2d/bone_outline_size**
`🔗<class_EditorSettings_property_editors/2d/bone_outline_size>`{.interpreted-text
role="ref"}

The outline size in the 2D skeleton editor (in pixels). See also
`editors/2d/bone_width<class_EditorSettings_property_editors/2d/bone_width>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Changes to this value only apply after modifying a
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node in any way, or
closing and reopening the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/bone_selected_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/bone_selected_color**
`🔗<class_EditorSettings_property_editors/2d/bone_selected_color>`{.interpreted-text
role="ref"}

The color to use for selected bones in the 2D skeleton editor. See also
`editors/2d/bone_outline_color<class_EditorSettings_property_editors/2d/bone_outline_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/bone_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/2d/bone_width**
`🔗<class_EditorSettings_property_editors/2d/bone_width>`{.interpreted-text
role="ref"}

The bone width in the 2D skeleton editor (in pixels). See also
`editors/2d/bone_outline_size<class_EditorSettings_property_editors/2d/bone_outline_size>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Changes to this value only apply after modifying a
`Bone2D<class_Bone2D>`{.interpreted-text role="ref"} node in any way, or
closing and reopening the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/grid_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/grid_color**
`🔗<class_EditorSettings_property_editors/2d/grid_color>`{.interpreted-text
role="ref"}

The grid color to use in the 2D editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/guides_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/guides_color**
`🔗<class_EditorSettings_property_editors/2d/guides_color>`{.interpreted-text
role="ref"}

The guides color to use in the 2D editor. Guides can be created by
dragging the mouse cursor from the rulers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/ruler_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/2d/ruler_width**
`🔗<class_EditorSettings_property_editors/2d/ruler_width>`{.interpreted-text
role="ref"}

The thickness of the coordinate ruler in the 2D editor. Increasing this
will also increase the size of the ruler font, improving readability
when using a lower editor scale. The editor may force a minimum size to
keep the ruler numbers legible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/smart_snapping_line_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/smart_snapping_line_color**
`🔗<class_EditorSettings_property_editors/2d/smart_snapping_line_color>`{.interpreted-text
role="ref"}

The color to use when drawing smart snapping lines in the 2D editor. The
smart snapping lines will automatically display when moving 2D nodes if
smart snapping is enabled in the Snapping Options menu at the top of the
2D editor viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/use_integer_zoom_by_default}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/2d/use_integer_zoom_by_default**
`🔗<class_EditorSettings_property_editors/2d/use_integer_zoom_by_default>`{.interpreted-text
role="ref"}

If `true`, the 2D editor will snap to integer zoom values when not
holding the `Alt`{.interpreted-text role="kbd"} key. If `false`, this
behavior is swapped.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/viewport_border_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/2d/viewport_border_color**
`🔗<class_EditorSettings_property_editors/2d/viewport_border_color>`{.interpreted-text
role="ref"}

The color of the viewport border in the 2D editor. This border
represents the viewport\'s size at the base resolution defined in the
Project Settings. Objects placed outside this border will not be visible
unless a `Camera2D<class_Camera2D>`{.interpreted-text role="ref"} node
is used, or unless the window is resized and the stretch mode is set to
`disabled`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/2d/zoom_speed_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/2d/zoom_speed_factor**
`🔗<class_EditorSettings_property_editors/2d/zoom_speed_factor>`{.interpreted-text
role="ref"}

The factor to use when zooming in or out in the 2D editor. For example,
`1.1` will zoom in by 10% with every step. If set to `2.0`, zooming will
only cycle through powers of two.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/active_selection_box_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d/active_selection_box_color**
`🔗<class_EditorSettings_property_editors/3d/active_selection_box_color>`{.interpreted-text
role="ref"}

The color to use for the active selection box that surrounds selected
nodes in the 3D editor viewport. The color\'s alpha channel influences
the selection box\'s opacity.

\*\*Note:\*\* The term \"active\" indicates that this object is the
primary selection used as the basis for certain operations. This is the
last selected `Node3D<class_Node3D>`{.interpreted-text role="ref"},
which can be reordered with
`Shift + Left mouse button`{.interpreted-text role="kbd"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/default_fov}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/default_fov**
`🔗<class_EditorSettings_property_editors/3d/default_fov>`{.interpreted-text
role="ref"}

The default camera vertical field of view to use in the 3D editor (in
degrees). The camera field of view can be adjusted on a per-scene basis
using the **View** menu at the top of the 3D editor. If a scene had its
camera field of view adjusted using the **View** menu, this setting is
ignored in the scene in question. This setting is also ignored while a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} node is being
previewed in the editor.

\*\*Note:\*\* The editor camera always uses the **Keep Height** aspect
mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/default_z_far}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/default_z_far**
`🔗<class_EditorSettings_property_editors/3d/default_z_far>`{.interpreted-text
role="ref"}

The default camera far clip distance to use in the 3D editor (in
degrees). Higher values make it possible to view objects placed further
away from the camera, at the cost of lower precision in the depth buffer
(which can result in visible Z-fighting in the distance). The camera far
clip distance can be adjusted on a per-scene basis using the **View**
menu at the top of the 3D editor. If a scene had its camera far clip
distance adjusted using the **View** menu, this setting is ignored in
the scene in question. This setting is also ignored while a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} node is being
previewed in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/default_z_near}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/default_z_near**
`🔗<class_EditorSettings_property_editors/3d/default_z_near>`{.interpreted-text
role="ref"}

The default camera near clip distance to use in the 3D editor (in
degrees). Lower values make it possible to view objects placed closer to
the camera, at the cost of lower precision in the depth buffer (which
can result in visible Z-fighting in the distance). The camera near clip
distance can be adjusted on a per-scene basis using the **View** menu at
the top of the 3D editor. If a scene had its camera near clip distance
adjusted using the **View** menu, this setting is ignored in the scene
in question. This setting is also ignored while a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} node is being
previewed in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/freelook/freelook_activation_modifier}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/freelook/freelook_activation_modifier**
`🔗<class_EditorSettings_property_editors/3d/freelook/freelook_activation_modifier>`{.interpreted-text
role="ref"}

The modifier key to use to enable freelook in the 3D editor (on top of
pressing the right mouse button).

\*\*Note:\*\* Regardless of this setting, the freelook toggle keyboard
shortcut (`Shift + F`{.interpreted-text role="kbd"} by default) is
always available.

\*\*Note:\*\* On certain window managers on Linux, the
`Alt`{.interpreted-text role="kbd"} key will be intercepted by the
window manager when clicking a mouse button at the same time. This means
Godot will not see the modifier key as being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/freelook/freelook_base_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/freelook/freelook_base_speed**
`🔗<class_EditorSettings_property_editors/3d/freelook/freelook_base_speed>`{.interpreted-text
role="ref"}

The base 3D freelook speed in units per second. This can be adjusted by
using the mouse wheel while in freelook mode, or by holding down the
\"fast\" or \"slow\" modifier keys (`Shift`{.interpreted-text
role="kbd"} and `Alt`{.interpreted-text role="kbd"} by default,
respectively).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/freelook/freelook_inertia}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/freelook/freelook_inertia**
`🔗<class_EditorSettings_property_editors/3d/freelook/freelook_inertia>`{.interpreted-text
role="ref"}

The inertia of the 3D freelook camera. Higher values make the camera
start and stop slower, which looks smoother but adds latency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/freelook/freelook_navigation_scheme}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/freelook/freelook_navigation_scheme**
`🔗<class_EditorSettings_property_editors/3d/freelook/freelook_navigation_scheme>`{.interpreted-text
role="ref"}

The navigation scheme to use when freelook is enabled in the 3D editor.
Some of the navigation schemes below may be more convenient when
designing specific levels in the 3D editor.

- **Default:** The \"Freelook Forward\", \"Freelook Backward\",
  \"Freelook Up\" and \"Freelook Down\" keys will move relative to the
  camera, taking its pitch angle into account for the movement.
- **Partially Axis-Locked:** The \"Freelook Forward\" and \"Freelook
  Backward\" keys will move relative to the camera, taking its pitch
  angle into account for the movement. The \"Freelook Up\" and
  \"Freelook Down\" keys will move in an \"absolute\" manner, *not*
  taking the camera\'s pitch angle into account for the movement.
- **Fully Axis-Locked:** The \"Freelook Forward\", \"Freelook
  Backward\", \"Freelook Up\" and \"Freelook Down\" keys will move in an
  \"absolute\" manner, *not* taking the camera\'s pitch angle into
  account for the movement.

See also
`editors/3d/navigation/navigation_scheme<class_EditorSettings_property_editors/3d/navigation/navigation_scheme>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/freelook/freelook_sensitivity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/freelook/freelook_sensitivity**
`🔗<class_EditorSettings_property_editors/3d/freelook/freelook_sensitivity>`{.interpreted-text
role="ref"}

The mouse sensitivity to use while freelook mode is active in the 3D
editor. See also
`editors/3d/navigation_feel/orbit_sensitivity<class_EditorSettings_property_editors/3d/navigation_feel/orbit_sensitivity>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/freelook/freelook_speed_zoom_link}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/freelook/freelook_speed_zoom_link**
`🔗<class_EditorSettings_property_editors/3d/freelook/freelook_speed_zoom_link>`{.interpreted-text
role="ref"}

If `true`, freelook speed is linked to the zoom value used in the camera
orbit mode in the 3D editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/grid_division_level_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/grid_division_level_bias**
`🔗<class_EditorSettings_property_editors/3d/grid_division_level_bias>`{.interpreted-text
role="ref"}

The grid division bias to use in the 3D editor. Negative values will
cause small grid divisions to appear earlier, whereas positive values
will cause small grid divisions to appear later.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/grid_division_level_max}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/grid_division_level_max**
`🔗<class_EditorSettings_property_editors/3d/grid_division_level_max>`{.interpreted-text
role="ref"}

The largest grid division to use in the 3D editor. Together with
`editors/3d/primary_grid_steps<class_EditorSettings_property_editors/3d/primary_grid_steps>`{.interpreted-text
role="ref"}, this determines how large the grid divisions can be. The
grid divisions will not be able to get larger than
`primary_grid_steps ^ grid_division_level_max` units. By default, when
`editors/3d/primary_grid_steps<class_EditorSettings_property_editors/3d/primary_grid_steps>`{.interpreted-text
role="ref"} is `8`, this means grid divisions cannot get larger than
`64` units each (so primary grid lines are `512` units apart), no matter
how far away the camera is from the grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/grid_division_level_min}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/grid_division_level_min**
`🔗<class_EditorSettings_property_editors/3d/grid_division_level_min>`{.interpreted-text
role="ref"}

The smallest grid division to use in the 3D editor. Together with
`editors/3d/primary_grid_steps<class_EditorSettings_property_editors/3d/primary_grid_steps>`{.interpreted-text
role="ref"}, this determines how small the grid divisions can be. The
grid divisions will not be able to get smaller than
`primary_grid_steps ^ grid_division_level_min` units. By default, this
means grid divisions cannot get smaller than 1 unit each, no matter how
close the camera is from the grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/grid_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **editors/3d/grid_size**
`🔗<class_EditorSettings_property_editors/3d/grid_size>`{.interpreted-text
role="ref"}

The grid size in units. Higher values prevent the grid from appearing
\"cut off\" at certain angles, but make the grid more demanding to
render. Depending on the camera\'s position, the grid may not be fully
visible since a shader is used to fade it progressively.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/grid_xy_plane}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/grid_xy_plane**
`🔗<class_EditorSettings_property_editors/3d/grid_xy_plane>`{.interpreted-text
role="ref"}

If `true`, renders the grid on the XY plane in perspective view. This
can be useful for 3D side-scrolling games.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/grid_xz_plane}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/grid_xz_plane**
`🔗<class_EditorSettings_property_editors/3d/grid_xz_plane>`{.interpreted-text
role="ref"}

If `true`, renders the grid on the XZ plane in perspective view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/grid_yz_plane}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/grid_yz_plane**
`🔗<class_EditorSettings_property_editors/3d/grid_yz_plane>`{.interpreted-text
role="ref"}

If `true`, renders the grid on the YZ plane in perspective view. This
can be useful for 3D side-scrolling games.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/manipulator_gizmo_opacity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/manipulator_gizmo_opacity**
`🔗<class_EditorSettings_property_editors/3d/manipulator_gizmo_opacity>`{.interpreted-text
role="ref"}

Opacity of the default gizmo for moving, rotating, and scaling 3D nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/manipulator_gizmo_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/manipulator_gizmo_size**
`🔗<class_EditorSettings_property_editors/3d/manipulator_gizmo_size>`{.interpreted-text
role="ref"}

Size of the default gizmo for moving, rotating, and scaling 3D nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/emulate_3_button_mouse}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/navigation/emulate_3_button_mouse**
`🔗<class_EditorSettings_property_editors/3d/navigation/emulate_3_button_mouse>`{.interpreted-text
role="ref"}

If `true`, enables 3-button mouse emulation mode. This is useful on
laptops when using a trackpad.

When 3-button mouse emulation mode is enabled, the pan, zoom and orbit
modifiers can always be used in the 3D editor viewport, even when not
holding down any mouse button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/emulate_numpad}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/navigation/emulate_numpad**
`🔗<class_EditorSettings_property_editors/3d/navigation/emulate_numpad>`{.interpreted-text
role="ref"}

If `true`, allows using the top row `0`{.interpreted-text
role="kbd"}-`9`{.interpreted-text role="kbd"} keys to function as their
equivalent numpad keys for 3D editor navigation. This should be enabled
on keyboards that have no numeric keypad available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/invert_x_axis}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/navigation/invert_x_axis**
`🔗<class_EditorSettings_property_editors/3d/navigation/invert_x_axis>`{.interpreted-text
role="ref"}

If `true`, invert the horizontal mouse axis when panning or orbiting in
the 3D editor. This setting does *not* apply to freelook mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/invert_y_axis}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/navigation/invert_y_axis**
`🔗<class_EditorSettings_property_editors/3d/navigation/invert_y_axis>`{.interpreted-text
role="ref"}

If `true`, invert the vertical mouse axis when panning, orbiting, or
using freelook mode in the 3D editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/navigation_scheme}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/navigation/navigation_scheme**
`🔗<class_EditorSettings_property_editors/3d/navigation/navigation_scheme>`{.interpreted-text
role="ref"}

The navigation scheme preset to use in the 3D editor. Changing this
setting will affect the mouse button and modifier keys used to navigate
the 3D editor viewport.

All schemes can use `Mouse wheel`{.interpreted-text role="kbd"} to zoom.

- **Godot:** `Middle mouse button`{.interpreted-text role="kbd"} to
  orbit. `Shift + Middle mouse button`{.interpreted-text role="kbd"} to
  pan. `Ctrl + Middle mouse button`{.interpreted-text role="kbd"} to
  zoom.
- **Maya:** `Alt + Left mouse button`{.interpreted-text role="kbd"} to
  orbit. `Middle mouse button`{.interpreted-text role="kbd"} to pan,
  `Shift + Middle mouse button`{.interpreted-text role="kbd"} to pan 10
  times faster. `Alt + Right mouse button`{.interpreted-text role="kbd"}
  to zoom.
- **Modo:** `Alt + Left mouse button`{.interpreted-text role="kbd"} to
  orbit. `Alt + Shift + Left mouse button`{.interpreted-text role="kbd"}
  to pan. `Ctrl + Alt + Left mouse button`{.interpreted-text role="kbd"}
  to zoom.
- **Tablet/Trackpad:** `Alt`{.interpreted-text role="kbd"} to orbit.
  `Shift`{.interpreted-text role="kbd"} to pan. `Ctrl`{.interpreted-text
  role="kbd"} to zoom. Enables 3-button mouse emulation mode.

See also
`editors/3d/navigation/orbit_mouse_button<class_EditorSettings_property_editors/3d/navigation/orbit_mouse_button>`{.interpreted-text
role="ref"},
`editors/3d/navigation/pan_mouse_button<class_EditorSettings_property_editors/3d/navigation/pan_mouse_button>`{.interpreted-text
role="ref"},
`editors/3d/navigation/zoom_mouse_button<class_EditorSettings_property_editors/3d/navigation/zoom_mouse_button>`{.interpreted-text
role="ref"},
`editors/3d/freelook/freelook_navigation_scheme<class_EditorSettings_property_editors/3d/freelook/freelook_navigation_scheme>`{.interpreted-text
role="ref"}, and
`editors/3d/navigation/emulate_3_button_mouse<class_EditorSettings_property_editors/3d/navigation/emulate_3_button_mouse>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* On certain window managers on Linux, the
`Alt`{.interpreted-text role="kbd"} key will be intercepted by the
window manager when clicking a mouse button at the same time. This means
Godot will not see the modifier key as being pressed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/orbit_mouse_button}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/navigation/orbit_mouse_button**
`🔗<class_EditorSettings_property_editors/3d/navigation/orbit_mouse_button>`{.interpreted-text
role="ref"}

The mouse button that needs to be held down to orbit in the 3D editor
viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/pan_mouse_button}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/navigation/pan_mouse_button**
`🔗<class_EditorSettings_property_editors/3d/navigation/pan_mouse_button>`{.interpreted-text
role="ref"}

The mouse button that needs to be held down to pan in the 3D editor
viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/show_viewport_navigation_gizmo}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/navigation/show_viewport_navigation_gizmo**
`🔗<class_EditorSettings_property_editors/3d/navigation/show_viewport_navigation_gizmo>`{.interpreted-text
role="ref"}

If `true`, shows gizmos for moving and rotating the camera in the bottom
corners of the 3D editor\'s viewport. Useful for devices that use touch
screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/show_viewport_rotation_gizmo}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/navigation/show_viewport_rotation_gizmo**
`🔗<class_EditorSettings_property_editors/3d/navigation/show_viewport_rotation_gizmo>`{.interpreted-text
role="ref"}

If `true`, shows a small orientation gizmo in the top-right corner of
the 3D editor\'s viewports.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/warped_mouse_panning}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/3d/navigation/warped_mouse_panning**
`🔗<class_EditorSettings_property_editors/3d/navigation/warped_mouse_panning>`{.interpreted-text
role="ref"}

If `true`, warps the mouse around the 3D viewport while panning in the
3D editor. This makes it possible to pan over a large area without
having to exit panning and adjust the mouse cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/zoom_mouse_button}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/navigation/zoom_mouse_button**
`🔗<class_EditorSettings_property_editors/3d/navigation/zoom_mouse_button>`{.interpreted-text
role="ref"}

The mouse button that needs to be held down to zoom in the 3D editor
viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation/zoom_style}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/navigation/zoom_style**
`🔗<class_EditorSettings_property_editors/3d/navigation/zoom_style>`{.interpreted-text
role="ref"}

The mouse cursor movement direction to use when zooming by moving the
mouse. This does not affect zooming with the mouse wheel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation_feel/orbit_inertia}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/navigation_feel/orbit_inertia**
`🔗<class_EditorSettings_property_editors/3d/navigation_feel/orbit_inertia>`{.interpreted-text
role="ref"}

The inertia to use when orbiting in the 3D editor. Higher values make
the camera start and stop slower, which looks smoother but adds latency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation_feel/orbit_sensitivity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/navigation_feel/orbit_sensitivity**
`🔗<class_EditorSettings_property_editors/3d/navigation_feel/orbit_sensitivity>`{.interpreted-text
role="ref"}

The mouse sensitivity to use when orbiting in the 3D editor. See also
`editors/3d/freelook/freelook_sensitivity<class_EditorSettings_property_editors/3d/freelook/freelook_sensitivity>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation_feel/translation_inertia}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/navigation_feel/translation_inertia**
`🔗<class_EditorSettings_property_editors/3d/navigation_feel/translation_inertia>`{.interpreted-text
role="ref"}

The inertia to use when panning in the 3D editor. Higher values make the
camera start and stop slower, which looks smoother but adds latency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation_feel/translation_sensitivity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/navigation_feel/translation_sensitivity**
`🔗<class_EditorSettings_property_editors/3d/navigation_feel/translation_sensitivity>`{.interpreted-text
role="ref"}

The mouse sensitivity to use when panning in the 3D editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/navigation_feel/zoom_inertia}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d/navigation_feel/zoom_inertia**
`🔗<class_EditorSettings_property_editors/3d/navigation_feel/zoom_inertia>`{.interpreted-text
role="ref"}

The inertia to use when zooming in the 3D editor. Higher values make the
camera start and stop slower, which looks smoother but adds latency.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/primary_grid_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d/primary_grid_color**
`🔗<class_EditorSettings_property_editors/3d/primary_grid_color>`{.interpreted-text
role="ref"}

The color to use for the primary 3D grid. The color\'s alpha channel
affects the grid\'s opacity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/primary_grid_steps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d/primary_grid_steps**
`🔗<class_EditorSettings_property_editors/3d/primary_grid_steps>`{.interpreted-text
role="ref"}

If set above 0, where a primary grid line should be drawn. By default,
primary lines are configured to be more visible than secondary lines.
This helps with measurements in the 3D editor. See also
`editors/3d/primary_grid_color<class_EditorSettings_property_editors/3d/primary_grid_color>`{.interpreted-text
role="ref"} and
`editors/3d/secondary_grid_color<class_EditorSettings_property_editors/3d/secondary_grid_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/secondary_grid_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d/secondary_grid_color**
`🔗<class_EditorSettings_property_editors/3d/secondary_grid_color>`{.interpreted-text
role="ref"}

The color to use for the secondary 3D grid. This is generally a less
visible color than
`editors/3d/primary_grid_color<class_EditorSettings_property_editors/3d/primary_grid_color>`{.interpreted-text
role="ref"}. The color\'s alpha channel affects the grid\'s opacity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d/selection_box_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d/selection_box_color**
`🔗<class_EditorSettings_property_editors/3d/selection_box_color>`{.interpreted-text
role="ref"}

The color to use for the selection box that surrounds selected nodes in
the 3D editor viewport. The color\'s alpha channel influences the
selection box\'s opacity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/aabb}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/aabb**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/aabb>`{.interpreted-text
role="ref"}

The color to use for the AABB gizmo that displays the
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"}\'s custom `AABB<class_AABB>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/camera}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/camera**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/camera>`{.interpreted-text
role="ref"}

The 3D editor gizmo color for
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/csg}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/csg**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/csg>`{.interpreted-text
role="ref"}

The 3D editor gizmo color for CSG nodes (such as
`CSGShape3D<class_CSGShape3D>`{.interpreted-text role="ref"} or
`CSGBox3D<class_CSGBox3D>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/decal}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/decal**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/decal>`{.interpreted-text
role="ref"}

The 3D editor gizmo color for `Decal<class_Decal>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/fog_volume}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/fog_volume**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/fog_volume>`{.interpreted-text
role="ref"}

The 3D editor gizmo color for
`FogVolume<class_FogVolume>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/gridmap_grid}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/gridmap_grid**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/gridmap_grid>`{.interpreted-text
role="ref"}

The 3D editor gizmo color for the
`GridMap<class_GridMap>`{.interpreted-text role="ref"} grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/instantiated}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/instantiated**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/instantiated>`{.interpreted-text
role="ref"}

The color override to use for 3D editor gizmos if the
`Node3D<class_Node3D>`{.interpreted-text role="ref"} in question is part
of an instantiated scene file (from the perspective of the current
scene).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/joint}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/joint**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/joint>`{.interpreted-text
role="ref"}

The 3D editor gizmo color for `Joint3D<class_Joint3D>`{.interpreted-text
role="ref"}s and
`PhysicalBone3D<class_PhysicalBone3D>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/joint_body_a}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/joint_body_a**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/joint_body_a>`{.interpreted-text
role="ref"}

Color for representing
`Joint3D.node_a<class_Joint3D_property_node_a>`{.interpreted-text
role="ref"} for some `Joint3D<class_Joint3D>`{.interpreted-text
role="ref"} types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/joint_body_b}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/joint_body_b**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/joint_body_b>`{.interpreted-text
role="ref"}

Color for representing
`Joint3D.node_b<class_Joint3D_property_node_b>`{.interpreted-text
role="ref"} for some `Joint3D<class_Joint3D>`{.interpreted-text
role="ref"} types.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/lightmap_lines}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/lightmap_lines**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/lightmap_lines>`{.interpreted-text
role="ref"}

Color of lines displayed in baked
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} node\'s
grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/lightprobe_lines}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/lightprobe_lines**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/lightprobe_lines>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/occluder}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/occluder**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/occluder>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/particle_attractor}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/particle_attractor**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/particle_attractor>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`GPUParticlesAttractor3D<class_GPUParticlesAttractor3D>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/particle_collision}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/particle_collision**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/particle_collision>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/particles}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/particles**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/particles>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`CPUParticles3D<class_CPUParticles3D>`{.interpreted-text role="ref"} and
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/path_tilt}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/path_tilt**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/path_tilt>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`Path3D<class_Path3D>`{.interpreted-text role="ref"} tilt circles, which
indicate the direction the `Curve3D<class_Curve3D>`{.interpreted-text
role="ref"} is tilted towards.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/reflection_probe}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/reflection_probe**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/reflection_probe>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/selected_bone}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/selected_bone**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/selected_bone>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for the currently selected
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} bone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/skeleton}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/skeleton**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/skeleton>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`Skeleton3D<class_Skeleton3D>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/spring_bone_collision}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/spring_bone_collision**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/spring_bone_collision>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/spring_bone_inside_collision}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/spring_bone_inside_collision**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/spring_bone_inside_collision>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`SpringBoneCollision3D<class_SpringBoneCollision3D>`{.interpreted-text
role="ref"} nodes with inside mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/spring_bone_joint}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/spring_bone_joint**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/spring_bone_joint>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`SpringBoneSimulator3D<class_SpringBoneSimulator3D>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/stream_player_3d}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/stream_player_3d**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/stream_player_3d>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`AudioStreamPlayer3D<class_AudioStreamPlayer3D>`{.interpreted-text
role="ref"}\'s emission angle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/visibility_notifier}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/visibility_notifier**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/visibility_notifier>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`VisibleOnScreenNotifier3D<class_VisibleOnScreenNotifier3D>`{.interpreted-text
role="ref"} and
`VisibleOnScreenEnabler3D<class_VisibleOnScreenEnabler3D>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/voxel_gi}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_colors/voxel_gi**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_colors/voxel_gi>`{.interpreted-text
role="ref"}

The 3D editor gizmo color used for
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/bone_axis_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_settings/bone_axis_length**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/bone_axis_length>`{.interpreted-text
role="ref"}

The length of `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} bone gizmos in the 3D editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/bone_shape}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_settings/bone_shape**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/bone_shape>`{.interpreted-text
role="ref"}

The shape of `Skeleton3D<class_Skeleton3D>`{.interpreted-text
role="ref"} bone gizmos in the 3D editor. **Wire** is a thin line, while
**Octahedron** is a set of lines that represent a thicker hollow line
pointing in a specific direction (similar to most 3D animation
software).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/lightmap_gi_probe_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_settings/lightmap_gi_probe_size**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/lightmap_gi_probe_size>`{.interpreted-text
role="ref"}

Size of probe gizmos displayed when editing
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} and
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}
nodes. Setting this to `0.0` will hide the probe spheres of
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} and
wireframes of `LightmapProbe<class_LightmapProbe>`{.interpreted-text
role="ref"} nodes, but will keep the wireframes linking probes from
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"} and
billboard icons from
`LightmapProbe<class_LightmapProbe>`{.interpreted-text role="ref"}
intact.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/path3d_tilt_disk_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/3d_gizmos/gizmo_settings/path3d_tilt_disk_size**
`🔗<class_EditorSettings_property_editors/3d_gizmos/gizmo_settings/path3d_tilt_disk_size>`{.interpreted-text
role="ref"}

Size of the disk gizmo displayed when editing
`Path3D<class_Path3D>`{.interpreted-text role="ref"}\'s tilt handles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/autorename_animation_tracks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/animation/autorename_animation_tracks**
`🔗<class_EditorSettings_property_editors/animation/autorename_animation_tracks>`{.interpreted-text
role="ref"}

If `true`, automatically updates animation tracks\' target paths when
renaming or reparenting nodes in the Scene tree dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/confirm_insert_track}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/animation/confirm_insert_track**
`🔗<class_EditorSettings_property_editors/animation/confirm_insert_track>`{.interpreted-text
role="ref"}

If `true`, display a confirmation dialog when adding a new track to an
animation by pressing the \"key\" icon next to a property. Holding Shift
will bypass the dialog.

If `false`, the behavior is reversed, i.e. the dialog only appears when
Shift is held.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/default_animation_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/animation/default_animation_step**
`🔗<class_EditorSettings_property_editors/animation/default_animation_step>`{.interpreted-text
role="ref"}

Default step used when creating a new
`Animation<class_Animation>`{.interpreted-text role="ref"} in the
Animation bottom panel. Only affects the first animation created in the
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}.
By default, other newly created animations will use the step from the
previous ones.

This value is always expressed in seconds. If you want e.g. `10` FPS to
be the default, you need to set the default step to `0.1`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/default_create_bezier_tracks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/animation/default_create_bezier_tracks**
`🔗<class_EditorSettings_property_editors/animation/default_create_bezier_tracks>`{.interpreted-text
role="ref"}

If `true`, create a Bezier track instead of a standard track when
pressing the \"key\" icon next to a property. Bezier tracks provide more
control over animation curves, but are more difficult to adjust quickly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/default_create_reset_tracks}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/animation/default_create_reset_tracks**
`🔗<class_EditorSettings_property_editors/animation/default_create_reset_tracks>`{.interpreted-text
role="ref"}

If `true`, create a `RESET` track when creating a new animation track.
This track can be used to restore the animation to a \"default\" state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/default_fps_compatibility}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/animation/default_fps_compatibility**
`🔗<class_EditorSettings_property_editors/animation/default_fps_compatibility>`{.interpreted-text
role="ref"}

Controls whether
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
will apply snapping to nearest integer FPS when snapping is in Seconds
mode. The option is remembered locally for a scene and this option only
determines the default value when scene doesn\'t have local state yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/default_fps_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/animation/default_fps_mode**
`🔗<class_EditorSettings_property_editors/animation/default_fps_mode>`{.interpreted-text
role="ref"}

Default step mode for
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
(seconds or FPS). The option is remembered locally for a scene and this
option only determines the default value when scene doesn\'t have local
state yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/onion_layers_future_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/animation/onion_layers_future_color**
`🔗<class_EditorSettings_property_editors/animation/onion_layers_future_color>`{.interpreted-text
role="ref"}

The modulate color to use for \"future\" frames displayed in the
animation editor\'s onion skinning feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/animation/onion_layers_past_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/animation/onion_layers_past_color**
`🔗<class_EditorSettings_property_editors/animation/onion_layers_past_color>`{.interpreted-text
role="ref"}

The modulate color to use for \"past\" frames displayed in the animation
editor\'s onion skinning feature.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/bone_mapper/handle_colors/error}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/bone_mapper/handle_colors/error**
`🔗<class_EditorSettings_property_editors/bone_mapper/handle_colors/error>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/bone_mapper/handle_colors/missing}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/bone_mapper/handle_colors/missing**
`🔗<class_EditorSettings_property_editors/bone_mapper/handle_colors/missing>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/bone_mapper/handle_colors/set}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/bone_mapper/handle_colors/set**
`🔗<class_EditorSettings_property_editors/bone_mapper/handle_colors/set>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/bone_mapper/handle_colors/unset}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/bone_mapper/handle_colors/unset**
`🔗<class_EditorSettings_property_editors/bone_mapper/handle_colors/unset>`{.interpreted-text
role="ref"}

::: {.container .contribute}
There is currently no description for this property. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/grid_map/palette_min_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/grid_map/palette_min_width**
`🔗<class_EditorSettings_property_editors/grid_map/palette_min_width>`{.interpreted-text
role="ref"}

Minimum width of GridMap\'s mesh palette side panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/grid_map/pick_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/grid_map/pick_distance**
`🔗<class_EditorSettings_property_editors/grid_map/pick_distance>`{.interpreted-text
role="ref"}

The maximum distance at which tiles can be placed on a GridMap, relative
to the camera position (in 3D units).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/grid_map/preview_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/grid_map/preview_size**
`🔗<class_EditorSettings_property_editors/grid_map/preview_size>`{.interpreted-text
role="ref"}

Texture size of mesh previews generated for GridMap\'s MeshLibrary.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/panning/2d_editor_pan_speed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/panning/2d_editor_pan_speed**
`🔗<class_EditorSettings_property_editors/panning/2d_editor_pan_speed>`{.interpreted-text
role="ref"}

The panning speed when using the mouse wheel or touchscreen events in
the 2D editor. This setting does not apply to panning by holding down
the middle or right mouse buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/panning/2d_editor_panning_scheme}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/panning/2d_editor_panning_scheme**
`🔗<class_EditorSettings_property_editors/panning/2d_editor_panning_scheme>`{.interpreted-text
role="ref"}

Controls whether the mouse wheel scroll zooms or pans in the 2D editor.
See also
`editors/panning/sub_editors_panning_scheme<class_EditorSettings_property_editors/panning/sub_editors_panning_scheme>`{.interpreted-text
role="ref"} and
`editors/panning/animation_editors_panning_scheme<class_EditorSettings_property_editors/panning/animation_editors_panning_scheme>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/panning/animation_editors_panning_scheme}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/panning/animation_editors_panning_scheme**
`🔗<class_EditorSettings_property_editors/panning/animation_editors_panning_scheme>`{.interpreted-text
role="ref"}

Controls whether the mouse wheel scroll zooms or pans in the animation
track and Bezier editors. See also
`editors/panning/2d_editor_panning_scheme<class_EditorSettings_property_editors/panning/2d_editor_panning_scheme>`{.interpreted-text
role="ref"} and
`editors/panning/sub_editors_panning_scheme<class_EditorSettings_property_editors/panning/sub_editors_panning_scheme>`{.interpreted-text
role="ref"} (which controls the animation blend tree editor\'s pan
behavior).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/panning/simple_panning}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/panning/simple_panning**
`🔗<class_EditorSettings_property_editors/panning/simple_panning>`{.interpreted-text
role="ref"}

If `true`, allows panning by holding down `Space`{.interpreted-text
role="kbd"} in the 2D editor viewport (in addition to panning with the
middle or right mouse buttons). If `false`, the left mouse button must
be held down while holding down `Space`{.interpreted-text role="kbd"} to
pan in the 2D editor viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/panning/sub_editors_panning_scheme}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/panning/sub_editors_panning_scheme**
`🔗<class_EditorSettings_property_editors/panning/sub_editors_panning_scheme>`{.interpreted-text
role="ref"}

Controls whether the mouse wheel scroll zooms or pans in subeditors. The
list of affected subeditors is: animation blend tree editor,
`Polygon2D<class_Polygon2D>`{.interpreted-text role="ref"} editor,
tileset editor, texture region editor and visual shader editor. See also
`editors/panning/2d_editor_panning_scheme<class_EditorSettings_property_editors/panning/2d_editor_panning_scheme>`{.interpreted-text
role="ref"} and
`editors/panning/animation_editors_panning_scheme<class_EditorSettings_property_editors/panning/animation_editors_panning_scheme>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/panning/warped_mouse_panning}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/panning/warped_mouse_panning**
`🔗<class_EditorSettings_property_editors/panning/warped_mouse_panning>`{.interpreted-text
role="ref"}

If `true`, warps the mouse around the 2D viewport while panning in the
2D editor. This makes it possible to pan over a large area without
having to exit panning and adjust the mouse cursor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/panning/zoom_style}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/panning/zoom_style**
`🔗<class_EditorSettings_property_editors/panning/zoom_style>`{.interpreted-text
role="ref"}

The mouse cursor movement direction to use when drag-zooming in any
editor (except 3D scene editor) by moving the mouse. This does not
affect zooming with the mouse wheel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/polygon_editor/auto_bake_delay}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/polygon_editor/auto_bake_delay**
`🔗<class_EditorSettings_property_editors/polygon_editor/auto_bake_delay>`{.interpreted-text
role="ref"}

The delay in seconds until more complex and performance costly polygon
editors commit their outlines, e.g. the 2D navigation polygon editor
rebakes the navigation mesh polygons. A negative value stops the auto
bake.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/polygon_editor/point_grab_radius}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/polygon_editor/point_grab_radius**
`🔗<class_EditorSettings_property_editors/polygon_editor/point_grab_radius>`{.interpreted-text
role="ref"}

The radius in which points can be selected in the
`Polygon2D<class_Polygon2D>`{.interpreted-text role="ref"} and
`CollisionPolygon2D<class_CollisionPolygon2D>`{.interpreted-text
role="ref"} editors (in pixels). Higher values make it easier to select
points quickly, but can make it more difficult to select the expected
point when several points are located close to each other.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/polygon_editor/show_previous_outline}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/polygon_editor/show_previous_outline**
`🔗<class_EditorSettings_property_editors/polygon_editor/show_previous_outline>`{.interpreted-text
role="ref"}

If `true`, displays the polygon\'s previous shape in the 2D polygon
editors with an opaque gray outline. This outline is displayed while
dragging a point until the left mouse button is released.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/shader_editor/behavior/files/restore_shaders_on_load}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/shader_editor/behavior/files/restore_shaders_on_load**
`🔗<class_EditorSettings_property_editors/shader_editor/behavior/files/restore_shaders_on_load>`{.interpreted-text
role="ref"}

If `true`, reopens shader files that were open in the shader editor when
the project was last closed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/tiles_editor/display_grid}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/tiles_editor/display_grid**
`🔗<class_EditorSettings_property_editors/tiles_editor/display_grid>`{.interpreted-text
role="ref"}

If `true`, displays a grid while the TileMap editor is active. See also
`editors/tiles_editor/grid_color<class_EditorSettings_property_editors/tiles_editor/grid_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/tiles_editor/grid_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/tiles_editor/grid_color**
`🔗<class_EditorSettings_property_editors/tiles_editor/grid_color>`{.interpreted-text
role="ref"}

The color to use for the TileMap editor\'s grid.

\*\*Note:\*\* Only effective if
`editors/tiles_editor/display_grid<class_EditorSettings_property_editors/tiles_editor/display_grid>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/tiles_editor/highlight_selected_layer}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**editors/tiles_editor/highlight_selected_layer**
`🔗<class_EditorSettings_property_editors/tiles_editor/highlight_selected_layer>`{.interpreted-text
role="ref"}

Highlight the currently selected TileMapLayer by dimming the other ones
in the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/color_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/color_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/color_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Color\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/conditional_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/conditional_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/conditional_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the
\"Conditional\" category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/input_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/input_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/input_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Input\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/output_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/output_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/output_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Output\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/particle_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/particle_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/particle_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Particle\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/scalar_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/scalar_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/scalar_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Scalar\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/special_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/special_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/special_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Special\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/textures_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/textures_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/textures_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Textures\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/transform_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/transform_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/transform_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Transform\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/utility_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/utility_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/utility_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Utility\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/category_colors/vector_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/category_colors/vector_color**
`🔗<class_EditorSettings_property_editors/visual_editors/category_colors/vector_color>`{.interpreted-text
role="ref"}

The color of a graph node\'s header when it belongs to the \"Vector\"
category.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/color_theme}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editors/visual_editors/color_theme**
`🔗<class_EditorSettings_property_editors/visual_editors/color_theme>`{.interpreted-text
role="ref"}

The color theme to use in the visual shader editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/connection_colors/boolean_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/connection_colors/boolean_color**
`🔗<class_EditorSettings_property_editors/visual_editors/connection_colors/boolean_color>`{.interpreted-text
role="ref"}

The color of a port/connection of boolean type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/connection_colors/sampler_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/connection_colors/sampler_color**
`🔗<class_EditorSettings_property_editors/visual_editors/connection_colors/sampler_color>`{.interpreted-text
role="ref"}

The color of a port/connection of sampler type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/connection_colors/scalar_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/connection_colors/scalar_color**
`🔗<class_EditorSettings_property_editors/visual_editors/connection_colors/scalar_color>`{.interpreted-text
role="ref"}

The color of a port/connection of scalar type (float, int, unsigned
int).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/connection_colors/transform_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/connection_colors/transform_color**
`🔗<class_EditorSettings_property_editors/visual_editors/connection_colors/transform_color>`{.interpreted-text
role="ref"}

The color of a port/connection of transform type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/connection_colors/vector2_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/connection_colors/vector2_color**
`🔗<class_EditorSettings_property_editors/visual_editors/connection_colors/vector2_color>`{.interpreted-text
role="ref"}

The color of a port/connection of Vector2 type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/connection_colors/vector3_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/connection_colors/vector3_color**
`🔗<class_EditorSettings_property_editors/visual_editors/connection_colors/vector3_color>`{.interpreted-text
role="ref"}

The color of a port/connection of Vector3 type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/connection_colors/vector4_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**editors/visual_editors/connection_colors/vector4_color**
`🔗<class_EditorSettings_property_editors/visual_editors/connection_colors/vector4_color>`{.interpreted-text
role="ref"}

The color of a port/connection of Vector4 type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/grid_pattern}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/visual_editors/grid_pattern**
`🔗<class_EditorSettings_property_editors/visual_editors/grid_pattern>`{.interpreted-text
role="ref"}

The pattern used for the background grid.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/lines_curvature}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/visual_editors/lines_curvature**
`🔗<class_EditorSettings_property_editors/visual_editors/lines_curvature>`{.interpreted-text
role="ref"}

The curvature to use for connection lines in the visual shader editor.
Higher values will make connection lines appear more curved, with values
above `0.5` resulting in more \"angular\" turns in the middle of
connection lines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/minimap_opacity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**editors/visual_editors/minimap_opacity**
`🔗<class_EditorSettings_property_editors/visual_editors/minimap_opacity>`{.interpreted-text
role="ref"}

The opacity of the minimap displayed in the bottom-right corner of the
visual shader editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_editors/visual_editors/visual_shader/port_preview_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**editors/visual_editors/visual_shader/port_preview_size**
`🔗<class_EditorSettings_property_editors/visual_editors/visual_shader/port_preview_size>`{.interpreted-text
role="ref"}

The size to use for port previews in the visual shader uniforms (toggled
by clicking the \"eye\" icon next to an output). The value is defined in
pixels at 100% zoom, and will scale with zoom automatically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_export/ssh/scp}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **export/ssh/scp**
`🔗<class_EditorSettings_property_export/ssh/scp>`{.interpreted-text
role="ref"}

Path to the SCP (secure copy) executable (used for remote deploy to
desktop platforms). If left empty, the editor will attempt to run `scp`
from `PATH`.

\*\*Note:\*\* SCP is not the same as SFTP. Specifying the SFTP
executable here will not work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_export/ssh/ssh}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **export/ssh/ssh**
`🔗<class_EditorSettings_property_export/ssh/ssh>`{.interpreted-text
role="ref"}

Path to the SSH executable (used for remote deploy to desktop
platforms). If left empty, the editor will attempt to run `ssh` from
`PATH`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/directories/autoscan_project_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/directories/autoscan_project_path**
`🔗<class_EditorSettings_property_filesystem/directories/autoscan_project_path>`{.interpreted-text
role="ref"}

The folder where projects should be scanned for (recursively), in a way
similar to the project manager\'s **Scan** button. This can be set to
the same value as
`filesystem/directories/default_project_path<class_EditorSettings_property_filesystem/directories/default_project_path>`{.interpreted-text
role="ref"} for convenience.

\*\*Note:\*\* Setting this path to a folder with very large amounts of
files/folders can slow down the project manager startup significantly.
To keep the project manager quick to start up, it is recommended to set
this value to a folder as \"specific\" as possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/directories/default_project_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/directories/default_project_path**
`🔗<class_EditorSettings_property_filesystem/directories/default_project_path>`{.interpreted-text
role="ref"}

The folder where new projects should be created by default when clicking
the project manager\'s **New Project** button. This can be set to the
same value as
`filesystem/directories/autoscan_project_path<class_EditorSettings_property_filesystem/directories/autoscan_project_path>`{.interpreted-text
role="ref"} for convenience.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/external_programs/3d_model_editor}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/external_programs/3d_model_editor**
`🔗<class_EditorSettings_property_filesystem/external_programs/3d_model_editor>`{.interpreted-text
role="ref"}

The program that opens 3D model scene files when clicking \"Open in
External Program\" option in Filesystem Dock. If not specified, the file
will be opened in the system\'s default program.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/external_programs/audio_editor}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/external_programs/audio_editor**
`🔗<class_EditorSettings_property_filesystem/external_programs/audio_editor>`{.interpreted-text
role="ref"}

The program that opens audio files when clicking \"Open in External
Program\" option in Filesystem Dock. If not specified, the file will be
opened in the system\'s default program.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/external_programs/raster_image_editor}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/external_programs/raster_image_editor**
`🔗<class_EditorSettings_property_filesystem/external_programs/raster_image_editor>`{.interpreted-text
role="ref"}

The program that opens raster image files when clicking \"Open in
External Program\" option in Filesystem Dock. If not specified, the file
will be opened in the system\'s default program.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/external_programs/terminal_emulator}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/external_programs/terminal_emulator**
`🔗<class_EditorSettings_property_filesystem/external_programs/terminal_emulator>`{.interpreted-text
role="ref"}

The terminal emulator program to use when using **Open in Terminal**
context menu action in the FileSystem dock. You can enter an absolute
path to a program binary, or a path to a program that is present in the
`PATH` environment variable.

If left empty, Godot will use the default terminal emulator for the
system:

- **Windows:** PowerShell
- **macOS:** Terminal.app
- **Linux:** The first terminal found on the system in this order:
  gnome-terminal, konsole, xfce4-terminal, lxterminal, kitty, alacritty,
  urxvt, xterm.

To use Command Prompt (cmd) instead of PowerShell on Windows, enter
`cmd` in this field and the correct flags will automatically be used.

On macOS, make sure to point to the actual program binary located within
the `Programs/MacOS` folder of the .app bundle, rather than the .app
bundle directory.

If specifying a custom terminal emulator, you may need to override
`filesystem/external_programs/terminal_emulator_flags<class_EditorSettings_property_filesystem/external_programs/terminal_emulator_flags>`{.interpreted-text
role="ref"} so it opens in the correct folder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/external_programs/terminal_emulator_flags}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/external_programs/terminal_emulator_flags**
`🔗<class_EditorSettings_property_filesystem/external_programs/terminal_emulator_flags>`{.interpreted-text
role="ref"}

The command-line arguments to pass to the terminal emulator that is run
when using **Open in Terminal** context menu action in the FileSystem
dock. See also
`filesystem/external_programs/terminal_emulator<class_EditorSettings_property_filesystem/external_programs/terminal_emulator>`{.interpreted-text
role="ref"}.

If left empty, the default flags are `{directory}`, which is replaced by
the absolute path to the directory that is being opened in the terminal.

\*\*Note:\*\* If the terminal emulator is set to PowerShell, cmd, or
Konsole, Godot will automatically prepend arguments to this list, as
these terminals require nonstandard arguments to open in the correct
folder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/external_programs/vector_image_editor}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/external_programs/vector_image_editor**
`🔗<class_EditorSettings_property_filesystem/external_programs/vector_image_editor>`{.interpreted-text
role="ref"}

The program that opens vector image files when clicking \"Open in
External Program\" option in Filesystem Dock. If not specified, the file
will be opened in the system\'s default program.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/file_dialog/display_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**filesystem/file_dialog/display_mode**
`🔗<class_EditorSettings_property_filesystem/file_dialog/display_mode>`{.interpreted-text
role="ref"}

The display mode to use in the editor\'s file dialogs.

- **Thumbnails** takes more space, but displays dynamic resource
  thumbnails, making resources easier to preview without having to open
  them.
- **List** is more compact but doesn\'t display dynamic resource
  thumbnails. Instead, it displays static icons based on the file
  extension.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/file_dialog/show_hidden_files}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/file_dialog/show_hidden_files**
`🔗<class_EditorSettings_property_filesystem/file_dialog/show_hidden_files>`{.interpreted-text
role="ref"}

If `true`, display hidden files in the editor\'s file dialogs. Files
that have names starting with `.` are considered hidden (e.g.
`.hidden_file`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/file_dialog/thumbnail_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**filesystem/file_dialog/thumbnail_size**
`🔗<class_EditorSettings_property_filesystem/file_dialog/thumbnail_size>`{.interpreted-text
role="ref"}

The thumbnail size to use in the editor\'s file dialogs (in pixels). See
also
`docks/filesystem/thumbnail_size<class_EditorSettings_property_docks/filesystem/thumbnail_size>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/file_server/password}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/file_server/password**
`🔗<class_EditorSettings_property_filesystem/file_server/password>`{.interpreted-text
role="ref"}

Password used for file server when exporting project with remote file
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/file_server/port}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**filesystem/file_server/port**
`🔗<class_EditorSettings_property_filesystem/file_server/port>`{.interpreted-text
role="ref"}

Port used for file server when exporting project with remote file
system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/import/blender/blender_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/import/blender/blender_path**
`🔗<class_EditorSettings_property_filesystem/import/blender/blender_path>`{.interpreted-text
role="ref"}

The path to the Blender executable used for converting the Blender 3D
scene files `.blend` to glTF 2.0 format during import. Blender 3.0 or
later is required.

To enable this feature for your specific project, use
`ProjectSettings.filesystem/import/blender/enabled<class_ProjectSettings_property_filesystem/import/blender/enabled>`{.interpreted-text
role="ref"}.

If this setting is empty, Blender\'s default paths will be detected and
used automatically if present in this order:

\*\*Windows:\*\*

    - C:\Program Files\Blender Foundation\blender.exe
    - C:\Program Files (x86)\Blender Foundation\blender.exe

\*\*macOS:\*\*

    - /opt/homebrew/bin/blender
    - /opt/local/bin/blender
    - /usr/local/bin/blender
    - /usr/local/opt/blender
    - /Applications/Blender.app/Contents/MacOS/Blender

\*\*Linux/\*BSD:\*\*

    - /usr/bin/blender
    - /usr/local/bin/blender
    - /opt/blender/bin/blender

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/import/blender/rpc_port}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**filesystem/import/blender/rpc_port**
`🔗<class_EditorSettings_property_filesystem/import/blender/rpc_port>`{.interpreted-text
role="ref"}

The port number used for Remote Procedure Call (RPC) communication with
Godot\'s created process of the blender executable.

Setting this to 0 effectively disables communication with Godot and the
blender process, making performance slower.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/import/blender/rpc_server_uptime}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**filesystem/import/blender/rpc_server_uptime**
`🔗<class_EditorSettings_property_filesystem/import/blender/rpc_server_uptime>`{.interpreted-text
role="ref"}

The maximum idle uptime (in seconds) of the Blender process.

This prevents Godot from having to create a new process for each import
within the given seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/import/fbx/fbx2gltf_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/import/fbx/fbx2gltf_path**
`🔗<class_EditorSettings_property_filesystem/import/fbx/fbx2gltf_path>`{.interpreted-text
role="ref"}

The path to the FBX2glTF executable used for converting Autodesk FBX 3D
scene files `.fbx` to glTF 2.0 format during import.

To enable this feature for your specific project, use
`ProjectSettings.filesystem/import/fbx2gltf/enabled<class_ProjectSettings_property_filesystem/import/fbx2gltf/enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/on_save/compress_binary_resources}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/on_save/compress_binary_resources**
`🔗<class_EditorSettings_property_filesystem/on_save/compress_binary_resources>`{.interpreted-text
role="ref"}

If `true`, uses lossless compression for binary resources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/on_save/safe_save_on_backup_then_rename}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/on_save/safe_save_on_backup_then_rename**
`🔗<class_EditorSettings_property_filesystem/on_save/safe_save_on_backup_then_rename>`{.interpreted-text
role="ref"}

If `true`, when saving a file, the editor will rename the old file to a
different name, save a new file, then only remove the old file once the
new file has been saved. This makes loss of data less likely to happen
if the editor or operating system exits unexpectedly while saving (e.g.
due to a crash or power outage).

\*\*Note:\*\* On Windows, this feature can interact negatively with
certain antivirus programs. In this case, you may have to set this to
`false` to prevent file locking issues.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/quick_open_dialog/default_display_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**filesystem/quick_open_dialog/default_display_mode**
`🔗<class_EditorSettings_property_filesystem/quick_open_dialog/default_display_mode>`{.interpreted-text
role="ref"}

If set to `Adaptive`, the dialog opens in list view or grid view
depending on the requested type. If set to `Last Used`, the display mode
will always open the way you last used it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/quick_open_dialog/enable_fuzzy_matching}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/quick_open_dialog/enable_fuzzy_matching**
`🔗<class_EditorSettings_property_filesystem/quick_open_dialog/enable_fuzzy_matching>`{.interpreted-text
role="ref"}

If `true`, together with exact matches of a filename, the dialog
includes approximate matches.

This is useful for finding the correct files even when there are typos
in the search query; for example, searching \"nprmal\" will find
\"normal\". Additionally, it allows you to write shorter search queries;
for example, searching \"nml\" will also find \"normal\".

See also
`filesystem/quick_open_dialog/max_fuzzy_misses<class_EditorSettings_property_filesystem/quick_open_dialog/max_fuzzy_misses>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/quick_open_dialog/include_addons}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/quick_open_dialog/include_addons**
`🔗<class_EditorSettings_property_filesystem/quick_open_dialog/include_addons>`{.interpreted-text
role="ref"}

If `true`, results will include files located in the `addons` folder.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/quick_open_dialog/max_fuzzy_misses}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**filesystem/quick_open_dialog/max_fuzzy_misses**
`🔗<class_EditorSettings_property_filesystem/quick_open_dialog/max_fuzzy_misses>`{.interpreted-text
role="ref"}

The number of missed query characters allowed in a match when fuzzy
matching is enabled. For example, with the default value of `2`,
`"normal"` would match `"narmal"` and `"norma"` but not `"nor"`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/quick_open_dialog/max_results}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**filesystem/quick_open_dialog/max_results**
`🔗<class_EditorSettings_property_filesystem/quick_open_dialog/max_results>`{.interpreted-text
role="ref"}

Maximum number of matches to show in dialog.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/quick_open_dialog/show_search_highlight}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**filesystem/quick_open_dialog/show_search_highlight**
`🔗<class_EditorSettings_property_filesystem/quick_open_dialog/show_search_highlight>`{.interpreted-text
role="ref"}

If `true`, results will be highlighted with their search matches.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_filesystem/tools/oidn/oidn_denoise_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**filesystem/tools/oidn/oidn_denoise_path**
`🔗<class_EditorSettings_property_filesystem/tools/oidn/oidn_denoise_path>`{.interpreted-text
role="ref"}

The path to the directory containing the Open Image Denoise (OIDN)
executable, used optionally for denoising lightmaps. It can be
downloaded from
[openimagedenoise.org](https://www.openimagedenoise.org/downloads.html).

To enable this feature for your specific project, use
`ProjectSettings.rendering/lightmapping/denoising/denoiser<class_ProjectSettings_property_rendering/lightmapping/denoising/denoiser>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_input/buffering/agile_event_flushing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input/buffering/agile_event_flushing**
`🔗<class_EditorSettings_property_input/buffering/agile_event_flushing>`{.interpreted-text
role="ref"}

If `true`, input events will be flushed just before every idle and
physics frame.

If `false`, these events will be flushed only once per process frame,
between iterations of the engine.

Enabling this setting can greatly improve input responsiveness,
especially in devices that struggle to run at the project\'s intended
frame rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_input/buffering/use_accumulated_input}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**input/buffering/use_accumulated_input**
`🔗<class_EditorSettings_property_input/buffering/use_accumulated_input>`{.interpreted-text
role="ref"}

If `true`, similar input events sent by the operating system are
accumulated. When input accumulation is enabled, all input events
generated during a frame will be merged and emitted when the frame is
done rendering. Therefore, this limits the number of input method calls
per second to the rendering FPS.

Input accumulation can be disabled to get slightly more precise/reactive
input at the cost of increased CPU usage.

\*\*Note:\*\* Input accumulation is *enabled* by default.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/accessibility/accessibility_support}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/accessibility/accessibility_support**
`🔗<class_EditorSettings_property_interface/accessibility/accessibility_support>`{.interpreted-text
role="ref"}

Editor accessibility support mode:

- **Auto** (`0`): Accessibility support is enabled, but updates to the
  accessibility information are processed only if an assistive app (such
  as a screen reader or a Braille display) is active (default).
- **Always Active** (`1`): Accessibility support is enabled, and updates
  to the accessibility information are always processed, regardless of
  the status of assistive apps.
- **Disabled** (`2`): Accessibility support is fully disabled.

\*\*Note:\*\* Accessibility debugging tools, such as Accessibility
Insights for Windows, Accessibility Inspector (macOS), or AT-SPI Browser
(Linux/BSD) do not count as assistive apps. To test your project with
these tools, use **Always Active**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/accept_dialog_cancel_ok_buttons}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/accept_dialog_cancel_ok_buttons**
`🔗<class_EditorSettings_property_interface/editor/accept_dialog_cancel_ok_buttons>`{.interpreted-text
role="ref"}

How to position the Cancel and OK buttons in the editor\'s
`AcceptDialog<class_AcceptDialog>`{.interpreted-text role="ref"}s.
Different platforms have different standard behaviors for this, which
can be overridden using this setting. This is useful if you use Godot
both on Windows and macOS/Linux and your Godot muscle memory is stronger
than your OS specific one.

- **Auto** follows the platform convention: OK first on Windows, KDE,
  and LXQt, Cancel first on macOS and other Linux desktop environments.
- **Cancel First** forces the ordering Cancel/OK.
- **OK First** forces the ordering OK/Cancel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/automatically_open_screenshots}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/automatically_open_screenshots**
`🔗<class_EditorSettings_property_interface/editor/automatically_open_screenshots>`{.interpreted-text
role="ref"}

If `true`, automatically opens screenshots with the default program
associated to `.png` files after a screenshot is taken using the
**Editor \> Take Screenshot** action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/code_font}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/editor/code_font**
`🔗<class_EditorSettings_property_interface/editor/code_font>`{.interpreted-text
role="ref"}

The font to use for the script editor. Must be a resource of a
`Font<class_Font>`{.interpreted-text role="ref"} type such as a `.ttf`
or `.otf` font file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/code_font_contextual_ligatures}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/code_font_contextual_ligatures**
`🔗<class_EditorSettings_property_interface/editor/code_font_contextual_ligatures>`{.interpreted-text
role="ref"}

The font ligatures to enable for the currently configured code font. Not
all fonts include support for ligatures.

\*\*Note:\*\* The default editor code font ([JetBrains
Mono](https://www.jetbrains.com/lp/mono/)) has contextual ligatures in
its font file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/code_font_custom_opentype_features}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/editor/code_font_custom_opentype_features**
`🔗<class_EditorSettings_property_interface/editor/code_font_custom_opentype_features>`{.interpreted-text
role="ref"}

List of custom OpenType features to use, if supported by the currently
configured code font. Not all fonts include support for custom OpenType
features. The string should follow the OpenType specification.

\*\*Note:\*\* The default editor code font ([JetBrains
Mono](https://www.jetbrains.com/lp/mono/)) has custom OpenType features
in its font file, but there is no documented list yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/code_font_custom_variations}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/editor/code_font_custom_variations**
`🔗<class_EditorSettings_property_interface/editor/code_font_custom_variations>`{.interpreted-text
role="ref"}

List of alternative characters to use, if supported by the currently
configured code font. Not all fonts include support for custom
variations. The string should follow the OpenType specification.

\*\*Note:\*\* The default editor code font ([JetBrains
Mono](https://www.jetbrains.com/lp/mono/)) has alternate characters in
its font file, but there is no documented list yet.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/code_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/code_font_size**
`🔗<class_EditorSettings_property_interface/editor/code_font_size>`{.interpreted-text
role="ref"}

The size of the font in the script editor. This setting does not impact
the font size of the Output panel (see
`run/output/font_size<class_EditorSettings_property_run/output/font_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/collapse_main_menu}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/collapse_main_menu**
`🔗<class_EditorSettings_property_interface/editor/collapse_main_menu>`{.interpreted-text
role="ref"}

If `true`, the main menu collapses into a
`MenuButton<class_MenuButton>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This setting is only applicable on macOS when
`interface/editor/use_embedded_menu<class_EditorSettings_property_interface/editor/use_embedded_menu>`{.interpreted-text
role="ref"} is `true`.

\*\*Note:\*\* Defaults to `true` on the Android editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/custom_display_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**interface/editor/custom_display_scale**
`🔗<class_EditorSettings_property_interface/editor/custom_display_scale>`{.interpreted-text
role="ref"}

The custom editor scale factor to use. This can be used for displays
with very high DPI where a scale factor of 200% is not sufficient.

\*\*Note:\*\* Only effective if
`interface/editor/display_scale<class_EditorSettings_property_interface/editor/display_scale>`{.interpreted-text
role="ref"} is set to **Custom**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/display_scale}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/display_scale**
`🔗<class_EditorSettings_property_interface/editor/display_scale>`{.interpreted-text
role="ref"}

The display scale factor to use for the editor interface. Higher values
are more suited to hiDPI/Retina displays.

If set to **Auto**, the editor scale is automatically determined based
on the screen resolution and reported display DPI. This heuristic is not
always ideal, which means you can get better results by setting the
editor scale manually.

If set to **Custom**, the scaling value in
`interface/editor/custom_display_scale<class_EditorSettings_property_interface/editor/custom_display_scale>`{.interpreted-text
role="ref"} will be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/dock_tab_style}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/dock_tab_style**
`🔗<class_EditorSettings_property_interface/editor/dock_tab_style>`{.interpreted-text
role="ref"}

Tab style of editor docks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/editor_language}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/editor/editor_language**
`🔗<class_EditorSettings_property_interface/editor/editor_language>`{.interpreted-text
role="ref"}

The language to use for the editor interface.

Translations are provided by the community. If you spot a mistake,
`contribute to editor translations on Weblate! <../contributing/documentation/editor_and_docs_localization>`{.interpreted-text
role="doc"}

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/editor_screen}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/editor_screen**
`🔗<class_EditorSettings_property_interface/editor/editor_screen>`{.interpreted-text
role="ref"}

The preferred monitor to display the editor. If **Auto**, the editor
will remember the last screen it was displayed on across multiple
sessions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/expand_to_title}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/expand_to_title**
`🔗<class_EditorSettings_property_interface/editor/expand_to_title>`{.interpreted-text
role="ref"}

Expanding main editor window content to the title, if supported by
`DisplayServer<class_DisplayServer>`{.interpreted-text role="ref"}. See
`DisplayServer.WINDOW_FLAG_EXTEND_TO_TITLE<class_DisplayServer_constant_WINDOW_FLAG_EXTEND_TO_TITLE>`{.interpreted-text
role="ref"}.

Specific to the macOS platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/font_allow_msdf}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/font_allow_msdf**
`🔗<class_EditorSettings_property_interface/editor/font_allow_msdf>`{.interpreted-text
role="ref"}

If set to `true`, MSDF font rendering will be used for the visual shader
graph editor. You may need to set this to `false` when using a custom
main font, as some fonts will look broken due to the use of
self-intersecting outlines in their font data. Downloading the font from
the font maker\'s official website as opposed to a service like Google
Fonts can help resolve this issue.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/font_antialiasing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/font_antialiasing**
`🔗<class_EditorSettings_property_interface/editor/font_antialiasing>`{.interpreted-text
role="ref"}

FreeType\'s font anti-aliasing mode used to render the editor fonts.
Most fonts are not designed to look good with anti-aliasing disabled, so
it\'s recommended to leave this enabled unless you\'re using a pixel art
font.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/font_disable_embedded_bitmaps}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/font_disable_embedded_bitmaps**
`🔗<class_EditorSettings_property_interface/editor/font_disable_embedded_bitmaps>`{.interpreted-text
role="ref"}

If set to `true`, embedded font bitmap loading is disabled (bitmap-only
and color fonts ignore this property).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/font_hinting}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/font_hinting**
`🔗<class_EditorSettings_property_interface/editor/font_hinting>`{.interpreted-text
role="ref"}

The font hinting mode to use for the editor fonts. FreeType supports the
following font hinting modes:

- **None:** Don\'t use font hinting when rasterizing the font. This
  results in a smooth font, but it can look blurry.
- **Light:** Use hinting on the X axis only. This is a compromise
  between font sharpness and smoothness.
- **Normal:** Use hinting on both X and Y axes. This results in a sharp
  font, but it doesn\'t look very smooth.

If set to **Auto**, the font hinting mode will be set to match the
current operating system in use. This means the **Light** hinting mode
will be used on Windows and Linux, and the **None** hinting mode will be
used on macOS.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/font_subpixel_positioning}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/font_subpixel_positioning**
`🔗<class_EditorSettings_property_interface/editor/font_subpixel_positioning>`{.interpreted-text
role="ref"}

The subpixel positioning mode to use when rendering editor font glyphs.
This affects both the main and code fonts. **Disabled** is the fastest
to render and uses the least memory. **Auto** only uses subpixel
positioning for small font sizes (where the benefit is the most
noticeable). **One Half of a Pixel** and **One Quarter of a Pixel**
force the same subpixel positioning mode for all editor fonts,
regardless of their size (with **One Quarter of a Pixel** being the
highest-quality option).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/import_resources_when_unfocused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/import_resources_when_unfocused**
`🔗<class_EditorSettings_property_interface/editor/import_resources_when_unfocused>`{.interpreted-text
role="ref"}

If `true`, (re)imports resources even if the editor window is unfocused
or minimized. If `false`, resources are only (re)imported when the
editor window is focused. This can be set to `true` to speed up
iteration by starting the import process earlier when saving files in
the project folder. This also allows getting visual feedback on changes
without having to click the editor window, which is useful with
multi-monitor setups. The downside of setting this to `true` is that it
increases idle CPU usage and may steal CPU time from other applications
when importing resources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/keep_screen_on}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/keep_screen_on**
`🔗<class_EditorSettings_property_interface/editor/keep_screen_on>`{.interpreted-text
role="ref"}

If `true`, keeps the screen on (even in case of inactivity), so the
screensaver does not take over. Works on desktop and mobile platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/localize_settings}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/localize_settings**
`🔗<class_EditorSettings_property_interface/editor/localize_settings>`{.interpreted-text
role="ref"}

If `true`, setting names in the editor are localized when possible.

\*\*Note:\*\* This setting affects most
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}s
in the editor UI, primarily Project Settings and Editor Settings. To
control names displayed in the Inspector dock, use
`interface/inspector/default_property_name_style<class_EditorSettings_property_interface/inspector/default_property_name_style>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/low_processor_mode_sleep_usec}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/low_processor_mode_sleep_usec**
`🔗<class_EditorSettings_property_interface/editor/low_processor_mode_sleep_usec>`{.interpreted-text
role="ref"}

The amount of sleeping between frames in the editor (in microseconds).
Higher values will result in lower CPU/GPU usage, which can improve
battery life on laptops. However, higher values will result in a less
responsive editor. The default value is set to allow for maximum
smoothness on monitors up to 144 Hz. See also
`interface/editor/unfocused_low_processor_mode_sleep_usec<class_EditorSettings_property_interface/editor/unfocused_low_processor_mode_sleep_usec>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting is ignored if
`interface/editor/update_continuously<class_EditorSettings_property_interface/editor/update_continuously>`{.interpreted-text
role="ref"} is `true`, as enabling that setting disables low-processor
mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/main_font}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/editor/main_font**
`🔗<class_EditorSettings_property_interface/editor/main_font>`{.interpreted-text
role="ref"}

The font to use for the editor interface. Must be a resource of a
`Font<class_Font>`{.interpreted-text role="ref"} type such as a `.ttf`
or `.otf` font file.

\*\*Note:\*\* If the provided font is variable, a weight of 400 (normal)
will be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/main_font_bold}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/editor/main_font_bold**
`🔗<class_EditorSettings_property_interface/editor/main_font_bold>`{.interpreted-text
role="ref"}

The font to use for bold text in the editor interface. Must be a
resource of a `Font<class_Font>`{.interpreted-text role="ref"} type such
as a `.ttf` or `.otf` font file.

\*\*Note:\*\* If the provided font is variable, a weight of 700 (bold)
will be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/main_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/main_font_size**
`🔗<class_EditorSettings_property_interface/editor/main_font_size>`{.interpreted-text
role="ref"}

The size of the font in the editor interface.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/mouse_extra_buttons_navigate_history}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/mouse_extra_buttons_navigate_history**
`🔗<class_EditorSettings_property_interface/editor/mouse_extra_buttons_navigate_history>`{.interpreted-text
role="ref"}

If `true`, the mouse\'s additional side buttons will be usable to
navigate in the script editor\'s file history. Set this to `false` if
you\'re using the side buttons for other purposes (such as a
push-to-talk button in a VoIP program).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/project_manager_screen}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/project_manager_screen**
`🔗<class_EditorSettings_property_interface/editor/project_manager_screen>`{.interpreted-text
role="ref"}

The preferred monitor to display the project manager.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/save_each_scene_on_quit}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/save_each_scene_on_quit**
`🔗<class_EditorSettings_property_interface/editor/save_each_scene_on_quit>`{.interpreted-text
role="ref"}

If `false`, the editor will save all scenes when confirming the **Save**
action when quitting the editor or quitting to the project list. If
`true`, the editor will ask to save each scene individually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/save_on_focus_loss}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/save_on_focus_loss**
`🔗<class_EditorSettings_property_interface/editor/save_on_focus_loss>`{.interpreted-text
role="ref"}

If `true`, scenes and scripts are saved when the editor loses focus.
Depending on the work flow, this behavior can be less intrusive than
`text_editor/behavior/files/autosave_interval_secs<class_EditorSettings_property_text_editor/behavior/files/autosave_interval_secs>`{.interpreted-text
role="ref"} or remembering to save manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/separate_distraction_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/separate_distraction_mode**
`🔗<class_EditorSettings_property_interface/editor/separate_distraction_mode>`{.interpreted-text
role="ref"}

If `true`, the editor\'s Script tab will have a separate distraction
mode setting from the 2D/3D/Game/AssetLib tabs. If `false`, the
distraction-free mode toggle is shared between all tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/show_internal_errors_in_toast_notifications}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/show_internal_errors_in_toast_notifications**
`🔗<class_EditorSettings_property_interface/editor/show_internal_errors_in_toast_notifications>`{.interpreted-text
role="ref"}

If enabled, displays internal engine errors in toast notifications
(toggleable by clicking the \"bell\" icon at the bottom of the editor).
No matter the value of this setting, non-internal engine errors will
always be visible in toast notifications.

The default **Auto** value will only enable this if the editor was
compiled with the `dev_build=yes` SCons option (the default is
`dev_build=no`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/show_update_spinner}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/show_update_spinner**
`🔗<class_EditorSettings_property_interface/editor/show_update_spinner>`{.interpreted-text
role="ref"}

If enabled, displays an icon in the top-right corner of the editor that
spins when the editor redraws a frame. This can be used to diagnose
situations where the engine is constantly redrawing, which should be
avoided as this increases CPU and GPU utilization for no good reason. To
further troubleshoot these situations, start the editor with the
`--debug-canvas-item-redraw`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}.

Consider enabling this if you are developing editor plugins to ensure
they only make the editor redraw when required.

The default **Auto** value will only enable this if the editor was
compiled with the `dev_build=yes` SCons option (the default is
`dev_build=no`).

\*\*Note:\*\* If
`interface/editor/update_continuously<class_EditorSettings_property_interface/editor/update_continuously>`{.interpreted-text
role="ref"} is `true`, the spinner icon displays in red.

\*\*Note:\*\* If the editor was started with the
`--debug-canvas-item-redraw`
`command line argument <../tutorials/editor/command_line_tutorial>`{.interpreted-text
role="doc"}, the update spinner will *never* display regardless of this
setting\'s value. This is to avoid confusion with what would cause
redrawing in real world scenarios.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/single_window_mode}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/single_window_mode**
`🔗<class_EditorSettings_property_interface/editor/single_window_mode>`{.interpreted-text
role="ref"}

If `true`, embed modal windows such as docks inside the main editor
window. When single-window mode is enabled, tooltips will also be
embedded inside the main editor window, which means they can\'t be
displayed outside of the editor window. Single-window mode can be faster
as it does not need to create a separate window for every popup and
tooltip, which can be a slow operation depending on the operating system
and rendering method in use.

This is equivalent to
`ProjectSettings.display/window/subwindows/embed_subwindows<class_ProjectSettings_property_display/window/subwindows/embed_subwindows>`{.interpreted-text
role="ref"} in the running project, except the setting\'s value is
inverted.

\*\*Note:\*\* To query whether the editor can use multiple windows in an
editor plugin, use
`EditorInterface.is_multi_window_enabled()<class_EditorInterface_method_is_multi_window_enabled>`{.interpreted-text
role="ref"} instead of querying the value of this editor setting.

\*\*Note:\*\* If `true`, game embedding is disabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/tablet_driver}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/tablet_driver**
`🔗<class_EditorSettings_property_interface/editor/tablet_driver>`{.interpreted-text
role="ref"}

Overrides the tablet driver used by the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/ui_layout_direction}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/ui_layout_direction**
`🔗<class_EditorSettings_property_interface/editor/ui_layout_direction>`{.interpreted-text
role="ref"}

Editor UI default layout direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/unfocused_low_processor_mode_sleep_usec}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/unfocused_low_processor_mode_sleep_usec**
`🔗<class_EditorSettings_property_interface/editor/unfocused_low_processor_mode_sleep_usec>`{.interpreted-text
role="ref"}

When the editor window is unfocused, the amount of sleeping between
frames when the low-processor usage mode is enabled (in microseconds).
Higher values will result in lower CPU/GPU usage, which can improve
battery life on laptops (in addition to improving the running project\'s
performance if the editor has to redraw continuously). However, higher
values will result in a less responsive editor. The default value is set
to limit the editor to 10 FPS when the editor window is unfocused. See
also
`interface/editor/low_processor_mode_sleep_usec<class_EditorSettings_property_interface/editor/low_processor_mode_sleep_usec>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This setting is ignored if
`interface/editor/update_continuously<class_EditorSettings_property_interface/editor/update_continuously>`{.interpreted-text
role="ref"} is `true`, as enabling that setting disables low-processor
mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/update_continuously}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/update_continuously**
`🔗<class_EditorSettings_property_interface/editor/update_continuously>`{.interpreted-text
role="ref"}

If `true`, redraws the editor every frame even if nothing has changed on
screen. When this setting is enabled, the update spinner displays in red
(see
`interface/editor/show_update_spinner<class_EditorSettings_property_interface/editor/show_update_spinner>`{.interpreted-text
role="ref"}).

\*\*Warning:\*\* This greatly increases CPU and GPU utilization, leading
to increased power usage. This should only be enabled for
troubleshooting purposes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/use_embedded_menu}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/use_embedded_menu**
`🔗<class_EditorSettings_property_interface/editor/use_embedded_menu>`{.interpreted-text
role="ref"}

If `true`, editor main menu is using embedded
`MenuBar<class_MenuBar>`{.interpreted-text role="ref"} instead of system
global menu.

Specific to the macOS platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/use_native_file_dialogs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editor/use_native_file_dialogs**
`🔗<class_EditorSettings_property_interface/editor/use_native_file_dialogs>`{.interpreted-text
role="ref"}

If `true`, editor UI uses OS native file/directory selection dialogs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editor/vsync_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/editor/vsync_mode**
`🔗<class_EditorSettings_property_interface/editor/vsync_mode>`{.interpreted-text
role="ref"}

Sets the V-Sync mode for the editor. Does not affect the project when
run from the editor (this is controlled by
`ProjectSettings.display/window/vsync/vsync_mode<class_ProjectSettings_property_display/window/vsync/vsync_mode>`{.interpreted-text
role="ref"}).

Depending on the platform and used renderer, the engine will fall back
to **Enabled** if the desired mode is not supported.

\*\*Note:\*\* V-Sync modes other than **Enabled** are only supported in
the Forward+ and Mobile rendering methods, not Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editors/derive_script_globals_by_name}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editors/derive_script_globals_by_name**
`🔗<class_EditorSettings_property_interface/editors/derive_script_globals_by_name>`{.interpreted-text
role="ref"}

If `true`, when extending a script, the global class name of the script
is inserted in the script creation dialog, if it exists. If `false`, the
script\'s file path is always inserted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/editors/show_scene_tree_root_selection}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/editors/show_scene_tree_root_selection**
`🔗<class_EditorSettings_property_interface/editors/show_scene_tree_root_selection>`{.interpreted-text
role="ref"}

If `true`, the Scene dock will display buttons to quickly add a root
node to a newly created scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/auto_unfold_foreign_scenes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/auto_unfold_foreign_scenes**
`🔗<class_EditorSettings_property_interface/inspector/auto_unfold_foreign_scenes>`{.interpreted-text
role="ref"}

If `true`, automatically unfolds Inspector property groups containing
modified values when opening a scene for the first time. Only affects
scenes without saved folding preferences and only unfolds groups with
properties that have been changed from their default values.

\*\*Note:\*\* This setting only works in specific scenarios: when
opening a scene brought in from another project, or when opening a new
scene that already has modified properties (e.g., from version control).
Duplicated scenes are not considered foreign, so this setting will not
affect them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/color_picker_show_intensity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/color_picker_show_intensity**
`🔗<class_EditorSettings_property_interface/inspector/color_picker_show_intensity>`{.interpreted-text
role="ref"}

If `true`, show the intensity slider in the
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}s opened
in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/default_color_picker_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/inspector/default_color_picker_mode**
`🔗<class_EditorSettings_property_interface/inspector/default_color_picker_mode>`{.interpreted-text
role="ref"}

The default color picker mode to use when opening
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}s in the
editor. This mode can be temporarily adjusted on the color picker
itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/default_color_picker_shape}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/inspector/default_color_picker_shape**
`🔗<class_EditorSettings_property_interface/inspector/default_color_picker_shape>`{.interpreted-text
role="ref"}

The default color picker shape to use when opening
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}s in the
editor. This shape can be temporarily adjusted on the color picker
itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/default_float_step}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**interface/inspector/default_float_step**
`🔗<class_EditorSettings_property_interface/inspector/default_float_step>`{.interpreted-text
role="ref"}

The floating-point precision to use for properties that don\'t define an
explicit precision step. Lower values allow entering more precise
values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/default_property_name_style}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/inspector/default_property_name_style**
`🔗<class_EditorSettings_property_interface/inspector/default_property_name_style>`{.interpreted-text
role="ref"}

The default property name style to display in the Inspector dock. This
style can be temporarily adjusted in the Inspector dock\'s menu.

- **Raw:** Displays properties in `snake_case`.
- **Capitalized:** Displays properties capitalized.
- **Localized:** Displays the localized string for the current editor
  language if a translation is available for the given property. If no
  translation is available, falls back to **Capitalized**.

\*\*Note:\*\* To display translated setting names in Project Settings
and Editor Settings, use
`interface/editor/localize_settings<class_EditorSettings_property_interface/editor/localize_settings>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/delimitate_all_container_and_resources}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/delimitate_all_container_and_resources**
`🔗<class_EditorSettings_property_interface/inspector/delimitate_all_container_and_resources>`{.interpreted-text
role="ref"}

If `true`, add a margin around Array, Dictionary, and Resource Editors
that are not already colored.

\*\*Note:\*\* If
`interface/inspector/nested_color_mode<class_EditorSettings_property_interface/inspector/nested_color_mode>`{.interpreted-text
role="ref"} is set to **Containers & Resources** this parameter will
have no effect since those editors will already be colored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/disable_folding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/disable_folding**
`🔗<class_EditorSettings_property_interface/inspector/disable_folding>`{.interpreted-text
role="ref"}

If `true`, forces all property groups to be expanded in the Inspector
dock and prevents collapsing them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/float_drag_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**interface/inspector/float_drag_speed**
`🔗<class_EditorSettings_property_interface/inspector/float_drag_speed>`{.interpreted-text
role="ref"}

Base speed for increasing/decreasing float values by dragging them in
the inspector.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/horizontal_vector2_editing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/horizontal_vector2_editing**
`🔗<class_EditorSettings_property_interface/inspector/horizontal_vector2_editing>`{.interpreted-text
role="ref"}

If `true`, `Vector2<class_Vector2>`{.interpreted-text role="ref"} and
`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} properties are
shown on a single line in the inspector instead of two lines. This is
overall more compact, but it can be harder to view and edit large values
without expanding the inspector horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/horizontal_vector_types_editing}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/horizontal_vector_types_editing**
`🔗<class_EditorSettings_property_interface/inspector/horizontal_vector_types_editing>`{.interpreted-text
role="ref"}

If `true`, `Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Vector3i<class_Vector3i>`{.interpreted-text role="ref"},
`Vector4<class_Vector4>`{.interpreted-text role="ref"},
`Vector4i<class_Vector4i>`{.interpreted-text role="ref"},
`Rect2<class_Rect2>`{.interpreted-text role="ref"},
`Rect2i<class_Rect2i>`{.interpreted-text role="ref"},
`Plane<class_Plane>`{.interpreted-text role="ref"}, and
`Quaternion<class_Quaternion>`{.interpreted-text role="ref"} properties
are shown on a single line in the inspector instead of multiple lines.
This is overall more compact, but it can be harder to view and edit
large values without expanding the inspector horizontally.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/max_array_dictionary_items_per_page}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/inspector/max_array_dictionary_items_per_page**
`🔗<class_EditorSettings_property_interface/inspector/max_array_dictionary_items_per_page>`{.interpreted-text
role="ref"}

The number of `Array<class_Array>`{.interpreted-text role="ref"} or
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} items to
display on each \"page\" in the inspector. Higher values allow viewing
more values per page, but take more time to load. This increased load
time is noticeable when selecting nodes that have array or dictionary
properties in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/nested_color_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/inspector/nested_color_mode**
`🔗<class_EditorSettings_property_interface/inspector/nested_color_mode>`{.interpreted-text
role="ref"}

Control which property editors are colored when they are opened.

- **Containers & Resources:** Color all Array, Dictionary, and Resource
  Editors.
- **Resources:** Color all Resource Editors.
- **External Resources:** Color Resource Editors that edits an external
  resource.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/open_resources_in_current_inspector}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/open_resources_in_current_inspector**
`🔗<class_EditorSettings_property_interface/inspector/open_resources_in_current_inspector>`{.interpreted-text
role="ref"}

If `true`, subresources can be edited in the current inspector view. If
the resource type is defined in
`interface/inspector/resources_to_open_in_new_inspector<class_EditorSettings_property_interface/inspector/resources_to_open_in_new_inspector>`{.interpreted-text
role="ref"} or if this setting is `false`, attempting to edit a
subresource always opens a new inspector view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/resources_to_open_in_new_inspector}
::: rst-class
classref-property
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **interface/inspector/resources_to_open_in_new_inspector**
`🔗<class_EditorSettings_property_interface/inspector/resources_to_open_in_new_inspector>`{.interpreted-text
role="ref"}

List of resources that should always be opened in a new inspector view,
even if
`interface/inspector/open_resources_in_current_inspector<class_EditorSettings_property_interface/inspector/open_resources_in_current_inspector>`{.interpreted-text
role="ref"} is `true`.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/inspector/show_low_level_opentype_features}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/inspector/show_low_level_opentype_features**
`🔗<class_EditorSettings_property_interface/inspector/show_low_level_opentype_features>`{.interpreted-text
role="ref"}

If `true`, display OpenType features marked as `hidden` by the font file
in the `Font<class_Font>`{.interpreted-text role="ref"} editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/multi_window/enable}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/multi_window/enable**
`🔗<class_EditorSettings_property_interface/multi_window/enable>`{.interpreted-text
role="ref"}

If `true`, multiple window support in editor is enabled. The following
panels can become dedicated windows (i.e. made floating): Docks, Script
editor, Shader editor, and Game Workspace.

\*\*Note:\*\* When
`interface/editor/single_window_mode<class_EditorSettings_property_interface/editor/single_window_mode>`{.interpreted-text
role="ref"} is `true`, the multi window support is always disabled.

\*\*Note:\*\* To query whether the editor can use multiple windows in an
editor plugin, use
`EditorInterface.is_multi_window_enabled()<class_EditorInterface_method_is_multi_window_enabled>`{.interpreted-text
role="ref"} instead of querying the value of this editor setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/multi_window/maximize_window}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/multi_window/maximize_window**
`🔗<class_EditorSettings_property_interface/multi_window/maximize_window>`{.interpreted-text
role="ref"}

If `true`, when panels are made floating they will be maximized.

If `false`, when panels are made floating their position and size will
match the ones when they are attached (excluding window border) to the
editor window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/multi_window/restore_windows_on_load}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/multi_window/restore_windows_on_load**
`🔗<class_EditorSettings_property_interface/multi_window/restore_windows_on_load>`{.interpreted-text
role="ref"}

If `true`, the floating panel position, size, and screen will be saved
on editor exit. On next launch the panels that were floating will be
made floating in the saved positions, sizes and screens, if possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/scene_tabs/display_close_button}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/scene_tabs/display_close_button**
`🔗<class_EditorSettings_property_interface/scene_tabs/display_close_button>`{.interpreted-text
role="ref"}

Controls when the Close (X) button is displayed on scene tabs at the top
of the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/scene_tabs/maximum_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/scene_tabs/maximum_width**
`🔗<class_EditorSettings_property_interface/scene_tabs/maximum_width>`{.interpreted-text
role="ref"}

The maximum width of each scene tab at the top editor (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/scene_tabs/restore_scenes_on_load}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/scene_tabs/restore_scenes_on_load**
`🔗<class_EditorSettings_property_interface/scene_tabs/restore_scenes_on_load>`{.interpreted-text
role="ref"}

If `true`, when a project is loaded, restores scenes that were opened on
the last editor session.

\*\*Note:\*\* With many opened scenes, the editor may take longer to
become usable. If starting the editor quickly is necessary, consider
setting this to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/scene_tabs/show_script_button}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/scene_tabs/show_script_button**
`🔗<class_EditorSettings_property_interface/scene_tabs/show_script_button>`{.interpreted-text
role="ref"}

If `true`, show a button next to each scene tab that opens the scene\'s
\"dominant\" script when clicked. The \"dominant\" script is the one
that is at the highest level in the scene\'s hierarchy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/scene_tabs/show_thumbnail_on_hover}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/scene_tabs/show_thumbnail_on_hover**
`🔗<class_EditorSettings_property_interface/scene_tabs/show_thumbnail_on_hover>`{.interpreted-text
role="ref"}

If `true`, display an automatically-generated thumbnail when hovering
scene tabs with the mouse. Scene thumbnails are generated when saving
the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/accent_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**interface/theme/accent_color**
`🔗<class_EditorSettings_property_interface/theme/accent_color>`{.interpreted-text
role="ref"}

The color to use for \"highlighted\" user interface elements in the
editor (pressed and hovered items).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/additional_spacing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/theme/additional_spacing**
`🔗<class_EditorSettings_property_interface/theme/additional_spacing>`{.interpreted-text
role="ref"}

The extra spacing to add to various GUI elements in the editor (in
pixels). Increasing this value is useful to improve usability on touch
screens, at the cost of reducing the amount of usable screen real
estate.

See also
`interface/theme/spacing_preset<class_EditorSettings_property_interface/theme/spacing_preset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/base_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**interface/theme/base_color**
`🔗<class_EditorSettings_property_interface/theme/base_color>`{.interpreted-text
role="ref"}

The base color to use for user interface elements in the editor.
Secondary colors (such as darker/lighter variants) are derived from this
color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/base_spacing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/theme/base_spacing**
`🔗<class_EditorSettings_property_interface/theme/base_spacing>`{.interpreted-text
role="ref"}

The base spacing used by various GUI elements in the editor (in pixels).
See also
`interface/theme/spacing_preset<class_EditorSettings_property_interface/theme/spacing_preset>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/border_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/theme/border_size**
`🔗<class_EditorSettings_property_interface/theme/border_size>`{.interpreted-text
role="ref"}

The border size to use for interface elements (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/contrast}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**interface/theme/contrast**
`🔗<class_EditorSettings_property_interface/theme/contrast>`{.interpreted-text
role="ref"}

The contrast factor to use when deriving the editor theme\'s base color
(see
`interface/theme/base_color<class_EditorSettings_property_interface/theme/base_color>`{.interpreted-text
role="ref"}). When using a positive values, the derived colors will be
*darker* than the base color. This contrast factor can be set to a
negative value, which will make the derived colors *brighter* than the
base color. Negative contrast rates often look better for light themes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/corner_radius}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/theme/corner_radius**
`🔗<class_EditorSettings_property_interface/theme/corner_radius>`{.interpreted-text
role="ref"}

The corner radius to use for interface elements (in pixels). `0` is
square.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/custom_theme}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/theme/custom_theme**
`🔗<class_EditorSettings_property_interface/theme/custom_theme>`{.interpreted-text
role="ref"}

The custom theme resource to use for the editor. Must be a Godot theme
resource in `.tres` or `.res` format.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/draw_extra_borders}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/theme/draw_extra_borders**
`🔗<class_EditorSettings_property_interface/theme/draw_extra_borders>`{.interpreted-text
role="ref"}

If `true`, draws additional borders around interactive UI elements in
the editor. This is automatically enabled when using the **Black
(OLED)** theme preset, as this theme preset uses a fully black
background.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/follow_system_theme}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/theme/follow_system_theme**
`🔗<class_EditorSettings_property_interface/theme/follow_system_theme>`{.interpreted-text
role="ref"}

If `true`, the editor theme preset will attempt to automatically match
the system theme.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/icon_and_font_color}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/theme/icon_and_font_color**
`🔗<class_EditorSettings_property_interface/theme/icon_and_font_color>`{.interpreted-text
role="ref"}

The icon and font color scheme to use in the editor.

- **Auto** determines the color scheme to use automatically based on
  `interface/theme/base_color<class_EditorSettings_property_interface/theme/base_color>`{.interpreted-text
  role="ref"}.
- **Dark** makes fonts and icons dark (suitable for light themes). Icon
  colors are automatically converted by the editor following the set of
  rules defined in [this
  file](https://github.com/godotengine/godot/blob/master/editor/themes/editor_theme_manager.cpp).
- **Light** makes fonts and icons light (suitable for dark themes).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/icon_saturation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**interface/theme/icon_saturation**
`🔗<class_EditorSettings_property_interface/theme/icon_saturation>`{.interpreted-text
role="ref"}

The saturation to use for editor icons. Higher values result in more
vibrant colors.

\*\*Note:\*\* The default editor icon saturation was increased by 30% in
Godot 4.0 and later. To get Godot 3.x\'s icon saturation back, set
`interface/theme/icon_saturation<class_EditorSettings_property_interface/theme/icon_saturation>`{.interpreted-text
role="ref"} to `0.77`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/preset}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/theme/preset**
`🔗<class_EditorSettings_property_interface/theme/preset>`{.interpreted-text
role="ref"}

The editor theme preset to use.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/relationship_line_opacity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**interface/theme/relationship_line_opacity**
`🔗<class_EditorSettings_property_interface/theme/relationship_line_opacity>`{.interpreted-text
role="ref"}

The opacity to use when drawing relationship lines in the editor\'s
`Tree<class_Tree>`{.interpreted-text role="ref"}-based GUIs (such as the
Scene tree dock).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/spacing_preset}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**interface/theme/spacing_preset**
`🔗<class_EditorSettings_property_interface/theme/spacing_preset>`{.interpreted-text
role="ref"}

The editor theme spacing preset to use. See also
`interface/theme/base_spacing<class_EditorSettings_property_interface/theme/base_spacing>`{.interpreted-text
role="ref"} and
`interface/theme/additional_spacing<class_EditorSettings_property_interface/theme/additional_spacing>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/theme/use_system_accent_color}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/theme/use_system_accent_color**
`🔗<class_EditorSettings_property_interface/theme/use_system_accent_color>`{.interpreted-text
role="ref"}

If `true`, set accent color based on system settings.

\*\*Note:\*\* This setting is only effective on Windows, MacOS, and
Android.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/touchscreen/enable_long_press_as_right_click}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/touchscreen/enable_long_press_as_right_click**
`🔗<class_EditorSettings_property_interface/touchscreen/enable_long_press_as_right_click>`{.interpreted-text
role="ref"}

If `true`, long press on touchscreen is treated as right click.

\*\*Note:\*\* Defaults to `true` on touchscreen devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/touchscreen/enable_pan_and_scale_gestures}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/touchscreen/enable_pan_and_scale_gestures**
`🔗<class_EditorSettings_property_interface/touchscreen/enable_pan_and_scale_gestures>`{.interpreted-text
role="ref"}

If `true`, enable two finger pan and scale gestures on touchscreen
devices.

\*\*Note:\*\* Defaults to `true` on touchscreen devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/touchscreen/enable_touch_optimizations}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**interface/touchscreen/enable_touch_optimizations**
`🔗<class_EditorSettings_property_interface/touchscreen/enable_touch_optimizations>`{.interpreted-text
role="ref"}

If `true`, increases the scrollbar touch area and enables a larger
dragger for split containers to improve usability on touchscreen devices

\*\*Note:\*\* Defaults to `true` on touchscreen devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/touchscreen/scale_gizmo_handles}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**interface/touchscreen/scale_gizmo_handles**
`🔗<class_EditorSettings_property_interface/touchscreen/scale_gizmo_handles>`{.interpreted-text
role="ref"}

Specify the multiplier to apply to the scale for the editor gizmo
handles to improve usability on touchscreen devices.

\*\*Note:\*\* Defaults to `1` on non-touchscreen devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_interface/touchscreen/touch_actions_panel}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**interface/touchscreen/touch_actions_panel**
`🔗<class_EditorSettings_property_interface/touchscreen/touch_actions_panel>`{.interpreted-text
role="ref"}

A touch-friendly panel that provides easy access to common actions such
as save, delete, undo, and redo without requiring a keyboard.

\*\*Note:\*\* Only available in the Android and XR editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/connection/check_for_updates}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/connection/check_for_updates**
`🔗<class_EditorSettings_property_network/connection/check_for_updates>`{.interpreted-text
role="ref"}

Specifies how the engine should check for updates.

- **Disable Update Checks** will block the engine from checking updates
  (see also
  `network/connection/network_mode<class_EditorSettings_property_network/connection/network_mode>`{.interpreted-text
  role="ref"}).
- **Check Newest Preview** (default for preview versions) will check for
  the newest available development snapshot.
- **Check Newest Stable** (default for stable versions) will check for
  the newest available stable version.
- **Check Newest Patch** will check for the latest available stable
  version, but only within the same minor version. E.g. if your version
  is `4.3.stable`, you will be notified about `4.3.1.stable`, but not
  `4.4.stable`.

All update modes will ignore builds with different major versions (e.g.
Godot 4 -\> Godot 5).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/connection/network_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/connection/network_mode**
`🔗<class_EditorSettings_property_network/connection/network_mode>`{.interpreted-text
role="ref"}

Determines whether online features are enabled in the editor, such as
the Asset Library or update checks. Disabling these online features
helps alleviate privacy concerns by preventing the editor from making
HTTP requests to the Godot website or third-party platforms hosting
assets from the Asset Library.

Editor plugins and tool scripts are recommended to follow this setting.
However, Godot can\'t prevent them from violating this rule.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/debug/remote_host}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**network/debug/remote_host**
`🔗<class_EditorSettings_property_network/debug/remote_host>`{.interpreted-text
role="ref"}

The address to listen to when starting the remote debugger. This can be
set to this device\'s local IP address to allow external clients to
connect to the remote debugger (instead of restricting the remote
debugger to connections from `localhost`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/debug/remote_port}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/debug/remote_port**
`🔗<class_EditorSettings_property_network/debug/remote_port>`{.interpreted-text
role="ref"}

The port to listen to when starting the remote debugger. Godot will try
to use port numbers above the configured number if the configured number
is already taken by another application.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/http_proxy/host}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**network/http_proxy/host**
`🔗<class_EditorSettings_property_network/http_proxy/host>`{.interpreted-text
role="ref"}

The host to use to contact the HTTP and HTTPS proxy in the editor (for
the asset library and export template downloads). See also
`network/http_proxy/port<class_EditorSettings_property_network/http_proxy/port>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Godot currently doesn\'t automatically use system proxy
settings, so you have to enter them manually here if needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/http_proxy/port}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**network/http_proxy/port**
`🔗<class_EditorSettings_property_network/http_proxy/port>`{.interpreted-text
role="ref"}

The port number to use to contact the HTTP and HTTPS proxy in the editor
(for the asset library and export template downloads). See also
`network/http_proxy/host<class_EditorSettings_property_network/http_proxy/host>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Godot currently doesn\'t automatically use system proxy
settings, so you have to enter them manually here if needed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/tls/editor_tls_certificates}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**network/tls/editor_tls_certificates**
`🔗<class_EditorSettings_property_network/tls/editor_tls_certificates>`{.interpreted-text
role="ref"}

The TLS certificate bundle to use for HTTP requests made within the
editor (e.g. from the AssetLib tab). If left empty, the [included
Mozilla certificate
bundle](https://github.com/godotengine/godot/blob/master/thirdparty/certs/ca-certificates.crt)
will be used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_network/tls/enable_tls_v1.3}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**network/tls/enable_tls_v1.3**
`🔗<class_EditorSettings_property_network/tls/enable_tls_v1.3>`{.interpreted-text
role="ref"}

If `true`, enable TLSv1.3 negotiation.

\*\*Note:\*\* Only supported when using Mbed TLS 3.0 or later (Linux
distribution packages may be compiled against older system Mbed TLS
packages), otherwise the maximum supported TLS version is always
TLSv1.2.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_project_manager/default_renderer}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**project_manager/default_renderer**
`🔗<class_EditorSettings_property_project_manager/default_renderer>`{.interpreted-text
role="ref"}

The renderer type that will be checked off by default when creating a
new project. Accepted strings are \"forward_plus\", \"mobile\" or
\"gl_compatibility\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_project_manager/directory_naming_convention}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**project_manager/directory_naming_convention**
`🔗<class_EditorSettings_property_project_manager/directory_naming_convention>`{.interpreted-text
role="ref"}

Directory naming convention for the project manager. Options are \"No
convention\" (project name is directory name), \"kebab-case\" (default),
\"snake_case\", \"camelCase\", \"PascalCase\", or \"Title Case\".

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_project_manager/sorting_order}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**project_manager/sorting_order**
`🔗<class_EditorSettings_property_project_manager/sorting_order>`{.interpreted-text
role="ref"}

The sorting order to use in the project manager. When changing the
sorting order in the project manager, this setting is set permanently in
the editor settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/auto_save/save_before_running}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**run/auto_save/save_before_running**
`🔗<class_EditorSettings_property_run/auto_save/save_before_running>`{.interpreted-text
role="ref"}

If `true`, saves all scenes and scripts automatically before running the
project. Setting this to `false` prevents the editor from saving if
there are no changes which can speed up the project startup slightly,
but it makes it possible to run a project that has unsaved changes.
(Unsaved changes will not be visible in the running project.)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/bottom_panel/action_on_play}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**run/bottom_panel/action_on_play**
`🔗<class_EditorSettings_property_run/bottom_panel/action_on_play>`{.interpreted-text
role="ref"}

The action to execute on the bottom panel when running the project.

\*\*Note:\*\* This option won\'t do anything if the bottom panel
switching is locked using the pin button in the corner of the bottom
panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/bottom_panel/action_on_stop}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**run/bottom_panel/action_on_stop**
`🔗<class_EditorSettings_property_run/bottom_panel/action_on_stop>`{.interpreted-text
role="ref"}

The action to execute on the bottom panel when stopping the project.

\*\*Note:\*\* This option won\'t do anything if the bottom panel
switching is locked using the pin button in the corner of the bottom
panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/output/always_clear_output_on_play}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**run/output/always_clear_output_on_play**
`🔗<class_EditorSettings_property_run/output/always_clear_output_on_play>`{.interpreted-text
role="ref"}

If `true`, the editor will clear the Output panel when running the
project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/output/font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **run/output/font_size**
`🔗<class_EditorSettings_property_run/output/font_size>`{.interpreted-text
role="ref"}

The size of the font in the **Output** panel at the bottom of the
editor. This setting does not impact the font size of the script editor
(see
`interface/editor/code_font_size<class_EditorSettings_property_interface/editor/code_font_size>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/output/max_lines}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **run/output/max_lines**
`🔗<class_EditorSettings_property_run/output/max_lines>`{.interpreted-text
role="ref"}

Maximum number of lines to show at any one time in the Output panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/platforms/linuxbsd/prefer_wayland}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**run/platforms/linuxbsd/prefer_wayland**
`🔗<class_EditorSettings_property_run/platforms/linuxbsd/prefer_wayland>`{.interpreted-text
role="ref"}

If `true`, on Linux/BSD, the editor will check for Wayland first instead
of X11 (if available).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/window_placement/android_window}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**run/window_placement/android_window**
`🔗<class_EditorSettings_property_run/window_placement/android_window>`{.interpreted-text
role="ref"}

Specifies how the Play window is launched relative to the Android
editor.

- **Auto (based on screen size)** (default) will automatically choose
  how to launch the Play window based on the device and screen metrics.
  Defaults to **Same as Editor** on phones and **Side-by-side with
  Editor** on tablets.
- **Same as Editor** will launch the Play window in the same window as
  the Editor.
- **Side-by-side with Editor** will launch the Play window side-by-side
  with the Editor window.

\*\*Note:\*\* Only available in the Android editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/window_placement/game_embed_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**run/window_placement/game_embed_mode**
`🔗<class_EditorSettings_property_run/window_placement/game_embed_mode>`{.interpreted-text
role="ref"}

Overrides game embedding setting for all newly opened projects. If
enabled, game embedding settings are not saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/window_placement/rect}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**run/window_placement/rect**
`🔗<class_EditorSettings_property_run/window_placement/rect>`{.interpreted-text
role="ref"}

The window mode to use to display the project when starting the project
from the editor.

\*\*Note:\*\* Game embedding is not available for **\"Force
Maximized\"** or **\"Force Fullscreen\"**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/window_placement/rect_custom_position}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**run/window_placement/rect_custom_position**
`🔗<class_EditorSettings_property_run/window_placement/rect_custom_position>`{.interpreted-text
role="ref"}

The custom position to use when starting the project from the editor (in
pixels from the top-left corner). Only effective if
`run/window_placement/rect<class_EditorSettings_property_run/window_placement/rect>`{.interpreted-text
role="ref"} is set to **Custom Position**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_run/window_placement/screen}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**run/window_placement/screen**
`🔗<class_EditorSettings_property_run/window_placement/screen>`{.interpreted-text
role="ref"}

The monitor to display the project on when starting the project from the
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/caret/caret_blink}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/caret/caret_blink**
`🔗<class_EditorSettings_property_text_editor/appearance/caret/caret_blink>`{.interpreted-text
role="ref"}

If `true`, makes the caret blink according to
`text_editor/appearance/caret/caret_blink_interval<class_EditorSettings_property_text_editor/appearance/caret/caret_blink_interval>`{.interpreted-text
role="ref"}. Disabling this setting can improve battery life on laptops
if you spend long amounts of time in the script editor, since it will
reduce the frequency at which the editor needs to be redrawn.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/caret/caret_blink_interval}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**text_editor/appearance/caret/caret_blink_interval**
`🔗<class_EditorSettings_property_text_editor/appearance/caret/caret_blink_interval>`{.interpreted-text
role="ref"}

The interval at which the caret will blink (in seconds). See also
`text_editor/appearance/caret/caret_blink<class_EditorSettings_property_text_editor/appearance/caret/caret_blink>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/caret/highlight_all_occurrences}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/caret/highlight_all_occurrences**
`🔗<class_EditorSettings_property_text_editor/appearance/caret/highlight_all_occurrences>`{.interpreted-text
role="ref"}

If `true`, highlights all occurrences of the currently selected text in
the script editor. See also
`text_editor/theme/highlighting/word_highlighted_color<class_EditorSettings_property_text_editor/theme/highlighting/word_highlighted_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/caret/highlight_current_line}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/caret/highlight_current_line**
`🔗<class_EditorSettings_property_text_editor/appearance/caret/highlight_current_line>`{.interpreted-text
role="ref"}

If `true`, colors the background of the line the caret is currently on
with
`text_editor/theme/highlighting/current_line_color<class_EditorSettings_property_text_editor/theme/highlighting/current_line_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/caret/type}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/appearance/caret/type**
`🔗<class_EditorSettings_property_text_editor/appearance/caret/type>`{.interpreted-text
role="ref"}

The shape of the caret to use in the script editor. **Line** displays a
vertical line to the left of the current character, whereas **Block**
displays an outline over the current character.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/enable_inline_color_picker}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/enable_inline_color_picker**
`🔗<class_EditorSettings_property_text_editor/appearance/enable_inline_color_picker>`{.interpreted-text
role="ref"}

If `true`, displays a colored button before any
`Color<class_Color>`{.interpreted-text role="ref"} constructor in the
script editor. Clicking on them allows the color to be modified through
a color picker.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_hard_column}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/appearance/guidelines/line_length_guideline_hard_column**
`🔗<class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_hard_column>`{.interpreted-text
role="ref"}

The column at which to display a subtle line as a line length guideline
for scripts. This should generally be greater than
`text_editor/appearance/guidelines/line_length_guideline_soft_column<class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_soft_column>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_soft_column}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/appearance/guidelines/line_length_guideline_soft_column**
`🔗<class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_soft_column>`{.interpreted-text
role="ref"}

The column at which to display a *very* subtle line as a line length
guideline for scripts. This should generally be lower than
`text_editor/appearance/guidelines/line_length_guideline_hard_column<class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_hard_column>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/guidelines/show_line_length_guidelines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/guidelines/show_line_length_guidelines**
`🔗<class_EditorSettings_property_text_editor/appearance/guidelines/show_line_length_guidelines>`{.interpreted-text
role="ref"}

If `true`, displays line length guidelines to help you keep line lengths
in check. See also
`text_editor/appearance/guidelines/line_length_guideline_soft_column<class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_soft_column>`{.interpreted-text
role="ref"} and
`text_editor/appearance/guidelines/line_length_guideline_hard_column<class_EditorSettings_property_text_editor/appearance/guidelines/line_length_guideline_hard_column>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/gutters/highlight_type_safe_lines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/gutters/highlight_type_safe_lines**
`🔗<class_EditorSettings_property_text_editor/appearance/gutters/highlight_type_safe_lines>`{.interpreted-text
role="ref"}

If `true`, highlights type-safe lines by displaying their line number
color with
`text_editor/theme/highlighting/safe_line_number_color<class_EditorSettings_property_text_editor/theme/highlighting/safe_line_number_color>`{.interpreted-text
role="ref"} instead of
`text_editor/theme/highlighting/line_number_color<class_EditorSettings_property_text_editor/theme/highlighting/line_number_color>`{.interpreted-text
role="ref"}. Type-safe lines are lines of code where the type of all
variables is known at compile-time. These type-safe lines may run faster
thanks to typed instructions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/gutters/line_numbers_zero_padded}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/gutters/line_numbers_zero_padded**
`🔗<class_EditorSettings_property_text_editor/appearance/gutters/line_numbers_zero_padded>`{.interpreted-text
role="ref"}

If `true`, displays line numbers with zero padding (e.g. `007` instead
of `7`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/gutters/show_info_gutter}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/gutters/show_info_gutter**
`🔗<class_EditorSettings_property_text_editor/appearance/gutters/show_info_gutter>`{.interpreted-text
role="ref"}

If `true`, displays a gutter at the left containing icons for methods
with signal connections and for overridden methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/gutters/show_line_numbers}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/gutters/show_line_numbers**
`🔗<class_EditorSettings_property_text_editor/appearance/gutters/show_line_numbers>`{.interpreted-text
role="ref"}

If `true`, displays line numbers in a gutter at the left.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/lines/autowrap_mode}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/appearance/lines/autowrap_mode**
`🔗<class_EditorSettings_property_text_editor/appearance/lines/autowrap_mode>`{.interpreted-text
role="ref"}

If
`text_editor/appearance/lines/word_wrap<class_EditorSettings_property_text_editor/appearance/lines/word_wrap>`{.interpreted-text
role="ref"} is set to `1`, sets text wrapping mode. To see how each mode
behaves, see
`AutowrapMode<enum_TextServer_AutowrapMode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/lines/code_folding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/lines/code_folding**
`🔗<class_EditorSettings_property_text_editor/appearance/lines/code_folding>`{.interpreted-text
role="ref"}

If `true`, displays the folding arrows next to indented code sections
and allows code folding. If `false`, hides the folding arrows next to
indented code sections and disallows code folding.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/lines/word_wrap}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/appearance/lines/word_wrap**
`🔗<class_EditorSettings_property_text_editor/appearance/lines/word_wrap>`{.interpreted-text
role="ref"}

If `true`, wraps long lines over multiple lines to avoid horizontal
scrolling. This is a display-only feature; it does not actually insert
line breaks in your scripts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/minimap/minimap_width}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/appearance/minimap/minimap_width**
`🔗<class_EditorSettings_property_text_editor/appearance/minimap/minimap_width>`{.interpreted-text
role="ref"}

The width of the minimap in the script editor (in pixels).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/minimap/show_minimap}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/minimap/show_minimap**
`🔗<class_EditorSettings_property_text_editor/appearance/minimap/show_minimap>`{.interpreted-text
role="ref"}

If `true`, draws an overview of the script near the scroll bar. The
minimap can be left-clicked to scroll directly to a location in an
\"absolute\" manner.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/whitespace/draw_spaces}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/whitespace/draw_spaces**
`🔗<class_EditorSettings_property_text_editor/appearance/whitespace/draw_spaces>`{.interpreted-text
role="ref"}

If `true`, draws space characters as centered points.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/whitespace/draw_tabs}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/appearance/whitespace/draw_tabs**
`🔗<class_EditorSettings_property_text_editor/appearance/whitespace/draw_tabs>`{.interpreted-text
role="ref"}

If `true`, draws tab characters as chevrons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/appearance/whitespace/line_spacing}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/appearance/whitespace/line_spacing**
`🔗<class_EditorSettings_property_text_editor/appearance/whitespace/line_spacing>`{.interpreted-text
role="ref"}

The space to add between lines (in pixels). Greater line spacing can
help improve readability at the cost of displaying fewer lines on
screen.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/documentation/enable_tooltips}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/documentation/enable_tooltips**
`🔗<class_EditorSettings_property_text_editor/behavior/documentation/enable_tooltips>`{.interpreted-text
role="ref"}

If `true`, documentation tooltips will appear when hovering over a
symbol.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/auto_reload_and_parse_scripts_on_save}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/auto_reload_and_parse_scripts_on_save**
`🔗<class_EditorSettings_property_text_editor/behavior/files/auto_reload_and_parse_scripts_on_save>`{.interpreted-text
role="ref"}

If `true`, tool scripts will be automatically soft-reloaded after they
are saved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/auto_reload_scripts_on_external_change}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/auto_reload_scripts_on_external_change**
`🔗<class_EditorSettings_property_text_editor/behavior/files/auto_reload_scripts_on_external_change>`{.interpreted-text
role="ref"}

If `true`, automatically reloads scripts and text-based shaders in the
editor when they have been modified and saved by external editors or
tools and the editor regains focus. External changes can be discarded by
using the Undo function after they\'ve been loaded in the editor.

If `false`, a file conflict dialog will always be displayed when the
editor regains focus. This dialog allows you to choose whether to keep
local changes or discard them.

\*\*Note:\*\* Even when this setting is `true`, a file conflict dialog
is still displayed in certain situations. For instance, it will display
when the script editor has unsaved changes that the external editor did
not account for.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/autosave_interval_secs}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/behavior/files/autosave_interval_secs**
`🔗<class_EditorSettings_property_text_editor/behavior/files/autosave_interval_secs>`{.interpreted-text
role="ref"}

If set to a value greater than `0`, automatically saves the current
script following the specified interval (in seconds). This can be used
to prevent data loss if the editor crashes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/convert_indent_on_save}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/convert_indent_on_save**
`🔗<class_EditorSettings_property_text_editor/behavior/files/convert_indent_on_save>`{.interpreted-text
role="ref"}

If `true`, converts indentation to match the script editor\'s
indentation settings when saving a script. See also
`text_editor/behavior/indent/type<class_EditorSettings_property_text_editor/behavior/indent/type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/drop_preload_resources_as_uid}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/drop_preload_resources_as_uid**
`🔗<class_EditorSettings_property_text_editor/behavior/files/drop_preload_resources_as_uid>`{.interpreted-text
role="ref"}

If `true`, when dropping a `Resource<class_Resource>`{.interpreted-text
role="ref"} file to script editor while `Ctrl`{.interpreted-text
role="kbd"} is held, the resource will be preloaded with a UID. If
`false`, the resource will be preloaded with a path.

When you hold `Ctrl+Shift`{.interpreted-text role="kbd"}, the behavior
is reversed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/open_dominant_script_on_scene_change}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/open_dominant_script_on_scene_change**
`🔗<class_EditorSettings_property_text_editor/behavior/files/open_dominant_script_on_scene_change>`{.interpreted-text
role="ref"}

If `true`, opening a scene automatically opens the script attached to
the root node, or the topmost node if the root has no script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/restore_scripts_on_load}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/restore_scripts_on_load**
`🔗<class_EditorSettings_property_text_editor/behavior/files/restore_scripts_on_load>`{.interpreted-text
role="ref"}

If `true`, reopens scripts that were opened in the last session when the
editor is reopened on a given project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/trim_final_newlines_on_save}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/trim_final_newlines_on_save**
`🔗<class_EditorSettings_property_text_editor/behavior/files/trim_final_newlines_on_save>`{.interpreted-text
role="ref"}

If `true`, trims all empty newlines after the final newline when saving
a script. Final newlines refer to the empty newlines found at the end of
files. Since these serve no practical purpose, they can and should be
removed to make version control diffs less noisy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/files/trim_trailing_whitespace_on_save}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/files/trim_trailing_whitespace_on_save**
`🔗<class_EditorSettings_property_text_editor/behavior/files/trim_trailing_whitespace_on_save>`{.interpreted-text
role="ref"}

If `true`, trims trailing whitespace when saving a script. Trailing
whitespace refers to tab and space characters placed at the end of
lines. Since these serve no practical purpose, they can and should be
removed to make version control diffs less noisy.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/general/empty_selection_clipboard}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/general/empty_selection_clipboard**
`🔗<class_EditorSettings_property_text_editor/behavior/general/empty_selection_clipboard>`{.interpreted-text
role="ref"}

If `true`, copying or cutting without a selection is performed on all
lines with a caret. Otherwise, copy and cut require a selection.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/indent/auto_indent}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/indent/auto_indent**
`🔗<class_EditorSettings_property_text_editor/behavior/indent/auto_indent>`{.interpreted-text
role="ref"}

If `true`, automatically indents code when pressing the
`Enter`{.interpreted-text role="kbd"} key based on blocks above the new
line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/indent/indent_wrapped_lines}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/indent/indent_wrapped_lines**
`🔗<class_EditorSettings_property_text_editor/behavior/indent/indent_wrapped_lines>`{.interpreted-text
role="ref"}

If `true`, all wrapped lines are indented to the same amount as the
unwrapped line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/indent/size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/behavior/indent/size**
`🔗<class_EditorSettings_property_text_editor/behavior/indent/size>`{.interpreted-text
role="ref"}

When using tab indentation, determines the length of each tab. When
using space indentation, determines how many spaces are inserted when
pressing `Tab`{.interpreted-text role="kbd"} and when automatic
indentation is performed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/indent/type}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/behavior/indent/type**
`🔗<class_EditorSettings_property_text_editor/behavior/indent/type>`{.interpreted-text
role="ref"}

The indentation style to use (tabs or spaces).

\*\*Note:\*\* The
`GDScript style guide <../tutorials/scripting/gdscript/gdscript_styleguide>`{.interpreted-text
role="doc"} recommends using tabs for indentation. It is advised to
change this setting only if you need to work on a project that currently
uses spaces for indentation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/custom_word_separators}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/custom_word_separators**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/custom_word_separators>`{.interpreted-text
role="ref"}

The characters to consider as word delimiters if
`text_editor/behavior/navigation/use_custom_word_separators<class_EditorSettings_property_text_editor/behavior/navigation/use_custom_word_separators>`{.interpreted-text
role="ref"} is `true`. This is in addition to default characters if
`text_editor/behavior/navigation/use_default_word_separators<class_EditorSettings_property_text_editor/behavior/navigation/use_default_word_separators>`{.interpreted-text
role="ref"} is `true`. The characters should be defined without
separation, for example `_♥=`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/drag_and_drop_selection}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/drag_and_drop_selection**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/drag_and_drop_selection>`{.interpreted-text
role="ref"}

If `true`, allows drag-and-dropping text in the script editor to move
text. Disable this if you find yourself accidentally drag-and-dropping
text in the script editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/move_caret_on_right_click}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/move_caret_on_right_click**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/move_caret_on_right_click>`{.interpreted-text
role="ref"}

If `true`, the caret will be moved when right-clicking somewhere in the
script editor (like when left-clicking or middle-clicking). If `false`,
the caret will only be moved when left-clicking or middle-clicking
somewhere.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/open_script_when_connecting_signal_to_existing_method}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/open_script_when_connecting_signal_to_existing_method**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/open_script_when_connecting_signal_to_existing_method>`{.interpreted-text
role="ref"}

If `true`, opens the script editor when connecting a signal to an
existing script method from the Node dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/scroll_past_end_of_file}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/scroll_past_end_of_file**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/scroll_past_end_of_file>`{.interpreted-text
role="ref"}

If `true`, allows scrolling past the end of the file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/smooth_scrolling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/smooth_scrolling**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/smooth_scrolling>`{.interpreted-text
role="ref"}

If `true`, enables a smooth scrolling animation when using the mouse
wheel to scroll. See
`text_editor/behavior/navigation/v_scroll_speed<class_EditorSettings_property_text_editor/behavior/navigation/v_scroll_speed>`{.interpreted-text
role="ref"} for the speed of this animation.

\*\*Note:\*\*
`text_editor/behavior/navigation/smooth_scrolling<class_EditorSettings_property_text_editor/behavior/navigation/smooth_scrolling>`{.interpreted-text
role="ref"} currently behaves poorly in projects where
`ProjectSettings.physics/common/physics_ticks_per_second<class_ProjectSettings_property_physics/common/physics_ticks_per_second>`{.interpreted-text
role="ref"} has been increased significantly from its default value
(`60`). In this case, it is recommended to disable this setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/stay_in_script_editor_on_node_selected}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/stay_in_script_editor_on_node_selected**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/stay_in_script_editor_on_node_selected>`{.interpreted-text
role="ref"}

If `true`, prevents automatically switching between the Script and 2D/3D
screens when selecting a node in the Scene tree dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/use_custom_word_separators}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/use_custom_word_separators**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/use_custom_word_separators>`{.interpreted-text
role="ref"}

If `true`, uses the characters in
`text_editor/behavior/navigation/custom_word_separators<class_EditorSettings_property_text_editor/behavior/navigation/custom_word_separators>`{.interpreted-text
role="ref"} as word separators for word navigation and operations. This
is in addition to the default characters if
`text_editor/behavior/navigation/use_default_word_separators<class_EditorSettings_property_text_editor/behavior/navigation/use_default_word_separators>`{.interpreted-text
role="ref"} is also enabled. Word navigation and operations include
double-clicking on a word or holding `Ctrl`{.interpreted-text
role="kbd"} (`Cmd`{.interpreted-text role="kbd"} on macOS) while
pressing `left`{.interpreted-text role="kbd"}, `right`{.interpreted-text
role="kbd"}, `backspace`{.interpreted-text role="kbd"}, or
`delete`{.interpreted-text role="kbd"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/use_default_word_separators}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/use_default_word_separators**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/use_default_word_separators>`{.interpreted-text
role="ref"}

If `true`, uses the characters in
`` `!"#$%&'()*+,-./:;<=>?@[\]^`{|}~ ``, the Unicode General Punctuation
table, and the Unicode CJK Punctuation table as word separators for word
navigation and operations. If `false`, a subset of these characters are
used and does not include the characters `<>$~^=+|`. This is in addition
to custom characters if
`text_editor/behavior/navigation/use_custom_word_separators<class_EditorSettings_property_text_editor/behavior/navigation/use_custom_word_separators>`{.interpreted-text
role="ref"} is also enabled. These characters are used to determine
where a word stops. Word navigation and operations include
double-clicking on a word or holding `Ctrl`{.interpreted-text
role="kbd"} (`Cmd`{.interpreted-text role="kbd"} on macOS) while
pressing `left`{.interpreted-text role="kbd"}, `right`{.interpreted-text
role="kbd"}, `backspace`{.interpreted-text role="kbd"}, or
`delete`{.interpreted-text role="kbd"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/behavior/navigation/v_scroll_speed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/behavior/navigation/v_scroll_speed**
`🔗<class_EditorSettings_property_text_editor/behavior/navigation/v_scroll_speed>`{.interpreted-text
role="ref"}

The speed of scrolling in lines per second when
`text_editor/behavior/navigation/smooth_scrolling<class_EditorSettings_property_text_editor/behavior/navigation/smooth_scrolling>`{.interpreted-text
role="ref"} is `true`. Higher values make the script scroll by faster
when using the mouse wheel.

\*\*Note:\*\* You can hold down `Alt`{.interpreted-text role="kbd"}
while using the mouse wheel to temporarily scroll 5 times faster.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/add_node_path_literals}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/add_node_path_literals**
`🔗<class_EditorSettings_property_text_editor/completion/add_node_path_literals>`{.interpreted-text
role="ref"}

If `true`, uses `NodePath<class_NodePath>`{.interpreted-text role="ref"}
instead of `String<class_String>`{.interpreted-text role="ref"} when
appropriate for code autocompletion or for drag and dropping object
properties into the script editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/add_string_name_literals}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/add_string_name_literals**
`🔗<class_EditorSettings_property_text_editor/completion/add_string_name_literals>`{.interpreted-text
role="ref"}

If `true`, uses `StringName<class_StringName>`{.interpreted-text
role="ref"} instead of `String<class_String>`{.interpreted-text
role="ref"} when appropriate for code autocompletion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/add_type_hints}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/add_type_hints**
`🔗<class_EditorSettings_property_text_editor/completion/add_type_hints>`{.interpreted-text
role="ref"}

If `true`, automatically adds
`GDScript static typing <../tutorials/scripting/gdscript/static_typing>`{.interpreted-text
role="doc"} (such as `-> void` and `: int`) in many situations where
it\'s possible to, including when:

- Accepting a suggestion from code autocompletion;
- Creating a new script from a template;
- Connecting signals from the Node dock;
- Creating variables prefixed with
  `@GDScript.@onready<class_@GDScript_annotation_@onready>`{.interpreted-text
  role="ref"}, by dropping nodes from the Scene dock into the script
  editor while holding `Ctrl`{.interpreted-text role="kbd"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/auto_brace_complete}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/auto_brace_complete**
`🔗<class_EditorSettings_property_text_editor/completion/auto_brace_complete>`{.interpreted-text
role="ref"}

If `true`, automatically inserts the matching closing brace when the
opening brace is inserted by typing or autocompletion. Also
automatically removes the closing brace when pressing
`Backspace`{.interpreted-text role="kbd"} on the opening brace. This
includes brackets (`()`, `[]`, `{}`), string quotation marks (`''`,
`""`), and comments (`/**/`) if the language supports it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/code_complete_delay}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**text_editor/completion/code_complete_delay**
`🔗<class_EditorSettings_property_text_editor/completion/code_complete_delay>`{.interpreted-text
role="ref"}

The delay in seconds after which autocompletion suggestions should be
displayed when the user stops typing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/code_complete_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/code_complete_enabled**
`🔗<class_EditorSettings_property_text_editor/completion/code_complete_enabled>`{.interpreted-text
role="ref"}

If `true`, code completion will be triggered automatically after
`text_editor/completion/code_complete_delay<class_EditorSettings_property_text_editor/completion/code_complete_delay>`{.interpreted-text
role="ref"}. Even if `false`, code completion can be triggered manually
with the `ui_text_completion_query` action (by default
`Ctrl + Space`{.interpreted-text role="kbd"} or
`Cmd + Space`{.interpreted-text role="kbd"} on macOS).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/colorize_suggestions}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/colorize_suggestions**
`🔗<class_EditorSettings_property_text_editor/completion/colorize_suggestions>`{.interpreted-text
role="ref"}

If `true` enables the coloring for some items in the autocompletion
suggestions, like vector components.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/complete_file_paths}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/complete_file_paths**
`🔗<class_EditorSettings_property_text_editor/completion/complete_file_paths>`{.interpreted-text
role="ref"}

If `true`, provides autocompletion suggestions for file paths in methods
such as `load()` and `preload()`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/idle_parse_delay}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**text_editor/completion/idle_parse_delay**
`🔗<class_EditorSettings_property_text_editor/completion/idle_parse_delay>`{.interpreted-text
role="ref"}

The delay in seconds after which the script editor should check for
errors when the user stops typing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/idle_parse_delay_with_errors_found}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**text_editor/completion/idle_parse_delay_with_errors_found**
`🔗<class_EditorSettings_property_text_editor/completion/idle_parse_delay_with_errors_found>`{.interpreted-text
role="ref"}

The delay used instead of
`text_editor/completion/idle_parse_delay<class_EditorSettings_property_text_editor/completion/idle_parse_delay>`{.interpreted-text
role="ref"}, when the parser has found errors. A lower value should feel
more responsive while fixing code, but may cause notable stuttering and
increase CPU usage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/put_callhint_tooltip_below_current_line}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/put_callhint_tooltip_below_current_line**
`🔗<class_EditorSettings_property_text_editor/completion/put_callhint_tooltip_below_current_line>`{.interpreted-text
role="ref"}

If `true`, the code completion tooltip will appear below the current
line unless there is no space on screen below the current line. If
`false`, the code completion tooltip will appear above the current line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/completion/use_single_quotes}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/completion/use_single_quotes**
`🔗<class_EditorSettings_property_text_editor/completion/use_single_quotes>`{.interpreted-text
role="ref"}

If `true`, performs string autocompletion with single quotes. If
`false`, performs string autocompletion with double quotes (which
matches the
`GDScript style guide <../tutorials/scripting/gdscript/gdscript_styleguide>`{.interpreted-text
role="doc"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/external/exec_flags}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**text_editor/external/exec_flags**
`🔗<class_EditorSettings_property_text_editor/external/exec_flags>`{.interpreted-text
role="ref"}

The command-line arguments to pass to the external text editor that is
run when
`text_editor/external/use_external_editor<class_EditorSettings_property_text_editor/external/use_external_editor>`{.interpreted-text
role="ref"} is `true`. See also
`text_editor/external/exec_path<class_EditorSettings_property_text_editor/external/exec_path>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/external/exec_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**text_editor/external/exec_path**
`🔗<class_EditorSettings_property_text_editor/external/exec_path>`{.interpreted-text
role="ref"}

The path to the text editor executable used to edit text files if
`text_editor/external/use_external_editor<class_EditorSettings_property_text_editor/external/use_external_editor>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/external/use_external_editor}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/external/use_external_editor**
`🔗<class_EditorSettings_property_text_editor/external/use_external_editor>`{.interpreted-text
role="ref"}

If `true`, uses an external editor instead of the built-in Script
Editor. See also
`text_editor/external/exec_path<class_EditorSettings_property_text_editor/external/exec_path>`{.interpreted-text
role="ref"} and
`text_editor/external/exec_flags<class_EditorSettings_property_text_editor/external/exec_flags>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/help/class_reference_examples}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/help/class_reference_examples**
`🔗<class_EditorSettings_property_text_editor/help/class_reference_examples>`{.interpreted-text
role="ref"}

Controls which multi-line code blocks should be displayed in the editor
help. This setting does not affect single-line code literals in the
editor help.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/help/help_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/help/help_font_size**
`🔗<class_EditorSettings_property_text_editor/help/help_font_size>`{.interpreted-text
role="ref"}

The font size to use for the editor help (built-in class reference).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/help/help_source_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/help/help_source_font_size**
`🔗<class_EditorSettings_property_text_editor/help/help_source_font_size>`{.interpreted-text
role="ref"}

The font size to use for code samples in the editor help (built-in class
reference).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/help/help_title_font_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/help/help_title_font_size**
`🔗<class_EditorSettings_property_text_editor/help/help_title_font_size>`{.interpreted-text
role="ref"}

The font size to use for headings in the editor help (built-in class
reference).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/help/show_help_index}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/help/show_help_index**
`🔗<class_EditorSettings_property_text_editor/help/show_help_index>`{.interpreted-text
role="ref"}

If `true`, displays a table of contents at the left of the editor help
(at the location where the members overview would appear when editing a
script).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/help/sort_functions_alphabetically}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/help/sort_functions_alphabetically**
`🔗<class_EditorSettings_property_text_editor/help/sort_functions_alphabetically>`{.interpreted-text
role="ref"}

If `true`, the script\'s method list in the Script Editor is sorted
alphabetically.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/group_help_pages}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/script_list/group_help_pages**
`🔗<class_EditorSettings_property_text_editor/script_list/group_help_pages>`{.interpreted-text
role="ref"}

If `true`, class reference pages are grouped together at the bottom of
the Script Editor\'s script list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/highlight_scene_scripts}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/script_list/highlight_scene_scripts**
`🔗<class_EditorSettings_property_text_editor/script_list/highlight_scene_scripts>`{.interpreted-text
role="ref"}

If `true`, the scripts that are used by the current scene are
highlighted in the Script Editor\'s script list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/list_script_names_as}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/script_list/list_script_names_as**
`🔗<class_EditorSettings_property_text_editor/script_list/list_script_names_as>`{.interpreted-text
role="ref"}

Specifies how script paths should be displayed in Script Editor\'s
script list. If using the \"Name\" option and some scripts share the
same file name, more parts of their paths are revealed to avoid
conflicts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/script_temperature_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/script_list/script_temperature_enabled**
`🔗<class_EditorSettings_property_text_editor/script_list/script_temperature_enabled>`{.interpreted-text
role="ref"}

If `true`, the names of recently opened scripts in the Script Editor are
highlighted with the accent color, with its intensity based on how
recently they were opened.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/script_temperature_history_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/script_list/script_temperature_history_size**
`🔗<class_EditorSettings_property_text_editor/script_list/script_temperature_history_size>`{.interpreted-text
role="ref"}

How many script names can be highlighted at most, if
`text_editor/script_list/script_temperature_enabled<class_EditorSettings_property_text_editor/script_list/script_temperature_enabled>`{.interpreted-text
role="ref"} is `true`. Scripts older than this value use the default
font color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/show_members_overview}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/script_list/show_members_overview**
`🔗<class_EditorSettings_property_text_editor/script_list/show_members_overview>`{.interpreted-text
role="ref"}

If `true`, displays an overview of the current script\'s member
variables and functions at the left of the script editor. See also
`text_editor/script_list/sort_members_outline_alphabetically<class_EditorSettings_property_text_editor/script_list/sort_members_outline_alphabetically>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/sort_members_outline_alphabetically}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**text_editor/script_list/sort_members_outline_alphabetically**
`🔗<class_EditorSettings_property_text_editor/script_list/sort_members_outline_alphabetically>`{.interpreted-text
role="ref"}

If `true`, sorts the members outline (located at the left of the script
editor) using alphabetical order. If `false`, sorts the members outline
depending on the order in which members are found in the script.

\*\*Note:\*\* Only effective if
`text_editor/script_list/show_members_overview<class_EditorSettings_property_text_editor/script_list/show_members_overview>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/script_list/sort_scripts_by}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**text_editor/script_list/sort_scripts_by**
`🔗<class_EditorSettings_property_text_editor/script_list/sort_scripts_by>`{.interpreted-text
role="ref"}

Specifies sorting used for Script Editor\'s open script list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/color_theme}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**text_editor/theme/color_theme**
`🔗<class_EditorSettings_property_text_editor/theme/color_theme>`{.interpreted-text
role="ref"}

The syntax theme to use in the script editor.

You can save your own syntax theme from your current settings by using
**File \> Theme \> Save As\...** at the top of the script editor. The
syntax theme will then be available locally in the list of color themes.

You can find additional syntax themes to install in the
[godot-syntax-themes](https://github.com/godotengine/godot-syntax-themes)
repository.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/background_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/background_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/background_color>`{.interpreted-text
role="ref"}

The script editor\'s background color. If set to a translucent color,
the editor theme\'s base color will be visible behind.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/base_type_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/base_type_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/base_type_color>`{.interpreted-text
role="ref"}

The script editor\'s base type color (used for types like
`Vector2<class_Vector2>`{.interpreted-text role="ref"},
`Vector3<class_Vector3>`{.interpreted-text role="ref"},
`Color<class_Color>`{.interpreted-text role="ref"}, \...).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/bookmark_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/bookmark_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/bookmark_color>`{.interpreted-text
role="ref"}

The script editor\'s bookmark icon color (displayed in the gutter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/brace_mismatch_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/brace_mismatch_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/brace_mismatch_color>`{.interpreted-text
role="ref"}

The script editor\'s brace mismatch color. Used when the caret is
currently on a mismatched brace, parenthesis or bracket character.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/breakpoint_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/breakpoint_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/breakpoint_color>`{.interpreted-text
role="ref"}

The script editor\'s breakpoint icon color (displayed in the gutter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/caret_background_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/caret_background_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/caret_background_color>`{.interpreted-text
role="ref"}

The script editor\'s caret background color.

\*\*Note:\*\* This setting has no effect as it\'s currently unused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/caret_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/caret_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/caret_color>`{.interpreted-text
role="ref"}

The script editor\'s caret color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/code_folding_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/code_folding_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/code_folding_color>`{.interpreted-text
role="ref"}

The script editor\'s color for the code folding icon (displayed in the
gutter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/comment_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/comment_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/comment_color>`{.interpreted-text
role="ref"}

The script editor\'s comment color.

\*\*Note:\*\* In GDScript, unlike Python, multiline strings are not
considered to be comments, and will use the string highlighting color
instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/critical_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/comment_markers/critical_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/critical_color>`{.interpreted-text
role="ref"}

The script editor\'s critical comment marker text color. These markers
are determined by
`text_editor/theme/highlighting/comment_markers/critical_list<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/critical_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/critical_list}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/comment_markers/critical_list**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/critical_list>`{.interpreted-text
role="ref"}

A comma-separated list of case-sensitive words to highlight in comments.
The text will be highlighted in the script editor with the
`text_editor/theme/highlighting/comment_markers/critical_color<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/critical_color>`{.interpreted-text
role="ref"} color. These must not include spaces or symbols or they will
not be highlighted.

\*\*Note:\*\* This is only implemented in the GDScript syntax
highlighter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/notice_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/comment_markers/notice_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/notice_color>`{.interpreted-text
role="ref"}

The script editor\'s notice comment marker text color. These markers are
determined by
`text_editor/theme/highlighting/comment_markers/notice_list<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/notice_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/notice_list}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/comment_markers/notice_list**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/notice_list>`{.interpreted-text
role="ref"}

A comma-separated list of case-sensitive words to highlight in comments.
The text will be highlighted in the script editor with the
`text_editor/theme/highlighting/comment_markers/notice_color<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/notice_color>`{.interpreted-text
role="ref"} color. These must not include spaces or symbols or they will
not be highlighted.

\*\*Note:\*\* This is only implemented in the GDScript syntax
highlighter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/warning_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/comment_markers/warning_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/warning_color>`{.interpreted-text
role="ref"}

The script editor\'s warning comment marker text color. These markers
are determined by
`text_editor/theme/highlighting/comment_markers/warning_list<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/warning_list>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/warning_list}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/comment_markers/warning_list**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/warning_list>`{.interpreted-text
role="ref"}

A comma-separated list of case-sensitive words to highlight in comments.
The text will be highlighted in the script editor with the
`text_editor/theme/highlighting/comment_markers/warning_color<class_EditorSettings_property_text_editor/theme/highlighting/comment_markers/warning_color>`{.interpreted-text
role="ref"} color. These must not include spaces or symbols or they will
not be highlighted.

\*\*Note:\*\* This is only implemented in the GDScript syntax
highlighter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/completion_background_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/completion_background_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/completion_background_color>`{.interpreted-text
role="ref"}

The script editor\'s autocompletion box background color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/completion_existing_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/completion_existing_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/completion_existing_color>`{.interpreted-text
role="ref"}

The script editor\'s autocompletion box background color to highlight
existing characters in the completion results. This should be a
translucent color so that
`text_editor/theme/highlighting/completion_selected_color<class_EditorSettings_property_text_editor/theme/highlighting/completion_selected_color>`{.interpreted-text
role="ref"} can be seen behind.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/completion_font_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/completion_font_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/completion_font_color>`{.interpreted-text
role="ref"}

The script editor\'s autocompletion box text color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/completion_scroll_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/completion_scroll_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/completion_scroll_color>`{.interpreted-text
role="ref"}

The script editor\'s autocompletion box scroll bar color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/completion_scroll_hovered_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/completion_scroll_hovered_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/completion_scroll_hovered_color>`{.interpreted-text
role="ref"}

The script editor\'s autocompletion box scroll bar color when hovered or
pressed with the mouse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/completion_selected_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/completion_selected_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/completion_selected_color>`{.interpreted-text
role="ref"}

The script editor\'s autocompletion box background color for the
currently selected line.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/control_flow_keyword_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/control_flow_keyword_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/control_flow_keyword_color>`{.interpreted-text
role="ref"}

The script editor\'s control flow keyword color (used for keywords like
`if`, `for`, `return`, \...).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/current_line_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/current_line_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/current_line_color>`{.interpreted-text
role="ref"}

The script editor\'s background color for the line the caret is
currently on. This should be set to a translucent color so that it can
display on top of other line color modifiers such as
`text_editor/theme/highlighting/mark_color<class_EditorSettings_property_text_editor/theme/highlighting/mark_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/doc_comment_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/doc_comment_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/doc_comment_color>`{.interpreted-text
role="ref"}

The script editor\'s documentation comment color. In GDScript, this is
used for comments starting with `##`. In C#, this is used for comments
starting with `///` or `/**`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/engine_type_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/engine_type_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/engine_type_color>`{.interpreted-text
role="ref"}

The script editor\'s engine type color
(`Object<class_Object>`{.interpreted-text role="ref"},
`Mesh<class_Mesh>`{.interpreted-text role="ref"},
`Node<class_Node>`{.interpreted-text role="ref"}, \...).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/executing_line_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/executing_line_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/executing_line_color>`{.interpreted-text
role="ref"}

The script editor\'s color for the debugger\'s executing line icon
(displayed in the gutter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/folded_code_region_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/folded_code_region_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/folded_code_region_color>`{.interpreted-text
role="ref"}

The script editor\'s background line highlighting color for folded code
region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/function_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/function_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/function_color>`{.interpreted-text
role="ref"}

The script editor\'s function call color.

\*\*Note:\*\* When using the GDScript syntax highlighter, this is only
used when calling some functions since function definitions and global
functions have their own colors
`text_editor/theme/highlighting/gdscript/function_definition_color<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/function_definition_color>`{.interpreted-text
role="ref"} and
`text_editor/theme/highlighting/gdscript/global_function_color<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/global_function_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/gdscript/annotation_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/gdscript/annotation_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/annotation_color>`{.interpreted-text
role="ref"}

The GDScript syntax highlighter text color for annotations (e.g.
`@export`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/gdscript/function_definition_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/gdscript/function_definition_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/function_definition_color>`{.interpreted-text
role="ref"}

The GDScript syntax highlighter text color for function definitions
(e.g. the `_ready` in `func _ready():`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/gdscript/global_function_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/gdscript/global_function_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/global_function_color>`{.interpreted-text
role="ref"}

The GDScript syntax highlighter text color for global functions, such as
the ones in `@GlobalScope<class_@GlobalScope>`{.interpreted-text
role="ref"} (e.g. `preload()`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/gdscript/node_path_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/gdscript/node_path_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/node_path_color>`{.interpreted-text
role="ref"}

The GDScript syntax highlighter text color for
`NodePath<class_NodePath>`{.interpreted-text role="ref"} literals (e.g.
`^"position:x"`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/gdscript/node_reference_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/gdscript/node_reference_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/node_reference_color>`{.interpreted-text
role="ref"}

The GDScript syntax highlighter text color for node reference literals
(e.g. `$"Sprite"` and `%"Sprite"`\]).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/gdscript/string_name_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/gdscript/string_name_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/gdscript/string_name_color>`{.interpreted-text
role="ref"}

The GDScript syntax highlighter text color for
`StringName<class_StringName>`{.interpreted-text role="ref"} literals
(e.g. `>"example"`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/keyword_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/keyword_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/keyword_color>`{.interpreted-text
role="ref"}

The script editor\'s non-control flow keyword color (used for keywords
like `var`, `func`, `extends`, \...).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/line_length_guideline_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/line_length_guideline_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/line_length_guideline_color>`{.interpreted-text
role="ref"}

The script editor\'s color for the line length guideline. The \"hard\"
line length guideline will be drawn with this color, whereas the
\"soft\" line length guideline will be drawn with half of its opacity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/line_number_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/line_number_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/line_number_color>`{.interpreted-text
role="ref"}

The script editor\'s color for line numbers. See also
`text_editor/theme/highlighting/safe_line_number_color<class_EditorSettings_property_text_editor/theme/highlighting/safe_line_number_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/mark_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/mark_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/mark_color>`{.interpreted-text
role="ref"}

The script editor\'s background color for lines with errors. This should
be set to a translucent color so that it can display on top of other
line color modifiers such as
`text_editor/theme/highlighting/current_line_color<class_EditorSettings_property_text_editor/theme/highlighting/current_line_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/member_variable_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/member_variable_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/member_variable_color>`{.interpreted-text
role="ref"}

The script editor\'s color for member variables on objects (e.g.
`self.some_property`).

\*\*Note:\*\* This color is not used for local variable declaration and
access.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/number_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/number_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/number_color>`{.interpreted-text
role="ref"}

The script editor\'s color for numbers (integer and floating-point).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/safe_line_number_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/safe_line_number_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/safe_line_number_color>`{.interpreted-text
role="ref"}

The script editor\'s color for type-safe line numbers. See also
`text_editor/theme/highlighting/line_number_color<class_EditorSettings_property_text_editor/theme/highlighting/line_number_color>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only displayed if
`text_editor/appearance/gutters/highlight_type_safe_lines<class_EditorSettings_property_text_editor/appearance/gutters/highlight_type_safe_lines>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/search_result_border_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/search_result_border_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/search_result_border_color>`{.interpreted-text
role="ref"}

The script editor\'s color for the border of search results. This border
helps bring further attention to the search result. Set this color\'s
opacity to 0 to disable the border.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/search_result_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/search_result_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/search_result_color>`{.interpreted-text
role="ref"}

The script editor\'s background color for search results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/selection_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/selection_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/selection_color>`{.interpreted-text
role="ref"}

The script editor\'s background color for the currently selected text.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/string_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/string_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/string_color>`{.interpreted-text
role="ref"}

The script editor\'s color for strings (single-line and multi-line).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/symbol_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/symbol_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/symbol_color>`{.interpreted-text
role="ref"}

The script editor\'s color for operators (`( ) [ ] { } + - * /`, \...).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/text_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/text_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/text_color>`{.interpreted-text
role="ref"}

The script editor\'s color for text not highlighted by any syntax
highlighting rule.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/text_selected_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/text_selected_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/text_selected_color>`{.interpreted-text
role="ref"}

The script editor\'s background color for text. This should be set to a
translucent color so that it can display on top of other line color
modifiers such as
`text_editor/theme/highlighting/current_line_color<class_EditorSettings_property_text_editor/theme/highlighting/current_line_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/user_type_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/user_type_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/user_type_color>`{.interpreted-text
role="ref"}

The script editor\'s color for user-defined types (using `class_name`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/warning_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/warning_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/warning_color>`{.interpreted-text
role="ref"}

The script editor\'s background color for lines with warnings. This
should be set to a translucent color so that it can display on top of
other line color modifiers such as
`text_editor/theme/highlighting/current_line_color<class_EditorSettings_property_text_editor/theme/highlighting/current_line_color>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_text_editor/theme/highlighting/word_highlighted_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**text_editor/theme/highlighting/word_highlighted_color**
`🔗<class_EditorSettings_property_text_editor/theme/highlighting/word_highlighted_color>`{.interpreted-text
role="ref"}

The script editor\'s color for words highlighted by selecting them. Only
visible if
`text_editor/appearance/caret/highlight_all_occurrences<class_EditorSettings_property_text_editor/appearance/caret/highlight_all_occurrences>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_version_control/ssh_private_key_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**version_control/ssh_private_key_path**
`🔗<class_EditorSettings_property_version_control/ssh_private_key_path>`{.interpreted-text
role="ref"}

Path to private SSH key file for the editor\'s Version Control
integration credentials.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_version_control/ssh_public_key_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**version_control/ssh_public_key_path**
`🔗<class_EditorSettings_property_version_control/ssh_public_key_path>`{.interpreted-text
role="ref"}

Path to public SSH key file for the editor\'s Version Control
integration credentials.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_property_version_control/username}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**version_control/username**
`🔗<class_EditorSettings_property_version_control/username>`{.interpreted-text
role="ref"}

Default username for editor\'s Version Control integration.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorSettings_method_add_property_info}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_property_info**(info:
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"})
`🔗<class_EditorSettings_method_add_property_info>`{.interpreted-text
role="ref"}

Adds a custom property info to a property. The dictionary must contain:

- `name`: `String<class_String>`{.interpreted-text role="ref"} (the name
  of the property)
- `type`: `int<class_int>`{.interpreted-text role="ref"} (see
  `Variant.Type<enum_@GlobalScope_Variant.Type>`{.interpreted-text
  role="ref"})
- optionally `hint`: `int<class_int>`{.interpreted-text role="ref"} (see
  `PropertyHint<enum_@GlobalScope_PropertyHint>`{.interpreted-text
  role="ref"}) and `hint_string`:
  `String<class_String>`{.interpreted-text role="ref"}

::::: tabs
::: code-tab
gdscript

var settings = EditorInterface.get_editor_settings()
settings.set(\"category/property_name\", 0)

var property_info = {

:   \"name\": \"category/property_name\", \"type\": TYPE_INT, \"hint\":
    PROPERTY_HINT_ENUM, \"hint_string\": \"one,two,three\"

}

settings.add_property_info(property_info)
:::

::: code-tab
csharp

var settings = GetEditorInterface().GetEditorSettings();
settings.Set(\"category/property_name\", 0);

var propertyInfo = new Godot.Collections.Dictionary { { \"name\",
\"category/propertyName\" }, { \"type\", Variant.Type.Int }, { \"hint\",
PropertyHint.Enum }, { \"hint_string\", \"one,two,three\" }, };

settings.AddPropertyInfo(propertyInfo);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_check_changed_settings_in_group}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**check_changed_settings_in_group**(setting_prefix:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSettings_method_check_changed_settings_in_group>`{.interpreted-text
role="ref"}

Checks if any settings with the prefix `setting_prefix` exist in the set
of changed settings. See also
`get_changed_settings()<class_EditorSettings_method_get_changed_settings>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_erase}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase**(property: `String<class_String>`{.interpreted-text
role="ref"}) `🔗<class_EditorSettings_method_erase>`{.interpreted-text
role="ref"}

Erases the setting whose name is specified by `property`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_get_changed_settings}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_changed_settings**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSettings_method_get_changed_settings>`{.interpreted-text
role="ref"}

Gets an array of the settings which have been changed since the last
save. Note that internally `changed_settings` is cleared after a
successful save, so generally the most appropriate place to use this
method is when processing
`NOTIFICATION_EDITOR_SETTINGS_CHANGED<class_EditorSettings_constant_NOTIFICATION_EDITOR_SETTINGS_CHANGED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_get_favorites}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_favorites**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSettings_method_get_favorites>`{.interpreted-text
role="ref"}

Returns the list of favorite files and directories for this project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_get_project_metadata}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_project_metadata**(section:
`String<class_String>`{.interpreted-text role="ref"}, key:
`String<class_String>`{.interpreted-text role="ref"}, default:
`Variant<class_Variant>`{.interpreted-text role="ref"} = null)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSettings_method_get_project_metadata>`{.interpreted-text
role="ref"}

Returns project-specific metadata for the `section` and `key` specified.
If the metadata doesn\'t exist, `default` will be returned instead. See
also
`set_project_metadata()<class_EditorSettings_method_set_project_metadata>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_get_recent_dirs}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_recent_dirs**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSettings_method_get_recent_dirs>`{.interpreted-text
role="ref"}

Returns the list of recently visited folders in the file dialog for this
project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_get_setting}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_setting**(name: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSettings_method_get_setting>`{.interpreted-text
role="ref"}

Returns the value of the setting specified by `name`. This is equivalent
to using `Object.get()<class_Object_method_get>`{.interpreted-text
role="ref"} on the EditorSettings instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_has_setting}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_setting**(name:
`String<class_String>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorSettings_method_has_setting>`{.interpreted-text
role="ref"}

Returns `true` if the setting specified by `name` exists, `false`
otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_mark_setting_changed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**mark_setting_changed**(setting:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorSettings_method_mark_setting_changed>`{.interpreted-text
role="ref"}

Marks the passed editor setting as being changed, see
`get_changed_settings()<class_EditorSettings_method_get_changed_settings>`{.interpreted-text
role="ref"}. Only settings which exist (see
`has_setting()<class_EditorSettings_method_has_setting>`{.interpreted-text
role="ref"}) will be accepted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_set_builtin_action_override}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_builtin_action_override**(name:
`String<class_String>`{.interpreted-text role="ref"}, actions_list:
`Array<class_Array>`{.interpreted-text
role="ref"}\[`InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}\])
`🔗<class_EditorSettings_method_set_builtin_action_override>`{.interpreted-text
role="ref"}

Overrides the built-in editor action `name` with the input actions
defined in `actions_list`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_set_favorites}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_favorites**(dirs:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorSettings_method_set_favorites>`{.interpreted-text
role="ref"}

Sets the list of favorite files and directories for this project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_set_initial_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_initial_value**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, update_current:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_EditorSettings_method_set_initial_value>`{.interpreted-text
role="ref"}

Sets the initial value of the setting specified by `name` to `value`.
This is used to provide a value for the Revert button in the Editor
Settings. If `update_current` is `true`, the setting is reset to `value`
as well.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_set_project_metadata}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_project_metadata**(section:
`String<class_String>`{.interpreted-text role="ref"}, key:
`String<class_String>`{.interpreted-text role="ref"}, data:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_EditorSettings_method_set_project_metadata>`{.interpreted-text
role="ref"}

Sets project-specific metadata with the `section`, `key` and `data`
specified. This metadata is stored outside the project folder and
therefore won\'t be checked into version control. See also
`get_project_metadata()<class_EditorSettings_method_get_project_metadata>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_set_recent_dirs}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_recent_dirs**(dirs:
`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"})
`🔗<class_EditorSettings_method_set_recent_dirs>`{.interpreted-text
role="ref"}

Sets the list of recently visited folders in the file dialog for this
project.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorSettings_method_set_setting}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_setting**(name: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_EditorSettings_method_set_setting>`{.interpreted-text
role="ref"}

Sets the `value` of the setting specified by `name`. This is equivalent
to using `Object.set()<class_Object_method_set>`{.interpreted-text
role="ref"} on the EditorSettings instance.
