# Fog shaders {#doc_fog_shader}

Fog shaders are used to define how fog is added (or subtracted) from a
scene in a given area. Fog shaders are always used together with
`FogVolumes <class_FogVolume>`{.interpreted-text role="ref"} and
volumetric fog. Fog shaders only have one processing function, the
`fog()` function.

The resolution of the fog shaders depends on the resolution of the
volumetric fog froxel grid. Accordingly, the level of detail that a fog
shader can add depends on how close the
`FogVolume <class_FogVolume>`{.interpreted-text role="ref"} is to the
camera.

Fog shaders are a special form of compute shader that is called once for
every froxel that is touched by an axis aligned bounding box of the
associated `FogVolume <class_FogVolume>`{.interpreted-text role="ref"}.
This means that froxels that just barely touch a given
`FogVolume <class_FogVolume>`{.interpreted-text role="ref"} will still
be used.

## Built-ins

Values marked as `in` are read-only. Values marked as `out` can
optionally be written to and will not necessarily contain sensible
values. Samplers cannot be written to so they are not marked.

## Global built-ins

Global built-ins are available everywhere, including in custom
functions.

  ----------------------------------------------------------------------------------------------------------------------------
  Built-in             Description
  -------------------- -------------------------------------------------------------------------------------------------------
  in float **TIME**    Global time since the engine has started, in seconds. It repeats after every `3,600` seconds (which can
                       be changed with the
                       `rollover<class_ProjectSettings_property_rendering/limits/time/time_rollover_secs>`{.interpreted-text
                       role="ref"} setting). It\'s affected by
                       `time_scale<class_Engine_property_time_scale>`{.interpreted-text role="ref"} but not by pausing. If you
                       need a `TIME` variable that is not affected by time scale, add your own
                       `global shader uniform<doc_shading_language_global_uniforms>`{.interpreted-text role="ref"} and update
                       it each frame.

  in float **PI**      A `PI` constant (`3.141592`). A ratio of a circle\'s circumference to its diameter and amount of
                       radians in half turn.

  in float **TAU**     A `TAU` constant (`6.283185`). An equivalent of `PI * 2` and amount of radians in full turn.

  in float **E**       An `E` constant (`2.718281`). Euler\'s number and a base of the natural logarithm.
  ----------------------------------------------------------------------------------------------------------------------------

## Fog built-ins

All of the output values of fog volumes overlap one another. This allows
`FogVolumes <class_FogVolume>`{.interpreted-text role="ref"} to be
rendered efficiently as they can all be drawn at once.

  ---------------------------------------------------------------------------------
  Built-in              Description
  --------------------- -----------------------------------------------------------
  in vec3               Position of current froxel cell in world space.
  **WORLD_POSITION**    

  in vec3               Position of the center of the current
  **OBJECT_POSITION**   `FogVolume <class_FogVolume>`{.interpreted-text role="ref"}
                        in world space.

  in vec3 **UVW**       3-dimensional UV, used to map a 3D texture to the current
                        `FogVolume <class_FogVolume>`{.interpreted-text
                        role="ref"}.

  in vec3 **SIZE**      Size of the current
                        `FogVolume <class_FogVolume>`{.interpreted-text role="ref"}
                        when its
                        `shape<class_FogVolume_property_shape>`{.interpreted-text
                        role="ref"} has a size.

  in vec3 **SDF**       Signed distance field to the surface of the
                        `FogVolume <class_FogVolume>`{.interpreted-text
                        role="ref"}. Negative if inside volume, positive otherwise.

  out vec3 **ALBEDO**   Output base color value, interacts with light to produce
                        final color. Only written to fog volume if used.

  out float **DENSITY** Output density value. Can be negative to allow subtracting
                        one volume from another. Density must be used for fog
                        shader to write anything at all.

  out vec3 **EMISSION** Output emission color value, added to color during light
                        pass to produce final color. Only written to fog volume if
                        used.
  ---------------------------------------------------------------------------------
