github_url
:   hide

# AnimationNodeOneShot {#class_AnimationNodeOneShot}

**Inherits:**
`AnimationNodeSync<class_AnimationNodeSync>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Plays an animation once in an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource to add to an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. This animation node will execute a sub-animation and return
once it finishes. Blend times for fading in and out can be customized,
as well as filters.

After setting the request and changing the animation playback, the
one-shot node automatically clears the request on the next process frame
by setting its `request` value to
`ONE_SHOT_REQUEST_NONE<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_NONE>`{.interpreted-text
role="ref"}.

::::: tabs
::: code-tab
gdscript

\# Play child animation connected to \"shot\" port.
animation_tree.set(\"parameters/OneShot/request\",
AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE) \# Alternative syntax (same
result as above). animation_tree\[\"parameters/OneShot/request\"\] =
AnimationNodeOneShot.ONE_SHOT_REQUEST_FIRE

\# Abort child animation connected to \"shot\" port.
animation_tree.set(\"parameters/OneShot/request\",
AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT) \# Alternative syntax (same
result as above). animation_tree\[\"parameters/OneShot/request\"\] =
AnimationNodeOneShot.ONE_SHOT_REQUEST_ABORT

\# Abort child animation with fading out connected to \"shot\" port.
animation_tree.set(\"parameters/OneShot/request\",
AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT) \# Alternative syntax
(same result as above). animation_tree\[\"parameters/OneShot/request\"\]
= AnimationNodeOneShot.ONE_SHOT_REQUEST_FADE_OUT

\# Get current state (read-only).
animation_tree.get(\"parameters/OneShot/active\") \# Alternative syntax
(same result as above). animation_tree\[\"parameters/OneShot/active\"\]

\# Get current internal state (read-only).
animation_tree.get(\"parameters/OneShot/internal_active\") \#
Alternative syntax (same result as above).
animation_tree\[\"parameters/OneShot/internal_active\"\]
:::

::: code-tab
csharp

// Play child animation connected to \"shot\" port.
animationTree.Set(\"parameters/OneShot/request\",
(int)AnimationNodeOneShot.OneShotRequest.Fire);

// Abort child animation connected to \"shot\" port.
animationTree.Set(\"parameters/OneShot/request\",
(int)AnimationNodeOneShot.OneShotRequest.Abort);

// Abort child animation with fading out connected to \"shot\" port.
animationTree.Set(\"parameters/OneShot/request\",
(int)AnimationNodeOneShot.OneShotRequest.FadeOut);

// Get current state (read-only).
animationTree.Get(\"parameters/OneShot/active\");

// Get current internal state (read-only).
animationTree.Get(\"parameters/OneShot/internal_active\");
:::
:::::

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

::: rst-class
classref-reftable-group
:::

## Properties

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AnimationNodeOneShot_OneShotRequest}
::: rst-class
classref-enumeration
:::
::::

enum **OneShotRequest**:
`🔗<enum_AnimationNodeOneShot_OneShotRequest>`{.interpreted-text
role="ref"}

:::: {#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>`{.interpreted-text
role="ref"} **ONE_SHOT_REQUEST_NONE** = `0`

The default state of the request. Nothing is done.

:::: {#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE}
::: rst-class
classref-enumeration-constant
:::
::::

`OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>`{.interpreted-text
role="ref"} **ONE_SHOT_REQUEST_FIRE** = `1`

The request to play the animation connected to \"shot\" port.

:::: {#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_ABORT}
::: rst-class
classref-enumeration-constant
:::
::::

`OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>`{.interpreted-text
role="ref"} **ONE_SHOT_REQUEST_ABORT** = `2`

The request to stop the animation connected to \"shot\" port.

:::: {#class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FADE_OUT}
::: rst-class
classref-enumeration-constant
:::
::::

`OneShotRequest<enum_AnimationNodeOneShot_OneShotRequest>`{.interpreted-text
role="ref"} **ONE_SHOT_REQUEST_FADE_OUT** = `3`

The request to fade out the animation connected to \"shot\" port.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AnimationNodeOneShot_MixMode}
::: rst-class
classref-enumeration
:::
::::

enum **MixMode**:
`🔗<enum_AnimationNodeOneShot_MixMode>`{.interpreted-text role="ref"}

:::: {#class_AnimationNodeOneShot_constant_MIX_MODE_BLEND}
::: rst-class
classref-enumeration-constant
:::
::::

`MixMode<enum_AnimationNodeOneShot_MixMode>`{.interpreted-text
role="ref"} **MIX_MODE_BLEND** = `0`

Blends two animations. See also
`AnimationNodeBlend2<class_AnimationNodeBlend2>`{.interpreted-text
role="ref"}.

:::: {#class_AnimationNodeOneShot_constant_MIX_MODE_ADD}
::: rst-class
classref-enumeration-constant
:::
::::

`MixMode<enum_AnimationNodeOneShot_MixMode>`{.interpreted-text
role="ref"} **MIX_MODE_ADD** = `1`

Blends two animations additively. See also
`AnimationNodeAdd2<class_AnimationNodeAdd2>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNodeOneShot_property_autorestart}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **autorestart** =
`false`
`🔗<class_AnimationNodeOneShot_property_autorestart>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autorestart**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **has_autorestart**()

If `true`, the sub-animation will restart automatically after finishing.

In other words, to start auto restarting, the animation must be played
once with the
`ONE_SHOT_REQUEST_FIRE<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE>`{.interpreted-text
role="ref"} request. The
`ONE_SHOT_REQUEST_ABORT<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_ABORT>`{.interpreted-text
role="ref"} request stops the auto restarting, but it does not disable
the
`autorestart<class_AnimationNodeOneShot_property_autorestart>`{.interpreted-text
role="ref"} itself. So, the
`ONE_SHOT_REQUEST_FIRE<class_AnimationNodeOneShot_constant_ONE_SHOT_REQUEST_FIRE>`{.interpreted-text
role="ref"} request will start auto restarting again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_autorestart_delay}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **autorestart_delay**
= `1.0`
`🔗<class_AnimationNodeOneShot_property_autorestart_delay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autorestart_delay**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_autorestart_delay**()

The delay after which the automatic restart is triggered, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_autorestart_random_delay}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**autorestart_random_delay** = `0.0`
`🔗<class_AnimationNodeOneShot_property_autorestart_random_delay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autorestart_random_delay**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_autorestart_random_delay**()

If
`autorestart<class_AnimationNodeOneShot_property_autorestart>`{.interpreted-text
role="ref"} is `true`, a random additional delay (in seconds) between 0
and this value will be added to
`autorestart_delay<class_AnimationNodeOneShot_property_autorestart_delay>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_break_loop_at_end}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **break_loop_at_end** =
`false`
`🔗<class_AnimationNodeOneShot_property_break_loop_at_end>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_break_loop_at_end**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_loop_broken_at_end**()

If `true`, breaks the loop at the end of the loop cycle for transition,
even if the animation is looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_fadein_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **fadein_curve**
`🔗<class_AnimationNodeOneShot_property_fadein_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fadein_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_fadein_curve**()

Determines how cross-fading between animations is eased. If empty, the
transition will be linear. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_fadein_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fadein_time** =
`0.0`
`🔗<class_AnimationNodeOneShot_property_fadein_time>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fadein_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fadein_time**()

The fade-in duration. For example, setting this to `1.0` for a 5 second
length animation will produce a cross-fade that starts at 0 second and
ends at 1 second during the animation.

\*\*Note:\*\* **AnimationNodeOneShot** transitions the current state
after the fading has finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_fadeout_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **fadeout_curve**
`🔗<class_AnimationNodeOneShot_property_fadeout_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fadeout_curve**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_fadeout_curve**()

Determines how cross-fading between animations is eased. If empty, the
transition will be linear. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_fadeout_time}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fadeout_time** =
`0.0`
`🔗<class_AnimationNodeOneShot_property_fadeout_time>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fadeout_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fadeout_time**()

The fade-out duration. For example, setting this to `1.0` for a 5 second
length animation will produce a cross-fade that starts at 4 second and
ends at 5 second during the animation.

\*\*Note:\*\* **AnimationNodeOneShot** transitions the current state
after the fading has finished.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeOneShot_property_mix_mode}
::: rst-class
classref-property
:::
::::

`MixMode<enum_AnimationNodeOneShot_MixMode>`{.interpreted-text
role="ref"} **mix_mode** = `0`
`🔗<class_AnimationNodeOneShot_property_mix_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mix_mode**(value:
  `MixMode<enum_AnimationNodeOneShot_MixMode>`{.interpreted-text
  role="ref"})
- `MixMode<enum_AnimationNodeOneShot_MixMode>`{.interpreted-text
  role="ref"} **get_mix_mode**()

The blend type.
