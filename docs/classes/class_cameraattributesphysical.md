github_url
:   hide

# CameraAttributesPhysical {#class_CameraAttributesPhysical}

**Inherits:**
`CameraAttributes<class_CameraAttributes>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Physically-based camera settings.

::: rst-class
classref-introduction-group
:::

## Description

**CameraAttributesPhysical** is used to set rendering settings based on
a physically-based camera\'s settings. It is responsible for exposure,
auto-exposure, and depth of field.

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
role="ref"} and will override the
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}s
`Camera3D.far<class_Camera3D_property_far>`{.interpreted-text
role="ref"},
`Camera3D.near<class_Camera3D_property_near>`{.interpreted-text
role="ref"},
`Camera3D.fov<class_Camera3D_property_fov>`{.interpreted-text
role="ref"}, and
`Camera3D.keep_aspect<class_Camera3D_property_keep_aspect>`{.interpreted-text
role="ref"} properties. When used in
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} or
`LightmapGI<class_LightmapGI>`{.interpreted-text role="ref"}, only the
exposure settings will be used.

The default settings are intended for use in an outdoor environment,
tips for settings for use in an indoor environment can be found in each
setting\'s documentation.

\*\*Note:\*\* Depth of field blur is only supported in the Forward+ and
Mobile rendering methods, not Compatibility.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Physical light and camera units <../tutorials/3d/physical_light_and_camera_units>`{.interpreted-text
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

## Property Descriptions

:::: {#class_CameraAttributesPhysical_property_auto_exposure_max_exposure_value}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**auto_exposure_max_exposure_value** = `10.0`
`🔗<class_CameraAttributesPhysical_property_auto_exposure_max_exposure_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_exposure_max_exposure_value**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auto_exposure_max_exposure_value**()

The maximum luminance (in EV100) used when calculating auto exposure.
When calculating scene average luminance, color values will be clamped
to at least this value. This limits the auto-exposure from exposing
below a certain brightness, resulting in a cut off point where the scene
will remain bright.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPhysical_property_auto_exposure_min_exposure_value}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**auto_exposure_min_exposure_value** = `-8.0`
`🔗<class_CameraAttributesPhysical_property_auto_exposure_min_exposure_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_auto_exposure_min_exposure_value**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_auto_exposure_min_exposure_value**()

The minimum luminance (in EV100) used when calculating auto exposure.
When calculating scene average luminance, color values will be clamped
to at least this value. This limits the auto-exposure from exposing
above a certain brightness, resulting in a cut off point where the scene
will remain dark.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPhysical_property_exposure_aperture}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **exposure_aperture**
= `16.0`
`🔗<class_CameraAttributesPhysical_property_exposure_aperture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_aperture**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_aperture**()

Size of the aperture of the camera, measured in f-stops. An f-stop is a
unitless ratio between the focal length of the camera and the diameter
of the aperture. A high aperture setting will result in a smaller
aperture which leads to a dimmer image and sharper focus. A low aperture
results in a wide aperture which lets in more light resulting in a
brighter, less-focused image. Default is appropriate for outdoors at
daytime (i.e. for use with a default
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}), for indoor lighting, a value between 2 and 4 is more
appropriate.

Only available when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPhysical_property_exposure_shutter_speed}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**exposure_shutter_speed** = `100.0`
`🔗<class_CameraAttributesPhysical_property_exposure_shutter_speed>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_shutter_speed**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_shutter_speed**()

Time for shutter to open and close, evaluated as `1 / shutter_speed`
seconds. A higher value will allow less light (leading to a darker
image), while a lower value will allow more light (leading to a brighter
image).

Only available when
`ProjectSettings.rendering/lights_and_shadows/use_physical_light_units<class_ProjectSettings_property_rendering/lights_and_shadows/use_physical_light_units>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPhysical_property_frustum_far}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **frustum_far** =
`4000.0`
`🔗<class_CameraAttributesPhysical_property_frustum_far>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_far**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_far**()

Override value for
`Camera3D.far<class_Camera3D_property_far>`{.interpreted-text
role="ref"}. Used internally when calculating depth of field. When
attached to a `Camera3D<class_Camera3D>`{.interpreted-text role="ref"}
as its
`Camera3D.attributes<class_Camera3D_property_attributes>`{.interpreted-text
role="ref"}, it will override the
`Camera3D.far<class_Camera3D_property_far>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPhysical_property_frustum_focal_length}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**frustum_focal_length** = `35.0`
`🔗<class_CameraAttributesPhysical_property_frustum_focal_length>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focal_length**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_focal_length**()

Distance between camera lens and camera aperture, measured in
millimeters. Controls field of view and depth of field. A larger focal
length will result in a smaller field of view and a narrower depth of
field meaning fewer objects will be in focus. A smaller focal length
will result in a wider field of view and a larger depth of field meaning
more objects will be in focus. When attached to a
`Camera3D<class_Camera3D>`{.interpreted-text role="ref"} as its
`Camera3D.attributes<class_Camera3D_property_attributes>`{.interpreted-text
role="ref"}, it will override the
`Camera3D.fov<class_Camera3D_property_fov>`{.interpreted-text
role="ref"} property and the
`Camera3D.keep_aspect<class_Camera3D_property_keep_aspect>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPhysical_property_frustum_focus_distance}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**frustum_focus_distance** = `10.0`
`🔗<class_CameraAttributesPhysical_property_frustum_focus_distance>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_focus_distance**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_focus_distance**()

Distance from camera of object that will be in focus, measured in
meters. Internally this will be clamped to be at least 1 millimeter
larger than
`frustum_focal_length<class_CameraAttributesPhysical_property_frustum_focal_length>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CameraAttributesPhysical_property_frustum_near}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **frustum_near** =
`0.05`
`🔗<class_CameraAttributesPhysical_property_frustum_near>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_near**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_near**()

Override value for
`Camera3D.near<class_Camera3D_property_near>`{.interpreted-text
role="ref"}. Used internally when calculating depth of field. When
attached to a `Camera3D<class_Camera3D>`{.interpreted-text role="ref"}
as its
`Camera3D.attributes<class_Camera3D_property_attributes>`{.interpreted-text
role="ref"}, it will override the
`Camera3D.near<class_Camera3D_property_near>`{.interpreted-text
role="ref"} property.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_CameraAttributesPhysical_method_get_fov}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **get_fov**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_CameraAttributesPhysical_method_get_fov>`{.interpreted-text
role="ref"}

Returns the vertical field of view that corresponds to the
`frustum_focal_length<class_CameraAttributesPhysical_property_frustum_focal_length>`{.interpreted-text
role="ref"}. This value is calculated internally whenever
`frustum_focal_length<class_CameraAttributesPhysical_property_frustum_focal_length>`{.interpreted-text
role="ref"} is changed.
