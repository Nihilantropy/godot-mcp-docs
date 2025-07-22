github_url
:   hide

# PropertyTweener {#class_PropertyTweener}

**Inherits:** `Tweener<class_Tweener>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Interpolates an `Object<class_Object>`{.interpreted-text role="ref"}\'s
property over time.

::: rst-class
classref-introduction-group
:::

## Description

**PropertyTweener** is used to interpolate a property in an object. See
`Tween.tween_property()<class_Tween_method_tween_property>`{.interpreted-text
role="ref"} for more usage information.

The tweener will finish automatically if the target object is freed.

\*\*Note:\*\*
`Tween.tween_property()<class_Tween_method_tween_property>`{.interpreted-text
role="ref"} is the only correct way to create **PropertyTweener**. Any
**PropertyTweener** created manually will not function correctly.

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

:::: {#class_PropertyTweener_method_as_relative}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**as_relative**()
`🔗<class_PropertyTweener_method_as_relative>`{.interpreted-text
role="ref"}

When called, the final value will be used as a relative value instead.

\*\*Example:\*\* Move the node by `100` pixels to the right.

::::: tabs
::: code-tab
gdscript

var tween = get_tree().create_tween() tween.tween_property(self,
\"position\", Vector2.RIGHT \* 100, 1).as_relative()
:::

::: code-tab
csharp

Tween tween = GetTree().CreateTween(); tween.TweenProperty(this,
\"position\", Vector2.Right \* 100.0f, 1.0f).AsRelative();
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PropertyTweener_method_from}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**from**(value: `Variant<class_Variant>`{.interpreted-text role="ref"})
`🔗<class_PropertyTweener_method_from>`{.interpreted-text role="ref"}

Sets a custom initial value to the **PropertyTweener**.

\*\*Example:\*\* Move the node from position `(100, 100)` to
`(200, 100)`.

::::: tabs
::: code-tab
gdscript

var tween = get_tree().create_tween() tween.tween_property(self,
\"position\", Vector2(200, 100), 1).from(Vector2(100, 100))
:::

::: code-tab
csharp

Tween tween = GetTree().CreateTween(); tween.TweenProperty(this,
\"position\", new Vector2(200.0f, 100.0f), 1.0f).From(new
Vector2(100.0f, 100.0f));
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PropertyTweener_method_from_current}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**from_current**()
`🔗<class_PropertyTweener_method_from_current>`{.interpreted-text
role="ref"}

Makes the **PropertyTweener** use the current property value (i.e. at
the time of creating this **PropertyTweener**) as a starting point. This
is equivalent of using
`from()<class_PropertyTweener_method_from>`{.interpreted-text
role="ref"} with the current value. These two calls will do the same:

::::: tabs
::: code-tab
gdscript

tween.tween_property(self, \"position\", Vector2(200, 100),
1).from(position) tween.tween_property(self, \"position\", Vector2(200,
100), 1).from_current()
:::

::: code-tab
csharp

tween.TweenProperty(this, \"position\", new Vector2(200.0f, 100.0f),
1.0f).From(Position); tween.TweenProperty(this, \"position\", new
Vector2(200.0f, 100.0f), 1.0f).FromCurrent();
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PropertyTweener_method_set_custom_interpolator}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**set_custom_interpolator**(interpolator_method:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_PropertyTweener_method_set_custom_interpolator>`{.interpreted-text
role="ref"}

Allows interpolating the value with a custom easing function. The
provided `interpolator_method` will be called with a value ranging from
`0.0` to `1.0` and is expected to return a value within the same range
(values outside the range can be used for overshoot). The return value
of the method is then used for interpolation between initial and final
value. Note that the parameter passed to the method is still subject to
the tweener\'s own easing.

::::: tabs
::: code-tab
gdscript

\@export var curve: Curve

func [ready]{#ready}():

:   var tween = create_tween() \# Interpolate the value using a custom
    curve. tween.tween_property(self, \"position:x\", 300,
    1).as_relative().set_custom_interpolator(tween_curve)

func tween_curve(v):

:   return curve.sample_baked(v)
:::

::: code-tab
csharp

\[Export\] public Curve Curve { get; set; }

public override void [Ready]{#ready}() { Tween tween = CreateTween(); //
Interpolate the value using a custom curve. Callable tweenCurveCallable
= Callable.From\<float, float\>(TweenCurve); tween.TweenProperty(this,
\"position:x\", 300.0f,
1.0f).AsRelative().SetCustomInterpolator(tweenCurveCallable); }

private float TweenCurve(float value) { return Curve.SampleBaked(value);
}
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PropertyTweener_method_set_delay}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**set_delay**(delay: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_PropertyTweener_method_set_delay>`{.interpreted-text
role="ref"}

Sets the time in seconds after which the **PropertyTweener** will start
interpolating. By default there\'s no delay.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PropertyTweener_method_set_ease}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**set_ease**(ease: `EaseType<enum_Tween_EaseType>`{.interpreted-text
role="ref"})
`🔗<class_PropertyTweener_method_set_ease>`{.interpreted-text
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

:::: {#class_PropertyTweener_method_set_trans}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**set_trans**(trans:
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"})
`🔗<class_PropertyTweener_method_set_trans>`{.interpreted-text
role="ref"}

Sets the type of used transition from
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"}. If not set, the default transition is used from the
`Tween<class_Tween>`{.interpreted-text role="ref"} that contains this
Tweener.
