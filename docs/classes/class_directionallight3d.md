github_url
:   hide

::: {.meta keywords="sun"}
:::

# DirectionalLight3D {#class_DirectionalLight3D}

**Inherits:** `Light3D<class_Light3D>`{.interpreted-text role="ref"}
**\<** `VisualInstance3D<class_VisualInstance3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Directional light from a distance, as from the Sun.

::: rst-class
classref-introduction-group
:::

## Description

A directional light is a type of
`Light3D<class_Light3D>`{.interpreted-text role="ref"} node that models
an infinite number of parallel rays covering the entire scene. It is
used for lights with strong intensity that are located far away from the
scene to model sunlight or moonlight.

Light is emitted in the -Z direction of the node\'s global basis. For an
unrotated light, this means that the light is emitted forwards,
illuminating the front side of a 3D model (see
`Vector3.FORWARD<class_Vector3_constant_FORWARD>`{.interpreted-text
role="ref"} and
`Vector3.MODEL_FRONT<class_Vector3_constant_MODEL_FRONT>`{.interpreted-text
role="ref"}). The position of the node is ignored; only the basis is
used to determine light direction.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `3D lights and shadows <../tutorials/3d/lights_and_shadows>`{.interpreted-text
  role="doc"}
- `Faking global illumination <../tutorials/3d/global_illumination/faking_global_illumination>`{.interpreted-text
  role="doc"}

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

:::: {#enum_DirectionalLight3D_ShadowMode}
::: rst-class
classref-enumeration
:::
::::

enum **ShadowMode**:
`🔗<enum_DirectionalLight3D_ShadowMode>`{.interpreted-text role="ref"}

:::: {#class_DirectionalLight3D_constant_SHADOW_ORTHOGONAL}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowMode<enum_DirectionalLight3D_ShadowMode>`{.interpreted-text
role="ref"} **SHADOW_ORTHOGONAL** = `0`

Renders the entire scene\'s shadow map from an orthogonal point of view.
This is the fastest directional shadow mode. May result in blurrier
shadows on close objects.

:::: {#class_DirectionalLight3D_constant_SHADOW_PARALLEL_2_SPLITS}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowMode<enum_DirectionalLight3D_ShadowMode>`{.interpreted-text
role="ref"} **SHADOW_PARALLEL_2_SPLITS** = `1`

Splits the view frustum in 2 areas, each with its own shadow map. This
shadow mode is a compromise between
`SHADOW_ORTHOGONAL<class_DirectionalLight3D_constant_SHADOW_ORTHOGONAL>`{.interpreted-text
role="ref"} and
`SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>`{.interpreted-text
role="ref"} in terms of performance.

:::: {#class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS}
::: rst-class
classref-enumeration-constant
:::
::::

`ShadowMode<enum_DirectionalLight3D_ShadowMode>`{.interpreted-text
role="ref"} **SHADOW_PARALLEL_4_SPLITS** = `2`

Splits the view frustum in 4 areas, each with its own shadow map. This
is the slowest directional shadow mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_DirectionalLight3D_SkyMode}
::: rst-class
classref-enumeration
:::
::::

enum **SkyMode**:
`🔗<enum_DirectionalLight3D_SkyMode>`{.interpreted-text role="ref"}

:::: {#class_DirectionalLight3D_constant_SKY_MODE_LIGHT_AND_SKY}
::: rst-class
classref-enumeration-constant
:::
::::

`SkyMode<enum_DirectionalLight3D_SkyMode>`{.interpreted-text role="ref"}
**SKY_MODE_LIGHT_AND_SKY** = `0`

Makes the light visible in both scene lighting and sky rendering.

:::: {#class_DirectionalLight3D_constant_SKY_MODE_LIGHT_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`SkyMode<enum_DirectionalLight3D_SkyMode>`{.interpreted-text role="ref"}
**SKY_MODE_LIGHT_ONLY** = `1`

Makes the light visible in scene lighting only (including direct
lighting and global illumination). When using this mode, the light will
not be visible from sky shaders.

:::: {#class_DirectionalLight3D_constant_SKY_MODE_SKY_ONLY}
::: rst-class
classref-enumeration-constant
:::
::::

`SkyMode<enum_DirectionalLight3D_SkyMode>`{.interpreted-text role="ref"}
**SKY_MODE_SKY_ONLY** = `2`

Makes the light visible to sky shaders only. When using this mode the
light will not cast light into the scene (either through direct lighting
or through global illumination), but can be accessed through sky
shaders. This can be useful, for example, when you want to control sky
effects without illuminating the scene (during a night cycle, for
example).

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_DirectionalLight3D_property_directional_shadow_blend_splits}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**directional_shadow_blend_splits** = `false`
`🔗<class_DirectionalLight3D_property_directional_shadow_blend_splits>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_splits**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_blend_splits_enabled**()

If `true`, shadow detail is sacrificed in exchange for smoother
transitions between splits. Enabling shadow blend splitting also has a
moderate performance cost. This is ignored when
`directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>`{.interpreted-text
role="ref"} is
`SHADOW_ORTHOGONAL<class_DirectionalLight3D_constant_SHADOW_ORTHOGONAL>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_directional_shadow_fade_start}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_shadow_fade_start** = `0.8`
`🔗<class_DirectionalLight3D_property_directional_shadow_fade_start>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

Proportion of
`directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"} at which point the shadow starts to fade. At
`directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"}, the shadow will disappear. The default value is a balance
between smooth fading and distant shadow visibility. If the camera moves
fast and the
`directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"} is low, consider lowering
`directional_shadow_fade_start<class_DirectionalLight3D_property_directional_shadow_fade_start>`{.interpreted-text
role="ref"} below `0.8` to make shadow transitions less noticeable. On
the other hand, if you tuned
`directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"} to cover the entire scene, you can set
`directional_shadow_fade_start<class_DirectionalLight3D_property_directional_shadow_fade_start>`{.interpreted-text
role="ref"} to `1.0` to prevent the shadow from fading in the distance
(it will suddenly cut off instead).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_directional_shadow_max_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_shadow_max_distance** = `100.0`
`🔗<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The maximum distance for shadow splits. Increasing this value will make
directional shadows visible from further away, at the cost of lower
overall shadow detail and performance (since more objects need to be
included in the directional shadow rendering).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_directional_shadow_mode}
::: rst-class
classref-property
:::
::::

`ShadowMode<enum_DirectionalLight3D_ShadowMode>`{.interpreted-text
role="ref"} **directional_shadow_mode** = `2`
`🔗<class_DirectionalLight3D_property_directional_shadow_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shadow_mode**(value:
  `ShadowMode<enum_DirectionalLight3D_ShadowMode>`{.interpreted-text
  role="ref"})
- `ShadowMode<enum_DirectionalLight3D_ShadowMode>`{.interpreted-text
  role="ref"} **get_shadow_mode**()

The light\'s shadow rendering algorithm.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_directional_shadow_pancake_size}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_shadow_pancake_size** = `20.0`
`🔗<class_DirectionalLight3D_property_directional_shadow_pancake_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

Sets the size of the directional shadow pancake. The pancake offsets the
start of the shadow\'s camera frustum to provide a higher effective
depth resolution for the shadow. However, a high pancake size can cause
artifacts in the shadows of large objects that are close to the edge of
the frustum. Reducing the pancake size can help. Setting the size to `0`
turns off the pancaking effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_directional_shadow_split_1}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_shadow_split_1** = `0.1`
`🔗<class_DirectionalLight3D_property_directional_shadow_split_1>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The distance from camera to shadow split 1. Relative to
`directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"}. Only used when
`directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>`{.interpreted-text
role="ref"} is
`SHADOW_PARALLEL_2_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_2_SPLITS>`{.interpreted-text
role="ref"} or
`SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_directional_shadow_split_2}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_shadow_split_2** = `0.2`
`🔗<class_DirectionalLight3D_property_directional_shadow_split_2>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The distance from shadow split 1 to split 2. Relative to
`directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"}. Only used when
`directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>`{.interpreted-text
role="ref"} is
`SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_directional_shadow_split_3}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**directional_shadow_split_3** = `0.5`
`🔗<class_DirectionalLight3D_property_directional_shadow_split_3>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The distance from shadow split 2 to split 3. Relative to
`directional_shadow_max_distance<class_DirectionalLight3D_property_directional_shadow_max_distance>`{.interpreted-text
role="ref"}. Only used when
`directional_shadow_mode<class_DirectionalLight3D_property_directional_shadow_mode>`{.interpreted-text
role="ref"} is
`SHADOW_PARALLEL_4_SPLITS<class_DirectionalLight3D_constant_SHADOW_PARALLEL_4_SPLITS>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_DirectionalLight3D_property_sky_mode}
::: rst-class
classref-property
:::
::::

`SkyMode<enum_DirectionalLight3D_SkyMode>`{.interpreted-text role="ref"}
**sky_mode** = `0`
`🔗<class_DirectionalLight3D_property_sky_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sky_mode**(value:
  `SkyMode<enum_DirectionalLight3D_SkyMode>`{.interpreted-text
  role="ref"})
- `SkyMode<enum_DirectionalLight3D_SkyMode>`{.interpreted-text
  role="ref"} **get_sky_mode**()

Whether this **DirectionalLight3D** is visible in the sky, in the scene,
or both in the sky and in the scene.
