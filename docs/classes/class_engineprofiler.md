github_url
:   hide

# EngineProfiler {#class_EngineProfiler}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Base class for creating custom profilers.

::: rst-class
classref-introduction-group
:::

## Description

This class can be used to implement custom profilers that are able to
interact with the engine and editor debugger.

See `EngineDebugger<class_EngineDebugger>`{.interpreted-text role="ref"}
and `EditorDebuggerPlugin<class_EditorDebuggerPlugin>`{.interpreted-text
role="ref"} for more information.

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

:::: {#class_EngineProfiler_private_method__add_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_add_frame**(data: `Array<class_Array>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EngineProfiler_private_method__add_frame>`{.interpreted-text
role="ref"}

Called when data is added to profiler using
`EngineDebugger.profiler_add_frame_data()<class_EngineDebugger_method_profiler_add_frame_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineProfiler_private_method__tick}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_tick**(frame_time: `float<class_float>`{.interpreted-text
role="ref"}, process_time: `float<class_float>`{.interpreted-text
role="ref"}, physics_time: `float<class_float>`{.interpreted-text
role="ref"}, physics_frame_time: `float<class_float>`{.interpreted-text
role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EngineProfiler_private_method__tick>`{.interpreted-text
role="ref"}

Called once every engine iteration when the profiler is active with
information about the current frame. All time values are in seconds.
Lower values represent faster processing times and are therefore
considered better.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_EngineProfiler_private_method__toggle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**\_toggle**(enable: `bool<class_bool>`{.interpreted-text role="ref"},
options: `Array<class_Array>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`🔗<class_EngineProfiler_private_method__toggle>`{.interpreted-text
role="ref"}

Called when the profiler is enabled/disabled, along with a set of
`options`.
