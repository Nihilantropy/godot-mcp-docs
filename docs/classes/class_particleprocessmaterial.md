github_url
:   hide

# ParticleProcessMaterial {#class_ParticleProcessMaterial}

**Inherits:** `Material<class_Material>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Holds a particle configuration for
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"} or
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes.

::: rst-class
classref-introduction-group
:::

## Description

**ParticleProcessMaterial** defines particle properties and behavior. It
is used in the `process_material` of the
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"} and
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
nodes. Some of this material\'s properties are applied to each particle
when emitted, while others can have a
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} or a
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"} applied to vary numerical or color values over the lifetime
of the particle.

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

:::: {#class_ParticleProcessMaterial_signal_emission_shape_changed}
::: rst-class
classref-signal
:::
::::

**emission_shape_changed**()
`🔗<class_ParticleProcessMaterial_signal_emission_shape_changed>`{.interpreted-text
role="ref"}

Emitted when this material\'s emission shape is changed in any way. This
includes changes to
`emission_shape<class_ParticleProcessMaterial_property_emission_shape>`{.interpreted-text
role="ref"},
`emission_shape_scale<class_ParticleProcessMaterial_property_emission_shape_scale>`{.interpreted-text
role="ref"}, or
`emission_sphere_radius<class_ParticleProcessMaterial_property_emission_sphere_radius>`{.interpreted-text
role="ref"}, and any other property that affects the emission shape\'s
offset, size, scale, or orientation.

\*\*Note:\*\* This signal is only emitted inside the editor for
performance reasons.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_ParticleProcessMaterial_Parameter}
::: rst-class
classref-enumeration
:::
::::

enum **Parameter**:
`🔗<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"}

:::: {#class_ParticleProcessMaterial_constant_PARAM_INITIAL_LINEAR_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_INITIAL_LINEAR_VELOCITY** = `0`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set initial velocity properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_ANGULAR_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_ANGULAR_VELOCITY** = `1`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set angular velocity properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_ORBIT_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_ORBIT_VELOCITY** = `2`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set orbital velocity properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_LINEAR_ACCEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_LINEAR_ACCEL** = `3`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set linear acceleration properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_RADIAL_ACCEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_RADIAL_ACCEL** = `4`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set radial acceleration properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_TANGENTIAL_ACCEL}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_TANGENTIAL_ACCEL** = `5`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set tangential acceleration properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_DAMPING}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_DAMPING** = `6`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set damping properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_ANGLE}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_ANGLE** = `7`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set angle properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_SCALE}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_SCALE** = `8`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set scale properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_HUE_VARIATION}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_HUE_VARIATION** = `9`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set hue variation properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_ANIM_SPEED}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_ANIM_SPEED** = `10`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set animation speed properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_ANIM_OFFSET}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_ANIM_OFFSET** = `11`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set animation offset properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_RADIAL_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_RADIAL_VELOCITY** = `15`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set radial velocity properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_DIRECTIONAL_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_DIRECTIONAL_VELOCITY** = `16`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set directional velocity properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_SCALE_OVER_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_SCALE_OVER_VELOCITY** = `17`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"},
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}, and
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set scale over velocity properties.

:::: {#class_ParticleProcessMaterial_constant_PARAM_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_MAX** = `18`

Represents the size of the
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} enum.

:::: {#class_ParticleProcessMaterial_constant_PARAM_TURB_VEL_INFLUENCE}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_TURB_VEL_INFLUENCE** = `13`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"} and
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"} to set the turbulence minimum und maximum influence on each
particles velocity.

:::: {#class_ParticleProcessMaterial_constant_PARAM_TURB_INIT_DISPLACEMENT}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_TURB_INIT_DISPLACEMENT** = `14`

Use with
`set_param_min()<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"} and
`set_param_max()<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"} to set the turbulence minimum and maximum displacement of
the particles spawn position.

:::: {#class_ParticleProcessMaterial_constant_PARAM_TURB_INFLUENCE_OVER_LIFE}
::: rst-class
classref-enumeration-constant
:::
::::

`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"} **PARAM_TURB_INFLUENCE_OVER_LIFE** = `12`

Use with
`set_param_texture()<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"} to set the turbulence influence over the particles life
time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ParticleProcessMaterial_ParticleFlags}
::: rst-class
classref-enumeration
:::
::::

enum **ParticleFlags**:
`🔗<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"}

:::: {#class_ParticleProcessMaterial_constant_PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_ALIGN_Y_TO_VELOCITY** = `0`

Use with
`set_particle_flag()<class_ParticleProcessMaterial_method_set_particle_flag>`{.interpreted-text
role="ref"} to set
`particle_flag_align_y<class_ParticleProcessMaterial_property_particle_flag_align_y>`{.interpreted-text
role="ref"}.

:::: {#class_ParticleProcessMaterial_constant_PARTICLE_FLAG_ROTATE_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_ROTATE_Y** = `1`

Use with
`set_particle_flag()<class_ParticleProcessMaterial_method_set_particle_flag>`{.interpreted-text
role="ref"} to set
`particle_flag_rotate_y<class_ParticleProcessMaterial_property_particle_flag_rotate_y>`{.interpreted-text
role="ref"}.

:::: {#class_ParticleProcessMaterial_constant_PARTICLE_FLAG_DISABLE_Z}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_DISABLE_Z** = `2`

Use with
`set_particle_flag()<class_ParticleProcessMaterial_method_set_particle_flag>`{.interpreted-text
role="ref"} to set
`particle_flag_disable_z<class_ParticleProcessMaterial_property_particle_flag_disable_z>`{.interpreted-text
role="ref"}.

:::: {#class_ParticleProcessMaterial_constant_PARTICLE_FLAG_DAMPING_AS_FRICTION}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_DAMPING_AS_FRICTION** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_ParticleProcessMaterial_constant_PARTICLE_FLAG_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"} **PARTICLE_FLAG_MAX** = `4`

Represents the size of the
`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ParticleProcessMaterial_EmissionShape}
::: rst-class
classref-enumeration
:::
::::

enum **EmissionShape**:
`🔗<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"}

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINT}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_POINT** = `0`

All particles will be emitted from a single point.

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_SPHERE}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_SPHERE** = `1`

Particles will be emitted in the volume of a sphere.

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_SPHERE_SURFACE}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_SPHERE_SURFACE** = `2`

Particles will be emitted on the surface of a sphere.

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_BOX}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_BOX** = `3`

Particles will be emitted in the volume of a box.

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_POINTS** = `4`

Particles will be emitted at a position determined by sampling a random
point on the
`emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`{.interpreted-text
role="ref"}. Particle color will be modulated by
`emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>`{.interpreted-text
role="ref"}.

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_DIRECTED_POINTS** = `5`

Particles will be emitted at a position determined by sampling a random
point on the
`emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`{.interpreted-text
role="ref"}. Particle velocity and rotation will be set based on
`emission_normal_texture<class_ParticleProcessMaterial_property_emission_normal_texture>`{.interpreted-text
role="ref"}. Particle color will be modulated by
`emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>`{.interpreted-text
role="ref"}.

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_RING** = `6`

Particles will be emitted in a ring or cylinder.

:::: {#class_ParticleProcessMaterial_constant_EMISSION_SHAPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **EMISSION_SHAPE_MAX** = `7`

Represents the size of the
`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ParticleProcessMaterial_SubEmitterMode}
::: rst-class
classref-enumeration
:::
::::

enum **SubEmitterMode**:
`🔗<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"}

:::: {#class_ParticleProcessMaterial_constant_SUB_EMITTER_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} **SUB_EMITTER_DISABLED** = `0`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_ParticleProcessMaterial_constant_SUB_EMITTER_CONSTANT}
::: rst-class
classref-enumeration-constant
:::
::::

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} **SUB_EMITTER_CONSTANT** = `1`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_ParticleProcessMaterial_constant_SUB_EMITTER_AT_END}
::: rst-class
classref-enumeration-constant
:::
::::

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} **SUB_EMITTER_AT_END** = `2`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_ParticleProcessMaterial_constant_SUB_EMITTER_AT_COLLISION}
::: rst-class
classref-enumeration-constant
:::
::::

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} **SUB_EMITTER_AT_COLLISION** = `3`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_ParticleProcessMaterial_constant_SUB_EMITTER_AT_START}
::: rst-class
classref-enumeration-constant
:::
::::

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} **SUB_EMITTER_AT_START** = `4`

::: {.container .contribute}
There is currently no description for this enum. Please help us by
`contributing one <doc_updating_the_class_reference>`{.interpreted-text
role="ref"}!
:::

:::: {#class_ParticleProcessMaterial_constant_SUB_EMITTER_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} **SUB_EMITTER_MAX** = `5`

Represents the size of the
`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_ParticleProcessMaterial_CollisionMode}
::: rst-class
classref-enumeration
:::
::::

enum **CollisionMode**:
`🔗<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
role="ref"}

:::: {#class_ParticleProcessMaterial_constant_COLLISION_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
role="ref"} **COLLISION_DISABLED** = `0`

No collision for particles. Particles will go through
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} nodes.

:::: {#class_ParticleProcessMaterial_constant_COLLISION_RIGID}
::: rst-class
classref-enumeration-constant
:::
::::

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
role="ref"} **COLLISION_RIGID** = `1`

`RigidBody3D<class_RigidBody3D>`{.interpreted-text role="ref"}-style
collision for particles using
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} nodes.

:::: {#class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT}
::: rst-class
classref-enumeration-constant
:::
::::

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
role="ref"} **COLLISION_HIDE_ON_CONTACT** = `2`

Hide particles instantly when colliding with a
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} node. This can be combined with a subemitter that uses the
`COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`{.interpreted-text
role="ref"} collision mode to \"replace\" the parent particle with the
subemitter on impact.

:::: {#class_ParticleProcessMaterial_constant_COLLISION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
role="ref"} **COLLISION_MAX** = `3`

Represents the size of the
`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_ParticleProcessMaterial_property_alpha_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**alpha_curve**
`🔗<class_ParticleProcessMaterial_property_alpha_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_curve**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_alpha_curve**()

The alpha value of each particle\'s color will be multiplied by this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} over
its lifetime.

\*\*Note:\*\*
`alpha_curve<class_ParticleProcessMaterial_property_alpha_curve>`{.interpreted-text
role="ref"} multiplies the particle mesh\'s vertex colors. To have a
visible effect on a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} *must* be `true`. For a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
`ALBEDO *= COLOR.rgb;` must be inserted in the shader\'s `fragment()`
function. Otherwise,
`alpha_curve<class_ParticleProcessMaterial_property_alpha_curve>`{.interpreted-text
role="ref"} will have no visible effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_angle_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**angle_curve**
`🔗<class_ParticleProcessMaterial_property_angle_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s rotation will be animated along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_angle_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_angle_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial rotation applied to each particle, in degrees.

Only applied when
`particle_flag_disable_z<class_ParticleProcessMaterial_property_particle_flag_disable_z>`{.interpreted-text
role="ref"} or
`particle_flag_rotate_y<class_ParticleProcessMaterial_property_particle_flag_rotate_y>`{.interpreted-text
role="ref"} are `true` or the
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
being used to draw the particle is using
`BaseMaterial3D.BILLBOARD_PARTICLES<class_BaseMaterial3D_constant_BILLBOARD_PARTICLES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_angle_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **angle_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_angle_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`angle_max<class_ParticleProcessMaterial_property_angle_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_angular_velocity_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**angular_velocity_curve**
`🔗<class_ParticleProcessMaterial_property_angular_velocity_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s angular velocity (rotation speed) will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} over
its lifetime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_angular_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_velocity_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_angular_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial angular velocity (rotation speed) applied to each
particle in *degrees* per second.

Only applied when
`particle_flag_disable_z<class_ParticleProcessMaterial_property_particle_flag_disable_z>`{.interpreted-text
role="ref"} or
`particle_flag_rotate_y<class_ParticleProcessMaterial_property_particle_flag_rotate_y>`{.interpreted-text
role="ref"} are `true` or the
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
being used to draw the particle is using
`BaseMaterial3D.BILLBOARD_PARTICLES<class_BaseMaterial3D_constant_BILLBOARD_PARTICLES>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_angular_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**angular_velocity_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_angular_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`angular_velocity_max<class_ParticleProcessMaterial_property_angular_velocity_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_anim_offset_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**anim_offset_curve**
`🔗<class_ParticleProcessMaterial_property_anim_offset_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s animation offset will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_anim_offset_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_offset_max** =
`0.0`
`🔗<class_ParticleProcessMaterial_property_anim_offset_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
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

:::: {#class_ParticleProcessMaterial_property_anim_offset_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_offset_min** =
`0.0`
`🔗<class_ParticleProcessMaterial_property_anim_offset_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`anim_offset_max<class_ParticleProcessMaterial_property_anim_offset_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_anim_speed_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**anim_speed_curve**
`🔗<class_ParticleProcessMaterial_property_anim_speed_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s animation speed will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_anim_speed_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_speed_max** =
`0.0`
`🔗<class_ParticleProcessMaterial_property_anim_speed_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
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

:::: {#class_ParticleProcessMaterial_property_anim_speed_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **anim_speed_min** =
`0.0`
`🔗<class_ParticleProcessMaterial_property_anim_speed_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`anim_speed_max<class_ParticleProcessMaterial_property_anim_speed_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_attractor_interaction_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**attractor_interaction_enabled** = `true`
`🔗<class_ParticleProcessMaterial_property_attractor_interaction_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attractor_interaction_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_attractor_interaction_enabled**()

If `true`, interaction with particle attractors is enabled. In 3D,
attraction only occurs within the area defined by the
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
node\'s
`GPUParticles3D.visibility_aabb<class_GPUParticles3D_property_visibility_aabb>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_collision_bounce}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **collision_bounce**
`🔗<class_ParticleProcessMaterial_property_collision_bounce>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_bounce**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_collision_bounce**()

The particles\' bounciness. Values range from `0` (no bounce) to `1`
(full bounciness). Only effective if
`collision_mode<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"} is
`COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_collision_friction}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**collision_friction**
`🔗<class_ParticleProcessMaterial_property_collision_friction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_friction**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_collision_friction**()

The particles\' friction. Values range from `0` (frictionless) to `1`
(maximum friction). Only effective if
`collision_mode<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"} is
`COLLISION_RIGID<class_ParticleProcessMaterial_constant_COLLISION_RIGID>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_collision_mode}
::: rst-class
classref-property
:::
::::

`CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
role="ref"} **collision_mode** = `0`
`🔗<class_ParticleProcessMaterial_property_collision_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_mode**(value:
  `CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
  role="ref"})
- `CollisionMode<enum_ParticleProcessMaterial_CollisionMode>`{.interpreted-text
  role="ref"} **get_collision_mode**()

The particles\' collision mode.

\*\*Note:\*\* 3D Particles can only collide with
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} nodes, not
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
nodes. To make particles collide with various objects, you can add
`GPUParticlesCollision3D<class_GPUParticlesCollision3D>`{.interpreted-text
role="ref"} nodes as children of
`PhysicsBody3D<class_PhysicsBody3D>`{.interpreted-text role="ref"}
nodes. In 3D, collisions only occur within the area defined by the
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
node\'s
`GPUParticles3D.visibility_aabb<class_GPUParticles3D_property_visibility_aabb>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* 2D Particles can only collide with
`LightOccluder2D<class_LightOccluder2D>`{.interpreted-text role="ref"}
nodes, not `PhysicsBody2D<class_PhysicsBody2D>`{.interpreted-text
role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_collision_use_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **collision_use_scale**
= `false`
`🔗<class_ParticleProcessMaterial_property_collision_use_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_collision_use_scale**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_collision_using_scale**()

If `true`,
`GPUParticles3D.collision_base_size<class_GPUParticles3D_property_collision_base_size>`{.interpreted-text
role="ref"} is multiplied by the particle\'s effective scale (see
`scale_min<class_ParticleProcessMaterial_property_scale_min>`{.interpreted-text
role="ref"},
`scale_max<class_ParticleProcessMaterial_property_scale_max>`{.interpreted-text
role="ref"},
`scale_curve<class_ParticleProcessMaterial_property_scale_curve>`{.interpreted-text
role="ref"}, and
`scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **color** =
`Color(1, 1, 1, 1)`
`🔗<class_ParticleProcessMaterial_property_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"} **get_color**()

Each particle\'s initial color. If the
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"}\'s
`texture` is defined, it will be multiplied by this color.

\*\*Note:\*\*
`color<class_ParticleProcessMaterial_property_color>`{.interpreted-text
role="ref"} multiplies the particle mesh\'s vertex colors. To have a
visible effect on a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} *must* be `true`. For a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
`ALBEDO *= COLOR.rgb;` must be inserted in the shader\'s `fragment()`
function. Otherwise,
`color<class_ParticleProcessMaterial_property_color>`{.interpreted-text
role="ref"} will have no visible effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_color_initial_ramp}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**color_initial_ramp**
`🔗<class_ParticleProcessMaterial_property_color_initial_ramp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_initial_ramp**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_color_initial_ramp**()

Each particle\'s initial color will vary along this
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"} (multiplied with
`color<class_ParticleProcessMaterial_property_color>`{.interpreted-text
role="ref"}).

\*\*Note:\*\*
`color_initial_ramp<class_ParticleProcessMaterial_property_color_initial_ramp>`{.interpreted-text
role="ref"} multiplies the particle mesh\'s vertex colors. To have a
visible effect on a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} *must* be `true`. For a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
`ALBEDO *= COLOR.rgb;` must be inserted in the shader\'s `fragment()`
function. Otherwise,
`color_initial_ramp<class_ParticleProcessMaterial_property_color_initial_ramp>`{.interpreted-text
role="ref"} will have no visible effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_color_ramp}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**color_ramp**
`🔗<class_ParticleProcessMaterial_property_color_ramp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_ramp**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_color_ramp**()

Each particle\'s color will vary along this
`GradientTexture1D<class_GradientTexture1D>`{.interpreted-text
role="ref"} over its lifetime (multiplied with
`color<class_ParticleProcessMaterial_property_color>`{.interpreted-text
role="ref"}).

\*\*Note:\*\*
`color_ramp<class_ParticleProcessMaterial_property_color_ramp>`{.interpreted-text
role="ref"} multiplies the particle mesh\'s vertex colors. To have a
visible effect on a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} *must* be `true`. For a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
`ALBEDO *= COLOR.rgb;` must be inserted in the shader\'s `fragment()`
function. Otherwise,
`color_ramp<class_ParticleProcessMaterial_property_color_ramp>`{.interpreted-text
role="ref"} will have no visible effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_damping_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**damping_curve**
`🔗<class_ParticleProcessMaterial_property_damping_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Damping will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_damping_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **damping_max** =
`0.0`
`🔗<class_ParticleProcessMaterial_property_damping_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
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

:::: {#class_ParticleProcessMaterial_property_damping_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **damping_min** =
`0.0`
`🔗<class_ParticleProcessMaterial_property_damping_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`damping_max<class_ParticleProcessMaterial_property_damping_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_direction}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **direction** =
`Vector3(1, 0, 0)`
`🔗<class_ParticleProcessMaterial_property_direction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_direction**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_direction**()

Unit vector specifying the particles\' emission direction.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_directional_velocity_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**directional_velocity_curve**
`🔗<class_ParticleProcessMaterial_property_directional_velocity_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A curve that specifies the velocity along each of the axes of the
particle system along its lifetime.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_directional_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_velocity_max**
`🔗<class_ParticleProcessMaterial_property_directional_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum directional velocity value, which is multiplied by
`directional_velocity_curve<class_ParticleProcessMaterial_property_directional_velocity_curve>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_directional_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_velocity_min**
`🔗<class_ParticleProcessMaterial_property_directional_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum directional velocity value, which is multiplied by
`directional_velocity_curve<class_ParticleProcessMaterial_property_directional_velocity_curve>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_box_extents}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**emission_box_extents**
`🔗<class_ParticleProcessMaterial_property_emission_box_extents>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_box_extents**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_emission_box_extents**()

The box\'s extents if
`emission_shape<class_ParticleProcessMaterial_property_emission_shape>`{.interpreted-text
role="ref"} is set to
`EMISSION_SHAPE_BOX<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_BOX>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`emission_box_extents<class_ParticleProcessMaterial_property_emission_box_extents>`{.interpreted-text
role="ref"} starts from the center point and applies the X, Y, and Z
values in both directions. The size is twice the area of the extents.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_color_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**emission_color_texture**
`🔗<class_ParticleProcessMaterial_property_emission_color_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_color_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_emission_color_texture**()

Particle color will be modulated by color determined by sampling this
texture at the same point as the
`emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`{.interpreted-text
role="ref"}.

\*\*Note:\*\*
`emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>`{.interpreted-text
role="ref"} multiplies the particle mesh\'s vertex colors. To have a
visible effect on a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} *must* be `true`. For a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
`ALBEDO *= COLOR.rgb;` must be inserted in the shader\'s `fragment()`
function. Otherwise,
`emission_color_texture<class_ParticleProcessMaterial_property_emission_color_texture>`{.interpreted-text
role="ref"} will have no visible effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**emission_curve**
`🔗<class_ParticleProcessMaterial_property_emission_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_curve**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_emission_curve**()

Each particle\'s color will be multiplied by this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} over
its lifetime.

\*\*Note:\*\*
`emission_curve<class_ParticleProcessMaterial_property_emission_curve>`{.interpreted-text
role="ref"} multiplies the particle mesh\'s vertex colors. To have a
visible effect on a
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"},
`BaseMaterial3D.vertex_color_use_as_albedo<class_BaseMaterial3D_property_vertex_color_use_as_albedo>`{.interpreted-text
role="ref"} *must* be `true`. For a
`ShaderMaterial<class_ShaderMaterial>`{.interpreted-text role="ref"},
`ALBEDO *= COLOR.rgb;` must be inserted in the shader\'s `fragment()`
function. Otherwise,
`emission_curve<class_ParticleProcessMaterial_property_emission_curve>`{.interpreted-text
role="ref"} will have no visible effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_normal_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**emission_normal_texture**
`🔗<class_ParticleProcessMaterial_property_emission_normal_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_normal_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_emission_normal_texture**()

Particle velocity and rotation will be set by sampling this texture at
the same point as the
`emission_point_texture<class_ParticleProcessMaterial_property_emission_point_texture>`{.interpreted-text
role="ref"}. Used only in
`EMISSION_SHAPE_DIRECTED_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS>`{.interpreted-text
role="ref"}. Can be created automatically from mesh or node by selecting
\"Create Emission Points from Mesh/Node\" under the \"Particles\" tool
in the toolbar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_point_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **emission_point_count**
`🔗<class_ParticleProcessMaterial_property_emission_point_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_point_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_emission_point_count**()

The number of emission points if
`emission_shape<class_ParticleProcessMaterial_property_emission_shape>`{.interpreted-text
role="ref"} is set to
`EMISSION_SHAPE_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS>`{.interpreted-text
role="ref"} or
`EMISSION_SHAPE_DIRECTED_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_point_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**emission_point_texture**
`🔗<class_ParticleProcessMaterial_property_emission_point_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_point_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_emission_point_texture**()

Particles will be emitted at positions determined by sampling this
texture at a random position. Used with
`EMISSION_SHAPE_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_POINTS>`{.interpreted-text
role="ref"} and
`EMISSION_SHAPE_DIRECTED_POINTS<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_DIRECTED_POINTS>`{.interpreted-text
role="ref"}. Can be created automatically from mesh or node by selecting
\"Create Emission Points from Mesh/Node\" under the \"Particles\" tool
in the toolbar.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_ring_axis}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**emission_ring_axis**
`🔗<class_ParticleProcessMaterial_property_emission_ring_axis>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_ring_axis**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_emission_ring_axis**()

The axis of the ring when using the emitter
`EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_ring_cone_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_ring_cone_angle**
`🔗<class_ParticleProcessMaterial_property_emission_ring_cone_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_ring_cone_angle**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_ring_cone_angle**()

The angle of the cone when using the emitter
`EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`{.interpreted-text
role="ref"}. The default angle of 90 degrees results in a ring, while an
angle of 0 degrees results in a cone. Intermediate values will result in
a ring where one end is larger than the other.

\*\*Note:\*\* Depending on
`emission_ring_height<class_ParticleProcessMaterial_property_emission_ring_height>`{.interpreted-text
role="ref"}, the angle may be clamped if the ring\'s end is reached to
form a perfect cone.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_ring_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_ring_height**
`🔗<class_ParticleProcessMaterial_property_emission_ring_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_ring_height**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_ring_height**()

The height of the ring when using the emitter
`EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_ring_inner_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_ring_inner_radius**
`🔗<class_ParticleProcessMaterial_property_emission_ring_inner_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_ring_inner_radius**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_ring_inner_radius**()

The inner radius of the ring when using the emitter
`EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_ring_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_ring_radius**
`🔗<class_ParticleProcessMaterial_property_emission_ring_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_ring_radius**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_emission_ring_radius**()

The radius of the ring when using the emitter
`EMISSION_SHAPE_RING<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_RING>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_shape}
::: rst-class
classref-property
:::
::::

`EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
role="ref"} **emission_shape** = `0`
`🔗<class_ParticleProcessMaterial_property_emission_shape>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_shape**(value:
  `EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
  role="ref"})
- `EmissionShape<enum_ParticleProcessMaterial_EmissionShape>`{.interpreted-text
  role="ref"} **get_emission_shape**()

Particles will be emitted inside this region.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_shape_offset}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**emission_shape_offset** = `Vector3(0, 0, 0)`
`🔗<class_ParticleProcessMaterial_property_emission_shape_offset>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_shape_offset**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_emission_shape_offset**()

The offset for the
`emission_shape<class_ParticleProcessMaterial_property_emission_shape>`{.interpreted-text
role="ref"}, in local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_shape_scale}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**emission_shape_scale** = `Vector3(1, 1, 1)`
`🔗<class_ParticleProcessMaterial_property_emission_shape_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_emission_shape_scale**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_emission_shape_scale**()

The scale of the
`emission_shape<class_ParticleProcessMaterial_property_emission_shape>`{.interpreted-text
role="ref"}, in local space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_emission_sphere_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**emission_sphere_radius**
`🔗<class_ParticleProcessMaterial_property_emission_sphere_radius>`{.interpreted-text
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
`emission_shape<class_ParticleProcessMaterial_property_emission_shape>`{.interpreted-text
role="ref"} is set to
`EMISSION_SHAPE_SPHERE<class_ParticleProcessMaterial_constant_EMISSION_SHAPE_SPHERE>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_flatness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **flatness** = `0.0`
`🔗<class_ParticleProcessMaterial_property_flatness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_flatness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_flatness**()

Amount of
`spread<class_ParticleProcessMaterial_property_spread>`{.interpreted-text
role="ref"} along the Y axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_gravity}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"} **gravity** =
`Vector3(0, -9.8, 0)`
`🔗<class_ParticleProcessMaterial_property_gravity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_gravity**(value: `Vector3<class_Vector3>`{.interpreted-text
  role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_gravity**()

Gravity applied to every particle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_hue_variation_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**hue_variation_curve**
`🔗<class_ParticleProcessMaterial_property_hue_variation_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s hue will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_hue_variation_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **hue_variation_max**
= `0.0`
`🔗<class_ParticleProcessMaterial_property_hue_variation_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial hue variation applied to each particle. It will shift
the particle color\'s hue.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_hue_variation_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **hue_variation_min**
= `0.0`
`🔗<class_ParticleProcessMaterial_property_hue_variation_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`hue_variation_max<class_ParticleProcessMaterial_property_hue_variation_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_inherit_velocity_ratio}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**inherit_velocity_ratio** = `0.0`
`🔗<class_ParticleProcessMaterial_property_inherit_velocity_ratio>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_inherit_velocity_ratio**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_inherit_velocity_ratio**()

Percentage of the velocity of the respective
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"} or
`GPUParticles3D<class_GPUParticles3D>`{.interpreted-text role="ref"}
inherited by each particle when spawning.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_initial_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**initial_velocity_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_initial_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial velocity magnitude for each particle. Direction comes
from
`direction<class_ParticleProcessMaterial_property_direction>`{.interpreted-text
role="ref"} and
`spread<class_ParticleProcessMaterial_property_spread>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_initial_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**initial_velocity_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_initial_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`initial_velocity_max<class_ParticleProcessMaterial_property_initial_velocity_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_lifetime_randomness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**lifetime_randomness** = `0.0`
`🔗<class_ParticleProcessMaterial_property_lifetime_randomness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_lifetime_randomness**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_lifetime_randomness**()

Particle lifetime randomness ratio. The equation for the lifetime of a
particle is `lifetime * (1.0 - randf() * lifetime_randomness)`. For
example, a
`lifetime_randomness<class_ParticleProcessMaterial_property_lifetime_randomness>`{.interpreted-text
role="ref"} of `0.4` scales the lifetime between `0.6` to `1.0` of its
original value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_linear_accel_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**linear_accel_curve**
`🔗<class_ParticleProcessMaterial_property_linear_accel_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s linear acceleration will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_linear_accel_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_accel_max**
= `0.0`
`🔗<class_ParticleProcessMaterial_property_linear_accel_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum linear acceleration applied to each particle in the direction of
motion.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_linear_accel_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **linear_accel_min**
= `0.0`
`🔗<class_ParticleProcessMaterial_property_linear_accel_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`linear_accel_max<class_ParticleProcessMaterial_property_linear_accel_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_orbit_velocity_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**orbit_velocity_curve**
`🔗<class_ParticleProcessMaterial_property_orbit_velocity_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s orbital velocity will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

\*\*Note:\*\* For 3D orbital velocity, use a
`CurveXYZTexture<class_CurveXYZTexture>`{.interpreted-text role="ref"}.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_orbit_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**orbit_velocity_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_orbit_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum orbital velocity applied to each particle. Makes the particles
circle around origin. Specified in number of full rotations around
origin per second.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_orbit_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**orbit_velocity_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_orbit_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`orbit_velocity_max<class_ParticleProcessMaterial_property_orbit_velocity_max>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_particle_flag_align_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**particle_flag_align_y** = `false`
`🔗<class_ParticleProcessMaterial_property_particle_flag_align_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Align Y axis of particle with the direction of its velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_particle_flag_damping_as_friction}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**particle_flag_damping_as_friction** = `false`
`🔗<class_ParticleProcessMaterial_property_particle_flag_damping_as_friction>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Changes the behavior of the damping properties from a linear
deceleration to a deceleration based on speed percentage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_particle_flag_disable_z}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**particle_flag_disable_z** = `false`
`🔗<class_ParticleProcessMaterial_property_particle_flag_disable_z>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, particles will not move on the z axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_particle_flag_rotate_y}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**particle_flag_rotate_y** = `false`
`🔗<class_ParticleProcessMaterial_property_particle_flag_rotate_y>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_particle_flag**(particle_flag:
  `ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

If `true`, particles rotate around Y axis by
`angle_min<class_ParticleProcessMaterial_property_angle_min>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_radial_accel_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radial_accel_curve**
`🔗<class_ParticleProcessMaterial_property_radial_accel_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s radial acceleration will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_radial_accel_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radial_accel_max**
= `0.0`
`🔗<class_ParticleProcessMaterial_property_radial_accel_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum radial acceleration applied to each particle. Makes particle
accelerate away from the origin or towards it if negative.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_radial_accel_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **radial_accel_min**
= `0.0`
`🔗<class_ParticleProcessMaterial_property_radial_accel_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`radial_accel_max<class_ParticleProcessMaterial_property_radial_accel_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_radial_velocity_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**radial_velocity_curve**
`🔗<class_ParticleProcessMaterial_property_radial_velocity_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

A `CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} that
defines the velocity over the particle\'s lifetime away (or toward) the
`velocity_pivot<class_ParticleProcessMaterial_property_velocity_pivot>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_radial_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**radial_velocity_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_radial_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum radial velocity applied to each particle. Makes particles move
away from the
`velocity_pivot<class_ParticleProcessMaterial_property_velocity_pivot>`{.interpreted-text
role="ref"}, or toward it if negative.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_radial_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**radial_velocity_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_radial_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum radial velocity applied to each particle. Makes particles move
away from the
`velocity_pivot<class_ParticleProcessMaterial_property_velocity_pivot>`{.interpreted-text
role="ref"}, or toward it if negative.

\*\*Note:\*\* Animated velocities will not be affected by damping, use
`velocity_limit_curve<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_scale_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**scale_curve**
`🔗<class_ParticleProcessMaterial_property_scale_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s scale will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} over
its lifetime. If a
`CurveXYZTexture<class_CurveXYZTexture>`{.interpreted-text role="ref"}
is supplied instead, the scale will be separated per-axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_scale_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **scale_max** = `1.0`
`🔗<class_ParticleProcessMaterial_property_scale_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum initial scale applied to each particle.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_scale_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **scale_min** = `1.0`
`🔗<class_ParticleProcessMaterial_property_scale_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`scale_max<class_ParticleProcessMaterial_property_scale_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_scale_over_velocity_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**scale_over_velocity_curve**
`🔗<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Either a `CurveTexture<class_CurveTexture>`{.interpreted-text
role="ref"} or a
`CurveXYZTexture<class_CurveXYZTexture>`{.interpreted-text role="ref"}
that scales each particle based on its velocity.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_scale_over_velocity_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**scale_over_velocity_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_scale_over_velocity_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum velocity value reference for
`scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`{.interpreted-text
role="ref"}.

`scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`{.interpreted-text
role="ref"} will be interpolated between
`scale_over_velocity_min<class_ParticleProcessMaterial_property_scale_over_velocity_min>`{.interpreted-text
role="ref"} and
`scale_over_velocity_max<class_ParticleProcessMaterial_property_scale_over_velocity_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_scale_over_velocity_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**scale_over_velocity_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_scale_over_velocity_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum velocity value reference for
`scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`{.interpreted-text
role="ref"}.

`scale_over_velocity_curve<class_ParticleProcessMaterial_property_scale_over_velocity_curve>`{.interpreted-text
role="ref"} will be interpolated between
`scale_over_velocity_min<class_ParticleProcessMaterial_property_scale_over_velocity_min>`{.interpreted-text
role="ref"} and
`scale_over_velocity_max<class_ParticleProcessMaterial_property_scale_over_velocity_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_spread}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spread** = `45.0`
`🔗<class_ParticleProcessMaterial_property_spread>`{.interpreted-text
role="ref"}

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

:::: {#class_ParticleProcessMaterial_property_sub_emitter_amount_at_collision}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**sub_emitter_amount_at_collision**
`🔗<class_ParticleProcessMaterial_property_sub_emitter_amount_at_collision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sub_emitter_amount_at_collision**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sub_emitter_amount_at_collision**()

The amount of particles to spawn from the subemitter node when a
collision occurs. When combined with
`COLLISION_HIDE_ON_CONTACT<class_ParticleProcessMaterial_constant_COLLISION_HIDE_ON_CONTACT>`{.interpreted-text
role="ref"} on the main particles material, this can be used to achieve
effects such as raindrops hitting the ground.

\*\*Note:\*\* This value shouldn\'t exceed
`GPUParticles2D.amount<class_GPUParticles2D_property_amount>`{.interpreted-text
role="ref"} or
`GPUParticles3D.amount<class_GPUParticles3D_property_amount>`{.interpreted-text
role="ref"} defined on the *subemitter node* (not the main node),
relative to the subemitter\'s particle lifetime. If the number of
particles is exceeded, no new particles will spawn from the subemitter
until enough particles have expired.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_sub_emitter_amount_at_end}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**sub_emitter_amount_at_end**
`🔗<class_ParticleProcessMaterial_property_sub_emitter_amount_at_end>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sub_emitter_amount_at_end**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sub_emitter_amount_at_end**()

The amount of particles to spawn from the subemitter node when the
particle expires.

\*\*Note:\*\* This value shouldn\'t exceed
`GPUParticles2D.amount<class_GPUParticles2D_property_amount>`{.interpreted-text
role="ref"} or
`GPUParticles3D.amount<class_GPUParticles3D_property_amount>`{.interpreted-text
role="ref"} defined on the *subemitter node* (not the main node),
relative to the subemitter\'s particle lifetime. If the number of
particles is exceeded, no new particles will spawn from the subemitter
until enough particles have expired.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_sub_emitter_amount_at_start}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**sub_emitter_amount_at_start**
`🔗<class_ParticleProcessMaterial_property_sub_emitter_amount_at_start>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sub_emitter_amount_at_start**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_sub_emitter_amount_at_start**()

The amount of particles to spawn from the subemitter node when the
particle spawns.

\*\*Note:\*\* This value shouldn\'t exceed
`GPUParticles2D.amount<class_GPUParticles2D_property_amount>`{.interpreted-text
role="ref"} or
`GPUParticles3D.amount<class_GPUParticles3D_property_amount>`{.interpreted-text
role="ref"} defined on the *subemitter node* (not the main node),
relative to the subemitter\'s particle lifetime. If the number of
particles is exceeded, no new particles will spawn from the subemitter
until enough particles have expired.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_sub_emitter_frequency}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**sub_emitter_frequency**
`🔗<class_ParticleProcessMaterial_property_sub_emitter_frequency>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sub_emitter_frequency**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_sub_emitter_frequency**()

The frequency at which particles should be emitted from the subemitter
node. One particle will be spawned every
`sub_emitter_frequency<class_ParticleProcessMaterial_property_sub_emitter_frequency>`{.interpreted-text
role="ref"} seconds.

\*\*Note:\*\* This value shouldn\'t exceed
`GPUParticles2D.amount<class_GPUParticles2D_property_amount>`{.interpreted-text
role="ref"} or
`GPUParticles3D.amount<class_GPUParticles3D_property_amount>`{.interpreted-text
role="ref"} defined on the *subemitter node* (not the main node),
relative to the subemitter\'s particle lifetime. If the number of
particles is exceeded, no new particles will spawn from the subemitter
until enough particles have expired.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_sub_emitter_keep_velocity}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**sub_emitter_keep_velocity** = `false`
`🔗<class_ParticleProcessMaterial_property_sub_emitter_keep_velocity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sub_emitter_keep_velocity**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_sub_emitter_keep_velocity**()

If `true`, the subemitter inherits the parent particle\'s velocity when
it spawns.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_sub_emitter_mode}
::: rst-class
classref-property
:::
::::

`SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
role="ref"} **sub_emitter_mode** = `0`
`🔗<class_ParticleProcessMaterial_property_sub_emitter_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sub_emitter_mode**(value:
  `SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
  role="ref"})
- `SubEmitterMode<enum_ParticleProcessMaterial_SubEmitterMode>`{.interpreted-text
  role="ref"} **get_sub_emitter_mode**()

The particle subemitter mode (see
`GPUParticles2D.sub_emitter<class_GPUParticles2D_property_sub_emitter>`{.interpreted-text
role="ref"} and
`GPUParticles3D.sub_emitter<class_GPUParticles3D_property_sub_emitter>`{.interpreted-text
role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_tangential_accel_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**tangential_accel_curve**
`🔗<class_ParticleProcessMaterial_property_tangential_accel_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s tangential acceleration will vary along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_tangential_accel_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**tangential_accel_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_tangential_accel_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
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

:::: {#class_ParticleProcessMaterial_property_tangential_accel_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**tangential_accel_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_tangential_accel_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum equivalent of
`tangential_accel_max<class_ParticleProcessMaterial_property_tangential_accel_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **turbulence_enabled**
= `false`
`🔗<class_ParticleProcessMaterial_property_turbulence_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_turbulence_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_turbulence_enabled**()

If `true`, enables turbulence for the particle system. Turbulence can be
used to vary particle movement according to its position (based on a 3D
noise pattern). In 3D,
`GPUParticlesAttractorVectorField3D<class_GPUParticlesAttractorVectorField3D>`{.interpreted-text
role="ref"} with
`NoiseTexture3D<class_NoiseTexture3D>`{.interpreted-text role="ref"} can
be used as an alternative to turbulence that works in world space and
with multiple particle systems reacting in the same way.

\*\*Note:\*\* Enabling turbulence has a high performance cost on the
GPU. Only enable turbulence on a few particle systems at once at most,
and consider disabling it when targeting mobile/web platforms.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_influence_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**turbulence_influence_max** = `0.1`
`🔗<class_ParticleProcessMaterial_property_turbulence_influence_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated
as a random value between
`turbulence_influence_min<class_ParticleProcessMaterial_property_turbulence_influence_min>`{.interpreted-text
role="ref"} and
`turbulence_influence_max<class_ParticleProcessMaterial_property_turbulence_influence_max>`{.interpreted-text
role="ref"} and multiplied by the amount of turbulence influence from
`turbulence_influence_over_life<class_ParticleProcessMaterial_property_turbulence_influence_over_life>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_influence_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**turbulence_influence_min** = `0.1`
`🔗<class_ParticleProcessMaterial_property_turbulence_influence_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum turbulence influence on each particle.

The actual amount of turbulence influence on each particle is calculated
as a random value between
`turbulence_influence_min<class_ParticleProcessMaterial_property_turbulence_influence_min>`{.interpreted-text
role="ref"} and
`turbulence_influence_max<class_ParticleProcessMaterial_property_turbulence_influence_max>`{.interpreted-text
role="ref"} and multiplied by the amount of turbulence influence from
`turbulence_influence_over_life<class_ParticleProcessMaterial_property_turbulence_influence_over_life>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_influence_over_life}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**turbulence_influence_over_life**
`🔗<class_ParticleProcessMaterial_property_turbulence_influence_over_life>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_param_texture**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Each particle\'s amount of turbulence will be influenced along this
`CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} over
its life time.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_initial_displacement_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**turbulence_initial_displacement_max** = `0.0`
`🔗<class_ParticleProcessMaterial_property_turbulence_initial_displacement_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_max**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Maximum displacement of each particle\'s spawn position by the
turbulence.

The actual amount of displacement will be a factor of the underlying
turbulence multiplied by a random value between
`turbulence_initial_displacement_min<class_ParticleProcessMaterial_property_turbulence_initial_displacement_min>`{.interpreted-text
role="ref"} and
`turbulence_initial_displacement_max<class_ParticleProcessMaterial_property_turbulence_initial_displacement_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_initial_displacement_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**turbulence_initial_displacement_min** = `0.0`
`🔗<class_ParticleProcessMaterial_property_turbulence_initial_displacement_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"}, value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_param_min**(param:
  `Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
  role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

Minimum displacement of each particle\'s spawn position by the
turbulence.

The actual amount of displacement will be a factor of the underlying
turbulence multiplied by a random value between
`turbulence_initial_displacement_min<class_ParticleProcessMaterial_property_turbulence_initial_displacement_min>`{.interpreted-text
role="ref"} and
`turbulence_initial_displacement_max<class_ParticleProcessMaterial_property_turbulence_initial_displacement_max>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_noise_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**turbulence_noise_scale** = `9.0`
`🔗<class_ParticleProcessMaterial_property_turbulence_noise_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_turbulence_noise_scale**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_turbulence_noise_scale**()

This value controls the overall scale/frequency of the turbulence noise
pattern.

A small scale will result in smaller features with more detail while a
high scale will result in smoother noise with larger features.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_noise_speed}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**turbulence_noise_speed** = `Vector3(0, 0, 0)`
`🔗<class_ParticleProcessMaterial_property_turbulence_noise_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_turbulence_noise_speed**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_turbulence_noise_speed**()

A scrolling velocity for the turbulence field. This sets a directional
trend for the pattern to move in over time.

The default value of `Vector3(0, 0, 0)` turns off the scrolling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_noise_speed_random}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**turbulence_noise_speed_random** = `0.2`
`🔗<class_ParticleProcessMaterial_property_turbulence_noise_speed_random>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_turbulence_noise_speed_random**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_turbulence_noise_speed_random**()

The in-place rate of change of the turbulence field. This defines how
quickly the noise pattern varies over time.

A value of 0.0 will result in a fixed pattern.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_turbulence_noise_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**turbulence_noise_strength** = `1.0`
`🔗<class_ParticleProcessMaterial_property_turbulence_noise_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_turbulence_noise_strength**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_turbulence_noise_strength**()

The turbulence noise strength. Increasing this will result in a
stronger, more contrasting, flow pattern.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_velocity_limit_curve}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**velocity_limit_curve**
`🔗<class_ParticleProcessMaterial_property_velocity_limit_curve>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_velocity_limit_curve**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_velocity_limit_curve**()

A `CurveTexture<class_CurveTexture>`{.interpreted-text role="ref"} that
defines the maximum velocity of a particle during its lifetime.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_property_velocity_pivot}
::: rst-class
classref-property
:::
::::

`Vector3<class_Vector3>`{.interpreted-text role="ref"}
**velocity_pivot** = `Vector3(0, 0, 0)`
`🔗<class_ParticleProcessMaterial_property_velocity_pivot>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_velocity_pivot**(value:
  `Vector3<class_Vector3>`{.interpreted-text role="ref"})
- `Vector3<class_Vector3>`{.interpreted-text role="ref"}
  **get_velocity_pivot**()

A pivot point used to calculate radial and orbital velocity of
particles.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_ParticleProcessMaterial_method_get_param}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_param**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ParticleProcessMaterial_method_get_param>`{.interpreted-text
role="ref"}

Returns the minimum and maximum values of the given `param` as a vector.

The `x` component of the returned vector corresponds to minimum and the
`y` component corresponds to maximum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_get_param_max}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_param_max**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ParticleProcessMaterial_method_get_param_max>`{.interpreted-text
role="ref"}

Returns the maximum value range for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_get_param_min}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_param_min**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ParticleProcessMaterial_method_get_param_min>`{.interpreted-text
role="ref"}

Returns the minimum value range for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_get_param_texture}
::: rst-class
classref-method
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**get_param_texture**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ParticleProcessMaterial_method_get_param_texture>`{.interpreted-text
role="ref"}

Returns the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
used by the specified parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_get_particle_flag}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_particle_flag**(particle_flag:
`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_ParticleProcessMaterial_method_get_particle_flag>`{.interpreted-text
role="ref"}

Returns `true` if the specified particle flag is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_set_param}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"}, value: `Vector2<class_Vector2>`{.interpreted-text
role="ref"})
`🔗<class_ParticleProcessMaterial_method_set_param>`{.interpreted-text
role="ref"}

Sets the minimum and maximum values of the given `param`.

The `x` component of the argument vector corresponds to minimum and the
`y` component corresponds to maximum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_set_param_max}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_max**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_ParticleProcessMaterial_method_set_param_max>`{.interpreted-text
role="ref"}

Sets the maximum value range for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_set_param_min}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_min**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"}, value: `float<class_float>`{.interpreted-text role="ref"})
`🔗<class_ParticleProcessMaterial_method_set_param_min>`{.interpreted-text
role="ref"}

Sets the minimum value range for the given parameter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_set_param_texture}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_param_texture**(param:
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"}, texture: `Texture2D<class_Texture2D>`{.interpreted-text
role="ref"})
`🔗<class_ParticleProcessMaterial_method_set_param_texture>`{.interpreted-text
role="ref"}

Sets the `Texture2D<class_Texture2D>`{.interpreted-text role="ref"} for
the specified
`Parameter<enum_ParticleProcessMaterial_Parameter>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_ParticleProcessMaterial_method_set_particle_flag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_particle_flag**(particle_flag:
`ParticleFlags<enum_ParticleProcessMaterial_ParticleFlags>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_ParticleProcessMaterial_method_set_particle_flag>`{.interpreted-text
role="ref"}

Sets the `particle_flag` to `enable`.
