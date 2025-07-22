github_url
:   hide

# OpenXRCompositionLayer {#class_OpenXRCompositionLayer}

**Experimental:** This class may be changed or removed in future
versions.

**Inherits:** `Node3D<class_Node3D>`{.interpreted-text role="ref"}
**\<** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`OpenXRCompositionLayerCylinder<class_OpenXRCompositionLayerCylinder>`{.interpreted-text
role="ref"},
`OpenXRCompositionLayerEquirect<class_OpenXRCompositionLayerEquirect>`{.interpreted-text
role="ref"},
`OpenXRCompositionLayerQuad<class_OpenXRCompositionLayerQuad>`{.interpreted-text
role="ref"}

The parent class of all OpenXR composition layer nodes.

::: rst-class
classref-introduction-group
:::

## Description

Composition layers allow 2D viewports to be displayed inside of the
headset by the XR compositor through special projections that retain
their quality. This allows for rendering clear text while keeping the
layer at a native resolution.

\*\*Note:\*\* If the OpenXR runtime doesn\'t support the given
composition layer type, a fallback mesh can be generated with a
`ViewportTexture<class_ViewportTexture>`{.interpreted-text role="ref"},
in order to emulate the composition layer.

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

## Enumerations

:::: {#enum_OpenXRCompositionLayer_Filter}
::: rst-class
classref-enumeration
:::
::::

enum **Filter**:
`🔗<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text role="ref"}

:::: {#class_OpenXRCompositionLayer_constant_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
role="ref"} **FILTER_NEAREST** = `0`

Perform nearest-neighbor filtering when sampling the texture.

:::: {#class_OpenXRCompositionLayer_constant_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
role="ref"} **FILTER_LINEAR** = `1`

Perform linear filtering when sampling the texture.

:::: {#class_OpenXRCompositionLayer_constant_FILTER_CUBIC}
::: rst-class
classref-enumeration-constant
:::
::::

`Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
role="ref"} **FILTER_CUBIC** = `2`

Perform cubic filtering when sampling the texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRCompositionLayer_MipmapMode}
::: rst-class
classref-enumeration
:::
::::

enum **MipmapMode**:
`🔗<enum_OpenXRCompositionLayer_MipmapMode>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRCompositionLayer_constant_MIPMAP_MODE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>`{.interpreted-text
role="ref"} **MIPMAP_MODE_DISABLED** = `0`

Disable mipmapping.

\*\*Note:\*\* Mipmapping can only be disabled in the Compatibility
renderer.

:::: {#class_OpenXRCompositionLayer_constant_MIPMAP_MODE_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>`{.interpreted-text
role="ref"} **MIPMAP_MODE_NEAREST** = `1`

Use the mipmap of the nearest resolution.

:::: {#class_OpenXRCompositionLayer_constant_MIPMAP_MODE_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>`{.interpreted-text
role="ref"} **MIPMAP_MODE_LINEAR** = `2`

Use linear interpolation of the two mipmaps of the nearest resolution.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRCompositionLayer_Wrap}
::: rst-class
classref-enumeration
:::
::::

enum **Wrap**: `🔗<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text
role="ref"}

:::: {#class_OpenXRCompositionLayer_constant_WRAP_CLAMP_TO_BORDER}
::: rst-class
classref-enumeration-constant
:::
::::

`Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
**WRAP_CLAMP_TO_BORDER** = `0`

Clamp the texture to its specified border color.

:::: {#class_OpenXRCompositionLayer_constant_WRAP_CLAMP_TO_EDGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
**WRAP_CLAMP_TO_EDGE** = `1`

Clamp the texture to its edge color.

:::: {#class_OpenXRCompositionLayer_constant_WRAP_REPEAT}
::: rst-class
classref-enumeration-constant
:::
::::

`Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
**WRAP_REPEAT** = `2`

Repeat the texture infinitely.

:::: {#class_OpenXRCompositionLayer_constant_WRAP_MIRRORED_REPEAT}
::: rst-class
classref-enumeration-constant
:::
::::

`Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
**WRAP_MIRRORED_REPEAT** = `3`

Repeat the texture infinitely, mirroring it on each repeat.

:::: {#class_OpenXRCompositionLayer_constant_WRAP_MIRROR_CLAMP_TO_EDGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
**WRAP_MIRROR_CLAMP_TO_EDGE** = `4`

Mirror the texture once and then clamp the texture to its edge color.

\*\*Note:\*\* This wrap mode is not available in the Compatibility
renderer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_OpenXRCompositionLayer_Swizzle}
::: rst-class
classref-enumeration
:::
::::

enum **Swizzle**:
`🔗<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text role="ref"}

:::: {#class_OpenXRCompositionLayer_constant_SWIZZLE_RED}
::: rst-class
classref-enumeration-constant
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **SWIZZLE_RED** = `0`

Maps a color channel to the value of the red channel.

:::: {#class_OpenXRCompositionLayer_constant_SWIZZLE_GREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **SWIZZLE_GREEN** = `1`

Maps a color channel to the value of the green channel.

:::: {#class_OpenXRCompositionLayer_constant_SWIZZLE_BLUE}
::: rst-class
classref-enumeration-constant
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **SWIZZLE_BLUE** = `2`

Maps a color channel to the value of the blue channel.

:::: {#class_OpenXRCompositionLayer_constant_SWIZZLE_ALPHA}
::: rst-class
classref-enumeration-constant
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **SWIZZLE_ALPHA** = `3`

Maps a color channel to the value of the alpha channel.

:::: {#class_OpenXRCompositionLayer_constant_SWIZZLE_ZERO}
::: rst-class
classref-enumeration-constant
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **SWIZZLE_ZERO** = `4`

Maps a color channel to the value of zero.

:::: {#class_OpenXRCompositionLayer_constant_SWIZZLE_ONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **SWIZZLE_ONE** = `5`

Maps a color channel to the value of one.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_OpenXRCompositionLayer_property_alpha_blend}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **alpha_blend** =
`false`
`🔗<class_OpenXRCompositionLayer_property_alpha_blend>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_blend**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_alpha_blend**()

Enables the blending the layer using its alpha channel.

Can be combined with
`Viewport.transparent_bg<class_Viewport_property_transparent_bg>`{.interpreted-text
role="ref"} to give the layer a transparent background.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_android_surface_size}
::: rst-class
classref-property
:::
::::

`Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
**android_surface_size** = `Vector2i(1024, 1024)`
`🔗<class_OpenXRCompositionLayer_property_android_surface_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_android_surface_size**(value:
  `Vector2i<class_Vector2i>`{.interpreted-text role="ref"})
- `Vector2i<class_Vector2i>`{.interpreted-text role="ref"}
  **get_android_surface_size**()

The size of the Android surface to create if
`use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"} is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_enable_hole_punch}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_hole_punch** =
`false`
`🔗<class_OpenXRCompositionLayer_property_enable_hole_punch>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_hole_punch**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_hole_punch**()

Enables a technique called \"hole punching\", which allows putting the
composition layer behind the main projection layer (i.e. setting
`sort_order<class_OpenXRCompositionLayer_property_sort_order>`{.interpreted-text
role="ref"} to a negative value) while \"punching a hole\" through
everything rendered by Godot so that the layer is still visible.

This can be used to create the illusion that the composition layer
exists in the same 3D space as everything rendered by Godot, allowing
objects to appear to pass both behind or in front of the composition
layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_layer_viewport}
::: rst-class
classref-property
:::
::::

`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
**layer_viewport**
`🔗<class_OpenXRCompositionLayer_property_layer_viewport>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_layer_viewport**(value:
  `SubViewport<class_SubViewport>`{.interpreted-text role="ref"})
- `SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
  **get_layer_viewport**()

The `SubViewport<class_SubViewport>`{.interpreted-text role="ref"} to
render on the composition layer.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_sort_order}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **sort_order** = `1`
`🔗<class_OpenXRCompositionLayer_property_sort_order>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sort_order**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_sort_order**()

The sort order for this composition layer. Higher numbers will be shown
in front of lower numbers.

\*\*Note:\*\* This will have no effect if a fallback mesh is being used.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_alpha_swizzle}
::: rst-class
classref-property
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **swapchain_state_alpha_swizzle** = `3`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_alpha_swizzle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_swizzle**(value:
  `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"})
- `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"} **get_alpha_swizzle**()

The swizzle value for the alpha channel of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_blue_swizzle}
::: rst-class
classref-property
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **swapchain_state_blue_swizzle** = `2`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_blue_swizzle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blue_swizzle**(value:
  `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"})
- `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"} **get_blue_swizzle**()

The swizzle value for the blue channel of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_border_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"}
**swapchain_state_border_color** = `Color(0, 0, 0, 0)`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_border_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_border_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_border_color**()

The border color of the swapchain state that is used when the wrap mode
clamps to the border.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_green_swizzle}
::: rst-class
classref-property
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **swapchain_state_green_swizzle** = `1`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_green_swizzle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_green_swizzle**(value:
  `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"})
- `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"} **get_green_swizzle**()

The swizzle value for the green channel of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_horizontal_wrap}
::: rst-class
classref-property
:::
::::

`Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
**swapchain_state_horizontal_wrap** = `0`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_horizontal_wrap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_horizontal_wrap**(value:
  `Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text
  role="ref"})
- `Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
  **get_horizontal_wrap**()

The horizontal wrap mode of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_mag_filter}
::: rst-class
classref-property
:::
::::

`Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
role="ref"} **swapchain_state_mag_filter** = `1`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_mag_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mag_filter**(value:
  `Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
  role="ref"})
- `Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
  role="ref"} **get_mag_filter**()

The magnification filter of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_max_anisotropy}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**swapchain_state_max_anisotropy** = `1.0`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_max_anisotropy>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_max_anisotropy**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_max_anisotropy**()

The max anisotropy of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_min_filter}
::: rst-class
classref-property
:::
::::

`Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
role="ref"} **swapchain_state_min_filter** = `1`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_min_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_min_filter**(value:
  `Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
  role="ref"})
- `Filter<enum_OpenXRCompositionLayer_Filter>`{.interpreted-text
  role="ref"} **get_min_filter**()

The minification filter of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_mipmap_mode}
::: rst-class
classref-property
:::
::::

`MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>`{.interpreted-text
role="ref"} **swapchain_state_mipmap_mode** = `2`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_mipmap_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mipmap_mode**(value:
  `MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>`{.interpreted-text
  role="ref"})
- `MipmapMode<enum_OpenXRCompositionLayer_MipmapMode>`{.interpreted-text
  role="ref"} **get_mipmap_mode**()

The mipmap mode of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_red_swizzle}
::: rst-class
classref-property
:::
::::

`Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
role="ref"} **swapchain_state_red_swizzle** = `0`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_red_swizzle>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_red_swizzle**(value:
  `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"})
- `Swizzle<enum_OpenXRCompositionLayer_Swizzle>`{.interpreted-text
  role="ref"} **get_red_swizzle**()

The swizzle value for the red channel of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_swapchain_state_vertical_wrap}
::: rst-class
classref-property
:::
::::

`Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
**swapchain_state_vertical_wrap** = `0`
`🔗<class_OpenXRCompositionLayer_property_swapchain_state_vertical_wrap>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vertical_wrap**(value:
  `Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text
  role="ref"})
- `Wrap<enum_OpenXRCompositionLayer_Wrap>`{.interpreted-text role="ref"}
  **get_vertical_wrap**()

The vertical wrap mode of the swapchain state.

\*\*Note:\*\* This property only has an effect on devices that support
the OpenXR XR_FB_swapchain_update_state OpenGLES/Vulkan extensions.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_property_use_android_surface}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_android_surface**
= `false`
`🔗<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_android_surface**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_use_android_surface**()

If enabled, an Android surface will be created (with the dimensions from
`android_surface_size<class_OpenXRCompositionLayer_property_android_surface_size>`{.interpreted-text
role="ref"}) which will provide the 2D content for the composition
layer, rather than using
`layer_viewport<class_OpenXRCompositionLayer_property_layer_viewport>`{.interpreted-text
role="ref"}.

See
`get_android_surface()<class_OpenXRCompositionLayer_method_get_android_surface>`{.interpreted-text
role="ref"} for information about how to get the surface so that your
application can draw to it.

\*\*Note:\*\* This will only work in Android builds.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_OpenXRCompositionLayer_method_get_android_surface}
::: rst-class
classref-method
:::
::::

`JavaObject<class_JavaObject>`{.interpreted-text role="ref"}
**get_android_surface**()
`🔗<class_OpenXRCompositionLayer_method_get_android_surface>`{.interpreted-text
role="ref"}

Returns a `JavaObject<class_JavaObject>`{.interpreted-text role="ref"}
representing an `android.view.Surface` if
`use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"} is enabled and OpenXR has created the surface. Otherwise,
this will return `null`.

\*\*Note:\*\* The surface can only be created during an active OpenXR
session. So, if
`use_android_surface<class_OpenXRCompositionLayer_property_use_android_surface>`{.interpreted-text
role="ref"} is enabled outside of an OpenXR session, it won\'t be
created until a new session fully starts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_method_intersects_ray}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**intersects_ray**(origin: `Vector3<class_Vector3>`{.interpreted-text
role="ref"}, direction: `Vector3<class_Vector3>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRCompositionLayer_method_intersects_ray>`{.interpreted-text
role="ref"}

Returns UV coordinates where the given ray intersects with the
composition layer. `origin` and `direction` must be in global space.

Returns `Vector2(-1.0, -1.0)` if the ray doesn\'t intersect.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_OpenXRCompositionLayer_method_is_natively_supported}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**is_natively_supported**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_OpenXRCompositionLayer_method_is_natively_supported>`{.interpreted-text
role="ref"}

Returns `true` if the OpenXR runtime natively supports this composition
layer type.

\*\*Note:\*\* This will only return an accurate result after the OpenXR
session has started.
