github_url
:   hide

# AnimationMixer {#class_AnimationMixer}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"},
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}

Base class for
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
and `AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

Base class for
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}
and `AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}
to manage animation lists. It also has general properties and methods
for playback and blending.

After instantiating the playback information data within the extended
class, the blending is processed by the **AnimationMixer**.

::: rst-class
classref-introduction-group
:::

## Tutorials

- [Migrating Animations from Godot 4.0 to
  4.3](https://godotengine.org/article/migrating-animations-from-godot-4-0-to-4-3/)

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

:::: {#class_AnimationMixer_signal_animation_finished}
::: rst-class
classref-signal
:::
::::

**animation_finished**(anim_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationMixer_signal_animation_finished>`{.interpreted-text
role="ref"}

Notifies when an animation finished playing.

\*\*Note:\*\* This signal is not emitted if an animation is looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_signal_animation_libraries_updated}
::: rst-class
classref-signal
:::
::::

**animation_libraries_updated**()
`🔗<class_AnimationMixer_signal_animation_libraries_updated>`{.interpreted-text
role="ref"}

Notifies when the animation libraries have changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_signal_animation_list_changed}
::: rst-class
classref-signal
:::
::::

**animation_list_changed**()
`🔗<class_AnimationMixer_signal_animation_list_changed>`{.interpreted-text
role="ref"}

Notifies when an animation list is changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_signal_animation_started}
::: rst-class
classref-signal
:::
::::

**animation_started**(anim_name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationMixer_signal_animation_started>`{.interpreted-text
role="ref"}

Notifies when an animation starts playing.

\*\*Note:\*\* This signal is not emitted if an animation is looping.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_signal_caches_cleared}
::: rst-class
classref-signal
:::
::::

**caches_cleared**()
`🔗<class_AnimationMixer_signal_caches_cleared>`{.interpreted-text
role="ref"}

Notifies when the caches have been cleared, either automatically, or
manually via
`clear_caches()<class_AnimationMixer_method_clear_caches>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_signal_mixer_applied}
::: rst-class
classref-signal
:::
::::

**mixer_applied**()
`🔗<class_AnimationMixer_signal_mixer_applied>`{.interpreted-text
role="ref"}

Notifies when the blending result related have been applied to the
target objects.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_signal_mixer_updated}
::: rst-class
classref-signal
:::
::::

**mixer_updated**()
`🔗<class_AnimationMixer_signal_mixer_updated>`{.interpreted-text
role="ref"}

Notifies when the property related process have been updated.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_AnimationMixer_AnimationCallbackModeProcess}
::: rst-class
classref-enumeration
:::
::::

enum **AnimationCallbackModeProcess**:
`🔗<enum_AnimationMixer_AnimationCallbackModeProcess>`{.interpreted-text
role="ref"}

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_PROCESS_PHYSICS** = `0`

Process animation during physics frames (see
`Node.NOTIFICATION_INTERNAL_PHYSICS_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PHYSICS_PROCESS>`{.interpreted-text
role="ref"}). This is especially useful when animating physics bodies.

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_IDLE}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_PROCESS_IDLE** = `1`

Process animation during process frames (see
`Node.NOTIFICATION_INTERNAL_PROCESS<class_Node_constant_NOTIFICATION_INTERNAL_PROCESS>`{.interpreted-text
role="ref"}).

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_PROCESS_MANUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_PROCESS_MANUAL** = `2`

Do not process animation. Use
`advance()<class_AnimationMixer_method_advance>`{.interpreted-text
role="ref"} to process the animation manually.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AnimationMixer_AnimationCallbackModeMethod}
::: rst-class
classref-enumeration
:::
::::

enum **AnimationCallbackModeMethod**:
`🔗<enum_AnimationMixer_AnimationCallbackModeMethod>`{.interpreted-text
role="ref"}

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_METHOD_DEFERRED}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_METHOD_DEFERRED** = `0`

Batch method calls during the animation process, then do the calls after
events are processed. This avoids bugs involving deleting nodes or
modifying the AnimationPlayer while playing.

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_METHOD_IMMEDIATE** = `1`

Make method calls immediately when reached in the animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_AnimationMixer_AnimationCallbackModeDiscrete}
::: rst-class
classref-enumeration
:::
::::

enum **AnimationCallbackModeDiscrete**:
`🔗<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
role="ref"}

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_DOMINANT}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_DISCRETE_DOMINANT** = `0`

An
`Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>`{.interpreted-text
role="ref"} track value takes precedence when blending
`Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>`{.interpreted-text
role="ref"} or
`Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>`{.interpreted-text
role="ref"} track values and
`Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>`{.interpreted-text
role="ref"} track values.

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE** = `1`

An
`Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>`{.interpreted-text
role="ref"} or
`Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>`{.interpreted-text
role="ref"} track value takes precedence when blending the
`Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>`{.interpreted-text
role="ref"} or
`Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>`{.interpreted-text
role="ref"} track values and the
`Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>`{.interpreted-text
role="ref"} track values. This is the default behavior for
`AnimationPlayer<class_AnimationPlayer>`{.interpreted-text role="ref"}.

:::: {#class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS}
::: rst-class
classref-enumeration-constant
:::
::::

`AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
role="ref"} **ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS** = `2`

Always treat the
`Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>`{.interpreted-text
role="ref"} track value as
`Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>`{.interpreted-text
role="ref"} with
`Animation.INTERPOLATION_NEAREST<class_Animation_constant_INTERPOLATION_NEAREST>`{.interpreted-text
role="ref"}. This is the default behavior for
`AnimationTree<class_AnimationTree>`{.interpreted-text role="ref"}.

If a value track has un-interpolatable type key values, it is internally
converted to use
`ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_RECESSIVE>`{.interpreted-text
role="ref"} with
`Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>`{.interpreted-text
role="ref"}.

Un-interpolatable type list:

- `@GlobalScope.TYPE_NIL<class_@GlobalScope_constant_TYPE_NIL>`{.interpreted-text
  role="ref"}
- `@GlobalScope.TYPE_NODE_PATH<class_@GlobalScope_constant_TYPE_NODE_PATH>`{.interpreted-text
  role="ref"}
- `@GlobalScope.TYPE_RID<class_@GlobalScope_constant_TYPE_RID>`{.interpreted-text
  role="ref"}
- `@GlobalScope.TYPE_OBJECT<class_@GlobalScope_constant_TYPE_OBJECT>`{.interpreted-text
  role="ref"}
- `@GlobalScope.TYPE_CALLABLE<class_@GlobalScope_constant_TYPE_CALLABLE>`{.interpreted-text
  role="ref"}
- `@GlobalScope.TYPE_SIGNAL<class_@GlobalScope_constant_TYPE_SIGNAL>`{.interpreted-text
  role="ref"}
- `@GlobalScope.TYPE_DICTIONARY<class_@GlobalScope_constant_TYPE_DICTIONARY>`{.interpreted-text
  role="ref"}
- `@GlobalScope.TYPE_PACKED_BYTE_ARRAY<class_@GlobalScope_constant_TYPE_PACKED_BYTE_ARRAY>`{.interpreted-text
  role="ref"}

`@GlobalScope.TYPE_BOOL<class_@GlobalScope_constant_TYPE_BOOL>`{.interpreted-text
role="ref"} and
`@GlobalScope.TYPE_INT<class_@GlobalScope_constant_TYPE_INT>`{.interpreted-text
role="ref"} are treated as
`@GlobalScope.TYPE_FLOAT<class_@GlobalScope_constant_TYPE_FLOAT>`{.interpreted-text
role="ref"} during blending and rounded when the result is retrieved.

It is same for arrays and vectors with them such as
`@GlobalScope.TYPE_PACKED_INT32_ARRAY<class_@GlobalScope_constant_TYPE_PACKED_INT32_ARRAY>`{.interpreted-text
role="ref"} or
`@GlobalScope.TYPE_VECTOR2I<class_@GlobalScope_constant_TYPE_VECTOR2I>`{.interpreted-text
role="ref"}, they are treated as
`@GlobalScope.TYPE_PACKED_FLOAT32_ARRAY<class_@GlobalScope_constant_TYPE_PACKED_FLOAT32_ARRAY>`{.interpreted-text
role="ref"} or
`@GlobalScope.TYPE_VECTOR2<class_@GlobalScope_constant_TYPE_VECTOR2>`{.interpreted-text
role="ref"}. Also note that for arrays, the size is also interpolated.

`@GlobalScope.TYPE_STRING<class_@GlobalScope_constant_TYPE_STRING>`{.interpreted-text
role="ref"} and
`@GlobalScope.TYPE_STRING_NAME<class_@GlobalScope_constant_TYPE_STRING_NAME>`{.interpreted-text
role="ref"} are interpolated between character codes and lengths, but
note that there is a difference in algorithm between interpolation
between keys and interpolation by blending.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_AnimationMixer_property_active}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **active** = `true`
`🔗<class_AnimationMixer_property_active>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_active**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_active**()

If `true`, the **AnimationMixer** will be processing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_audio_max_polyphony}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **audio_max_polyphony** =
`32`
`🔗<class_AnimationMixer_property_audio_max_polyphony>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_audio_max_polyphony**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_audio_max_polyphony**()

The number of possible simultaneous sounds for each of the assigned
AudioStreamPlayers.

For example, if this value is `32` and the animation has two audio
tracks, the two
`AudioStreamPlayer<class_AudioStreamPlayer>`{.interpreted-text
role="ref"}s assigned can play simultaneously up to `32` voices each.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_callback_mode_discrete}
::: rst-class
classref-property
:::
::::

`AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
role="ref"} **callback_mode_discrete** = `1`
`🔗<class_AnimationMixer_property_callback_mode_discrete>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_callback_mode_discrete**(value:
  `AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
  role="ref"})
- `AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
  role="ref"} **get_callback_mode_discrete**()

Ordinarily, tracks can be set to
`Animation.UPDATE_DISCRETE<class_Animation_constant_UPDATE_DISCRETE>`{.interpreted-text
role="ref"} to update infrequently, usually when using nearest
interpolation.

However, when blending with
`Animation.UPDATE_CONTINUOUS<class_Animation_constant_UPDATE_CONTINUOUS>`{.interpreted-text
role="ref"} several results are considered. The
`callback_mode_discrete<class_AnimationMixer_property_callback_mode_discrete>`{.interpreted-text
role="ref"} specify it explicitly. See also
`AnimationCallbackModeDiscrete<enum_AnimationMixer_AnimationCallbackModeDiscrete>`{.interpreted-text
role="ref"}.

To make the blended results look good, it is recommended to set this to
`ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS<class_AnimationMixer_constant_ANIMATION_CALLBACK_MODE_DISCRETE_FORCE_CONTINUOUS>`{.interpreted-text
role="ref"} to update every frame during blending. Other values exist
for compatibility and they are fine if there is no blending, but not so,
may produce artifacts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_callback_mode_method}
::: rst-class
classref-property
:::
::::

`AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>`{.interpreted-text
role="ref"} **callback_mode_method** = `0`
`🔗<class_AnimationMixer_property_callback_mode_method>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_callback_mode_method**(value:
  `AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>`{.interpreted-text
  role="ref"})
- `AnimationCallbackModeMethod<enum_AnimationMixer_AnimationCallbackModeMethod>`{.interpreted-text
  role="ref"} **get_callback_mode_method**()

The call mode used for \"Call Method\" tracks.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_callback_mode_process}
::: rst-class
classref-property
:::
::::

`AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>`{.interpreted-text
role="ref"} **callback_mode_process** = `1`
`🔗<class_AnimationMixer_property_callback_mode_process>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_callback_mode_process**(value:
  `AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>`{.interpreted-text
  role="ref"})
- `AnimationCallbackModeProcess<enum_AnimationMixer_AnimationCallbackModeProcess>`{.interpreted-text
  role="ref"} **get_callback_mode_process**()

The process notification in which to update animations.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_deterministic}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **deterministic** =
`false`
`🔗<class_AnimationMixer_property_deterministic>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_deterministic**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_deterministic**()

If `true`, the blending uses the deterministic algorithm. The total
weight is not normalized and the result is accumulated with an initial
value (`0` or a `"RESET"` animation if present).

This means that if the total amount of blending is `0.0`, the result is
equal to the `"RESET"` animation.

If the number of tracks between the blended animations is different, the
animation with the missing track is treated as if it had the initial
value.

If `false`, The blend does not use the deterministic algorithm. The
total weight is normalized and always `1.0`. If the number of tracks
between the blended animations is different, nothing is done about the
animation that is missing a track.

\*\*Note:\*\* In `AnimationTree<class_AnimationTree>`{.interpreted-text
role="ref"}, the blending with
`AnimationNodeAdd2<class_AnimationNodeAdd2>`{.interpreted-text
role="ref"},
`AnimationNodeAdd3<class_AnimationNodeAdd3>`{.interpreted-text
role="ref"},
`AnimationNodeSub2<class_AnimationNodeSub2>`{.interpreted-text
role="ref"} or the weight greater than `1.0` may produce unexpected
results.

For example, if
`AnimationNodeAdd2<class_AnimationNodeAdd2>`{.interpreted-text
role="ref"} blends two nodes with the amount `1.0`, then total weight is
`2.0` but it will be normalized to make the total amount `1.0` and the
result will be equal to
`AnimationNodeBlend2<class_AnimationNodeBlend2>`{.interpreted-text
role="ref"} with the amount `0.5`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_reset_on_save}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **reset_on_save** =
`true`
`🔗<class_AnimationMixer_property_reset_on_save>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_reset_on_save_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_reset_on_save_enabled**()

This is used by the editor. If set to `true`, the scene will be saved
with the effects of the reset animation (the animation with the key
`"RESET"`) applied as if it had been seeked to time 0, with the editor
keeping the values that the scene had before saving.

This makes it more convenient to preview and edit animations in the
editor, as changes to the scene will not be saved as long as they are
set in the reset animation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_root_motion_local}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **root_motion_local** =
`false`
`🔗<class_AnimationMixer_property_root_motion_local>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_motion_local**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_root_motion_local**()

If `true`,
`get_root_motion_position()<class_AnimationMixer_method_get_root_motion_position>`{.interpreted-text
role="ref"} value is extracted as a local translation value before
blending. In other words, it is treated like the translation is done
after the rotation.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_root_motion_track}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"}
**root_motion_track** = `NodePath("")`
`🔗<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_motion_track**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_root_motion_track**()

The path to the Animation track used for root motion. Paths must be
valid scene-tree paths to a node, and must be specified starting from
the parent node of the node that will reproduce the animation. The
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} uses the same format as
`Animation.track_set_path()<class_Animation_method_track_set_path>`{.interpreted-text
role="ref"}, but note that a bone must be specified.

If the track has type
`Animation.TYPE_POSITION_3D<class_Animation_constant_TYPE_POSITION_3D>`{.interpreted-text
role="ref"},
`Animation.TYPE_ROTATION_3D<class_Animation_constant_TYPE_ROTATION_3D>`{.interpreted-text
role="ref"}, or
`Animation.TYPE_SCALE_3D<class_Animation_constant_TYPE_SCALE_3D>`{.interpreted-text
role="ref"} the transformation will be canceled visually, and the
animation will appear to stay in place. See also
`get_root_motion_position()<class_AnimationMixer_method_get_root_motion_position>`{.interpreted-text
role="ref"},
`get_root_motion_rotation()<class_AnimationMixer_method_get_root_motion_rotation>`{.interpreted-text
role="ref"},
`get_root_motion_scale()<class_AnimationMixer_method_get_root_motion_scale>`{.interpreted-text
role="ref"}, and
`RootMotionView<class_RootMotionView>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_property_root_node}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **root_node** =
`NodePath("..")`
`🔗<class_AnimationMixer_property_root_node>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_root_node**(value: `NodePath<class_NodePath>`{.interpreted-text
  role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_root_node**()

The node which node path references will travel from.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_AnimationMixer_private_method__post_process_key_value}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**\_post_process_key_value**(animation:
`Animation<class_Animation>`{.interpreted-text role="ref"}, track:
`int<class_int>`{.interpreted-text role="ref"}, value:
`Variant<class_Variant>`{.interpreted-text role="ref"}, object_id:
`int<class_int>`{.interpreted-text role="ref"}, object_sub_idx:
`int<class_int>`{.interpreted-text role="ref"})
`virtual (This method should typically be overridden by the user to have any effect.)`{.interpreted-text
role="abbr"}
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_private_method__post_process_key_value>`{.interpreted-text
role="ref"}

A virtual function for processing after getting a key during playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_add_animation_library}
::: rst-class
classref-method
:::
::::

`Error<enum_@GlobalScope_Error>`{.interpreted-text role="ref"}
**add_animation_library**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, library:
`AnimationLibrary<class_AnimationLibrary>`{.interpreted-text
role="ref"})
`🔗<class_AnimationMixer_method_add_animation_library>`{.interpreted-text
role="ref"}

Adds `library` to the animation player, under the key `name`.

AnimationMixer has a global library by default with an empty string as
key. For adding an animation to the global library:

:::: tabs
::: code-tab
gdscript

var global_library = mixer.get_animation_library(\"\")
global_library.add_animation(\"animation_name\", animation_resource)
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_advance}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**advance**(delta: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_AnimationMixer_method_advance>`{.interpreted-text role="ref"}

Manually advance the animations by the specified time (in seconds).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_capture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**capture**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"}, duration: `float<class_float>`{.interpreted-text
role="ref"}, trans_type:
`TransitionType<enum_Tween_TransitionType>`{.interpreted-text
role="ref"} = 0, ease_type:
`EaseType<enum_Tween_EaseType>`{.interpreted-text role="ref"} = 0)
`🔗<class_AnimationMixer_method_capture>`{.interpreted-text role="ref"}

If the animation track specified by `name` has an option
`Animation.UPDATE_CAPTURE<class_Animation_constant_UPDATE_CAPTURE>`{.interpreted-text
role="ref"}, stores current values of the objects indicated by the track
path as a cache. If there is already a captured cache, the old cache is
discarded.

After this it will interpolate with current animation blending result
during the playback process for the time specified by `duration`,
working like a crossfade.

You can specify `trans_type` as the curve for the interpolation. For
better results, it may be appropriate to specify
`Tween.TRANS_LINEAR<class_Tween_constant_TRANS_LINEAR>`{.interpreted-text
role="ref"} for cases where the first key of the track begins with a
non-zero value or where the key value does not change, and
`Tween.TRANS_QUAD<class_Tween_constant_TRANS_QUAD>`{.interpreted-text
role="ref"} for cases where the key value changes linearly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_clear_caches}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**clear_caches**()
`🔗<class_AnimationMixer_method_clear_caches>`{.interpreted-text
role="ref"}

**AnimationMixer** caches animated nodes. It may not notice if a node
disappears;
`clear_caches()<class_AnimationMixer_method_clear_caches>`{.interpreted-text
role="ref"} forces it to update the cache again.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_find_animation}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**find_animation**(animation:
`Animation<class_Animation>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_find_animation>`{.interpreted-text
role="ref"}

Returns the key of `animation` or an empty
`StringName<class_StringName>`{.interpreted-text role="ref"} if not
found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_find_animation_library}
::: rst-class
classref-method
:::
::::

`StringName<class_StringName>`{.interpreted-text role="ref"}
**find_animation_library**(animation:
`Animation<class_Animation>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_find_animation_library>`{.interpreted-text
role="ref"}

Returns the key for the
`AnimationLibrary<class_AnimationLibrary>`{.interpreted-text role="ref"}
that contains `animation` or an empty
`StringName<class_StringName>`{.interpreted-text role="ref"} if not
found.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_animation}
::: rst-class
classref-method
:::
::::

`Animation<class_Animation>`{.interpreted-text role="ref"}
**get_animation**(name: `StringName<class_StringName>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_animation>`{.interpreted-text
role="ref"}

Returns the `Animation<class_Animation>`{.interpreted-text role="ref"}
with the key `name`. If the animation does not exist, `null` is returned
and an error is logged.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_animation_library}
::: rst-class
classref-method
:::
::::

`AnimationLibrary<class_AnimationLibrary>`{.interpreted-text role="ref"}
**get_animation_library**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_animation_library>`{.interpreted-text
role="ref"}

Returns the first
`AnimationLibrary<class_AnimationLibrary>`{.interpreted-text role="ref"}
with key `name` or `null` if not found.

To get the **AnimationMixer**\'s global animation library, use
`get_animation_library("")`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_animation_library_list}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`StringName<class_StringName>`{.interpreted-text
role="ref"}\] **get_animation_library_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_animation_library_list>`{.interpreted-text
role="ref"}

Returns the list of stored library keys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_animation_list}
::: rst-class
classref-method
:::
::::

`PackedStringArray<class_PackedStringArray>`{.interpreted-text
role="ref"} **get_animation_list**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_animation_list>`{.interpreted-text
role="ref"}

Returns the list of stored animation keys.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_root_motion_position}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_root_motion_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_root_motion_position>`{.interpreted-text
role="ref"}

Retrieve the motion delta of position with the
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} as a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
that can be used elsewhere.

If
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} is not a path to a track of type
`Animation.TYPE_POSITION_3D<class_Animation_constant_TYPE_POSITION_3D>`{.interpreted-text
role="ref"}, returns `Vector3(0, 0, 0)`.

See also
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} and `RootMotionView<class_RootMotionView>`{.interpreted-text
role="ref"}.

The most basic example is applying position to
`CharacterBody3D<class_CharacterBody3D>`{.interpreted-text role="ref"}:

:::: tabs
::: code-tab
gdscript

var current_rotation

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   current_rotation = get_quaternion()
        state_machine.travel(\"Animate\")

    var velocity = current_rotation \*
    animation_tree.get_root_motion_position() / delta
    set_velocity(velocity) move_and_slide()
:::
::::

By using this in combination with
`get_root_motion_rotation_accumulator()<class_AnimationMixer_method_get_root_motion_rotation_accumulator>`{.interpreted-text
role="ref"}, you can apply the root motion position more correctly to
account for the rotation of the node.

:::: tabs
::: code-tab
gdscript

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   state_machine.travel(\"Animate\")

    set_quaternion(get_quaternion() \*
    animation_tree.get_root_motion_rotation()) var velocity =
    (animation_tree.get_root_motion_rotation_accumulator().inverse() \*
    get_quaternion()) \* animation_tree.get_root_motion_position() /
    delta set_velocity(velocity) move_and_slide()
:::
::::

If
`root_motion_local<class_AnimationMixer_property_root_motion_local>`{.interpreted-text
role="ref"} is `true`, returns the pre-multiplied translation value with
the inverted rotation.

In this case, the code can be written as follows:

:::: tabs
::: code-tab
gdscript

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   state_machine.travel(\"Animate\")

    set_quaternion(get_quaternion() \*
    animation_tree.get_root_motion_rotation()) var velocity =
    get_quaternion() \* animation_tree.get_root_motion_position() /
    delta set_velocity(velocity) move_and_slide()
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_root_motion_position_accumulator}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_root_motion_position_accumulator**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_root_motion_position_accumulator>`{.interpreted-text
role="ref"}

Retrieve the blended value of the position tracks with the
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} as a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
that can be used elsewhere.

This is useful in cases where you want to respect the initial key values
of the animation.

For example, if an animation with only one key `Vector3(0, 0, 0)` is
played in the previous frame and then an animation with only one key
`Vector3(1, 0, 1)` is played in the next frame, the difference can be
calculated as follows:

:::: tabs
::: code-tab
gdscript

var prev_root_motion_position_accumulator

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   state_machine.travel(\"Animate\")

    var current_root_motion_position_accumulator =
    animation_tree.get_root_motion_position_accumulator() var difference
    = current_root_motion_position_accumulator -
    prev_root_motion_position_accumulator
    prev_root_motion_position_accumulator =
    current_root_motion_position_accumulator transform.origin +=
    difference
:::
::::

However, if the animation loops, an unintended discrete change may
occur, so this is only useful for some simple use cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_root_motion_rotation}
::: rst-class
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**get_root_motion_rotation**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_root_motion_rotation>`{.interpreted-text
role="ref"}

Retrieve the motion delta of rotation with the
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} as a `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"} that can be used elsewhere.

If
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} is not a path to a track of type
`Animation.TYPE_ROTATION_3D<class_Animation_constant_TYPE_ROTATION_3D>`{.interpreted-text
role="ref"}, returns `Quaternion(0, 0, 0, 1)`.

See also
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} and `RootMotionView<class_RootMotionView>`{.interpreted-text
role="ref"}.

The most basic example is applying rotation to
`CharacterBody3D<class_CharacterBody3D>`{.interpreted-text role="ref"}:

:::: tabs
::: code-tab
gdscript

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   state_machine.travel(\"Animate\")

    set_quaternion(get_quaternion() \*
    animation_tree.get_root_motion_rotation())
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_root_motion_rotation_accumulator}
::: rst-class
classref-method
:::
::::

`Quaternion<class_Quaternion>`{.interpreted-text role="ref"}
**get_root_motion_rotation_accumulator**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_root_motion_rotation_accumulator>`{.interpreted-text
role="ref"}

Retrieve the blended value of the rotation tracks with the
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} as a `Quaternion<class_Quaternion>`{.interpreted-text
role="ref"} that can be used elsewhere.

This is necessary to apply the root motion position correctly, taking
rotation into account. See also
`get_root_motion_position()<class_AnimationMixer_method_get_root_motion_position>`{.interpreted-text
role="ref"}.

Also, this is useful in cases where you want to respect the initial key
values of the animation.

For example, if an animation with only one key `Quaternion(0, 0, 0, 1)`
is played in the previous frame and then an animation with only one key
`Quaternion(0, 0.707, 0, 0.707)` is played in the next frame, the
difference can be calculated as follows:

:::: tabs
::: code-tab
gdscript

var prev_root_motion_rotation_accumulator

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   state_machine.travel(\"Animate\")

    var current_root_motion_rotation_accumulator =
    animation_tree.get_root_motion_rotation_accumulator() var difference
    = prev_root_motion_rotation_accumulator.inverse() \*
    current_root_motion_rotation_accumulator
    prev_root_motion_rotation_accumulator =
    current_root_motion_rotation_accumulator transform.basis \*=
    Basis(difference)
:::
::::

However, if the animation loops, an unintended discrete change may
occur, so this is only useful for some simple use cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_root_motion_scale}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_root_motion_scale**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_root_motion_scale>`{.interpreted-text
role="ref"}

Retrieve the motion delta of scale with the
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} as a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
that can be used elsewhere.

If
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} is not a path to a track of type
`Animation.TYPE_SCALE_3D<class_Animation_constant_TYPE_SCALE_3D>`{.interpreted-text
role="ref"}, returns `Vector3(0, 0, 0)`.

See also
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} and `RootMotionView<class_RootMotionView>`{.interpreted-text
role="ref"}.

The most basic example is applying scale to
`CharacterBody3D<class_CharacterBody3D>`{.interpreted-text role="ref"}:

:::: tabs
::: code-tab
gdscript

var current_scale = Vector3(1, 1, 1) var scale_accum = Vector3(1, 1, 1)

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   current_scale = get_scale() scale_accum = Vector3(1, 1, 1)
        state_machine.travel(\"Animate\")

    scale_accum += animation_tree.get_root_motion_scale()
    set_scale(current_scale \* scale_accum)
:::
::::

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_get_root_motion_scale_accumulator}
::: rst-class
classref-method
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**get_root_motion_scale_accumulator**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_get_root_motion_scale_accumulator>`{.interpreted-text
role="ref"}

Retrieve the blended value of the scale tracks with the
`root_motion_track<class_AnimationMixer_property_root_motion_track>`{.interpreted-text
role="ref"} as a `Vector3<class_Vector3>`{.interpreted-text role="ref"}
that can be used elsewhere.

For example, if an animation with only one key `Vector3(1, 1, 1)` is
played in the previous frame and then an animation with only one key
`Vector3(2, 2, 2)` is played in the next frame, the difference can be
calculated as follows:

:::: tabs
::: code-tab
gdscript

var prev_root_motion_scale_accumulator

func [process]{#process}(delta):

:   

    if Input.is_action_just_pressed(\"animate\"):

    :   state_machine.travel(\"Animate\")

    var current_root_motion_scale_accumulator =
    animation_tree.get_root_motion_scale_accumulator() var difference =
    current_root_motion_scale_accumulator -
    prev_root_motion_scale_accumulator
    prev_root_motion_scale_accumulator =
    current_root_motion_scale_accumulator transform.basis =
    transform.basis.scaled(difference)
:::
::::

However, if the animation loops, an unintended discrete change may
occur, so this is only useful for some simple use cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_has_animation}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **has_animation**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_has_animation>`{.interpreted-text
role="ref"}

Returns `true` if the **AnimationMixer** stores an
`Animation<class_Animation>`{.interpreted-text role="ref"} with key
`name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_has_animation_library}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**has_animation_library**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_AnimationMixer_method_has_animation_library>`{.interpreted-text
role="ref"}

Returns `true` if the **AnimationMixer** stores an
`AnimationLibrary<class_AnimationLibrary>`{.interpreted-text role="ref"}
with key `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_remove_animation_library}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**remove_animation_library**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationMixer_method_remove_animation_library>`{.interpreted-text
role="ref"}

Removes the `AnimationLibrary<class_AnimationLibrary>`{.interpreted-text
role="ref"} associated with the key `name`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_AnimationMixer_method_rename_animation_library}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**rename_animation_library**(name:
`StringName<class_StringName>`{.interpreted-text role="ref"}, newname:
`StringName<class_StringName>`{.interpreted-text role="ref"})
`🔗<class_AnimationMixer_method_rename_animation_library>`{.interpreted-text
role="ref"}

Moves the `AnimationLibrary<class_AnimationLibrary>`{.interpreted-text
role="ref"} associated with the key `name` to the key `newname`.
