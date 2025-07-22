github_url
:   hide

# Mutex {#class_Mutex}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A binary `Semaphore<class_Semaphore>`{.interpreted-text role="ref"} for
synchronization of multiple `Thread<class_Thread>`{.interpreted-text
role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

A synchronization mutex (mutual exclusion). This is used to synchronize
multiple `Thread<class_Thread>`{.interpreted-text role="ref"}s, and is
equivalent to a binary `Semaphore<class_Semaphore>`{.interpreted-text
role="ref"}. It guarantees that only one thread can access a critical
section at a time.

This is a reentrant mutex, meaning that it can be locked multiple times
by one thread, provided it also unlocks it as many times.

\*\*Warning:\*\* Mutexes must be used carefully to avoid deadlocks.

\*\*Warning:\*\* To ensure proper cleanup without crashes or deadlocks,
the following conditions must be met:

- When a **Mutex**\'s reference count reaches zero and it is therefore
  destroyed, no threads (including the one on which the destruction will
  happen) must have it locked.
- When a `Thread<class_Thread>`{.interpreted-text role="ref"}\'s
  reference count reaches zero and it is therefore destroyed, it must
  not have any mutex locked.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using multiple threads <../tutorials/performance/using_multiple_threads>`{.interpreted-text
  role="doc"}
- `Thread-safe APIs <../tutorials/performance/thread_safe_apis>`{.interpreted-text
  role="doc"}

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

:::: {#class_Mutex_method_lock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **lock**()
`🔗<class_Mutex_method_lock>`{.interpreted-text role="ref"}

Locks this **Mutex**, blocks until it is unlocked by the current owner.

\*\*Note:\*\* This function returns without blocking if the thread
already has ownership of the mutex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mutex_method_try_lock}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **try_lock**()
`🔗<class_Mutex_method_try_lock>`{.interpreted-text role="ref"}

Tries locking this **Mutex**, but does not block. Returns `true` on
success, `false` otherwise.

\*\*Note:\*\* This function returns `true` if the thread already has
ownership of the mutex.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Mutex_method_unlock}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **unlock**()
`🔗<class_Mutex_method_unlock>`{.interpreted-text role="ref"}

Unlocks this **Mutex**, leaving it to other threads.

\*\*Note:\*\* If a thread called
`lock()<class_Mutex_method_lock>`{.interpreted-text role="ref"} or
`try_lock()<class_Mutex_method_try_lock>`{.interpreted-text role="ref"}
multiple times while already having ownership of the mutex, it must also
call `unlock()<class_Mutex_method_unlock>`{.interpreted-text role="ref"}
the same number of times in order to unlock it correctly.

\*\*Warning:\*\* Calling
`unlock()<class_Mutex_method_unlock>`{.interpreted-text role="ref"} more
times that `lock()<class_Mutex_method_lock>`{.interpreted-text
role="ref"} on a given thread, thus ending up trying to unlock a
non-locked mutex, is wrong and may causes crashes or deadlocks.
