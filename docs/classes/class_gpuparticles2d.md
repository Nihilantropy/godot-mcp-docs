github_url
:   hide

# GPUParticles2D {#class_GPUParticles2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A 2D particle emitter.

::: rst-class
classref-introduction-group
:::

## Description

2D particle node used to create a variety of particle systems and
effects. **GPUParticles2D** features an emitter that generates some
number of particles at a given rate.

Use the
`process_material<class_GPUParticles2D_property_process_material>`{.interpreted-text
role="ref"} property to add a
`ParticleProcessMaterial<class_ParticleProcessMaterial>`{.interpreted-text
role="ref"} to configure particle appearance and behavior.
Alternatively, you can add a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}
which will be applied to all particles.

2D particles can optionally collide with
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"},
but they don\'t collide with
`PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Particle systems (2D) <../tutorials/2d/particle_systems_2d>`{.interpreted-text
  role="doc"}
- [2D Particles Demo](https://godotengine.org/asset-library/asset/2724)
- [2D Dodge The Creeps Demo (uses GPUParticles2D for the trail behind
  the player)](https://godotengine.org/asset-library/asset/2712)

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

:::: {#class_GPUParticles2D_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**()
`🔗<class_GPUParticles2D_signal_finished>`{.interpreted-text role="ref"}

Emitted when all active particles have finished processing. To
immediately restart the emission cycle, call
`restart()<class_GPUParticles2D_method_restart>`{.interpreted-text
role="ref"}.

This signal is never emitted when
`one_shot<class_GPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} is disabled, as particles will be emitted and processed
continuously.

\*\*Note:\*\* For
`one_shot<class_GPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} emitters, due to the particles being computed on the GPU,
there may be a short period after receiving the signal during which
setting
`emitting<class_GPUParticles2D_property_emitting>`{.interpreted-text
role="ref"} to `true` will not restart the emission cycle. This delay is
avoided by instead calling
`restart()<class_GPUParticles2D_method_restart>`{.interpreted-text
role="ref"}.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_GPUParticles2D_DrawOrder}
::: rst-class
classref-enumeration
:::
::::

enum **DrawOrder**:
`🔗<enum_GPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}

:::: {#class_GPUParticles2D_constant_DRAW_ORDER_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawOrder<enum_GPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}
**DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

:::: {#class_GPUParticles2D_constant_DRAW_ORDER_LIFETIME}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawOrder<enum_GPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}
**DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the
particle with the highest lifetime is drawn at the front.

:::: {#class_GPUParticles2D_constant_DRAW_ORDER_REVERSE_LIFETIME}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawOrder<enum_GPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}
**DRAW_ORDER_REVERSE_LIFETIME** = `2`

Particles are drawn in reverse order of remaining lifetime. In other
words, the particle with the lowest lifetime is drawn at the front.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_GPUParticles2D_EmitFlags}
::: rst-class
classref-enumeration
:::
::::

enum **EmitFlags**:
`🔗<enum_GPUParticles2D_EmitFlags>`{.interpreted-text role="ref"}

:::: {#class_GPUParticles2D_constant_EMIT_FLAG_POSITION}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_GPUParticles2D_EmitFlags>`{.interpreted-text role="ref"}
**EMIT_FLAG_POSITION** = `1`

Particle starts at the specified position.

:::: {#class_GPUParticles2D_constant_EMIT_FLAG_ROTATION_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_GPUParticles2D_EmitFlags>`{.interpreted-text role="ref"}
**EMIT_FLAG_ROTATION_SCALE** = `2`

Particle starts with specified rotation and scale.

:::: {#class_GPUParticles2D_constant_EMIT_FLAG_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_GPUParticles2D_EmitFlags>`{.interpreted-text role="ref"}
**EMIT_FLAG_VELOCITY** = `4`

Particle starts with the specified velocity vector, which defines the
emission direction and speed.

:::: {#class_GPUParticles2D_constant_EMIT_FLAG_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_GPUParticles2D_EmitFlags>`{.interpreted-text role="ref"}
**EMIT_FLAG_COLOR** = `8`

Particle starts with specified color.

:::: {#class_GPUParticles2D_constant_EMIT_FLAG_CUSTOM}
::: rst-class
classref-enumeration-constant
:::
::::

`EmitFlags<enum_GPUParticles2D_EmitFlags>`{.interpreted-text role="ref"}
**EMIT_FLAG_CUSTOM** = `16`

Particle starts with specified `CUSTOM` data.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_GPUParticles2D_property_amount}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **amount** = `8`
`🔗<class_GPUParticles2D_property_amount>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_amount**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_amount**()

The number of particles to emit in one emission cycle. The effective
emission rate is `(amount * amount_ratio) / lifetime` particles per
second. Higher values will increase GPU requirements, even if not all
particles are visible at a given time or if
`amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"} is decreased.

\*\*Note:\*\* Changing this value will cause the particle system to
restart. To avoid this, change
`amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_amount_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **amount_ratio** =
`1.0` `🔗<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_amount_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_amount_ratio**()

The ratio of particles that should actually be emitted. If set to a
value lower than `1.0`, this will set the amount of emitted particles
throughout the lifetime to `amount * amount_ratio`. Unlike changing
`amount<class_GPUParticles2D_property_amount>`{.interpreted-text
role="ref"}, changing
`amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"} while emitting does not affect already-emitted particles and
doesn\'t cause the particle system to restart.
`amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"} can be used to create effects that make the number of
emitted particles vary over time.

\*\*Note:\*\* Reducing the
`amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"} has no performance benefit, since resources need to be
allocated and processed for the total
`amount<class_GPUParticles2D_property_amount>`{.interpreted-text
role="ref"} of particles regardless of the
`amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"}. If you don\'t intend to change the number of particles
emitted while the particles are emitting, make sure
`amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
role="ref"} is set to `1` and change
`amount<class_GPUParticles2D_property_amount>`{.interpreted-text
role="ref"} to your liking instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_collision_base_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**collision_base_size** = `1.0`
`🔗<class_GPUParticles2D_property_collision_base_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_base_size**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_collision_base_size**()

Multiplier for particle\'s collision radius. `1.0` corresponds to the
size of the sprite. If particles appear to sink into the ground when
colliding, increase this value. If particles appear to float when
colliding, decrease this value. Only effective if
`ParticleProcessMaterial.collision_mode<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"} is
`ParticleProcessMaterial.COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`{.interpreted-text
role="ref"} or
`ParticleProcessMaterial.COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Particles always have a spherical collision shape.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_draw_order}
::: rst-class
classref-property
:::
::::

`DrawOrder<enum_GPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}
**draw_order** = `1`
`🔗<class_GPUParticles2D_property_draw_order>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_order**(value:
  `DrawOrder<enum_GPUParticles2D_DrawOrder>`{.interpreted-text
  role="ref"})
- `DrawOrder<enum_GPUParticles2D_DrawOrder>`{.interpreted-text
  role="ref"} **get_draw_order**()

Particle draw order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_emitting}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **emitting** = `true`
`🔗<class_GPUParticles2D_property_emitting>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emitting**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_emitting**()

If `true`, particles are being emitted.
`emitting<class_GPUParticles2D_property_emitting>`{.interpreted-text
role="ref"} can be used to start and stop particles from emitting.
However, if
`one_shot<class_GPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} is `true` setting
`emitting<class_GPUParticles2D_property_emitting>`{.interpreted-text
role="ref"} to `true` will not restart the emission cycle unless all
active particles have finished processing. Use the
`finished<class_GPUParticles2D_signal_finished>`{.interpreted-text
role="ref"} signal to be notified once all active particles finish
processing.

\*\*Note:\*\* For
`one_shot<class_GPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} emitters, due to the particles being computed on the GPU,
there may be a short period after receiving the
`finished<class_GPUParticles2D_signal_finished>`{.interpreted-text
role="ref"} signal during which setting this to `true` will not restart
the emission cycle.

\*\*Tip:\*\* If your
`one_shot<class_GPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} emitter needs to immediately restart emitting particles once
`finished<class_GPUParticles2D_signal_finished>`{.interpreted-text
role="ref"} signal is received, consider calling
`restart()<class_GPUParticles2D_method_restart>`{.interpreted-text
role="ref"} instead of setting
`emitting<class_GPUParticles2D_property_emitting>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_explosiveness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **explosiveness** =
`0.0`
`🔗<class_GPUParticles2D_property_explosiveness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_explosiveness_ratio**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_explosiveness_ratio**()

How rapidly particles in an emission cycle are emitted. If greater than
`0`, there will be a gap in emissions before the next cycle begins.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_fixed_fps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fixed_fps** = `30`
`🔗<class_GPUParticles2D_property_fixed_fps>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fixed_fps**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_fixed_fps**()

The particle system\'s frame rate is fixed to a value. For example,
changing the value to 2 will make the particles render at 2 frames per
second. Note this does not slow down the simulation of the particle
system itself.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_fract_delta}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **fract_delta** =
`true` `🔗<class_GPUParticles2D_property_fract_delta>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fractional_delta**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_fractional_delta**()

If `true`, results in fractional delta calculation which has a smoother
particles display effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_interp_to_end}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **interp_to_end** =
`0.0`
`🔗<class_GPUParticles2D_property_interp_to_end>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interp_to_end**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_interp_to_end**()

Causes all the particles in this node to interpolate towards the end of
their lifetime.

\*\*Note:\*\* This only works when used with a
`ParticleProcessMaterial<class_ParticleProcessMaterial>`{.interpreted-text
role="ref"}. It needs to be manually implemented for custom process
shaders.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_interpolate}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **interpolate** =
`true` `🔗<class_GPUParticles2D_property_interpolate>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_interpolate**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_interpolate**()

Enables particle interpolation, which makes the particle movement
smoother when their
`fixed_fps<class_GPUParticles2D_property_fixed_fps>`{.interpreted-text
role="ref"} is lower than the screen refresh rate.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_lifetime}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **lifetime** = `1.0`
`🔗<class_GPUParticles2D_property_lifetime>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lifetime**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_lifetime**()

The amount of time each particle will exist (in seconds). The effective
emission rate is `(amount * amount_ratio) / lifetime` particles per
second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_local_coords}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **local_coords** =
`false`
`🔗<class_GPUParticles2D_property_local_coords>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_local_coordinates**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_local_coordinates**()

If `true`, particles use the parent node\'s coordinate space (known as
local coordinates). This will cause particles to move and rotate along
the **GPUParticles2D** node (and its parents) when it is moved or
rotated. If `false`, particles use global coordinates; they will not
move or rotate along the **GPUParticles2D** node (and its parents) when
it is moved or rotated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_one_shot}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **one_shot** = `false`
`🔗<class_GPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_one_shot**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_one_shot**()

If `true`, only one emission cycle occurs. If set `true` during a cycle,
emission will stop at the cycle\'s end.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_preprocess}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **preprocess** =
`0.0` `🔗<class_GPUParticles2D_property_preprocess>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_pre_process_time**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_pre_process_time**()

Particle system starts as if it had already run for this many seconds.

\*\*Note:\*\* This can be very expensive if set to a high number as it
requires running the particle shader a number of times equal to the
`fixed_fps<class_GPUParticles2D_property_fixed_fps>`{.interpreted-text
role="ref"} (or 30, if
`fixed_fps<class_GPUParticles2D_property_fixed_fps>`{.interpreted-text
role="ref"} is 0) for every second. In extreme cases it can even lead to
a GPU crash due to the volume of work done in a single frame.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_process_material}
::: rst-class
classref-property
:::
::::

`Material<class_Material>`{.interpreted-text role="ref"}
**process_material**
`🔗<class_GPUParticles2D_property_process_material>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_process_material**(value:
  `Material<class_Material>`{.interpreted-text role="ref"})
- `Material<class_Material>`{.interpreted-text role="ref"}
  **get_process_material**()

`Material<class_Material>`{.interpreted-text role="ref"} for processing
particles. Can be a
`ParticleProcessMaterial<class_ParticleProcessMaterial>`{.interpreted-text
role="ref"} or a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_randomness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randomness** =
`0.0` `🔗<class_GPUParticles2D_property_randomness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_randomness_ratio**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_randomness_ratio**()

Emission lifetime randomness ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_seed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **seed** = `0`
`🔗<class_GPUParticles2D_property_seed>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_seed**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_seed**()

Sets the random seed used by the particle system. Only effective if
`use_fixed_seed<class_GPUParticles2D_property_use_fixed_seed>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_speed_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **speed_scale** =
`1.0` `🔗<class_GPUParticles2D_property_speed_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_speed_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_speed_scale**()

Particle system\'s running speed scaling ratio. A value of `0` can be
used to pause the particles.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_sub_emitter}
::: rst-class
classref-property
:::
::::

`NodePath<class_NodePath>`{.interpreted-text role="ref"} **sub_emitter**
= `NodePath("")`
`🔗<class_GPUParticles2D_property_sub_emitter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sub_emitter**(value:
  `NodePath<class_NodePath>`{.interpreted-text role="ref"})
- `NodePath<class_NodePath>`{.interpreted-text role="ref"}
  **get_sub_emitter**()

Path to another **GPUParticles2D** node that will be used as a
subemitter (see
`ParticleProcessMaterial.sub_emitter_mode<class_ParticleProcessMaterial_property_sub_emitter_mode>`{.interpreted-text
role="ref"}). Subemitters can be used to achieve effects such as
fireworks, sparks on collision, bubbles popping into water drops, and
more.

\*\*Note:\*\* When
`sub_emitter<class_GPUParticles2D_property_sub_emitter>`{.interpreted-text
role="ref"} is set, the target **GPUParticles2D** node will no longer
emit particles on its own.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_GPUParticles2D_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

Particle texture. If `null`, particles will be squares with a size of
1×1 pixels.

\*\*Note:\*\* To use a flipbook texture, assign a new
`CanvasItemMaterial<class_CanvasItemMaterial>`{.interpreted-text
role="ref"} to the **GPUParticles2D**\'s
`CanvasItem.material<class_CanvasItem_property_material>`{.interpreted-text
role="ref"} property, then enable
`CanvasItemMaterial.particles_animation<class_CanvasItemMaterial_property_particles_animation>`{.interpreted-text
role="ref"} and set
`CanvasItemMaterial.particles_anim_h_frames<class_CanvasItemMaterial_property_particles_anim_h_frames>`{.interpreted-text
role="ref"},
`CanvasItemMaterial.particles_anim_v_frames<class_CanvasItemMaterial_property_particles_anim_v_frames>`{.interpreted-text
role="ref"}, and
`CanvasItemMaterial.particles_anim_loop<class_CanvasItemMaterial_property_particles_anim_loop>`{.interpreted-text
role="ref"} to match the flipbook texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_trail_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **trail_enabled** =
`false`
`🔗<class_GPUParticles2D_property_trail_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_trail_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_trail_enabled**()

If `true`, enables particle trails using a mesh skinning system.

\*\*Note:\*\* Unlike
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"},
the number of trail sections and subdivisions is set with the
`trail_sections<class_GPUParticles2D_property_trail_sections>`{.interpreted-text
role="ref"} and
`trail_section_subdivisions<class_GPUParticles2D_property_trail_section_subdivisions>`{.interpreted-text
role="ref"} properties.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_trail_lifetime}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **trail_lifetime** =
`0.3`
`🔗<class_GPUParticles2D_property_trail_lifetime>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_trail_lifetime**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_trail_lifetime**()

The amount of time the particle\'s trail should represent (in seconds).
Only effective if
`trail_enabled<class_GPUParticles2D_property_trail_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_trail_section_subdivisions}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**trail_section_subdivisions** = `4`
`🔗<class_GPUParticles2D_property_trail_section_subdivisions>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_trail_section_subdivisions**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_trail_section_subdivisions**()

The number of subdivisions to use for the particle trail rendering.
Higher values can result in smoother trail curves, at the cost of
performance due to increased mesh complexity. See also
`trail_sections<class_GPUParticles2D_property_trail_sections>`{.interpreted-text
role="ref"}. Only effective if
`trail_enabled<class_GPUParticles2D_property_trail_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_trail_sections}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **trail_sections** = `8`
`🔗<class_GPUParticles2D_property_trail_sections>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_trail_sections**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_trail_sections**()

The number of sections to use for the particle trail rendering. Higher
values can result in smoother trail curves, at the cost of performance
due to increased mesh complexity. See also
`trail_section_subdivisions<class_GPUParticles2D_property_trail_section_subdivisions>`{.interpreted-text
role="ref"}. Only effective if
`trail_enabled<class_GPUParticles2D_property_trail_enabled>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_use_fixed_seed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_fixed_seed** =
`false`
`🔗<class_GPUParticles2D_property_use_fixed_seed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_fixed_seed**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_fixed_seed**()

If `true`, particles will use the same seed for every simulation using
the seed defined in
`seed<class_GPUParticles2D_property_seed>`{.interpreted-text
role="ref"}. This is useful for situations where the visual outcome
should be consistent across replays, for example when using Movie Maker
mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_property_visibility_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **visibility_rect** =
`Rect2(-100, -100, 200, 200)`
`🔗<class_GPUParticles2D_property_visibility_rect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_visibility_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  **get_visibility_rect**()

The `Rect2<class_Rect2>`{.interpreted-text role="ref"} that determines
the node\'s region which needs to be visible on screen for the particle
system to be active.

Grow the rect if particles suddenly appear/disappear when the node
enters/exits the screen. The `Rect2<class_Rect2>`{.interpreted-text
role="ref"} can be grown via code or with the **Particles → Generate
Visibility Rect** editor tool.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_GPUParticles2D_method_capture_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **capture_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_GPUParticles2D_method_capture_rect>`{.interpreted-text
role="ref"}

Returns a rectangle containing the positions of all existing particles.

\*\*Note:\*\* When using threaded rendering this method synchronizes the
rendering thread. Calling it often may have a negative impact on
performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_method_convert_from_particles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**convert_from_particles**(particles:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_GPUParticles2D_method_convert_from_particles>`{.interpreted-text
role="ref"}

Sets this node\'s properties to match a given
`CPUParticles2D<class_CPUParticles2D>`{.interpreted-text role="ref"}
node.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_method_emit_particle}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**emit_particle**(xform:
`Transform2D<class_Transform2D>`{.interpreted-text role="ref"},
velocity: `Vector2<class_Vector2>`{.interpreted-text role="ref"}, color:
`Color<class_Color>`{.interpreted-text role="ref"}, custom:
`Color<class_Color>`{.interpreted-text role="ref"}, flags:
`int<class_int>`{.interpreted-text role="ref"})
`🔗<class_GPUParticles2D_method_emit_particle>`{.interpreted-text
role="ref"}

Emits a single particle. Whether `xform`, `velocity`, `color` and
`custom` are applied depends on the value of `flags`. See
`EmitFlags<enum_GPUParticles2D_EmitFlags>`{.interpreted-text
role="ref"}.

The default ParticleProcessMaterial will overwrite `color` and use the
contents of `custom` as `(rotation, age, animation, lifetime)`.

\*\*Note:\*\*
`emit_particle()<class_GPUParticles2D_method_emit_particle>`{.interpreted-text
role="ref"} is only supported on the Forward+ and Mobile rendering
methods, not Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_method_request_particles_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_particles_process**(process_time:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_GPUParticles2D_method_request_particles_process>`{.interpreted-text
role="ref"}

Requests the particles to process for extra process time during a single
frame.

Useful for particle playback, if used in combination with
`use_fixed_seed<class_GPUParticles2D_property_use_fixed_seed>`{.interpreted-text
role="ref"} or by calling
`restart()<class_GPUParticles2D_method_restart>`{.interpreted-text
role="ref"} with parameter `keep_seed` set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_GPUParticles2D_method_restart}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**restart**(keep_seed: `bool<class_bool>`{.interpreted-text role="ref"}
= false) `🔗<class_GPUParticles2D_method_restart>`{.interpreted-text
role="ref"}

Restarts the particle emission cycle, clearing existing particles. To
avoid particles vanishing from the viewport, wait for the
`finished<class_GPUParticles2D_signal_finished>`{.interpreted-text
role="ref"} signal before calling.

\*\*Note:\*\* The
`finished<class_GPUParticles2D_signal_finished>`{.interpreted-text
role="ref"} signal is only emitted by
`one_shot<class_GPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} emitters.

If `keep_seed` is `true`, the current random seed will be preserved.
Useful for seeking and playback.
