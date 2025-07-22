github_url
:   hide

# Tweener {#class_Tweener}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CallbackTweener<class_CallbackTweener>`{.interpreted-text role="ref"},
`IntervalTweener<class_IntervalTweener>`{.interpreted-text role="ref"},
`MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"},
`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"},
`SubtweenTweener<class_SubtweenTweener>`{.interpreted-text role="ref"}

Abstract class for all Tweeners used by
`Tween<class_Tween>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Tweeners are objects that perform a specific animating task, e.g.
interpolating a property or calling a method at a given time. A
**Tweener** can\'t be created manually, you need to use a dedicated
method from `Tween<class_Tween>`{.interpreted-text role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Signals

:::: {#class_Tweener_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**() `🔗<class_Tweener_signal_finished>`{.interpreted-text
role="ref"}

Emitted when the **Tweener** has just finished its job or became invalid
(e.g. due to a freed object).
