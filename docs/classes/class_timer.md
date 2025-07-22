github_url
:   hide

# Timer {#class_Timer}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A countdown timer.

::: rst-class
classref-introduction-group
:::

## Description

The **Timer** node is a countdown timer and is the simplest way to
handle time-based logic in the engine. When a timer reaches the end of
its `wait_time<class_Timer_property_wait_time>`{.interpreted-text
role="ref"}, it will emit the
`timeout<class_Timer_signal_timeout>`{.interpreted-text role="ref"}
signal.

After a timer enters the scene tree, it can be manually started with
`start()<class_Timer_method_start>`{.interpreted-text role="ref"}. A
timer node is also started automatically if
`autostart<class_Timer_property_autostart>`{.interpreted-text
role="ref"} is `true`.

Without requiring much code, a timer node can be added and configured in
the editor. The `timeout<class_Timer_signal_timeout>`{.interpreted-text
role="ref"} signal it emits can also be connected through the Node dock
in the editor:

    func _on_timer_timeout():
        print("Time to attack!")

\*\*Note:\*\* To create a one-shot timer without instantiating a node,
use
`SceneTree.create_timer()<class_SceneTree_method_create_timer>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Timers are affected by
`Engine.time_scale<class_Engine_property_time_scale>`{.interpreted-text
role="ref"} unless
`ignore_time_scale<class_Timer_property_ignore_time_scale>`{.interpreted-text
role="ref"} is `true`. The higher the time scale, the sooner timers will
end. How often a timer processes may depend on the framerate or
`Engine.physics_ticks_per_second<class_Engine_property_physics_ticks_per_second>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [2D Dodge The Creeps
  Demo](https://godotengine.org/asset-library/asset/2712)

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

:::: {#class_Timer_signal_timeout}
::: rst-class
classref-signal
:::
::::

**timeout**() `🔗<class_Timer_signal_timeout>`{.interpreted-text
role="ref"}

Emitted when the timer reaches the end.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Timer_TimerProcessCallback}
::: rst-class
classref-enumeration
:::
::::

enum **TimerProcessCallback**:
`🔗<enum_Timer_TimerProcessCallback>`{.interpreted-text role="ref"}

:::: {#class_Timer_constant_TIMER_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`TimerProcessCallback<enum_Timer_TimerProcessCallback>`{.interpreted-text
role="ref"} **TIMER_PROCESS_PHYSICS** = `0`

Update the timer every physics process frame (see
`Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_Timer_constant_TIMER_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`TimerProcessCallback<enum_Timer_TimerProcessCallback>`{.interpreted-text
role="ref"} **TIMER_PROCESS_IDLE** = `1`

Update the timer every process (rendered) frame (see
`Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Timer_property_autostart}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autostart** = `false`
`🔗<class_Timer_property_autostart>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autostart**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_autostart**()

If `true`, the timer will start immediately when it enters the scene
tree.

\*\*Note:\*\* After the timer enters the tree, this property is
automatically set to `false`.

\*\*Note:\*\* This property does nothing when the timer is running in
the editor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_property_ignore_time_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **ignore_time_scale** =
`false` `🔗<class_Timer_property_ignore_time_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_ignore_time_scale**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_ignoring_time_scale**()

If `true`, the timer will ignore
`Engine.time_scale<class_Engine_property_time_scale>`{.interpreted-text
role="ref"} and update with the real, elapsed time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_property_one_shot}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **one_shot** = `false`
`🔗<class_Timer_property_one_shot>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_one_shot**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_one_shot**()

If `true`, the timer will stop after reaching the end. Otherwise, as by
default, the timer will automatically restart.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_property_paused}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **paused**
`🔗<class_Timer_property_paused>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_paused**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_paused**()

If `true`, the timer is paused. A paused timer does not process until
this property is set back to `false`, even when
`start()<class_Timer_method_start>`{.interpreted-text role="ref"} is
called. See also `stop()<class_Timer_method_stop>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_property_process_callback}
::: rst-class
classref-property
:::
::::

`TimerProcessCallback<enum_Timer_TimerProcessCallback>`{.interpreted-text
role="ref"} **process_callback** = `1`
`🔗<class_Timer_property_process_callback>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_timer_process_callback**(value:
  `TimerProcessCallback<enum_Timer_TimerProcessCallback>`{.interpreted-text
  role="ref"})
- `TimerProcessCallback<enum_Timer_TimerProcessCallback>`{.interpreted-text
  role="ref"} **get_timer_process_callback**()

Specifies when the timer is updated during the main loop.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_property_time_left}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **time_left**
`🔗<class_Timer_property_time_left>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `float<class_float>`{.interpreted-text role="ref"} **get_time_left**()

The timer\'s remaining time in seconds. This is always `0` if the timer
is stopped.

\*\*Note:\*\* This property is read-only and cannot be modified. It is
based on `wait_time<class_Timer_property_wait_time>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_property_wait_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **wait_time** = `1.0`
`🔗<class_Timer_property_wait_time>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wait_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_wait_time**()

The time required for the timer to end, in seconds. This property can
also be set every time
`start()<class_Timer_method_start>`{.interpreted-text role="ref"} is
called.

\*\*Note:\*\* Timers can only process once per physics or process frame
(depending on the
`process_callback<class_Timer_property_process_callback>`{.interpreted-text
role="ref"}). An unstable framerate may cause the timer to end
inconsistently, which is especially noticeable if the wait time is lower
than roughly `0.05` seconds. For very short timers, it is recommended to
write your own code instead of using a **Timer** node. Timers are also
affected by
`Engine.time_scale<class_Engine_property_time_scale>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Timer_method_is_stopped}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_stopped**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Timer_method_is_stopped>`{.interpreted-text
role="ref"}

Returns `true` if the timer is stopped or has not started.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_method_start}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**start**(time_sec: `float<class_float>`{.interpreted-text role="ref"} =
-1) `🔗<class_Timer_method_start>`{.interpreted-text role="ref"}

Starts the timer, or resets the timer if it was started already. Fails
if the timer is not inside the scene tree. If `time_sec` is greater than
`0`, this value is used for the
`wait_time<class_Timer_property_wait_time>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This method does not resume a paused timer. See
`paused<class_Timer_property_paused>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Timer_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_Timer_method_stop>`{.interpreted-text role="ref"}

Stops the timer. See also
`paused<class_Timer_property_paused>`{.interpreted-text role="ref"}.
Unlike `start()<class_Timer_method_start>`{.interpreted-text
role="ref"}, this can safely be called if the timer is not inside the
scene tree.

\*\*Note:\*\* Calling
`stop()<class_Timer_method_stop>`{.interpreted-text role="ref"} does not
emit the `timeout<class_Timer_signal_timeout>`{.interpreted-text
role="ref"} signal, as the timer is not considered to have timed out. If
this is desired, use `$Timer.timeout.emit()` after calling
`stop()<class_Timer_method_stop>`{.interpreted-text role="ref"} to
manually emit the signal.
