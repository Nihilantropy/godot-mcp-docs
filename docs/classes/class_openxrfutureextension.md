github_url
:   hide

# OpenXRFutureExtension {#class_OpenXRFutureExtension}

**Inherits:**
`OpenXRExtensionWrapper<class_OpenXRExtensionWrapper>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

The OpenXR Future extension allows for asynchronous APIs to be used.

::: rst-class
classref-introduction-group
:::

## Description

This is a support extension in OpenXR that allows other OpenXR
extensions to start asynchronous functions and get a callback after this
function finishes. It is not intended for consumption within GDScript
but can be accessed from GDExtension.

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

:::: {#class_OpenXRFutureExtension_method_cancel_future}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**cancel_future**(future: `int<class_int>`{.interpreted-text
role="ref"})
`🔗<class_OpenXRFutureExtension_method_cancel_future>`{.interpreted-text
role="ref"}

Cancels an in-progress future. `future` must be an `XrFutureEXT` value
previously returned by an API that started an asynchronous function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRFutureExtension_method_is_active}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_active**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRFutureExtension_method_is_active>`{.interpreted-text
role="ref"}

Returns `true` if futures are available in the OpenXR runtime used. This
function will only return a usable result after OpenXR has been
initialized.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRFutureExtension_method_register_future}
::: rst-class
classref-method
:::
::::

`OpenXRFutureResult<class_OpenXRFutureResult>`{.interpreted-text
role="ref"} **register_future**(future:
`int<class_int>`{.interpreted-text role="ref"}, on_success:
`Callable<class_Callable>`{.interpreted-text role="ref"} = Callable())
`🔗<class_OpenXRFutureExtension_method_register_future>`{.interpreted-text
role="ref"}

Register an OpenXR Future object so we monitor for completion. `future`
must be an `XrFutureEXT` value previously returned by an API that
started an asynchronous function.

You can optionally specify `on_success`, it will be invoked on
successful completion of the future.

Or you can use the returned
`OpenXRFutureResult<class_OpenXRFutureResult>`{.interpreted-text
role="ref"} object to `await` its
`OpenXRFutureResult.completed<class_OpenXRFutureResult_signal_completed>`{.interpreted-text
role="ref"} signal.

    var future_result = OpenXRFutureExtension.register_future(future)
    await future_result.completed
    if future_result.get_status() == OpenXRFutureResult.RESULT_FINISHED:
        # Handle your success
        pass
