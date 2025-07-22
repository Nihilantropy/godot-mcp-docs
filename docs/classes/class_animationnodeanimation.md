github_url
:   hide

# AnimationNodeAnimation {#class_AnimationNodeAnimation}

**Inherits:**
`AnimationRootNode<class_AnimationRootNode>`{.interpreted-text
role="ref"} **\<**
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An input animation for an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A resource to add to an
`AnimationNodeBlendTree<class_AnimationNodeBlendTree>`{.interpreted-text
role="ref"}. Only has one output port using the
`animation<class_AnimationNodeAnimation_property_animation>`{.interpreted-text
role="ref"} property. Used as an input for
`AnimationNode<class_AnimationNode>`{.interpreted-text role="ref"}s that
blend animations together.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using AnimationTree <../tutorials/animation/animation_tree>`{.interpreted-text
  role="doc"}
- [3D Platformer Demo](https://godotengine.org/asset-library/asset/2748)
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

:::: {#enum_AnimationNodeAnimation_PlayMode}
::: rst-class
classref-enumeration
:::
::::

enum **PlayMode**:
`🔗<enum_AnimationNodeAnimation_PlayMode>`{.interpreted-text role="ref"}

:::: {#class_AnimationNodeAnimation_constant_PLAY_MODE_FORWARD}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayMode<enum_AnimationNodeAnimation_PlayMode>`{.interpreted-text
role="ref"} **PLAY_MODE_FORWARD** = `0`

Plays animation in forward direction.

:::: {#class_AnimationNodeAnimation_constant_PLAY_MODE_BACKWARD}
::: rst-class
classref-enumeration-constant
:::
::::

`PlayMode<enum_AnimationNodeAnimation_PlayMode>`{.interpreted-text
role="ref"} **PLAY_MODE_BACKWARD** = `1`

Plays animation in backward direction.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationNodeAnimation_property_advance_on_start}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **advance_on_start** =
`false`
`🔗<class_AnimationNodeAnimation_property_advance_on_start>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_advance_on_start**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_advance_on_start**()

If `true`, on receiving a request to play an animation from the start,
the first frame is not drawn, but only processed, and playback starts
from the next frame.

See also the notes of
`AnimationPlayer.play()<class_AnimationPlayer_method_play>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeAnimation_property_animation}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**animation** = `&""`
`🔗<class_AnimationNodeAnimation_property_animation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_animation**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_animation**()

Animation to use as an output. It is one of the animations provided by
`AnimationTree.anim_player<class_AnimationTree_property_anim_player>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeAnimation_property_loop_mode}
::: rst-class
classref-property
:::
::::

`LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
**loop_mode**
`🔗<class_AnimationNodeAnimation_property_loop_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_loop_mode**(value:
  `LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"})
- `LoopMode<enum_Animation_LoopMode>`{.interpreted-text role="ref"}
  **get_loop_mode**()

If
`use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>`{.interpreted-text
role="ref"} is `true`, override the loop settings of the original
`Animation<class_Animation>`{.interpreted-text role="ref"} resource with
the value.

\*\*Note:\*\* If the
`Animation.loop_mode<class_Animation_property_loop_mode>`{.interpreted-text
role="ref"} isn\'t set to looping, the
`Animation.track_set_interpolation_loop_wrap()<class_Animation_method_track_set_interpolation_loop_wrap>`{.interpreted-text
role="ref"} option will not be respected. If you cannot get the expected
behavior, consider duplicating the
`Animation<class_Animation>`{.interpreted-text role="ref"} resource and
changing the loop settings.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeAnimation_property_play_mode}
::: rst-class
classref-property
:::
::::

`PlayMode<enum_AnimationNodeAnimation_PlayMode>`{.interpreted-text
role="ref"} **play_mode** = `0`
`🔗<class_AnimationNodeAnimation_property_play_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_play_mode**(value:
  `PlayMode<enum_AnimationNodeAnimation_PlayMode>`{.interpreted-text
  role="ref"})
- `PlayMode<enum_AnimationNodeAnimation_PlayMode>`{.interpreted-text
  role="ref"} **get_play_mode**()

Determines the playback direction of the animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeAnimation_property_start_offset}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **start_offset**
`🔗<class_AnimationNodeAnimation_property_start_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_start_offset**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_start_offset**()

If
`use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>`{.interpreted-text
role="ref"} is `true`, offset the start position of the animation.

This is useful for adjusting which foot steps first in 3D walking
animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeAnimation_property_stretch_time_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **stretch_time_scale**
`🔗<class_AnimationNodeAnimation_property_stretch_time_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_stretch_time_scale**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_stretching_time_scale**()

If `true`, scales the time so that the length specified in
`timeline_length<class_AnimationNodeAnimation_property_timeline_length>`{.interpreted-text
role="ref"} is one cycle.

This is useful for matching the periods of walking and running
animations.

If `false`, the original animation length is respected. If you set the
loop to
`loop_mode<class_AnimationNodeAnimation_property_loop_mode>`{.interpreted-text
role="ref"}, the animation will loop in
`timeline_length<class_AnimationNodeAnimation_property_timeline_length>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeAnimation_property_timeline_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **timeline_length**
`🔗<class_AnimationNodeAnimation_property_timeline_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_timeline_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_timeline_length**()

If
`use_custom_timeline<class_AnimationNodeAnimation_property_use_custom_timeline>`{.interpreted-text
role="ref"} is `true`, offset the start position of the animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationNodeAnimation_property_use_custom_timeline}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_custom_timeline**
= `false`
`🔗<class_AnimationNodeAnimation_property_use_custom_timeline>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_custom_timeline**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_custom_timeline**()

If `true`, `AnimationNode<class_AnimationNode>`{.interpreted-text
role="ref"} provides an animation based on the
`Animation<class_Animation>`{.interpreted-text role="ref"} resource with
some parameters adjusted.
