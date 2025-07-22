github_url
:   hide

# Thread {#class_Thread}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A unit of execution in a process.

::: rst-class
classref-introduction-group
:::

## Description

A unit of execution in a process. Can run methods on
`Object<class_Object>`{.interpreted-text role="ref"}s simultaneously.
The use of synchronization via `Mutex<class_Mutex>`{.interpreted-text
role="ref"} or `Semaphore<class_Semaphore>`{.interpreted-text
role="ref"} is advised if working with shared objects.

\*\*Warning:\*\*

To ensure proper cleanup without crashes or deadlocks, when a
**Thread**\'s reference count reaches zero and it is therefore
destroyed, the following conditions must be met:

- It must not have any `Mutex<class_Mutex>`{.interpreted-text
  role="ref"} objects locked.
- It must not be waiting on any
  `Semaphore<class_Semaphore>`{.interpreted-text role="ref"} objects.
- `wait_to_finish()<class_Thread_method_wait_to_finish>`{.interpreted-text
  role="ref"} should have been called on it.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using multiple threads <../tutorials/performance/using_multiple_threads>`{.interpreted-text
  role="doc"}
- `Thread-safe APIs <../tutorials/performance/thread_safe_apis>`{.interpreted-text
  role="doc"}
- [3D Voxel Demo](https://godotengine.org/asset-library/asset/2755)

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

:::: {#enum_Thread_Priority}
::: rst-class
classref-enumeration
:::
::::

enum **Priority**: `🔗<enum_Thread_Priority>`{.interpreted-text
role="ref"}

:::: {#class_Thread_constant_PRIORITY_LOW}
::: rst-class
classref-enumeration-constant
:::
::::

`Priority<enum_Thread_Priority>`{.interpreted-text role="ref"}
**PRIORITY_LOW** = `0`

A thread running with lower priority than normally.

:::: {#class_Thread_constant_PRIORITY_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Priority<enum_Thread_Priority>`{.interpreted-text role="ref"}
**PRIORITY_NORMAL** = `1`

A thread with a standard priority.

:::: {#class_Thread_constant_PRIORITY_HIGH}
::: rst-class
classref-enumeration-constant
:::
::::

`Priority<enum_Thread_Priority>`{.interpreted-text role="ref"}
**PRIORITY_HIGH** = `2`

A thread running with higher priority than normally.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Thread_method_get_id}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **get_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Thread_method_get_id>`{.interpreted-text
role="ref"}

Returns the current **Thread**\'s ID, uniquely identifying it among all
threads. If the **Thread** has not started running or if
`wait_to_finish()<class_Thread_method_wait_to_finish>`{.interpreted-text
role="ref"} has been called, this returns an empty string.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Thread_method_is_alive}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_alive**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Thread_method_is_alive>`{.interpreted-text
role="ref"}

Returns `true` if this **Thread** is currently running the provided
function. This is useful for determining if
`wait_to_finish()<class_Thread_method_wait_to_finish>`{.interpreted-text
role="ref"} can be called without blocking the calling thread.

To check if a **Thread** is joinable, use
`is_started()<class_Thread_method_is_started>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Thread_method_is_started}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_started**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Thread_method_is_started>`{.interpreted-text
role="ref"}

Returns `true` if this **Thread** has been started. Once started, this
will return `true` until it is joined using
`wait_to_finish()<class_Thread_method_wait_to_finish>`{.interpreted-text
role="ref"}. For checking if a **Thread** is still executing its task,
use `is_alive()<class_Thread_method_is_alive>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Thread_method_set_thread_safety_checks_enabled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_thread_safety_checks_enabled**(enabled:
`bool<class_bool>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Thread_method_set_thread_safety_checks_enabled>`{.interpreted-text
role="ref"}

Sets whether the thread safety checks the engine normally performs in
methods of certain classes (e.g., `Node<class_Node>`{.interpreted-text
role="ref"}) should happen **on the current thread**.

The default, for every thread, is that they are enabled (as if called
with `enabled` being `true`).

Those checks are conservative. That means that they will only succeed in
considering a call thread-safe (and therefore allow it to happen) if the
engine can guarantee such safety.

Because of that, there may be cases where the user may want to disable
them (`enabled` being `false`) to make certain operations allowed again.
By doing so, it becomes the user\'s responsibility to ensure thread
safety (e.g., by using `Mutex<class_Mutex>`{.interpreted-text
role="ref"}) for those objects that are otherwise protected by the
engine.

\*\*Note:\*\* This is an advanced usage of the engine. You are advised
to use it only if you know what you are doing and there is no safer way.

\*\*Note:\*\* This is useful for scripts running on either arbitrary
**Thread** objects or tasks submitted to the
`WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text
role="ref"}. It doesn\'t apply to code running during
`Node<class_Node>`{.interpreted-text role="ref"} group processing, where
the checks will be always performed.

\*\*Note:\*\* Even in the case of having disabled the checks in a
`WorkerThreadPool<class_WorkerThreadPool>`{.interpreted-text role="ref"}
task, there\'s no need to re-enable them at the end. The engine will do
so.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Thread_method_start}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**start**(callable: `Callable<class_Callable>`{.interpreted-text
role="ref"}, priority:
`Priority<enum_Thread_Priority>`{.interpreted-text role="ref"} = 1)
`🔗<class_Thread_method_start>`{.interpreted-text role="ref"}

Starts a new **Thread** that calls `callable`.

If the method takes some arguments, you can pass them using
`Callable.bind()<class_Callable_method_bind>`{.interpreted-text
role="ref"}.

The `priority` of the **Thread** can be changed by passing a value from
the `Priority<enum_Thread_Priority>`{.interpreted-text role="ref"} enum.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} on success, or
`@GlobalScope.ERR_CANT_CREATE<class_@GlobalScope_constant_ERR_CANT_CREATE>`{.interpreted-text
role="ref"} on failure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Thread_method_wait_to_finish}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**wait_to_finish**()
`🔗<class_Thread_method_wait_to_finish>`{.interpreted-text role="ref"}

Joins the **Thread** and waits for it to finish. Returns the output of
the `Callable<class_Callable>`{.interpreted-text role="ref"} passed to
`start()<class_Thread_method_start>`{.interpreted-text role="ref"}.

Should either be used when you want to retrieve the value returned from
the method called by the **Thread** or before freeing the instance that
contains the **Thread**.

To determine if this can be called without blocking the calling thread,
check if `is_alive()<class_Thread_method_is_alive>`{.interpreted-text
role="ref"} is `false`.
