github_url
:   hide

# SpriteFrames {#class_SpriteFrames}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

Sprite frame library for AnimatedSprite2D and AnimatedSprite3D.

::: rst-class
classref-introduction-group
:::

## Description

Sprite frame library for an
`AnimatedSprite2D<class_AnimatedSprite2D>`{.interpreted-text role="ref"}
or `AnimatedSprite3D<class_AnimatedSprite3D>`{.interpreted-text
role="ref"} node. Contains frames and animation data for playback.

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

:::: {#class_SpriteFrames_method_add_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_animation**(anim: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`🔗<class_SpriteFrames_method_add_animation>`{.interpreted-text
role="ref"}

Adds a new `anim` animation to the library.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_add_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**add_frame**(anim: `StringName<class_StringName>`{.interpreted-text
role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"}, duration: `float<class_float>`{.interpreted-text
role="ref"} = 1.0, at_position: `int<class_int>`{.interpreted-text
role="ref"} = -1)
`🔗<class_SpriteFrames_method_add_frame>`{.interpreted-text role="ref"}

Adds a frame to the `anim` animation. If `at_position` is `-1`, the
frame will be added to the end of the animation. `duration` specifies
the relative duration, see
`get_frame_duration()<class_SpriteFrames_method_get_frame_duration>`{.interpreted-text
role="ref"} for details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_clear}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SpriteFrames_method_clear>`{.interpreted-text role="ref"}

Removes all frames from the `anim` animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_clear_all}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **clear_all**()
`🔗<class_SpriteFrames_method_clear_all>`{.interpreted-text role="ref"}

Removes all animations. An empty `default` animation will be created.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_duplicate_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**duplicate_animation**(anim_from:
`StringName<class_StringName>`{.interpreted-text role="ref"}, anim_to:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SpriteFrames_method_duplicate_animation>`{.interpreted-text
role="ref"}

Duplicates the animation `anim_from` to a new animation named `anim_to`.
Fails if `anim_to` already exists, or if `anim_from` does not exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_get_animation_loop}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_animation_loop**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteFrames_method_get_animation_loop>`{.interpreted-text
role="ref"}

Returns `true` if the given animation is configured to loop when it
finishes playing. Otherwise, returns `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_get_animation_names}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_animation_names**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteFrames_method_get_animation_names>`{.interpreted-text
role="ref"}

Returns an array containing the names associated to each animation.
Values are placed in alphabetical order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_get_animation_speed}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_animation_speed**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteFrames_method_get_animation_speed>`{.interpreted-text
role="ref"}

Returns the speed in frames per second for the `anim` animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_get_frame_count}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_frame_count**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteFrames_method_get_frame_count>`{.interpreted-text
role="ref"}

Returns the number of frames for the `anim` animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_get_frame_duration}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_frame_duration**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteFrames_method_get_frame_duration>`{.interpreted-text
role="ref"}

Returns a relative duration of the frame `idx` in the `anim` animation
(defaults to `1.0`). For example, a frame with a duration of `2.0` is
displayed twice as long as a frame with a duration of `1.0`. You can
calculate the absolute duration (in seconds) of a frame using the
following formula:

    absolute_duration = relative_duration / (animation_fps * abs(playing_speed))

In this example, `playing_speed` refers to either
`AnimatedSprite2D.get_playing_speed()<class_AnimatedSprite2D_method_get_playing_speed>`{.interpreted-text
role="ref"} or
`AnimatedSprite3D.get_playing_speed()<class_AnimatedSprite3D_method_get_playing_speed>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_get_frame_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_frame_texture**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"}, idx:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteFrames_method_get_frame_texture>`{.interpreted-text
role="ref"}

Returns the texture of the frame `idx` in the `anim` animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_has_animation}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_animation**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_SpriteFrames_method_has_animation>`{.interpreted-text
role="ref"}

Returns `true` if the `anim` animation exists.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_remove_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_animation**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SpriteFrames_method_remove_animation>`{.interpreted-text
role="ref"}

Removes the `anim` animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_remove_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_frame**(anim: `StringName<class_StringName>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"})
`🔗<class_SpriteFrames_method_remove_frame>`{.interpreted-text
role="ref"}

Removes the `anim` animation\'s frame `idx`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_rename_animation}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_animation**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"}, newname:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_SpriteFrames_method_rename_animation>`{.interpreted-text
role="ref"}

Changes the `anim` animation\'s name to `newname`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_set_animation_loop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_animation_loop**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"}, loop:
`bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_SpriteFrames_method_set_animation_loop>`{.interpreted-text
role="ref"}

If `loop` is `true`, the `anim` animation will loop when it reaches the
end, or the start if it is played in reverse.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_set_animation_speed}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_animation_speed**(anim:
`StringName<class_StringName>`{.interpreted-text role="ref"}, fps:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_SpriteFrames_method_set_animation_speed>`{.interpreted-text
role="ref"}

Sets the speed for the `anim` animation in frames per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpriteFrames_method_set_frame}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_frame**(anim: `StringName<class_StringName>`{.interpreted-text
role="ref"}, idx: `int<class_int>`{.interpreted-text role="ref"},
texture: `Texture2D<class_Texture2D>`{.interpreted-text role="ref"},
duration: `float<class_float>`{.interpreted-text role="ref"} = 1.0)
`🔗<class_SpriteFrames_method_set_frame>`{.interpreted-text role="ref"}

Sets the `texture` and the `duration` of the frame `idx` in the `anim`
animation. `duration` specifies the relative duration, see
`get_frame_duration()<class_SpriteFrames_method_get_frame_duration>`{.interpreted-text
role="ref"} for details.
