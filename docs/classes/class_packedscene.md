github_url
:   hide

# PackedScene {#class_PackedScene}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

An abstraction of a serialized scene.

::: rst-class
classref-introduction-group
:::

## Description

A simplified interface to a scene file. Provides access to operations
and checks that can be performed on the scene resource itself.

Can be used to save a node to a file. When saving, the node as well as
all the nodes it owns get saved (see
`Node.owner<class_Node_property_owner>`{.interpreted-text role="ref"}
property).

\*\*Note:\*\* The node doesn\'t need to own itself.

\*\*Example:\*\* Load a saved scene:

::::: tabs
::: code-tab
gdscript

\# Use load() instead of preload() if the path isn\'t known at
compile-time. var scene = preload(\"res://scene.tscn\").instantiate() \#
Add the node as a child of the node the script is attached to.
add_child(scene)
:::

::: code-tab
csharp

// C# has no preload, so you have to always use
ResourceLoader.Load\<PackedScene\>(). var scene =
ResourceLoader.Load\<PackedScene\>(\"res://scene.tscn\").Instantiate();
// Add the node as a child of the node the script is attached to.
AddChild(scene);
:::
:::::

\*\*Example:\*\* Save a node with different owners. The following
example creates 3 objects: `Node2D<class_Node2D>`{.interpreted-text
role="ref"} (`node`), `RigidBody2D<class_RigidBody2D>`{.interpreted-text
role="ref"} (`body`) and
`CollisionObject2D<class_CollisionObject2D>`{.interpreted-text
role="ref"} (`collision`). `collision` is a child of `body` which is a
child of `node`. Only `body` is owned by `node` and
`pack()<class_PackedScene_method_pack>`{.interpreted-text role="ref"}
will therefore only save those two nodes, but not `collision`.

::::: tabs
::: code-tab
gdscript

\# Create the objects. var node = Node2D.new() var body =
RigidBody2D.new() var collision = CollisionShape2D.new()

\# Create the object hierarchy. body.add_child(collision)
node.add_child(body)

\# Change owner of [body]{.title-ref}, but not of
[collision]{.title-ref}. body.owner = node var scene = PackedScene.new()

\# Only [node]{.title-ref} and [body]{.title-ref} are now packed. var
result = scene.pack(node) if result == OK: var error =
ResourceSaver.save(scene, \"res://path/name.tscn\") \# Or
\"user://\...\" if error != OK: push_error(\"An error occurred while
saving the scene to disk.\")
:::

::: code-tab
csharp

// Create the objects. var node = new Node2D(); var body = new
RigidBody2D(); var collision = new CollisionShape2D();

// Create the object hierarchy. body.AddChild(collision);
node.AddChild(body);

// Change owner of [body]{.title-ref}, but not of
[collision]{.title-ref}. body.Owner = node; var scene = new
PackedScene();

// Only [node]{.title-ref} and [body]{.title-ref} are now packed. Error
result = scene.Pack(node); if (result == Error.Ok) { Error error =
ResourceSaver.Save(scene, \"res://path/name.tscn\"); // Or
\"user://\...\" if (error != Error.Ok) { GD.PushError(\"An error
occurred while saving the scene to disk.\"); } }
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D Role Playing Game (RPG)
  Demo](https://godotengine.org/asset-library/asset/2729)

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

## Enumerations

:::: {#enum_PackedScene_GenEditState}
::: rst-class
classref-enumeration
:::
::::

enum **GenEditState**:
`🔗<enum_PackedScene_GenEditState>`{.interpreted-text role="ref"}

:::: {#class_PackedScene_constant_GEN_EDIT_STATE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_PackedScene_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_DISABLED** = `0`

If passed to
`instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}, blocks edits to the scene state.

:::: {#class_PackedScene_constant_GEN_EDIT_STATE_INSTANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_PackedScene_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_INSTANCE** = `1`

If passed to
`instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}, provides local scene resources to the local scene.

\*\*Note:\*\* Only available in editor builds.

:::: {#class_PackedScene_constant_GEN_EDIT_STATE_MAIN}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_PackedScene_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_MAIN** = `2`

If passed to
`instantiate()<class_PackedScene_method_instantiate>`{.interpreted-text
role="ref"}, provides local scene resources to the local scene. Only the
main scene should receive the main edit state.

\*\*Note:\*\* Only available in editor builds.

:::: {#class_PackedScene_constant_GEN_EDIT_STATE_MAIN_INHERITED}
::: rst-class
classref-enumeration-constant
:::
::::

`GenEditState<enum_PackedScene_GenEditState>`{.interpreted-text
role="ref"} **GEN_EDIT_STATE_MAIN_INHERITED** = `3`

It\'s similar to
`GEN_EDIT_STATE_MAIN<class_PackedScene_constant_GEN_EDIT_STATE_MAIN>`{.interpreted-text
role="ref"}, but for the case where the scene is being instantiated to
be the base of another one.

\*\*Note:\*\* Only available in editor builds.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_PackedScene_method_can_instantiate}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **can_instantiate**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedScene_method_can_instantiate>`{.interpreted-text
role="ref"}

Returns `true` if the scene file has nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedScene_method_get_state}
::: rst-class
classref-method
:::
::::

`SceneState<class_SceneState>`{.interpreted-text role="ref"}
**get_state**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_PackedScene_method_get_state>`{.interpreted-text
role="ref"}

Returns the `SceneState<class_SceneState>`{.interpreted-text role="ref"}
representing the scene file contents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedScene_method_instantiate}
::: rst-class
classref-method
:::
::::

`Node<class_Node>`{.interpreted-text role="ref"}
**instantiate**(edit_state:
`GenEditState<enum_PackedScene_GenEditState>`{.interpreted-text
role="ref"} = 0)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_PackedScene_method_instantiate>`{.interpreted-text role="ref"}

Instantiates the scene\'s node hierarchy. Triggers child scene
instantiation(s). Triggers a
`Node.NOTIFICATION_SCENE_INSTANTIATED<class_Node_constant_NOTIFICATION_SCENE_INSTANTIATED>`{.interpreted-text
role="ref"} notification on the root node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PackedScene_method_pack}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**pack**(path: `Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_PackedScene_method_pack>`{.interpreted-text role="ref"}

Packs the `path` node, and all owned sub-nodes, into this
**PackedScene**. Any existing data will be cleared. See
`Node.owner<class_Node_property_owner>`{.interpreted-text role="ref"}.
