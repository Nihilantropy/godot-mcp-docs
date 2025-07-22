github_url
:   hide

# CameraAttributes {#class_CameraAttributes}

**Inherits:** `Resource<class_Resource>`{.interpreted-text role="ref"}
**\<** `RefCounted<class_RefCounted>`{.interpreted-text role="ref"}
**\<** `Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`CameraAttributesPhysical<class_CameraAttributesPhysical>`{.interpreted-text
role="ref"},
`CameraAttributesPractical<class_CameraAttributesPractical>`{.interpreted-text
role="ref"}

Parent class for camera settings.

::: rst-class
classref-introduction-group
:::

## Description

Controls camera-specific attributes such as depth of field and exposure
override.

When used in a
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text role="ref"}
it provides default settings for exposure, auto-exposure, and depth of
field that will be used by all cameras without their own
**CameraAttributes**, including the editor camera. When used in a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} it will
override any **CameraAttributes** set in the
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}. When used in `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} or `LightmapGI<class_LightmapGI>`{.interpreted-text
role="ref"}, only the exposure settings will be used.

See also `Environment<class_Environment>`{.interpreted-text role="ref"}
for general 3D environment settings.

This is a pure virtual class that is inherited by
`CameraAttributesPhysical<class_CameraAttributesPhysical>`{.interpreted-text
role="ref"} and
`CameraAttributesPractical<class_CameraAttributesPractical>`{.interpreted-text
role="ref"}.

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

:::: {#class_CameraAttributes_property_auto_exposure_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**auto_exposure_enabled** = `false`
`🔗<class_CameraAttributes_property_auto_exposure_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_exposure_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_auto_exposure_enabled**()

If `true`, enables the tonemapping auto exposure mode of the scene
renderer. If `true`, the renderer will automatically determine the
exposure setting to adapt to the scene\'s illumination and the observed
light.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributes_property_auto_exposure_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**auto_exposure_scale** = `0.4`
`🔗<class_CameraAttributes_property_auto_exposure_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_exposure_scale**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auto_exposure_scale**()

The scale of the auto exposure effect. Affects the intensity of auto
exposure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributes_property_auto_exposure_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**auto_exposure_speed** = `0.5`
`🔗<class_CameraAttributes_property_auto_exposure_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_exposure_speed**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auto_exposure_speed**()

The speed of the auto exposure effect. Affects the time needed for the
camera to perform auto exposure.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributes_property_exposure_multiplier}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**exposure_multiplier** = `1.0`
`🔗<class_CameraAttributes_property_exposure_multiplier>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exposure_multiplier**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_exposure_multiplier**()

Multiplier for the exposure amount. A higher value results in a brighter
image.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributes_property_exposure_sensitivity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**exposure_sensitivity** = `100.0`
`🔗<class_CameraAttributes_property_exposure_sensitivity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_exposure_sensitivity**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_exposure_sensitivity**()

Sensitivity of camera sensors, measured in ISO. A higher sensitivity
results in a brighter image.

If
`auto_exposure_enabled<class_CameraAttributes_property_auto_exposure_enabled>`{.interpreted-text
role="ref"} is `true`, this can be used as a method of exposure
compensation, doubling the value will increase the exposure value
(measured in EV100) by 1 stop.

\*\*Note:\*\* Only available when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is enabled.
