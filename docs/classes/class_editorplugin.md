github_url
:   hide

# EditorPlugin {#class_EditorPlugin}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`GridMapEditorPlugin<class_GridMapEditorPlugin>`{.interpreted-text
role="ref"}

Used by the editor to extend its functionality.

::: rst-class
classref-introduction-group
:::

## Description

Plugins are used by the editor to extend functionality. The most common
types of plugins are those which edit a given node or resource type,
import plugins and export plugins. See also
`EditorScript<class_EditorScript>`{.interpreted-text role="ref"} to add
functions to the editor.

\*\*Note:\*\* Some names in this class contain \"left\" or \"right\"
(e.g.
`DOCK_SLOT_LEFT_UL<class_EditorPlugin_constant_DOCK_SLOT_LEFT_UL>`{.interpreted-text
role="ref"}). These APIs assume left-to-right layout, and would be
backwards when using right-to-left layout. These names are kept for
compatibility reasons.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Editor plugins documentation index <../tutorials/plugins/editor/index>`{.interpreted-text
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

## Signals

:::: {#class_EditorPlugin_signal_main_screen_changed}
::: rst-class
classref-signal
:::
::::

**main_screen_changed**(screen_name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_signal_main_screen_changed>`{.interpreted-text
role="ref"}

Emitted when user changes the workspace (**2D**, **3D**, **Script**,
**Game**, **AssetLib**). Also works with custom screens defined by
plugins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_signal_project_settings_changed}
::: rst-class
classref-signal
:::
::::

**project_settings_changed**()
`🔗<class_EditorPlugin_signal_project_settings_changed>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`ProjectSettings.settings_changed<class_ProjectSettings_signal_settings_changed>`{.interpreted-text
role="ref"} instead.

Emitted when any project setting has changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_signal_resource_saved}
::: rst-class
classref-signal
:::
::::

**resource_saved**(resource:
`Resource<class_Resource>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_signal_resource_saved>`{.interpreted-text
role="ref"}

Emitted when the given `resource` was saved on disc. See also
`scene_saved<class_EditorPlugin_signal_scene_saved>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_signal_scene_changed}
::: rst-class
classref-signal
:::
::::

**scene_changed**(scene_root: `Node<class_Node>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_signal_scene_changed>`{.interpreted-text
role="ref"}

Emitted when the scene is changed in the editor. The argument will
return the root node of the scene that has just become active. If this
scene is new and empty, the argument will be `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_signal_scene_closed}
::: rst-class
classref-signal
:::
::::

**scene_closed**(filepath: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_signal_scene_closed>`{.interpreted-text
role="ref"}

Emitted when user closes a scene. The argument is a file path to the
closed scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_signal_scene_saved}
::: rst-class
classref-signal
:::
::::

**scene_saved**(filepath: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_signal_scene_saved>`{.interpreted-text
role="ref"}

Emitted when a scene was saved on disc. The argument is a file path to
the saved scene. See also
`resource_saved<class_EditorPlugin_signal_resource_saved>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_EditorPlugin_CustomControlContainer}
::: rst-class
classref-enumeration
:::
::::

enum **CustomControlContainer**:
`🔗<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"}

:::: {#class_EditorPlugin_constant_CONTAINER_TOOLBAR}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_TOOLBAR** = `0`

Main editor toolbar, next to play buttons.

:::: {#class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_MENU}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_SPATIAL_EDITOR_MENU** = `1`

The toolbar that appears when 3D editor is active.

:::: {#class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_SIDE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_SPATIAL_EDITOR_SIDE_LEFT** = `2`

Left sidebar of the 3D editor.

:::: {#class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_SIDE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_SPATIAL_EDITOR_SIDE_RIGHT** = `3`

Right sidebar of the 3D editor.

:::: {#class_EditorPlugin_constant_CONTAINER_SPATIAL_EDITOR_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_SPATIAL_EDITOR_BOTTOM** = `4`

Bottom panel of the 3D editor.

:::: {#class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_MENU}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_CANVAS_EDITOR_MENU** = `5`

The toolbar that appears when 2D editor is active.

:::: {#class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_SIDE_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_CANVAS_EDITOR_SIDE_LEFT** = `6`

Left sidebar of the 2D editor.

:::: {#class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_SIDE_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_CANVAS_EDITOR_SIDE_RIGHT** = `7`

Right sidebar of the 2D editor.

:::: {#class_EditorPlugin_constant_CONTAINER_CANVAS_EDITOR_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_CANVAS_EDITOR_BOTTOM** = `8`

Bottom panel of the 2D editor.

:::: {#class_EditorPlugin_constant_CONTAINER_INSPECTOR_BOTTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_INSPECTOR_BOTTOM** = `9`

Bottom section of the inspector.

:::: {#class_EditorPlugin_constant_CONTAINER_PROJECT_SETTING_TAB_LEFT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_PROJECT_SETTING_TAB_LEFT** = `10`

Tab of Project Settings dialog, to the left of other tabs.

:::: {#class_EditorPlugin_constant_CONTAINER_PROJECT_SETTING_TAB_RIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"} **CONTAINER_PROJECT_SETTING_TAB_RIGHT** = `11`

Tab of Project Settings dialog, to the right of other tabs.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorPlugin_DockSlot}
::: rst-class
classref-enumeration
:::
::::

enum **DockSlot**: `🔗<enum_EditorPlugin_DockSlot>`{.interpreted-text
role="ref"}

:::: {#class_EditorPlugin_constant_DOCK_SLOT_LEFT_UL}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_LEFT_UL** = `0`

Dock slot, left side, upper-left (empty in default layout).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_LEFT_BL}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_LEFT_BL** = `1`

Dock slot, left side, bottom-left (empty in default layout).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_LEFT_UR}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_LEFT_UR** = `2`

Dock slot, left side, upper-right (in default layout includes Scene and
Import docks).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_LEFT_BR}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_LEFT_BR** = `3`

Dock slot, left side, bottom-right (in default layout includes
FileSystem dock).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_RIGHT_UL}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_RIGHT_UL** = `4`

Dock slot, right side, upper-left (in default layout includes Inspector,
Node, and History docks).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_RIGHT_BL}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_RIGHT_BL** = `5`

Dock slot, right side, bottom-left (empty in default layout).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_RIGHT_UR}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_RIGHT_UR** = `6`

Dock slot, right side, upper-right (empty in default layout).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_RIGHT_BR}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_RIGHT_BR** = `7`

Dock slot, right side, bottom-right (empty in default layout).

:::: {#class_EditorPlugin_constant_DOCK_SLOT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
**DOCK_SLOT_MAX** = `8`

Represents the size of the
`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_EditorPlugin_AfterGUIInput}
::: rst-class
classref-enumeration
:::
::::

enum **AfterGUIInput**:
`🔗<enum_EditorPlugin_AfterGUIInput>`{.interpreted-text role="ref"}

:::: {#class_EditorPlugin_constant_AFTER_GUI_INPUT_PASS}
::: rst-class
classref-enumeration-constant
:::
::::

`AfterGUIInput<enum_EditorPlugin_AfterGUIInput>`{.interpreted-text
role="ref"} **AFTER_GUI_INPUT_PASS** = `0`

Forwards the `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} to other EditorPlugins.

:::: {#class_EditorPlugin_constant_AFTER_GUI_INPUT_STOP}
::: rst-class
classref-enumeration-constant
:::
::::

`AfterGUIInput<enum_EditorPlugin_AfterGUIInput>`{.interpreted-text
role="ref"} **AFTER_GUI_INPUT_STOP** = `1`

Prevents the `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} from reaching other Editor classes.

:::: {#class_EditorPlugin_constant_AFTER_GUI_INPUT_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`AfterGUIInput<enum_EditorPlugin_AfterGUIInput>`{.interpreted-text
role="ref"} **AFTER_GUI_INPUT_CUSTOM** = `2`

Pass the `InputEvent<class_InputEvent>`{.interpreted-text role="ref"} to
other editor plugins except the main
`Node3D<class_Node3D>`{.interpreted-text role="ref"} one. This can be
used to prevent node selection changes and work with sub-gizmos instead.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorPlugin_private_method__apply_changes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_apply_changes**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__apply_changes>`{.interpreted-text
role="ref"}

This method is called when the editor is about to save the project,
switch to another tab, etc. It asks the plugin to apply any pending
state changes to ensure consistency.

This is used, for example, in shader editors to let the plugin know that
it must apply the shader code being written by the user to the object.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__build}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_build**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__build>`{.interpreted-text
role="ref"}

This method is called when the editor is about to run the project. The
plugin can then perform required operations before the project runs.

This method must return a boolean. If this method returns `false`, the
project will not run. The run is aborted immediately, so this also
prevents all other plugins\'
`_build()<class_EditorPlugin_private_method__build>`{.interpreted-text
role="ref"} methods from running.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_clear**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__clear>`{.interpreted-text
role="ref"}

Clear all the state and reset the object being edited to zero. This
ensures your plugin does not keep editing a currently existing node, or
a node from the wrong scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__disable_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_disable_plugin**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__disable_plugin>`{.interpreted-text
role="ref"}

Called by the engine when the user disables the **EditorPlugin** in the
Plugin tab of the project settings window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__edit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_edit**(object: `Object<class_Object>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__edit>`{.interpreted-text
role="ref"}

This function is used for plugins that edit specific object types (nodes
or resources). It requests the editor to edit the given object.

`object` can be `null` if the plugin was editing an object, but there is
no longer any selected object handled by this plugin. It can be used to
cleanup editing state.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__enable_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_enable_plugin**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__enable_plugin>`{.interpreted-text
role="ref"}

Called by the engine when the user enables the **EditorPlugin** in the
Plugin tab of the project settings window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__forward_3d_draw_over_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_forward_3d_draw_over_viewport**(viewport_control:
`Control<class_Control>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__forward_3d_draw_over_viewport>`{.interpreted-text
role="ref"}

Called by the engine when the 3D editor\'s viewport is updated.
`viewport_control` is an overlay on top of the viewport and it can be
used for drawing. You can update the viewport manually by calling
`update_overlays()<class_EditorPlugin_method_update_overlays>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

func [forward_3d_draw_over_viewport]{#forward_3d_draw_over_viewport}(overlay):

:   \# Draw a circle at the cursor\'s position.
    overlay.draw_circle(overlay.get_local_mouse_position(), 64,
    Color.WHITE)

func [forward_3d_gui_input]{#forward_3d_gui_input}(camera, event):

:   

    if event is InputEventMouseMotion:

    :   \# Redraw the viewport when the cursor is moved.
        update_overlays() return EditorPlugin.AFTER_GUI_INPUT_STOP

    return EditorPlugin.AFTER_GUI_INPUT_PASS
:::

::: code-tab
csharp

public override void
[Forward3DDrawOverViewport]{#forward3ddrawoverviewport}(Control
viewportControl) { // Draw a circle at the cursor\'s position.
viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64,
Colors.White); }

public override EditorPlugin.AfterGuiInput
[Forward3DGuiInput]{#forward3dguiinput}(Camera3D viewportCamera,
InputEvent \@event) { if (@event is InputEventMouseMotion) { // Redraw
the viewport when the cursor is moved. UpdateOverlays(); return
EditorPlugin.AfterGuiInput.Stop; } return
EditorPlugin.AfterGuiInput.Pass; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_forward_3d_force_draw_over_viewport**(viewport_control:
`Control<class_Control>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport>`{.interpreted-text
role="ref"}

This method is the same as
`_forward_3d_draw_over_viewport()<class_EditorPlugin_private_method__forward_3d_draw_over_viewport>`{.interpreted-text
role="ref"}, except it draws on top of everything. Useful when you need
an extra layer that shows over anything else.

You need to enable calling of this method by using
`set_force_draw_over_forwarding_enabled()<class_EditorPlugin_method_set_force_draw_over_forwarding_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__forward_3d_gui_input}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**\_forward_3d_gui_input**(viewport_camera:
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}, event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__forward_3d_gui_input>`{.interpreted-text
role="ref"}

Called when there is a root node in the current edited scene,
`_handles()<class_EditorPlugin_private_method__handles>`{.interpreted-text
role="ref"} is implemented, and an
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} happens in
the 3D viewport. The return value decides whether the
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} is consumed
or forwarded to other **EditorPlugin**s. See
`AfterGUIInput<enum_EditorPlugin_AfterGUIInput>`{.interpreted-text
role="ref"} for options.

::::: tabs
::: code-tab
gdscript

\# Prevents the InputEvent from reaching other Editor classes. func
[forward_3d_gui_input]{#forward_3d_gui_input}(camera, event): return
EditorPlugin.AFTER_GUI_INPUT_STOP
:::

::: code-tab
csharp

// Prevents the InputEvent from reaching other Editor classes. public
override EditorPlugin.AfterGuiInput
[Forward3DGuiInput]{#forward3dguiinput}(Camera3D camera, InputEvent
\@event) { return EditorPlugin.AfterGuiInput.Stop; }
:::
:::::

This method must return
`AFTER_GUI_INPUT_PASS<class_EditorPlugin_constant_AFTER_GUI_INPUT_PASS>`{.interpreted-text
role="ref"} in order to forward the
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} to other
Editor classes.

::::: tabs
::: code-tab
gdscript

\# Consumes InputEventMouseMotion and forwards other InputEvent types.
func [forward_3d_gui_input]{#forward_3d_gui_input}(camera, event):
return EditorPlugin.AFTER_GUI_INPUT_STOP if event is
InputEventMouseMotion else EditorPlugin.AFTER_GUI_INPUT_PASS
:::

::: code-tab
csharp

// Consumes InputEventMouseMotion and forwards other InputEvent types.
public override EditorPlugin.AfterGuiInput
[Forward3DGuiInput]{#forward3dguiinput}(Camera3D camera, InputEvent
\@event) { return \@event is InputEventMouseMotion ?
EditorPlugin.AfterGuiInput.Stop : EditorPlugin.AfterGuiInput.Pass; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__forward_canvas_draw_over_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_forward_canvas_draw_over_viewport**(viewport_control:
`Control<class_Control>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__forward_canvas_draw_over_viewport>`{.interpreted-text
role="ref"}

Called by the engine when the 2D editor\'s viewport is updated.
`viewport_control` is an overlay on top of the viewport and it can be
used for drawing. You can update the viewport manually by calling
`update_overlays()<class_EditorPlugin_method_update_overlays>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

func [forward_canvas_draw_over_viewport]{#forward_canvas_draw_over_viewport}(overlay):

:   \# Draw a circle at the cursor\'s position.
    overlay.draw_circle(overlay.get_local_mouse_position(), 64,
    Color.WHITE)

func [forward_canvas_gui_input]{#forward_canvas_gui_input}(event):

:   

    if event is InputEventMouseMotion:

    :   \# Redraw the viewport when the cursor is moved.
        update_overlays() return true

    return false
:::

::: code-tab
csharp

public override void
[ForwardCanvasDrawOverViewport]{#forwardcanvasdrawoverviewport}(Control
viewportControl) { // Draw a circle at the cursor\'s position.
viewportControl.DrawCircle(viewportControl.GetLocalMousePosition(), 64,
Colors.White); }

public override bool
[ForwardCanvasGuiInput]{#forwardcanvasguiinput}(InputEvent \@event) { if
(@event is InputEventMouseMotion) { // Redraw the viewport when the
cursor is moved. UpdateOverlays(); return true; } return false; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_forward_canvas_force_draw_over_viewport**(viewport_control:
`Control<class_Control>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport>`{.interpreted-text
role="ref"}

This method is the same as
`_forward_canvas_draw_over_viewport()<class_EditorPlugin_private_method__forward_canvas_draw_over_viewport>`{.interpreted-text
role="ref"}, except it draws on top of everything. Useful when you need
an extra layer that shows over anything else.

You need to enable calling of this method by using
`set_force_draw_over_forwarding_enabled()<class_EditorPlugin_method_set_force_draw_over_forwarding_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__forward_canvas_gui_input}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**\_forward_canvas_gui_input**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__forward_canvas_gui_input>`{.interpreted-text
role="ref"}

Called when there is a root node in the current edited scene,
`_handles()<class_EditorPlugin_private_method__handles>`{.interpreted-text
role="ref"} is implemented, and an
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} happens in
the 2D viewport. If this method returns `true`, `event` is intercepted
by this **EditorPlugin**, otherwise `event` is forwarded to other Editor
classes.

::::: tabs
::: code-tab
gdscript

\# Prevents the InputEvent from reaching other Editor classes. func
[forward_canvas_gui_input]{#forward_canvas_gui_input}(event): return
true
:::

::: code-tab
csharp

// Prevents the InputEvent from reaching other Editor classes. public
override bool ForwardCanvasGuiInput(InputEvent \@event) { return true; }
:::
:::::

This method must return `false` in order to forward the
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} to other
Editor classes.

::::: tabs
::: code-tab
gdscript

\# Consumes InputEventMouseMotion and forwards other InputEvent types.
func [forward_canvas_gui_input]{#forward_canvas_gui_input}(event): if
(event is InputEventMouseMotion): return true return false
:::

::: code-tab
csharp

// Consumes InputEventMouseMotion and forwards other InputEvent types.
public override bool
[ForwardCanvasGuiInput]{#forwardcanvasguiinput}(InputEvent \@event) { if
(@event is InputEventMouseMotion) { return true; } return false; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__get_breakpoints}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_breakpoints**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__get_breakpoints>`{.interpreted-text
role="ref"}

This is for editors that edit script-based objects. You can return a
list of breakpoints in the format (`script:line`), for example:
`res://path_to_script.gd:25`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__get_plugin_icon}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\_get_plugin_icon**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__get_plugin_icon>`{.interpreted-text
role="ref"}

Override this method in your plugin to return a
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} in order to
give it an icon.

For main screen plugins, this appears at the top of the screen, to the
right of the \"2D\", \"3D\", \"Script\", \"Game\", and \"AssetLib\"
buttons.

Ideally, the plugin icon should be white with a transparent background
and 16×16 pixels in size.

::::: tabs
::: code-tab
gdscript

func [get_plugin_icon]{#get_plugin_icon}():

:   \# You can use a custom icon: return
    preload(\"res://addons/my_plugin/my_plugin_icon.svg\") \# Or use a
    built-in icon: return
    EditorInterface.get_editor_theme().get_icon(\"Node\",
    \"EditorIcons\")
:::

::: code-tab
csharp

public override Texture2D [GetPluginIcon]{#getpluginicon}() { // You can
use a custom icon: return
ResourceLoader.Load\<Texture2D\>(\"res://addons/my_plugin/my_plugin_icon.svg\");
// Or use a built-in icon: return
EditorInterface.Singleton.GetEditorTheme().GetIcon(\"Node\",
\"EditorIcons\"); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__get_plugin_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_plugin_name**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__get_plugin_name>`{.interpreted-text
role="ref"}

Override this method in your plugin to provide the name of the plugin
when displayed in the Godot editor.

For main screen plugins, this appears at the top of the screen, to the
right of the \"2D\", \"3D\", \"Script\", \"Game\", and \"AssetLib\"
buttons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__get_state}
::: rst-class
classref-method
:::
::::

`Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
**\_get_state**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__get_state>`{.interpreted-text
role="ref"}

Override this method to provide a state data you want to be saved, like
view position, grid settings, folding, etc. This is used when saving the
scene (so state is kept when opening it again) and for switching tabs
(so state can be restored when the tab returns). This data is
automatically saved for each scene in an `editstate` file in the editor
metadata folder. If you want to store global (scene-independent) editor
data for your plugin, you can use
`_get_window_layout()<class_EditorPlugin_private_method__get_window_layout>`{.interpreted-text
role="ref"} instead.

Use
`_set_state()<class_EditorPlugin_private_method__set_state>`{.interpreted-text
role="ref"} to restore your saved state.

\*\*Note:\*\* This method should not be used to save important settings
that should persist with the project.

\*\*Note:\*\* You must implement
`_get_plugin_name()<class_EditorPlugin_private_method__get_plugin_name>`{.interpreted-text
role="ref"} for the state to be stored and restored correctly.

    func _get_state():
        var state = { "zoom": zoom, "preferred_color": my_color }
        return state

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__get_unsaved_status}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**\_get_unsaved_status**(for_scene:
`String<class_String>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__get_unsaved_status>`{.interpreted-text
role="ref"}

Override this method to provide a custom message that lists unsaved
changes. The editor will call this method when exiting or when closing a
scene, and display the returned string in a confirmation dialog. Return
empty string if the plugin has no unsaved changes.

When closing a scene, `for_scene` is the path to the scene being closed.
You can use it to handle built-in resources in that scene.

If the user confirms saving,
`_save_external_data()<class_EditorPlugin_private_method__save_external_data>`{.interpreted-text
role="ref"} will be called, before closing the editor.

    func _get_unsaved_status(for_scene):
        if not unsaved:
            return ""

        if for_scene.is_empty():
            return "Save changes in MyCustomPlugin before closing?"
        else:
            return "Scene %s has changes from MyCustomPlugin. Save before closing?" % for_scene.get_file()

    func _save_external_data():
        unsaved = false

If the plugin has no scene-specific changes, you can ignore the calls
when closing scenes:

    func _get_unsaved_status(for_scene):
        if not for_scene.is_empty():
            return ""

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__get_window_layout}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_get_window_layout**(configuration:
`ConfigFile<class_ConfigFile>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__get_window_layout>`{.interpreted-text
role="ref"}

Override this method to provide the GUI layout of the plugin or any
other data you want to be stored. This is used to save the project\'s
editor layout when
`queue_save_layout()<class_EditorPlugin_method_queue_save_layout>`{.interpreted-text
role="ref"} is called or the editor layout was changed (for example
changing the position of a dock). The data is stored in the
`editor_layout.cfg` file in the editor metadata directory.

Use
`_set_window_layout()<class_EditorPlugin_private_method__set_window_layout>`{.interpreted-text
role="ref"} to restore your saved layout.

    func _get_window_layout(configuration):
        configuration.set_value("MyPlugin", "window_position", $Window.position)
        configuration.set_value("MyPlugin", "icon_color", $Icon.modulate)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__handles}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_handles**(object:
`Object<class_Object>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__handles>`{.interpreted-text
role="ref"}

Implement this function if your plugin edits a specific type of object
(Resource or Node). If you return `true`, then you will get the
functions
`_edit()<class_EditorPlugin_private_method__edit>`{.interpreted-text
role="ref"} and
`_make_visible()<class_EditorPlugin_private_method__make_visible>`{.interpreted-text
role="ref"} called when the editor requests them. If you have declared
the methods
`_forward_canvas_gui_input()<class_EditorPlugin_private_method__forward_canvas_gui_input>`{.interpreted-text
role="ref"} and
`_forward_3d_gui_input()<class_EditorPlugin_private_method__forward_3d_gui_input>`{.interpreted-text
role="ref"} these will be called too.

\*\*Note:\*\* Each plugin should handle only one type of objects at a
time. If a plugin handles more types of objects and they are edited at
the same time, it will result in errors.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__has_main_screen}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **\_has_main_screen**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__has_main_screen>`{.interpreted-text
role="ref"}

Returns `true` if this is a main screen editor plugin (it goes in the
workspace selector together with **2D**, **3D**, **Script**, **Game**,
and **AssetLib**).

When the plugin\'s workspace is selected, other main screen plugins will
be hidden, but your plugin will not appear automatically. It needs to be
added as a child of
`EditorInterface.get_editor_main_screen()<class_EditorInterface_method_get_editor_main_screen>`{.interpreted-text
role="ref"} and made visible inside
`_make_visible()<class_EditorPlugin_private_method__make_visible>`{.interpreted-text
role="ref"}.

Use
`_get_plugin_name()<class_EditorPlugin_private_method__get_plugin_name>`{.interpreted-text
role="ref"} and
`_get_plugin_icon()<class_EditorPlugin_private_method__get_plugin_icon>`{.interpreted-text
role="ref"} to customize the plugin button\'s appearance.

    var plugin_control

    func _enter_tree():
        plugin_control = preload("my_plugin_control.tscn").instantiate()
        EditorInterface.get_editor_main_screen().add_child(plugin_control)
        plugin_control.hide()

    func _has_main_screen():
        return true

    func _make_visible(visible):
        plugin_control.visible = visible

    func _get_plugin_name():
        return "My Super Cool Plugin 3000"

    func _get_plugin_icon():
        return EditorInterface.get_editor_theme().get_icon("Node", "EditorIcons")

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__make_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_make_visible**(visible: `bool<class_bool>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__make_visible>`{.interpreted-text
role="ref"}

This function will be called when the editor is requested to become
visible. It is used for plugins that edit a specific object type.

Remember that you have to manage the visibility of all your editor
controls manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__save_external_data}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_save_external_data**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__save_external_data>`{.interpreted-text
role="ref"}

This method is called after the editor saves the project or when it\'s
closed. It asks the plugin to save edited external scenes/resources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__set_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_state**(state: `Dictionary<class_Dictionary>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__set_state>`{.interpreted-text
role="ref"}

Restore the state saved by
`_get_state()<class_EditorPlugin_private_method__get_state>`{.interpreted-text
role="ref"}. This method is called when the current scene tab is changed
in the editor.

\*\*Note:\*\* Your plugin must implement
`_get_plugin_name()<class_EditorPlugin_private_method__get_plugin_name>`{.interpreted-text
role="ref"}, otherwise it will not be recognized and this method will
not be called.

    func _set_state(data):
        zoom = data.get("zoom", 1.0)
        preferred_color = data.get("my_color", Color.WHITE)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_private_method__set_window_layout}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_set_window_layout**(configuration:
`ConfigFile<class_ConfigFile>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_private_method__set_window_layout>`{.interpreted-text
role="ref"}

Restore the plugin GUI layout and data saved by
`_get_window_layout()<class_EditorPlugin_private_method__get_window_layout>`{.interpreted-text
role="ref"}. This method is called for every plugin on editor startup.
Use the provided `configuration` file to read your saved data.

    func _set_window_layout(configuration):
        $Window.position = configuration.get_value("MyPlugin", "window_position", Vector2())
        $Icon.modulate = configuration.get_value("MyPlugin", "icon_color", Color.WHITE)

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_autoload_singleton}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_autoload_singleton**(name:
`String<class_String>`{.interpreted-text role="ref"}, path:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_add_autoload_singleton>`{.interpreted-text
role="ref"}

Adds a script at `path` to the Autoload list as `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_context_menu_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_context_menu_plugin**(slot:
`ContextMenuSlot<enum_EditorContextMenuPlugin_ContextMenuSlot>`{.interpreted-text
role="ref"}, plugin:
`EditorContextMenuPlugin<class_EditorContextMenuPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_context_menu_plugin>`{.interpreted-text
role="ref"}

Adds a plugin to the context menu. `slot` is the context menu where the
plugin will be added.

\*\*Note:\*\* A plugin instance can belong only to a single context menu
slot.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_control_to_bottom_panel}
::: rst-class
classref-method
:::
::::

`Button<class_Button>`{.interpreted-text role="ref"}
**add_control_to_bottom_panel**(control:
`Control<class_Control>`{.interpreted-text role="ref"}, title:
`String<class_String>`{.interpreted-text role="ref"}, shortcut:
`Shortcut<class_Shortcut>`{.interpreted-text role="ref"} = null)
`🔗<class_EditorPlugin_method_add_control_to_bottom_panel>`{.interpreted-text
role="ref"}

Adds a control to the bottom panel (together with Output, Debug,
Animation, etc.). Returns a reference to the button added. It\'s up to
you to hide/show the button when needed. When your plugin is
deactivated, make sure to remove your custom control with
`remove_control_from_bottom_panel()<class_EditorPlugin_method_remove_control_from_bottom_panel>`{.interpreted-text
role="ref"} and free it with
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}.

Optionally, you can specify a shortcut parameter. When pressed, this
shortcut will toggle the bottom panel\'s visibility. See the default
editor bottom panel shortcuts in the Editor Settings for inspiration.
Per convention, they all use `Alt`{.interpreted-text role="kbd"}
modifier.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_control_to_container}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_control_to_container**(container:
`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"}, control: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_control_to_container>`{.interpreted-text
role="ref"}

Adds a custom control to a container in the editor UI.

Please remember that you have to manage the visibility of your custom
controls yourself (and likely hide it after adding it).

When your plugin is deactivated, make sure to remove your custom control
with
`remove_control_from_container()<class_EditorPlugin_method_remove_control_from_container>`{.interpreted-text
role="ref"} and free it with
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_control_to_dock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_control_to_dock**(slot:
`DockSlot<enum_EditorPlugin_DockSlot>`{.interpreted-text role="ref"},
control: `Control<class_Control>`{.interpreted-text role="ref"},
shortcut: `Shortcut<class_Shortcut>`{.interpreted-text role="ref"} =
null)
`🔗<class_EditorPlugin_method_add_control_to_dock>`{.interpreted-text
role="ref"}

Adds the control to a specific dock slot.

If the dock is repositioned and as long as the plugin is active, the
editor will save the dock position on further sessions.

When your plugin is deactivated, make sure to remove your custom control
with
`remove_control_from_docks()<class_EditorPlugin_method_remove_control_from_docks>`{.interpreted-text
role="ref"} and free it with
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}.

Optionally, you can specify a shortcut parameter. When pressed, this
shortcut will open and focus the dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_custom_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_custom_type**(type: `String<class_String>`{.interpreted-text
role="ref"}, base: `String<class_String>`{.interpreted-text role="ref"},
script: `Script<class_Script>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_add_custom_type>`{.interpreted-text
role="ref"}

Adds a custom type, which will appear in the list of nodes or resources.

When a given node or resource is selected, the base type will be
instantiated (e.g. \"Node3D\", \"Control\", \"Resource\"), then the
script will be loaded and set to this object.

\*\*Note:\*\* The base type is the base engine class which this type\'s
class hierarchy inherits, not any custom type parent classes.

You can use the virtual method
`_handles()<class_EditorPlugin_private_method__handles>`{.interpreted-text
role="ref"} to check if your custom object is being edited by checking
the script or using the `is` keyword.

During run-time, this will be a simple object with a script so this
function does not need to be called then.

\*\*Note:\*\* Custom types added this way are not true classes. They are
just a helper to create a node with specific script.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_debugger_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_debugger_plugin**(script:
`EditorDebuggerPlugin<class_EditorDebuggerPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_debugger_plugin>`{.interpreted-text
role="ref"}

Adds a `Script<class_Script>`{.interpreted-text role="ref"} as debugger
plugin to the Debugger. The script must extend
`EditorDebuggerPlugin<class_EditorDebuggerPlugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_export_platform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_export_platform**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_export_platform>`{.interpreted-text
role="ref"}

Registers a new
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"}. Export platforms provides functionality of exporting to the
specific platform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_export_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_export_plugin**(plugin:
`EditorExportPlugin<class_EditorExportPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_export_plugin>`{.interpreted-text
role="ref"}

Registers a new
`EditorExportPlugin<class_EditorExportPlugin>`{.interpreted-text
role="ref"}. Export plugins are used to perform tasks when the project
is being exported.

See
`add_inspector_plugin()<class_EditorPlugin_method_add_inspector_plugin>`{.interpreted-text
role="ref"} for an example of how to register a plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_import_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_import_plugin**(importer:
`EditorImportPlugin<class_EditorImportPlugin>`{.interpreted-text
role="ref"}, first_priority: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_EditorPlugin_method_add_import_plugin>`{.interpreted-text
role="ref"}

Registers a new
`EditorImportPlugin<class_EditorImportPlugin>`{.interpreted-text
role="ref"}. Import plugins are used to import custom and unsupported
assets as a custom `Resource<class_Resource>`{.interpreted-text
role="ref"} type.

If `first_priority` is `true`, the new import plugin is inserted first
in the list and takes precedence over pre-existing plugins.

\*\*Note:\*\* If you want to import custom 3D asset formats use
`add_scene_format_importer_plugin()<class_EditorPlugin_method_add_scene_format_importer_plugin>`{.interpreted-text
role="ref"} instead.

See
`add_inspector_plugin()<class_EditorPlugin_method_add_inspector_plugin>`{.interpreted-text
role="ref"} for an example of how to register a plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_inspector_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_inspector_plugin**(plugin:
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_inspector_plugin>`{.interpreted-text
role="ref"}

Registers a new
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"}. Inspector plugins are used to extend
`EditorInspector<class_EditorInspector>`{.interpreted-text role="ref"}
and provide custom configuration tools for your object\'s properties.

\*\*Note:\*\* Always use
`remove_inspector_plugin()<class_EditorPlugin_method_remove_inspector_plugin>`{.interpreted-text
role="ref"} to remove the registered
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"} when your **EditorPlugin** is disabled to prevent leaks and
an unexpected behavior.

:::: tabs
::: code-tab
gdscript

const MyInspectorPlugin =
preload(\"res://addons/your_addon/path/to/your/script.gd\") var
inspector_plugin = MyInspectorPlugin.new()

func [enter_tree]{#enter_tree}():

:   add_inspector_plugin(inspector_plugin)

func [exit_tree]{#exit_tree}():

:   remove_inspector_plugin(inspector_plugin)
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_node_3d_gizmo_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_node_3d_gizmo_plugin**(plugin:
`EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_node_3d_gizmo_plugin>`{.interpreted-text
role="ref"}

Registers a new
`EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>`{.interpreted-text
role="ref"}. Gizmo plugins are used to add custom gizmos to the 3D
preview viewport for a `Node3D<class_Node3D>`{.interpreted-text
role="ref"}.

See
`add_inspector_plugin()<class_EditorPlugin_method_add_inspector_plugin>`{.interpreted-text
role="ref"} for an example of how to register a plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_resource_conversion_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_resource_conversion_plugin**(plugin:
`EditorResourceConversionPlugin<class_EditorResourceConversionPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_resource_conversion_plugin>`{.interpreted-text
role="ref"}

Registers a new
`EditorResourceConversionPlugin<class_EditorResourceConversionPlugin>`{.interpreted-text
role="ref"}. Resource conversion plugins are used to add custom resource
converters to the editor inspector.

See
`EditorResourceConversionPlugin<class_EditorResourceConversionPlugin>`{.interpreted-text
role="ref"} for an example of how to create a resource conversion
plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_scene_format_importer_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_scene_format_importer_plugin**(scene_format_importer:
`EditorSceneFormatImporter<class_EditorSceneFormatImporter>`{.interpreted-text
role="ref"}, first_priority: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_EditorPlugin_method_add_scene_format_importer_plugin>`{.interpreted-text
role="ref"}

Registers a new
`EditorSceneFormatImporter<class_EditorSceneFormatImporter>`{.interpreted-text
role="ref"}. Scene importers are used to import custom 3D asset formats
as scenes.

If `first_priority` is `true`, the new import plugin is inserted first
in the list and takes precedence over pre-existing plugins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_scene_post_import_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_scene_post_import_plugin**(scene_import_plugin:
`EditorScenePostImportPlugin<class_EditorScenePostImportPlugin>`{.interpreted-text
role="ref"}, first_priority: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_EditorPlugin_method_add_scene_post_import_plugin>`{.interpreted-text
role="ref"}

Add an
`EditorScenePostImportPlugin<class_EditorScenePostImportPlugin>`{.interpreted-text
role="ref"}. These plugins allow customizing the import process of 3D
assets by adding new options to the import dialogs.

If `first_priority` is `true`, the new import plugin is inserted first
in the list and takes precedence over pre-existing plugins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_tool_menu_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_tool_menu_item**(name: `String<class_String>`{.interpreted-text
role="ref"}, callable: `Callable<class_Callable>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_tool_menu_item>`{.interpreted-text
role="ref"}

Adds a custom menu item to **Project \> Tools** named `name`. When
clicked, the provided `callable` will be called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_tool_submenu_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_tool_submenu_item**(name: `String<class_String>`{.interpreted-text
role="ref"}, submenu: `PopupMenu<class_PopupMenu>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_tool_submenu_item>`{.interpreted-text
role="ref"}

Adds a custom `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
submenu under **Project \> Tools \>** `name`. Use
`remove_tool_menu_item()<class_EditorPlugin_method_remove_tool_menu_item>`{.interpreted-text
role="ref"} on plugin clean up to remove the menu.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_translation_parser_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_translation_parser_plugin**(parser:
`EditorTranslationParserPlugin<class_EditorTranslationParserPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_add_translation_parser_plugin>`{.interpreted-text
role="ref"}

Registers a custom translation parser plugin for extracting translatable
strings from custom files.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_add_undo_redo_inspector_hook_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_undo_redo_inspector_hook_callback**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_add_undo_redo_inspector_hook_callback>`{.interpreted-text
role="ref"}

Hooks a callback into the undo/redo action creation when a property is
modified in the inspector. This allows, for example, to save other
properties that may be lost when a given property is modified.

The callback should have 4 arguments:
`Object<class_Object>`{.interpreted-text role="ref"} `undo_redo`,
`Object<class_Object>`{.interpreted-text role="ref"} `modified_object`,
`String<class_String>`{.interpreted-text role="ref"} `property` and
`Variant<class_Variant>`{.interpreted-text role="ref"} `new_value`. They
are, respectively, the `UndoRedo<class_UndoRedo>`{.interpreted-text
role="ref"} object used by the inspector, the currently modified object,
the name of the modified property and the new value the property is
about to take.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_get_editor_interface}
::: rst-class
classref-method
:::
::::

`EditorInterface<class_EditorInterface>`{.interpreted-text role="ref"}
**get_editor_interface**()
`🔗<class_EditorPlugin_method_get_editor_interface>`{.interpreted-text
role="ref"}

**Deprecated:**
`EditorInterface<class_EditorInterface>`{.interpreted-text role="ref"}
is a global singleton and can be accessed directly by its name.

Returns the `EditorInterface<class_EditorInterface>`{.interpreted-text
role="ref"} singleton instance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_get_export_as_menu}
::: rst-class
classref-method
:::
::::

`PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
**get_export_as_menu**()
`🔗<class_EditorPlugin_method_get_export_as_menu>`{.interpreted-text
role="ref"}

Returns the `PopupMenu<class_PopupMenu>`{.interpreted-text role="ref"}
under **Scene \> Export As\...**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_get_plugin_version}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_plugin_version**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_method_get_plugin_version>`{.interpreted-text
role="ref"}

Provide the version of the plugin declared in the `plugin.cfg` config
file.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_get_script_create_dialog}
::: rst-class
classref-method
:::
::::

`ScriptCreateDialog<class_ScriptCreateDialog>`{.interpreted-text
role="ref"} **get_script_create_dialog**()
`🔗<class_EditorPlugin_method_get_script_create_dialog>`{.interpreted-text
role="ref"}

Gets the Editor\'s dialog used for making scripts.

\*\*Note:\*\* Users can configure it before use.

\*\*Warning:\*\* Removing and freeing this node will render a part of
the editor useless and may cause a crash.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_get_undo_redo}
::: rst-class
classref-method
:::
::::

`EditorUndoRedoManager<class_EditorUndoRedoManager>`{.interpreted-text
role="ref"} **get_undo_redo**()
`🔗<class_EditorPlugin_method_get_undo_redo>`{.interpreted-text
role="ref"}

Gets the undo/redo object. Most actions in the editor can be undoable,
so use this object to make sure this happens when it\'s worth it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_hide_bottom_panel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**hide_bottom_panel**()
`🔗<class_EditorPlugin_method_hide_bottom_panel>`{.interpreted-text
role="ref"}

Minimizes the bottom panel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_make_bottom_panel_item_visible}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**make_bottom_panel_item_visible**(item:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_make_bottom_panel_item_visible>`{.interpreted-text
role="ref"}

Makes a specific item in the bottom panel visible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_queue_save_layout}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_save_layout**()
`🔗<class_EditorPlugin_method_queue_save_layout>`{.interpreted-text
role="ref"}

Queue save the project\'s editor layout.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_autoload_singleton}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_autoload_singleton**(name:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_remove_autoload_singleton>`{.interpreted-text
role="ref"}

Removes an Autoload `name` from the list.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_context_menu_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_context_menu_plugin**(plugin:
`EditorContextMenuPlugin<class_EditorContextMenuPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_context_menu_plugin>`{.interpreted-text
role="ref"}

Removes the specified context menu plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_control_from_bottom_panel}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_control_from_bottom_panel**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_remove_control_from_bottom_panel>`{.interpreted-text
role="ref"}

Removes the control from the bottom panel. You have to manually
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} the control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_control_from_container}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_control_from_container**(container:
`CustomControlContainer<enum_EditorPlugin_CustomControlContainer>`{.interpreted-text
role="ref"}, control: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_control_from_container>`{.interpreted-text
role="ref"}

Removes the control from the specified container. You have to manually
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} the control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_control_from_docks}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_control_from_docks**(control:
`Control<class_Control>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_remove_control_from_docks>`{.interpreted-text
role="ref"}

Removes the control from the dock. You have to manually
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} the control.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_custom_type}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_custom_type**(type: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_custom_type>`{.interpreted-text
role="ref"}

Removes a custom type added by
`add_custom_type()<class_EditorPlugin_method_add_custom_type>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_debugger_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_debugger_plugin**(script:
`EditorDebuggerPlugin<class_EditorDebuggerPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_debugger_plugin>`{.interpreted-text
role="ref"}

Removes the debugger plugin with given script from the Debugger.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_export_platform}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_export_platform**(platform:
`EditorExportPlatform<class_EditorExportPlatform>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_export_platform>`{.interpreted-text
role="ref"}

Removes an export platform registered by
`add_export_platform()<class_EditorPlugin_method_add_export_platform>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_export_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_export_plugin**(plugin:
`EditorExportPlugin<class_EditorExportPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_export_plugin>`{.interpreted-text
role="ref"}

Removes an export plugin registered by
`add_export_plugin()<class_EditorPlugin_method_add_export_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_import_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_import_plugin**(importer:
`EditorImportPlugin<class_EditorImportPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_import_plugin>`{.interpreted-text
role="ref"}

Removes an import plugin registered by
`add_import_plugin()<class_EditorPlugin_method_add_import_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_inspector_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_inspector_plugin**(plugin:
`EditorInspectorPlugin<class_EditorInspectorPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_inspector_plugin>`{.interpreted-text
role="ref"}

Removes an inspector plugin registered by
`add_inspector_plugin()<class_EditorPlugin_method_add_inspector_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_node_3d_gizmo_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_node_3d_gizmo_plugin**(plugin:
`EditorNode3DGizmoPlugin<class_EditorNode3DGizmoPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_node_3d_gizmo_plugin>`{.interpreted-text
role="ref"}

Removes a gizmo plugin registered by
`add_node_3d_gizmo_plugin()<class_EditorPlugin_method_add_node_3d_gizmo_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_resource_conversion_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_resource_conversion_plugin**(plugin:
`EditorResourceConversionPlugin<class_EditorResourceConversionPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_resource_conversion_plugin>`{.interpreted-text
role="ref"}

Removes a resource conversion plugin registered by
`add_resource_conversion_plugin()<class_EditorPlugin_method_add_resource_conversion_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_scene_format_importer_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_scene_format_importer_plugin**(scene_format_importer:
`EditorSceneFormatImporter<class_EditorSceneFormatImporter>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_scene_format_importer_plugin>`{.interpreted-text
role="ref"}

Removes a scene format importer registered by
`add_scene_format_importer_plugin()<class_EditorPlugin_method_add_scene_format_importer_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_scene_post_import_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_scene_post_import_plugin**(scene_import_plugin:
`EditorScenePostImportPlugin<class_EditorScenePostImportPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_scene_post_import_plugin>`{.interpreted-text
role="ref"}

Remove the
`EditorScenePostImportPlugin<class_EditorScenePostImportPlugin>`{.interpreted-text
role="ref"}, added with
`add_scene_post_import_plugin()<class_EditorPlugin_method_add_scene_post_import_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_tool_menu_item}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_tool_menu_item**(name: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_tool_menu_item>`{.interpreted-text
role="ref"}

Removes a menu `name` from **Project \> Tools**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_translation_parser_plugin}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_translation_parser_plugin**(parser:
`EditorTranslationParserPlugin<class_EditorTranslationParserPlugin>`{.interpreted-text
role="ref"})
`🔗<class_EditorPlugin_method_remove_translation_parser_plugin>`{.interpreted-text
role="ref"}

Removes a custom translation parser plugin registered by
`add_translation_parser_plugin()<class_EditorPlugin_method_add_translation_parser_plugin>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_remove_undo_redo_inspector_hook_callback}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_undo_redo_inspector_hook_callback**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_remove_undo_redo_inspector_hook_callback>`{.interpreted-text
role="ref"}

Removes a callback previously added by
`add_undo_redo_inspector_hook_callback()<class_EditorPlugin_method_add_undo_redo_inspector_hook_callback>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_set_dock_tab_icon}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_dock_tab_icon**(control:
`Control<class_Control>`{.interpreted-text role="ref"}, icon:
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
`🔗<class_EditorPlugin_method_set_dock_tab_icon>`{.interpreted-text
role="ref"}

Sets the tab icon for the given control in a dock slot. Setting to
`null` removes the icon.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_set_force_draw_over_forwarding_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_force_draw_over_forwarding_enabled**()
`🔗<class_EditorPlugin_method_set_force_draw_over_forwarding_enabled>`{.interpreted-text
role="ref"}

Enables calling of
`_forward_canvas_force_draw_over_viewport()<class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport>`{.interpreted-text
role="ref"} for the 2D editor and
`_forward_3d_force_draw_over_viewport()<class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport>`{.interpreted-text
role="ref"} for the 3D editor when their viewports are updated. You need
to call this method only once and it will work permanently for this
plugin.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_set_input_event_forwarding_always_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input_event_forwarding_always_enabled**()
`🔗<class_EditorPlugin_method_set_input_event_forwarding_always_enabled>`{.interpreted-text
role="ref"}

Use this method if you always want to receive inputs from 3D view screen
inside
`_forward_3d_gui_input()<class_EditorPlugin_private_method__forward_3d_gui_input>`{.interpreted-text
role="ref"}. It might be especially usable if your plugin will want to
use raycast in the scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorPlugin_method_update_overlays}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **update_overlays**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorPlugin_method_update_overlays>`{.interpreted-text
role="ref"}

Updates the overlays of the 2D and 3D editor viewport. Causes methods
`_forward_canvas_draw_over_viewport()<class_EditorPlugin_private_method__forward_canvas_draw_over_viewport>`{.interpreted-text
role="ref"},
`_forward_canvas_force_draw_over_viewport()<class_EditorPlugin_private_method__forward_canvas_force_draw_over_viewport>`{.interpreted-text
role="ref"},
`_forward_3d_draw_over_viewport()<class_EditorPlugin_private_method__forward_3d_draw_over_viewport>`{.interpreted-text
role="ref"} and
`_forward_3d_force_draw_over_viewport()<class_EditorPlugin_private_method__forward_3d_force_draw_over_viewport>`{.interpreted-text
role="ref"} to be called.
