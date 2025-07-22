github_url
:   hide

# AnimatedSprite3D {#class_AnimatedSprite3D}

**Inherits:** `SpriteBase3D<class_SpriteBase3D>`{.interpreted-text
role="ref"} **\<**
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} **\<**
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text role="ref"}
**\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

2D sprite node in 3D world, that can use multiple 2D textures for
animation.

::: rst-class
classref-introduction-group
:::

## Description

**AnimatedSprite3D** is similar to the
`Sprite3D<class_Sprite3D>`{.interpreted-text role="ref"} node, except it
carries multiple textures as animation
`sprite_frames<class_AnimatedSprite3D_property_sprite_frames>`{.interpreted-text
role="ref"}. Animations are created using a
`SpriteFrames<class_SpriteFrames>`{.interpreted-text role="ref"}
resource, which allows you to import image files (or a folder containing
said files) to provide the animation frames for the sprite. The
`SpriteFrames<class_SpriteFrames>`{.interpreted-text role="ref"}
resource can be configured in the editor via the SpriteFrames bottom
panel.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D Sprite animation (also applies to 3D) <../tutorials/2d/2d_sprite_animation>`{.interpreted-text
  role="doc"}

::: rst-class
classref-reftable-group
:::

## Properties

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

:::: {#class_AnimatedSprite3D_signal_animation_changed}
::: rst-class
classref-signal
:::
::::

**animation_changed**()
`🔗<class_AnimatedSprite3D_signal_animation_changed>`{.interpreted-text
role="ref"}

Emitted when
`animation<class_AnimatedSprite3D_property_animation>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_signal_animation_finished}
::: rst-class
classref-signal
:::
::::

**animation_finished**()
`🔗<class_AnimatedSprite3D_signal_animation_finished>`{.interpreted-text
role="ref"}

Emitted when the animation reaches the end, or the start if it is played
in reverse. When the animation finishes, it pauses the playback.

\*\*Note:\*\* This signal is not emitted if an animation is looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_signal_animation_looped}
::: rst-class
classref-signal
:::
::::

**animation_looped**()
`🔗<class_AnimatedSprite3D_signal_animation_looped>`{.interpreted-text
role="ref"}

Emitted when the animation loops.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_signal_frame_changed}
::: rst-class
classref-signal
:::
::::

**frame_changed**()
`🔗<class_AnimatedSprite3D_signal_frame_changed>`{.interpreted-text
role="ref"}

Emitted when
`frame<class_AnimatedSprite3D_property_frame>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_signal_sprite_frames_changed}
::: rst-class
classref-signal
:::
::::

**sprite_frames_changed**()
`🔗<class_AnimatedSprite3D_signal_sprite_frames_changed>`{.interpreted-text
role="ref"}

Emitted when
`sprite_frames<class_AnimatedSprite3D_property_sprite_frames>`{.interpreted-text
role="ref"} changes.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimatedSprite3D_property_animation}
::: rst-class
classref-property
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**animation** = `&"default"`
`🔗<class_AnimatedSprite3D_property_animation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_animation**(value:
  `StringName<class_StringName>`{.interpreted-text role="ref"})
- `StringName<class_StringName>`{.interpreted-text role="ref"}
  **get_animation**()

The current animation from the
`sprite_frames<class_AnimatedSprite3D_property_sprite_frames>`{.interpreted-text
role="ref"} resource. If this value is changed, the
`frame<class_AnimatedSprite3D_property_frame>`{.interpreted-text
role="ref"} counter and the
`frame_progress<class_AnimatedSprite3D_property_frame_progress>`{.interpreted-text
role="ref"} are reset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_property_autoplay}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **autoplay** = `""`
`🔗<class_AnimatedSprite3D_property_autoplay>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_autoplay**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_autoplay**()

The key of the animation to play when the scene loads.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_property_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **frame** = `0`
`🔗<class_AnimatedSprite3D_property_frame>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frame**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_frame**()

The displayed animation frame\'s index. Setting this property also
resets
`frame_progress<class_AnimatedSprite3D_property_frame_progress>`{.interpreted-text
role="ref"}. If this is not desired, use
`set_frame_and_progress()<class_AnimatedSprite3D_method_set_frame_and_progress>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_property_frame_progress}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **frame_progress** =
`0.0`
`🔗<class_AnimatedSprite3D_property_frame_progress>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frame_progress**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_frame_progress**()

The progress value between `0.0` and `1.0` until the current frame
transitions to the next frame. If the animation is playing backwards,
the value transitions from `1.0` to `0.0`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_property_speed_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **speed_scale** =
`1.0`
`🔗<class_AnimatedSprite3D_property_speed_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_speed_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_speed_scale**()

The speed scaling ratio. For example, if this value is `1`, then the
animation plays at normal speed. If it\'s `0.5`, then it plays at half
speed. If it\'s `2`, then it plays at double speed.

If set to a negative value, the animation is played in reverse. If set
to `0`, the animation will not advance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_property_sprite_frames}
::: rst-class
classref-property
:::
::::

`SpriteFrames<class_SpriteFrames>`{.interpreted-text role="ref"}
**sprite_frames**
`🔗<class_AnimatedSprite3D_property_sprite_frames>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sprite_frames**(value:
  `SpriteFrames<class_SpriteFrames>`{.interpreted-text role="ref"})
- `SpriteFrames<class_SpriteFrames>`{.interpreted-text role="ref"}
  **get_sprite_frames**()

The `SpriteFrames<class_SpriteFrames>`{.interpreted-text role="ref"}
resource containing the animation(s). Allows you the option to load,
edit, clear, make unique and save the states of the
`SpriteFrames<class_SpriteFrames>`{.interpreted-text role="ref"}
resource.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimatedSprite3D_method_get_playing_speed}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_playing_speed**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimatedSprite3D_method_get_playing_speed>`{.interpreted-text
role="ref"}

Returns the actual playing speed of current animation or `0` if not
playing. This speed is the
`speed_scale<class_AnimatedSprite3D_property_speed_scale>`{.interpreted-text
role="ref"} property multiplied by `custom_speed` argument specified
when calling the
`play()<class_AnimatedSprite3D_method_play>`{.interpreted-text
role="ref"} method.

Returns a negative value if the current animation is playing backwards.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_method_is_playing}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_playing**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimatedSprite3D_method_is_playing>`{.interpreted-text
role="ref"}

Returns `true` if an animation is currently playing (even if
`speed_scale<class_AnimatedSprite3D_property_speed_scale>`{.interpreted-text
role="ref"} and/or `custom_speed` are `0`).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_method_pause}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **pause**()
`🔗<class_AnimatedSprite3D_method_pause>`{.interpreted-text role="ref"}

Pauses the currently playing animation. The
`frame<class_AnimatedSprite3D_property_frame>`{.interpreted-text
role="ref"} and
`frame_progress<class_AnimatedSprite3D_property_frame_progress>`{.interpreted-text
role="ref"} will be kept and calling
`play()<class_AnimatedSprite3D_method_play>`{.interpreted-text
role="ref"} or
`play_backwards()<class_AnimatedSprite3D_method_play_backwards>`{.interpreted-text
role="ref"} without arguments will resume the animation from the current
playback position.

See also `stop()<class_AnimatedSprite3D_method_stop>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_method_play}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **play**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\",
custom_speed: `float<class_float>`{.interpreted-text role="ref"} = 1.0,
from_end: `bool<class_bool>`{.interpreted-text role="ref"} = false)
`🔗<class_AnimatedSprite3D_method_play>`{.interpreted-text role="ref"}

Plays the animation with key `name`. If `custom_speed` is negative and
`from_end` is `true`, the animation will play backwards (which is
equivalent to calling
`play_backwards()<class_AnimatedSprite3D_method_play_backwards>`{.interpreted-text
role="ref"}).

If this method is called with that same animation `name`, or with no
`name` parameter, the assigned animation will resume playing if it was
paused.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_method_play_backwards}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**play_backwards**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"} = &\"\")
`🔗<class_AnimatedSprite3D_method_play_backwards>`{.interpreted-text
role="ref"}

Plays the animation with key `name` in reverse.

This method is a shorthand for
`play()<class_AnimatedSprite3D_method_play>`{.interpreted-text
role="ref"} with `custom_speed = -1.0` and `from_end = true`, so see its
description for more information.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_method_set_frame_and_progress}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_frame_and_progress**(frame: `int<class_int>`{.interpreted-text
role="ref"}, progress: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AnimatedSprite3D_method_set_frame_and_progress>`{.interpreted-text
role="ref"}

Sets `frame<class_AnimatedSprite3D_property_frame>`{.interpreted-text
role="ref"} and
`frame_progress<class_AnimatedSprite3D_property_frame_progress>`{.interpreted-text
role="ref"} to the given values. Unlike setting
`frame<class_AnimatedSprite3D_property_frame>`{.interpreted-text
role="ref"}, this method does not reset the
`frame_progress<class_AnimatedSprite3D_property_frame_progress>`{.interpreted-text
role="ref"} to `0.0` implicitly.

\*\*Example:\*\* Change the animation while keeping the same
`frame<class_AnimatedSprite3D_property_frame>`{.interpreted-text
role="ref"} and
`frame_progress<class_AnimatedSprite3D_property_frame_progress>`{.interpreted-text
role="ref"}:

:::: tabs
::: code-tab
gdscript

var current_frame = animated_sprite.get_frame() var current_progress =
animated_sprite.get_frame_progress()
animated_sprite.play(\"walk_another_skin\")
animated_sprite.set_frame_and_progress(current_frame, current_progress)
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedSprite3D_method_stop}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"} **stop**()
`🔗<class_AnimatedSprite3D_method_stop>`{.interpreted-text role="ref"}

Stops the currently playing animation. The animation position is reset
to `0` and the `custom_speed` is reset to `1.0`. See also
`pause()<class_AnimatedSprite3D_method_pause>`{.interpreted-text
role="ref"}.
