github_url
:   hide

# MobileVRInterface {#class_MobileVRInterface}

**Inherits:** `XRInterface<class_XRInterface>`{.interpreted-text
role="ref"} **\<** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Generic mobile VR implementation.

::: rst-class
classref-introduction-group
:::

## Description

This is a generic mobile VR implementation where you need to provide
details about the phone and HMD used. It does not rely on any existing
framework. This is the most basic interface we have. For the best
effect, you need a mobile phone with a gyroscope and accelerometer.

Note that even though there is no positional tracking, the camera will
assume the headset is at a height of 1.85 meters. You can change this by
setting
`eye_height<class_MobileVRInterface_property_eye_height>`{.interpreted-text
role="ref"}.

You can initialize this interface as follows:

    var interface = XRServer.find_interface("Native mobile")
    if interface and interface.initialize():
        get_viewport().use_xr = true

\*\*Note:\*\* For Android,
`ProjectSettings.input_devices/sensors/enable_accelerometer<class_ProjectSettings_property_input_devices/sensors/enable_accelerometer>`{.interpreted-text
role="ref"},
`ProjectSettings.input_devices/sensors/enable_gravity<class_ProjectSettings_property_input_devices/sensors/enable_gravity>`{.interpreted-text
role="ref"},
`ProjectSettings.input_devices/sensors/enable_gyroscope<class_ProjectSettings_property_input_devices/sensors/enable_gyroscope>`{.interpreted-text
role="ref"} and
`ProjectSettings.input_devices/sensors/enable_magnetometer<class_ProjectSettings_property_input_devices/sensors/enable_magnetometer>`{.interpreted-text
role="ref"} must be enabled.

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

:::: {#class_MobileVRInterface_property_display_to_lens}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **display_to_lens** =
`4.0`
`🔗<class_MobileVRInterface_property_display_to_lens>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_display_to_lens**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_display_to_lens**()

The distance between the display and the lenses inside of the device in
centimeters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_display_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **display_width** =
`14.5`
`🔗<class_MobileVRInterface_property_display_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_display_width**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_display_width**()

The width of the display in centimeters.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_eye_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **eye_height** =
`1.85`
`🔗<class_MobileVRInterface_property_eye_height>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_eye_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_eye_height**()

The height at which the camera is placed in relation to the ground (i.e.
`XROrigin3D<class_XROrigin3D>`{.interpreted-text role="ref"} node).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_iod}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **iod** = `6.0`
`🔗<class_MobileVRInterface_property_iod>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_iod**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_iod**()

The interocular distance, also known as the interpupillary distance. The
distance between the pupils of the left and right eye.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_k1}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **k1** = `0.215`
`🔗<class_MobileVRInterface_property_k1>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_k1**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_k1**()

The k1 lens factor is one of the two constants that define the strength
of the lens used and directly influences the lens distortion effect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_k2}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **k2** = `0.215`
`🔗<class_MobileVRInterface_property_k2>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_k2**(value: `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_k2**()

The k2 lens factor, see k1.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_offset_rect}
::: rst-class
classref-property
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"} **offset_rect** =
`Rect2(0, 0, 1, 1)`
`🔗<class_MobileVRInterface_property_offset_rect>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_offset_rect**(value: `Rect2<class_Rect2>`{.interpreted-text
  role="ref"})
- `Rect2<class_Rect2>`{.interpreted-text role="ref"}
  **get_offset_rect**()

Set the offset rect relative to the area being rendered. A length of 1
represents the whole rendering area on that axis.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_oversample}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **oversample** =
`1.5`
`🔗<class_MobileVRInterface_property_oversample>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_oversample**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_oversample**()

The oversample setting. Because of the lens distortion we have to render
our buffers at a higher resolution then the screen can natively handle.
A value between 1.5 and 2.0 often provides good results but at the cost
of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_vrs_min_radius}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **vrs_min_radius** =
`20.0`
`🔗<class_MobileVRInterface_property_vrs_min_radius>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_min_radius**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vrs_min_radius**()

The minimum radius around the focal point where full quality is
guaranteed if VRS is used as a percentage of screen size.

\*\*Note:\*\* Mobile and Forward+ renderers only. Requires
`Viewport.vrs_mode<class_Viewport_property_vrs_mode>`{.interpreted-text
role="ref"} to be set to
`Viewport.VRS_XR<class_Viewport_constant_VRS_XR>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_MobileVRInterface_property_vrs_strength}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **vrs_strength** =
`1.0`
`🔗<class_MobileVRInterface_property_vrs_strength>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_strength**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_vrs_strength**()

The strength used to calculate the VRS density map. The greater this
value, the more noticeable VRS is. This improves performance at the cost
of quality.

\*\*Note:\*\* Mobile and Forward+ renderers only. Requires
`Viewport.vrs_mode<class_Viewport_property_vrs_mode>`{.interpreted-text
role="ref"} to be set to
`Viewport.VRS_XR<class_Viewport_constant_VRS_XR>`{.interpreted-text
role="ref"}.
