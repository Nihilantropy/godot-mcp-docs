github_url
:   hide

# MethodTweener {#class_MethodTweener}

**Inherits:** `Tweener<class_Tweener>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Interpolates an abstract value and supplies it to a method called over
time.

::: rst-class
classref-introduction-group
:::

## Description

**MethodTweener** is similar to a combination of
`CallbackTweener<class_CallbackTweener>`{.interpreted-text role="ref"}
and `PropertyTweener<class_PropertyTweener>`{.interpreted-text
role="ref"}. It calls a method providing an interpolated value as a
parameter. See
`Tween.tween_method()<class_Tween_method_tween_method>`{.interpreted-text
role="ref"} for more usage information.

The tweener will finish automatically if the callback\'s target object
is freed.

\*\*Note:\*\*
`Tween.tween_method()<class_Tween_method_tween_method>`{.interpreted-text
role="ref"} is the only correct way to create **MethodTweener**. Any
**MethodTweener** created manually will not function correctly.

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

:::: {#class_MethodTweener_method_set_delay}
::: rst-class
classref-method
:::
::::

`MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"}
**set_delay**(delay: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_MethodTweener_method_set_delay>`{.interpreted-text role="ref"}

Sets the time in seconds after which the **MethodTweener** will start
interpolating. By default there\'s no delay.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MethodTweener_method_set_ease}
::: rst-class
classref-method
:::
::::

`MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"}
**set_ease**(ease: `EaseType<enum_Tween_EaseType>`{.interpreted-text
role="ref"}) `🔗<class_MethodTweener_method_set_ease>`{.interpreted-text
role="ref"}

Sets the type of used easing from
`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}. If not
set, the default easing is used from the
`Tween<class_Tween>`{.interpreted-text role="ref"} that contains this
Tweener.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MethodTweener_method_set_trans}
::: rst-class
classref-method
:::
::::

`MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"}
**set_trans**(trans:
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"})
`🔗<class_MethodTweener_method_set_trans>`{.interpreted-text role="ref"}

Sets the type of used transition from
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"}. If not set, the default transition is used from the
`Tween<class_Tween>`{.interpreted-text role="ref"} that contains this
Tweener.
