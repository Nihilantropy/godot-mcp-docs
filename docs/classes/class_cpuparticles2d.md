github_url
:   hide

# CPUParticles2D {#class_CPUParticles2D}

**Inherits:** `Node2D<class_Node2D>`{.interpreted-text role="ref"}
**\<** `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A CPU-based 2D particle emitter.

::: rst-class
classref-introduction-group
:::

## Description

CPU-based 2D particle node used to create a variety of particle systems
and effects.

See also `GPUParticles2D<class_GPUParticles2D>`{.interpreted-text
role="ref"}, which provides the same functionality with hardware
acceleration, but may not run on older devices.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Particle systems (2D) <../tutorials/2d/particle_systems_2d>`{.interpreted-text
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

:::: {#class_CPUParticles2D_signal_finished}
::: rst-class
classref-signal
:::
::::

**finished**()
`🔗<class_CPUParticles2D_signal_finished>`{.interpreted-text role="ref"}

Emitted when all active particles have finished processing. When
`one_shot<class_CPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} is disabled, particles will process continuously, so this is
never emitted.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_CPUParticles2D_DrawOrder}
::: rst-class
classref-enumeration
:::
::::

enum **DrawOrder**:
`🔗<enum_CPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}

:::: {#class_CPUParticles2D_constant_DRAW_ORDER_INDEX}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawOrder<enum_CPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}
**DRAW_ORDER_INDEX** = `0`

Particles are drawn in the order emitted.

:::: {#class_CPUParticles2D_constant_DRAW_ORDER_LIFETIME}
::: rst-class
classref-enumeration-constant
:::
::::

`DrawOrder<enum_CPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}
**DRAW_ORDER_LIFETIME** = `1`

Particles are drawn in order of remaining lifetime. In other words, the
particle with the highest lifetime is drawn at the front.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CPUParticles2D_Parameter}
::: rst-class
classref-enumeration
:::
::::

enum **Parameter**:
`🔗<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}

:::: {#class_CPUParticles2D_constant_PARAM_INITIAL_LINEAR_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set initial velocity properties.

:::: {#class_CPUParticles2D_constant_PARAM_ANGULAR_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_ANGULAR_VELOCITY** = `1`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set angular velocity properties.

:::: {#class_CPUParticles2D_constant_PARAM_ORBIT_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_ORBIT_VELOCITY** = `2`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set orbital velocity properties.

:::: {#class_CPUParticles2D_constant_PARAM_LINEAR_ACCEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_LINEAR_ACCEL** = `3`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set linear acceleration properties.

:::: {#class_CPUParticles2D_constant_PARAM_RADIAL_ACCEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_RADIAL_ACCEL** = `4`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set radial acceleration properties.

:::: {#class_CPUParticles2D_constant_PARAM_TANGENTIAL_ACCEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_TANGENTIAL_ACCEL** = `5`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set tangential acceleration properties.

:::: {#class_CPUParticles2D_constant_PARAM_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_DAMPING** = `6`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set damping properties.

:::: {#class_CPUParticles2D_constant_PARAM_ANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_ANGLE** = `7`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set angle properties.

:::: {#class_CPUParticles2D_constant_PARAM_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_SCALE** = `8`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set scale properties.

:::: {#class_CPUParticles2D_constant_PARAM_HUE_VARIATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_HUE_VARIATION** = `9`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set hue variation properties.

:::: {#class_CPUParticles2D_constant_PARAM_ANIM_SPEED}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_ANIM_SPEED** = `10`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set animation speed properties.

:::: {#class_CPUParticles2D_constant_PARAM_ANIM_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_ANIM_OFFSET** = `11`

Use with
`set_param_min()<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_curve()<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"} to set animation offset properties.

:::: {#class_CPUParticles2D_constant_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
**PARAM_MAX** = `12`

Represents the size of the
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CPUParticles2D_ParticleFlags}
::: rst-class
classref-enumeration
:::
::::

enum **ParticleFlags**:
`🔗<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text role="ref"}

:::: {#class_CPUParticles2D_constant_PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with
`set_particle_flag()<class_CPUParticles2D_method_set_particle_flag>`{.interpreted-text
role="ref"} to set
`particle_flag_align_y<class_CPUParticles2D_property_particle_flag_align_y>`{.interpreted-text
role="ref"}.

:::: {#class_CPUParticles2D_constant_PARTICLE_FLAG_ROTATE_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_ROTATE_Y** = `1`

Present for consistency with 3D particle nodes, not used in 2D.

:::: {#class_CPUParticles2D_constant_PARTICLE_FLAG_DISABLE_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_DISABLE_Z** = `2`

Present for consistency with 3D particle nodes, not used in 2D.

:::: {#class_CPUParticles2D_constant_PARTICLE_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_MAX** = `3`

Represents the size of the
`ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_CPUParticles2D_EmissionShape}
::: rst-class
classref-enumeration
:::
::::

enum **EmissionShape**:
`🔗<enum_CPUParticles2D_EmissionShape>`{.interpreted-text role="ref"}

:::: {#class_CPUParticles2D_constant_EMISSION_SHAPE_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

:::: {#class_CPUParticles2D_constant_EMISSION_SHAPE_SPHERE}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere flattened to two
dimensions.

:::: {#class_CPUParticles2D_constant_EMISSION_SHAPE_SPHERE_SURFACE}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere flattened to two
dimensions.

:::: {#class_CPUParticles2D_constant_EMISSION_SHAPE_RECTANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_RECTANGLE** = `3`

Particles will be emitted in the area of a rectangle.

:::: {#class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position chosen randomly among
`emission_points<class_CPUParticles2D_property_emission_points>`{.interpreted-text
role="ref"}. Particle color will be modulated by
`emission_colors<class_CPUParticles2D_property_emission_colors>`{.interpreted-text
role="ref"}.

:::: {#class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position chosen randomly among
`emission_points<class_CPUParticles2D_property_emission_points>`{.interpreted-text
role="ref"}. Particle velocity and rotation will be set based on
`emission_normals<class_CPUParticles2D_property_emission_normals>`{.interpreted-text
role="ref"}. Particle color will be modulated by
`emission_colors<class_CPUParticles2D_property_emission_colors>`{.interpreted-text
role="ref"}.

:::: {#class_CPUParticles2D_constant_EMISSION_SHAPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_MAX** = `6`

Represents the size of the
`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_CPUParticles2D_property_amount}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **amount** = `8`
`🔗<class_CPUParticles2D_property_amount>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_amount**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_amount**()

Number of particles emitted in one emission cycle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_angle_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **angle_curve**
`🔗<class_CPUParticles2D_property_angle_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s rotation will be animated along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_angle_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle_max** = `0.0`
`🔗<class_CPUParticles2D_property_angle_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial rotation applied to each particle, in degrees.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_angle_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle_min** = `0.0`
`🔗<class_CPUParticles2D_property_angle_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`angle_max<class_CPUParticles2D_property_angle_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_angular_velocity_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**angular_velocity_curve**
`🔗<class_CPUParticles2D_property_angular_velocity_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s angular velocity will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_angular_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_velocity_max** = `0.0`
`🔗<class_CPUParticles2D_property_angular_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial angular velocity (rotation speed) applied to each
particle in *degrees* per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_angular_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_velocity_min** = `0.0`
`🔗<class_CPUParticles2D_property_angular_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`angular_velocity_max<class_CPUParticles2D_property_angular_velocity_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_anim_offset_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **anim_offset_curve**
`🔗<class_CPUParticles2D_property_anim_offset_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s animation offset will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_anim_offset_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_offset_max** =
`0.0`
`🔗<class_CPUParticles2D_property_anim_offset_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum animation offset that corresponds to frame index in the texture.
`0` is the first frame, `1` is the last one. See
`CanvasItemMaterial.particles_animation<class_CanvasItemMaterial_property_particles_animation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_anim_offset_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_offset_min** =
`0.0`
`🔗<class_CPUParticles2D_property_anim_offset_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`anim_offset_max<class_CPUParticles2D_property_anim_offset_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_anim_speed_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **anim_speed_curve**
`🔗<class_CPUParticles2D_property_anim_speed_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s animation speed will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_anim_speed_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_speed_max** =
`0.0`
`🔗<class_CPUParticles2D_property_anim_speed_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum particle animation speed. Animation speed of `1` means that the
particles will make full `0` to `1` offset cycle during lifetime, `2`
means `2` cycles etc.

With animation speed greater than `1`, remember to enable
`CanvasItemMaterial.particles_anim_loop<class_CanvasItemMaterial_property_particles_anim_loop>`{.interpreted-text
role="ref"} property if you want the animation to repeat.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_anim_speed_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_speed_min** =
`0.0`
`🔗<class_CPUParticles2D_property_anim_speed_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`anim_speed_max<class_CPUParticles2D_property_anim_speed_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(1, 1, 1, 1)`
`🔗<class_CPUParticles2D_property_color>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

Each particle\'s initial color. If
`texture<class_CPUParticles2D_property_texture>`{.interpreted-text
role="ref"} is defined, it will be multiplied by this color.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_color_initial_ramp}
::: rst-class
classref-property
:::
::::

`Gradient<class_Gradient>`{.interpreted-text role="ref"}
**color_initial_ramp**
`🔗<class_CPUParticles2D_property_color_initial_ramp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_initial_ramp**(value:
  `Gradient<class_Gradient>`{.interpreted-text role="ref"})
- `Gradient<class_Gradient>`{.interpreted-text role="ref"}
  **get_color_initial_ramp**()

Each particle\'s initial color will vary along this
`Gradient<class_Gradient>`{.interpreted-text role="ref"} (multiplied
with `color<class_CPUParticles2D_property_color>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_color_ramp}
::: rst-class
classref-property
:::
::::

`Gradient<class_Gradient>`{.interpreted-text role="ref"} **color_ramp**
`🔗<class_CPUParticles2D_property_color_ramp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_ramp**(value: `Gradient<class_Gradient>`{.interpreted-text
  role="ref"})
- `Gradient<class_Gradient>`{.interpreted-text role="ref"}
  **get_color_ramp**()

Each particle\'s color will vary along this
`Gradient<class_Gradient>`{.interpreted-text role="ref"} over its
lifetime (multiplied with
`color<class_CPUParticles2D_property_color>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_damping_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **damping_curve**
`🔗<class_CPUParticles2D_property_damping_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Damping will vary along this `Curve<class_Curve>`{.interpreted-text
role="ref"}. Should be a unit `Curve<class_Curve>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_damping_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **damping_max** =
`0.0` `🔗<class_CPUParticles2D_property_damping_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The maximum rate at which particles lose velocity. For example value of
`100` means that the particle will go from `100` velocity to `0` in `1`
second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_damping_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **damping_min** =
`0.0` `🔗<class_CPUParticles2D_property_damping_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`damping_max<class_CPUParticles2D_property_damping_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_direction}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **direction** =
`Vector2(1, 0)`
`🔗<class_CPUParticles2D_property_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_direction**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_direction**()

Unit vector specifying the particles\' emission direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_draw_order}
::: rst-class
classref-property
:::
::::

`DrawOrder<enum_CPUParticles2D_DrawOrder>`{.interpreted-text role="ref"}
**draw_order** = `0`
`🔗<class_CPUParticles2D_property_draw_order>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_draw_order**(value:
  `DrawOrder<enum_CPUParticles2D_DrawOrder>`{.interpreted-text
  role="ref"})
- `DrawOrder<enum_CPUParticles2D_DrawOrder>`{.interpreted-text
  role="ref"} **get_draw_order**()

Particle draw order.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_emission_colors}
::: rst-class
classref-property
:::
::::

`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
**emission_colors**
`🔗<class_CPUParticles2D_property_emission_colors>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_colors**(value:
  `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"})
- `PackedColorArray<class_PackedColorArray>`{.interpreted-text
  role="ref"} **get_emission_colors**()

Sets the `Color<class_Color>`{.interpreted-text role="ref"}s to modulate
particles by when using
`EMISSION_SHAPE_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS>`{.interpreted-text
role="ref"} or
`EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedColorArray<class_PackedColorArray>`{.interpreted-text role="ref"}
for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_emission_normals}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **emission_normals**
`🔗<class_CPUParticles2D_property_emission_normals>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_normals**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_emission_normals**()

Sets the direction the particles will be emitted in when using
`EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_emission_points}
::: rst-class
classref-property
:::
::::

`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} **emission_points**
`🔗<class_CPUParticles2D_property_emission_points>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_points**(value:
  `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"})
- `PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
  role="ref"} **get_emission_points**()

Sets the initial positions to spawn particles when using
`EMISSION_SHAPE_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_POINTS>`{.interpreted-text
role="ref"} or
`EMISSION_SHAPE_DIRECTED_POINTS<class_CPUParticles2D_constant_EMISSION_SHAPE_DIRECTED_POINTS>`{.interpreted-text
role="ref"}.

**Note:** The returned array is *copied* and any changes to it will not
update the original property value. See
`PackedVector2Array<class_PackedVector2Array>`{.interpreted-text
role="ref"} for more details.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_emission_rect_extents}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**emission_rect_extents**
`🔗<class_CPUParticles2D_property_emission_rect_extents>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_rect_extents**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_emission_rect_extents**()

The rectangle\'s extents if
`emission_shape<class_CPUParticles2D_property_emission_shape>`{.interpreted-text
role="ref"} is set to
`EMISSION_SHAPE_RECTANGLE<class_CPUParticles2D_constant_EMISSION_SHAPE_RECTANGLE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_emission_shape}
::: rst-class
classref-property
:::
::::

`EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
role="ref"} **emission_shape** = `0`
`🔗<class_CPUParticles2D_property_emission_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_shape**(value:
  `EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
  role="ref"})
- `EmissionShape<enum_CPUParticles2D_EmissionShape>`{.interpreted-text
  role="ref"} **get_emission_shape**()

Particles will be emitted inside this region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_emission_sphere_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_sphere_radius**
`🔗<class_CPUParticles2D_property_emission_sphere_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_sphere_radius**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_sphere_radius**()

The sphere\'s radius if
`emission_shape<class_CPUParticles2D_property_emission_shape>`{.interpreted-text
role="ref"} is set to
`EMISSION_SHAPE_SPHERE<class_CPUParticles2D_constant_EMISSION_SHAPE_SPHERE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_emitting}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **emitting** = `true`
`🔗<class_CPUParticles2D_property_emitting>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emitting**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_emitting**()

If `true`, particles are being emitted.
`emitting<class_CPUParticles2D_property_emitting>`{.interpreted-text
role="ref"} can be used to start and stop particles from emitting.
However, if
`one_shot<class_CPUParticles2D_property_one_shot>`{.interpreted-text
role="ref"} is `true` setting
`emitting<class_CPUParticles2D_property_emitting>`{.interpreted-text
role="ref"} to `true` will not restart the emission cycle until after
all active particles finish processing. You can use the
`finished<class_CPUParticles2D_signal_finished>`{.interpreted-text
role="ref"} signal to be notified once all active particles finish
processing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_explosiveness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **explosiveness** =
`0.0`
`🔗<class_CPUParticles2D_property_explosiveness>`{.interpreted-text
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

:::: {#class_CPUParticles2D_property_fixed_fps}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **fixed_fps** = `0`
`🔗<class_CPUParticles2D_property_fixed_fps>`{.interpreted-text
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

:::: {#class_CPUParticles2D_property_fract_delta}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **fract_delta** =
`true` `🔗<class_CPUParticles2D_property_fract_delta>`{.interpreted-text
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

:::: {#class_CPUParticles2D_property_gravity}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **gravity** =
`Vector2(0, 980)`
`🔗<class_CPUParticles2D_property_gravity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_gravity**()

Gravity applied to every particle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_hue_variation_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**hue_variation_curve**
`🔗<class_CPUParticles2D_property_hue_variation_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s hue will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_hue_variation_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **hue_variation_max**
= `0.0`
`🔗<class_CPUParticles2D_property_hue_variation_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial hue variation applied to each particle. It will shift
the particle color\'s hue.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_hue_variation_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **hue_variation_min**
= `0.0`
`🔗<class_CPUParticles2D_property_hue_variation_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`hue_variation_max<class_CPUParticles2D_property_hue_variation_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_initial_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**initial_velocity_max** = `0.0`
`🔗<class_CPUParticles2D_property_initial_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial velocity magnitude for each particle. Direction comes
from
`direction<class_CPUParticles2D_property_direction>`{.interpreted-text
role="ref"} and
`spread<class_CPUParticles2D_property_spread>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_initial_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**initial_velocity_min** = `0.0`
`🔗<class_CPUParticles2D_property_initial_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`initial_velocity_max<class_CPUParticles2D_property_initial_velocity_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_lifetime}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **lifetime** = `1.0`
`🔗<class_CPUParticles2D_property_lifetime>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lifetime**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_lifetime**()

Amount of time each particle will exist.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_lifetime_randomness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**lifetime_randomness** = `0.0`
`🔗<class_CPUParticles2D_property_lifetime_randomness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lifetime_randomness**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_lifetime_randomness**()

Particle lifetime randomness ratio.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_linear_accel_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**linear_accel_curve**
`🔗<class_CPUParticles2D_property_linear_accel_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s linear acceleration will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_linear_accel_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_accel_max**
= `0.0`
`🔗<class_CPUParticles2D_property_linear_accel_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum linear acceleration applied to each particle in the direction of
motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_linear_accel_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_accel_min**
= `0.0`
`🔗<class_CPUParticles2D_property_linear_accel_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`linear_accel_max<class_CPUParticles2D_property_linear_accel_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_local_coords}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **local_coords** =
`false`
`🔗<class_CPUParticles2D_property_local_coords>`{.interpreted-text
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
the **CPUParticles2D** node (and its parents) when it is moved or
rotated. If `false`, particles use global coordinates; they will not
move or rotate along the **CPUParticles2D** node (and its parents) when
it is moved or rotated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_one_shot}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **one_shot** = `false`
`🔗<class_CPUParticles2D_property_one_shot>`{.interpreted-text
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

:::: {#class_CPUParticles2D_property_orbit_velocity_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**orbit_velocity_curve**
`🔗<class_CPUParticles2D_property_orbit_velocity_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s orbital velocity will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_orbit_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**orbit_velocity_max** = `0.0`
`🔗<class_CPUParticles2D_property_orbit_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum orbital velocity applied to each particle. Makes the particles
circle around origin. Specified in number of full rotations around
origin per second.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_orbit_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**orbit_velocity_min** = `0.0`
`🔗<class_CPUParticles2D_property_orbit_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`orbit_velocity_max<class_CPUParticles2D_property_orbit_velocity_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_particle_flag_align_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**particle_flag_align_y** = `false`
`🔗<class_CPUParticles2D_property_particle_flag_align_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particle_flag**(particle_flag:
  `ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
  role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_particle_flag**(particle_flag:
  `ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Align Y axis of particle with the direction of its velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_preprocess}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **preprocess** =
`0.0` `🔗<class_CPUParticles2D_property_preprocess>`{.interpreted-text
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

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_radial_accel_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**radial_accel_curve**
`🔗<class_CPUParticles2D_property_radial_accel_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s radial acceleration will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_radial_accel_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radial_accel_max**
= `0.0`
`🔗<class_CPUParticles2D_property_radial_accel_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum radial acceleration applied to each particle. Makes particle
accelerate away from the origin or towards it if negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_radial_accel_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radial_accel_min**
= `0.0`
`🔗<class_CPUParticles2D_property_radial_accel_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`radial_accel_max<class_CPUParticles2D_property_radial_accel_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_randomness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **randomness** =
`0.0` `🔗<class_CPUParticles2D_property_randomness>`{.interpreted-text
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

:::: {#class_CPUParticles2D_property_scale_amount_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**scale_amount_curve**
`🔗<class_CPUParticles2D_property_scale_amount_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s scale will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_scale_amount_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **scale_amount_max**
= `1.0`
`🔗<class_CPUParticles2D_property_scale_amount_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial scale applied to each particle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_scale_amount_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **scale_amount_min**
= `1.0`
`🔗<class_CPUParticles2D_property_scale_amount_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`scale_amount_max<class_CPUParticles2D_property_scale_amount_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_scale_curve_x}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **scale_curve_x**
`🔗<class_CPUParticles2D_property_scale_curve_x>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale_curve_x**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_scale_curve_x**()

Each particle\'s horizontal scale will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

`split_scale<class_CPUParticles2D_property_split_scale>`{.interpreted-text
role="ref"} must be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_scale_curve_y}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"} **scale_curve_y**
`🔗<class_CPUParticles2D_property_scale_curve_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scale_curve_y**(value: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_scale_curve_y**()

Each particle\'s vertical scale will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

`split_scale<class_CPUParticles2D_property_split_scale>`{.interpreted-text
role="ref"} must be enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_seed}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **seed** = `0`
`🔗<class_CPUParticles2D_property_seed>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_seed**(value: `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_seed**()

Sets the random seed used by the particle system. Only effective if
`use_fixed_seed<class_CPUParticles2D_property_use_fixed_seed>`{.interpreted-text
role="ref"} is `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_speed_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **speed_scale** =
`1.0` `🔗<class_CPUParticles2D_property_speed_scale>`{.interpreted-text
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

:::: {#class_CPUParticles2D_property_split_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **split_scale** =
`false`
`🔗<class_CPUParticles2D_property_split_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_split_scale**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_split_scale**()

If `true`, the scale curve will be split into x and y components. See
`scale_curve_x<class_CPUParticles2D_property_scale_curve_x>`{.interpreted-text
role="ref"} and
`scale_curve_y<class_CPUParticles2D_property_scale_curve_y>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_spread}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spread** = `45.0`
`🔗<class_CPUParticles2D_property_spread>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_spread**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_spread**()

Each particle\'s initial direction range from `+spread` to `-spread`
degrees.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_tangential_accel_curve}
::: rst-class
classref-property
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**tangential_accel_curve**
`🔗<class_CPUParticles2D_property_tangential_accel_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text
  role="ref"})
- `Curve<class_Curve>`{.interpreted-text role="ref"}
  **get_param_curve**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s tangential acceleration will vary along this
`Curve<class_Curve>`{.interpreted-text role="ref"}. Should be a unit
`Curve<class_Curve>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_tangential_accel_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**tangential_accel_max** = `0.0`
`🔗<class_CPUParticles2D_property_tangential_accel_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum tangential acceleration applied to each particle. Tangential
acceleration is perpendicular to the particle\'s velocity giving the
particles a swirling motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_tangential_accel_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**tangential_accel_min** = `0.0`
`🔗<class_CPUParticles2D_property_tangential_accel_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`tangential_accel_max<class_CPUParticles2D_property_tangential_accel_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_CPUParticles2D_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

Particle texture. If `null`, particles will be squares.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_property_use_fixed_seed}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_fixed_seed** =
`false`
`🔗<class_CPUParticles2D_property_use_fixed_seed>`{.interpreted-text
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
`seed<class_CPUParticles2D_property_seed>`{.interpreted-text
role="ref"}. This is useful for situations where the visual outcome
should be consistent across replays, for example when using Movie Maker
mode.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CPUParticles2D_method_convert_from_particles}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**convert_from_particles**(particles:
`Node<class_Node>`{.interpreted-text role="ref"})
`🔗<class_CPUParticles2D_method_convert_from_particles>`{.interpreted-text
role="ref"}

Sets this node\'s properties to match a given
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"}
node with an assigned
`ParticleProcessMaterial<class_ParticleProcessMaterial>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_get_param_curve}
::: rst-class
classref-method
:::
::::

`Curve<class_Curve>`{.interpreted-text role="ref"}
**get_param_curve**(param:
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CPUParticles2D_method_get_param_curve>`{.interpreted-text
role="ref"}

Returns the `Curve<class_Curve>`{.interpreted-text role="ref"} of the
parameter specified by
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_get_param_max}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_param_max**(param:
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CPUParticles2D_method_get_param_max>`{.interpreted-text
role="ref"}

Returns the maximum value range for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_get_param_min}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_param_min**(param:
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CPUParticles2D_method_get_param_min>`{.interpreted-text
role="ref"}

Returns the minimum value range for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_get_particle_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_particle_flag**(particle_flag:
`ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CPUParticles2D_method_get_particle_flag>`{.interpreted-text
role="ref"}

Returns the enabled state of the given particle flag.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_request_particles_process}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**request_particles_process**(process_time:
`float<class_float>`{.interpreted-text role="ref"})
`🔗<class_CPUParticles2D_method_request_particles_process>`{.interpreted-text
role="ref"}

Requests the particles to process for extra process time during a single
frame.

Useful for particle playback, if used in combination with
`use_fixed_seed<class_CPUParticles2D_property_use_fixed_seed>`{.interpreted-text
role="ref"} or by calling
`restart()<class_CPUParticles2D_method_restart>`{.interpreted-text
role="ref"} with parameter `keep_seed` set to `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_restart}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**restart**(keep_seed: `bool<class_bool>`{.interpreted-text role="ref"}
= false) `🔗<class_CPUParticles2D_method_restart>`{.interpreted-text
role="ref"}

Restarts the particle emitter.

If `keep_seed` is `true`, the current random seed will be preserved.
Useful for seeking and playback.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_set_param_curve}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_curve**(param:
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"}, curve: `Curve<class_Curve>`{.interpreted-text role="ref"})
`🔗<class_CPUParticles2D_method_set_param_curve>`{.interpreted-text
role="ref"}

Sets the `Curve<class_Curve>`{.interpreted-text role="ref"} of the
parameter specified by
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"}. Should be a unit `Curve<class_Curve>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_set_param_max}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_max**(param:
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_CPUParticles2D_method_set_param_max>`{.interpreted-text
role="ref"}

Sets the maximum value for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_set_param_min}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_min**(param:
`Parameter<enum_CPUParticles2D_Parameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_CPUParticles2D_method_set_param_min>`{.interpreted-text
role="ref"}

Sets the minimum value for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CPUParticles2D_method_set_particle_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_particle_flag**(particle_flag:
`ParticleFlags<enum_CPUParticles2D_ParticleFlags>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_CPUParticles2D_method_set_particle_flag>`{.interpreted-text
role="ref"}

Enables or disables the given particle flag.
