github_url
:   hide

# Semaphore {#class_Semaphore}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

A synchronization mechanism used to control access to a shared resource
by `Thread<class_Thread>`{.interpreted-text role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

A synchronization semaphore that can be used to synchronize multiple
`Thread<class_Thread>`{.interpreted-text role="ref"}s. Initialized to
zero on creation. For a binary version, see
`Mutex<class_Mutex>`{.interpreted-text role="ref"}.

\*\*Warning:\*\* Semaphores must be used carefully to avoid deadlocks.

\*\*Warning:\*\* To guarantee that the operating system is able to
perform proper cleanup (no crashes, no deadlocks), these conditions must
be met:

- When a **Semaphore**\'s reference count reaches zero and it is
  therefore destroyed, no threads must be waiting on it.
- When a `Thread<class_Thread>`{.interpreted-text role="ref"}\'s
  reference count reaches zero and it is therefore destroyed, it must
  not be waiting on any semaphore.

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

:::: {#class_Semaphore_method_post}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **post**(count:
`int<class_int>`{.interpreted-text role="ref"} = 1)
`🔗<class_Semaphore_method_post>`{.interpreted-text role="ref"}

Lowers the **Semaphore**, allowing one thread in, or more if `count` is
specified.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Semaphore_method_try_wait}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **try_wait**()
`🔗<class_Semaphore_method_try_wait>`{.interpreted-text role="ref"}

Like `wait()<class_Semaphore_method_wait>`{.interpreted-text
role="ref"}, but won\'t block, so if the value is zero, fails
immediately and returns `false`. If non-zero, it returns `true` to
report success.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Semaphore_method_wait}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **wait**()
`🔗<class_Semaphore_method_wait>`{.interpreted-text role="ref"}

Waits for the **Semaphore**, if its value is zero, blocks until
non-zero.
