# Particle shaders {#doc_particle_shader}

Particle shaders are a special type of shader that runs before the
object is drawn. They are used for calculating material properties such
as color, position, and rotation. They are drawn with any regular
material for CanvasItem or Spatial, depending on whether they are 2D or
3D.

Particle shaders are unique because they are not used to draw the object
itself; they are used to calculate particle properties, which are then
used by a `CanvasItem<doc_canvas_item_shader>`{.interpreted-text
role="ref"} or `Spatial<doc_spatial_shader>`{.interpreted-text
role="ref"} shader. They contain two processor functions: `start()` and
`process()`.

Unlike other shader types, particle shaders keep the data that was
output the previous frame. Therefore, particle shaders can be used for
complex effects that take place over multiple frames.

:::: note
::: title
Note
:::

Particle shaders are only available with GPU-based particle nodes
(`class_GPUParticles2D`{.interpreted-text role="ref"} and
`class_GPUParticles3D`{.interpreted-text role="ref"}).

CPU-based particle nodes (`class_CPUParticles2D`{.interpreted-text
role="ref"} and `class_CPUParticles3D`{.interpreted-text role="ref"})
are *rendered* on the GPU (which means they can use custom CanvasItem or
Spatial shaders), but their motion is *simulated* on the CPU.
::::

## Render modes

  ----------------------------------------------------------------------
  Render mode                Description
  -------------------------- -------------------------------------------
  **keep_data**              Do not clear previous data on restart.

  **disable_force**          Disable attractor force.

  **disable_velocity**       Ignore `VELOCITY` value.

  **collision_use_scale**    Scale the particle\'s size for collisions.
  ----------------------------------------------------------------------

## Built-ins

Values marked as `in` are read-only. Values marked as `out` can
optionally be written to and will not necessarily contain sensible
values. Values marked as `inout` provide a sensible default value, and
can optionally be written to. Samplers cannot be written to so they are
not marked.

## Global built-ins

Global built-ins are available everywhere, including custom functions.

  --------------------------------------------------------------------------------------------------------------------
  Built-in     Description
  ------------ -------------------------------------------------------------------------------------------------------
  in float     Global time since the engine has started, in seconds. It repeats after every `3,600` seconds (which can
  **TIME**     be changed with the
               `rollover<class_ProjectSettings_property_rendering/limits/time/time_rollover_secs>`{.interpreted-text
               role="ref"} setting). It\'s affected by
               `time_scale<class_Engine_property_time_scale>`{.interpreted-text role="ref"} but not by pausing. If you
               need a `TIME` variable that is not affected by time scale, add your own
               `global shader uniform<doc_shading_language_global_uniforms>`{.interpreted-text role="ref"} and update
               it each frame.

  in float     A `PI` constant (`3.141592`). A ratio of a circle\'s circumference to its diameter and amount of
  **PI**       radians in half turn.

  in float     A `TAU` constant (`6.283185`). An equivalent of `PI * 2` and amount of radians in full turn.
  **TAU**      

  in float     An `E` constant (`2.718281`). Euler\'s number and a base of the natural logarithm.
  **E**        
  --------------------------------------------------------------------------------------------------------------------

## Start and Process built-ins

These properties can be accessed from both the `start()` and `process()`
functions.

  ----------------------------------------------------------------------------------------------------------
  Function                  Description
  ------------------------- --------------------------------------------------------------------------------
  in float **LIFETIME**     Particle lifetime.

  in float **DELTA**        Delta process time.

  in uint **NUMBER**        Unique number since emission start.

  in uint **INDEX**         Particle index (from total particles).

  in mat4                   Emitter transform (used for non-local systems).
  **EMISSION_TRANSFORM**    

  in uint **RANDOM_SEED**   Random seed used as base for random.

  inout bool **ACTIVE**     `true` when the particle is active, can be set `false`.

  inout vec4 **COLOR**      Particle color, can be written to and accessed in mesh\'s vertex function.

  inout vec3 **VELOCITY**   Particle velocity, can be modified.

  inout mat4 **TRANSFORM**  Particle transform.

  inout vec4 **CUSTOM**     Custom particle data. Accessible from shader of mesh as `INSTANCE_CUSTOM`.

  inout float **MASS**      Particle mass, intended to be used with attractors. Equals `1.0` by default.

  in vec4 **USERDATAX**     Vector that enables the integration of supplementary user-defined data into the
                            particle process shader. `USERDATAX` are six built-ins identified by number, `X`
                            can be numbers between 1 and 6, for example `USERDATA3`.

  in uint                   A flag for using on the last argument of `emit_subparticle()` function to assign
  **FLAG_EMIT_POSITION**    a position to a new particle\'s transform.

  in uint                   A flag for using on the last argument of `emit_subparticle()` function to assign
  **FLAG_EMIT_ROT_SCALE**   the rotation and scale to a new particle\'s transform.

  in uint                   A flag for using on the last argument of `emit_subparticle()` function to assign
  **FLAG_EMIT_VELOCITY**    a velocity to a new particle.

  in uint                   A flag for using on the last argument of `emit_subparticle()` function to assign
  **FLAG_EMIT_COLOR**       a color to a new particle.

  in uint                   A flag for using on the last argument of `emit_subparticle()` function to assign
  **FLAG_EMIT_CUSTOM**      a custom data vector to a new particle.

  in vec3                   Velocity of the `Particles2D<class_GPUParticles2D>`{.interpreted-text
  **EMITTER_VELOCITY**      role="ref"} (`3D<class_GPUParticles3D>`{.interpreted-text role="ref"}) node.

  in float                  Value of
  **INTERPOLATE_TO_END**    `interp_to_end<class_GPUParticles2D_property_interp_to_end>`{.interpreted-text
                            role="ref"} (`3D<class_GPUParticles3D_property_interp_to_end>`{.interpreted-text
                            role="ref"}) property of Particles node.

  in uint **AMOUNT_RATIO**  Value of
                            `amount_ratio<class_GPUParticles2D_property_amount_ratio>`{.interpreted-text
                            role="ref"} (`3D<class_GPUParticles3D_property_amount_ratio>`{.interpreted-text
                            role="ref"}) property of Particles node.
  ----------------------------------------------------------------------------------------------------------

:::: note
::: title
Note
:::

In order to use the `COLOR` variable in a StandardMaterial3D, set
`vertex_color_use_as_albedo` to `true`. In a ShaderMaterial, access it
with the `COLOR` variable.
::::

## Start built-ins

  -----------------------------------------------------------------------------------
  Built-in                Description
  ----------------------- -----------------------------------------------------------
  in bool                 `true` if particle is restarted, or emitted without a
  **RESTART_POSITION**    custom position (i.e. this particle was created by
                          `emit_subparticle()` without the `FLAG_EMIT_POSITION`
                          flag).

  in bool                 `true` if particle is restarted, or emitted without a
  **RESTART_ROT_SCALE**   custom rotation or scale (i.e. this particle was created by
                          `emit_subparticle()` without the `FLAG_EMIT_ROT_SCALE`
                          flag).

  in bool                 `true` if particle is restarted, or emitted without a
  **RESTART_VELOCITY**    custom velocity (i.e. this particle was created by
                          `emit_subparticle()` without the `FLAG_EMIT_VELOCITY`
                          flag).

  in bool                 `true` if particle is restarted, or emitted without a
  **RESTART_COLOR**       custom color (i.e. this particle was created by
                          `emit_subparticle()` without the `FLAG_EMIT_COLOR` flag).

  in bool                 `true` if particle is restarted, or emitted without a
  **RESTART_CUSTOM**      custom property (i.e. this particle was created by
                          `emit_subparticle()` without the `FLAG_EMIT_CUSTOM` flag).
  -----------------------------------------------------------------------------------

## Process built-ins

  ---------------------------------------------------------------------------
  Built-in               Description
  ---------------------- ----------------------------------------------------
  in bool **RESTART**    `true` if the current process frame is first for the
                         particle.

  in bool **COLLIDED**   `true` when the particle has collided with a
                         particle collider.

  in vec3                A normal of the last collision. If there is no
  **COLLISION_NORMAL**   collision detected it is equal to `(0.0, 0.0, 0.0)`.

  in float               A length of normal of the last collision. If there
  **COLLISION_DEPTH**    is no collision detected it is equal to `0.0`.

  in vec3                A combined force of the attractors at the moment on
  **ATTRACTOR_FORCE**    that particle.
  ---------------------------------------------------------------------------

## Process functions

`emit_subparticle()` is currently the only custom function supported by
particles shaders. It allows users to add a new particle with specified
parameters from a sub-emitter. The newly created particle will only use
the properties that match the `flags` parameter. For example, the
following code will emit a particle with a specified position, velocity,
and color, but unspecified rotation, scale, and custom value:

``` glsl
mat4 custom_transform = mat4(1.0);
custom_transform[3].xyz = vec3(10.5, 0.0, 4.0);
emit_subparticle(custom_transform, vec3(1.0, 0.5, 1.0), vec4(1.0, 0.0, 0.0, 1.0), vec4(1.0), FLAG_EMIT_POSITION | FLAG_EMIT_VELOCITY | FLAG_EMIT_COLOR);
```

  -----------------------------------------------------------------------
  Function                                           Description
  -------------------------------------------------- --------------------
  bool **emit_subparticle** (mat4 xform, vec3        Emits a particle
  velocity, vec4 color, vec4 custom, uint flags)     from a sub-emitter.

  -----------------------------------------------------------------------
