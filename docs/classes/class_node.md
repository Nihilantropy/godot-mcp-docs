github_url
:   hide

# Node {#class_Node}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimationMixer<class_AnimationMixer>`{.interpreted-text role="ref"},
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"}, `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"}, `CanvasLayer<class_CanvasLayer>`{.interpreted-text
role="ref"},
`EditorFileSystem<class_EditorFileSystem>`{.interpreted-text
role="ref"}, `EditorPlugin<class_EditorPlugin>`{.interpreted-text
role="ref"},
`EditorResourcePreview<class_EditorResourcePreview>`{.interpreted-text
role="ref"}, `HTTPRequest<class_HTTPRequest>`{.interpreted-text
role="ref"},
`InstancePlaceholder<class_InstancePlaceholder>`{.interpreted-text
role="ref"}, `MissingNode<class_MissingNode>`{.interpreted-text
role="ref"},
`MultiplayerSpawner<class_MultiplayerSpawner>`{.interpreted-text
role="ref"},
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"},
`NavigationAgent2D<class_NavigationAgent2D>`{.interpreted-text
role="ref"},
`NavigationAgent3D<class_NavigationAgent3D>`{.interpreted-text
role="ref"}, `Node3D<class_Node3D>`{.interpreted-text role="ref"},
`ResourcePreloader<class_ResourcePreloader>`{.interpreted-text
role="ref"},
`ShaderGlobalsOverride<class_ShaderGlobalsOverride>`{.interpreted-text
role="ref"}, `StatusIndicator<class_StatusIndicator>`{.interpreted-text
role="ref"}, `Timer<class_Timer>`{.interpreted-text role="ref"},
`Viewport<class_Viewport>`{.interpreted-text role="ref"},
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text role="ref"}

Base class for all scene objects.

::: rst-class
classref-introduction-group
:::

## Description

Nodes are Godot\'s building blocks. They can be assigned as the child of
another node, resulting in a tree arrangement. A given node can contain
any number of nodes as children with the requirement that all siblings
(direct children of a node) should have unique names.

A tree of nodes is called a *scene*. Scenes can be saved to the disk and
then instantiated into other scenes. This allows for very high
flexibility in the architecture and data model of Godot projects.

\*\*Scene tree:\*\* The `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"} contains the active tree of nodes. When a node is added to
the scene tree, it receives the
`NOTIFICATION_ENTER_TREE<class_Node_constant_NOTIFICATION_ENTER_TREE>`{.interpreted-text
role="ref"} notification and its
`_enter_tree()<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"} callback is triggered. Child nodes are always added *after*
their parent node, i.e. the
`_enter_tree()<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"} callback of a parent node will be triggered before its
child\'s.

Once all nodes have been added in the scene tree, they receive the
`NOTIFICATION_READY<class_Node_constant_NOTIFICATION_READY>`{.interpreted-text
role="ref"} notification and their respective
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} callbacks are triggered. For groups of nodes, the
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} callback is called in reverse order, starting with the
children and moving up to the parent nodes.

This means that when adding a node to the scene tree, the following
order will be used for the callbacks:
`_enter_tree()<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"} of the parent,
`_enter_tree()<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"} of the children,
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} of the children and finally
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} of the parent (recursively for the entire scene tree).

\*\*Processing:\*\* Nodes can override the \"process\" state, so that
they receive a callback on each frame requesting them to process (do
something). Normal processing (callback
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, toggled with
`set_process()<class_Node_method_set_process>`{.interpreted-text
role="ref"}) happens as fast as possible and is dependent on the frame
rate, so the processing time *delta* (in seconds) is passed as an
argument. Physics processing (callback
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}, toggled with
`set_physics_process()<class_Node_method_set_physics_process>`{.interpreted-text
role="ref"}) happens a fixed number of times per second (60 by default)
and is useful for code related to the physics engine.

Nodes can also process input events. When present, the
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} function will be called for each input that the program
receives. In many cases, this can be overkill (unless used for simple
projects), and the
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} function might be preferred; it is called when the input
event was not handled by anyone else (typically, GUI
`Control<class_Control>`{.interpreted-text role="ref"} nodes), ensuring
that the node only receives the events that were meant for it.

To keep track of the scene hierarchy (especially when instantiating
scenes into other scenes), an \"owner\" can be set for the node with the
`owner<class_Node_property_owner>`{.interpreted-text role="ref"}
property. This keeps track of who instantiated what. This is mostly
useful when writing editors and tools, though.

Finally, when a node is freed with
`Object.free()<class_Object_method_free>`{.interpreted-text role="ref"}
or `queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}, it will also free all its children.

\*\*Groups:\*\* Nodes can be added to as many groups as you want to be
easy to manage, you could create groups like \"enemies\" or
\"collectables\" for example, depending on your game. See
`add_to_group()<class_Node_method_add_to_group>`{.interpreted-text
role="ref"},
`is_in_group()<class_Node_method_is_in_group>`{.interpreted-text
role="ref"} and
`remove_from_group()<class_Node_method_remove_from_group>`{.interpreted-text
role="ref"}. You can then retrieve all nodes in these groups, iterate
them and even call methods on groups via the methods on
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

\*\*Networking with nodes:\*\* After connecting to a server (or making
one, see
`ENetMultiplayerPeer<class_ENetMultiplayerPeer>`{.interpreted-text
role="ref"}), it is possible to use the built-in RPC (remote procedure
call) system to communicate over the network. By calling
`rpc()<class_Node_method_rpc>`{.interpreted-text role="ref"} with a
method name, it will be called locally and in all connected peers (peers
= clients and the server that accepts connections). To identify which
node receives the RPC call, Godot will use its
`NodePath<class_NodePath>`{.interpreted-text role="ref"} (make sure node
names are the same on all peers). Also, take a look at the high-level
networking tutorial and corresponding demos.

\*\*Note:\*\* The `script` property is part of the
`Object<class_Object>`{.interpreted-text role="ref"} class, not
**Node**. It isn\'t exposed like most properties but does have a setter
and getter (see
`Object.set_script()<class_Object_method_set_script>`{.interpreted-text
role="ref"} and
`Object.get_script()<class_Object_method_get_script>`{.interpreted-text
role="ref"}).

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Nodes and scenes <../getting_started/step_by_step/nodes_and_scenes>`{.interpreted-text
  role="doc"}
- [All Demos](https://github.com/godotengine/godot-demo-projects/)

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

:::: {#class_Node_signal_child_entered_tree}
::: rst-class
classref-signal
:::
::::

**child_entered_tree**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`🔗<class_Node_signal_child_entered_tree>`{.interpreted-text role="ref"}

Emitted when the child `node` enters the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}, usually
because this node entered the tree (see
`tree_entered<class_Node_signal_tree_entered>`{.interpreted-text
role="ref"}), or
`add_child()<class_Node_method_add_child>`{.interpreted-text role="ref"}
has been called.

This signal is emitted *after* the child node\'s own
`NOTIFICATION_ENTER_TREE<class_Node_constant_NOTIFICATION_ENTER_TREE>`{.interpreted-text
role="ref"} and
`tree_entered<class_Node_signal_tree_entered>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_child_exiting_tree}
::: rst-class
classref-signal
:::
::::

**child_exiting_tree**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`🔗<class_Node_signal_child_exiting_tree>`{.interpreted-text role="ref"}

Emitted when the child `node` is about to exit the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}, usually
because this node is exiting the tree (see
`tree_exiting<class_Node_signal_tree_exiting>`{.interpreted-text
role="ref"}), or because the child `node` is being removed or freed.

When this signal is received, the child `node` is still accessible
inside the tree. This signal is emitted *after* the child node\'s own
`tree_exiting<class_Node_signal_tree_exiting>`{.interpreted-text
role="ref"} and
`NOTIFICATION_EXIT_TREE<class_Node_constant_NOTIFICATION_EXIT_TREE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_child_order_changed}
::: rst-class
classref-signal
:::
::::

**child_order_changed**()
`🔗<class_Node_signal_child_order_changed>`{.interpreted-text
role="ref"}

Emitted when the list of children is changed. This happens when child
nodes are added, moved or removed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_editor_description_changed}
::: rst-class
classref-signal
:::
::::

**editor_description_changed**(node:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_Node_signal_editor_description_changed>`{.interpreted-text
role="ref"}

Emitted when the node\'s editor description field changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_editor_state_changed}
::: rst-class
classref-signal
:::
::::

**editor_state_changed**()
`🔗<class_Node_signal_editor_state_changed>`{.interpreted-text
role="ref"}

Emitted when an attribute of the node that is relevant to the editor is
changed. Only emitted in the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_ready}
::: rst-class
classref-signal
:::
::::

**ready**() `🔗<class_Node_signal_ready>`{.interpreted-text role="ref"}

Emitted when the node is considered ready, after
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_renamed}
::: rst-class
classref-signal
:::
::::

**renamed**() `🔗<class_Node_signal_renamed>`{.interpreted-text
role="ref"}

Emitted when the node\'s
`name<class_Node_property_name>`{.interpreted-text role="ref"} is
changed, if the node is inside the tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_replacing_by}
::: rst-class
classref-signal
:::
::::

**replacing_by**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_Node_signal_replacing_by>`{.interpreted-text role="ref"}

Emitted when this node is being replaced by the `node`, see
`replace_by()<class_Node_method_replace_by>`{.interpreted-text
role="ref"}.

This signal is emitted *after* `node` has been added as a child of the
original parent node, but *before* all original child nodes have been
reparented to `node`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_tree_entered}
::: rst-class
classref-signal
:::
::::

**tree_entered**()
`🔗<class_Node_signal_tree_entered>`{.interpreted-text role="ref"}

Emitted when the node enters the tree.

This signal is emitted *after* the related
`NOTIFICATION_ENTER_TREE<class_Node_constant_NOTIFICATION_ENTER_TREE>`{.interpreted-text
role="ref"} notification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_tree_exited}
::: rst-class
classref-signal
:::
::::

**tree_exited**() `🔗<class_Node_signal_tree_exited>`{.interpreted-text
role="ref"}

Emitted after the node exits the tree and is no longer active.

This signal is emitted *after* the related
`NOTIFICATION_EXIT_TREE<class_Node_constant_NOTIFICATION_EXIT_TREE>`{.interpreted-text
role="ref"} notification.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_signal_tree_exiting}
::: rst-class
classref-signal
:::
::::

**tree_exiting**()
`🔗<class_Node_signal_tree_exiting>`{.interpreted-text role="ref"}

Emitted when the node is just about to exit the tree. The node is still
valid. As such, this is the right place for de-initialization (or a
\"destructor\", if you will).

This signal is emitted *after* the node\'s
`_exit_tree()<class_Node_private_method__exit_tree>`{.interpreted-text
role="ref"}, and *before* the related
`NOTIFICATION_EXIT_TREE<class_Node_constant_NOTIFICATION_EXIT_TREE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Node_ProcessMode}
::: rst-class
classref-enumeration
:::
::::

enum **ProcessMode**: `🔗<enum_Node_ProcessMode>`{.interpreted-text
role="ref"}

:::: {#class_Node_constant_PROCESS_MODE_INHERIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_INHERIT** = `0`

Inherits
`process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} from the node\'s parent. This is the default for any newly
created node.

:::: {#class_Node_constant_PROCESS_MODE_PAUSABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_PAUSABLE** = `1`

Stops processing when
`SceneTree.paused<class_SceneTree_property_paused>`{.interpreted-text
role="ref"} is `true`. This is the inverse of
`PROCESS_MODE_WHEN_PAUSED<class_Node_constant_PROCESS_MODE_WHEN_PAUSED>`{.interpreted-text
role="ref"}, and the default for the root node.

:::: {#class_Node_constant_PROCESS_MODE_WHEN_PAUSED}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_WHEN_PAUSED** = `2`

Process **only** when
`SceneTree.paused<class_SceneTree_property_paused>`{.interpreted-text
role="ref"} is `true`. This is the inverse of
`PROCESS_MODE_PAUSABLE<class_Node_constant_PROCESS_MODE_PAUSABLE>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_PROCESS_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_ALWAYS** = `3`

Always process. Keeps processing, ignoring
`SceneTree.paused<class_SceneTree_property_paused>`{.interpreted-text
role="ref"}. This is the inverse of
`PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_PROCESS_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}
**PROCESS_MODE_DISABLED** = `4`

Never process. Completely disables processing, ignoring
`SceneTree.paused<class_SceneTree_property_paused>`{.interpreted-text
role="ref"}. This is the inverse of
`PROCESS_MODE_ALWAYS<class_Node_constant_PROCESS_MODE_ALWAYS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Node_ProcessThreadGroup}
::: rst-class
classref-enumeration
:::
::::

enum **ProcessThreadGroup**:
`🔗<enum_Node_ProcessThreadGroup>`{.interpreted-text role="ref"}

:::: {#class_Node_constant_PROCESS_THREAD_GROUP_INHERIT}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessThreadGroup<enum_Node_ProcessThreadGroup>`{.interpreted-text
role="ref"} **PROCESS_THREAD_GROUP_INHERIT** = `0`

Process this node based on the thread group mode of the first parent (or
grandparent) node that has a thread group mode that is not inherit. See
`process_thread_group<class_Node_property_process_thread_group>`{.interpreted-text
role="ref"} for more information.

:::: {#class_Node_constant_PROCESS_THREAD_GROUP_MAIN_THREAD}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessThreadGroup<enum_Node_ProcessThreadGroup>`{.interpreted-text
role="ref"} **PROCESS_THREAD_GROUP_MAIN_THREAD** = `1`

Process this node (and child nodes set to inherit) on the main thread.
See
`process_thread_group<class_Node_property_process_thread_group>`{.interpreted-text
role="ref"} for more information.

:::: {#class_Node_constant_PROCESS_THREAD_GROUP_SUB_THREAD}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessThreadGroup<enum_Node_ProcessThreadGroup>`{.interpreted-text
role="ref"} **PROCESS_THREAD_GROUP_SUB_THREAD** = `2`

Process this node (and child nodes set to inherit) on a sub-thread. See
`process_thread_group<class_Node_property_process_thread_group>`{.interpreted-text
role="ref"} for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Node_ProcessThreadMessages}
::: rst-class
classref-enumeration
:::
::::

flags **ProcessThreadMessages**:
`🔗<enum_Node_ProcessThreadMessages>`{.interpreted-text role="ref"}

:::: {#class_Node_constant_FLAG_PROCESS_THREAD_MESSAGES}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessThreadMessages<enum_Node_ProcessThreadMessages>`{.interpreted-text
role="ref"} **FLAG_PROCESS_THREAD_MESSAGES** = `1`

Allows this node to process threaded messages created with
`call_deferred_thread_group()<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"} right before
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} is called.

:::: {#class_Node_constant_FLAG_PROCESS_THREAD_MESSAGES_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessThreadMessages<enum_Node_ProcessThreadMessages>`{.interpreted-text
role="ref"} **FLAG_PROCESS_THREAD_MESSAGES_PHYSICS** = `2`

Allows this node to process threaded messages created with
`call_deferred_thread_group()<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"} right before
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} is called.

:::: {#class_Node_constant_FLAG_PROCESS_THREAD_MESSAGES_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`ProcessThreadMessages<enum_Node_ProcessThreadMessages>`{.interpreted-text
role="ref"} **FLAG_PROCESS_THREAD_MESSAGES_ALL** = `3`

Allows this node to process threaded messages created with
`call_deferred_thread_group()<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"} right before either
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} or
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} are called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Node_PhysicsInterpolationMode}
::: rst-class
classref-enumeration
:::
::::

enum **PhysicsInterpolationMode**:
`🔗<enum_Node_PhysicsInterpolationMode>`{.interpreted-text role="ref"}

:::: {#class_Node_constant_PHYSICS_INTERPOLATION_MODE_INHERIT}
::: rst-class
classref-enumeration-constant
:::
::::

`PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>`{.interpreted-text
role="ref"} **PHYSICS_INTERPOLATION_MODE_INHERIT** = `0`

Inherits
`physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`{.interpreted-text
role="ref"} from the node\'s parent. This is the default for any newly
created node.

:::: {#class_Node_constant_PHYSICS_INTERPOLATION_MODE_ON}
::: rst-class
classref-enumeration-constant
:::
::::

`PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>`{.interpreted-text
role="ref"} **PHYSICS_INTERPOLATION_MODE_ON** = `1`

Enables physics interpolation for this node and for children set to
`PHYSICS_INTERPOLATION_MODE_INHERIT<class_Node_constant_PHYSICS_INTERPOLATION_MODE_INHERIT>`{.interpreted-text
role="ref"}. This is the default for the root node.

:::: {#class_Node_constant_PHYSICS_INTERPOLATION_MODE_OFF}
::: rst-class
classref-enumeration-constant
:::
::::

`PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>`{.interpreted-text
role="ref"} **PHYSICS_INTERPOLATION_MODE_OFF** = `2`

Disables physics interpolation for this node and for children set to
`PHYSICS_INTERPOLATION_MODE_INHERIT<class_Node_constant_PHYSICS_INTERPOLATION_MODE_INHERIT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Node_DuplicateFlags}
::: rst-class
classref-enumeration
:::
::::

enum **DuplicateFlags**:
`🔗<enum_Node_DuplicateFlags>`{.interpreted-text role="ref"}

:::: {#class_Node_constant_DUPLICATE_SIGNALS}
::: rst-class
classref-enumeration-constant
:::
::::

`DuplicateFlags<enum_Node_DuplicateFlags>`{.interpreted-text role="ref"}
**DUPLICATE_SIGNALS** = `1`

Duplicate the node\'s signal connections that are connected with the
`Object.CONNECT_PERSIST<class_Object_constant_CONNECT_PERSIST>`{.interpreted-text
role="ref"} flag.

:::: {#class_Node_constant_DUPLICATE_GROUPS}
::: rst-class
classref-enumeration-constant
:::
::::

`DuplicateFlags<enum_Node_DuplicateFlags>`{.interpreted-text role="ref"}
**DUPLICATE_GROUPS** = `2`

Duplicate the node\'s groups.

:::: {#class_Node_constant_DUPLICATE_SCRIPTS}
::: rst-class
classref-enumeration-constant
:::
::::

`DuplicateFlags<enum_Node_DuplicateFlags>`{.interpreted-text role="ref"}
**DUPLICATE_SCRIPTS** = `4`

Duplicate the node\'s script (also overriding the duplicated children\'s
scripts, if combined with
`DUPLICATE_USE_INSTANTIATION<class_Node_constant_DUPLICATE_USE_INSTANTIATION>`{.interpreted-text
role="ref"}).

:::: {#class_Node_constant_DUPLICATE_USE_INSTANTIATION}
::: rst-class
classref-enumeration-constant
:::
::::

`DuplicateFlags<enum_Node_DuplicateFlags>`{.interpreted-text role="ref"}
**DUPLICATE_USE_INSTANTIATION** = `8`

Duplicate using
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}. If the node comes from a scene saved on disk, reuses
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"} as the base for the duplicated node and its children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Node_InternalMode}
::: rst-class
classref-enumeration
:::
::::

enum **InternalMode**: `🔗<enum_Node_InternalMode>`{.interpreted-text
role="ref"}

:::: {#class_Node_constant_INTERNAL_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalMode<enum_Node_InternalMode>`{.interpreted-text role="ref"}
**INTERNAL_MODE_DISABLED** = `0`

The node will not be internal.

:::: {#class_Node_constant_INTERNAL_MODE_FRONT}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalMode<enum_Node_InternalMode>`{.interpreted-text role="ref"}
**INTERNAL_MODE_FRONT** = `1`

The node will be placed at the beginning of the parent\'s children,
before any non-internal sibling.

:::: {#class_Node_constant_INTERNAL_MODE_BACK}
::: rst-class
classref-enumeration-constant
:::
::::

`InternalMode<enum_Node_InternalMode>`{.interpreted-text role="ref"}
**INTERNAL_MODE_BACK** = `2`

The node will be placed at the end of the parent\'s children, after any
non-internal sibling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Node_AutoTranslateMode}
::: rst-class
classref-enumeration
:::
::::

enum **AutoTranslateMode**:
`🔗<enum_Node_AutoTranslateMode>`{.interpreted-text role="ref"}

:::: {#class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT}
::: rst-class
classref-enumeration-constant
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **AUTO_TRANSLATE_MODE_INHERIT** = `0`

Inherits
`auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"} from the node\'s parent. This is the default for any newly
created node.

:::: {#class_Node_constant_AUTO_TRANSLATE_MODE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **AUTO_TRANSLATE_MODE_ALWAYS** = `1`

Always automatically translate. This is the inverse of
`AUTO_TRANSLATE_MODE_DISABLED<class_Node_constant_AUTO_TRANSLATE_MODE_DISABLED>`{.interpreted-text
role="ref"}, and the default for the root node.

:::: {#class_Node_constant_AUTO_TRANSLATE_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **AUTO_TRANSLATE_MODE_DISABLED** = `2`

Never automatically translate. This is the inverse of
`AUTO_TRANSLATE_MODE_ALWAYS<class_Node_constant_AUTO_TRANSLATE_MODE_ALWAYS>`{.interpreted-text
role="ref"}.

String parsing for POT generation will be skipped for this node and
children that are set to
`AUTO_TRANSLATE_MODE_INHERIT<class_Node_constant_AUTO_TRANSLATE_MODE_INHERIT>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Constants

:::: {#class_Node_constant_NOTIFICATION_ENTER_TREE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_ENTER_TREE** = `10`
`🔗<class_Node_constant_NOTIFICATION_ENTER_TREE>`{.interpreted-text
role="ref"}

Notification received when the node enters a
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}. See
`_enter_tree()<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"}.

This notification is received *before* the related
`tree_entered<class_Node_signal_tree_entered>`{.interpreted-text
role="ref"} signal.

:::: {#class_Node_constant_NOTIFICATION_EXIT_TREE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_EXIT_TREE** = `11`
`🔗<class_Node_constant_NOTIFICATION_EXIT_TREE>`{.interpreted-text
role="ref"}

Notification received when the node is about to exit a
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}. See
`_exit_tree()<class_Node_private_method__exit_tree>`{.interpreted-text
role="ref"}.

This notification is received *after* the related
`tree_exiting<class_Node_signal_tree_exiting>`{.interpreted-text
role="ref"} signal.

:::: {#class_Node_constant_NOTIFICATION_MOVED_IN_PARENT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_MOVED_IN_PARENT** = `12`
`🔗<class_Node_constant_NOTIFICATION_MOVED_IN_PARENT>`{.interpreted-text
role="ref"}

**Deprecated:** This notification is no longer sent by the engine. Use
`NOTIFICATION_CHILD_ORDER_CHANGED<class_Node_constant_NOTIFICATION_CHILD_ORDER_CHANGED>`{.interpreted-text
role="ref"} instead.

:::: {#class_Node_constant_NOTIFICATION_READY}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_READY** = `13`
`🔗<class_Node_constant_NOTIFICATION_READY>`{.interpreted-text
role="ref"}

Notification received when the node is ready. See
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_PAUSED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_PAUSED** = `14`
`🔗<class_Node_constant_NOTIFICATION_PAUSED>`{.interpreted-text
role="ref"}

Notification received when the node is paused. See
`process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_UNPAUSED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_UNPAUSED** = `15`
`🔗<class_Node_constant_NOTIFICATION_UNPAUSED>`{.interpreted-text
role="ref"}

Notification received when the node is unpaused. See
`process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_PHYSICS_PROCESS}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_PHYSICS_PROCESS** = `16`
`🔗<class_Node_constant_NOTIFICATION_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}

Notification received from the tree every physics frame when
`is_physics_processing()<class_Node_method_is_physics_processing>`{.interpreted-text
role="ref"} returns `true`. See
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_PROCESS}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_PROCESS** = `17`
`🔗<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"}

Notification received from the tree every rendered frame when
`is_processing()<class_Node_method_is_processing>`{.interpreted-text
role="ref"} returns `true`. See
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_PARENTED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_PARENTED** = `18`
`🔗<class_Node_constant_NOTIFICATION_PARENTED>`{.interpreted-text
role="ref"}

Notification received when the node is set as a child of another node
(see `add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"} and
`add_sibling()<class_Node_method_add_sibling>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* This does *not* mean that the node entered the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_UNPARENTED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_UNPARENTED** = `19`
`🔗<class_Node_constant_NOTIFICATION_UNPARENTED>`{.interpreted-text
role="ref"}

Notification received when the parent node calls
`remove_child()<class_Node_method_remove_child>`{.interpreted-text
role="ref"} on this node.

\*\*Note:\*\* This does *not* mean that the node exited the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_SCENE_INSTANTIATED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_SCENE_INSTANTIATED** = `20`
`🔗<class_Node_constant_NOTIFICATION_SCENE_INSTANTIATED>`{.interpreted-text
role="ref"}

Notification received *only* by the newly instantiated scene root node,
when
`PackedScene.instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"} is completed.

:::: {#class_Node_constant_NOTIFICATION_DRAG_BEGIN}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_DRAG_BEGIN** = `21`
`🔗<class_Node_constant_NOTIFICATION_DRAG_BEGIN>`{.interpreted-text
role="ref"}

Notification received when a drag operation begins. All nodes receive
this notification, not only the dragged one.

Can be triggered either by dragging a
`Control<class_Control>`{.interpreted-text role="ref"} that provides
drag data (see
`Control._get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"}) or using
`Control.force_drag()<class_Control_method_force_drag>`{.interpreted-text
role="ref"}.

Use
`Viewport.gui_get_drag_data()<class_Viewport_method_gui_get_drag_data>`{.interpreted-text
role="ref"} to get the dragged data.

:::: {#class_Node_constant_NOTIFICATION_DRAG_END}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_DRAG_END** = `22`
`🔗<class_Node_constant_NOTIFICATION_DRAG_END>`{.interpreted-text
role="ref"}

Notification received when a drag operation ends.

Use
`Viewport.gui_is_drag_successful()<class_Viewport_method_gui_is_drag_successful>`{.interpreted-text
role="ref"} to check if the drag succeeded.

:::: {#class_Node_constant_NOTIFICATION_PATH_RENAMED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_PATH_RENAMED** = `23`
`🔗<class_Node_constant_NOTIFICATION_PATH_RENAMED>`{.interpreted-text
role="ref"}

Notification received when the node\'s
`name<class_Node_property_name>`{.interpreted-text role="ref"} or one of
its ancestors\' `name<class_Node_property_name>`{.interpreted-text
role="ref"} is changed. This notification is *not* received when the
node is removed from the `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_CHILD_ORDER_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_CHILD_ORDER_CHANGED** = `24`
`🔗<class_Node_constant_NOTIFICATION_CHILD_ORDER_CHANGED>`{.interpreted-text
role="ref"}

Notification received when the list of children is changed. This happens
when child nodes are added, moved or removed.

:::: {#class_Node_constant_NOTIFICATION_INTERNAL_PROCESS}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_INTERNAL_PROCESS** = `25`
`🔗<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}

Notification received from the tree every rendered frame when
`is_processing_internal()<class_Node_method_is_processing_internal>`{.interpreted-text
role="ref"} returns `true`.

:::: {#class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_INTERNAL_PHYSICS_PROCESS** = `26`
`🔗<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}

Notification received from the tree every physics frame when
`is_physics_processing_internal()<class_Node_method_is_physics_processing_internal>`{.interpreted-text
role="ref"} returns `true`.

:::: {#class_Node_constant_NOTIFICATION_POST_ENTER_TREE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_POST_ENTER_TREE** = `27`
`🔗<class_Node_constant_NOTIFICATION_POST_ENTER_TREE>`{.interpreted-text
role="ref"}

Notification received when the node enters the tree, just before
`NOTIFICATION_READY<class_Node_constant_NOTIFICATION_READY>`{.interpreted-text
role="ref"} may be received. Unlike the latter, it is sent every time
the node enters tree, not just once.

:::: {#class_Node_constant_NOTIFICATION_DISABLED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_DISABLED** = `28`
`🔗<class_Node_constant_NOTIFICATION_DISABLED>`{.interpreted-text
role="ref"}

Notification received when the node is disabled. See
`PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_ENABLED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_ENABLED** = `29`
`🔗<class_Node_constant_NOTIFICATION_ENABLED>`{.interpreted-text
role="ref"}

Notification received when the node is enabled again after being
disabled. See
`PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}.

:::: {#class_Node_constant_NOTIFICATION_RESET_PHYSICS_INTERPOLATION}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_RESET_PHYSICS_INTERPOLATION** = `2001`
`🔗<class_Node_constant_NOTIFICATION_RESET_PHYSICS_INTERPOLATION>`{.interpreted-text
role="ref"}

Notification received when
`reset_physics_interpolation()<class_Node_method_reset_physics_interpolation>`{.interpreted-text
role="ref"} is called on the node or its ancestors.

:::: {#class_Node_constant_NOTIFICATION_EDITOR_PRE_SAVE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_EDITOR_PRE_SAVE** = `9001`
`🔗<class_Node_constant_NOTIFICATION_EDITOR_PRE_SAVE>`{.interpreted-text
role="ref"}

Notification received right before the scene with the node is saved in
the editor. This notification is only sent in the Godot editor and will
not occur in exported projects.

:::: {#class_Node_constant_NOTIFICATION_EDITOR_POST_SAVE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_EDITOR_POST_SAVE** = `9002`
`🔗<class_Node_constant_NOTIFICATION_EDITOR_POST_SAVE>`{.interpreted-text
role="ref"}

Notification received right after the scene with the node is saved in
the editor. This notification is only sent in the Godot editor and will
not occur in exported projects.

:::: {#class_Node_constant_NOTIFICATION_WM_MOUSE_ENTER}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_MOUSE_ENTER** = `1002`
`🔗<class_Node_constant_NOTIFICATION_WM_MOUSE_ENTER>`{.interpreted-text
role="ref"}

Notification received when the mouse enters the window.

Implemented for embedded windows and on desktop and web platforms.

:::: {#class_Node_constant_NOTIFICATION_WM_MOUSE_EXIT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_MOUSE_EXIT** = `1003`
`🔗<class_Node_constant_NOTIFICATION_WM_MOUSE_EXIT>`{.interpreted-text
role="ref"}

Notification received when the mouse leaves the window.

Implemented for embedded windows and on desktop and web platforms.

:::: {#class_Node_constant_NOTIFICATION_WM_WINDOW_FOCUS_IN}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_WINDOW_FOCUS_IN** = `1004`
`🔗<class_Node_constant_NOTIFICATION_WM_WINDOW_FOCUS_IN>`{.interpreted-text
role="ref"}

Notification received from the OS when the node\'s
`Window<class_Window>`{.interpreted-text role="ref"} ancestor is
focused. This may be a change of focus between two windows of the same
engine instance, or from the OS desktop or a third-party application to
a window of the game (in which case
`NOTIFICATION_APPLICATION_FOCUS_IN<class_Node_constant_NOTIFICATION_APPLICATION_FOCUS_IN>`{.interpreted-text
role="ref"} is also received).

A `Window<class_Window>`{.interpreted-text role="ref"} node receives
this notification when it is focused.

:::: {#class_Node_constant_NOTIFICATION_WM_WINDOW_FOCUS_OUT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_WINDOW_FOCUS_OUT** = `1005`
`🔗<class_Node_constant_NOTIFICATION_WM_WINDOW_FOCUS_OUT>`{.interpreted-text
role="ref"}

Notification received from the OS when the node\'s
`Window<class_Window>`{.interpreted-text role="ref"} ancestor is
defocused. This may be a change of focus between two windows of the same
engine instance, or from a window of the game to the OS desktop or a
third-party application (in which case
`NOTIFICATION_APPLICATION_FOCUS_OUT<class_Node_constant_NOTIFICATION_APPLICATION_FOCUS_OUT>`{.interpreted-text
role="ref"} is also received).

A `Window<class_Window>`{.interpreted-text role="ref"} node receives
this notification when it is defocused.

:::: {#class_Node_constant_NOTIFICATION_WM_CLOSE_REQUEST}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_CLOSE_REQUEST** = `1006`
`🔗<class_Node_constant_NOTIFICATION_WM_CLOSE_REQUEST>`{.interpreted-text
role="ref"}

Notification received from the OS when a close request is sent (e.g.
closing the window with a \"Close\" button or
`Alt + F4`{.interpreted-text role="kbd"}).

Implemented on desktop platforms.

:::: {#class_Node_constant_NOTIFICATION_WM_GO_BACK_REQUEST}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_GO_BACK_REQUEST** = `1007`
`🔗<class_Node_constant_NOTIFICATION_WM_GO_BACK_REQUEST>`{.interpreted-text
role="ref"}

Notification received from the OS when a go back request is sent (e.g.
pressing the \"Back\" button on Android).

Implemented only on Android.

:::: {#class_Node_constant_NOTIFICATION_WM_SIZE_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_SIZE_CHANGED** = `1008`
`🔗<class_Node_constant_NOTIFICATION_WM_SIZE_CHANGED>`{.interpreted-text
role="ref"}

Notification received when the window is resized.

\*\*Note:\*\* Only the resized `Window<class_Window>`{.interpreted-text
role="ref"} node receives this notification, and it\'s not propagated to
the child nodes.

:::: {#class_Node_constant_NOTIFICATION_WM_DPI_CHANGE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_DPI_CHANGE** = `1009`
`🔗<class_Node_constant_NOTIFICATION_WM_DPI_CHANGE>`{.interpreted-text
role="ref"}

Notification received from the OS when the screen\'s dots per inch (DPI)
scale is changed. Only implemented on macOS.

:::: {#class_Node_constant_NOTIFICATION_VP_MOUSE_ENTER}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_VP_MOUSE_ENTER** = `1010`
`🔗<class_Node_constant_NOTIFICATION_VP_MOUSE_ENTER>`{.interpreted-text
role="ref"}

Notification received when the mouse cursor enters the
`Viewport<class_Viewport>`{.interpreted-text role="ref"}\'s visible
area, that is not occluded behind other
`Control<class_Control>`{.interpreted-text role="ref"}s or
`Window<class_Window>`{.interpreted-text role="ref"}s, provided its
`Viewport.gui_disable_input<class_Viewport_property_gui_disable_input>`{.interpreted-text
role="ref"} is `false` and regardless if it\'s currently focused or not.

:::: {#class_Node_constant_NOTIFICATION_VP_MOUSE_EXIT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_VP_MOUSE_EXIT** = `1011`
`🔗<class_Node_constant_NOTIFICATION_VP_MOUSE_EXIT>`{.interpreted-text
role="ref"}

Notification received when the mouse cursor leaves the
`Viewport<class_Viewport>`{.interpreted-text role="ref"}\'s visible
area, that is not occluded behind other
`Control<class_Control>`{.interpreted-text role="ref"}s or
`Window<class_Window>`{.interpreted-text role="ref"}s, provided its
`Viewport.gui_disable_input<class_Viewport_property_gui_disable_input>`{.interpreted-text
role="ref"} is `false` and regardless if it\'s currently focused or not.

:::: {#class_Node_constant_NOTIFICATION_WM_POSITION_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_POSITION_CHANGED** = `1012`
`🔗<class_Node_constant_NOTIFICATION_WM_POSITION_CHANGED>`{.interpreted-text
role="ref"}

Notification received when the window is moved.

:::: {#class_Node_constant_NOTIFICATION_OS_MEMORY_WARNING}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_OS_MEMORY_WARNING** = `2009`
`🔗<class_Node_constant_NOTIFICATION_OS_MEMORY_WARNING>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is exceeding its
allocated memory.

Implemented only on iOS.

:::: {#class_Node_constant_NOTIFICATION_TRANSLATION_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_TRANSLATION_CHANGED** = `2010`
`🔗<class_Node_constant_NOTIFICATION_TRANSLATION_CHANGED>`{.interpreted-text
role="ref"}

Notification received when translations may have changed. Can be
triggered by the user changing the locale, changing
`auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"} or when the node enters the scene tree. Can be used to
respond to language changes, for example to change the UI strings on the
fly. Useful when working with the built-in translation support, like
`Object.tr()<class_Object_method_tr>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This notification is received alongside
`NOTIFICATION_ENTER_TREE<class_Node_constant_NOTIFICATION_ENTER_TREE>`{.interpreted-text
role="ref"}, so if you are instantiating a scene, the child nodes will
not be initialized yet. You can use it to setup translations for this
node, child nodes created from script, or if you want to access child
nodes added in the editor, make sure the node is ready using
`is_node_ready()<class_Node_method_is_node_ready>`{.interpreted-text
role="ref"}.

    func _notification(what):
        if what == NOTIFICATION_TRANSLATION_CHANGED:
            if not is_node_ready():
                await ready # Wait until ready signal.
            $Label.text = atr("%d Bananas") % banana_counter

:::: {#class_Node_constant_NOTIFICATION_WM_ABOUT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_WM_ABOUT** = `2011`
`🔗<class_Node_constant_NOTIFICATION_WM_ABOUT>`{.interpreted-text
role="ref"}

Notification received from the OS when a request for \"About\"
information is sent.

Implemented only on macOS.

:::: {#class_Node_constant_NOTIFICATION_CRASH}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_CRASH** = `2012`
`🔗<class_Node_constant_NOTIFICATION_CRASH>`{.interpreted-text
role="ref"}

Notification received from Godot\'s crash handler when the engine is
about to crash.

Implemented on desktop platforms, if the crash handler is enabled.

:::: {#class_Node_constant_NOTIFICATION_OS_IME_UPDATE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_OS_IME_UPDATE** = `2013`
`🔗<class_Node_constant_NOTIFICATION_OS_IME_UPDATE>`{.interpreted-text
role="ref"}

Notification received from the OS when an update of the Input Method
Engine occurs (e.g. change of IME cursor position or composition
string).

Implemented only on macOS.

:::: {#class_Node_constant_NOTIFICATION_APPLICATION_RESUMED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_RESUMED** = `2014`
`🔗<class_Node_constant_NOTIFICATION_APPLICATION_RESUMED>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is resumed.

Specific to the Android and iOS platforms.

:::: {#class_Node_constant_NOTIFICATION_APPLICATION_PAUSED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_PAUSED** = `2015`
`🔗<class_Node_constant_NOTIFICATION_APPLICATION_PAUSED>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is paused.

Specific to the Android and iOS platforms.

\*\*Note:\*\* On iOS, you only have approximately 5 seconds to finish a
task started by this signal. If you go over this allotment, iOS will
kill the app instead of pausing it.

:::: {#class_Node_constant_NOTIFICATION_APPLICATION_FOCUS_IN}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_FOCUS_IN** = `2016`
`🔗<class_Node_constant_NOTIFICATION_APPLICATION_FOCUS_IN>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is focused, i.e.
when changing the focus from the OS desktop or a thirdparty application
to any open window of the Godot instance.

Implemented on desktop and mobile platforms.

:::: {#class_Node_constant_NOTIFICATION_APPLICATION_FOCUS_OUT}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_APPLICATION_FOCUS_OUT** = `2017`
`🔗<class_Node_constant_NOTIFICATION_APPLICATION_FOCUS_OUT>`{.interpreted-text
role="ref"}

Notification received from the OS when the application is defocused,
i.e. when changing the focus from any open window of the Godot instance
to the OS desktop or a thirdparty application.

Implemented on desktop and mobile platforms.

:::: {#class_Node_constant_NOTIFICATION_TEXT_SERVER_CHANGED}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_TEXT_SERVER_CHANGED** = `2018`
`🔗<class_Node_constant_NOTIFICATION_TEXT_SERVER_CHANGED>`{.interpreted-text
role="ref"}

Notification received when the
`TextServer<class_TextServer>`{.interpreted-text role="ref"} is changed.

:::: {#class_Node_constant_NOTIFICATION_ACCESSIBILITY_UPDATE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_ACCESSIBILITY_UPDATE** = `3000`
`🔗<class_Node_constant_NOTIFICATION_ACCESSIBILITY_UPDATE>`{.interpreted-text
role="ref"}

Notification received when an accessibility information update is
required.

:::: {#class_Node_constant_NOTIFICATION_ACCESSIBILITY_INVALIDATE}
::: rst-class
classref-constant
:::
::::

**NOTIFICATION_ACCESSIBILITY_INVALIDATE** = `3001`
`🔗<class_Node_constant_NOTIFICATION_ACCESSIBILITY_INVALIDATE>`{.interpreted-text
role="ref"}

Notification received when accessibility elements are invalidated. All
node accessibility elements are automatically deleted after receiving
this message, therefore all existing references to such elements should
be discarded.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Node_property_auto_translate_mode}
::: rst-class
classref-property
:::
::::

`AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
role="ref"} **auto_translate_mode** = `0`
`🔗<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_translate_mode**(value:
  `AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
  role="ref"})
- `AutoTranslateMode<enum_Node_AutoTranslateMode>`{.interpreted-text
  role="ref"} **get_auto_translate_mode**()

Defines if any text should automatically change to its translated
version depending on the current locale (for nodes such as
`Label<class_Label>`{.interpreted-text role="ref"},
`RichTextLabel<class_RichTextLabel>`{.interpreted-text role="ref"},
`Window<class_Window>`{.interpreted-text role="ref"}, etc.). Also
decides if the node\'s strings should be parsed for POT generation.

\*\*Note:\*\* For the root node, auto translate mode can also be set via
`ProjectSettings.internationalization/rendering/root_node_auto_translate<class_ProjectSettings_property_internationalization/rendering/root_node_auto_translate>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_editor_description}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**editor_description** = `""`
`🔗<class_Node_property_editor_description>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_editor_description**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_editor_description**()

An optional description to the node. It will be displayed as a tooltip
when hovering over the node in the editor\'s Scene dock.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_multiplayer}
::: rst-class
classref-property
:::
::::

`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
**multiplayer** `🔗<class_Node_property_multiplayer>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
  **get_multiplayer**()

The `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
instance associated with this node. See
`SceneTree.get_multiplayer()<class_SceneTree_method_get_multiplayer>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Renaming the node, or moving it in the tree, will not move
the `MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
to the new path, you will have to update this manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_name}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **name**
`🔗<class_Node_property_name>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_name**(value: `StringName<class_StringName>`{.interpreted-text
  role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_name**()

The name of the node. This name must be unique among the siblings (other
child nodes from the same parent). When set to an existing sibling\'s
name, the node is automatically renamed.

\*\*Note:\*\* When changing the name, the following characters will be
replaced with an underscore: (`.` `:` `@` `/` `"` `%`). In particular,
the `@` character is reserved for auto-generated names. See also
`String.validate_node_name()<class_String_method_validate_node_name>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_owner}
::: rst-class
classref-property
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **owner**
`🔗<class_Node_property_owner>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_owner**(value: `Node<class_Node>`{.interpreted-text role="ref"})
- `Node<class_Node>`{.interpreted-text role="ref"} **get_owner**()

The owner of this node. The owner must be an ancestor of this node. When
packing the owner node in a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}, all the
nodes it owns are also saved with it. See also
`unique_name_in_owner<class_Node_property_unique_name_in_owner>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In the editor, nodes not owned by the scene root are
usually not displayed in the Scene dock, and will **not** be saved. To
prevent this, remember to set the owner after calling
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_physics_interpolation_mode}
::: rst-class
classref-property
:::
::::

`PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>`{.interpreted-text
role="ref"} **physics_interpolation_mode** = `0`
`🔗<class_Node_property_physics_interpolation_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_interpolation_mode**(value:
  `PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>`{.interpreted-text
  role="ref"})
- `PhysicsInterpolationMode<enum_Node_PhysicsInterpolationMode>`{.interpreted-text
  role="ref"} **get_physics_interpolation_mode**()

The physics interpolation mode to use for this node. Only effective if
`ProjectSettings.physics/common/physics_interpolation<class_ProjectSettings_property_physics/common/physics_interpolation>`{.interpreted-text
role="ref"} or
`SceneTree.physics_interpolation<class_SceneTree_property_physics_interpolation>`{.interpreted-text
role="ref"} is `true`.

By default, nodes inherit the physics interpolation mode from their
parent. This property can enable or disable physics interpolation
individually for each node, regardless of their parents\' physics
interpolation mode.

\*\*Note:\*\* Some node types like
`VehicleWheel3D<class_VehicleWheel3D>`{.interpreted-text role="ref"}
have physics interpolation disabled by default, as they rely on their
own custom solution.

\*\*Note:\*\* When teleporting a node to a distant position, it\'s
recommended to temporarily disable interpolation with
`reset_physics_interpolation()<class_Node_method_reset_physics_interpolation>`{.interpreted-text
role="ref"} *after* moving the node. This avoids creating a visual
streak between the old and new positions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_process_mode}
::: rst-class
classref-property
:::
::::

`ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}
**process_mode** = `0`
`🔗<class_Node_property_process_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_mode**(value:
  `ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"})
- `ProcessMode<enum_Node_ProcessMode>`{.interpreted-text role="ref"}
  **get_process_mode**()

The node\'s processing behavior. To check if the node can process in its
current mode, use
`can_process()<class_Node_method_can_process>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_process_physics_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**process_physics_priority** = `0`
`🔗<class_Node_property_process_physics_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_process_priority**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_physics_process_priority**()

Similar to
`process_priority<class_Node_property_process_priority>`{.interpreted-text
role="ref"} but for
`NOTIFICATION_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_PHYSICS_PROCESS>`{.interpreted-text
role="ref"},
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}, or
`NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_process_priority}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **process_priority** =
`0` `🔗<class_Node_property_process_priority>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_priority**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_process_priority**()

The node\'s execution order of the process callbacks
(`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"},
`NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"}, and
`NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}). Nodes whose priority value is *lower* call their process
callbacks first, regardless of tree order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_process_thread_group}
::: rst-class
classref-property
:::
::::

`ProcessThreadGroup<enum_Node_ProcessThreadGroup>`{.interpreted-text
role="ref"} **process_thread_group** = `0`
`🔗<class_Node_property_process_thread_group>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_thread_group**(value:
  `ProcessThreadGroup<enum_Node_ProcessThreadGroup>`{.interpreted-text
  role="ref"})
- `ProcessThreadGroup<enum_Node_ProcessThreadGroup>`{.interpreted-text
  role="ref"} **get_process_thread_group**()

Set the process thread group for this node (basically, whether it
receives
`NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"},
`NOTIFICATION_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_PHYSICS_PROCESS>`{.interpreted-text
role="ref"},
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} or
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} (and the internal versions) on the main thread or in a
sub-thread.

By default, the thread group is
`PROCESS_THREAD_GROUP_INHERIT<class_Node_constant_PROCESS_THREAD_GROUP_INHERIT>`{.interpreted-text
role="ref"}, which means that this node belongs to the same thread group
as the parent node. The thread groups means that nodes in a specific
thread group will process together, separate to other thread groups
(depending on
`process_thread_group_order<class_Node_property_process_thread_group_order>`{.interpreted-text
role="ref"}). If the value is set is
`PROCESS_THREAD_GROUP_SUB_THREAD<class_Node_constant_PROCESS_THREAD_GROUP_SUB_THREAD>`{.interpreted-text
role="ref"}, this thread group will occur on a sub thread (not the main
thread), otherwise if set to
`PROCESS_THREAD_GROUP_MAIN_THREAD<class_Node_constant_PROCESS_THREAD_GROUP_MAIN_THREAD>`{.interpreted-text
role="ref"} it will process on the main thread. If there is not a parent
or grandparent node set to something other than inherit, the node will
belong to the *default thread group*. This default group will process on
the main thread and its group order is 0.

During processing in a sub-thread, accessing most functions in nodes
outside the thread group is forbidden (and it will result in an error in
debug mode). Use
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"},
`call_thread_safe()<class_Node_method_call_thread_safe>`{.interpreted-text
role="ref"},
`call_deferred_thread_group()<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"} and the likes in order to communicate from the thread groups
to the main thread (or to other thread groups).

To better understand process thread groups, the idea is that any node
set to any other value than
`PROCESS_THREAD_GROUP_INHERIT<class_Node_constant_PROCESS_THREAD_GROUP_INHERIT>`{.interpreted-text
role="ref"} will include any child (and grandchild) nodes set to inherit
into its process thread group. This means that the processing of all the
nodes in the group will happen together, at the same time as the node
including them.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_process_thread_group_order}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**process_thread_group_order**
`🔗<class_Node_property_process_thread_group_order>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_thread_group_order**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_process_thread_group_order**()

Change the process thread group order. Groups with a lesser order will
process before groups with a greater order. This is useful when a large
amount of nodes process in sub thread and, afterwards, another group
wants to collect their result in the main thread, as an example.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_process_thread_messages}
::: rst-class
classref-property
:::
::::

`BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
role="abbr"}\[`ProcessThreadMessages<enum_Node_ProcessThreadMessages>`{.interpreted-text
role="ref"}\] **process_thread_messages**
`🔗<class_Node_property_process_thread_messages>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_thread_messages**(value:
  `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`ProcessThreadMessages<enum_Node_ProcessThreadMessages>`{.interpreted-text
  role="ref"}\])
- `BitField (This value is an integer composed as a bitmask of the following flags.)`{.interpreted-text
  role="abbr"}\[`ProcessThreadMessages<enum_Node_ProcessThreadMessages>`{.interpreted-text
  role="ref"}\] **get_process_thread_messages**()

Set whether the current thread group will process messages (calls to
`call_deferred_thread_group()<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"} on threads), and whether it wants to receive them during
regular process or physics process callbacks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_scene_file_path}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **scene_file_path**
`🔗<class_Node_property_scene_file_path>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scene_file_path**(value:
  `String<class_String>`{.interpreted-text role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_scene_file_path**()

The original scene\'s file path, if the node has been instantiated from
a `PackedScene<class_PackedScene>`{.interpreted-text role="ref"} file.
Only scene root nodes contains this.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_property_unique_name_in_owner}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**unique_name_in_owner** = `false`
`🔗<class_Node_property_unique_name_in_owner>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_unique_name_in_owner**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_unique_name_in_owner**()

If `true`, the node can be accessed from any node sharing the same
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} or from
the `owner<class_Node_property_owner>`{.interpreted-text role="ref"}
itself, with special `%Name` syntax in
`get_node()<class_Node_method_get_node>`{.interpreted-text role="ref"}.

\*\*Note:\*\* If another node with the same
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} shares
the same `name<class_Node_property_name>`{.interpreted-text role="ref"}
as this node, the other node will no longer be accessible as unique.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Node_private_method__enter_tree}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_enter_tree**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"}

Called when the node enters the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} (e.g. upon
instantiating, scene changing, or after calling
`add_child()<class_Node_method_add_child>`{.interpreted-text role="ref"}
in a script). If the node has children, its
`_enter_tree()<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"} callback will be called first, and then that of the
children.

Corresponds to the
`NOTIFICATION_ENTER_TREE<class_Node_constant_NOTIFICATION_ENTER_TREE>`{.interpreted-text
role="ref"} notification in
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__exit_tree}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_exit_tree**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__exit_tree>`{.interpreted-text role="ref"}

Called when the node is about to leave the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} (e.g. upon
freeing, scene changing, or after calling
`remove_child()<class_Node_method_remove_child>`{.interpreted-text
role="ref"} in a script). If the node has children, its
`_exit_tree()<class_Node_private_method__exit_tree>`{.interpreted-text
role="ref"} callback will be called last, after all its children have
left the tree.

Corresponds to the
`NOTIFICATION_EXIT_TREE<class_Node_constant_NOTIFICATION_EXIT_TREE>`{.interpreted-text
role="ref"} notification in
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"} and signal
`tree_exiting<class_Node_signal_tree_exiting>`{.interpreted-text
role="ref"}. To get notified when the node has already left the active
tree, connect to the
`tree_exited<class_Node_signal_tree_exited>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__get_accessibility_configuration_warnings}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_accessibility_configuration_warnings**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__get_accessibility_configuration_warnings>`{.interpreted-text
role="ref"}

The elements in the array returned from this method are displayed as
warnings in the Scene dock if the script that overrides it is a `tool`
script, and accessibility warnings are enabled in the editor settings.

Returning an empty array produces no warnings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__get_configuration_warnings}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **\_get_configuration_warnings**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__get_configuration_warnings>`{.interpreted-text
role="ref"}

The elements in the array returned from this method are displayed as
warnings in the Scene dock if the script that overrides it is a `tool`
script.

Returning an empty array produces no warnings.

Call
`update_configuration_warnings()<class_Node_method_update_configuration_warnings>`{.interpreted-text
role="ref"} when the warnings need to be updated for this node.

    @export var energy = 0:
        set(value):
            energy = value
            update_configuration_warnings()

    func _get_configuration_warnings():
        if energy < 0:
            return ["Energy must be 0 or greater."]
        else:
            return []

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__get_focused_accessibility_element}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**\_get_focused_accessibility_element**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__get_focused_accessibility_element>`{.interpreted-text
role="ref"}

Called during accessibility information updates to determine the
currently focused sub-element, should return a sub-element RID or the
value returned by
`get_accessibility_element()<class_Node_method_get_accessibility_element>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_input**(event: `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_Node_private_method__input>`{.interpreted-text
role="ref"}

Called when there is an input event. The input event propagates up
through the node tree until a node consumes it.

It is only called if input processing is enabled, which is done
automatically if this method is overridden, and can be toggled with
`set_process_input()<class_Node_method_set_process_input>`{.interpreted-text
role="ref"}.

To consume the input event and stop it propagating further to other
nodes,
`Viewport.set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"} can be called.

For gameplay input,
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} and
`_unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"} are usually a better fit as they allow the GUI to intercept
the events first.

\*\*Note:\*\* This method is only called if the node is present in the
scene tree (i.e. if it\'s not an orphan).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__physics_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_physics_process**(delta: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}

Called during the physics processing step of the main loop. Physics
processing means that the frame rate is synced to the physics, i.e. the
`delta` parameter will *generally* be constant (see exceptions below).
`delta` is in seconds.

It is only called if physics processing is enabled, which is done
automatically if this method is overridden, and can be toggled with
`set_physics_process()<class_Node_method_set_physics_process>`{.interpreted-text
role="ref"}.

Processing happens in order of
`process_physics_priority<class_Node_property_process_physics_priority>`{.interpreted-text
role="ref"}, lower priority values are called first. Nodes with the same
priority are processed in tree order, or top to bottom as seen in the
editor (also known as pre-order traversal).

Corresponds to the
`NOTIFICATION_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_PHYSICS_PROCESS>`{.interpreted-text
role="ref"} notification in
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is only called if the node is present in the
scene tree (i.e. if it\'s not an orphan).

\*\*Note:\*\* `delta` will be larger than expected if running at a
framerate lower than
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} /
`Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>`{.interpreted-text
role="ref"} FPS. This is done to avoid \"spiral of death\" scenarios
where performance would plummet due to an ever-increasing number of
physics steps per frame. This behavior affects both
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} and
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. As a result, avoid using `delta` for time measurements in
real-world seconds. Use the `Time<class_Time>`{.interpreted-text
role="ref"} singleton\'s methods for this purpose instead, such as
`Time.get_ticks_usec()<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_process**(delta: `float<class_float>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_Node_private_method__process>`{.interpreted-text
role="ref"}

Called during the processing step of the main loop. Processing happens
at every frame and as fast as possible, so the `delta` time since the
previous frame is not constant. `delta` is in seconds.

It is only called if processing is enabled, which is done automatically
if this method is overridden, and can be toggled with
`set_process()<class_Node_method_set_process>`{.interpreted-text
role="ref"}.

Processing happens in order of
`process_priority<class_Node_property_process_priority>`{.interpreted-text
role="ref"}, lower priority values are called first. Nodes with the same
priority are processed in tree order, or top to bottom as seen in the
editor (also known as pre-order traversal).

Corresponds to the
`NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"} notification in
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is only called if the node is present in the
scene tree (i.e. if it\'s not an orphan).

\*\*Note:\*\* `delta` will be larger than expected if running at a
framerate lower than
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} /
`Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>`{.interpreted-text
role="ref"} FPS. This is done to avoid \"spiral of death\" scenarios
where performance would plummet due to an ever-increasing number of
physics steps per frame. This behavior affects both
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} and
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. As a result, avoid using `delta` for time measurements in
real-world seconds. Use the `Time<class_Time>`{.interpreted-text
role="ref"} singleton\'s methods for this purpose instead, such as
`Time.get_ticks_usec()<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__ready}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **\_ready**()
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"} `🔗<class_Node_private_method__ready>`{.interpreted-text
role="ref"}

Called when the node is \"ready\", i.e. when both the node and its
children have entered the scene tree. If the node has children, their
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} callbacks get triggered first, and the parent node will
receive the ready notification afterwards.

Corresponds to the
`NOTIFICATION_READY<class_Node_constant_NOTIFICATION_READY>`{.interpreted-text
role="ref"} notification in
`Object._notification()<class_Object_private_method__notification>`{.interpreted-text
role="ref"}. See also the `@onready` annotation for variables.

Usually used for initialization. For even earlier initialization,
`Object._init()<class_Object_private_method__init>`{.interpreted-text
role="ref"} may be used. See also
`_enter_tree()<class_Node_private_method__enter_tree>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method may be called only once for each node. After
removing a node from the scene tree and adding it again,
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} will **not** be called a second time. This can be bypassed
by requesting another call with
`request_ready()<class_Node_method_request_ready>`{.interpreted-text
role="ref"}, which may be called anywhere before adding the node again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__shortcut_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_shortcut_input**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"}

Called when an `InputEventKey<class_InputEventKey>`{.interpreted-text
role="ref"},
`InputEventShortcut<class_InputEventShortcut>`{.interpreted-text
role="ref"}, or
`InputEventJoypadButton<class_InputEventJoypadButton>`{.interpreted-text
role="ref"} hasn\'t been consumed by
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} or any GUI `Control<class_Control>`{.interpreted-text
role="ref"} item. It is called before
`_unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"} and
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"}. The input event propagates up through the node tree until a
node consumes it.

It is only called if shortcut processing is enabled, which is done
automatically if this method is overridden, and can be toggled with
`set_process_shortcut_input()<class_Node_method_set_process_shortcut_input>`{.interpreted-text
role="ref"}.

To consume the input event and stop it propagating further to other
nodes,
`Viewport.set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"} can be called.

This method can be used to handle shortcuts. For generic GUI events, use
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} instead. Gameplay events should usually be handled with
either
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} or
`_unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method is only called if the node is present in the
scene tree (i.e. if it\'s not orphan).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__unhandled_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_unhandled_input**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"}

Called when an `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} hasn\'t been consumed by
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} or any GUI `Control<class_Control>`{.interpreted-text
role="ref"} item. It is called after
`_shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"} and after
`_unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"}. The input event propagates up through the node tree until a
node consumes it.

It is only called if unhandled input processing is enabled, which is
done automatically if this method is overridden, and can be toggled with
`set_process_unhandled_input()<class_Node_method_set_process_unhandled_input>`{.interpreted-text
role="ref"}.

To consume the input event and stop it propagating further to other
nodes,
`Viewport.set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"} can be called.

For gameplay input, this method is usually a better fit than
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}, as GUI events need a higher priority. For keyboard
shortcuts, consider using
`_shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"} instead, as it is called before this method. Finally, to
handle keyboard events, consider using
`_unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"} for performance reasons.

\*\*Note:\*\* This method is only called if the node is present in the
scene tree (i.e. if it\'s not an orphan).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_private_method__unhandled_key_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_unhandled_key_input**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"}

Called when an `InputEventKey<class_InputEventKey>`{.interpreted-text
role="ref"} hasn\'t been consumed by
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} or any GUI `Control<class_Control>`{.interpreted-text
role="ref"} item. It is called after
`_shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"} but before
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"}. The input event propagates up through the node tree until a
node consumes it.

It is only called if unhandled key input processing is enabled, which is
done automatically if this method is overridden, and can be toggled with
`set_process_unhandled_key_input()<class_Node_method_set_process_unhandled_key_input>`{.interpreted-text
role="ref"}.

To consume the input event and stop it propagating further to other
nodes,
`Viewport.set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"} can be called.

This method can be used to handle Unicode character input with
`Alt`{.interpreted-text role="kbd"}, `Alt + Ctrl`{.interpreted-text
role="kbd"}, and `Alt + Shift`{.interpreted-text role="kbd"} modifiers,
after shortcuts were handled.

For gameplay input, this and
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} are usually a better fit than
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}, as GUI events should be handled first. This method also
performs better than
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"}, since unrelated events such as
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} are automatically filtered. For shortcuts, consider using
`_shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"} instead.

\*\*Note:\*\* This method is only called if the node is present in the
scene tree (i.e. if it\'s not an orphan).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_add_child}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_child**(node: `Node<class_Node>`{.interpreted-text role="ref"},
force_readable_name: `bool<class_bool>`{.interpreted-text role="ref"} =
false, internal:
`InternalMode<enum_Node_InternalMode>`{.interpreted-text role="ref"} =
0) `🔗<class_Node_method_add_child>`{.interpreted-text role="ref"}

Adds a child `node`. Nodes can have any number of children, but every
child must have a unique name. Child nodes are automatically deleted
when the parent node is deleted, so an entire scene can be removed by
deleting its topmost node.

If `force_readable_name` is `true`, improves the readability of the
added `node`. If not named, the `node` is renamed to its type, and if it
shares `name<class_Node_property_name>`{.interpreted-text role="ref"}
with a sibling, a number is suffixed more appropriately. This operation
is very slow. As such, it is recommended leaving this to `false`, which
assigns a dummy name featuring `@` in both situations.

If `internal` is different than
`INTERNAL_MODE_DISABLED<class_Node_constant_INTERNAL_MODE_DISABLED>`{.interpreted-text
role="ref"}, the child will be added as internal node. These nodes are
ignored by methods like
`get_children()<class_Node_method_get_children>`{.interpreted-text
role="ref"}, unless their parameter `include_internal` is `true`. It
also prevents these nodes being duplicated with their parent. The
intended usage is to hide the internal nodes from the user, so the user
won\'t accidentally delete or modify them. Used by some GUI nodes, e.g.
`ColorPicker<class_ColorPicker>`{.interpreted-text role="ref"}.

\*\*Note:\*\* If `node` already has a parent, this method will fail. Use
`remove_child()<class_Node_method_remove_child>`{.interpreted-text
role="ref"} first to remove `node` from its current parent. For example:

::::: tabs
::: code-tab
gdscript

var child_node = get_child(0) if child_node.get_parent():
child_node.get_parent().remove_child(child_node) add_child(child_node)
:::

::: code-tab
csharp

Node childNode = GetChild(0); if (childNode.GetParent() != null) {
childNode.GetParent().RemoveChild(childNode); } AddChild(childNode);
:::
:::::

If you need the child node to be added below a specific node in the list
of children, use
`add_sibling()<class_Node_method_add_sibling>`{.interpreted-text
role="ref"} instead of this method.

\*\*Note:\*\* If you want a child to be persisted to a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}, you must
set `owner<class_Node_property_owner>`{.interpreted-text role="ref"} in
addition to calling
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}. This is typically relevant for
`tool scripts <../tutorials/plugins/running_code_in_the_editor>`{.interpreted-text
role="doc"} and
`editor plugins <../tutorials/plugins/editor/index>`{.interpreted-text
role="doc"}. If
`add_child()<class_Node_method_add_child>`{.interpreted-text role="ref"}
is called without setting
`owner<class_Node_property_owner>`{.interpreted-text role="ref"}, the
newly added **Node** will not be visible in the scene tree, though it
will be visible in the 2D/3D view.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_add_sibling}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_sibling**(sibling: `Node<class_Node>`{.interpreted-text
role="ref"}, force_readable_name: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Node_method_add_sibling>`{.interpreted-text role="ref"}

Adds a `sibling` node to this node\'s parent, and moves the added
sibling right below this node.

If `force_readable_name` is `true`, improves the readability of the
added `sibling`. If not named, the `sibling` is renamed to its type, and
if it shares `name<class_Node_property_name>`{.interpreted-text
role="ref"} with a sibling, a number is suffixed more appropriately.
This operation is very slow. As such, it is recommended leaving this to
`false`, which assigns a dummy name featuring `@` in both situations.

Use `add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"} instead of this method if you don\'t need the child node to
be added below a specific node in the list of children.

\*\*Note:\*\* If this node is internal, the added sibling will be
internal too (see
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}\'s `internal` parameter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_add_to_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_to_group**(group: `StringName<class_StringName>`{.interpreted-text
role="ref"}, persistent: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Node_method_add_to_group>`{.interpreted-text role="ref"}

Adds the node to the `group`. Groups can be helpful to organize a subset
of nodes, for example `"enemies"` or `"collectables"`. See notes in the
description, and the group methods in
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

If `persistent` is `true`, the group will be stored when saved inside a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}. All
groups created and displayed in the Node dock are persistent.

\*\*Note:\*\* To improve performance, the order of group names is *not*
guaranteed and may vary between project runs. Therefore, do not rely on
the group order.

\*\*Note:\*\* `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"}\'s group methods will *not* work on this node if not inside
the tree (see
`is_inside_tree()<class_Node_method_is_inside_tree>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_atr}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **atr**(message:
`String<class_String>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_atr>`{.interpreted-text role="ref"}

Translates a `message`, using the translation catalogs configured in the
Project Settings. Further `context` can be specified to help with the
translation. Note that most `Control<class_Control>`{.interpreted-text
role="ref"} nodes automatically translate their strings, so this method
is mostly useful for formatted strings or custom drawn text.

This method works the same as
`Object.tr()<class_Object_method_tr>`{.interpreted-text role="ref"},
with the addition of respecting the
`auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"} state.

If
`Object.can_translate_messages()<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"} is `false`, or no translation is available, this method
returns the `message` without changes. See
`Object.set_message_translation()<class_Object_method_set_message_translation>`{.interpreted-text
role="ref"}.

For detailed examples, see
`Internationalizing games <../tutorials/i18n/internationalizing_games>`{.interpreted-text
role="doc"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_atr_n}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **atr_n**(message:
`String<class_String>`{.interpreted-text role="ref"}, plural_message:
`StringName<class_StringName>`{.interpreted-text role="ref"}, n:
`int<class_int>`{.interpreted-text role="ref"}, context:
`StringName<class_StringName>`{.interpreted-text role="ref"} = \"\")
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_atr_n>`{.interpreted-text role="ref"}

Translates a `message` or `plural_message`, using the translation
catalogs configured in the Project Settings. Further `context` can be
specified to help with the translation.

This method works the same as
`Object.tr_n()<class_Object_method_tr_n>`{.interpreted-text role="ref"},
with the addition of respecting the
`auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"} state.

If
`Object.can_translate_messages()<class_Object_method_can_translate_messages>`{.interpreted-text
role="ref"} is `false`, or no translation is available, this method
returns `message` or `plural_message`, without changes. See
`Object.set_message_translation()<class_Object_method_set_message_translation>`{.interpreted-text
role="ref"}.

The `n` is the number, or amount, of the message\'s subject. It is used
by the translation system to fetch the correct plural form for the
current language.

For detailed examples, see
`Localization using gettext <../tutorials/i18n/localization_using_gettext>`{.interpreted-text
role="doc"}.

\*\*Note:\*\* Negative and `float<class_float>`{.interpreted-text
role="ref"} numbers may not properly apply to some countable subjects.
It\'s recommended to handle these cases with
`atr()<class_Node_method_atr>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_call_deferred_thread_group}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**call_deferred_thread_group**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"}

This function is similar to
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"} except that the call will take place when the node thread
group is processed. If the node thread group processes in sub-threads,
then the call will be done on that thread, right before
`NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"} or
`NOTIFICATION_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}, the
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} or
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} or their internal versions are called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_call_thread_safe}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**call_thread_safe**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_call_thread_safe>`{.interpreted-text
role="ref"}

This function ensures that the calling of this function will succeed, no
matter whether it\'s being done from a thread or not. If called from a
thread that is not allowed to call the function, the call will become
deferred. Otherwise, the call will go through directly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_can_auto_translate}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**can_auto_translate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_can_auto_translate>`{.interpreted-text role="ref"}

Returns `true` if this node can automatically translate messages
depending on the current locale. See
`auto_translate_mode<class_Node_property_auto_translate_mode>`{.interpreted-text
role="ref"}, `atr()<class_Node_method_atr>`{.interpreted-text
role="ref"}, and `atr_n()<class_Node_method_atr_n>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_can_process}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_process**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_can_process>`{.interpreted-text
role="ref"}

Returns `true` if the node can receive processing notifications and
input callbacks
(`NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"},
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}, etc.) from the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} and
`Viewport<class_Viewport>`{.interpreted-text role="ref"}. The returned
value depends on
`process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"}:

- If set to
  `PROCESS_MODE_PAUSABLE<class_Node_constant_PROCESS_MODE_PAUSABLE>`{.interpreted-text
  role="ref"}, returns `true` when the game is processing, i.e.
  `SceneTree.paused<class_SceneTree_property_paused>`{.interpreted-text
  role="ref"} is `false`;
- If set to
  `PROCESS_MODE_WHEN_PAUSED<class_Node_constant_PROCESS_MODE_WHEN_PAUSED>`{.interpreted-text
  role="ref"}, returns `true` when the game is paused, i.e.
  `SceneTree.paused<class_SceneTree_property_paused>`{.interpreted-text
  role="ref"} is `true`;
- If set to
  `PROCESS_MODE_ALWAYS<class_Node_constant_PROCESS_MODE_ALWAYS>`{.interpreted-text
  role="ref"}, always returns `true`;
- If set to
  `PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
  role="ref"}, always returns `false`;
- If set to
  `PROCESS_MODE_INHERIT<class_Node_constant_PROCESS_MODE_INHERIT>`{.interpreted-text
  role="ref"}, use the parent node\'s
  `process_mode<class_Node_property_process_mode>`{.interpreted-text
  role="ref"} to determine the result.

If the node is not inside the tree, returns `false` no matter the value
of `process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_create_tween}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **create_tween**()
`🔗<class_Node_method_create_tween>`{.interpreted-text role="ref"}

Creates a new `Tween<class_Tween>`{.interpreted-text role="ref"} and
binds it to this node.

This is the equivalent of doing:

::::: tabs
::: code-tab
gdscript

get_tree().create_tween().bind_node(self)
:::

::: code-tab
csharp

GetTree().CreateTween().BindNode(this);
:::
:::::

The Tween will start automatically on the next process frame or physics
frame (depending on
`TweenProcessMode<enum_Tween_TweenProcessMode>`{.interpreted-text
role="ref"}). See
`Tween.bind_node()<class_Tween_method_bind_node>`{.interpreted-text
role="ref"} for more info on Tweens bound to nodes.

\*\*Note:\*\* The method can still be used when the node is not inside
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}. It can fail
in an unlikely case of using a custom
`MainLoop<class_MainLoop>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_duplicate}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **duplicate**(flags:
`int<class_int>`{.interpreted-text role="ref"} = 15)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_duplicate>`{.interpreted-text
role="ref"}

Duplicates the node, returning a new node with all of its properties,
signals, groups, and children copied from the original. The behavior can
be tweaked through the `flags` (see
`DuplicateFlags<enum_Node_DuplicateFlags>`{.interpreted-text
role="ref"}). Internal nodes are not duplicated.

\*\*Note:\*\* For nodes with a `Script<class_Script>`{.interpreted-text
role="ref"} attached, if
`Object._init()<class_Object_private_method__init>`{.interpreted-text
role="ref"} has been defined with required parameters, the duplicated
node will not have a `Script<class_Script>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_find_child}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **find_child**(pattern:
`String<class_String>`{.interpreted-text role="ref"}, recursive:
`bool<class_bool>`{.interpreted-text role="ref"} = true, owned:
`bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_find_child>`{.interpreted-text
role="ref"}

Finds the first descendant of this node whose
`name<class_Node_property_name>`{.interpreted-text role="ref"} matches
`pattern`, returning `null` if no match is found. The matching is done
against node names, *not* their paths, through
`String.match()<class_String_method_match>`{.interpreted-text
role="ref"}. As such, it is case-sensitive, `"*"` matches zero or more
characters, and `"?"` matches any single character.

If `recursive` is `false`, only this node\'s direct children are
checked. Nodes are checked in tree order, so this node\'s first direct
child is checked first, then its own direct children, etc., before
moving to the second direct child, and so on. Internal children are also
included in the search (see `internal` parameter in
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}).

If `owned` is `true`, only descendants with a valid
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} node
are checked.

\*\*Note:\*\* This method can be very slow. Consider storing a reference
to the found node in a variable. Alternatively, use
`get_node()<class_Node_method_get_node>`{.interpreted-text role="ref"}
with unique names (see
`unique_name_in_owner<class_Node_property_unique_name_in_owner>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* To find all descendant nodes matching a pattern or a class
type, see
`find_children()<class_Node_method_find_children>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_find_children}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node<class_Node>`{.interpreted-text role="ref"}\]
**find_children**(pattern: `String<class_String>`{.interpreted-text
role="ref"}, type: `String<class_String>`{.interpreted-text role="ref"}
= \"\", recursive: `bool<class_bool>`{.interpreted-text role="ref"} =
true, owned: `bool<class_bool>`{.interpreted-text role="ref"} = true)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_find_children>`{.interpreted-text
role="ref"}

Finds all descendants of this node whose names match `pattern`,
returning an empty `Array<class_Array>`{.interpreted-text role="ref"} if
no match is found. The matching is done against node names, *not* their
paths, through
`String.match()<class_String_method_match>`{.interpreted-text
role="ref"}. As such, it is case-sensitive, `"*"` matches zero or more
characters, and `"?"` matches any single character.

If `type` is not empty, only ancestors inheriting from `type` are
included (see
`Object.is_class()<class_Object_method_is_class>`{.interpreted-text
role="ref"}).

If `recursive` is `false`, only this node\'s direct children are
checked. Nodes are checked in tree order, so this node\'s first direct
child is checked first, then its own direct children, etc., before
moving to the second direct child, and so on. Internal children are also
included in the search (see `internal` parameter in
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}).

If `owned` is `true`, only descendants with a valid
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} node
are checked.

\*\*Note:\*\* This method can be very slow. Consider storing references
to the found nodes in a variable.

\*\*Note:\*\* To find a single descendant node matching a pattern, see
`find_child()<class_Node_method_find_child>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_find_parent}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**find_parent**(pattern: `String<class_String>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_find_parent>`{.interpreted-text
role="ref"}

Finds the first ancestor of this node whose
`name<class_Node_property_name>`{.interpreted-text role="ref"} matches
`pattern`, returning `null` if no match is found. The matching is done
through `String.match()<class_String_method_match>`{.interpreted-text
role="ref"}. As such, it is case-sensitive, `"*"` matches zero or more
characters, and `"?"` matches any single character. See also
`find_child()<class_Node_method_find_child>`{.interpreted-text
role="ref"} and
`find_children()<class_Node_method_find_children>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* As this method walks upwards in the scene tree, it can be
slow in large, deeply nested nodes. Consider storing a reference to the
found node in a variable. Alternatively, use
`get_node()<class_Node_method_get_node>`{.interpreted-text role="ref"}
with unique names (see
`unique_name_in_owner<class_Node_property_unique_name_in_owner>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_accessibility_element}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"}
**get_accessibility_element**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_accessibility_element>`{.interpreted-text
role="ref"}

Returns main accessibility element RID.

\*\*Note:\*\* This method should be called only during accessibility
information updates
(`NOTIFICATION_ACCESSIBILITY_UPDATE<class_Node_constant_NOTIFICATION_ACCESSIBILITY_UPDATE>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_child}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **get_child**(idx:
`int<class_int>`{.interpreted-text role="ref"}, include_internal:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_child>`{.interpreted-text
role="ref"}

Fetches a child node by its index. Each child node has an index relative
to its siblings (see
`get_index()<class_Node_method_get_index>`{.interpreted-text
role="ref"}). The first child is at index 0. Negative values can also be
used to start from the end of the list. This method can be used in
combination with
`get_child_count()<class_Node_method_get_child_count>`{.interpreted-text
role="ref"} to iterate over this node\'s children. If no child exists at
the given index, this method returns `null` and an error is generated.

If `include_internal` is `false`, internal children are ignored (see
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}\'s `internal` parameter).

    # Assuming the following are children of this node, in order:
    # First, Middle, Last.

    var a = get_child(0).name  # a is "First"
    var b = get_child(1).name  # b is "Middle"
    var b = get_child(2).name  # b is "Last"
    var c = get_child(-1).name # c is "Last"

\*\*Note:\*\* To fetch a node by
`NodePath<class_NodePath>`{.interpreted-text role="ref"}, use
`get_node()<class_Node_method_get_node>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_child_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_child_count**(include_internal:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_child_count>`{.interpreted-text
role="ref"}

Returns the number of children of this node.

If `include_internal` is `false`, internal children are not counted (see
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}\'s `internal` parameter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_children}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Node<class_Node>`{.interpreted-text role="ref"}\]
**get_children**(include_internal: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_children>`{.interpreted-text
role="ref"}

Returns all children of this node inside an
`Array<class_Array>`{.interpreted-text role="ref"}.

If `include_internal` is `false`, excludes internal children from the
returned array (see
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}\'s `internal` parameter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_groups}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_groups**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_groups>`{.interpreted-text
role="ref"}

Returns an `Array<class_Array>`{.interpreted-text role="ref"} of group
names that the node has been added to.

\*\*Note:\*\* To improve performance, the order of group names is *not*
guaranteed and may vary between project runs. Therefore, do not rely on
the group order.

\*\*Note:\*\* This method may also return some group names starting with
an underscore (`_`). These are internally used by the engine. To avoid
conflicts, do not use custom groups starting with underscores. To
exclude internal groups, see the following code snippet:

::::: tabs
::: code-tab
gdscript

\# Stores the node\'s non-internal groups only (as an array of
StringNames). var non_internal_groups = \[\] for group in get_groups():
if not str(group).begins_with(\"\_\"):
non_internal_groups.push_back(group)
:::

::: code-tab
csharp

// Stores the node\'s non-internal groups only (as a List of
StringNames). List\<string\> nonInternalGroups = new List\<string\>();
foreach (string group in GetGroups()) { if (!group.BeginsWith(\"\_\"))
nonInternalGroups.Add(group); }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_index}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_index**(include_internal: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_index>`{.interpreted-text
role="ref"}

Returns this node\'s order among its siblings. The first node\'s index
is `0`. See also
`get_child()<class_Node_method_get_child>`{.interpreted-text
role="ref"}.

If `include_internal` is `false`, returns the index ignoring internal
children. The first, non-internal child will have an index of `0` (see
`add_child()<class_Node_method_add_child>`{.interpreted-text
role="ref"}\'s `internal` parameter).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_last_exclusive_window}
::: rst-class
classref-method
:::
::::

`Window<class_Window>`{.interpreted-text role="ref"}
**get_last_exclusive_window**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_last_exclusive_window>`{.interpreted-text
role="ref"}

Returns the `Window<class_Window>`{.interpreted-text role="ref"} that
contains this node, or the last exclusive child in a chain of windows
starting with the one that contains this node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_multiplayer_authority}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_multiplayer_authority**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_multiplayer_authority>`{.interpreted-text
role="ref"}

Returns the peer ID of the multiplayer authority for this node. See
`set_multiplayer_authority()<class_Node_method_set_multiplayer_authority>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_node}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **get_node**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_node>`{.interpreted-text
role="ref"}

Fetches a node. The `NodePath<class_NodePath>`{.interpreted-text
role="ref"} can either be a relative path (from this node), or an
absolute path (from the
`SceneTree.root<class_SceneTree_property_root>`{.interpreted-text
role="ref"}) to a node. If `path` does not point to a valid node,
generates an error and returns `null`. Attempts to access methods on the
return value will result in an *\"Attempt to call \<method\> on a null
instance.\"* error.

\*\*Note:\*\* Fetching by absolute path only works when the node is
inside the scene tree (see
`is_inside_tree()<class_Node_method_is_inside_tree>`{.interpreted-text
role="ref"}).

\*\*Example:\*\* Assume this method is called from the Character node,
inside the following tree:

``` text
┖╴root
   ┠╴Character (you are here!)
   ┃  ┠╴Sword
   ┃  ┖╴Backpack
   ┃     ┖╴Dagger
   ┠╴MyGame
   ┖╴Swamp
      ┠╴Alligator
      ┠╴Mosquito
      ┖╴Goblin
```

The following calls will return a valid node:

::::: tabs
::: code-tab
gdscript

get_node(\"Sword\") get_node(\"Backpack/Dagger\")
get_node(\"../Swamp/Alligator\") get_node(\"/root/MyGame\")
:::

::: code-tab
csharp

GetNode(\"Sword\"); GetNode(\"Backpack/Dagger\");
GetNode(\"../Swamp/Alligator\"); GetNode(\"/root/MyGame\");
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_node_and_resource}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text role="ref"}
**get_node_and_resource**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`🔗<class_Node_method_get_node_and_resource>`{.interpreted-text
role="ref"}

Fetches a node and its most nested resource as specified by the
`NodePath<class_NodePath>`{.interpreted-text role="ref"}\'s subname.
Returns an `Array<class_Array>`{.interpreted-text role="ref"} of size
`3` where:

- Element `0` is the **Node**, or `null` if not found;
- Element `1` is the subname\'s last nested
  `Resource<class_Resource>`{.interpreted-text role="ref"}, or `null` if
  not found;
- Element `2` is the remaining
  `NodePath<class_NodePath>`{.interpreted-text role="ref"}, referring to
  an existing, non-`Resource<class_Resource>`{.interpreted-text
  role="ref"} property (see
  `Object.get_indexed()<class_Object_method_get_indexed>`{.interpreted-text
  role="ref"}).

\*\*Example:\*\* Assume that the child\'s
`Sprite2D.texture<class_Sprite2D_property_texture>`{.interpreted-text
role="ref"} has been assigned an
`AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"}:

::::: tabs
::: code-tab
gdscript

var a = get_node_and_resource(\"Area2D/Sprite2D\") print(a\[0\].name) \#
Prints Sprite2D print(a\[1\]) \# Prints \<null\> print(a\[2\]) \# Prints
\^\"\"

var b = get_node_and_resource(\"Area2D/Sprite2D:texture:atlas\")
print(b\[0\].name) \# Prints Sprite2D print(b\[1\].get_class()) \#
Prints AtlasTexture print(b\[2\]) \# Prints \^\"\"

var c = get_node_and_resource(\"Area2D/Sprite2D:texture:atlas:region\")
print(c\[0\].name) \# Prints Sprite2D print(c\[1\].get_class()) \#
Prints AtlasTexture print(c\[2\]) \# Prints \^\":region\"
:::

::: code-tab
csharp

var a = GetNodeAndResource(NodePath(\"Area2D/Sprite2D\"));
GD.Print(a\[0\].Name); // Prints Sprite2D GD.Print(a\[1\]); // Prints
\<null\> GD.Print(a\[2\]); // Prints \^\"

var b = GetNodeAndResource(NodePath(\"Area2D/Sprite2D:texture:atlas\"));
GD.Print(b\[0\].name); // Prints Sprite2D GD.Print(b\[1\].get_class());
// Prints AtlasTexture GD.Print(b\[2\]); // Prints \^\"\"

var c =
GetNodeAndResource(NodePath(\"Area2D/Sprite2D:texture:atlas:region\"));
GD.Print(c\[0\].name); // Prints Sprite2D GD.Print(c\[1\].get_class());
// Prints AtlasTexture GD.Print(c\[2\]); // Prints \^\":region\"
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_node_or_null}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**get_node_or_null**(path: `NodePath<class_NodePath>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_node_or_null>`{.interpreted-text
role="ref"}

Fetches a node by `NodePath<class_NodePath>`{.interpreted-text
role="ref"}. Similar to
`get_node()<class_Node_method_get_node>`{.interpreted-text role="ref"},
but does not generate an error if `path` does not point to a valid node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_node_rpc_config}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_node_rpc_config**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_node_rpc_config>`{.interpreted-text
role="ref"}

Returns a `Dictionary<class_Dictionary>`{.interpreted-text role="ref"}
mapping method names to their RPC configuration defined for this node
using `rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method only returns the RPC configuration assigned
via `rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"}. See
`Script.get_rpc_config()<class_Script_method_get_rpc_config>`{.interpreted-text
role="ref"} to retrieve the RPCs defined by the
`Script<class_Script>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_orphan_node_ids}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`int<class_int>`{.interpreted-text role="ref"}\]
**get_orphan_node_ids**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_orphan_node_ids>`{.interpreted-text
role="ref"}

Returns object IDs of all orphan nodes (nodes outside the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}). Used for
debugging.

\*\*Note:\*\*
`get_orphan_node_ids()<class_Node_method_get_orphan_node_ids>`{.interpreted-text
role="ref"} only works in debug builds. When called in a project
exported in release mode,
`get_orphan_node_ids()<class_Node_method_get_orphan_node_ids>`{.interpreted-text
role="ref"} will return an empty array.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_parent}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"} **get_parent**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_parent>`{.interpreted-text
role="ref"}

Returns this node\'s parent node, or `null` if the node doesn\'t have a
parent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_path}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **get_path**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_path>`{.interpreted-text
role="ref"}

Returns the node\'s absolute path, relative to the
`SceneTree.root<class_SceneTree_property_root>`{.interpreted-text
role="ref"}. If the node is not inside the scene tree, this method fails
and returns an empty `NodePath<class_NodePath>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_path_to}
::: rst-class
classref-method
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**get_path_to**(node: `Node<class_Node>`{.interpreted-text role="ref"},
use_unique_path: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_path_to>`{.interpreted-text
role="ref"}

Returns the relative `NodePath<class_NodePath>`{.interpreted-text
role="ref"} from this node to the specified `node`. Both nodes must be
in the same `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}
or scene hierarchy, otherwise this method fails and returns an empty
`NodePath<class_NodePath>`{.interpreted-text role="ref"}.

If `use_unique_path` is `true`, returns the shortest path accounting for
this node\'s unique name (see
`unique_name_in_owner<class_Node_property_unique_name_in_owner>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* If you get a relative path which starts from a unique
node, the path may be longer than a normal relative path, due to the
addition of the unique node\'s name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_physics_process_delta_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_physics_process_delta_time**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_physics_process_delta_time>`{.interpreted-text
role="ref"}

Returns the time elapsed (in seconds) since the last physics callback.
This value is identical to
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}\'s `delta` parameter, and is often consistent at run-time,
unless
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} is changed. See also
`NOTIFICATION_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The returned value will be larger than expected if running
at a framerate lower than
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} /
`Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>`{.interpreted-text
role="ref"} FPS. This is done to avoid \"spiral of death\" scenarios
where performance would plummet due to an ever-increasing number of
physics steps per frame. This behavior affects both
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} and
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. As a result, avoid using `delta` for time measurements in
real-world seconds. Use the `Time<class_Time>`{.interpreted-text
role="ref"} singleton\'s methods for this purpose instead, such as
`Time.get_ticks_usec()<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_process_delta_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_process_delta_time**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_process_delta_time>`{.interpreted-text
role="ref"}

Returns the time elapsed (in seconds) since the last process callback.
This value is identical to
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}\'s `delta` parameter, and may vary from frame to frame. See
also
`NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The returned value will be larger than expected if running
at a framerate lower than
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} /
`Engine.max_physics_steps_per_frame<class_Engine_property_max_physics_steps_per_frame>`{.interpreted-text
role="ref"} FPS. This is done to avoid \"spiral of death\" scenarios
where performance would plummet due to an ever-increasing number of
physics steps per frame. This behavior affects both
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} and
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. As a result, avoid using `delta` for time measurements in
real-world seconds. Use the `Time<class_Time>`{.interpreted-text
role="ref"} singleton\'s methods for this purpose instead, such as
`Time.get_ticks_usec()<class_Time_method_get_ticks_usec>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_scene_instance_load_placeholder}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_scene_instance_load_placeholder**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_get_scene_instance_load_placeholder>`{.interpreted-text
role="ref"}

Returns `true` if this node is an instance load placeholder. See
`InstancePlaceholder<class_InstancePlaceholder>`{.interpreted-text
role="ref"} and
`set_scene_instance_load_placeholder()<class_Node_method_set_scene_instance_load_placeholder>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_tree}
::: rst-class
classref-method
:::
::::

`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}
**get_tree**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_tree>`{.interpreted-text
role="ref"}

Returns the `SceneTree<class_SceneTree>`{.interpreted-text role="ref"}
that contains this node. If this node is not inside the tree, generates
an error and returns `null`. See also
`is_inside_tree()<class_Node_method_is_inside_tree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_tree_string}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tree_string**()
`🔗<class_Node_method_get_tree_string>`{.interpreted-text role="ref"}

Returns the tree as a `String<class_String>`{.interpreted-text
role="ref"}. Used mainly for debugging purposes. This version displays
the path relative to the current node, and is good for copy/pasting into
the `get_node()<class_Node_method_get_node>`{.interpreted-text
role="ref"} function. It also can be used in game UI/UX.

May print, for example:

``` text
TheGame
TheGame/Menu
TheGame/Menu/Label
TheGame/Menu/Camera2D
TheGame/SplashScreen
TheGame/SplashScreen/Camera2D
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_tree_string_pretty}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_tree_string_pretty**()
`🔗<class_Node_method_get_tree_string_pretty>`{.interpreted-text
role="ref"}

Similar to
`get_tree_string()<class_Node_method_get_tree_string>`{.interpreted-text
role="ref"}, this returns the tree as a
`String<class_String>`{.interpreted-text role="ref"}. This version
displays a more graphical representation similar to what is displayed in
the Scene Dock. It is useful for inspecting larger trees.

May print, for example:

``` text
┖╴TheGame
   ┠╴Menu
   ┃  ┠╴Label
   ┃  ┖╴Camera2D
   ┖╴SplashScreen
      ┖╴Camera2D
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_viewport}
::: rst-class
classref-method
:::
::::

`Viewport<class_Viewport>`{.interpreted-text role="ref"}
**get_viewport**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_viewport>`{.interpreted-text
role="ref"}

Returns the node\'s closest `Viewport<class_Viewport>`{.interpreted-text
role="ref"} ancestor, if the node is inside the tree. Otherwise, returns
`null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_get_window}
::: rst-class
classref-method
:::
::::

`Window<class_Window>`{.interpreted-text role="ref"} **get_window**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_get_window>`{.interpreted-text
role="ref"}

Returns the `Window<class_Window>`{.interpreted-text role="ref"} that
contains this node. If the node is in the main window, this is
equivalent to getting the root node (`get_tree().get_root()`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_has_node}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_node**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_has_node>`{.interpreted-text
role="ref"}

Returns `true` if the `path` points to a valid node. See also
`get_node()<class_Node_method_get_node>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_has_node_and_resource}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_node_and_resource**(path:
`NodePath<class_NodePath>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_has_node_and_resource>`{.interpreted-text
role="ref"}

Returns `true` if `path` points to a valid node and its subnames point
to a valid `Resource<class_Resource>`{.interpreted-text role="ref"},
e.g. `Area2D/CollisionShape2D:shape`. Properties that are not
`Resource<class_Resource>`{.interpreted-text role="ref"} types (such as
nodes or other `Variant<class_Variant>`{.interpreted-text role="ref"}
types) are not considered. See also
`get_node_and_resource()<class_Node_method_get_node_and_resource>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_ancestor_of}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_ancestor_of**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_is_ancestor_of>`{.interpreted-text
role="ref"}

Returns `true` if the given `node` is a direct or indirect child of this
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_displayed_folded}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_displayed_folded**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_displayed_folded>`{.interpreted-text
role="ref"}

Returns `true` if the node is folded (collapsed) in the Scene dock. This
method is intended to be used in editor plugins and tools. See also
`set_display_folded()<class_Node_method_set_display_folded>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_editable_instance}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_editable_instance**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_editable_instance>`{.interpreted-text
role="ref"}

Returns `true` if `node` has editable children enabled relative to this
node. This method is intended to be used in editor plugins and tools.
See also
`set_editable_instance()<class_Node_method_set_editable_instance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_greater_than}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_greater_than**(node: `Node<class_Node>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_is_greater_than>`{.interpreted-text
role="ref"}

Returns `true` if the given `node` occurs later in the scene hierarchy
than this node. A node occurring later is usually processed last.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_in_group}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_in_group**(group:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_is_in_group>`{.interpreted-text
role="ref"}

Returns `true` if this node has been added to the given `group`. See
`add_to_group()<class_Node_method_add_to_group>`{.interpreted-text
role="ref"} and
`remove_from_group()<class_Node_method_remove_from_group>`{.interpreted-text
role="ref"}. See also notes in the description, and the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}\'s group
methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_inside_tree}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_inside_tree**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_is_inside_tree>`{.interpreted-text
role="ref"}

Returns `true` if this node is currently inside a
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}. See also
`get_tree()<class_Node_method_get_tree>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_multiplayer_authority}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_multiplayer_authority**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_multiplayer_authority>`{.interpreted-text
role="ref"}

Returns `true` if the local system is the multiplayer authority of this
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_node_ready}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_node_ready**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_is_node_ready>`{.interpreted-text
role="ref"}

Returns `true` if the node is ready, i.e. it\'s inside scene tree and
all its children are initialized.

`request_ready()<class_Node_method_request_ready>`{.interpreted-text
role="ref"} resets it back to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_part_of_edited_scene}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_part_of_edited_scene**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_part_of_edited_scene>`{.interpreted-text
role="ref"}

Returns `true` if the node is part of the scene currently opened in the
editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_physics_interpolated}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_physics_interpolated**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_physics_interpolated>`{.interpreted-text
role="ref"}

Returns `true` if physics interpolation is enabled for this node (see
`physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* Interpolation will only be active if both the flag is set
**and** physics interpolation is enabled within the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}. This can be
tested using
`is_physics_interpolated_and_enabled()<class_Node_method_is_physics_interpolated_and_enabled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_physics_interpolated_and_enabled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_physics_interpolated_and_enabled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_physics_interpolated_and_enabled>`{.interpreted-text
role="ref"}

Returns `true` if physics interpolation is enabled (see
`physics_interpolation_mode<class_Node_property_physics_interpolation_mode>`{.interpreted-text
role="ref"}) **and** enabled in the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

This is a convenience version of
`is_physics_interpolated()<class_Node_method_is_physics_interpolated>`{.interpreted-text
role="ref"} that also checks whether physics interpolation is enabled
globally.

See
`SceneTree.physics_interpolation<class_SceneTree_property_physics_interpolation>`{.interpreted-text
role="ref"} and
`ProjectSettings.physics/common/physics_interpolation<class_ProjectSettings_property_physics/common/physics_interpolation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_physics_processing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_physics_processing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_physics_processing>`{.interpreted-text
role="ref"}

Returns `true` if physics processing is enabled (see
`set_physics_process()<class_Node_method_set_physics_process>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_physics_processing_internal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_physics_processing_internal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_physics_processing_internal>`{.interpreted-text
role="ref"}

Returns `true` if internal physics processing is enabled (see
`set_physics_process_internal()<class_Node_method_set_physics_process_internal>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_processing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_processing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_is_processing>`{.interpreted-text
role="ref"}

Returns `true` if processing is enabled (see
`set_process()<class_Node_method_set_process>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_processing_input}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_processing_input**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_processing_input>`{.interpreted-text
role="ref"}

Returns `true` if the node is processing input (see
`set_process_input()<class_Node_method_set_process_input>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_processing_internal}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_processing_internal**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_processing_internal>`{.interpreted-text
role="ref"}

Returns `true` if internal processing is enabled (see
`set_process_internal()<class_Node_method_set_process_internal>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_processing_shortcut_input}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_processing_shortcut_input**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_processing_shortcut_input>`{.interpreted-text
role="ref"}

Returns `true` if the node is processing shortcuts (see
`set_process_shortcut_input()<class_Node_method_set_process_shortcut_input>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_processing_unhandled_input}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_processing_unhandled_input**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_processing_unhandled_input>`{.interpreted-text
role="ref"}

Returns `true` if the node is processing unhandled input (see
`set_process_unhandled_input()<class_Node_method_set_process_unhandled_input>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_is_processing_unhandled_key_input}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_processing_unhandled_key_input**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_is_processing_unhandled_key_input>`{.interpreted-text
role="ref"}

Returns `true` if the node is processing unhandled key input (see
`set_process_unhandled_key_input()<class_Node_method_set_process_unhandled_key_input>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_move_child}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**move_child**(child_node: `Node<class_Node>`{.interpreted-text
role="ref"}, to_index: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Node_method_move_child>`{.interpreted-text role="ref"}

Moves `child_node` to the given index. A node\'s index is the order
among its siblings. If `to_index` is negative, the index is counted from
the end of the list. See also
`get_child()<class_Node_method_get_child>`{.interpreted-text role="ref"}
and `get_index()<class_Node_method_get_index>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* The processing order of several engine callbacks
(`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"},
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}, etc.) and notifications sent through
`propagate_notification()<class_Node_method_propagate_notification>`{.interpreted-text
role="ref"} is affected by tree order.
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} nodes are
also rendered in tree order. See also
`process_priority<class_Node_property_process_priority>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_notify_deferred_thread_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_deferred_thread_group**(what:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Node_method_notify_deferred_thread_group>`{.interpreted-text
role="ref"}

Similar to
`call_deferred_thread_group()<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"}, but for notifications.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_notify_thread_safe}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_thread_safe**(what: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Node_method_notify_thread_safe>`{.interpreted-text role="ref"}

Similar to
`call_thread_safe()<class_Node_method_call_thread_safe>`{.interpreted-text
role="ref"}, but for notifications.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_print_orphan_nodes}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**print_orphan_nodes**()
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Node_method_print_orphan_nodes>`{.interpreted-text role="ref"}

Prints all orphan nodes (nodes outside the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}). Useful for
debugging.

\*\*Note:\*\* This method only works in debug builds. Does nothing in a
project exported in release mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_print_tree}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**print_tree**() `🔗<class_Node_method_print_tree>`{.interpreted-text
role="ref"}

Prints the node and its children to the console, recursively. The node
does not have to be inside the tree. This method outputs
`NodePath<class_NodePath>`{.interpreted-text role="ref"}s relative to
this node, and is good for copy/pasting into
`get_node()<class_Node_method_get_node>`{.interpreted-text role="ref"}.
See also
`print_tree_pretty()<class_Node_method_print_tree_pretty>`{.interpreted-text
role="ref"}.

May print, for example:

``` text
.
Menu
Menu/Label
Menu/Camera2D
SplashScreen
SplashScreen/Camera2D
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_print_tree_pretty}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**print_tree_pretty**()
`🔗<class_Node_method_print_tree_pretty>`{.interpreted-text role="ref"}

Prints the node and its children to the console, recursively. The node
does not have to be inside the tree. Similar to
`print_tree()<class_Node_method_print_tree>`{.interpreted-text
role="ref"}, but the graphical representation looks like what is
displayed in the editor\'s Scene dock. It is useful for inspecting
larger trees.

May print, for example:

``` text
┖╴TheGame
   ┠╴Menu
   ┃  ┠╴Label
   ┃  ┖╴Camera2D
   ┖╴SplashScreen
      ┖╴Camera2D
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_propagate_call}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**propagate_call**(method:
`StringName<class_StringName>`{.interpreted-text role="ref"}, args:
`Array<class_Array>`{.interpreted-text role="ref"} = \[\], parent_first:
`bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Node_method_propagate_call>`{.interpreted-text role="ref"}

Calls the given `method` name, passing `args` as arguments, on this node
and all of its children, recursively.

If `parent_first` is `true`, the method is called on this node first,
then on all of its children. If `false`, the children\'s methods are
called first.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_propagate_notification}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**propagate_notification**(what: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_Node_method_propagate_notification>`{.interpreted-text
role="ref"}

Calls
`Object.notification()<class_Object_method_notification>`{.interpreted-text
role="ref"} with `what` on this node and all of its children,
recursively.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_queue_accessibility_update}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_accessibility_update**()
`🔗<class_Node_method_queue_accessibility_update>`{.interpreted-text
role="ref"}

Queues an accessibility information update for this node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_queue_free}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**queue_free**() `🔗<class_Node_method_queue_free>`{.interpreted-text
role="ref"}

Queues this node to be deleted at the end of the current frame. When
deleted, all of its children are deleted as well, and all references to
the node and its children become invalid.

Unlike with `Object.free()<class_Object_method_free>`{.interpreted-text
role="ref"}, the node is not deleted instantly, and it can still be
accessed before deletion. It is also safe to call
`queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} multiple times. Use
`Object.is_queued_for_deletion()<class_Object_method_is_queued_for_deletion>`{.interpreted-text
role="ref"} to check if the node will be deleted at the end of the
frame.

\*\*Note:\*\* The node will only be freed after all other deferred calls
are finished. Using this method is not always the same as calling
`Object.free()<class_Object_method_free>`{.interpreted-text role="ref"}
through
`Object.call_deferred()<class_Object_method_call_deferred>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_remove_child}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_child**(node: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_Node_method_remove_child>`{.interpreted-text role="ref"}

Removes a child `node`. The `node`, along with its children, are **not**
deleted. To delete a node, see
`queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When this node is inside the tree, this method sets the
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} of the
removed `node` (or its descendants) to `null`, if their
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} is no
longer an ancestor (see
`is_ancestor_of()<class_Node_method_is_ancestor_of>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_remove_from_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_from_group**(group:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_Node_method_remove_from_group>`{.interpreted-text role="ref"}

Removes the node from the given `group`. Does nothing if the node is not
in the `group`. See also notes in the description, and the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}\'s group
methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_reparent}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reparent**(new_parent: `Node<class_Node>`{.interpreted-text
role="ref"}, keep_global_transform: `bool<class_bool>`{.interpreted-text
role="ref"} = true) `🔗<class_Node_method_reparent>`{.interpreted-text
role="ref"}

Changes the parent of this **Node** to the `new_parent`. The node needs
to already have a parent. The node\'s
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} is
preserved if its owner is still reachable from the new location (i.e.,
the node is still a descendant of the new parent after the operation).

If `keep_global_transform` is `true`, the node\'s global transform will
be preserved if supported. `Node2D<class_Node2D>`{.interpreted-text
role="ref"}, `Node3D<class_Node3D>`{.interpreted-text role="ref"} and
`Control<class_Control>`{.interpreted-text role="ref"} support this
argument (but `Control<class_Control>`{.interpreted-text role="ref"}
keeps only position).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_replace_by}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**replace_by**(node: `Node<class_Node>`{.interpreted-text role="ref"},
keep_groups: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_Node_method_replace_by>`{.interpreted-text role="ref"}

Replaces this node by the given `node`. All children of this node are
moved to `node`.

If `keep_groups` is `true`, the `node` is added to the same groups that
the replaced node is in (see
`add_to_group()<class_Node_method_add_to_group>`{.interpreted-text
role="ref"}).

\*\*Warning:\*\* The replaced node is removed from the tree, but it is
**not** deleted. To prevent memory leaks, store a reference to the node
in a variable, or use
`Object.free()<class_Object_method_free>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_request_ready}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_ready**()
`🔗<class_Node_method_request_ready>`{.interpreted-text role="ref"}

Requests `_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} to be called again the next time the node enters the tree.
Does **not** immediately call
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method only affects the current node. If the node\'s
children also need to request ready, this method needs to be called for
each one of them. When the node and its children enter the tree again,
the order of
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} callbacks will be the same as normal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_reset_physics_interpolation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**reset_physics_interpolation**()
`🔗<class_Node_method_reset_physics_interpolation>`{.interpreted-text
role="ref"}

When physics interpolation is active, moving a node to a radically
different transform (such as placement within a level) can result in a
visible glitch as the object is rendered moving from the old to new
position over the physics tick.

That glitch can be prevented by calling this method, which temporarily
disables interpolation until the physics tick is complete.

The notification
`NOTIFICATION_RESET_PHYSICS_INTERPOLATION<class_Node_constant_NOTIFICATION_RESET_PHYSICS_INTERPOLATION>`{.interpreted-text
role="ref"} will be received by the node and all children recursively.

\*\*Note:\*\* This function should be called **after** moving the node,
rather than before.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_rpc}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**rpc**(method: `StringName<class_StringName>`{.interpreted-text
role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_rpc>`{.interpreted-text role="ref"}

Sends a remote procedure call request for the given `method` to peers on
the network (and locally), sending additional arguments to the method
called by the RPC. The call request will only be received by nodes with
the same `NodePath<class_NodePath>`{.interpreted-text role="ref"},
including the exact same
`name<class_Node_property_name>`{.interpreted-text role="ref"}. Behavior
depends on the RPC configuration for the given `method` (see
`rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"} and
`@GDScript.@rpc<class_@GDScript_annotation_@rpc>`{.interpreted-text
role="ref"}). By default, methods are not exposed to RPCs.

May return
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if the call is successful,
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if the arguments passed in the `method` do not match,
`@GlobalScope.ERR_UNCONFIGURED<class_@GlobalScope_constant_ERR_UNCONFIGURED>`{.interpreted-text
role="ref"} if the node\'s
`multiplayer<class_Node_property_multiplayer>`{.interpreted-text
role="ref"} cannot be fetched (such as when the node is not inside the
tree),
`@GlobalScope.ERR_CONNECTION_ERROR<class_@GlobalScope_constant_ERR_CONNECTION_ERROR>`{.interpreted-text
role="ref"} if
`multiplayer<class_Node_property_multiplayer>`{.interpreted-text
role="ref"}\'s connection is not available.

\*\*Note:\*\* You can only safely use RPCs on clients after you received
the
`MultiplayerAPI.connected_to_server<class_MultiplayerAPI_signal_connected_to_server>`{.interpreted-text
role="ref"} signal from the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.
You also need to keep track of the connection state, either by the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}
signals like
`MultiplayerAPI.server_disconnected<class_MultiplayerAPI_signal_server_disconnected>`{.interpreted-text
role="ref"} or by checking
(`get_multiplayer().peer.get_connection_status() == CONNECTION_CONNECTED`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_rpc_config}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rpc_config**(method: `StringName<class_StringName>`{.interpreted-text
role="ref"}, config: `Variant<class_Variant>`{.interpreted-text
role="ref"}) `🔗<class_Node_method_rpc_config>`{.interpreted-text
role="ref"}

Changes the RPC configuration for the given `method`. `config` should
either be `null` to disable the feature (as by default), or a
`Dictionary<class_Dictionary>`{.interpreted-text role="ref"} containing
the following entries:

- `rpc_mode`: see
  `RPCMode<enum_MultiplayerAPI_RPCMode>`{.interpreted-text role="ref"};
- `transfer_mode`: see
  `TransferMode<enum_MultiplayerPeer_TransferMode>`{.interpreted-text
  role="ref"};
- `call_local`: if `true`, the method will also be called locally;
- `channel`: an `int<class_int>`{.interpreted-text role="ref"}
  representing the channel to send the RPC on.

\*\*Note:\*\* In GDScript, this method corresponds to the
`@GDScript.@rpc<class_@GDScript_annotation_@rpc>`{.interpreted-text
role="ref"} annotation, with various parameters passed (`@rpc(any)`,
`@rpc(authority)`\...). See also the
`high-level multiplayer <../tutorials/networking/high_level_multiplayer>`{.interpreted-text
role="doc"} tutorial.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_rpc_id}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**rpc_id**(peer_id: `int<class_int>`{.interpreted-text role="ref"},
method: `StringName<class_StringName>`{.interpreted-text role="ref"},
\...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"} `🔗<class_Node_method_rpc_id>`{.interpreted-text
role="ref"}

Sends a `rpc()<class_Node_method_rpc>`{.interpreted-text role="ref"} to
a specific peer identified by `peer_id` (see
`MultiplayerPeer.set_target_peer()<class_MultiplayerPeer_method_set_target_peer>`{.interpreted-text
role="ref"}).

May return
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if the call is successful,
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if the arguments passed in the `method` do not match,
`@GlobalScope.ERR_UNCONFIGURED<class_@GlobalScope_constant_ERR_UNCONFIGURED>`{.interpreted-text
role="ref"} if the node\'s
`multiplayer<class_Node_property_multiplayer>`{.interpreted-text
role="ref"} cannot be fetched (such as when the node is not inside the
tree),
`@GlobalScope.ERR_CONNECTION_ERROR<class_@GlobalScope_constant_ERR_CONNECTION_ERROR>`{.interpreted-text
role="ref"} if
`multiplayer<class_Node_property_multiplayer>`{.interpreted-text
role="ref"}\'s connection is not available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_deferred_thread_group}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_deferred_thread_group**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Node_method_set_deferred_thread_group>`{.interpreted-text
role="ref"}

Similar to
`call_deferred_thread_group()<class_Node_method_call_deferred_thread_group>`{.interpreted-text
role="ref"}, but for setting properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_display_folded}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_display_folded**(fold: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node_method_set_display_folded>`{.interpreted-text role="ref"}

If set to `true`, the node appears folded in the Scene dock. As a
result, all of its children are hidden. This method is intended to be
used in editor plugins and tools, but it also works in release builds.
See also
`is_displayed_folded()<class_Node_method_is_displayed_folded>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_editable_instance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_editable_instance**(node: `Node<class_Node>`{.interpreted-text
role="ref"}, is_editable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node_method_set_editable_instance>`{.interpreted-text
role="ref"}

Set to `true` to allow all nodes owned by `node` to be available, and
editable, in the Scene dock, even if their
`owner<class_Node_property_owner>`{.interpreted-text role="ref"} is not
the scene root. This method is intended to be used in editor plugins and
tools, but it also works in release builds. See also
`is_editable_instance()<class_Node_method_is_editable_instance>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_multiplayer_authority}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_multiplayer_authority**(id: `int<class_int>`{.interpreted-text
role="ref"}, recursive: `bool<class_bool>`{.interpreted-text role="ref"}
= true)
`🔗<class_Node_method_set_multiplayer_authority>`{.interpreted-text
role="ref"}

Sets the node\'s multiplayer authority to the peer with the given peer
`id`. The multiplayer authority is the peer that has authority over the
node on the network. Defaults to peer ID 1 (the server). Useful in
conjunction with
`rpc_config()<class_Node_method_rpc_config>`{.interpreted-text
role="ref"} and the
`MultiplayerAPI<class_MultiplayerAPI>`{.interpreted-text role="ref"}.

If `recursive` is `true`, the given peer is recursively set as the
authority for all children of this node.

\*\*Warning:\*\* This does **not** automatically replicate the new
authority to other peers. It is the developer\'s responsibility to do
so. You may replicate the new authority\'s information using
`MultiplayerSpawner.spawn_function<class_MultiplayerSpawner_property_spawn_function>`{.interpreted-text
role="ref"}, an RPC, or a
`MultiplayerSynchronizer<class_MultiplayerSynchronizer>`{.interpreted-text
role="ref"}. Furthermore, the parent\'s authority does **not** propagate
to newly added children.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_physics_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_physics_process**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node_method_set_physics_process>`{.interpreted-text
role="ref"}

If set to `true`, enables physics (fixed framerate) processing. When a
node is being processed, it will receive a
`NOTIFICATION_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_PHYSICS_PROCESS>`{.interpreted-text
role="ref"} at a fixed (usually 60 FPS, see
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"} to change) interval (and the
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} callback will be called if it exists).

\*\*Note:\*\* If
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} is overridden, this will be automatically enabled before
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_physics_process_internal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_physics_process_internal**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node_method_set_physics_process_internal>`{.interpreted-text
role="ref"}

If set to `true`, enables internal physics for this node. Internal
physics processing happens in isolation from the normal
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} calls and is used by some nodes internally to guarantee
proper functioning even if the node is paused or physics processing is
disabled for scripting
(`set_physics_process()<class_Node_method_set_physics_process>`{.interpreted-text
role="ref"}).

\*\*Warning:\*\* Built-in nodes rely on internal processing for their
internal logic. Disabling it is unsafe and may lead to unexpected
behavior. Use this method if you know what you are doing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process**(enable: `bool<class_bool>`{.interpreted-text
role="ref"}) `🔗<class_Node_method_set_process>`{.interpreted-text
role="ref"}

If set to `true`, enables processing. When a node is being processed, it
will receive a
`NOTIFICATION_PROCESS<class_Node_constant_NOTIFICATION_PROCESS>`{.interpreted-text
role="ref"} on every drawn frame (and the
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} callback will be called if it exists).

\*\*Note:\*\* If
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} is overridden, this will be automatically enabled before
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} is called.

\*\*Note:\*\* This method only affects the
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} callback, i.e. it has no effect on other callbacks like
`_physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}. If you want to disable all processing for the node, set
`process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"} to
`PROCESS_MODE_DISABLED<class_Node_constant_PROCESS_MODE_DISABLED>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_process_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process_input**(enable: `bool<class_bool>`{.interpreted-text
role="ref"}) `🔗<class_Node_method_set_process_input>`{.interpreted-text
role="ref"}

If set to `true`, enables input processing.

\*\*Note:\*\* If
`_input()<class_Node_private_method__input>`{.interpreted-text
role="ref"} is overridden, this will be automatically enabled before
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} is called. Input processing is also already enabled for GUI
controls, such as `Button<class_Button>`{.interpreted-text role="ref"}
and `TextEdit<class_TextEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_process_internal}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process_internal**(enable: `bool<class_bool>`{.interpreted-text
role="ref"})
`🔗<class_Node_method_set_process_internal>`{.interpreted-text
role="ref"}

If set to `true`, enables internal processing for this node. Internal
processing happens in isolation from the normal
`_process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} calls and is used by some nodes internally to guarantee
proper functioning even if the node is paused or processing is disabled
for scripting
(`set_process()<class_Node_method_set_process>`{.interpreted-text
role="ref"}).

\*\*Warning:\*\* Built-in nodes rely on internal processing for their
internal logic. Disabling it is unsafe and may lead to unexpected
behavior. Use this method if you know what you are doing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_process_shortcut_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process_shortcut_input**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node_method_set_process_shortcut_input>`{.interpreted-text
role="ref"}

If set to `true`, enables shortcut processing for this node.

\*\*Note:\*\* If
`_shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
role="ref"} is overridden, this will be automatically enabled before
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_process_unhandled_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process_unhandled_input**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node_method_set_process_unhandled_input>`{.interpreted-text
role="ref"}

If set to `true`, enables unhandled input processing. It enables the
node to receive all input that was not previously handled (usually by a
`Control<class_Control>`{.interpreted-text role="ref"}).

\*\*Note:\*\* If
`_unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
role="ref"} is overridden, this will be automatically enabled before
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} is called. Unhandled input processing is also already
enabled for GUI controls, such as
`Button<class_Button>`{.interpreted-text role="ref"} and
`TextEdit<class_TextEdit>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_process_unhandled_key_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_process_unhandled_key_input**(enable:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node_method_set_process_unhandled_key_input>`{.interpreted-text
role="ref"}

If set to `true`, enables unhandled key input processing.

\*\*Note:\*\* If
`_unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
role="ref"} is overridden, this will be automatically enabled before
`_ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"} is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_scene_instance_load_placeholder}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_scene_instance_load_placeholder**(load_placeholder:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Node_method_set_scene_instance_load_placeholder>`{.interpreted-text
role="ref"}

If set to `true`, the node becomes an
`InstancePlaceholder<class_InstancePlaceholder>`{.interpreted-text
role="ref"} when packed and instantiated from a
`PackedScene<class_PackedScene>`{.interpreted-text role="ref"}. See also
`get_scene_instance_load_placeholder()<class_Node_method_get_scene_instance_load_placeholder>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_thread_safe}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_thread_safe**(property:
`StringName<class_StringName>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_Node_method_set_thread_safe>`{.interpreted-text role="ref"}

Similar to
`call_thread_safe()<class_Node_method_call_thread_safe>`{.interpreted-text
role="ref"}, but for setting properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_set_translation_domain_inherited}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_translation_domain_inherited**()
`🔗<class_Node_method_set_translation_domain_inherited>`{.interpreted-text
role="ref"}

Makes this node inherit the translation domain from its parent node. If
this node has no parent, the main translation domain will be used.

This is the default behavior for all nodes. Calling
`Object.set_translation_domain()<class_Object_method_set_translation_domain>`{.interpreted-text
role="ref"} disables this behavior.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Node_method_update_configuration_warnings}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_configuration_warnings**()
`🔗<class_Node_method_update_configuration_warnings>`{.interpreted-text
role="ref"}

Refreshes the warnings displayed for this node in the Scene dock. Use
`_get_configuration_warnings()<class_Node_private_method__get_configuration_warnings>`{.interpreted-text
role="ref"} to customize the warning messages to display.
