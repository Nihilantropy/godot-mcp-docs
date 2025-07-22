github_url
:   hide

# InputEventAction {#class_InputEventAction}

**Inherits:** `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"} **\<** `Resource<class_Resource>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

An input event type for actions.

::: rst-class
classref-introduction-group
:::

## Description

Contains a generic action which can be targeted from several types of
inputs. Actions and their events can be set in the **Input Map** tab in
**Project \> Project Settings**, or with the
`InputMap<class_InputMap>`{.interpreted-text role="ref"} class.

\*\*Note:\*\* Unlike the other
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} subclasses
which map to unique physical events, this virtual one is not emitted by
the engine. This class is useful to emit actions manually with
`Input.parse_input_event()<class_Input_method_parse_input_event>`{.interpreted-text
role="ref"}, which are then received in
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"}. To check if a physical event matches an action from the
Input Map, use
`InputEvent.is_action()<class_InputEvent_method_is_action>`{.interpreted-text
role="ref"} and
`InputEvent.is_action_pressed()<class_InputEvent_method_is_action_pressed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Using InputEvent:
  Actions](../tutorials/inputs/inputevent.html#actions)
- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_InputEventAction_property_action}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"} **action**
= `&""` `🔗<class_InputEventAction_property_action>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_action**(value: `StringName<class_StringName>`{.interpreted-text
  role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_action**()

The action\'s name. This is usually the name of an existing action in
the `InputMap<class_InputMap>`{.interpreted-text role="ref"} which you
want this custom event to match.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventAction_property_event_index}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **event_index** = `-1`
`🔗<class_InputEventAction_property_event_index>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_event_index**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_event_index**()

The real event index in action this event corresponds to (from events
defined for this action in the
`InputMap<class_InputMap>`{.interpreted-text role="ref"}). If `-1`, a
unique ID will be used and actions pressed with this ID will need to be
released with another **InputEventAction**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventAction_property_pressed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pressed** = `false`
`🔗<class_InputEventAction_property_pressed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pressed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_pressed**()

If `true`, the action\'s state is pressed. If `false`, the action\'s
state is released.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_InputEventAction_property_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **strength** = `1.0`
`🔗<class_InputEventAction_property_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_strength**()

The action\'s strength between 0 and 1. This value is considered as
equal to 0 if pressed is `false`. The event strength allows faking
analog joypad motion events, by specifying how strongly the joypad axis
is bent or pressed.
