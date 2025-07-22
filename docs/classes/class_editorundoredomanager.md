github_url
:   hide

# EditorUndoRedoManager {#class_EditorUndoRedoManager}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

Manages undo history of scenes opened in the editor.

::: rst-class
classref-introduction-group
:::

## Description

**EditorUndoRedoManager** is a manager for
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"} objects
associated with edited scenes. Each scene has its own undo history and
**EditorUndoRedoManager** ensures that each action performed in the
editor gets associated with a proper scene. For actions not related to
scenes (`ProjectSettings<class_ProjectSettings>`{.interpreted-text
role="ref"} edits, external resources, etc.), a separate global history
is used.

The usage is mostly the same as
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"}. You create and
commit actions and the manager automatically decides under-the-hood what
scenes it belongs to. The scene is deduced based on the first operation
in an action, using the object from the operation. The rules are as
follows:

- If the object is a `Node<class_Node>`{.interpreted-text role="ref"},
  use the currently edited scene;
- If the object is a built-in resource, use the scene from its path;
- If the object is external resource or anything else, use global
  history.

This guessing can sometimes yield false results, so you can provide a
custom context object when creating an action.

\*\*EditorUndoRedoManager\*\* is intended to be used by Godot editor
plugins. You can obtain it using
`EditorPlugin.get_undo_redo()<class_EditorPlugin_method_get_undo_redo>`{.interpreted-text
role="ref"}. For non-editor uses or plugins that don\'t need to
integrate with the editor\'s undo history, use
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"} instead.

The manager\'s API is mostly the same as in
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"}, so you can
refer to its documentation for more examples. The main difference is
that **EditorUndoRedoManager** uses object + method name for actions,
instead of `Callable<class_Callable>`{.interpreted-text role="ref"}.

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

:::: {#class_EditorUndoRedoManager_signal_history_changed}
::: rst-class
classref-signal
:::
::::

**history_changed**()
`🔗<class_EditorUndoRedoManager_signal_history_changed>`{.interpreted-text
role="ref"}

Emitted when the list of actions in any history has changed, either when
an action is committed or a history is cleared.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_signal_version_changed}
::: rst-class
classref-signal
:::
::::

**version_changed**()
`🔗<class_EditorUndoRedoManager_signal_version_changed>`{.interpreted-text
role="ref"}

Emitted when the version of any history has changed as a result of undo
or redo call.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_EditorUndoRedoManager_SpecialHistory}
::: rst-class
classref-enumeration
:::
::::

enum **SpecialHistory**:
`🔗<enum_EditorUndoRedoManager_SpecialHistory>`{.interpreted-text
role="ref"}

:::: {#class_EditorUndoRedoManager_constant_GLOBAL_HISTORY}
::: rst-class
classref-enumeration-constant
:::
::::

`SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>`{.interpreted-text
role="ref"} **GLOBAL_HISTORY** = `0`

Global history not associated with any scene, but with external
resources etc.

:::: {#class_EditorUndoRedoManager_constant_REMOTE_HISTORY}
::: rst-class
classref-enumeration-constant
:::
::::

`SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>`{.interpreted-text
role="ref"} **REMOTE_HISTORY** = `-9`

History associated with remote inspector. Used when live editing a
running project.

:::: {#class_EditorUndoRedoManager_constant_INVALID_HISTORY}
::: rst-class
classref-enumeration-constant
:::
::::

`SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>`{.interpreted-text
role="ref"} **INVALID_HISTORY** = `-99`

Invalid \"null\" history. It\'s a special value, not associated with any
object.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_EditorUndoRedoManager_method_add_do_method}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_do_method**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, method: `StringName<class_StringName>`{.interpreted-text
role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorUndoRedoManager_method_add_do_method>`{.interpreted-text
role="ref"}

Register a method that will be called when the action is committed (i.e.
the \"do\" action).

If this is the first operation, the `object` will be used to deduce
target undo history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_add_do_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_do_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, property: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_EditorUndoRedoManager_method_add_do_property>`{.interpreted-text
role="ref"}

Register a property value change for \"do\".

If this is the first operation, the `object` will be used to deduce
target undo history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_add_do_reference}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_do_reference**(object: `Object<class_Object>`{.interpreted-text
role="ref"})
`🔗<class_EditorUndoRedoManager_method_add_do_reference>`{.interpreted-text
role="ref"}

Register a reference for \"do\" that will be erased if the \"do\"
history is lost. This is useful mostly for new nodes created for the
\"do\" call. Do not use for resources.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_add_undo_method}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_undo_method**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, method: `StringName<class_StringName>`{.interpreted-text
role="ref"}, \...)
`vararg (This method accepts any number of arguments after the ones described here.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorUndoRedoManager_method_add_undo_method>`{.interpreted-text
role="ref"}

Register a method that will be called when the action is undone (i.e.
the \"undo\" action).

If this is the first operation, the `object` will be used to deduce
target undo history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_add_undo_property}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_undo_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, property: `StringName<class_StringName>`{.interpreted-text
role="ref"}, value: `Variant<class_Variant>`{.interpreted-text
role="ref"})
`🔗<class_EditorUndoRedoManager_method_add_undo_property>`{.interpreted-text
role="ref"}

Register a property value change for \"undo\".

If this is the first operation, the `object` will be used to deduce
target undo history.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_add_undo_reference}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_undo_reference**(object: `Object<class_Object>`{.interpreted-text
role="ref"})
`🔗<class_EditorUndoRedoManager_method_add_undo_reference>`{.interpreted-text
role="ref"}

Register a reference for \"undo\" that will be erased if the \"undo\"
history is lost. This is useful mostly for nodes removed with the \"do\"
call (not the \"undo\" call!).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_clear_history}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_history**(id: `int<class_int>`{.interpreted-text role="ref"} =
-99, increase_version: `bool<class_bool>`{.interpreted-text role="ref"}
= true)
`🔗<class_EditorUndoRedoManager_method_clear_history>`{.interpreted-text
role="ref"}

Clears the given undo history. You can clear history for a specific
scene, global history, or for all scenes at once if `id` is
`INVALID_HISTORY<class_EditorUndoRedoManager_constant_INVALID_HISTORY>`{.interpreted-text
role="ref"}.

If `increase_version` is `true`, the undo history version will be
increased, marking it as unsaved. Useful for operations that modify the
scene, but don\'t support undo.

    var scene_root = EditorInterface.get_edited_scene_root()
    var undo_redo = EditorInterface.get_editor_undo_redo()
    undo_redo.clear_history(undo_redo.get_object_history_id(scene_root))

\*\*Note:\*\* If you want to mark an edited scene as unsaved without
clearing its history, use
`EditorInterface.mark_scene_as_unsaved()<class_EditorInterface_method_mark_scene_as_unsaved>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_commit_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**commit_action**(execute: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_EditorUndoRedoManager_method_commit_action>`{.interpreted-text
role="ref"}

Commits the action. If `execute` is `true` (default), all \"do\"
methods/properties are called/set when this function is called.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_create_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**create_action**(name: `String<class_String>`{.interpreted-text
role="ref"}, merge_mode:
`MergeMode<enum_UndoRedo_MergeMode>`{.interpreted-text role="ref"} = 0,
custom_context: `Object<class_Object>`{.interpreted-text role="ref"} =
null, backward_undo_ops: `bool<class_bool>`{.interpreted-text
role="ref"} = false, mark_unsaved: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_EditorUndoRedoManager_method_create_action>`{.interpreted-text
role="ref"}

Create a new action. After this is called, do all your calls to
`add_do_method()<class_EditorUndoRedoManager_method_add_do_method>`{.interpreted-text
role="ref"},
`add_undo_method()<class_EditorUndoRedoManager_method_add_undo_method>`{.interpreted-text
role="ref"},
`add_do_property()<class_EditorUndoRedoManager_method_add_do_property>`{.interpreted-text
role="ref"}, and
`add_undo_property()<class_EditorUndoRedoManager_method_add_undo_property>`{.interpreted-text
role="ref"}, then commit the action with
`commit_action()<class_EditorUndoRedoManager_method_commit_action>`{.interpreted-text
role="ref"}.

The way actions are merged is dictated by the `merge_mode` argument.

If `custom_context` object is provided, it will be used for deducing
target history (instead of using the first operation).

The way undo operation are ordered in actions is dictated by
`backward_undo_ops`. When `backward_undo_ops` is `false` undo option are
ordered in the same order they were added. Which means the first
operation to be added will be the first to be undone.

If `mark_unsaved` is `false`, the action will not mark the history as
unsaved. This is useful for example for actions that change a selection,
or a setting that will be saved automatically. Otherwise, this should be
left to `true` if the action requires saving by the user or if it can
cause data loss when left unsaved.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_force_fixed_history}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**force_fixed_history**()
`🔗<class_EditorUndoRedoManager_method_force_fixed_history>`{.interpreted-text
role="ref"}

Forces the next operation (e.g.
`add_do_method()<class_EditorUndoRedoManager_method_add_do_method>`{.interpreted-text
role="ref"}) to use the action\'s history rather than guessing it from
the object. This is sometimes needed when a history can\'t be correctly
determined, like for a nested resource that doesn\'t have a path yet.

This method should only be used when absolutely necessary, otherwise it
might cause invalid history state. For most of complex cases, the
`custom_context` parameter of
`create_action()<class_EditorUndoRedoManager_method_create_action>`{.interpreted-text
role="ref"} is sufficient.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_get_history_undo_redo}
::: rst-class
classref-method
:::
::::

`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"}
**get_history_undo_redo**(id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorUndoRedoManager_method_get_history_undo_redo>`{.interpreted-text
role="ref"}

Returns the `UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"}
object associated with the given history `id`.

`id` above `0` are mapped to the opened scene tabs (but it doesn\'t
match their order). `id` of `0` or lower have special meaning (see
`SpecialHistory<enum_EditorUndoRedoManager_SpecialHistory>`{.interpreted-text
role="ref"}).

Best used with
`get_object_history_id()<class_EditorUndoRedoManager_method_get_object_history_id>`{.interpreted-text
role="ref"}. This method is only provided in case you need some more
advanced methods of `UndoRedo<class_UndoRedo>`{.interpreted-text
role="ref"} (but keep in mind that directly operating on the
`UndoRedo<class_UndoRedo>`{.interpreted-text role="ref"} object might
affect editor\'s stability).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_get_object_history_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_object_history_id**(object:
`Object<class_Object>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorUndoRedoManager_method_get_object_history_id>`{.interpreted-text
role="ref"}

Returns the history ID deduced from the given `object`. It can be used
with
`get_history_undo_redo()<class_EditorUndoRedoManager_method_get_history_undo_redo>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EditorUndoRedoManager_method_is_committing_action}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_committing_action**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_EditorUndoRedoManager_method_is_committing_action>`{.interpreted-text
role="ref"}

Returns `true` if the **EditorUndoRedoManager** is currently committing
the action, i.e. running its \"do\" method or property change (see
`commit_action()<class_EditorUndoRedoManager_method_commit_action>`{.interpreted-text
role="ref"}).
