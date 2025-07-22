github_url
:   hide

# UndoRedo {#class_UndoRedo}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Provides a high-level interface for implementing undo and redo
operations.

::: rst-class
classref-introduction-group
:::

## Description

UndoRedo works by registering methods and property changes inside
\"actions\". You can create an action, then provide ways to do and undo
this action using function calls and property changes, then commit the
action.

When an action is committed, all of the `do_*` methods will run. If the
`undo()<class_UndoRedo_method_undo>`{.interpreted-text role="ref"}
method is used, the `undo_*` methods will run. If the
`redo()<class_UndoRedo_method_redo>`{.interpreted-text role="ref"}
method is used, once again, all of the `do_*` methods will run.

Here\'s an example on how to add an action:

::::: tabs
::: code-tab
gdscript

var undo_redo = UndoRedo.new()

func do_something():

:   pass \# Put your code here.

func undo_something():

:   pass \# Put here the code that reverts what\'s done by
    \"do_something()\".

func [on_my_button_pressed]{#on_my_button_pressed}():

:   var node = get_node(\"MyNode2D\") undo_redo.create_action(\"Move the
    node\") undo_redo.add_do_method(do_something)
    undo_redo.add_undo_method(undo_something)
    undo_redo.add_do_property(node, \"position\", Vector2(100, 100))
    undo_redo.add_undo_property(node, \"position\", node.position)
    undo_redo.commit_action()
:::

::: code-tab
csharp

private UndoRedo [undoRedo]{#undoredo};

public override void [Ready]{#ready}() { [undoRedo]{#undoredo} = new
UndoRedo(); }

public void DoSomething() { // Put your code here. }

public void UndoSomething() { // Put here the code that reverts what\'s
done by \"DoSomething()\". }

private void OnMyButtonPressed() { var node =
GetNode\<Node2D\>(\"MyNode2D\");
[undoRedo.CreateAction]{#undoredo.createaction}(\"Move the node\");
[undoRedo.AddDoMethod]{#undoredo.adddomethod}(new Callable(this,
MethodName.DoSomething));
[undoRedo.AddUndoMethod]{#undoredo.addundomethod}(new Callable(this,
MethodName.UndoSomething));
[undoRedo.AddDoProperty]{#undoredo.adddoproperty}(node, \"position\",
new Vector2(100, 100));
[undoRedo.AddUndoProperty]{#undoredo.addundoproperty}(node,
\"position\", node.Position);
[undoRedo.CommitAction]{#undoredo.commitaction}(); }
:::
:::::

Before calling any of the `add_(un)do_*` methods, you need to first call
`create_action()<class_UndoRedo_method_create_action>`{.interpreted-text
role="ref"}. Afterwards you need to call
`commit_action()<class_UndoRedo_method_commit_action>`{.interpreted-text
role="ref"}.

If you don\'t need to register a method, you can leave
`add_do_method()<class_UndoRedo_method_add_do_method>`{.interpreted-text
role="ref"} and
`add_undo_method()<class_UndoRedo_method_add_undo_method>`{.interpreted-text
role="ref"} out; the same goes for properties. You can also register
more than one method/property.

If you are making an
`EditorPlugin<class_EditorPlugin>`{.interpreted-text role="ref"} and
want to integrate into the editor\'s undo history, use
`EditorUndoRedoManager<class_EditorUndoRedoManager>`{.interpreted-text
role="ref"} instead.

If you are registering multiple properties/method which depend on one
another, be aware that by default undo operation are called in the same
order they have been added. Therefore instead of grouping do operation
with their undo operations it is better to group do on one side and undo
on the other as shown below.

::::: tabs
::: code-tab
gdscript

undo_redo.create_action(\"Add object\")

\# DO undo_redo.add_do_method([create_object]{#create_object})
undo_redo.add_do_method([add_object_to_singleton]{#add_object_to_singleton})

\# UNDO
undo_redo.add_undo_method([remove_object_from_singleton]{#remove_object_from_singleton})
undo_redo.add_undo_method([destroy_that_object]{#destroy_that_object})

undo_redo.commit_action()
:::

::: code-tab
csharp

[undo_redo.CreateAction]{#undo_redo.createaction}(\"Add object\");

// DO [undo_redo.AddDoMethod]{#undo_redo.adddomethod}(new Callable(this,
MethodName.CreateObject));
[undo_redo.AddDoMethod]{#undo_redo.adddomethod}(new Callable(this,
MethodName.AddObjectToSingleton));

// UNDO [undo_redo.AddUndoMethod]{#undo_redo.addundomethod}(new
Callable(this, MethodName.RemoveObjectFromSingleton));
[undo_redo.AddUndoMethod]{#undo_redo.addundomethod}(new Callable(this,
MethodName.DestroyThatObject));

[undo_redo.CommitAction]{#undo_redo.commitaction}();
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

## Signals

:::: {#class_UndoRedo_signal_version_changed}
::: rst-class
classref-signal
:::
::::

**version_changed**()
`🔗<class_UndoRedo_signal_version_changed>`{.interpreted-text
role="ref"}

Called when `undo()<class_UndoRedo_method_undo>`{.interpreted-text
role="ref"} or `redo()<class_UndoRedo_method_redo>`{.interpreted-text
role="ref"} was called.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_UndoRedo_MergeMode}
::: rst-class
classref-enumeration
:::
::::

enum **MergeMode**: `🔗<enum_UndoRedo_MergeMode>`{.interpreted-text
role="ref"}

:::: {#class_UndoRedo_constant_MERGE_DISABLE}
::: rst-class
classref-enumeration-constant
:::
::::

`MergeMode<enum_UndoRedo_MergeMode>`{.interpreted-text role="ref"}
**MERGE_DISABLE** = `0`

Makes \"do\"/\"undo\" operations stay in separate actions.

:::: {#class_UndoRedo_constant_MERGE_ENDS}
::: rst-class
classref-enumeration-constant
:::
::::

`MergeMode<enum_UndoRedo_MergeMode>`{.interpreted-text role="ref"}
**MERGE_ENDS** = `1`

Merges this action with the previous one if they have the same name.
Keeps only the first action\'s \"undo\" operations and the last
action\'s \"do\" operations. Useful for sequential changes to a single
value.

:::: {#class_UndoRedo_constant_MERGE_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`MergeMode<enum_UndoRedo_MergeMode>`{.interpreted-text role="ref"}
**MERGE_ALL** = `2`

Merges this action with the previous one if they have the same name.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_UndoRedo_property_max_steps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **max_steps** = `0`
`🔗<class_UndoRedo_property_max_steps>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_steps**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_max_steps**()

The maximum number of steps that can be stored in the undo/redo history.
If the number of stored steps exceeds this limit, older steps are
removed from history and can no longer be reached by calling
`undo()<class_UndoRedo_method_undo>`{.interpreted-text role="ref"}. A
value of `0` or lower means no limit.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_UndoRedo_method_add_do_method}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_do_method**(callable: `Callable<class_Callable>`{.interpreted-text
role="ref"}) `🔗<class_UndoRedo_method_add_do_method>`{.interpreted-text
role="ref"}

Register a `Callable<class_Callable>`{.interpreted-text role="ref"} that
will be called when the action is committed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_add_do_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_do_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, property: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_UndoRedo_method_add_do_property>`{.interpreted-text
role="ref"}

Register a `property` that would change its value to `value` when the
action is committed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_add_do_reference}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_do_reference**(object: `Object<class_Object>`{.interpreted-text
role="ref"})
`🔗<class_UndoRedo_method_add_do_reference>`{.interpreted-text
role="ref"}

Register a reference to an object that will be erased if the \"do\"
history is deleted. This is useful for objects added by the \"do\"
action and removed by the \"undo\" action.

When the \"do\" history is deleted, if the object is a
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"}, it will be
unreferenced. Otherwise, it will be freed. Do not use for resources.

    var node = Node2D.new()
    undo_redo.create_action("Add node")
    undo_redo.add_do_method(add_child.bind(node))
    undo_redo.add_do_reference(node)
    undo_redo.add_undo_method(remove_child.bind(node))
    undo_redo.commit_action()

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_add_undo_method}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_undo_method**(callable:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_UndoRedo_method_add_undo_method>`{.interpreted-text
role="ref"}

Register a `Callable<class_Callable>`{.interpreted-text role="ref"} that
will be called when the action is undone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_add_undo_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_undo_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, property: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_UndoRedo_method_add_undo_property>`{.interpreted-text
role="ref"}

Register a `property` that would change its value to `value` when the
action is undone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_add_undo_reference}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_undo_reference**(object: `Object<class_Object>`{.interpreted-text
role="ref"})
`🔗<class_UndoRedo_method_add_undo_reference>`{.interpreted-text
role="ref"}

Register a reference to an object that will be erased if the \"undo\"
history is deleted. This is useful for objects added by the \"undo\"
action and removed by the \"do\" action.

When the \"undo\" history is deleted, if the object is a
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"}, it will be
unreferenced. Otherwise, it will be freed. Do not use for resources.

    var node = $Node2D
    undo_redo.create_action("Remove node")
    undo_redo.add_do_method(remove_child.bind(node))
    undo_redo.add_undo_method(add_child.bind(node))
    undo_redo.add_undo_reference(node)
    undo_redo.commit_action()

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_clear_history}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_history**(increase_version: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_UndoRedo_method_clear_history>`{.interpreted-text role="ref"}

Clear the undo/redo history and associated references.

Passing `false` to `increase_version` will prevent the version number
from increasing when the history is cleared.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_commit_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**commit_action**(execute: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_UndoRedo_method_commit_action>`{.interpreted-text role="ref"}

Commit the action. If `execute` is `true` (which it is by default), all
\"do\" methods/properties are called/set when this function is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_create_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_action**(name: `String<class_String>`{.interpreted-text
role="ref"}, merge_mode:
`MergeMode<enum_UndoRedo_MergeMode>`{.interpreted-text role="ref"} = 0,
backward_undo_ops: `bool<class_bool>`{.interpreted-text role="ref"} =
false) `🔗<class_UndoRedo_method_create_action>`{.interpreted-text
role="ref"}

Create a new action. After this is called, do all your calls to
`add_do_method()<class_UndoRedo_method_add_do_method>`{.interpreted-text
role="ref"},
`add_undo_method()<class_UndoRedo_method_add_undo_method>`{.interpreted-text
role="ref"},
`add_do_property()<class_UndoRedo_method_add_do_property>`{.interpreted-text
role="ref"}, and
`add_undo_property()<class_UndoRedo_method_add_undo_property>`{.interpreted-text
role="ref"}, then commit the action with
`commit_action()<class_UndoRedo_method_commit_action>`{.interpreted-text
role="ref"}.

The way actions are merged is dictated by `merge_mode`.

The way undo operation are ordered in actions is dictated by
`backward_undo_ops`. When `backward_undo_ops` is `false` undo option are
ordered in the same order they were added. Which means the first
operation to be added will be the first to be undone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_end_force_keep_in_merge_ends}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**end_force_keep_in_merge_ends**()
`🔗<class_UndoRedo_method_end_force_keep_in_merge_ends>`{.interpreted-text
role="ref"}

Stops marking operations as to be processed even if the action gets
merged with another in the
`MERGE_ENDS<class_UndoRedo_constant_MERGE_ENDS>`{.interpreted-text
role="ref"} mode. See
`start_force_keep_in_merge_ends()<class_UndoRedo_method_start_force_keep_in_merge_ends>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_get_action_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_action_name**(id: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_UndoRedo_method_get_action_name>`{.interpreted-text
role="ref"}

Gets the action name from its index.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_get_current_action}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_current_action**()
`🔗<class_UndoRedo_method_get_current_action>`{.interpreted-text
role="ref"}

Gets the index of the current action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_get_current_action_name}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_current_action_name**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UndoRedo_method_get_current_action_name>`{.interpreted-text
role="ref"}

Gets the name of the current action, equivalent to
`get_action_name(get_current_action())`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_get_history_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_history_count**()
`🔗<class_UndoRedo_method_get_history_count>`{.interpreted-text
role="ref"}

Returns how many elements are in the history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_get_version}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_version**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_UndoRedo_method_get_version>`{.interpreted-text
role="ref"}

Gets the version. Every time a new action is committed, the
**UndoRedo**\'s version number is increased automatically.

This is useful mostly to check if something changed from a saved
version.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_has_redo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_redo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_UndoRedo_method_has_redo>`{.interpreted-text
role="ref"}

Returns `true` if a \"redo\" action is available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_has_undo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_undo**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_UndoRedo_method_has_undo>`{.interpreted-text
role="ref"}

Returns `true` if an \"undo\" action is available.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_is_committing_action}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_committing_action**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_UndoRedo_method_is_committing_action>`{.interpreted-text
role="ref"}

Returns `true` if the **UndoRedo** is currently committing the action,
i.e. running its \"do\" method or property change (see
`commit_action()<class_UndoRedo_method_commit_action>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_redo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **redo**()
`🔗<class_UndoRedo_method_redo>`{.interpreted-text role="ref"}

Redo the last action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_start_force_keep_in_merge_ends}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start_force_keep_in_merge_ends**()
`🔗<class_UndoRedo_method_start_force_keep_in_merge_ends>`{.interpreted-text
role="ref"}

Marks the next \"do\" and \"undo\" operations to be processed even if
the action gets merged with another in the
`MERGE_ENDS<class_UndoRedo_constant_MERGE_ENDS>`{.interpreted-text
role="ref"} mode. Return to normal operation using
`end_force_keep_in_merge_ends()<class_UndoRedo_method_end_force_keep_in_merge_ends>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_UndoRedo_method_undo}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **undo**()
`🔗<class_UndoRedo_method_undo>`{.interpreted-text role="ref"}

Undo the last action.
