github_url
:   hide

# CameraAttributesPractical {#class_CameraAttributesPractical}

**Inherits:**
`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Camera settings in an easy to use format.

::: rst-class
classref-introduction-group
:::

## Description

Controls camera-specific attributes such as auto-exposure, depth of
field, and exposure override.

When used in a
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text role="ref"}
it provides default settings for exposure, auto-exposure, and depth of
field that will be used by all cameras without their own
`CameraAttributes<class_CameraAttributes>`{.interpreted-text
role="ref"}, including the editor camera. When used in a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} it will
override any
`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
set in the `WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}. When used in `VoxelGI<class_VoxelGI>`{.interpreted-text
role="ref"} or `LightmapGI<class_LightmapGI>`{.interpreted-text
role="ref"}, only the exposure settings will be used.

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

:::: {#class_CameraAttributesPractical_property_auto_exposure_max_sensitivity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**auto_exposure_max_sensitivity** = `800.0`
`🔗<class_CameraAttributesPractical_property_auto_exposure_max_sensitivity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_exposure_max_sensitivity**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auto_exposure_max_sensitivity**()

The maximum sensitivity (in ISO) used when calculating auto exposure.
When calculating scene average luminance, color values will be clamped
to at least this value. This limits the auto-exposure from exposing
below a certain brightness, resulting in a cut off point where the scene
will remain bright.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_auto_exposure_min_sensitivity}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**auto_exposure_min_sensitivity** = `0.0`
`🔗<class_CameraAttributesPractical_property_auto_exposure_min_sensitivity>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_exposure_min_sensitivity**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auto_exposure_min_sensitivity**()

The minimum sensitivity (in ISO) used when calculating auto exposure.
When calculating scene average luminance, color values will be clamped
to at least this value. This limits the auto-exposure from exposing
above a certain brightness, resulting in a cut off point where the scene
will remain dark.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_dof_blur_amount}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **dof_blur_amount** =
`0.1`
`🔗<class_CameraAttributesPractical_property_dof_blur_amount>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dof_blur_amount**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_dof_blur_amount**()

Sets the maximum amount of blur. When using physically-based blur
amounts, will instead act as a multiplier. High values lead to an
increased amount of blurriness, but can be much more expensive to
calculate. It is best to keep this as low as possible for a given art
style.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_dof_blur_far_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**dof_blur_far_distance** = `10.0`
`🔗<class_CameraAttributesPractical_property_dof_blur_far_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dof_blur_far_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_dof_blur_far_distance**()

Objects further from the `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"} by this amount will be blurred by the depth of field effect.
Measured in meters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_dof_blur_far_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**dof_blur_far_enabled** = `false`
`🔗<class_CameraAttributesPractical_property_dof_blur_far_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dof_blur_far_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_dof_blur_far_enabled**()

Enables depth of field blur for objects further than
`dof_blur_far_distance<class_CameraAttributesPractical_property_dof_blur_far_distance>`{.interpreted-text
role="ref"}. Strength of blur is controlled by
`dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>`{.interpreted-text
role="ref"} and modulated by
`dof_blur_far_transition<class_CameraAttributesPractical_property_dof_blur_far_transition>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Depth of field blur is only supported in the Forward+ and
Mobile rendering methods, not Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_dof_blur_far_transition}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**dof_blur_far_transition** = `5.0`
`🔗<class_CameraAttributesPractical_property_dof_blur_far_transition>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dof_blur_far_transition**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_dof_blur_far_transition**()

When positive, distance over which (starting from
`dof_blur_far_distance<class_CameraAttributesPractical_property_dof_blur_far_distance>`{.interpreted-text
role="ref"}) blur effect will scale from 0 to
`dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>`{.interpreted-text
role="ref"}. When negative, uses physically-based scaling so depth of
field effect will scale from 0 at
`dof_blur_far_distance<class_CameraAttributesPractical_property_dof_blur_far_distance>`{.interpreted-text
role="ref"} and will increase in a physically accurate way as objects
get further from the `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_dof_blur_near_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**dof_blur_near_distance** = `2.0`
`🔗<class_CameraAttributesPractical_property_dof_blur_near_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dof_blur_near_distance**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_dof_blur_near_distance**()

Objects closer from the `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"} by this amount will be blurred by the depth of field effect.
Measured in meters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_dof_blur_near_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**dof_blur_near_enabled** = `false`
`🔗<class_CameraAttributesPractical_property_dof_blur_near_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dof_blur_near_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_dof_blur_near_enabled**()

Enables depth of field blur for objects closer than
`dof_blur_near_distance<class_CameraAttributesPractical_property_dof_blur_near_distance>`{.interpreted-text
role="ref"}. Strength of blur is controlled by
`dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>`{.interpreted-text
role="ref"} and modulated by
`dof_blur_near_transition<class_CameraAttributesPractical_property_dof_blur_near_transition>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Depth of field blur is only supported in the Forward+ and
Mobile rendering methods, not Compatibility.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPractical_property_dof_blur_near_transition}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**dof_blur_near_transition** = `1.0`
`🔗<class_CameraAttributesPractical_property_dof_blur_near_transition>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dof_blur_near_transition**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_dof_blur_near_transition**()

When positive, distance over which blur effect will scale from 0 to
`dof_blur_amount<class_CameraAttributesPractical_property_dof_blur_amount>`{.interpreted-text
role="ref"}, ending at
`dof_blur_near_distance<class_CameraAttributesPractical_property_dof_blur_near_distance>`{.interpreted-text
role="ref"}. When negative, uses physically-based scaling so depth of
field effect will scale from 0 at
`dof_blur_near_distance<class_CameraAttributesPractical_property_dof_blur_near_distance>`{.interpreted-text
role="ref"} and will increase in a physically accurate way as objects
get closer to the `Camera3D<class_Camera3D>`{.interpreted-text
role="ref"}.
