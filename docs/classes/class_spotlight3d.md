github_url
:   hide

# SpotLight3D {#class_SpotLight3D}

**Inherits:** `Light3D<class_Light3D>`{.interpreted-text role="ref"}
**\<** `VisualInstance3D<class_VisualInstance3D>`{.interpreted-text
role="ref"} **\<** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A spotlight, such as a reflector spotlight or a lantern.

::: rst-class
classref-introduction-group
:::

## Description

A Spotlight is a type of `Light3D<class_Light3D>`{.interpreted-text
role="ref"} node that emits lights in a specific direction, in the shape
of a cone. The light is attenuated through the distance. This
attenuation can be configured by changing the energy, radius and
attenuation parameters of `Light3D<class_Light3D>`{.interpreted-text
role="ref"}.

Light is emitted in the -Z direction of the node\'s global basis. For an
unrotated light, this means that the light is emitted forwards,
illuminating the front side of a 3D model (see
`Vector3.FORWARD<class_Vector3_constant_FORWARD>`{.interpreted-text
role="ref"} and
`Vector3.MODEL_FRONT<class_Vector3_constant_MODEL_FRONT>`{.interpreted-text
role="ref"}).

\*\*Note:\*\* When using the Mobile rendering method, only 8 spot lights
can be displayed on each mesh resource. Attempting to display more than
8 spot lights on a single mesh resource will result in spot lights
flickering in and out as the camera moves. When using the Compatibility
rendering method, only 8 spot lights can be displayed on each mesh
resource by default, but this can be increased by adjusting
`ProjectSettings.rendering/limits/opengl/max_lights_per_object<class_ProjectSettings_property_rendering/limits/opengl/max_lights_per_object>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* When using the Mobile or Compatibility rendering methods,
spot lights will only correctly affect meshes whose visibility AABB
intersects with the light\'s AABB. If using a shader to deform the mesh
in a way that makes it go outside its AABB,
`GeometryInstance3D.extra_cull_margin<class_GeometryInstance3D_property_extra_cull_margin>`{.interpreted-text
role="ref"} must be increased on the mesh. Otherwise, the light may not
be visible on the mesh.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `3D lights and shadows <../tutorials/3d/lights_and_shadows>`{.interpreted-text
  role="doc"}
- `Faking global illumination <../tutorials/3d/global_illumination/faking_global_illumination>`{.interpreted-text
  role="doc"}
- [Third Person Shooter (TPS)
  Demo](https://godotengine.org/asset-library/asset/2710)

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

## Property Descriptions

:::: {#class_SpotLight3D_property_spot_angle}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spot_angle** =
`45.0` `🔗<class_SpotLight3D_property_spot_angle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The spotlight\'s angle in degrees. This is the angular radius, meaning
the angle from the -Z axis, the cone\'s center, to the edge of the cone.
The default angular radius of 45 degrees corresponds to a cone with an
angular diameter of 90 degrees.

\*\*Note:\*\*
`spot_angle<class_SpotLight3D_property_spot_angle>`{.interpreted-text
role="ref"} is not affected by
`Node3D.scale<class_Node3D_property_scale>`{.interpreted-text
role="ref"} (the light\'s scale or its parent\'s scale).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpotLight3D_property_spot_angle_attenuation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**spot_angle_attenuation** = `1.0`
`🔗<class_SpotLight3D_property_spot_angle_attenuation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The spotlight\'s *angular* attenuation curve. See also
`spot_attenuation<class_SpotLight3D_property_spot_attenuation>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpotLight3D_property_spot_attenuation}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spot_attenuation**
= `1.0`
`🔗<class_SpotLight3D_property_spot_attenuation>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

Controls the distance attenuation function for spotlights.

A value of `0.0` will maintain a constant brightness through most of the
range, but smoothly attenuate the light at the edge of the range. Use a
value of `2.0` for physically accurate lights as it results in the
proper inverse square attenutation.

\*\*Note:\*\* Setting attenuation to `2.0` or higher may result in
distant objects receiving minimal light, even within range. For example,
with a range of `4096`, an object at `100` units is attenuated by a
factor of `0.0001`. With a default brightness of `1`, the light would
not be visible at that distance.

\*\*Note:\*\* Using negative or values higher than `10.0` may lead to
unexpected results.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_SpotLight3D_property_spot_range}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **spot_range** =
`5.0` `🔗<class_SpotLight3D_property_spot_range>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_param**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_param**()

The maximal range that can be reached by the spotlight. Note that the
effectively lit area may appear to be smaller depending on the
`spot_attenuation<class_SpotLight3D_property_spot_attenuation>`{.interpreted-text
role="ref"} in use. No matter the
`spot_attenuation<class_SpotLight3D_property_spot_attenuation>`{.interpreted-text
role="ref"} in use, the light will never reach anything outside this
range.

\*\*Note:\*\*
`spot_range<class_SpotLight3D_property_spot_range>`{.interpreted-text
role="ref"} is not affected by
`Node3D.scale<class_Node3D_property_scale>`{.interpreted-text
role="ref"} (the light\'s scale or its parent\'s scale).
