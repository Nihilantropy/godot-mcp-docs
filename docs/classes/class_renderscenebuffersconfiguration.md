github_url
:   hide

# RenderSceneBuffersConfiguration {#class_RenderSceneBuffersConfiguration}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Configuration object used to setup a
`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} object.

::: rst-class
classref-introduction-group
:::

## Description

This configuration object is created and populated by the render engine
on a viewport change and used to (re)configure a
`RenderSceneBuffers<class_RenderSceneBuffers>`{.interpreted-text
role="ref"} object.

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

:::: {#class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level}
::: rst-class
classref-property
:::
::::

`ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
role="ref"} **anisotropic_filtering_level** = `2`
`🔗<class_RenderSceneBuffersConfiguration_property_anisotropic_filtering_level>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_anisotropic_filtering_level**(value:
  `ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
  role="ref"})
- `ViewportAnisotropicFiltering<enum_RenderingServer_ViewportAnisotropicFiltering>`{.interpreted-text
  role="ref"} **get_anisotropic_filtering_level**()

Level of the anisotropic filter.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_fsr_sharpness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fsr_sharpness** =
`0.0`
`🔗<class_RenderSceneBuffersConfiguration_property_fsr_sharpness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fsr_sharpness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fsr_sharpness**()

FSR Sharpness applicable if FSR upscaling is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_internal_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**internal_size** = `Vector2i(0, 0)`
`🔗<class_RenderSceneBuffersConfiguration_property_internal_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_internal_size**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_internal_size**()

The size of the 3D render buffer used for rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_msaa_3d}
::: rst-class
classref-property
:::
::::

`ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
role="ref"} **msaa_3d** = `0`
`🔗<class_RenderSceneBuffersConfiguration_property_msaa_3d>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_msaa_3d**(value:
  `ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
  role="ref"})
- `ViewportMSAA<enum_RenderingServer_ViewportMSAA>`{.interpreted-text
  role="ref"} **get_msaa_3d**()

The MSAA mode we\'re using for 3D rendering.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_render_target}
::: rst-class
classref-property
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **render_target** =
`RID()`
`🔗<class_RenderSceneBuffersConfiguration_property_render_target>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_render_target**(value: `RID<class_RID>`{.interpreted-text
  role="ref"})
- `RID<class_RID>`{.interpreted-text role="ref"} **get_render_target**()

The render target associated with these buffer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_scaling_3d_mode}
::: rst-class
classref-property
:::
::::

`ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
role="ref"} **scaling_3d_mode** = `255`
`🔗<class_RenderSceneBuffersConfiguration_property_scaling_3d_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scaling_3d_mode**(value:
  `ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
  role="ref"})
- `ViewportScaling3DMode<enum_RenderingServer_ViewportScaling3DMode>`{.interpreted-text
  role="ref"} **get_scaling_3d_mode**()

The requested scaling mode with which we upscale/downscale if
`internal_size<class_RenderSceneBuffersConfiguration_property_internal_size>`{.interpreted-text
role="ref"} and
`target_size<class_RenderSceneBuffersConfiguration_property_target_size>`{.interpreted-text
role="ref"} are not equal.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_screen_space_aa}
::: rst-class
classref-property
:::
::::

`ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
role="ref"} **screen_space_aa** = `0`
`🔗<class_RenderSceneBuffersConfiguration_property_screen_space_aa>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_space_aa**(value:
  `ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
  role="ref"})
- `ViewportScreenSpaceAA<enum_RenderingServer_ViewportScreenSpaceAA>`{.interpreted-text
  role="ref"} **get_screen_space_aa**()

The requested screen space AA applied in post processing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_target_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"} **target_size**
= `Vector2i(0, 0)`
`🔗<class_RenderSceneBuffersConfiguration_property_target_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_target_size**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_target_size**()

The target (upscale) size if scaling is used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**texture_mipmap_bias** = `0.0`
`🔗<class_RenderSceneBuffersConfiguration_property_texture_mipmap_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_mipmap_bias**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_mipmap_bias**()

Bias applied to mipmaps.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RenderSceneBuffersConfiguration_property_view_count}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **view_count** = `1`
`🔗<class_RenderSceneBuffersConfiguration_property_view_count>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_view_count**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_view_count**()

The number of views we\'re rendering.
