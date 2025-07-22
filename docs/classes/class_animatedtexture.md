github_url
:   hide

# AnimatedTexture {#class_AnimatedTexture}

**Deprecated:** This class does not work properly in current versions
and may be removed in the future. There is currently no equivalent
workaround.

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Proxy texture for simple frame-based animations.

::: rst-class
classref-introduction-group
:::

## Description

**AnimatedTexture** is a resource format for frame-based animations,
where multiple textures can be chained automatically with a predefined
delay for each frame. Unlike
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
or `AnimatedSprite2D<class_AnimatedSprite2D>`{.interpreted-text
role="ref"}, it isn\'t a `Node<class_Node>`{.interpreted-text
role="ref"}, but has the advantage of being usable anywhere a
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} resource can
be used, e.g. in a `TileSet<class_TileSet>`{.interpreted-text
role="ref"}.

The playback of the animation is controlled by the
`speed_scale<class_AnimatedTexture_property_speed_scale>`{.interpreted-text
role="ref"} property, as well as each frame\'s duration (see
`set_frame_duration()<class_AnimatedTexture_method_set_frame_duration>`{.interpreted-text
role="ref"}). The animation loops, i.e. it will restart at frame 0
automatically after playing the last frame.

\*\*AnimatedTexture\*\* currently requires all frame textures to have
the same size, otherwise the bigger ones will be cropped to match the
smallest one.

\*\*Note:\*\* AnimatedTexture doesn\'t support using
`AtlasTexture<class_AtlasTexture>`{.interpreted-text role="ref"}s. Each
frame needs to be a separate
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}.

\*\*Warning:\*\* The current implementation is not efficient for the
modern renderers.

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

## Constants

:::: {#class_AnimatedTexture_constant_MAX_FRAMES}
::: rst-class
classref-constant
:::
::::

**MAX_FRAMES** = `256`
`🔗<class_AnimatedTexture_constant_MAX_FRAMES>`{.interpreted-text
role="ref"}

The maximum number of frames supported by **AnimatedTexture**. If you
need more frames in your animation, use
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
or `AnimatedSprite2D<class_AnimatedSprite2D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimatedTexture_property_current_frame}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **current_frame**
`🔗<class_AnimatedTexture_property_current_frame>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_current_frame**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_current_frame**()

Sets the currently visible frame of the texture. Setting this frame
while playing resets the current frame time, so the newly selected frame
plays for its whole configured frame duration.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedTexture_property_frames}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **frames** = `1`
`🔗<class_AnimatedTexture_property_frames>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_frames**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_frames**()

Number of frames to use in the animation. While you can create the
frames independently with
`set_frame_texture()<class_AnimatedTexture_method_set_frame_texture>`{.interpreted-text
role="ref"}, you need to set this value for the animation to take new
frames into account. The maximum number of frames is
`MAX_FRAMES<class_AnimatedTexture_constant_MAX_FRAMES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedTexture_property_one_shot}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **one_shot** = `false`
`🔗<class_AnimatedTexture_property_one_shot>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_one_shot**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_one_shot**()

If `true`, the animation will only play once and will not loop back to
the first frame after reaching the end. Note that reaching the end will
not set `pause<class_AnimatedTexture_property_pause>`{.interpreted-text
role="ref"} to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedTexture_property_pause}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **pause** = `false`
`🔗<class_AnimatedTexture_property_pause>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pause**(value: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_pause**()

If `true`, the animation will pause where it currently is (i.e. at
`current_frame<class_AnimatedTexture_property_current_frame>`{.interpreted-text
role="ref"}). The animation will continue from where it was paused when
changing this property to `false`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedTexture_property_speed_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **speed_scale** =
`1.0` `🔗<class_AnimatedTexture_property_speed_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_speed_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_speed_scale**()

The animation speed is multiplied by this value. If set to a negative
value, the animation is played in reverse.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimatedTexture_method_get_frame_duration}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_frame_duration**(frame: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimatedTexture_method_get_frame_duration>`{.interpreted-text
role="ref"}

Returns the given `frame`\'s duration, in seconds.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedTexture_method_get_frame_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_frame_texture**(frame: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimatedTexture_method_get_frame_texture>`{.interpreted-text
role="ref"}

Returns the given frame\'s
`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedTexture_method_set_frame_duration}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_frame_duration**(frame: `int<class_int>`{.interpreted-text
role="ref"}, duration: `float<class_float>`{.interpreted-text
role="ref"})
`🔗<class_AnimatedTexture_method_set_frame_duration>`{.interpreted-text
role="ref"}

Sets the duration of any given `frame`. The final duration is affected
by the
`speed_scale<class_AnimatedTexture_property_speed_scale>`{.interpreted-text
role="ref"}. If set to `0`, the frame is skipped during playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimatedTexture_method_set_frame_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_frame_texture**(frame: `int<class_int>`{.interpreted-text
role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_AnimatedTexture_method_set_frame_texture>`{.interpreted-text
role="ref"}

Assigns a `Texture2D<class_Texture2D>`{.interpreted-text role="ref"} to
the given frame. Frame IDs start at 0, so the first frame has ID 0, and
the last frame of the animation has ID
`frames<class_AnimatedTexture_property_frames>`{.interpreted-text
role="ref"} - 1.

You can define any number of textures up to
`MAX_FRAMES<class_AnimatedTexture_constant_MAX_FRAMES>`{.interpreted-text
role="ref"}, but keep in mind that only frames from 0 to
`frames<class_AnimatedTexture_property_frames>`{.interpreted-text
role="ref"} - 1 will be part of the animation.
