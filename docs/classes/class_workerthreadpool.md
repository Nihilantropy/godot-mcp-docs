github_url
:   hide

# WorkerThreadPool {#class_WorkerThreadPool}

**Inherits:** `Object<class_Object>`{.interpreted-text role="ref"}

A singleton that allocates some `Thread<class_Thread>`{.interpreted-text
role="ref"}s on startup, used to offload tasks to these threads.

::: rst-class
classref-introduction-group
:::

## Description

The **WorkerThreadPool** singleton allocates a set of
`Thread<class_Thread>`{.interpreted-text role="ref"}s (called worker
threads) on project startup and provides methods for offloading tasks to
them. This can be used for simple multithreading without having to
create `Thread<class_Thread>`{.interpreted-text role="ref"}s.

Tasks hold the `Callable<class_Callable>`{.interpreted-text role="ref"}
to be run by the threads. **WorkerThreadPool** can be used to create
regular tasks, which will be taken by one worker thread, or group tasks,
which can be distributed between multiple worker threads. Group tasks
execute the `Callable<class_Callable>`{.interpreted-text role="ref"}
multiple times, which makes them useful for iterating over a lot of
elements, such as the enemies in an arena.

Here\'s a sample on how to offload an expensive function to worker
threads:

::::: tabs
::: code-tab
gdscript

var enemies = \[\] \# An array to be filled with enemies.

func process_enemy_ai(enemy_index):

:   var processed_enemy = enemies\[enemy_index\] \# Expensive logic\...

func [process]{#process}(delta):

:   var task_id = WorkerThreadPool.add_group_task(process_enemy_ai,
    enemies.size()) \# Other code\...
    WorkerThreadPool.wait_for_group_task_completion(task_id) \# Other
    code that depends on the enemy AI already being processed.
:::

::: code-tab
csharp

private List\<Node\> [enemies]{#enemies} = new List\<Node\>(); // A list
to be filled with enemies.

private void ProcessEnemyAI(int enemyIndex) { Node processedEnemy =
[enemies]{#enemies}\[enemyIndex\]; // Expensive logic here. }

public override void [Process]{#process}(double delta) { long taskId =
WorkerThreadPool.AddGroupTask(Callable.From\<int\>(ProcessEnemyAI),
[enemies.Count]{#enemies.count}); // Other code\...
WorkerThreadPool.WaitForGroupTaskCompletion(taskId); // Other code that
depends on the enemy AI already being processed. }
:::
:::::

The above code relies on the number of elements in the `enemies` array
remaining constant during the multithreaded part.

\*\*Note:\*\* Using this singleton could affect performance negatively
if the task being distributed between threads is not computationally
expensive.

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

:::: {#class_WorkerThreadPool_method_add_group_task}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**add_group_task**(action: `Callable<class_Callable>`{.interpreted-text
role="ref"}, elements: `int<class_int>`{.interpreted-text role="ref"},
tasks_needed: `int<class_int>`{.interpreted-text role="ref"} = -1,
high_priority: `bool<class_bool>`{.interpreted-text role="ref"} = false,
description: `String<class_String>`{.interpreted-text role="ref"} =
\"\")
`🔗<class_WorkerThreadPool_method_add_group_task>`{.interpreted-text
role="ref"}

Adds `action` as a group task to be executed by the worker threads. The
`Callable<class_Callable>`{.interpreted-text role="ref"} will be called
a number of times based on `elements`, with the first thread calling it
with the value `0` as a parameter, and each consecutive execution
incrementing this value by 1 until it reaches `element - 1`.

The number of threads the task is distributed to is defined by
`tasks_needed`, where the default value `-1` means it is distributed to
all worker threads. `high_priority` determines if the task has a high
priority or a low priority (default). You can optionally provide a
`description` to help with debugging.

Returns a group task ID that can be used by other methods.

\*\*Warning:\*\* Every task must be waited for completion using
`wait_for_task_completion()<class_WorkerThreadPool_method_wait_for_task_completion>`{.interpreted-text
role="ref"} or
`wait_for_group_task_completion()<class_WorkerThreadPool_method_wait_for_group_task_completion>`{.interpreted-text
role="ref"} at some point so that any allocated resources inside the
task can be cleaned up.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_add_task}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **add_task**(action:
`Callable<class_Callable>`{.interpreted-text role="ref"}, high_priority:
`bool<class_bool>`{.interpreted-text role="ref"} = false, description:
`String<class_String>`{.interpreted-text role="ref"} = \"\")
`🔗<class_WorkerThreadPool_method_add_task>`{.interpreted-text
role="ref"}

Adds `action` as a task to be executed by a worker thread.
`high_priority` determines if the task has a high priority or a low
priority (default). You can optionally provide a `description` to help
with debugging.

Returns a task ID that can be used by other methods.

\*\*Warning:\*\* Every task must be waited for completion using
`wait_for_task_completion()<class_WorkerThreadPool_method_wait_for_task_completion>`{.interpreted-text
role="ref"} or
`wait_for_group_task_completion()<class_WorkerThreadPool_method_wait_for_group_task_completion>`{.interpreted-text
role="ref"} at some point so that any allocated resources inside the
task can be cleaned up.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_get_caller_group_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_caller_group_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WorkerThreadPool_method_get_caller_group_id>`{.interpreted-text
role="ref"}

Returns the task group ID of the current thread calling this method, or
`-1` if invalid or the current thread is not part of a task group.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_get_caller_task_id}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_caller_task_id**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WorkerThreadPool_method_get_caller_task_id>`{.interpreted-text
role="ref"}

Returns the task ID of the current thread calling this method, or `-1`
if the task is a group task, invalid or the current thread is not part
of the thread pool (e.g. the main thread).

Can be used by a task to get its own task ID, or to determine whether
the current code is running inside the worker thread pool.

\*\*Note:\*\* Group tasks have their own IDs, so this method will return
`-1` for group tasks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_get_group_processed_element_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**get_group_processed_element_count**(group_id:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WorkerThreadPool_method_get_group_processed_element_count>`{.interpreted-text
role="ref"}

Returns how many times the `Callable<class_Callable>`{.interpreted-text
role="ref"} of the group task with the given ID has already been
executed by the worker threads.

\*\*Note:\*\* If a thread has started executing the
`Callable<class_Callable>`{.interpreted-text role="ref"} but is yet to
finish, it won\'t be counted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_is_group_task_completed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_group_task_completed**(group_id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WorkerThreadPool_method_is_group_task_completed>`{.interpreted-text
role="ref"}

Returns `true` if the group task with the given ID is completed.

\*\*Note:\*\* You should only call this method between adding the group
task and awaiting its completion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_is_task_completed}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_task_completed**(task_id: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_WorkerThreadPool_method_is_task_completed>`{.interpreted-text
role="ref"}

Returns `true` if the task with the given ID is completed.

\*\*Note:\*\* You should only call this method between adding the task
and awaiting its completion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_wait_for_group_task_completion}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**wait_for_group_task_completion**(group_id:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_WorkerThreadPool_method_wait_for_group_task_completion>`{.interpreted-text
role="ref"}

Pauses the thread that calls this method until the group task with the
given ID is completed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_WorkerThreadPool_method_wait_for_task_completion}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**wait_for_task_completion**(task_id: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_WorkerThreadPool_method_wait_for_task_completion>`{.interpreted-text
role="ref"}

Pauses the thread that calls this method until the task with the given
ID is completed.

Returns
`@GlobalScope.OK<class_@GlobalScope_constant_OK>`{.interpreted-text
role="ref"} if the task could be successfully awaited.

Returns
`@GlobalScope.ERR_INVALID_PARAMETER<class_@GlobalScope_constant_ERR_INVALID_PARAMETER>`{.interpreted-text
role="ref"} if a task with the passed ID does not exist (maybe because
it was already awaited and disposed of).

Returns
`@GlobalScope.ERR_BUSY<class_@GlobalScope_constant_ERR_BUSY>`{.interpreted-text
role="ref"} if the call is made from another running task and, due to
task scheduling, there\'s potential for deadlocking (e.g., the task to
await may be at a lower level in the call stack and therefore can\'t
progress). This is an advanced situation that should only matter when
some tasks depend on others (in the current implementation, the tricky
case is a task trying to wait on an older one).
