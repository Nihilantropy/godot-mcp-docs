github_url
:   hide

# SubtweenTweener {#class_SubtweenTweener}

**Inherits:** `Tweener<class_Tweener>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Runs a `Tween<class_Tween>`{.interpreted-text role="ref"} nested within
another `Tween<class_Tween>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

**SubtweenTweener** is used to execute a
`Tween<class_Tween>`{.interpreted-text role="ref"} as one step in a
sequence defined by another `Tween<class_Tween>`{.interpreted-text
role="ref"}. See
`Tween.tween_subtween()<class_Tween_method_tween_subtween>`{.interpreted-text
role="ref"} for more usage information.

\*\*Note:\*\*
`Tween.tween_subtween()<class_Tween_method_tween_subtween>`{.interpreted-text
role="ref"} is the only correct way to create **SubtweenTweener**. Any
**SubtweenTweener** created manually will not function correctly.

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

:::: {#class_SubtweenTweener_method_set_delay}
::: rst-class
classref-method
:::
::::

`SubtweenTweener<class_SubtweenTweener>`{.interpreted-text role="ref"}
**set_delay**(delay: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SubtweenTweener_method_set_delay>`{.interpreted-text
role="ref"}

Sets the time in seconds after which the **SubtweenTweener** will start
running the subtween. By default there\'s no delay.
