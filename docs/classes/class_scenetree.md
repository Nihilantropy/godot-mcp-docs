github_url
:   hide

# SceneTree {#class_SceneTree}

**Inherits:** `MainLoop<class_MainLoop>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Manages the game loop via a hierarchy of nodes.

::: rst-class
classref-introduction-group
:::

## Description

As one of the most important classes, the **SceneTree** manages the
hierarchy of nodes in a scene, as well as scenes themselves. Nodes can
be added, fetched and removed. The whole scene tree (and thus the
current scene) can be paused. Scenes can be loaded, switched and
reloaded.

You can also use the **SceneTree** to organize your nodes into
**groups**: every node can be added to as many groups as you want to
create, e.g. an \"enemy\" group. You can then iterate these groups or
even call methods and set properties on all the nodes belonging to any
given group.

\*\*SceneTree\*\* is the default
`MainLoop<class_MainLoop>`{.interpreted-text role="ref"} implementation
used by the engine, and is thus in charge of the game loop.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `SceneTree <../tutorials/scripting/scene_tree>`{.interpreted-text
  role="doc"}
- `Multiple resolutions <../tutorials/rendering/multiple_resolutions>`{.interpreted-text
  role="doc"}

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

:::: {#class_SceneTree_signal_node_added}
::: rst-class
classref-signal
:::
::::

**node_added**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_SceneTree_signal_node_added>`{.interpreted-text role="ref"}

Emitted when the `node` enters this tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_node_configuration_warning_changed}
::: rst-class
classref-signal
:::
::::

**node_configuration_warning_changed**(node:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_SceneTree_signal_node_configuration_warning_changed>`{.interpreted-text
role="ref"}

Emitted when the `node`\'s
`Node.update_configuration_warnings()<class_Node_method_update_configuration_warnings>`{.interpreted-text
role="ref"} is called. Only emitted in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_node_removed}
::: rst-class
classref-signal
:::
::::

**node_removed**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_SceneTree_signal_node_removed>`{.interpreted-text role="ref"}

Emitted when the `node` exits this tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_node_renamed}
::: rst-class
classref-signal
:::
::::

**node_renamed**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_SceneTree_signal_node_renamed>`{.interpreted-text role="ref"}

Emitted when the `node`\'s
`Node.name<class_Node_property_name>`{.interpreted-text role="ref"} is
changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_physics_frame}
::: rst-class
classref-signal
:::
::::

**physics_frame**()
`🔗<class_SceneTree_signal_physics_frame>`{.interpreted-text role="ref"}

Emitted immediately before
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} is called on every node in this tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_process_frame}
::: rst-class
classref-signal
:::
::::

**process_frame**()
`🔗<class_SceneTree_signal_process_frame>`{.interpreted-text role="ref"}

Emitted immediately before
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} is called on every node in this tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_scene_changed}
::: rst-class
classref-signal
:::
::::

**scene_changed**()
`🔗<class_SceneTree_signal_scene_changed>`{.interpreted-text role="ref"}

Emitted after the new scene is added to scene tree and initialized. Can
be used to reliably access
`current_scene<class_SceneTree_property_current_scene>`{.interpreted-text
role="ref"} when changing scenes.

    # This code should be inside an autoload.
    get_tree().change_scene_to_file(other_scene_path)
    await get_tree().scene_changed
    print(get_tree().current_scene) # Prints the new scene.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_tree_changed}
::: rst-class
classref-signal
:::
::::

**tree_changed**()
`🔗<class_SceneTree_signal_tree_changed>`{.interpreted-text role="ref"}

Emitted any time the tree\'s hierarchy changes (nodes being moved,
renamed, etc.).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_signal_tree_process_mode_changed}
::: rst-class
classref-signal
:::
::::

**tree_process_mode_changed**()
`🔗<class_SceneTree_signal_tree_process_mode_changed>`{.interpreted-text
role="ref"}

Emitted when the
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} of any node inside the tree is changed. Only emitted in the
editor, to update the visibility of disabled nodes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_SceneTree_GroupCallFlags}
::: rst-class
classref-enumeration
:::
::::

enum **GroupCallFlags**:
`🔗<enum_SceneTree_GroupCallFlags>`{.interpreted-text role="ref"}

:::: {#class_SceneTree_constant_GROUP_CALL_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`GroupCallFlags<enum_SceneTree_GroupCallFlags>`{.interpreted-text
role="ref"} **GROUP_CALL_DEFAULT** = `0`

Call nodes within a group with no special behavior (default).

:::: {#class_SceneTree_constant_GROUP_CALL_REVERSE}
::: rst-class
classref-enumeration-constant
:::
::::

`GroupCallFlags<enum_SceneTree_GroupCallFlags>`{.interpreted-text
role="ref"} **GROUP_CALL_REVERSE** = `1`

Call nodes within a group in reverse tree hierarchy order (all nested
children are called before their respective parent nodes).

:::: {#class_SceneTree_constant_GROUP_CALL_DEFERRED}
::: rst-class
classref-enumeration-constant
:::
::::

`GroupCallFlags<enum_SceneTree_GroupCallFlags>`{.interpreted-text
role="ref"} **GROUP_CALL_DEFERRED** = `2`

Call nodes within a group at the end of the current frame (can be either
process or physics frame), similar to
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"}.

:::: {#class_SceneTree_constant_GROUP_CALL_UNIQUE}
::: rst-class
classref-enumeration-constant
:::
::::

`GroupCallFlags<enum_SceneTree_GroupCallFlags>`{.interpreted-text
role="ref"} **GROUP_CALL_UNIQUE** = `4`

Call nodes within a group only once, even if the call is executed many
times in the same frame. Must be combined with
`GROUP_CALL_DEFERRED<class_SceneTree_constant_GROUP_CALL_DEFERRED>`{.interpreted-text
role="ref"} to work.

\*\*Note:\*\* Different arguments are not taken into account. Therefore,
when the same call is executed with different arguments, only the first
call will be performed.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SceneTree_property_auto_accept_quit}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **auto_accept_quit** =
`true` `🔗<class_SceneTree_property_auto_accept_quit>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_accept_quit**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_auto_accept_quit**()

If `true`, the application automatically accepts quitting requests.

For mobile platforms, see
`quit_on_go_back<class_SceneTree_property_quit_on_go_back>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_current_scene}
::: rst-class
classref-property
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **current_scene**
`🔗<class_SceneTree_property_current_scene>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_scene**(value: `Node<class_Node>`{.interpreted-text
  role="ref"})
- `Node<class_Node>`{.interpreted-text role="ref"}
  **get_current_scene**()

The root node of the currently loaded main scene, usually as a direct
child of `root<class_SceneTree_property_root>`{.interpreted-text
role="ref"}. See also
`change_scene_to_file()<class_SceneTree_method_change_scene_to_file>`{.interpreted-text
role="ref"},
`change_scene_to_packed()<class_SceneTree_method_change_scene_to_packed>`{.interpreted-text
role="ref"}, and
`reload_current_scene()<class_SceneTree_method_reload_current_scene>`{.interpreted-text
role="ref"}.

\*\*Warning:\*\* Setting this property directly may not work as
expected, as it does *not* add or remove any nodes from this tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_debug_collisions_hint}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug_collisions_hint** = `false`
`🔗<class_SceneTree_property_debug_collisions_hint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_collisions_hint**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_debugging_collisions_hint**()

If `true`, collision shapes will be visible when running the game from
the editor for debugging purposes.

\*\*Note:\*\* This property is not designed to be changed at run-time.
Changing the value of
`debug_collisions_hint<class_SceneTree_property_debug_collisions_hint>`{.interpreted-text
role="ref"} while the project is running will not have the desired
effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_debug_navigation_hint}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**debug_navigation_hint** = `false`
`🔗<class_SceneTree_property_debug_navigation_hint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_navigation_hint**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_debugging_navigation_hint**()

If `true`, navigation polygons will be visible when running the game
from the editor for debugging purposes.

\*\*Note:\*\* This property is not designed to be changed at run-time.
Changing the value of
`debug_navigation_hint<class_SceneTree_property_debug_navigation_hint>`{.interpreted-text
role="ref"} while the project is running will not have the desired
effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_debug_paths_hint}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **debug_paths_hint** =
`false`
`🔗<class_SceneTree_property_debug_paths_hint>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_paths_hint**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_debugging_paths_hint**()

If `true`, curves from `Path2D<class_Path2D>`{.interpreted-text
role="ref"} and `Path3D<class_Path3D>`{.interpreted-text role="ref"}
nodes will be visible when running the game from the editor for
debugging purposes.

\*\*Note:\*\* This property is not designed to be changed at run-time.
Changing the value of
`debug_paths_hint<class_SceneTree_property_debug_paths_hint>`{.interpreted-text
role="ref"} while the project is running will not have the desired
effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_edited_scene_root}
::: rst-class
classref-property
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **edited_scene_root**
`🔗<class_SceneTree_property_edited_scene_root>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_edited_scene_root**(value: `Node<class_Node>`{.interpreted-text
  role="ref"})
- `Node<class_Node>`{.interpreted-text role="ref"}
  **get_edited_scene_root**()

The root of the scene currently being edited in the editor. This is
usually a direct child of
`root<class_SceneTree_property_root>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This property does nothing in release builds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_multiplayer_poll}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **multiplayer_poll** =
`true` `🔗<class_SceneTree_property_multiplayer_poll>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_multiplayer_poll_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_multiplayer_poll_enabled**()

If `true` (default value), enables automatic polling of the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"} for
this SceneTree during
`process_frame<class_SceneTree_signal_process_frame>`{.interpreted-text
role="ref"}.

If `false`, you need to manually call
`MultiplayerAPI.poll()<class_MultiplayerAPI_method_poll>`{.interpreted-text
role="ref"} to process network packets and deliver RPCs. This allows
running RPCs in a different loop (e.g. physics, thread, specific time
step) and for manual `Mutex<class_Mutex>`{.interpreted-text role="ref"}
protection when accessing the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
from threads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_paused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **paused** = `false`
`🔗<class_SceneTree_property_paused>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pause**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_paused**()

If `true`, the scene tree is considered paused. This causes the
following behavior:

- 2D and 3D physics will be stopped, as well as collision detection and
  related signals.
- Depending on each node\'s
  `Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
  role="ref"}, their
  `Node._process()<class_Node_private_method__process>`{.interpreted-text
  role="ref"},
  `Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
  role="ref"} and
  `Node._input()<class_Node_private_method__input>`{.interpreted-text
  role="ref"} callback methods may not called anymore.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_physics_interpolation}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics_interpolation** = `false`
`🔗<class_SceneTree_property_physics_interpolation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_interpolation_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_physics_interpolation_enabled**()

If `true`, the renderer will interpolate the transforms of objects (both
physics and non-physics) between the last two transforms, so that smooth
motion is seen even when physics ticks do not coincide with rendered
frames.

The default value of this property is controlled by
`ProjectSettings.physics/common/physics_interpolation<class_ProjectSettings_property_physics/common/physics_interpolation>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Although this is a global setting, finer control of
individual branches of the **SceneTree** is possible using
`Node.physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_quit_on_go_back}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **quit_on_go_back** =
`true` `🔗<class_SceneTree_property_quit_on_go_back>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_quit_on_go_back**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_quit_on_go_back**()

If `true`, the application quits automatically when navigating back
(e.g. using the system \"Back\" button on Android).

To handle \'Go Back\' button when this option is disabled, use
`DisplayServer.WINDOW_EVENT_GO_BACK_REQUEST<class_DisplayServer_constant_WINDOW_EVENT_GO_BACK_REQUEST>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_property_root}
::: rst-class
classref-property
:::
::::

`Window<class_Window>`{.interpreted-text role="ref"} **root**
`🔗<class_SceneTree_property_root>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `Window<class_Window>`{.interpreted-text role="ref"} **get_root**()

The tree\'s root `Window<class_Window>`{.interpreted-text role="ref"}.
This is top-most `Node<class_Node>`{.interpreted-text role="ref"} of the
scene tree, and is always present. An absolute
`NodePath<class_NodePath>`{.interpreted-text role="ref"} always starts
from this node. Children of the root node may include the loaded
`current_scene<class_SceneTree_property_current_scene>`{.interpreted-text
role="ref"}, as well as any
`AutoLoad <../tutorials/scripting/singletons_autoload>`{.interpreted-text
role="doc"} configured in the Project Settings.

\*\*Warning:\*\* Do not delete this node. This will result in unstable
behavior, followed by a crash.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_SceneTree_method_call_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**call_group**(group: `StringName<class_StringName>`{.interpreted-text
role="ref"}, method: `StringName<class_StringName>`{.interpreted-text
role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_SceneTree_method_call_group>`{.interpreted-text
role="ref"}

Calls `method` on each node inside this tree added to the given `group`.
You can pass arguments to `method` by specifying them at the end of this
method call. Nodes that cannot call `method` (either because the method
doesn\'t exist or the arguments do not match) are ignored. See also
`set_group()<class_SceneTree_method_set_group>`{.interpreted-text
role="ref"} and
`notify_group()<class_SceneTree_method_notify_group>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method acts immediately on all selected nodes at
once, which may cause stuttering in some performance-intensive
situations.

\*\*Note:\*\* In C#, `method` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`MethodName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_call_group_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**call_group_flags**(flags: `int<class_int>`{.interpreted-text
role="ref"}, group: `StringName<class_StringName>`{.interpreted-text
role="ref"}, method: `StringName<class_StringName>`{.interpreted-text
role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneTree_method_call_group_flags>`{.interpreted-text
role="ref"}

Calls the given `method` on each node inside this tree added to the
given `group`. Use `flags` to customize this method\'s behavior (see
`GroupCallFlags<enum_SceneTree_GroupCallFlags>`{.interpreted-text
role="ref"}). Additional arguments for `method` can be passed at the end
of this method. Nodes that cannot call `method` (either because the
method doesn\'t exist or the arguments do not match) are ignored.

    # Calls "hide" to all nodes of the "enemies" group, at the end of the frame and in reverse tree order.
    get_tree().call_group_flags(
            SceneTree.GROUP_CALL_DEFERRED | SceneTree.GROUP_CALL_REVERSE,
            "enemies", "hide")

\*\*Note:\*\* In C#, `method` must be in snake_case when referring to
built-in Godot methods. Prefer using the names exposed in the
`MethodName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_change_scene_to_file}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**change_scene_to_file**(path: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_SceneTree_method_change_scene_to_file>`{.interpreted-text
role="ref"}

Changes the running scene to the one at the given `path`, after loading
it into a `PackedScene<class_PackedScene>`{.interpreted-text role="ref"}
and creating a new instance.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success,
`@GlobalScope.ERR_CANT_OPEN<class_@GlobalScope_constant_ERR_CANT_OPEN>`{.interpreted-text
role="ref"} if the `path` cannot be loaded into a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}, or
`@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>`{.interpreted-text
role="ref"} if that scene cannot be instantiated.

\*\*Note:\*\* See
`change_scene_to_packed()<class_SceneTree_method_change_scene_to_packed>`{.interpreted-text
role="ref"} for details on the order of operations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_change_scene_to_packed}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**change_scene_to_packed**(packed_scene:
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"})
`🔗<class_SceneTree_method_change_scene_to_packed>`{.interpreted-text
role="ref"}

Changes the running scene to a new instance of the given
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"} (which
must be valid).

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success,
`@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>`{.interpreted-text
role="ref"} if the scene cannot be instantiated, or
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if the scene is invalid.

\*\*Note:\*\* Operations happen in the following order when
`change_scene_to_packed()<class_SceneTree_method_change_scene_to_packed>`{.interpreted-text
role="ref"} is called:

1.  The current scene node is immediately removed from the tree. From
    that point,
    `Node.get_tree()<class_Node_method_get_tree>`{.interpreted-text
    role="ref"} called on the current (outgoing) scene will return
    `null`.
    `current_scene<class_SceneTree_property_current_scene>`{.interpreted-text
    role="ref"} will be `null`, too, because the new scene is not
    available yet.
2.  At the end of the frame, the formerly current scene, already removed
    from the tree, will be deleted (freed from memory) and then the new
    scene will be instantiated and added to the tree.
    `Node.get_tree()<class_Node_method_get_tree>`{.interpreted-text
    role="ref"} and
    `current_scene<class_SceneTree_property_current_scene>`{.interpreted-text
    role="ref"} will be back to working as usual.

This ensures that both scenes aren\'t running at the same time, while
still freeing the previous scene in a safe way similar to
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}.

If you want to reliably access the new scene, await the
`scene_changed<class_SceneTree_signal_scene_changed>`{.interpreted-text
role="ref"} signal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_create_timer}
::: rst-class
classref-method
:::
::::

`SceneTreeTimer<class_SceneTreeTimer>`{.interpreted-text role="ref"}
**create_timer**(time_sec: `float<class_float>`{.interpreted-text
role="ref"}, process_always: `bool<class_bool>`{.interpreted-text
role="ref"} = true, process_in_physics:
`bool<class_bool>`{.interpreted-text role="ref"} = false,
ignore_time_scale: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_SceneTree_method_create_timer>`{.interpreted-text
role="ref"}

Returns a new `SceneTreeTimer<class_SceneTreeTimer>`{.interpreted-text
role="ref"}. After `time_sec` in seconds have passed, the timer will
emit
`SceneTreeTimer.timeout<class_SceneTreeTimer_signal_timeout>`{.interpreted-text
role="ref"} and will be automatically freed.

If `process_always` is `false`, the timer will be paused when setting
`paused<class_SceneTree_property_paused>`{.interpreted-text role="ref"}
to `true`.

If `process_in_physics` is `true`, the timer will update at the end of
the physics frame, instead of the process frame.

If `ignore_time_scale` is `true`, the timer will ignore
`Engine.time_scale<class_Engine_property_time_scale>`{.interpreted-text
role="ref"} and update with the real, elapsed time.

This method is commonly used to create a one-shot delay timer, as in the
following example:

::::: tabs
::: code-tab
gdscript

func some_function():

:   print(\"start\") await get_tree().create_timer(1.0).timeout
    print(\"end\")
:::

::: code-tab
csharp

public async Task SomeFunction() { GD.Print(\"start\"); await
ToSignal(GetTree().CreateTimer(1.0f),
SceneTreeTimer.SignalName.Timeout); GD.Print(\"end\"); }
:::
:::::

\*\*Note:\*\* The timer is always updated *after* all of the nodes in
the tree. A node\'s
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} method would be called before the timer updates (or
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} if `process_in_physics` is set to `true`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_create_tween}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **create_tween**()
`🔗<class_SceneTree_method_create_tween>`{.interpreted-text role="ref"}

Creates and returns a new `Tween<class_Tween>`{.interpreted-text
role="ref"} processed in this tree. The Tween will start automatically
on the next process frame or physics frame (depending on its
`TweenProcessMode<enum_Tween_TweenProcessMode>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* A `Tween<class_Tween>`{.interpreted-text role="ref"}
created using this method is not bound to any
`Node<class_Node>`{.interpreted-text role="ref"}. It may keep working
until there is nothing left to animate. If you want the
`Tween<class_Tween>`{.interpreted-text role="ref"} to be automatically
killed when the `Node<class_Node>`{.interpreted-text role="ref"} is
freed, use
`Node.create_tween()<class_Node_method_create_tween>`{.interpreted-text
role="ref"} or
`Tween.bind_node()<class_Tween_method_bind_node>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_get_first_node_in_group}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**get_first_node_in_group**(group:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SceneTree_method_get_first_node_in_group>`{.interpreted-text
role="ref"}

Returns the first `Node<class_Node>`{.interpreted-text role="ref"} found
inside the tree, that has been added to the given `group`, in scene
hierarchy order. Returns `null` if no match is found. See also
`get_nodes_in_group()<class_SceneTree_method_get_nodes_in_group>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_get_frame}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_frame**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_SceneTree_method_get_frame>`{.interpreted-text
role="ref"}

Returns how many physics process steps have been processed, since the
application started. This is *not* a measurement of elapsed time. See
also
`physics_frame<class_SceneTree_signal_physics_frame>`{.interpreted-text
role="ref"}. For the number of frames rendered, see
`Engine.get_process_frames()<class_Engine_method_get_process_frames>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_get_multiplayer}
::: rst-class
classref-method
:::
::::

`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
**get_multiplayer**(for_path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"} =
NodePath(\"\"))
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneTree_method_get_multiplayer>`{.interpreted-text
role="ref"}

Searches for the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
configured for the given path, if one does not exist it searches the
parent paths until one is found. If the path is empty, or none is found,
the default one is returned. See
`set_multiplayer()<class_SceneTree_method_set_multiplayer>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_get_node_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_node_count**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneTree_method_get_node_count>`{.interpreted-text
role="ref"}

Returns the number of nodes inside this tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_get_node_count_in_group}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_node_count_in_group**(group:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneTree_method_get_node_count_in_group>`{.interpreted-text
role="ref"}

Returns the number of nodes assigned to the given group.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_get_nodes_in_group}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node<class_Node>`{.interpreted-text role="ref"}\]
**get_nodes_in_group**(group:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SceneTree_method_get_nodes_in_group>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} containing
all nodes inside this tree, that have been added to the given `group`,
in scene hierarchy order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_get_processed_tweens}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Tween<class_Tween>`{.interpreted-text role="ref"}\]
**get_processed_tweens**()
`🔗<class_SceneTree_method_get_processed_tweens>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of
currently existing `Tween<class_Tween>`{.interpreted-text role="ref"}s
in the tree, including paused tweens.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_has_group}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_group**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_SceneTree_method_has_group>`{.interpreted-text
role="ref"}

Returns `true` if a node added to the given group `name` exists in the
tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_is_accessibility_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_accessibility_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneTree_method_is_accessibility_enabled>`{.interpreted-text
role="ref"}

Returns `true` if accessibility features are enabled, and accessibility
information updates are actively processed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_is_accessibility_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_accessibility_supported**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SceneTree_method_is_accessibility_supported>`{.interpreted-text
role="ref"}

Returns `true` if accessibility features are supported by the OS and
enabled in project settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_notify_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_group**(group: `StringName<class_StringName>`{.interpreted-text
role="ref"}, notification: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_SceneTree_method_notify_group>`{.interpreted-text
role="ref"}

Calls
`Object.notification()<class_Object_method_notification>`{.interpreted-text
role="ref"} with the given `notification` to all nodes inside this tree
added to the `group`. See also
`Godot notifications <../tutorials/best_practices/godot_notifications>`{.interpreted-text
role="doc"} and
`call_group()<class_SceneTree_method_call_group>`{.interpreted-text
role="ref"} and
`set_group()<class_SceneTree_method_set_group>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method acts immediately on all selected nodes at
once, which may cause stuttering in some performance-intensive
situations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_notify_group_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_group_flags**(call_flags: `int<class_int>`{.interpreted-text
role="ref"}, group: `StringName<class_StringName>`{.interpreted-text
role="ref"}, notification: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_SceneTree_method_notify_group_flags>`{.interpreted-text
role="ref"}

Calls
`Object.notification()<class_Object_method_notification>`{.interpreted-text
role="ref"} with the given `notification` to all nodes inside this tree
added to the `group`. Use `call_flags` to customize this method\'s
behavior (see
`GroupCallFlags<enum_SceneTree_GroupCallFlags>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_queue_delete}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_delete**(obj: `Object<class_Object>`{.interpreted-text
role="ref"}) `🔗<class_SceneTree_method_queue_delete>`{.interpreted-text
role="ref"}

Queues the given `obj` to be deleted, calling its
`Object.free()<class_Object_method_free>`{.interpreted-text role="ref"}
at the end of the current frame. This method is similar to
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_quit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**quit**(exit_code: `int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_SceneTree_method_quit>`{.interpreted-text role="ref"}

Quits the application at the end of the current iteration, with the
given `exit_code`.

By convention, an exit code of `0` indicates success, whereas any other
exit code indicates an error. For portability reasons, it should be
between `0` and `125` (inclusive).

\*\*Note:\*\* On iOS this method doesn\'t work. Instead, as recommended
by the [iOS Human Interface
Guidelines](https://developer.apple.com/library/archive/qa/qa1561/_index.html),
the user is expected to close apps via the Home button.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_reload_current_scene}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**reload_current_scene**()
`🔗<class_SceneTree_method_reload_current_scene>`{.interpreted-text
role="ref"}

Reloads the currently active scene, replacing
`current_scene<class_SceneTree_property_current_scene>`{.interpreted-text
role="ref"} with a new instance of its original
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success,
`@GlobalScope.ERR_UNCONFIGURED<class_@GlobalScope_constant_ERR_UNCONFIGURED>`{.interpreted-text
role="ref"} if no
`current_scene<class_SceneTree_property_current_scene>`{.interpreted-text
role="ref"} is defined,
`@GlobalScope.ERR_CANT_OPEN<class_@GlobalScope_constant_ERR_CANT_OPEN>`{.interpreted-text
role="ref"} if
`current_scene<class_SceneTree_property_current_scene>`{.interpreted-text
role="ref"} cannot be loaded into a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}, or
`@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>`{.interpreted-text
role="ref"} if the scene cannot be instantiated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_set_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_group**(group: `StringName<class_StringName>`{.interpreted-text
role="ref"}, property: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_SceneTree_method_set_group>`{.interpreted-text
role="ref"}

Sets the given `property` to `value` on all nodes inside this tree added
to the given `group`. Nodes that do not have the `property` are ignored.
See also
`call_group()<class_SceneTree_method_call_group>`{.interpreted-text
role="ref"} and
`notify_group()<class_SceneTree_method_notify_group>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method acts immediately on all selected nodes at
once, which may cause stuttering in some performance-intensive
situations.

\*\*Note:\*\* In C#, `property` must be in snake_case when referring to
built-in Godot properties. Prefer using the names exposed in the
`PropertyName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_set_group_flags}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_group_flags**(call_flags: `int<class_int>`{.interpreted-text
role="ref"}, group: `StringName<class_StringName>`{.interpreted-text
role="ref"}, property: `String<class_String>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_SceneTree_method_set_group_flags>`{.interpreted-text
role="ref"}

Sets the given `property` to `value` on all nodes inside this tree added
to the given `group`. Nodes that do not have the `property` are ignored.
Use `call_flags` to customize this method\'s behavior (see
`GroupCallFlags<enum_SceneTree_GroupCallFlags>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* In C#, `property` must be in snake_case when referring to
built-in Godot properties. Prefer using the names exposed in the
`PropertyName` class to avoid allocating a new
`StringName<class_StringName>`{.interpreted-text role="ref"} on each
call.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_set_multiplayer}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_multiplayer**(multiplayer:
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"},
root_path: `NodePath<class_NodePath>`{.interpreted-text role="ref"} =
NodePath(\"\"))
`🔗<class_SceneTree_method_set_multiplayer>`{.interpreted-text
role="ref"}

Sets a custom `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text
role="ref"} with the given `root_path` (controlling also the relative
subpaths), or override the default one if `root_path` is empty.

\*\*Note:\*\* No
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
must be configured for the subpath containing `root_path`, nested custom
multiplayers are not allowed. I.e. if one is configured for
`"/root/Foo"` setting one for `"/root/Foo/Bar"` will cause an error.

\*\*Note:\*\*
`set_multiplayer()<class_SceneTree_method_set_multiplayer>`{.interpreted-text
role="ref"} should be called *before* the child nodes are ready at the
given `root_path`. If multiplayer nodes like
`MultiplayerSpawner<class_MultiplayerSpawner>`{.interpreted-text
role="ref"} or
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"} are added to the tree before the custom multiplayer API is
set, they will not work.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SceneTree_method_unload_current_scene}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**unload_current_scene**()
`🔗<class_SceneTree_method_unload_current_scene>`{.interpreted-text
role="ref"}

If a current scene is loaded, calling this method will unload it.
