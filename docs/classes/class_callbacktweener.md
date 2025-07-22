github_url
:   hide

# CallbackTweener {#class_CallbackTweener}

**Inherits:** `Tweener<class_Tweener>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Calls the specified method after optional delay.

::: rst-class
classref-introduction-group
:::

## Description

**CallbackTweener** is used to call a method in a tweening sequence. See
`Tween.tween_callback()<class_Tween_method_tween_callback>`{.interpreted-text
role="ref"} for more usage information.

The tweener will finish automatically if the callback\'s target object
is freed.

\*\*Note:\*\*
`Tween.tween_callback()<class_Tween_method_tween_callback>`{.interpreted-text
role="ref"} is the only correct way to create **CallbackTweener**. Any
**CallbackTweener** created manually will not function correctly.

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

:::: {#class_CallbackTweener_method_set_delay}
::: rst-class
classref-method
:::
::::

`CallbackTweener<class_CallbackTweener>`{.interpreted-text role="ref"}
**set_delay**(delay: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_CallbackTweener_method_set_delay>`{.interpreted-text
role="ref"}

Makes the callback call delayed by given time in seconds.

\*\*Example:\*\* Call
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} after 2 seconds:

    var tween = get_tree().create_tween()
    tween.tween_callback(queue_free).set_delay(2)
