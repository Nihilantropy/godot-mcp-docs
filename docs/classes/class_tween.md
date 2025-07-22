github_url
:   hide

# Tween {#class_Tween}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Lightweight object used for general-purpose animation via script, using
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s.

::: rst-class
classref-introduction-group
:::

## Description

Tweens are mostly useful for animations requiring a numerical property
to be interpolated over a range of values. The name *tween* comes from
*in-betweening*, an animation technique where you specify *keyframes*
and the computer interpolates the frames that appear between them.
Animating something with a **Tween** is called tweening.

\*\*Tween\*\* is more suited than
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
for animations where you don\'t know the final values in advance. For
example, interpolating a dynamically-chosen camera zoom value is best
done with a **Tween**; it would be difficult to do the same thing with
an `AnimationPlayer<class_AnimationPlayer>`{.interpreted-text
role="ref"} node. Tweens are also more light-weight than
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"},
so they are very much suited for simple animations or general tasks that
don\'t require visual tweaking provided by the editor. They can be used
in a \"fire-and-forget\" manner for some logic that normally would be
done by code. You can e.g. make something shoot periodically by using a
looped `CallbackTweener<class_CallbackTweener>`{.interpreted-text
role="ref"} with a delay.

A **Tween** can be created by using either
`SceneTree.create_tween()<class_SceneTree_method_create_tween>`{.interpreted-text
role="ref"} or
`Node.create_tween()<class_Node_method_create_tween>`{.interpreted-text
role="ref"}. **Tween**s created manually (i.e. by using `Tween.new()`)
are invalid and can\'t be used for tweening values.

A tween animation is created by adding
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s to the **Tween**
object, using
`tween_property()<class_Tween_method_tween_property>`{.interpreted-text
role="ref"},
`tween_interval()<class_Tween_method_tween_interval>`{.interpreted-text
role="ref"},
`tween_callback()<class_Tween_method_tween_callback>`{.interpreted-text
role="ref"} or
`tween_method()<class_Tween_method_tween_method>`{.interpreted-text
role="ref"}:

::::: tabs
::: code-tab
gdscript

var tween = get_tree().create_tween() tween.tween_property(\$Sprite,
\"modulate\", Color.RED, 1.0) tween.tween_property(\$Sprite, \"scale\",
Vector2(), 1.0) tween.tween_callback(\$Sprite.queue_free)
:::

::: code-tab
csharp

Tween tween = GetTree().CreateTween();
tween.TweenProperty(GetNode(\"Sprite\"), \"modulate\", Colors.Red,
1.0f); tween.TweenProperty(GetNode(\"Sprite\"), \"scale\", Vector2.Zero,
1.0f);
tween.TweenCallback(Callable.From(GetNode(\"Sprite\").QueueFree));
:::
:::::

This sequence will make the `$Sprite` node turn red, then shrink, before
finally calling
`Node.queue_free()<class_Node_method_queue_free>`{.interpreted-text
role="ref"} to free the sprite.
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s are executed one
after another by default. This behavior can be changed using
`parallel()<class_Tween_method_parallel>`{.interpreted-text role="ref"}
and `set_parallel()<class_Tween_method_set_parallel>`{.interpreted-text
role="ref"}.

When a `Tweener<class_Tweener>`{.interpreted-text role="ref"} is created
with one of the `tween_*` methods, a chained method call can be used to
tweak the properties of this `Tweener<class_Tweener>`{.interpreted-text
role="ref"}. For example, if you want to set a different transition type
in the above example, you can use
`set_trans()<class_Tween_method_set_trans>`{.interpreted-text
role="ref"}:

::::: tabs
::: code-tab
gdscript

var tween = get_tree().create_tween() tween.tween_property(\$Sprite,
\"modulate\", Color.RED, 1.0).set_trans(Tween.TRANS_SINE)
tween.tween_property(\$Sprite, \"scale\", Vector2(),
1.0).set_trans(Tween.TRANS_BOUNCE)
tween.tween_callback(\$Sprite.queue_free)
:::

::: code-tab
csharp

Tween tween = GetTree().CreateTween();
tween.TweenProperty(GetNode(\"Sprite\"), \"modulate\", Colors.Red,
1.0f).SetTrans(Tween.TransitionType.Sine);
tween.TweenProperty(GetNode(\"Sprite\"), \"scale\", Vector2.Zero,
1.0f).SetTrans(Tween.TransitionType.Bounce);
tween.TweenCallback(Callable.From(GetNode(\"Sprite\").QueueFree));
:::
:::::

Most of the **Tween** methods can be chained this way too. In the
following example the **Tween** is bound to the running script\'s node
and a default transition is set for its
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s:

::::: tabs
::: code-tab
gdscript

var tween =
get_tree().create_tween().bind_node(self).set_trans(Tween.TRANS_ELASTIC)
tween.tween_property(\$Sprite, \"modulate\", Color.RED, 1.0)
tween.tween_property(\$Sprite, \"scale\", Vector2(), 1.0)
tween.tween_callback(\$Sprite.queue_free)
:::

::: code-tab
csharp

var tween =
GetTree().CreateTween().BindNode(this).SetTrans(Tween.TransitionType.Elastic);
tween.TweenProperty(GetNode(\"Sprite\"), \"modulate\", Colors.Red,
1.0f); tween.TweenProperty(GetNode(\"Sprite\"), \"scale\", Vector2.Zero,
1.0f);
tween.TweenCallback(Callable.From(GetNode(\"Sprite\").QueueFree));
:::
:::::

Another interesting use for **Tween**s is animating arbitrary sets of
objects:

::::: tabs
::: code-tab
gdscript

var tween = create_tween() for sprite in get_children():
tween.tween_property(sprite, \"position\", Vector2(0, 0), 1.0)
:::

::: code-tab
csharp

Tween tween = CreateTween(); foreach (Node sprite in GetChildren())
tween.TweenProperty(sprite, \"position\", Vector2.Zero, 1.0f);
:::
:::::

In the example above, all children of a node are moved one after another
to position `(0, 0)`.

You should avoid using more than one **Tween** per object\'s property.
If two or more tweens animate one property at the same time, the last
one created will take priority and assign the final value. If you want
to interrupt and restart an animation, consider assigning the **Tween**
to a variable:

::::: tabs
::: code-tab
gdscript

var tween func animate(): if tween: tween.kill() \# Abort the previous
animation. tween = create_tween()
:::

::: code-tab
csharp

private Tween [tween]{#tween};

public void Animate() { if ([tween]{#tween} != null)
[tween.Kill]{#tween.kill}(); // Abort the previous animation
[tween]{#tween} = CreateTween(); }
:::
:::::

Some `Tweener<class_Tweener>`{.interpreted-text role="ref"}s use
transitions and eases. The first accepts a
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} constant, and refers to the way the timing of the animation
is handled (see [easings.net](https://easings.net/) for some examples).
The second accepts an `EaseType<enum_Tween_EaseType>`{.interpreted-text
role="ref"} constant, and controls where the `trans_type` is applied to
the interpolation (in the beginning, the end, or both). If you don\'t
know which transition and easing to pick, you can try different
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} constants with
`EASE_IN_OUT<class_Tween_constant_EASE_IN_OUT>`{.interpreted-text
role="ref"}, and use the one that looks best.

\`Tween easing and transition types cheatsheet
\<https://raw.githubusercontent.com/godotengine/godot-docs/master/img/tween_cheatsheet.webp\>\`\_\_

\*\*Note:\*\* Tweens are not designed to be reused and trying to do so
results in an undefined behavior. Create a new Tween for each animation
and every time you replay an animation from start. Keep in mind that
Tweens start immediately, so only create a Tween when you want to start
animating.

\*\*Note:\*\* The tween is processed after all of the nodes in the
current frame, i.e. node\'s
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"} method would be called before the tween (or
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"} depending on the value passed to
`set_process_mode()<class_Tween_method_set_process_mode>`{.interpreted-text
role="ref"}).

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

:::: {#class_Tween_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**() `🔗<class_Tween_signal_finished>`{.interpreted-text
role="ref"}

Emitted when the **Tween** has finished all tweening. Never emitted when
the **Tween** is set to infinite looping (see
`set_loops()<class_Tween_method_set_loops>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_signal_loop_finished}
::: rst-class
classref-signal
:::
::::

**loop_finished**(loop_count: `int<class_int>`{.interpreted-text
role="ref"}) `🔗<class_Tween_signal_loop_finished>`{.interpreted-text
role="ref"}

Emitted when a full loop is complete (see
`set_loops()<class_Tween_method_set_loops>`{.interpreted-text
role="ref"}), providing the loop index. This signal is not emitted after
the final loop, use
`finished<class_Tween_signal_finished>`{.interpreted-text role="ref"}
instead for this case.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_signal_step_finished}
::: rst-class
classref-signal
:::
::::

**step_finished**(idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_Tween_signal_step_finished>`{.interpreted-text role="ref"}

Emitted when one step of the **Tween** is complete, providing the step
index. One step is either a single
`Tweener<class_Tweener>`{.interpreted-text role="ref"} or a group of
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s running in
parallel.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Tween_TweenProcessMode}
::: rst-class
classref-enumeration
:::
::::

enum **TweenProcessMode**:
`🔗<enum_Tween_TweenProcessMode>`{.interpreted-text role="ref"}

:::: {#class_Tween_constant_TWEEN_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`TweenProcessMode<enum_Tween_TweenProcessMode>`{.interpreted-text
role="ref"} **TWEEN_PROCESS_PHYSICS** = `0`

The **Tween** updates after each physics frame (see
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}).

:::: {#class_Tween_constant_TWEEN_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`TweenProcessMode<enum_Tween_TweenProcessMode>`{.interpreted-text
role="ref"} **TWEEN_PROCESS_IDLE** = `1`

The **Tween** updates after each process frame (see
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Tween_TweenPauseMode}
::: rst-class
classref-enumeration
:::
::::

enum **TweenPauseMode**:
`🔗<enum_Tween_TweenPauseMode>`{.interpreted-text role="ref"}

:::: {#class_Tween_constant_TWEEN_PAUSE_BOUND}
::: rst-class
classref-enumeration-constant
:::
::::

`TweenPauseMode<enum_Tween_TweenPauseMode>`{.interpreted-text
role="ref"} **TWEEN_PAUSE_BOUND** = `0`

If the **Tween** has a bound node, it will process when that node can
process (see
`Node.process_mode<class_Node_property_process_mode>`{.interpreted-text
role="ref"}). Otherwise it\'s the same as
`TWEEN_PAUSE_STOP<class_Tween_constant_TWEEN_PAUSE_STOP>`{.interpreted-text
role="ref"}.

:::: {#class_Tween_constant_TWEEN_PAUSE_STOP}
::: rst-class
classref-enumeration-constant
:::
::::

`TweenPauseMode<enum_Tween_TweenPauseMode>`{.interpreted-text
role="ref"} **TWEEN_PAUSE_STOP** = `1`

If `SceneTree<class_SceneTree>`{.interpreted-text role="ref"} is paused,
the **Tween** will also pause.

:::: {#class_Tween_constant_TWEEN_PAUSE_PROCESS}
::: rst-class
classref-enumeration-constant
:::
::::

`TweenPauseMode<enum_Tween_TweenPauseMode>`{.interpreted-text
role="ref"} **TWEEN_PAUSE_PROCESS** = `2`

The **Tween** will process regardless of whether
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} is paused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Tween_TransitionType}
::: rst-class
classref-enumeration
:::
::::

enum **TransitionType**:
`🔗<enum_Tween_TransitionType>`{.interpreted-text role="ref"}

:::: {#class_Tween_constant_TRANS_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_LINEAR** = `0`

The animation is interpolated linearly.

:::: {#class_Tween_constant_TRANS_SINE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_SINE** = `1`

The animation is interpolated using a sine function.

:::: {#class_Tween_constant_TRANS_QUINT}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_QUINT** = `2`

The animation is interpolated with a quintic (to the power of 5)
function.

:::: {#class_Tween_constant_TRANS_QUART}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_QUART** = `3`

The animation is interpolated with a quartic (to the power of 4)
function.

:::: {#class_Tween_constant_TRANS_QUAD}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_QUAD** = `4`

The animation is interpolated with a quadratic (to the power of 2)
function.

:::: {#class_Tween_constant_TRANS_EXPO}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_EXPO** = `5`

The animation is interpolated with an exponential (to the power of x)
function.

:::: {#class_Tween_constant_TRANS_ELASTIC}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_ELASTIC** = `6`

The animation is interpolated with elasticity, wiggling around the
edges.

:::: {#class_Tween_constant_TRANS_CUBIC}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_CUBIC** = `7`

The animation is interpolated with a cubic (to the power of 3) function.

:::: {#class_Tween_constant_TRANS_CIRC}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_CIRC** = `8`

The animation is interpolated with a function using square roots.

:::: {#class_Tween_constant_TRANS_BOUNCE}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_BOUNCE** = `9`

The animation is interpolated by bouncing at the end.

:::: {#class_Tween_constant_TRANS_BACK}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_BACK** = `10`

The animation is interpolated backing out at ends.

:::: {#class_Tween_constant_TRANS_SPRING}
::: rst-class
classref-enumeration-constant
:::
::::

`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} **TRANS_SPRING** = `11`

The animation is interpolated like a spring towards the end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Tween_EaseType}
::: rst-class
classref-enumeration
:::
::::

enum **EaseType**: `🔗<enum_Tween_EaseType>`{.interpreted-text
role="ref"}

:::: {#class_Tween_constant_EASE_IN}
::: rst-class
classref-enumeration-constant
:::
::::

`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
**EASE_IN** = `0`

The interpolation starts slowly and speeds up towards the end.

:::: {#class_Tween_constant_EASE_OUT}
::: rst-class
classref-enumeration-constant
:::
::::

`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
**EASE_OUT** = `1`

The interpolation starts quickly and slows down towards the end.

:::: {#class_Tween_constant_EASE_IN_OUT}
::: rst-class
classref-enumeration-constant
:::
::::

`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
**EASE_IN_OUT** = `2`

A combination of
`EASE_IN<class_Tween_constant_EASE_IN>`{.interpreted-text role="ref"}
and `EASE_OUT<class_Tween_constant_EASE_OUT>`{.interpreted-text
role="ref"}. The interpolation is slowest at both ends.

:::: {#class_Tween_constant_EASE_OUT_IN}
::: rst-class
classref-enumeration-constant
:::
::::

`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"}
**EASE_OUT_IN** = `3`

A combination of
`EASE_IN<class_Tween_constant_EASE_IN>`{.interpreted-text role="ref"}
and `EASE_OUT<class_Tween_constant_EASE_OUT>`{.interpreted-text
role="ref"}. The interpolation is fastest at both ends.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Tween_method_bind_node}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **bind_node**(node:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_Tween_method_bind_node>`{.interpreted-text role="ref"}

Binds this **Tween** with the given `node`. **Tween**s are processed
directly by the `SceneTree<class_SceneTree>`{.interpreted-text
role="ref"}, so they run independently of the animated nodes. When you
bind a `Node<class_Node>`{.interpreted-text role="ref"} with the
**Tween**, the **Tween** will halt the animation when the object is not
inside tree and the **Tween** will be automatically killed when the
bound object is freed. Also
`TWEEN_PAUSE_BOUND<class_Tween_constant_TWEEN_PAUSE_BOUND>`{.interpreted-text
role="ref"} will make the pausing behavior dependent on the bound node.

For a shorter way to create and bind a **Tween**, you can use
`Node.create_tween()<class_Node_method_create_tween>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_chain}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **chain**()
`🔗<class_Tween_method_chain>`{.interpreted-text role="ref"}

Used to chain two `Tweener<class_Tweener>`{.interpreted-text
role="ref"}s after
`set_parallel()<class_Tween_method_set_parallel>`{.interpreted-text
role="ref"} is called with `true`.

::::: tabs
::: code-tab
gdscript

var tween = create_tween().set_parallel(true) tween.tween_property(\...)
tween.tween_property(\...) \# Will run parallelly with above.
tween.chain().tween_property(\...) \# Will run after two above are
finished.
:::

::: code-tab
csharp

Tween tween = CreateTween().SetParallel(true);
tween.TweenProperty(\...); tween.TweenProperty(\...); // Will run
parallelly with above. tween.Chain().TweenProperty(\...); // Will run
after two above are finished.
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_custom_step}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **custom_step**(delta:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Tween_method_custom_step>`{.interpreted-text role="ref"}

Processes the **Tween** by the given `delta` value, in seconds. This is
mostly useful for manual control when the **Tween** is paused. It can
also be used to end the **Tween** animation immediately, by setting
`delta` longer than the whole duration of the **Tween** animation.

Returns `true` if the **Tween** still has
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s that haven\'t
finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_get_loops_left}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_loops_left**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Tween_method_get_loops_left>`{.interpreted-text
role="ref"}

Returns the number of remaining loops for this **Tween** (see
`set_loops()<class_Tween_method_set_loops>`{.interpreted-text
role="ref"}). A return value of `-1` indicates an infinitely looping
**Tween**, and a return value of `0` indicates that the **Tween** has
already finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_get_total_elapsed_time}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_total_elapsed_time**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Tween_method_get_total_elapsed_time>`{.interpreted-text
role="ref"}

Returns the total time in seconds the **Tween** has been animating (i.e.
the time since it started, not counting pauses etc.). The time is
affected by
`set_speed_scale()<class_Tween_method_set_speed_scale>`{.interpreted-text
role="ref"}, and `stop()<class_Tween_method_stop>`{.interpreted-text
role="ref"} will reset it to `0`.

\*\*Note:\*\* As it results from accumulating frame deltas, the time
returned after the **Tween** has finished animating will be slightly
greater than the actual **Tween** duration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_interpolate_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**interpolate_value**(initial_value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, delta_value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, elapsed_time:
`float<class_float>`{.interpreted-text role="ref"}, duration:
`float<class_float>`{.interpreted-text role="ref"}, trans_type:
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"}, ease_type:
`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"})
`static (This method doesn't need an instance to be called, so it can be called directly using the class name.)`{.interpreted-text
role="abbr"}
`🔗<class_Tween_method_interpolate_value>`{.interpreted-text role="ref"}

This method can be used for manual interpolation of a value, when you
don\'t want **Tween** to do animating for you. It\'s similar to
`@GlobalScope.lerp()<class_@GlobalScope_method_lerp>`{.interpreted-text
role="ref"}, but with support for custom transition and easing.

`initial_value` is the starting value of the interpolation.

`delta_value` is the change of the value in the interpolation, i.e.
it\'s equal to `final_value - initial_value`.

`elapsed_time` is the time in seconds that passed after the
interpolation started and it\'s used to control the position of the
interpolation. E.g. when it\'s equal to half of the `duration`, the
interpolated value will be halfway between initial and final values.
This value can also be greater than `duration` or lower than 0, which
will extrapolate the value.

`duration` is the total time of the interpolation.

\*\*Note:\*\* If `duration` is equal to `0`, the method will always
return the final value, regardless of `elapsed_time` provided.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_is_running}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_running**()
`🔗<class_Tween_method_is_running>`{.interpreted-text role="ref"}

Returns whether the **Tween** is currently running, i.e. it wasn\'t
paused and it\'s not finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_is_valid}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_valid**()
`🔗<class_Tween_method_is_valid>`{.interpreted-text role="ref"}

Returns whether the **Tween** is valid. A valid **Tween** is a **Tween**
contained by the scene tree (i.e. the array from
`SceneTree.get_processed_tweens()<class_SceneTree_method_get_processed_tweens>`{.interpreted-text
role="ref"} will contain this **Tween**). A **Tween** might become
invalid when it has finished tweening, is killed, or when created with
`Tween.new()`. Invalid **Tween**s can\'t have
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s appended.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_kill}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **kill**()
`🔗<class_Tween_method_kill>`{.interpreted-text role="ref"}

Aborts all tweening operations and invalidates the **Tween**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_parallel}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **parallel**()
`🔗<class_Tween_method_parallel>`{.interpreted-text role="ref"}

Makes the next `Tweener<class_Tweener>`{.interpreted-text role="ref"}
run parallelly to the previous one.

::::: tabs
::: code-tab
gdscript

var tween = create_tween() tween.tween_property(\...)
tween.parallel().tween_property(\...)
tween.parallel().tween_property(\...)
:::

::: code-tab
csharp

Tween tween = CreateTween(); tween.TweenProperty(\...);
tween.Parallel().TweenProperty(\...);
tween.Parallel().TweenProperty(\...);
:::
:::::

All `Tweener<class_Tweener>`{.interpreted-text role="ref"}s in the
example will run at the same time.

You can make the **Tween** parallel by default by using
`set_parallel()<class_Tween_method_set_parallel>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_pause}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **pause**()
`🔗<class_Tween_method_pause>`{.interpreted-text role="ref"}

Pauses the tweening. The animation can be resumed by using
`play()<class_Tween_method_play>`{.interpreted-text role="ref"}.

\*\*Note:\*\* If a Tween is paused and not bound to any node, it will
exist indefinitely until manually started or invalidated. If you lose a
reference to such Tween, you can retrieve it using
`SceneTree.get_processed_tweens()<class_SceneTree_method_get_processed_tweens>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **play**()
`🔗<class_Tween_method_play>`{.interpreted-text role="ref"}

Resumes a paused or stopped **Tween**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_ease}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **set_ease**(ease:
`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"})
`🔗<class_Tween_method_set_ease>`{.interpreted-text role="ref"}

Sets the default ease type for
`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}s
and `MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"}s
appended after this method.

Before this method is called, the default ease type is
`EASE_IN_OUT<class_Tween_constant_EASE_IN_OUT>`{.interpreted-text
role="ref"}.

    var tween = create_tween()
    tween.tween_property(self, "position", Vector2(300, 0), 0.5) # Uses EASE_IN_OUT.
    tween.set_ease(Tween.EASE_IN)
    tween.tween_property(self, "rotation_degrees", 45.0, 0.5) # Uses EASE_IN.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_ignore_time_scale}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"}
**set_ignore_time_scale**(ignore: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_Tween_method_set_ignore_time_scale>`{.interpreted-text
role="ref"}

If `ignore` is `true`, the tween will ignore
`Engine.time_scale<class_Engine_property_time_scale>`{.interpreted-text
role="ref"} and update with the real, elapsed time. This affects all
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s and their
delays. Default value is `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_loops}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **set_loops**(loops:
`int<class_int>`{.interpreted-text role="ref"} = 0)
`🔗<class_Tween_method_set_loops>`{.interpreted-text role="ref"}

Sets the number of times the tweening sequence will be repeated, i.e.
`set_loops(2)` will run the animation twice.

Calling this method without arguments will make the **Tween** run
infinitely, until either it is killed with
`kill()<class_Tween_method_kill>`{.interpreted-text role="ref"}, the
**Tween**\'s bound node is freed, or all the animated objects have been
freed (which makes further animation impossible).

\*\*Warning:\*\* Make sure to always add some duration/delay when using
infinite loops. To prevent the game freezing, 0-duration looped
animations (e.g. a single
`CallbackTweener<class_CallbackTweener>`{.interpreted-text role="ref"}
with no delay) are stopped after a small number of loops, which may
produce unexpected results. If a **Tween**\'s lifetime depends on some
node, always use
`bind_node()<class_Tween_method_bind_node>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_parallel}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"}
**set_parallel**(parallel: `bool<class_bool>`{.interpreted-text
role="ref"} = true)
`🔗<class_Tween_method_set_parallel>`{.interpreted-text role="ref"}

If `parallel` is `true`, the `Tweener<class_Tweener>`{.interpreted-text
role="ref"}s appended after this method will by default run
simultaneously, as opposed to sequentially.

\*\*Note:\*\* Just like with
`parallel()<class_Tween_method_parallel>`{.interpreted-text role="ref"},
the tweener added right before this method will also be part of the
parallel step.

    tween.tween_property(self, "position", Vector2(300, 0), 0.5)
    tween.set_parallel()
    tween.tween_property(self, "modulate", Color.GREEN, 0.5) # Runs together with the position tweener.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_pause_mode}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"}
**set_pause_mode**(mode:
`TweenPauseMode<enum_Tween_TweenPauseMode>`{.interpreted-text
role="ref"}) `🔗<class_Tween_method_set_pause_mode>`{.interpreted-text
role="ref"}

Determines the behavior of the **Tween** when the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"} is paused.

Default value is
`TWEEN_PAUSE_BOUND<class_Tween_constant_TWEEN_PAUSE_BOUND>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_process_mode}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"}
**set_process_mode**(mode:
`TweenProcessMode<enum_Tween_TweenProcessMode>`{.interpreted-text
role="ref"}) `🔗<class_Tween_method_set_process_mode>`{.interpreted-text
role="ref"}

Determines whether the **Tween** should run after process frames (see
`Node._process()<class_Node_private_method__process>`{.interpreted-text
role="ref"}) or physics frames (see
`Node._physics_process()<class_Node_private_method__physics_process>`{.interpreted-text
role="ref"}).

Default value is
`TWEEN_PROCESS_IDLE<class_Tween_constant_TWEEN_PROCESS_IDLE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_speed_scale}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"}
**set_speed_scale**(speed: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Tween_method_set_speed_scale>`{.interpreted-text
role="ref"}

Scales the speed of tweening. This affects all
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s and their
delays.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_set_trans}
::: rst-class
classref-method
:::
::::

`Tween<class_Tween>`{.interpreted-text role="ref"} **set_trans**(trans:
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"}) `🔗<class_Tween_method_set_trans>`{.interpreted-text
role="ref"}

Sets the default transition type for
`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}s
and `MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"}s
appended after this method.

Before this method is called, the default transition type is
`TRANS_LINEAR<class_Tween_constant_TRANS_LINEAR>`{.interpreted-text
role="ref"}.

    var tween = create_tween()
    tween.tween_property(self, "position", Vector2(300, 0), 0.5) # Uses TRANS_LINEAR.
    tween.set_trans(Tween.TRANS_SINE)
    tween.tween_property(self, "rotation_degrees", 45.0, 0.5) # Uses TRANS_SINE.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_Tween_method_stop>`{.interpreted-text role="ref"}

Stops the tweening and resets the **Tween** to its initial state. This
will not remove any appended `Tweener<class_Tweener>`{.interpreted-text
role="ref"}s.

\*\*Note:\*\* This does *not* reset targets of
`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}s
to their values when the **Tween** first started.

    var tween = create_tween()

    # Will move from 0 to 500 over 1 second.
    position.x = 0.0
    tween.tween_property(self, "position:x", 500, 1.0)

    # Will be at (about) 250 when the timer finishes.
    await get_tree().create_timer(0.5).timeout

    # Will now move from (about) 250 to 500 over 1 second,
    # thus at half the speed as before.
    tween.stop()
    tween.play()

\*\*Note:\*\* If a Tween is stopped and not bound to any node, it will
exist indefinitely until manually started or invalidated. If you lose a
reference to such Tween, you can retrieve it using
`SceneTree.get_processed_tweens()<class_SceneTree_method_get_processed_tweens>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_tween_callback}
::: rst-class
classref-method
:::
::::

`CallbackTweener<class_CallbackTweener>`{.interpreted-text role="ref"}
**tween_callback**(callback:
`Callable<class_Callable>`{.interpreted-text role="ref"})
`🔗<class_Tween_method_tween_callback>`{.interpreted-text role="ref"}

Creates and appends a
`CallbackTweener<class_CallbackTweener>`{.interpreted-text role="ref"}.
This method can be used to call an arbitrary method in any object. Use
`Callable.bind()<class_Callable_method_bind>`{.interpreted-text
role="ref"} to bind additional arguments for the call.

\*\*Example:\*\* Object that keeps shooting every 1 second:

::::: tabs
::: code-tab
gdscript

var tween = get_tree().create_tween().set_loops()
tween.tween_callback(shoot).set_delay(1.0)
:::

::: code-tab
csharp

Tween tween = GetTree().CreateTween().SetLoops();
tween.TweenCallback(Callable.From(Shoot)).SetDelay(1.0f);
:::
:::::

\*\*Example:\*\* Turning a sprite red and then blue, with 2 second
delay:

::::: tabs
::: code-tab
gdscript

var tween = get_tree().create_tween()
tween.tween_callback(\$Sprite.set_modulate.bind(Color.RED)).set_delay(2)
tween.tween_callback(\$Sprite.set_modulate.bind(Color.BLUE)).set_delay(2)
:::

::: code-tab
csharp

Tween tween = GetTree().CreateTween(); Sprite2D sprite =
GetNode\<Sprite2D\>(\"Sprite\"); tween.TweenCallback(Callable.From(()
=\> sprite.Modulate = Colors.Red)).SetDelay(2.0f);
tween.TweenCallback(Callable.From(() =\> sprite.Modulate =
Colors.Blue)).SetDelay(2.0f);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_tween_interval}
::: rst-class
classref-method
:::
::::

`IntervalTweener<class_IntervalTweener>`{.interpreted-text role="ref"}
**tween_interval**(time: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Tween_method_tween_interval>`{.interpreted-text
role="ref"}

Creates and appends an
`IntervalTweener<class_IntervalTweener>`{.interpreted-text role="ref"}.
This method can be used to create delays in the tween animation, as an
alternative to using the delay in other
`Tweener<class_Tweener>`{.interpreted-text role="ref"}s, or when
there\'s no animation (in which case the **Tween** acts as a timer).
`time` is the length of the interval, in seconds.

\*\*Example:\*\* Creating an interval in code execution:

::::: tabs
::: code-tab
gdscript

\# \... some code await create_tween().tween_interval(2).finished \#
\... more code
:::

::: code-tab
csharp

// \... some code await ToSignal(CreateTween().TweenInterval(2.0f),
Tween.SignalName.Finished); // \... more code
:::
:::::

\*\*Example:\*\* Creating an object that moves back and forth and jumps
every few seconds:

::::: tabs
::: code-tab
gdscript

var tween = create_tween().set_loops() tween.tween_property(\$Sprite,
\"position:x\", 200.0, 1.0).as_relative() tween.tween_callback(jump)
tween.tween_interval(2) tween.tween_property(\$Sprite, \"position:x\",
-200.0, 1.0).as_relative() tween.tween_callback(jump)
tween.tween_interval(2)
:::

::: code-tab
csharp

Tween tween = CreateTween().SetLoops();
tween.TweenProperty(GetNode(\"Sprite\"), \"position:x\", 200.0f,
1.0f).AsRelative(); tween.TweenCallback(Callable.From(Jump));
tween.TweenInterval(2.0f); tween.TweenProperty(GetNode(\"Sprite\"),
\"position:x\", -200.0f, 1.0f).AsRelative();
tween.TweenCallback(Callable.From(Jump)); tween.TweenInterval(2.0f);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_tween_method}
::: rst-class
classref-method
:::
::::

`MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"}
**tween_method**(method: `Callable<class_Callable>`{.interpreted-text
role="ref"}, from: `Variant<class_Variant>`{.interpreted-text
role="ref"}, to: `Variant<class_Variant>`{.interpreted-text role="ref"},
duration: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_Tween_method_tween_method>`{.interpreted-text role="ref"}

Creates and appends a
`MethodTweener<class_MethodTweener>`{.interpreted-text role="ref"}. This
method is similar to a combination of
`tween_callback()<class_Tween_method_tween_callback>`{.interpreted-text
role="ref"} and
`tween_property()<class_Tween_method_tween_property>`{.interpreted-text
role="ref"}. It calls a method over time with a tweened value provided
as an argument. The value is tweened between `from` and `to` over the
time specified by `duration`, in seconds. Use
`Callable.bind()<class_Callable_method_bind>`{.interpreted-text
role="ref"} to bind additional arguments for the call. You can use
`MethodTweener.set_ease()<class_MethodTweener_method_set_ease>`{.interpreted-text
role="ref"} and
`MethodTweener.set_trans()<class_MethodTweener_method_set_trans>`{.interpreted-text
role="ref"} to tweak the easing and transition of the value or
`MethodTweener.set_delay()<class_MethodTweener_method_set_delay>`{.interpreted-text
role="ref"} to delay the tweening.

\*\*Example:\*\* Making a 3D object look from one point to another
point:

::::: tabs
::: code-tab
gdscript

var tween = create_tween() tween.tween_method(look_at.bind(Vector3.UP),
Vector3(-1, 0, -1), Vector3(1, 0, -1), 1.0) \# The look_at() method
takes up vector as second argument.
:::

::: code-tab
csharp

Tween tween = CreateTween(); tween.TweenMethod(Callable.From((Vector3
target) =\> LookAt(target, Vector3.Up)), new Vector3(-1.0f, 0.0f,
-1.0f), new Vector3(1.0f, 0.0f, -1.0f), 1.0f); // Use lambdas to bind
additional arguments for the call.
:::
:::::

\*\*Example:\*\* Setting the text of a
`Label<class_Label>`{.interpreted-text role="ref"}, using an
intermediate method and after a delay:

::::: tabs
::: code-tab
gdscript

func [ready]{#ready}():

:   var tween = create_tween() tween.tween_method(set_label_text, 0, 10,
    1.0).set_delay(1.0)

func set_label_text(value: int):

:   \$Label.text = \"Counting \" + str(value)
:::

::: code-tab
csharp

public override void [Ready]{#ready}() { base.\_Ready();

> Tween tween = CreateTween();
> tween.TweenMethod(Callable.From\<int\>(SetLabelText), 0.0f, 10.0f,
> 1.0f).SetDelay(1.0f);

}

private void SetLabelText(int value) { GetNode\<Label\>(\"Label\").Text
= \$\"Counting {value}\"; }
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_tween_property}
::: rst-class
classref-method
:::
::::

`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
**tween_property**(object: `Object<class_Object>`{.interpreted-text
role="ref"}, property: `NodePath<class_NodePath>`{.interpreted-text
role="ref"}, final_val: `Variant<class_Variant>`{.interpreted-text
role="ref"}, duration: `float<class_float>`{.interpreted-text
role="ref"}) `🔗<class_Tween_method_tween_property>`{.interpreted-text
role="ref"}

Creates and appends a
`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}.
This method tweens a `property` of an `object` between an initial value
and `final_val` in a span of time equal to `duration`, in seconds. The
initial value by default is the property\'s value at the time the
tweening of the
`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
starts.

::::: tabs
::: code-tab
gdscript

var tween = create_tween() tween.tween_property(\$Sprite, \"position\",
Vector2(100, 200), 1.0) tween.tween_property(\$Sprite, \"position\",
Vector2(200, 300), 1.0)
:::

::: code-tab
csharp

Tween tween = CreateTween(); tween.TweenProperty(GetNode(\"Sprite\"),
\"position\", new Vector2(100.0f, 200.0f), 1.0f);
tween.TweenProperty(GetNode(\"Sprite\"), \"position\", new
Vector2(200.0f, 300.0f), 1.0f);
:::
:::::

will move the sprite to position (100, 200) and then to (200, 300). If
you use
`PropertyTweener.from()<class_PropertyTweener_method_from>`{.interpreted-text
role="ref"} or
`PropertyTweener.from_current()<class_PropertyTweener_method_from_current>`{.interpreted-text
role="ref"}, the starting position will be overwritten by the given
value instead. See other methods in
`PropertyTweener<class_PropertyTweener>`{.interpreted-text role="ref"}
to see how the tweening can be tweaked further.

\*\*Note:\*\* You can find the correct property name by hovering over
the property in the Inspector. You can also provide the components of a
property directly by using `"property:component"` (eg. `position:x`),
where it would only apply to that particular component.

\*\*Example:\*\* Moving an object twice from the same position, with
different transition types:

::::: tabs
::: code-tab
gdscript

var tween = create_tween() tween.tween_property(\$Sprite, \"position\",
Vector2.RIGHT \* 300, 1.0).as_relative().set_trans(Tween.TRANS_SINE)
tween.tween_property(\$Sprite, \"position\", Vector2.RIGHT \* 300,
1.0).as_relative().from_current().set_trans(Tween.TRANS_EXPO)
:::

::: code-tab
csharp

Tween tween = CreateTween(); tween.TweenProperty(GetNode(\"Sprite\"),
\"position\", Vector2.Right \* 300.0f,
1.0f).AsRelative().SetTrans(Tween.TransitionType.Sine);
tween.TweenProperty(GetNode(\"Sprite\"), \"position\", Vector2.Right \*
300.0f,
1.0f).AsRelative().FromCurrent().SetTrans(Tween.TransitionType.Expo);
:::
:::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Tween_method_tween_subtween}
::: rst-class
classref-method
:::
::::

`SubtweenTweener<class_SubtweenTweener>`{.interpreted-text role="ref"}
**tween_subtween**(subtween: `Tween<class_Tween>`{.interpreted-text
role="ref"}) `🔗<class_Tween_method_tween_subtween>`{.interpreted-text
role="ref"}

Creates and appends a
`SubtweenTweener<class_SubtweenTweener>`{.interpreted-text role="ref"}.
This method can be used to nest `subtween` within this **Tween**,
allowing for the creation of more complex and composable sequences.

    # Subtween will rotate the object.
    var subtween = create_tween()
    subtween.tween_property(self, "rotation_degrees", 45.0, 1.0)
    subtween.tween_property(self, "rotation_degrees", 0.0, 1.0)

    # Parent tween will execute the subtween as one of its steps.
    var tween = create_tween()
    tween.tween_property(self, "position:x", 500, 3.0)
    tween.tween_subtween(subtween)
    tween.tween_property(self, "position:x", 300, 2.0)

\*\*Note:\*\* The methods
`pause()<class_Tween_method_pause>`{.interpreted-text role="ref"},
`stop()<class_Tween_method_stop>`{.interpreted-text role="ref"}, and
`set_loops()<class_Tween_method_set_loops>`{.interpreted-text
role="ref"} can cause the parent **Tween** to get stuck on the subtween
step; see the documentation for those methods for more information.

\*\*Note:\*\* The pause and process modes set by
`set_pause_mode()<class_Tween_method_set_pause_mode>`{.interpreted-text
role="ref"} and
`set_process_mode()<class_Tween_method_set_process_mode>`{.interpreted-text
role="ref"} on `subtween` will be overridden by the parent **Tween**\'s
settings.
