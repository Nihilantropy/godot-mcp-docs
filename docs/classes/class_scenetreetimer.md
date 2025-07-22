github_url
:   hide

# SceneTreeTimer {#class_SceneTreeTimer}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

One-shot timer.

::: rst-class
classref-introduction-group
:::

## Description

A one-shot timer managed by the scene tree, which emits
`timeout<class_SceneTreeTimer_signal_timeout>`{.interpreted-text
role="ref"} on completion. See also
`SceneTree.create_timer()<class_SceneTree_method_create_timer>`{.interpreted-text
role="ref"}.

As opposed to `Timer<class_Timer>`{.interpreted-text role="ref"}, it
does not require the instantiation of a node. Commonly used to create a
one-shot delay timer as in the following example:

::::: tabs
::: code-tab
gdscript

func some_function():

:   print(\"Timer started.\") await get_tree().create_timer(1.0).timeout
    print(\"Timer ended.\")
:::

::: code-tab
csharp

public async Task SomeFunction() { GD.Print(\"Timer started.\"); await
ToSignal(GetTree().CreateTimer(1.0f),
SceneTreeTimer.SignalName.Timeout); GD.Print(\"Timer ended.\"); }
:::
:::::

The timer will be dereferenced after its time elapses. To preserve the
timer, you can keep a reference to it. See
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"}.

\*\*Note:\*\* The timer is processed after all of the nodes in the
current frame, i.e. node\'s
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} method would be called before the timer (or
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} if `process_in_physics` in
`SceneTree.create_timer()<class_SceneTree_method_create_timer>`{.interpreted-text
role="ref"} has been set to `true`).

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

## Signals

:::: {#class_SceneTreeTimer_signal_timeout}
::: rst-class
classref-signal
:::
::::

**timeout**()
`🔗<class_SceneTreeTimer_signal_timeout>`{.interpreted-text role="ref"}

Emitted when the timer reaches 0.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_SceneTreeTimer_property_time_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **time_left**
`🔗<class_SceneTreeTimer_property_time_left>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_time_left**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_time_left**()

The time remaining (in seconds).
