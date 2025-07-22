github_url
:   hide

# InputMap {#class_InputMap}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton that manages all
`InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

Manages all `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} which can be created/modified from the project settings menu
**Project \> Project Settings \> Input Map** or in code with
`add_action()<class_InputMap_method_add_action>`{.interpreted-text
role="ref"} and
`action_add_event()<class_InputMap_method_action_add_event>`{.interpreted-text
role="ref"}. See
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Using InputEvent:
  InputMap](../tutorials/inputs/inputevent.html#inputmap)

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

:::: {#class_InputMap_method_action_add_event}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**action_add_event**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"}, event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_action_add_event>`{.interpreted-text
role="ref"}

Adds an `InputEvent<class_InputEvent>`{.interpreted-text role="ref"} to
an action. This `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} will trigger the action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_action_erase_event}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**action_erase_event**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"}, event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_action_erase_event>`{.interpreted-text
role="ref"}

Removes an `InputEvent<class_InputEvent>`{.interpreted-text role="ref"}
from an action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_action_erase_events}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**action_erase_events**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_action_erase_events>`{.interpreted-text
role="ref"}

Removes all events from an action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_action_get_deadzone}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**action_get_deadzone**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_action_get_deadzone>`{.interpreted-text
role="ref"}

Returns a deadzone value for the action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_action_get_events}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}\] **action_get_events**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_action_get_events>`{.interpreted-text
role="ref"}

Returns an array of `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}s associated with a given action.

\*\*Note:\*\* When used in the editor (e.g. a tool script or
`EditorPlugin<class_EditorPlugin>`{.interpreted-text role="ref"}), this
method will return events for the editor action. If you want to access
your project\'s input binds from the editor, read the `input/*` settings
from `ProjectSettings<class_ProjectSettings>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_action_has_event}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**action_has_event**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"}, event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_action_has_event>`{.interpreted-text
role="ref"}

Returns `true` if the action has the given
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} associated
with it.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_action_set_deadzone}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**action_set_deadzone**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"}, deadzone:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_action_set_deadzone>`{.interpreted-text
role="ref"}

Sets a deadzone value for the action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_add_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_action**(action: `StringName<class_StringName>`{.interpreted-text
role="ref"}, deadzone: `float<class_float>`{.interpreted-text
role="ref"} = 0.2)
`🔗<class_InputMap_method_add_action>`{.interpreted-text role="ref"}

Adds an empty action to the **InputMap** with a configurable `deadzone`.

An `InputEvent<class_InputEvent>`{.interpreted-text role="ref"} can then
be added to this action with
`action_add_event()<class_InputMap_method_action_add_event>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_erase_action}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**erase_action**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_InputMap_method_erase_action>`{.interpreted-text role="ref"}

Removes an action from the **InputMap**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_event_is_action}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**event_is_action**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}, action:
`StringName<class_StringName>`{.interpreted-text role="ref"},
exact_match: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputMap_method_event_is_action>`{.interpreted-text
role="ref"}

Returns `true` if the given event is part of an existing action. This
method ignores keyboard modifiers if the given
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} is not
pressed (for proper release detection). See
`action_has_event()<class_InputMap_method_action_has_event>`{.interpreted-text
role="ref"} if you don\'t want this behavior.

If `exact_match` is `false`, it ignores additional input modifiers for
`InputEventKey<class_InputEventKey>`{.interpreted-text role="ref"} and
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} events, and the direction for
`InputEventJoypadMotion<class_InputEventJoypadMotion>`{.interpreted-text
role="ref"} events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_get_action_description}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**get_action_description**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_InputMap_method_get_action_description>`{.interpreted-text
role="ref"}

Returns the human-readable description of the given action.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_get_actions}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_actions**()
`🔗<class_InputMap_method_get_actions>`{.interpreted-text role="ref"}

Returns an array of all actions in the **InputMap**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_has_action}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_action**(action:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_InputMap_method_has_action>`{.interpreted-text
role="ref"}

Returns `true` if the **InputMap** has a registered action with the
given name.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputMap_method_load_from_project_settings}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**load_from_project_settings**()
`🔗<class_InputMap_method_load_from_project_settings>`{.interpreted-text
role="ref"}

Clears all `InputEventAction<class_InputEventAction>`{.interpreted-text
role="ref"} in the **InputMap** and load it anew from
`ProjectSettings<class_ProjectSettings>`{.interpreted-text role="ref"}.
