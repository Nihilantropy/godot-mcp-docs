github_url
:   hide

# OpenXRFutureResult {#class_OpenXRFutureResult}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Result object tracking the asynchronous result of an OpenXR Future
object.

::: rst-class
classref-introduction-group
:::

## Description

Result object tracking the asynchronous result of an OpenXR Future
object, you can use this object to track the result status.

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

:::: {#class_OpenXRFutureResult_signal_completed}
::: rst-class
classref-signal
:::
::::

**completed**(result:
`OpenXRFutureResult<class_OpenXRFutureResult>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRFutureResult_signal_completed>`{.interpreted-text
role="ref"}

Emitted when the asynchronous function is finished or has been
cancelled.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_OpenXRFutureResult_ResultStatus}
::: rst-class
classref-enumeration
:::
::::

enum **ResultStatus**:
`🔗<enum_OpenXRFutureResult_ResultStatus>`{.interpreted-text role="ref"}

:::: {#class_OpenXRFutureResult_constant_RESULT_RUNNING}
::: rst-class
classref-enumeration-constant
:::
::::

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>`{.interpreted-text
role="ref"} **RESULT_RUNNING** = `0`

The asynchronous function is running.

:::: {#class_OpenXRFutureResult_constant_RESULT_FINISHED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>`{.interpreted-text
role="ref"} **RESULT_FINISHED** = `1`

The asynchronous function has finished.

:::: {#class_OpenXRFutureResult_constant_RESULT_CANCELLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>`{.interpreted-text
role="ref"} **RESULT_CANCELLED** = `2`

The asynchronous function has been cancelled.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRFutureResult_method_cancel_future}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cancel_future**()
`🔗<class_OpenXRFutureResult_method_cancel_future>`{.interpreted-text
role="ref"}

Cancel this future, this will interrupt and stop the asynchronous
function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRFutureResult_method_get_future}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_future**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRFutureResult_method_get_future>`{.interpreted-text
role="ref"}

Return the `XrFutureEXT` value this result relates to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRFutureResult_method_get_result_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**get_result_value**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRFutureResult_method_get_result_value>`{.interpreted-text
role="ref"}

Returns the result value of our asynchronous function (if set by the
extension). The type of this result value depends on the function being
called. Consult the documentation of the relevant function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRFutureResult_method_get_status}
::: rst-class
classref-method
:::
::::

`ResultStatus<enum_OpenXRFutureResult_ResultStatus>`{.interpreted-text
role="ref"} **get_status**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRFutureResult_method_get_status>`{.interpreted-text
role="ref"}

Returns the status of this result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRFutureResult_method_set_result_value}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_result_value**(result_value:
`Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_OpenXRFutureResult_method_set_result_value>`{.interpreted-text
role="ref"}

Stores the result value we expose to the user.

\*\*Note:\*\* This method should only be called by an OpenXR extension
that implements an asynchronous function.
