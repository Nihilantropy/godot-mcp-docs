github_url
:   hide

# Viewport {#class_Viewport}

**Inherits:** `Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:** `SubViewport<class_SubViewport>`{.interpreted-text
role="ref"}, `Window<class_Window>`{.interpreted-text role="ref"}

Abstract base class for viewports. Encapsulates drawing and interaction
with a game world.

::: rst-class
classref-introduction-group
:::

## Description

A **Viewport** creates a different view into the screen, or a sub-view
inside another viewport. Child 2D nodes will display on it, and child
Camera3D 3D nodes will render on it too.

Optionally, a viewport can have its own 2D or 3D world, so it doesn\'t
share what it draws with other viewports.

Viewports can also choose to be audio listeners, so they generate
positional audio depending on a 2D or 3D camera child of it.

Also, viewports can be assigned to different screens in case the devices
have multiple screens.

Finally, viewports can also behave as render targets, in which case they
will not be visible unless the associated texture is used to draw.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `Using Viewports <../tutorials/rendering/viewports>`{.interpreted-text
  role="doc"}
- `Viewport and canvas transforms <../tutorials/2d/2d_transforms>`{.interpreted-text
  role="doc"}
- [GUI in 3D Viewport
  Demo](https://godotengine.org/asset-library/asset/2807)
- [3D in 2D Viewport
  Demo](https://godotengine.org/asset-library/asset/2804)
- [2D in 3D Viewport
  Demo](https://godotengine.org/asset-library/asset/2803)
- [Screen Capture
  Demo](https://godotengine.org/asset-library/asset/2808)
- [Dynamic Split Screen
  Demo](https://godotengine.org/asset-library/asset/2806)
- [3D Resolution Scaling
  Demo](https://godotengine.org/asset-library/asset/2805)

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

## Signals

:::: {#class_Viewport_signal_gui_focus_changed}
::: rst-class
classref-signal
:::
::::

**gui_focus_changed**(node: `Control<class_Control>`{.interpreted-text
role="ref"})
`🔗<class_Viewport_signal_gui_focus_changed>`{.interpreted-text
role="ref"}

Emitted when a Control node grabs keyboard focus.

\*\*Note:\*\* A Control node losing focus doesn\'t cause this signal to
be emitted.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_signal_size_changed}
::: rst-class
classref-signal
:::
::::

**size_changed**()
`🔗<class_Viewport_signal_size_changed>`{.interpreted-text role="ref"}

Emitted when the size of the viewport is changed, whether by resizing of
window, or some other means.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Enumerations

:::: {#enum_Viewport_PositionalShadowAtlasQuadrantSubdiv}
::: rst-class
classref-enumeration
:::
::::

enum **PositionalShadowAtlasQuadrantSubdiv**:
`🔗<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_DISABLED** = `0`

This quadrant will not be used.

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_1}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_1** = `1`

This quadrant will only be used by one shadow map.

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_4}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_4** = `2`

This quadrant will be split in 4 and used by up to 4 shadow maps.

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_16}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_16** = `3`

This quadrant will be split 16 ways and used by up to 16 shadow maps.

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_64}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_64** = `4`

This quadrant will be split 64 ways and used by up to 64 shadow maps.

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_256}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_256** = `5`

This quadrant will be split 256 ways and used by up to 256 shadow maps.
Unless the
`positional_shadow_atlas_size<class_Viewport_property_positional_shadow_atlas_size>`{.interpreted-text
role="ref"} is very high, the shadows in this quadrant will be very low
resolution.

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_1024}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_1024** = `6`

This quadrant will be split 1024 ways and used by up to 1024 shadow
maps. Unless the
`positional_shadow_atlas_size<class_Viewport_property_positional_shadow_atlas_size>`{.interpreted-text
role="ref"} is very high, the shadows in this quadrant will be very low
resolution.

:::: {#class_Viewport_constant_SHADOW_ATLAS_QUADRANT_SUBDIV_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **SHADOW_ATLAS_QUADRANT_SUBDIV_MAX** = `7`

Represents the size of the
`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_Scaling3DMode}
::: rst-class
classref-enumeration
:::
::::

enum **Scaling3DMode**:
`🔗<enum_Viewport_Scaling3DMode>`{.interpreted-text role="ref"}

:::: {#class_Viewport_constant_SCALING_3D_MODE_BILINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} **SCALING_3D_MODE_BILINEAR** = `0`

Use bilinear scaling for the viewport\'s 3D buffer. The amount of
scaling can be set using
`scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in undersampling while
values greater than `1.0` will result in supersampling. A value of `1.0`
disables scaling.

:::: {#class_Viewport_constant_SCALING_3D_MODE_FSR}
::: rst-class
classref-enumeration-constant
:::
::::

`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} **SCALING_3D_MODE_FSR** = `1`

Use AMD FidelityFX Super Resolution 1.0 upscaling for the viewport\'s 3D
buffer. The amount of scaling can be set using
`scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in the viewport being
upscaled using FSR. Values greater than `1.0` are not supported and
bilinear downsampling will be used instead. A value of `1.0` disables
scaling.

:::: {#class_Viewport_constant_SCALING_3D_MODE_FSR2}
::: rst-class
classref-enumeration-constant
:::
::::

`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} **SCALING_3D_MODE_FSR2** = `2`

Use AMD FidelityFX Super Resolution 2.2 upscaling for the viewport\'s 3D
buffer. The amount of scaling can be set using
`scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. Values less than `1.0` will result in the viewport being
upscaled using FSR2. Values greater than `1.0` are not supported and
bilinear downsampling will be used instead. A value of `1.0` will use
FSR2 at native resolution as a TAA solution.

:::: {#class_Viewport_constant_SCALING_3D_MODE_METALFX_SPATIAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} **SCALING_3D_MODE_METALFX_SPATIAL** = `3`

Use the [MetalFX spatial
upscaler](https://developer.apple.com/documentation/metalfx/mtlfxspatialscaler#overview)
for the viewport\'s 3D buffer.

The amount of scaling can be set using
`scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}.

Values less than `1.0` will result in the viewport being upscaled using
MetalFX. Values greater than `1.0` are not supported and bilinear
downsampling will be used instead. A value of `1.0` disables scaling.

More information:
[MetalFX](https://developer.apple.com/documentation/metalfx).

\*\*Note:\*\* Only supported when the Metal rendering driver is in use,
which limits this scaling mode to macOS and iOS.

:::: {#class_Viewport_constant_SCALING_3D_MODE_METALFX_TEMPORAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} **SCALING_3D_MODE_METALFX_TEMPORAL** = `4`

Use the [MetalFX temporal
upscaler](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscaler#overview)
for the viewport\'s 3D buffer.

The amount of scaling can be set using
`scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}. To determine the minimum input scale, use the
`RenderingDevice.limit_get()<class_RenderingDevice_method_limit_get>`{.interpreted-text
role="ref"} method with
`RenderingDevice.LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE<class_RenderingDevice_constant_LIMIT_METALFX_TEMPORAL_SCALER_MIN_SCALE>`{.interpreted-text
role="ref"}.

Values less than `1.0` will result in the viewport being upscaled using
MetalFX. Values greater than `1.0` are not supported and bilinear
downsampling will be used instead. A value of `1.0` will use MetalFX at
native resolution as a TAA solution.

More information:
[MetalFX](https://developer.apple.com/documentation/metalfx).

\*\*Note:\*\* Only supported when the Metal rendering driver is in use,
which limits this scaling mode to macOS and iOS.

:::: {#class_Viewport_constant_SCALING_3D_MODE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} **SCALING_3D_MODE_MAX** = `5`

Represents the size of the
`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_MSAA}
::: rst-class
classref-enumeration
:::
::::

enum **MSAA**: `🔗<enum_Viewport_MSAA>`{.interpreted-text role="ref"}

:::: {#class_Viewport_constant_MSAA_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"}
**MSAA_DISABLED** = `0`

Multisample antialiasing mode disabled. This is the default value, and
is also the fastest setting.

:::: {#class_Viewport_constant_MSAA_2X}
::: rst-class
classref-enumeration-constant
:::
::::

`MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"} **MSAA_2X** =
`1`

Use 2× Multisample Antialiasing. This has a moderate performance cost.
It helps reduce aliasing noticeably, but 4× MSAA still looks
substantially better.

:::: {#class_Viewport_constant_MSAA_4X}
::: rst-class
classref-enumeration-constant
:::
::::

`MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"} **MSAA_4X** =
`2`

Use 4× Multisample Antialiasing. This has a significant performance
cost, and is generally a good compromise between performance and
quality.

:::: {#class_Viewport_constant_MSAA_8X}
::: rst-class
classref-enumeration-constant
:::
::::

`MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"} **MSAA_8X** =
`3`

Use 8× Multisample Antialiasing. This has a very high performance cost.
The difference between 4× and 8× MSAA may not always be visible in real
gameplay conditions. Likely unsupported on low-end and older hardware.

:::: {#class_Viewport_constant_MSAA_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"} **MSAA_MAX** =
`4`

Represents the size of the `MSAA<enum_Viewport_MSAA>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_AnisotropicFiltering}
::: rst-class
classref-enumeration
:::
::::

enum **AnisotropicFiltering**:
`🔗<enum_Viewport_AnisotropicFiltering>`{.interpreted-text role="ref"}

:::: {#class_Viewport_constant_ANISOTROPY_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} **ANISOTROPY_DISABLED** = `0`

Anisotropic filtering is disabled.

:::: {#class_Viewport_constant_ANISOTROPY_2X}
::: rst-class
classref-enumeration-constant
:::
::::

`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} **ANISOTROPY_2X** = `1`

Use 2× anisotropic filtering.

:::: {#class_Viewport_constant_ANISOTROPY_4X}
::: rst-class
classref-enumeration-constant
:::
::::

`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} **ANISOTROPY_4X** = `2`

Use 4× anisotropic filtering. This is the default value.

:::: {#class_Viewport_constant_ANISOTROPY_8X}
::: rst-class
classref-enumeration-constant
:::
::::

`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} **ANISOTROPY_8X** = `3`

Use 8× anisotropic filtering.

:::: {#class_Viewport_constant_ANISOTROPY_16X}
::: rst-class
classref-enumeration-constant
:::
::::

`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} **ANISOTROPY_16X** = `4`

Use 16× anisotropic filtering.

:::: {#class_Viewport_constant_ANISOTROPY_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} **ANISOTROPY_MAX** = `5`

Represents the size of the
`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_ScreenSpaceAA}
::: rst-class
classref-enumeration
:::
::::

enum **ScreenSpaceAA**:
`🔗<enum_Viewport_ScreenSpaceAA>`{.interpreted-text role="ref"}

:::: {#class_Viewport_constant_SCREEN_SPACE_AA_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
role="ref"} **SCREEN_SPACE_AA_DISABLED** = `0`

Do not perform any antialiasing in the full screen post-process.

:::: {#class_Viewport_constant_SCREEN_SPACE_AA_FXAA}
::: rst-class
classref-enumeration-constant
:::
::::

`ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
role="ref"} **SCREEN_SPACE_AA_FXAA** = `1`

Use fast approximate antialiasing. FXAA is a popular screen-space
antialiasing method, which is fast but will make the image look blurry,
especially at lower resolutions. It can still work relatively well at
large resolutions such as 1440p and 4K.

:::: {#class_Viewport_constant_SCREEN_SPACE_AA_SMAA}
::: rst-class
classref-enumeration-constant
:::
::::

`ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
role="ref"} **SCREEN_SPACE_AA_SMAA** = `2`

Use subpixel morphological antialiasing. SMAA may produce clearer
results than FXAA, but at a slightly higher performance cost.

:::: {#class_Viewport_constant_SCREEN_SPACE_AA_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
role="ref"} **SCREEN_SPACE_AA_MAX** = `3`

Represents the size of the
`ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_RenderInfo}
::: rst-class
classref-enumeration
:::
::::

enum **RenderInfo**: `🔗<enum_Viewport_RenderInfo>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_RENDER_INFO_OBJECTS_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfo<enum_Viewport_RenderInfo>`{.interpreted-text role="ref"}
**RENDER_INFO_OBJECTS_IN_FRAME** = `0`

Amount of objects in frame.

:::: {#class_Viewport_constant_RENDER_INFO_PRIMITIVES_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfo<enum_Viewport_RenderInfo>`{.interpreted-text role="ref"}
**RENDER_INFO_PRIMITIVES_IN_FRAME** = `1`

Amount of vertices in frame.

:::: {#class_Viewport_constant_RENDER_INFO_DRAW_CALLS_IN_FRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfo<enum_Viewport_RenderInfo>`{.interpreted-text role="ref"}
**RENDER_INFO_DRAW_CALLS_IN_FRAME** = `2`

Amount of draw calls in frame.

:::: {#class_Viewport_constant_RENDER_INFO_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfo<enum_Viewport_RenderInfo>`{.interpreted-text role="ref"}
**RENDER_INFO_MAX** = `3`

Represents the size of the
`RenderInfo<enum_Viewport_RenderInfo>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_RenderInfoType}
::: rst-class
classref-enumeration
:::
::::

enum **RenderInfoType**:
`🔗<enum_Viewport_RenderInfoType>`{.interpreted-text role="ref"}

:::: {#class_Viewport_constant_RENDER_INFO_TYPE_VISIBLE}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfoType<enum_Viewport_RenderInfoType>`{.interpreted-text
role="ref"} **RENDER_INFO_TYPE_VISIBLE** = `0`

Visible render pass (excluding shadows).

:::: {#class_Viewport_constant_RENDER_INFO_TYPE_SHADOW}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfoType<enum_Viewport_RenderInfoType>`{.interpreted-text
role="ref"} **RENDER_INFO_TYPE_SHADOW** = `1`

Shadow render pass. Objects will be rendered several times depending on
the number of amounts of lights with shadows and the number of
directional shadow splits.

:::: {#class_Viewport_constant_RENDER_INFO_TYPE_CANVAS}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfoType<enum_Viewport_RenderInfoType>`{.interpreted-text
role="ref"} **RENDER_INFO_TYPE_CANVAS** = `2`

Canvas item rendering. This includes all 2D rendering.

:::: {#class_Viewport_constant_RENDER_INFO_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`RenderInfoType<enum_Viewport_RenderInfoType>`{.interpreted-text
role="ref"} **RENDER_INFO_TYPE_MAX** = `3`

Represents the size of the
`RenderInfoType<enum_Viewport_RenderInfoType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_DebugDraw}
::: rst-class
classref-enumeration
:::
::::

enum **DebugDraw**: `🔗<enum_Viewport_DebugDraw>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_DEBUG_DRAW_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_DISABLED** = `0`

Objects are displayed normally.

:::: {#class_Viewport_constant_DEBUG_DRAW_UNSHADED}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_UNSHADED** = `1`

Objects are displayed without light information.

:::: {#class_Viewport_constant_DEBUG_DRAW_LIGHTING}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_LIGHTING** = `2`

Objects are displayed without textures and only with lighting
information.

\*\*Note:\*\* When using this debug draw mode, custom shaders are
ignored since all materials in the scene temporarily use a debug
material. This means the result from custom shader functions (such as
vertex displacement) won\'t be visible anymore when using this debug
draw mode.

:::: {#class_Viewport_constant_DEBUG_DRAW_OVERDRAW}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_OVERDRAW** = `3`

Objects are displayed semi-transparent with additive blending so you can
see where they are drawing over top of one another. A higher overdraw
means you are wasting performance on drawing pixels that are being
hidden behind others.

\*\*Note:\*\* When using this debug draw mode, custom shaders are
ignored since all materials in the scene temporarily use a debug
material. This means the result from custom shader functions (such as
vertex displacement) won\'t be visible anymore when using this debug
draw mode.

:::: {#class_Viewport_constant_DEBUG_DRAW_WIREFRAME}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_WIREFRAME** = `4`

Objects are displayed as wireframe models.

\*\*Note:\*\*
`RenderingServer.set_debug_generate_wireframes()<class_RenderingServer_method_set_debug_generate_wireframes>`{.interpreted-text
role="ref"} must be called before loading any meshes for wireframes to
be visible when using the Compatibility renderer.

:::: {#class_Viewport_constant_DEBUG_DRAW_NORMAL_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_NORMAL_BUFFER** = `5`

Objects are displayed without lighting information and their textures
replaced by normal mapping.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_VOXEL_GI_ALBEDO}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_VOXEL_GI_ALBEDO** = `6`

Objects are displayed with only the albedo value from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}s. Requires at
least one visible `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}
node that has been baked to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_VOXEL_GI_LIGHTING}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_VOXEL_GI_LIGHTING** = `7`

Objects are displayed with only the lighting value from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}s. Requires at
least one visible `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}
node that has been baked to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_VOXEL_GI_EMISSION}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_VOXEL_GI_EMISSION** = `8`

Objects are displayed with only the emission color from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}s. Requires at
least one visible `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"}
node that has been baked to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_SHADOW_ATLAS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_SHADOW_ATLAS** = `9`

Draws the shadow atlas that stores shadows from
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"}s and
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"}s in the
upper left quadrant of the **Viewport**.

:::: {#class_Viewport_constant_DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_DIRECTIONAL_SHADOW_ATLAS** = `10`

Draws the shadow atlas that stores shadows from
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s in the upper left quadrant of the **Viewport**.

:::: {#class_Viewport_constant_DEBUG_DRAW_SCENE_LUMINANCE}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_SCENE_LUMINANCE** = `11`

Draws the scene luminance buffer (if available) in the upper left
quadrant of the **Viewport**.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_Viewport_constant_DEBUG_DRAW_SSAO}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_SSAO** = `12`

Draws the screen-space ambient occlusion texture instead of the scene so
that you can clearly see how it is affecting objects. In order for this
display mode to work, you must have
`Environment.ssao_enabled<class_Environment_property_ssao_enabled>`{.interpreted-text
role="ref"} set in your
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_SSIL}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_SSIL** = `13`

Draws the screen-space indirect lighting texture instead of the scene so
that you can clearly see how it is affecting objects. In order for this
display mode to work, you must have
`Environment.ssil_enabled<class_Environment_property_ssil_enabled>`{.interpreted-text
role="ref"} set in your
`WorldEnvironment<class_WorldEnvironment>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_PSSM_SPLITS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_PSSM_SPLITS** = `14`

Colors each PSSM split for the
`DirectionalLight3D<class_DirectionalLight3D>`{.interpreted-text
role="ref"}s in the scene a different color so you can see where the
splits are. In order (from closest to furthest from the camera), they
are colored red, green, blue, and yellow.

\*\*Note:\*\* When using this debug draw mode, custom shaders are
ignored since all materials in the scene temporarily use a debug
material. This means the result from custom shader functions (such as
vertex displacement) won\'t be visible anymore when using this debug
draw mode.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_Viewport_constant_DEBUG_DRAW_DECAL_ATLAS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_DECAL_ATLAS** = `15`

Draws the decal atlas used by `Decal<class_Decal>`{.interpreted-text
role="ref"}s and light projector textures in the upper left quadrant of
the **Viewport**.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_Viewport_constant_DEBUG_DRAW_SDFGI}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_SDFGI** = `16`

Draws the cascades used to render signed distance field global
illumination (SDFGI).

Does nothing if the current environment\'s
`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"} is `false`.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_SDFGI_PROBES}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_SDFGI_PROBES** = `17`

Draws the probes used for signed distance field global illumination
(SDFGI).

Does nothing if the current environment\'s
`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"} is `false`.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_GI_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_GI_BUFFER** = `18`

Draws the buffer used for global illumination from
`VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} or SDFGI.
Requires `VoxelGI<class_VoxelGI>`{.interpreted-text role="ref"} (at
least one visible baked VoxelGI node) or SDFGI
(`Environment.sdfgi_enabled<class_Environment_property_sdfgi_enabled>`{.interpreted-text
role="ref"}) to be enabled to have a visible effect.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_DISABLE_LOD}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_DISABLE_LOD** = `19`

Draws all of the objects at their highest polycount regardless of their
distance from the camera. No low level of detail (LOD) is applied.

:::: {#class_Viewport_constant_DEBUG_DRAW_CLUSTER_OMNI_LIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_CLUSTER_OMNI_LIGHTS** = `20`

Draws the cluster used by
`OmniLight3D<class_OmniLight3D>`{.interpreted-text role="ref"} nodes to
optimize light rendering.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_CLUSTER_SPOT_LIGHTS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_CLUSTER_SPOT_LIGHTS** = `21`

Draws the cluster used by
`SpotLight3D<class_SpotLight3D>`{.interpreted-text role="ref"} nodes to
optimize light rendering.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_CLUSTER_DECALS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_CLUSTER_DECALS** = `22`

Draws the cluster used by `Decal<class_Decal>`{.interpreted-text
role="ref"} nodes to optimize decal rendering.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_CLUSTER_REFLECTION_PROBES}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_CLUSTER_REFLECTION_PROBES** = `23`

Draws the cluster used by
`ReflectionProbe<class_ReflectionProbe>`{.interpreted-text role="ref"}
nodes to optimize reflection probes.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_OCCLUDERS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_OCCLUDERS** = `24`

Draws the buffer used for occlusion culling.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

:::: {#class_Viewport_constant_DEBUG_DRAW_MOTION_VECTORS}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_MOTION_VECTORS** = `25`

Draws vector lines over the viewport to indicate the movement of pixels
between frames.

\*\*Note:\*\* Only supported when using the Forward+ rendering method.

:::: {#class_Viewport_constant_DEBUG_DRAW_INTERNAL_BUFFER}
::: rst-class
classref-enumeration-constant
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**DEBUG_DRAW_INTERNAL_BUFFER** = `26`

Draws the internal resolution buffer of the scene in linear colorspace
before tonemapping or post-processing is applied.

\*\*Note:\*\* Only supported when using the Forward+ or Mobile rendering
methods.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_DefaultCanvasItemTextureFilter}
::: rst-class
classref-enumeration
:::
::::

enum **DefaultCanvasItemTextureFilter**:
`🔗<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST** = `0`

The texture filter reads from the nearest pixel only. This makes the
texture look pixelated from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR** = `1`

The texture filter blends between the nearest 4 pixels. This makes the
texture look smooth from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS** =
`2`

The texture filter blends between the nearest 4 pixels and between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look smooth from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS**
= `3`

The texture filter reads from the nearest pixel and blends between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look pixelated from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_FILTER_MAX** = `4`

Represents the size of the
`DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_DefaultCanvasItemTextureRepeat}
::: rst-class
classref-enumeration
:::
::::

enum **DefaultCanvasItemTextureRepeat**:
`🔗<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_DISABLED** = `0`

Disables textures repeating. Instead, when reading UVs outside the 0-1
range, the value will be clamped to the edge of the texture, resulting
in a stretched out look at the borders of the texture.

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_ENABLED** = `1`

Enables the texture to repeat when UV coordinates are outside the 0-1
range. If using one of the linear filtering modes, this can result in
artifacts at the edges of a texture when the sampler filters across the
edges of the texture.

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MIRROR}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MIRROR** = `2`

Flip the texture when repeating so that the edge lines up instead of
abruptly changing.

:::: {#class_Viewport_constant_DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **DEFAULT_CANVAS_ITEM_TEXTURE_REPEAT_MAX** = `3`

Represents the size of the
`DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_SDFOversize}
::: rst-class
classref-enumeration
:::
::::

enum **SDFOversize**: `🔗<enum_Viewport_SDFOversize>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_SDF_OVERSIZE_100_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
**SDF_OVERSIZE_100_PERCENT** = `0`

The signed distance field only covers the viewport\'s own rectangle.

:::: {#class_Viewport_constant_SDF_OVERSIZE_120_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
**SDF_OVERSIZE_120_PERCENT** = `1`

The signed distance field is expanded to cover 20% of the viewport\'s
size around the borders.

:::: {#class_Viewport_constant_SDF_OVERSIZE_150_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
**SDF_OVERSIZE_150_PERCENT** = `2`

The signed distance field is expanded to cover 50% of the viewport\'s
size around the borders.

:::: {#class_Viewport_constant_SDF_OVERSIZE_200_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
**SDF_OVERSIZE_200_PERCENT** = `3`

The signed distance field is expanded to cover 100% (double) of the
viewport\'s size around the borders.

:::: {#class_Viewport_constant_SDF_OVERSIZE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
**SDF_OVERSIZE_MAX** = `4`

Represents the size of the
`SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_SDFScale}
::: rst-class
classref-enumeration
:::
::::

enum **SDFScale**: `🔗<enum_Viewport_SDFScale>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_SDF_SCALE_100_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"}
**SDF_SCALE_100_PERCENT** = `0`

The signed distance field is rendered at full resolution.

:::: {#class_Viewport_constant_SDF_SCALE_50_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"}
**SDF_SCALE_50_PERCENT** = `1`

The signed distance field is rendered at half the resolution of this
viewport.

:::: {#class_Viewport_constant_SDF_SCALE_25_PERCENT}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"}
**SDF_SCALE_25_PERCENT** = `2`

The signed distance field is rendered at a quarter the resolution of
this viewport.

:::: {#class_Viewport_constant_SDF_SCALE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"}
**SDF_SCALE_MAX** = `3`

Represents the size of the
`SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_VRSMode}
::: rst-class
classref-enumeration
:::
::::

enum **VRSMode**: `🔗<enum_Viewport_VRSMode>`{.interpreted-text
role="ref"}

:::: {#class_Viewport_constant_VRS_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"}
**VRS_DISABLED** = `0`

Variable Rate Shading is disabled.

:::: {#class_Viewport_constant_VRS_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"}
**VRS_TEXTURE** = `1`

Variable Rate Shading uses a texture. Note, for stereoscopic use a
texture atlas with a texture for each view.

:::: {#class_Viewport_constant_VRS_XR}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"}
**VRS_XR** = `2`

Variable Rate Shading\'s texture is supplied by the primary
`XRInterface<class_XRInterface>`{.interpreted-text role="ref"}.

:::: {#class_Viewport_constant_VRS_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"}
**VRS_MAX** = `3`

Represents the size of the
`VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_Viewport_VRSUpdateMode}
::: rst-class
classref-enumeration
:::
::::

enum **VRSUpdateMode**:
`🔗<enum_Viewport_VRSUpdateMode>`{.interpreted-text role="ref"}

:::: {#class_Viewport_constant_VRS_UPDATE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
role="ref"} **VRS_UPDATE_DISABLED** = `0`

The input texture for variable rate shading will not be processed.

:::: {#class_Viewport_constant_VRS_UPDATE_ONCE}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
role="ref"} **VRS_UPDATE_ONCE** = `1`

The input texture for variable rate shading will be processed once.

:::: {#class_Viewport_constant_VRS_UPDATE_ALWAYS}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
role="ref"} **VRS_UPDATE_ALWAYS** = `2`

The input texture for variable rate shading will be processed each
frame.

:::: {#class_Viewport_constant_VRS_UPDATE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
role="ref"} **VRS_UPDATE_MAX** = `3`

Represents the size of the
`VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_Viewport_property_anisotropic_filtering_level}
::: rst-class
classref-property
:::
::::

`AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
role="ref"} **anisotropic_filtering_level** = `2`
`🔗<class_Viewport_property_anisotropic_filtering_level>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_anisotropic_filtering_level**(value:
  `AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
  role="ref"})
- `AnisotropicFiltering<enum_Viewport_AnisotropicFiltering>`{.interpreted-text
  role="ref"} **get_anisotropic_filtering_level**()

Sets the maximum number of samples to take when using anisotropic
filtering on textures (as a power of two). A higher sample count will
result in sharper textures at oblique angles, but is more expensive to
compute. A value of `0` forcibly disables anisotropic filtering, even on
materials where it is enabled.

The anisotropic filtering level also affects decals and light projectors
if they are configured to use anisotropic filtering. See
`ProjectSettings.rendering/textures/decals/filter<class_ProjectSettings_property_rendering/textures/decals/filter>`{.interpreted-text
role="ref"} and
`ProjectSettings.rendering/textures/light_projectors/filter<class_ProjectSettings_property_rendering/textures/light_projectors/filter>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In 3D, for this setting to have an effect, set
`BaseMaterial3D.texture_filter<class_BaseMaterial3D_property_texture_filter>`{.interpreted-text
role="ref"} to
`BaseMaterial3D.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC<class_BaseMaterial3D_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} or
`BaseMaterial3D.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC<class_BaseMaterial3D_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} on materials.

\*\*Note:\*\* In 2D, for this setting to have an effect, set
`CanvasItem.texture_filter<class_CanvasItem_property_texture_filter>`{.interpreted-text
role="ref"} to
`CanvasItem.TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC<class_CanvasItem_constant_TEXTURE_FILTER_LINEAR_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} or
`CanvasItem.TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC<class_CanvasItem_constant_TEXTURE_FILTER_NEAREST_WITH_MIPMAPS_ANISOTROPIC>`{.interpreted-text
role="ref"} on the `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} node displaying the texture (or in
`CanvasTexture<class_CanvasTexture>`{.interpreted-text role="ref"}).
However, anisotropic filtering is rarely useful in 2D, so only enable it
for textures in 2D if it makes a meaningful visual difference.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_audio_listener_enable_2d}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**audio_listener_enable_2d** = `false`
`🔗<class_Viewport_property_audio_listener_enable_2d>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_audio_listener_2d**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_audio_listener_2d**()

If `true`, the viewport will process 2D audio streams.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_audio_listener_enable_3d}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**audio_listener_enable_3d** = `false`
`🔗<class_Viewport_property_audio_listener_enable_3d>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_as_audio_listener_3d**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_audio_listener_3d**()

If `true`, the viewport will process 3D audio streams.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_canvas_cull_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **canvas_cull_mask** =
`4294967295`
`🔗<class_Viewport_property_canvas_cull_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_canvas_cull_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_canvas_cull_mask**()

The rendering layers in which this **Viewport** renders
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} nodes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_canvas_item_default_texture_filter}
::: rst-class
classref-property
:::
::::

`DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
role="ref"} **canvas_item_default_texture_filter** = `1`
`🔗<class_Viewport_property_canvas_item_default_texture_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_canvas_item_texture_filter**(value:
  `DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
  role="ref"})
- `DefaultCanvasItemTextureFilter<enum_Viewport_DefaultCanvasItemTextureFilter>`{.interpreted-text
  role="ref"} **get_default_canvas_item_texture_filter**()

Sets the default filter mode used by
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}s in this
Viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_canvas_item_default_texture_repeat}
::: rst-class
classref-property
:::
::::

`DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
role="ref"} **canvas_item_default_texture_repeat** = `0`
`🔗<class_Viewport_property_canvas_item_default_texture_repeat>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_canvas_item_texture_repeat**(value:
  `DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
  role="ref"})
- `DefaultCanvasItemTextureRepeat<enum_Viewport_DefaultCanvasItemTextureRepeat>`{.interpreted-text
  role="ref"} **get_default_canvas_item_texture_repeat**()

Sets the default repeat mode used by
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}s in this
Viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_canvas_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**canvas_transform**
`🔗<class_Viewport_property_canvas_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_canvas_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_canvas_transform**()

The canvas transform of the viewport, useful for changing the on-screen
positions of all child `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"}s. This is relative to the global canvas transform of the
viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_debug_draw}
::: rst-class
classref-property
:::
::::

`DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
**debug_draw** = `0`
`🔗<class_Viewport_property_debug_draw>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_debug_draw**(value:
  `DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"})
- `DebugDraw<enum_Viewport_DebugDraw>`{.interpreted-text role="ref"}
  **get_debug_draw**()

The overlay mode for test rendered geometry in debug purposes.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_disable_3d}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **disable_3d** =
`false` `🔗<class_Viewport_property_disable_3d>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disable_3d**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_3d_disabled**()

Disable 3D rendering (but keep 2D rendering).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_fsr_sharpness}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **fsr_sharpness** =
`0.2` `🔗<class_Viewport_property_fsr_sharpness>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_fsr_sharpness**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_fsr_sharpness**()

Determines how sharp the upscaled image will be when using the FSR
upscaling mode. Sharpness halves with every whole number. Values go from
0.0 (sharpest) to 2.0. Values above 2.0 won\'t make a visible
difference.

To control this property on the root viewport, set the
`ProjectSettings.rendering/scaling_3d/fsr_sharpness<class_ProjectSettings_property_rendering/scaling_3d/fsr_sharpness>`{.interpreted-text
role="ref"} project setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_global_canvas_transform}
::: rst-class
classref-property
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**global_canvas_transform**
`🔗<class_Viewport_property_global_canvas_transform>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_global_canvas_transform**(value:
  `Transform2D<class_Transform2D>`{.interpreted-text role="ref"})
- `Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
  **get_global_canvas_transform**()

The global canvas transform of the viewport. The canvas transform is
relative to this.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_gui_disable_input}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **gui_disable_input** =
`false`
`🔗<class_Viewport_property_gui_disable_input>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_disable_input**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_input_disabled**()

If `true`, the viewport will not receive input events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_gui_embed_subwindows}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gui_embed_subwindows** = `false`
`🔗<class_Viewport_property_gui_embed_subwindows>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_embedding_subwindows**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_embedding_subwindows**()

If `true`, sub-windows (popups and dialogs) will be embedded inside
application window as control-like nodes. If `false`, they will appear
as separate windows handled by the operating system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_gui_snap_controls_to_pixels}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gui_snap_controls_to_pixels** = `true`
`🔗<class_Viewport_property_gui_snap_controls_to_pixels>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snap_controls_to_pixels**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_snap_controls_to_pixels_enabled**()

If `true`, the GUI controls on the viewport will lay pixel perfectly.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_handle_input_locally}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**handle_input_locally** = `true`
`🔗<class_Viewport_property_handle_input_locally>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_handle_input_locally**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_handling_input_locally**()

If `true`, this viewport will mark incoming input events as handled by
itself. If `false`, this is instead done by the first parent viewport
that is set to handle input locally.

A `SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"} will automatically set this property to `false` for the
**Viewport** contained inside of it.

See also
`set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"} and
`is_input_handled()<class_Viewport_method_is_input_handled>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_mesh_lod_threshold}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**mesh_lod_threshold** = `1.0`
`🔗<class_Viewport_property_mesh_lod_threshold>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_mesh_lod_threshold**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_mesh_lod_threshold**()

The automatic LOD bias to use for meshes rendered within the
**Viewport** (this is analogous to
`ReflectionProbe.mesh_lod_threshold<class_ReflectionProbe_property_mesh_lod_threshold>`{.interpreted-text
role="ref"}). Higher values will use less detailed versions of meshes
that have LOD variations generated. If set to `0.0`, automatic LOD is
disabled. Increase
`mesh_lod_threshold<class_Viewport_property_mesh_lod_threshold>`{.interpreted-text
role="ref"} to improve performance at the cost of geometry detail.

To control this property on the root viewport, set the
`ProjectSettings.rendering/mesh_lod/lod_change/threshold_pixels<class_ProjectSettings_property_rendering/mesh_lod/lod_change/threshold_pixels>`{.interpreted-text
role="ref"} project setting.

\*\*Note:\*\*
`mesh_lod_threshold<class_Viewport_property_mesh_lod_threshold>`{.interpreted-text
role="ref"} does not affect
`GeometryInstance3D<class_GeometryInstance3D>`{.interpreted-text
role="ref"} visibility ranges (also known as \"manual\" LOD or
hierarchical LOD).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_msaa_2d}
::: rst-class
classref-property
:::
::::

`MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"} **msaa_2d** =
`0` `🔗<class_Viewport_property_msaa_2d>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_msaa_2d**(value: `MSAA<enum_Viewport_MSAA>`{.interpreted-text
  role="ref"})
- `MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"}
  **get_msaa_2d**()

The multisample antialiasing mode for 2D/Canvas rendering. A higher
number results in smoother edges at the cost of significantly worse
performance. A value of
`MSAA_2X<class_Viewport_constant_MSAA_2X>`{.interpreted-text role="ref"}
or `MSAA_4X<class_Viewport_constant_MSAA_4X>`{.interpreted-text
role="ref"} is best unless targeting very high-end systems. This has no
effect on shader-induced aliasing or texture aliasing.

See also
`ProjectSettings.rendering/anti_aliasing/quality/msaa_2d<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_2d>`{.interpreted-text
role="ref"} and
`RenderingServer.viewport_set_msaa_2d()<class_RenderingServer_method_viewport_set_msaa_2d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_msaa_3d}
::: rst-class
classref-property
:::
::::

`MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"} **msaa_3d** =
`0` `🔗<class_Viewport_property_msaa_3d>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_msaa_3d**(value: `MSAA<enum_Viewport_MSAA>`{.interpreted-text
  role="ref"})
- `MSAA<enum_Viewport_MSAA>`{.interpreted-text role="ref"}
  **get_msaa_3d**()

The multisample antialiasing mode for 3D rendering. A higher number
results in smoother edges at the cost of significantly worse
performance. A value of
`MSAA_2X<class_Viewport_constant_MSAA_2X>`{.interpreted-text role="ref"}
or `MSAA_4X<class_Viewport_constant_MSAA_4X>`{.interpreted-text
role="ref"} is best unless targeting very high-end systems. See also
bilinear scaling 3D
`scaling_3d_mode<class_Viewport_property_scaling_3d_mode>`{.interpreted-text
role="ref"} for supersampling, which provides higher quality but is much
more expensive. This has no effect on shader-induced aliasing or texture
aliasing.

See also
`ProjectSettings.rendering/anti_aliasing/quality/msaa_3d<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_3d>`{.interpreted-text
role="ref"} and
`RenderingServer.viewport_set_msaa_3d()<class_RenderingServer_method_viewport_set_msaa_3d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_oversampling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **oversampling** =
`true` `🔗<class_Viewport_property_oversampling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_oversampling**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_oversampling**()

If `true` and one of the following conditions is true:
`SubViewport.size_2d_override_stretch<class_SubViewport_property_size_2d_override_stretch>`{.interpreted-text
role="ref"} and
`SubViewport.size_2d_override<class_SubViewport_property_size_2d_override>`{.interpreted-text
role="ref"} are set,
`Window.content_scale_factor<class_Window_property_content_scale_factor>`{.interpreted-text
role="ref"} is set and scaling is enabled,
`oversampling_override<class_Viewport_property_oversampling_override>`{.interpreted-text
role="ref"} is set, font and
`SVGTexture<class_SVGTexture>`{.interpreted-text role="ref"}
oversampling is enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_oversampling_override}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**oversampling_override** = `0.0`
`🔗<class_Viewport_property_oversampling_override>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_oversampling_override**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_oversampling_override**()

If greater than zero, this value is used as the font oversampling
factor, otherwise oversampling is equal to viewport scale.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_own_world_3d}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **own_world_3d** =
`false` `🔗<class_Viewport_property_own_world_3d>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_own_world_3d**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_own_world_3d**()

If `true`, the viewport will use a unique copy of the
`World3D<class_World3D>`{.interpreted-text role="ref"} defined in
`world_3d<class_Viewport_property_world_3d>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_physics_object_picking}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics_object_picking** = `false`
`🔗<class_Viewport_property_physics_object_picking>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_object_picking**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_physics_object_picking**()

If `true`, the objects rendered by viewport become subjects of mouse
picking process.

\*\*Note:\*\* The number of simultaneously pickable objects is limited
to 64 and they are selected in a non-deterministic order, which can be
different in each picking process.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_physics_object_picking_first_only}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics_object_picking_first_only** = `false`
`🔗<class_Viewport_property_physics_object_picking_first_only>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_object_picking_first_only**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_physics_object_picking_first_only**()

If `true`, the input_event signal will only be sent to one physics
object in the mouse picking process. If you want to get the top object
only, you must also enable
`physics_object_picking_sort<class_Viewport_property_physics_object_picking_sort>`{.interpreted-text
role="ref"}.

If `false`, an input_event signal will be sent to all physics objects in
the mouse picking process.

This applies to 2D CanvasItem object picking only.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_physics_object_picking_sort}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**physics_object_picking_sort** = `false`
`🔗<class_Viewport_property_physics_object_picking_sort>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_physics_object_picking_sort**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_physics_object_picking_sort**()

If `true`, objects receive mouse picking events sorted primarily by
their
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} and secondarily by their position in the scene tree. If
`false`, the order is undetermined.

\*\*Note:\*\* This setting is disabled by default because of its
potential expensive computational cost.

\*\*Note:\*\* Sorting happens after selecting the pickable objects.
Because of the limitation of 64 simultaneously pickable objects, it is
not guaranteed that the object with the highest
`CanvasItem.z_index<class_CanvasItem_property_z_index>`{.interpreted-text
role="ref"} receives the picking event.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_positional_shadow_atlas_16_bits}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**positional_shadow_atlas_16_bits** = `true`
`🔗<class_Viewport_property_positional_shadow_atlas_16_bits>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_positional_shadow_atlas_16_bits**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_positional_shadow_atlas_16_bits**()

Use 16 bits for the omni/spot shadow depth map. Enabling this results in
shadows having less precision and may result in shadow acne, but can
lead to performance improvements on some devices.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_positional_shadow_atlas_quad_0}
::: rst-class
classref-property
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **positional_shadow_atlas_quad_0** = `2`
`🔗<class_Viewport_property_positional_shadow_atlas_quad_0>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"}, subdiv:
  `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"})
- `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"} **get_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The subdivision amount of the first quadrant on the shadow atlas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_positional_shadow_atlas_quad_1}
::: rst-class
classref-property
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **positional_shadow_atlas_quad_1** = `2`
`🔗<class_Viewport_property_positional_shadow_atlas_quad_1>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"}, subdiv:
  `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"})
- `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"} **get_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The subdivision amount of the second quadrant on the shadow atlas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_positional_shadow_atlas_quad_2}
::: rst-class
classref-property
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **positional_shadow_atlas_quad_2** = `3`
`🔗<class_Viewport_property_positional_shadow_atlas_quad_2>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"}, subdiv:
  `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"})
- `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"} **get_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The subdivision amount of the third quadrant on the shadow atlas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_positional_shadow_atlas_quad_3}
::: rst-class
classref-property
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **positional_shadow_atlas_quad_3** = `4`
`🔗<class_Viewport_property_positional_shadow_atlas_quad_3>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"}, subdiv:
  `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"})
- `PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
  role="ref"} **get_positional_shadow_atlas_quadrant_subdiv**(quadrant:
  `int<class_int>`{.interpreted-text role="ref"})
  `const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
  role="abbr"}

The subdivision amount of the fourth quadrant on the shadow atlas.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_positional_shadow_atlas_size}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"}
**positional_shadow_atlas_size** = `2048`
`🔗<class_Viewport_property_positional_shadow_atlas_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_positional_shadow_atlas_size**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_positional_shadow_atlas_size**()

The shadow atlas\' resolution (used for omni and spot lights). The value
is rounded up to the nearest power of 2.

\*\*Note:\*\* If this is set to `0`, no positional shadows will be
visible at all. This can improve performance significantly on low-end
systems by reducing both the CPU and GPU load (as fewer draw calls are
needed to draw the scene without shadows).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_scaling_3d_mode}
::: rst-class
classref-property
:::
::::

`Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
role="ref"} **scaling_3d_mode** = `0`
`🔗<class_Viewport_property_scaling_3d_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scaling_3d_mode**(value:
  `Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
  role="ref"})
- `Scaling3DMode<enum_Viewport_Scaling3DMode>`{.interpreted-text
  role="ref"} **get_scaling_3d_mode**()

Sets scaling 3D mode. Bilinear scaling renders at different resolution
to either undersample or supersample the viewport. FidelityFX Super
Resolution 1.0, abbreviated to FSR, is an upscaling technology that
produces high quality images at fast framerates by using a spatially
aware upscaling algorithm. FSR is slightly more expensive than bilinear,
but it produces significantly higher image quality. FSR should be used
where possible.

To control this property on the root viewport, set the
`ProjectSettings.rendering/scaling_3d/mode<class_ProjectSettings_property_rendering/scaling_3d/mode>`{.interpreted-text
role="ref"} project setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_scaling_3d_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **scaling_3d_scale**
= `1.0` `🔗<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_scaling_3d_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_scaling_3d_scale**()

Scales the 3D render buffer based on the viewport size uses an image
filter specified in
`ProjectSettings.rendering/scaling_3d/mode<class_ProjectSettings_property_rendering/scaling_3d/mode>`{.interpreted-text
role="ref"} to scale the output image to the full viewport size. Values
lower than `1.0` can be used to speed up 3D rendering at the cost of
quality (undersampling). Values greater than `1.0` are only valid for
bilinear mode and can be used to improve 3D rendering quality at a high
performance cost (supersampling). See also
`ProjectSettings.rendering/anti_aliasing/quality/msaa_3d<class_ProjectSettings_property_rendering/anti_aliasing/quality/msaa_3d>`{.interpreted-text
role="ref"} for multi-sample antialiasing, which is significantly
cheaper but only smooths the edges of polygons.

When using FSR upscaling, AMD recommends exposing the following values
as preset options to users \"Ultra Quality: 0.77\", \"Quality: 0.67\",
\"Balanced: 0.59\", \"Performance: 0.5\" instead of exposing the entire
scale.

To control this property on the root viewport, set the
`ProjectSettings.rendering/scaling_3d/scale<class_ProjectSettings_property_rendering/scaling_3d/scale>`{.interpreted-text
role="ref"} project setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_screen_space_aa}
::: rst-class
classref-property
:::
::::

`ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
role="ref"} **screen_space_aa** = `0`
`🔗<class_Viewport_property_screen_space_aa>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_screen_space_aa**(value:
  `ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
  role="ref"})
- `ScreenSpaceAA<enum_Viewport_ScreenSpaceAA>`{.interpreted-text
  role="ref"} **get_screen_space_aa**()

Sets the screen-space antialiasing method used. Screen-space
antialiasing works by selectively blurring edges in a post-process
shader. It differs from MSAA which takes multiple coverage samples while
rendering objects. Screen-space AA methods are typically faster than
MSAA and will smooth out specular aliasing, but tend to make scenes
appear blurry.

See also
`ProjectSettings.rendering/anti_aliasing/quality/screen_space_aa<class_ProjectSettings_property_rendering/anti_aliasing/quality/screen_space_aa>`{.interpreted-text
role="ref"} and
`RenderingServer.viewport_set_screen_space_aa()<class_RenderingServer_method_viewport_set_screen_space_aa>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_sdf_oversize}
::: rst-class
classref-property
:::
::::

`SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
**sdf_oversize** = `1`
`🔗<class_Viewport_property_sdf_oversize>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdf_oversize**(value:
  `SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text
  role="ref"})
- `SDFOversize<enum_Viewport_SDFOversize>`{.interpreted-text role="ref"}
  **get_sdf_oversize**()

Controls how much of the original viewport\'s size should be covered by
the 2D signed distance field. This SDF can be sampled in
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} shaders and
is also used for
`GPUParticles2D<class_GPUParticles2D>`{.interpreted-text role="ref"}
collision. Higher values allow portions of occluders located outside the
viewport to still be taken into account in the generated signed distance
field, at the cost of performance. If you notice particles falling
through `LightOccluder2D<class_LightOccluder2D>`{.interpreted-text
role="ref"}s as the occluders leave the viewport, increase this setting.

The percentage is added on each axis and on both sides. For example,
with the default
`SDF_OVERSIZE_120_PERCENT<class_Viewport_constant_SDF_OVERSIZE_120_PERCENT>`{.interpreted-text
role="ref"}, the signed distance field will cover 20% of the viewport\'s
size outside the viewport on each side (top, right, bottom, left).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_sdf_scale}
::: rst-class
classref-property
:::
::::

`SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"}
**sdf_scale** = `1`
`🔗<class_Viewport_property_sdf_scale>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_sdf_scale**(value:
  `SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"})
- `SDFScale<enum_Viewport_SDFScale>`{.interpreted-text role="ref"}
  **get_sdf_scale**()

The resolution scale to use for the 2D signed distance field. Higher
values lead to a more precise and more stable signed distance field as
the camera moves, at the cost of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_snap_2d_transforms_to_pixel}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**snap_2d_transforms_to_pixel** = `false`
`🔗<class_Viewport_property_snap_2d_transforms_to_pixel>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snap_2d_transforms_to_pixel**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_snap_2d_transforms_to_pixel_enabled**()

If `true`, `CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"}
nodes will internally snap to full pixels. Their position can still be
sub-pixel, but the decimals will not have effect. This can lead to a
crisper appearance at the cost of less smooth movement, especially when
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} smoothing is
enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_snap_2d_vertices_to_pixel}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**snap_2d_vertices_to_pixel** = `false`
`🔗<class_Viewport_property_snap_2d_vertices_to_pixel>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_snap_2d_vertices_to_pixel**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_snap_2d_vertices_to_pixel_enabled**()

If `true`, vertices of `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"} nodes will snap to full pixels. Only affects the final
vertex positions, not the transforms. This can lead to a crisper
appearance at the cost of less smooth movement, especially when
`Camera2D<class_Camera2D>`{.interpreted-text role="ref"} smoothing is
enabled.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_texture_mipmap_bias}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**texture_mipmap_bias** = `0.0`
`🔗<class_Viewport_property_texture_mipmap_bias>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_mipmap_bias**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_mipmap_bias**()

Affects the final texture sharpness by reading from a lower or higher
mipmap (also called \"texture LOD bias\"). Negative values make
mipmapped textures sharper but grainier when viewed at a distance, while
positive values make mipmapped textures blurrier (even when up close).

Enabling temporal antialiasing
(`use_taa<class_Viewport_property_use_taa>`{.interpreted-text
role="ref"}) will automatically apply a `-0.5` offset to this value,
while enabling FXAA
(`screen_space_aa<class_Viewport_property_screen_space_aa>`{.interpreted-text
role="ref"}) will automatically apply a `-0.25` offset to this value. If
both TAA and FXAA are enabled at the same time, an offset of `-0.75` is
applied to this value.

\*\*Note:\*\* If
`scaling_3d_scale<class_Viewport_property_scaling_3d_scale>`{.interpreted-text
role="ref"} is lower than `1.0` (exclusive),
`texture_mipmap_bias<class_Viewport_property_texture_mipmap_bias>`{.interpreted-text
role="ref"} is used to adjust the automatic mipmap bias which is
calculated internally based on the scale factor. The formula for this is
`log2(scaling_3d_scale) + mipmap_bias`.

To control this property on the root viewport, set the
`ProjectSettings.rendering/textures/default_filters/texture_mipmap_bias<class_ProjectSettings_property_rendering/textures/default_filters/texture_mipmap_bias>`{.interpreted-text
role="ref"} project setting.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_transparent_bg}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **transparent_bg** =
`false` `🔗<class_Viewport_property_transparent_bg>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_transparent_background**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **has_transparent_background**()

If `true`, the viewport should render its background as transparent.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_use_debanding}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_debanding** =
`false` `🔗<class_Viewport_property_use_debanding>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_debanding**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_debanding**()

If `true`, uses a fast post-processing filter to make banding
significantly less visible. If
`use_hdr_2d<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"} is `false`, 2D rendering is *not* affected by debanding
unless the
`Environment.background_mode<class_Environment_property_background_mode>`{.interpreted-text
role="ref"} is
`Environment.BG_CANVAS<class_Environment_constant_BG_CANVAS>`{.interpreted-text
role="ref"}. If
`use_hdr_2d<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"} is `true`, debanding will only be applied if this is the
root **Viewport** and will affect all 2D and 3D rendering, including
canvas items.

In some cases, debanding may introduce a slightly noticeable dithering
pattern. It\'s recommended to enable debanding only when actually needed
since the dithering pattern will make lossless-compressed screenshots
larger.

See also
`ProjectSettings.rendering/anti_aliasing/quality/use_debanding<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_debanding>`{.interpreted-text
role="ref"} and
`RenderingServer.viewport_set_use_debanding()<class_RenderingServer_method_viewport_set_use_debanding>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_use_hdr_2d}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_hdr_2d** =
`false` `🔗<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_hdr_2d**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_hdr_2d**()

If `true`, 2D rendering will use a high dynamic range (HDR) format
framebuffer matching the bit depth of the 3D framebuffer. When using the
Forward+ renderer this will be an `RGBA16` framebuffer, while when using
the Mobile renderer it will be an `RGB10_A2` framebuffer. Additionally,
2D rendering will take place in linear color space and will be converted
to sRGB space immediately before blitting to the screen (if the Viewport
is attached to the screen). Practically speaking, this means that the
end result of the Viewport will not be clamped into the `0-1` range and
can be used in 3D rendering without color space adjustments. This allows
2D rendering to take advantage of effects requiring high dynamic range
(e.g. 2D glow) as well as substantially improves the appearance of
effects requiring highly detailed gradients.

\*\*Note:\*\* This setting will have no effect when using the
Compatibility renderer, which always renders in low dynamic range for
performance reasons.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_use_occlusion_culling}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**use_occlusion_culling** = `false`
`🔗<class_Viewport_property_use_occlusion_culling>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_occlusion_culling**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_using_occlusion_culling**()

If `true`,
`OccluderInstance3D<class_OccluderInstance3D>`{.interpreted-text
role="ref"} nodes will be usable for occlusion culling in 3D for this
viewport. For the root viewport,
`ProjectSettings.rendering/occlusion_culling/use_occlusion_culling<class_ProjectSettings_property_rendering/occlusion_culling/use_occlusion_culling>`{.interpreted-text
role="ref"} must be set to `true` instead.

\*\*Note:\*\* Enabling occlusion culling has a cost on the CPU. Only
enable occlusion culling if you actually plan to use it, and think
whether your scene can actually benefit from occlusion culling. Large,
open scenes with few or no objects blocking the view will generally not
benefit much from occlusion culling. Large open scenes generally benefit
more from mesh LOD and visibility ranges
(`GeometryInstance3D.visibility_range_begin<class_GeometryInstance3D_property_visibility_range_begin>`{.interpreted-text
role="ref"} and
`GeometryInstance3D.visibility_range_end<class_GeometryInstance3D_property_visibility_range_end>`{.interpreted-text
role="ref"}) compared to occlusion culling.

\*\*Note:\*\* Due to memory constraints, occlusion culling is not
supported by default in Web export templates. It can be enabled by
compiling custom Web export templates with `module_raycast_enabled=yes`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_use_taa}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_taa** = `false`
`🔗<class_Viewport_property_use_taa>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_taa**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_taa**()

Enables temporal antialiasing for this viewport. TAA works by jittering
the camera and accumulating the images of the last rendered frames,
motion vector rendering is used to account for camera and object motion.

\*\*Note:\*\* The implementation is not complete yet, some visual
instances such as particles and skinned meshes may show artifacts.

See also
`ProjectSettings.rendering/anti_aliasing/quality/use_taa<class_ProjectSettings_property_rendering/anti_aliasing/quality/use_taa>`{.interpreted-text
role="ref"} and
`RenderingServer.viewport_set_use_taa()<class_RenderingServer_method_viewport_set_use_taa>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_use_xr}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **use_xr** = `false`
`🔗<class_Viewport_property_use_xr>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_use_xr**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **is_using_xr**()

If `true`, the viewport will use the primary XR interface to render XR
output. When applicable this can result in a stereoscopic image and the
resulting render being output to a headset.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_vrs_mode}
::: rst-class
classref-property
:::
::::

`VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"}
**vrs_mode** = `0`
`🔗<class_Viewport_property_vrs_mode>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_mode**(value:
  `VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"})
- `VRSMode<enum_Viewport_VRSMode>`{.interpreted-text role="ref"}
  **get_vrs_mode**()

The Variable Rate Shading (VRS) mode that is used for this viewport.
Note, if hardware does not support VRS this property is ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_vrs_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**vrs_texture**
`🔗<class_Viewport_property_vrs_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_vrs_texture**()

Texture to use when
`vrs_mode<class_Viewport_property_vrs_mode>`{.interpreted-text
role="ref"} is set to
`VRS_TEXTURE<class_Viewport_constant_VRS_TEXTURE>`{.interpreted-text
role="ref"}.

The texture *must* use a lossless compression format so that colors can
be matched precisely. The following VRS densities are mapped to various
colors, with brighter colors representing a lower level of shading
precision:

``` text
- 1×1 = rgb(0, 0, 0)     - #000000
- 1×2 = rgb(0, 85, 0)    - #005500
- 2×1 = rgb(85, 0, 0)    - #550000
- 2×2 = rgb(85, 85, 0)   - #555500
- 2×4 = rgb(85, 170, 0)  - #55aa00
- 4×2 = rgb(170, 85, 0)  - #aa5500
- 4×4 = rgb(170, 170, 0) - #aaaa00
- 4×8 = rgb(170, 255, 0) - #aaff00 - Not supported on most hardware
- 8×4 = rgb(255, 170, 0) - #ffaa00 - Not supported on most hardware
- 8×8 = rgb(255, 255, 0) - #ffff00 - Not supported on most hardware
```

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_vrs_update_mode}
::: rst-class
classref-property
:::
::::

`VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
role="ref"} **vrs_update_mode** = `1`
`🔗<class_Viewport_property_vrs_update_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_vrs_update_mode**(value:
  `VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
  role="ref"})
- `VRSUpdateMode<enum_Viewport_VRSUpdateMode>`{.interpreted-text
  role="ref"} **get_vrs_update_mode**()

Sets the update mode for Variable Rate Shading (VRS) for the viewport.
VRS requires the input texture to be converted to the format usable by
the VRS method supported by the hardware. The update mode defines how
often this happens. If the GPU does not support VRS, or VRS is not
enabled, this property is ignored.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_world_2d}
::: rst-class
classref-property
:::
::::

`World2D<class_World2D>`{.interpreted-text role="ref"} **world_2d**
`🔗<class_Viewport_property_world_2d>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_world_2d**(value: `World2D<class_World2D>`{.interpreted-text
  role="ref"})
- `World2D<class_World2D>`{.interpreted-text role="ref"}
  **get_world_2d**()

The custom `World2D<class_World2D>`{.interpreted-text role="ref"} which
can be used as 2D environment source.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_property_world_3d}
::: rst-class
classref-property
:::
::::

`World3D<class_World3D>`{.interpreted-text role="ref"} **world_3d**
`🔗<class_Viewport_property_world_3d>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_world_3d**(value: `World3D<class_World3D>`{.interpreted-text
  role="ref"})
- `World3D<class_World3D>`{.interpreted-text role="ref"}
  **get_world_3d**()

The custom `World3D<class_World3D>`{.interpreted-text role="ref"} which
can be used as 3D environment source.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_Viewport_method_find_world_2d}
::: rst-class
classref-method
:::
::::

`World2D<class_World2D>`{.interpreted-text role="ref"}
**find_world_2d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Viewport_method_find_world_2d>`{.interpreted-text
role="ref"}

Returns the first valid `World2D<class_World2D>`{.interpreted-text
role="ref"} for this viewport, searching the
`world_2d<class_Viewport_property_world_2d>`{.interpreted-text
role="ref"} property of itself and any Viewport ancestor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_find_world_3d}
::: rst-class
classref-method
:::
::::

`World3D<class_World3D>`{.interpreted-text role="ref"}
**find_world_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Viewport_method_find_world_3d>`{.interpreted-text
role="ref"}

Returns the first valid `World3D<class_World3D>`{.interpreted-text
role="ref"} for this viewport, searching the
`world_3d<class_Viewport_property_world_3d>`{.interpreted-text
role="ref"} property of itself and any Viewport ancestor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_audio_listener_2d}
::: rst-class
classref-method
:::
::::

`AudioListener2D<class_AudioListener2D>`{.interpreted-text role="ref"}
**get_audio_listener_2d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_audio_listener_2d>`{.interpreted-text
role="ref"}

Returns the currently active 2D audio listener. Returns `null` if there
are no active 2D audio listeners, in which case the active 2D camera
will be treated as listener.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_audio_listener_3d}
::: rst-class
classref-method
:::
::::

`AudioListener3D<class_AudioListener3D>`{.interpreted-text role="ref"}
**get_audio_listener_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_audio_listener_3d>`{.interpreted-text
role="ref"}

Returns the currently active 3D audio listener. Returns `null` if there
are no active 3D audio listeners, in which case the active 3D camera
will be treated as listener.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_camera_2d}
::: rst-class
classref-method
:::
::::

`Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
**get_camera_2d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Viewport_method_get_camera_2d>`{.interpreted-text
role="ref"}

Returns the currently active 2D camera. Returns `null` if there are no
active cameras.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_camera_3d}
::: rst-class
classref-method
:::
::::

`Camera3D<class_Camera3D>`{.interpreted-text role="ref"}
**get_camera_3d**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Viewport_method_get_camera_3d>`{.interpreted-text
role="ref"}

Returns the currently active 3D camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_canvas_cull_mask_bit}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**get_canvas_cull_mask_bit**(layer: `int<class_int>`{.interpreted-text
role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_canvas_cull_mask_bit>`{.interpreted-text
role="ref"}

Returns an individual bit on the rendering layer mask.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_embedded_subwindows}
::: rst-class
classref-method
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`Window<class_Window>`{.interpreted-text role="ref"}\]
**get_embedded_subwindows**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_embedded_subwindows>`{.interpreted-text
role="ref"}

Returns a list of the visible embedded
`Window<class_Window>`{.interpreted-text role="ref"}s inside the
viewport.

\*\*Note:\*\* `Window<class_Window>`{.interpreted-text role="ref"}s
inside other viewports will not be listed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_final_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_final_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_final_transform>`{.interpreted-text
role="ref"}

Returns the transform from the viewport\'s coordinate system to the
embedder\'s coordinate system.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_mouse_position}
::: rst-class
classref-method
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"}
**get_mouse_position**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_mouse_position>`{.interpreted-text
role="ref"}

Returns the mouse\'s position in this **Viewport** using the coordinate
system of this **Viewport**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_oversampling}
::: rst-class
classref-method
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**get_oversampling**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_oversampling>`{.interpreted-text
role="ref"}

Returns viewport oversampling factor.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_positional_shadow_atlas_quadrant_subdiv}
::: rst-class
classref-method
:::
::::

`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"} **get_positional_shadow_atlas_quadrant_subdiv**(quadrant:
`int<class_int>`{.interpreted-text role="ref"})
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_positional_shadow_atlas_quadrant_subdiv>`{.interpreted-text
role="ref"}

Returns the positional shadow atlas quadrant subdivision of the
specified quadrant.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_render_info}
::: rst-class
classref-method
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **get_render_info**(type:
`RenderInfoType<enum_Viewport_RenderInfoType>`{.interpreted-text
role="ref"}, info:
`RenderInfo<enum_Viewport_RenderInfo>`{.interpreted-text role="ref"})
`🔗<class_Viewport_method_get_render_info>`{.interpreted-text
role="ref"}

Returns rendering statistics of the given type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_screen_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_screen_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_screen_transform>`{.interpreted-text
role="ref"}

Returns the transform from the Viewport\'s coordinates to the screen
coordinates of the containing window manager window.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_stretch_transform}
::: rst-class
classref-method
:::
::::

`Transform2D<class_Transform2D>`{.interpreted-text role="ref"}
**get_stretch_transform**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_stretch_transform>`{.interpreted-text
role="ref"}

Returns the automatically computed 2D stretch transform, taking the
**Viewport**\'s stretch settings into account. The final value is
multiplied by
`Window.content_scale_factor<class_Window_property_content_scale_factor>`{.interpreted-text
role="ref"}, but only for the root viewport. If this method is called on
a `SubViewport<class_SubViewport>`{.interpreted-text role="ref"} (e.g.,
in a scene tree with
`SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"} and `SubViewport<class_SubViewport>`{.interpreted-text
role="ref"}), the scale factor of the root window will not be applied.
Using
`Transform2D.get_scale()<class_Transform2D_method_get_scale>`{.interpreted-text
role="ref"} on the returned value, this can be used to compensate for
scaling when zooming a `Camera2D<class_Camera2D>`{.interpreted-text
role="ref"} node, or to scale down a
`TextureRect<class_TextureRect>`{.interpreted-text role="ref"} to be
pixel-perfect regardless of the automatically computed scale factor.

\*\*Note:\*\* Due to how pixel scaling works, the returned transform\'s
X and Y scale may differ slightly, even when
`Window.content_scale_aspect<class_Window_property_content_scale_aspect>`{.interpreted-text
role="ref"} is set to a mode that preserves the pixels\' aspect ratio.
If
`Window.content_scale_aspect<class_Window_property_content_scale_aspect>`{.interpreted-text
role="ref"} is
`Window.CONTENT_SCALE_ASPECT_IGNORE<class_Window_constant_CONTENT_SCALE_ASPECT_IGNORE>`{.interpreted-text
role="ref"}, the X and Y scale may differ *significantly*.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_texture}
::: rst-class
classref-method
:::
::::

`ViewportTexture<class_ViewportTexture>`{.interpreted-text role="ref"}
**get_texture**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"} `🔗<class_Viewport_method_get_texture>`{.interpreted-text
role="ref"}

Returns the viewport\'s texture.

\*\*Note:\*\* When trying to store the current texture (e.g. in a file),
it might be completely black or outdated if used too early, especially
when used in e.g.
`Node._ready()<class_Node_private_method__ready>`{.interpreted-text
role="ref"}. To make sure the texture you get is correct, you can await
`RenderingServer.frame_post_draw<class_RenderingServer_signal_frame_post_draw>`{.interpreted-text
role="ref"} signal.

    func _ready():
        await RenderingServer.frame_post_draw
        $Viewport.get_texture().get_image().save_png("user://Screenshot.png")

\*\*Note:\*\* When
`use_hdr_2d<class_Viewport_property_use_hdr_2d>`{.interpreted-text
role="ref"} is `true` the returned texture will be an HDR image encoded
in linear space.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_viewport_rid}
::: rst-class
classref-method
:::
::::

`RID<class_RID>`{.interpreted-text role="ref"} **get_viewport_rid**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_viewport_rid>`{.interpreted-text
role="ref"}

Returns the viewport\'s RID from the
`RenderingServer<class_RenderingServer>`{.interpreted-text role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_get_visible_rect}
::: rst-class
classref-method
:::
::::

`Rect2<class_Rect2>`{.interpreted-text role="ref"}
**get_visible_rect**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_get_visible_rect>`{.interpreted-text
role="ref"}

Returns the visible rectangle in global screen coordinates.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_cancel_drag}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**gui_cancel_drag**()
`🔗<class_Viewport_method_gui_cancel_drag>`{.interpreted-text
role="ref"}

Cancels the drag operation that was previously started through
`Control._get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"} or forced with
`Control.force_drag()<class_Control_method_force_drag>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_get_drag_data}
::: rst-class
classref-method
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"}
**gui_get_drag_data**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_gui_get_drag_data>`{.interpreted-text
role="ref"}

Returns the drag data from the GUI, that was previously returned by
`Control._get_drag_data()<class_Control_private_method__get_drag_data>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_get_drag_description}
::: rst-class
classref-method
:::
::::

`String<class_String>`{.interpreted-text role="ref"}
**gui_get_drag_description**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_gui_get_drag_description>`{.interpreted-text
role="ref"}

Returns the drag data human-readable description.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_get_focus_owner}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**gui_get_focus_owner**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_gui_get_focus_owner>`{.interpreted-text
role="ref"}

Returns the currently focused `Control<class_Control>`{.interpreted-text
role="ref"} within this viewport. If no
`Control<class_Control>`{.interpreted-text role="ref"} is focused,
returns `null`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_get_hovered_control}
::: rst-class
classref-method
:::
::::

`Control<class_Control>`{.interpreted-text role="ref"}
**gui_get_hovered_control**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_gui_get_hovered_control>`{.interpreted-text
role="ref"}

Returns the `Control<class_Control>`{.interpreted-text role="ref"} that
the mouse is currently hovering over in this viewport. If no
`Control<class_Control>`{.interpreted-text role="ref"} has the cursor,
returns `null`.

Typically the leaf `Control<class_Control>`{.interpreted-text
role="ref"} node or deepest level of the subtree which claims hover.
This is very useful when used together with
`Node.is_ancestor_of()<class_Node_method_is_ancestor_of>`{.interpreted-text
role="ref"} to find if the mouse is within a control tree.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_is_drag_successful}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**gui_is_drag_successful**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_gui_is_drag_successful>`{.interpreted-text
role="ref"}

Returns `true` if the drag operation is successful.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_is_dragging}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **gui_is_dragging**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_gui_is_dragging>`{.interpreted-text
role="ref"}

Returns `true` if a drag operation is currently ongoing and where the
drop action could happen in this viewport.

Alternative to
`Node.NOTIFICATION_DRAG_BEGIN<class_Node_constant_NOTIFICATION_DRAG_BEGIN>`{.interpreted-text
role="ref"} and
`Node.NOTIFICATION_DRAG_END<class_Node_constant_NOTIFICATION_DRAG_END>`{.interpreted-text
role="ref"} when you prefer polling the value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_release_focus}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**gui_release_focus**()
`🔗<class_Viewport_method_gui_release_focus>`{.interpreted-text
role="ref"}

Removes the focus from the currently focused
`Control<class_Control>`{.interpreted-text role="ref"} within this
viewport. If no `Control<class_Control>`{.interpreted-text role="ref"}
has the focus, does nothing.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_gui_set_drag_description}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**gui_set_drag_description**(description:
`String<class_String>`{.interpreted-text role="ref"})
`🔗<class_Viewport_method_gui_set_drag_description>`{.interpreted-text
role="ref"}

Sets the drag data human-readable description.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_is_input_handled}
::: rst-class
classref-method
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **is_input_handled**()
`const (This method has no side effects. It doesn't modify any of the instance's member variables.)`{.interpreted-text
role="abbr"}
`🔗<class_Viewport_method_is_input_handled>`{.interpreted-text
role="ref"}

Returns whether the current
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"} has been
handled. Input events are not handled until
`set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"} has been called during the lifetime of an
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"}.

This is usually done as part of input handling methods like
`Node._input()<class_Node_private_method__input>`{.interpreted-text
role="ref"},
`Control._gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
role="ref"} or others, as well as in corresponding signal handlers.

If
`handle_input_locally<class_Viewport_property_handle_input_locally>`{.interpreted-text
role="ref"} is set to `false`, this method will try finding the first
parent viewport that is set to handle input locally, and return its
value for
`is_input_handled()<class_Viewport_method_is_input_handled>`{.interpreted-text
role="ref"} instead.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_notify_mouse_entered}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_mouse_entered**()
`🔗<class_Viewport_method_notify_mouse_entered>`{.interpreted-text
role="ref"}

Inform the Viewport that the mouse has entered its area. Use this
function before sending an
`InputEventMouseButton<class_InputEventMouseButton>`{.interpreted-text
role="ref"} or
`InputEventMouseMotion<class_InputEventMouseMotion>`{.interpreted-text
role="ref"} to the **Viewport** with
`push_input()<class_Viewport_method_push_input>`{.interpreted-text
role="ref"}. See also
`notify_mouse_exited()<class_Viewport_method_notify_mouse_exited>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In most cases, it is not necessary to call this function
because `SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
nodes that are children of
`SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"} are notified automatically. This is only necessary when
interacting with viewports in non-default ways, for example as textures
in `TextureRect<class_TextureRect>`{.interpreted-text role="ref"} or
with an `Area3D<class_Area3D>`{.interpreted-text role="ref"} that
forwards input events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_notify_mouse_exited}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**notify_mouse_exited**()
`🔗<class_Viewport_method_notify_mouse_exited>`{.interpreted-text
role="ref"}

Inform the Viewport that the mouse has left its area. Use this function
when the node that displays the viewport notices the mouse has left the
area of the displayed viewport. See also
`notify_mouse_entered()<class_Viewport_method_notify_mouse_entered>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* In most cases, it is not necessary to call this function
because `SubViewport<class_SubViewport>`{.interpreted-text role="ref"}
nodes that are children of
`SubViewportContainer<class_SubViewportContainer>`{.interpreted-text
role="ref"} are notified automatically. This is only necessary when
interacting with viewports in non-default ways, for example as textures
in `TextureRect<class_TextureRect>`{.interpreted-text role="ref"} or
with an `Area3D<class_Area3D>`{.interpreted-text role="ref"} that
forwards input events.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_push_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_input**(event: `InputEvent<class_InputEvent>`{.interpreted-text
role="ref"}, in_local_coords: `bool<class_bool>`{.interpreted-text
role="ref"} = false)
`🔗<class_Viewport_method_push_input>`{.interpreted-text role="ref"}

Triggers the given `event` in this **Viewport**. This can be used to
pass an `InputEvent<class_InputEvent>`{.interpreted-text role="ref"}
between viewports, or to locally apply inputs that were sent over the
network or saved to a file.

If `in_local_coords` is `false`, the event\'s position is in the
embedder\'s coordinates and will be converted to viewport coordinates.
If `in_local_coords` is `true`, the event\'s position is in viewport
coordinates.

While this method serves a similar purpose as
`Input.parse_input_event()<class_Input_method_parse_input_event>`{.interpreted-text
role="ref"}, it does not remap the specified `event` based on project
settings like
`ProjectSettings.input_devices/pointing/emulate_touch_from_mouse<class_ProjectSettings_property_input_devices/pointing/emulate_touch_from_mouse>`{.interpreted-text
role="ref"}.

Calling this method will propagate calls to child nodes for following
methods in the given order:

- `Node._input()<class_Node_private_method__input>`{.interpreted-text
  role="ref"}
- `Control._gui_input()<class_Control_private_method__gui_input>`{.interpreted-text
  role="ref"} for `Control<class_Control>`{.interpreted-text role="ref"}
  nodes
- `Node._shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
  role="ref"}
- `Node._unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
  role="ref"}
- `Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
  role="ref"}

If an earlier method marks the input as handled via
`set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"}, any later method in this list will not be called.

If none of the methods handle the event and
`physics_object_picking<class_Viewport_property_physics_object_picking>`{.interpreted-text
role="ref"} is `true`, the event is used for physics object picking.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_push_text_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_text_input**(text: `String<class_String>`{.interpreted-text
role="ref"})
`🔗<class_Viewport_method_push_text_input>`{.interpreted-text
role="ref"}

Helper method which calls the `set_text()` method on the currently
focused `Control<class_Control>`{.interpreted-text role="ref"}, provided
that it is defined (e.g. if the focused Control is
`Button<class_Button>`{.interpreted-text role="ref"} or
`LineEdit<class_LineEdit>`{.interpreted-text role="ref"}).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_push_unhandled_input}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**push_unhandled_input**(event:
`InputEvent<class_InputEvent>`{.interpreted-text role="ref"},
in_local_coords: `bool<class_bool>`{.interpreted-text role="ref"} =
false)
`🔗<class_Viewport_method_push_unhandled_input>`{.interpreted-text
role="ref"}

**Deprecated:** Use
`push_input()<class_Viewport_method_push_input>`{.interpreted-text
role="ref"} instead.

Triggers the given `event` in this **Viewport**. This can be used to
pass an `InputEvent<class_InputEvent>`{.interpreted-text role="ref"}
between viewports, or to locally apply inputs that were sent over the
network or saved to a file.

If `in_local_coords` is `false`, the event\'s position is in the
embedder\'s coordinates and will be converted to viewport coordinates.
If `in_local_coords` is `true`, the event\'s position is in viewport
coordinates.

Calling this method will propagate calls to child nodes for following
methods in the given order:

- `Node._shortcut_input()<class_Node_private_method__shortcut_input>`{.interpreted-text
  role="ref"}
- `Node._unhandled_key_input()<class_Node_private_method__unhandled_key_input>`{.interpreted-text
  role="ref"}
- `Node._unhandled_input()<class_Node_private_method__unhandled_input>`{.interpreted-text
  role="ref"}

If an earlier method marks the input as handled via
`set_input_as_handled()<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"}, any later method in this list will not be called.

If none of the methods handle the event and
`physics_object_picking<class_Viewport_property_physics_object_picking>`{.interpreted-text
role="ref"} is `true`, the event is used for physics object picking.

\*\*Note:\*\* This method doesn\'t propagate input events to embedded
`Window<class_Window>`{.interpreted-text role="ref"}s or
`SubViewport<class_SubViewport>`{.interpreted-text role="ref"}s.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_set_canvas_cull_mask_bit}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_canvas_cull_mask_bit**(layer: `int<class_int>`{.interpreted-text
role="ref"}, enable: `bool<class_bool>`{.interpreted-text role="ref"})
`🔗<class_Viewport_method_set_canvas_cull_mask_bit>`{.interpreted-text
role="ref"}

Set/clear individual bits on the rendering layer mask. This simplifies
editing this **Viewport**\'s layers.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_set_input_as_handled}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_input_as_handled**()
`🔗<class_Viewport_method_set_input_as_handled>`{.interpreted-text
role="ref"}

Stops the input from propagating further down the
`SceneTree<class_SceneTree>`{.interpreted-text role="ref"}.

\*\*Note:\*\* This does not affect the methods in
`Input<class_Input>`{.interpreted-text role="ref"}, only the way events
are propagated.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_set_positional_shadow_atlas_quadrant_subdiv}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_positional_shadow_atlas_quadrant_subdiv**(quadrant:
`int<class_int>`{.interpreted-text role="ref"}, subdiv:
`PositionalShadowAtlasQuadrantSubdiv<enum_Viewport_PositionalShadowAtlasQuadrantSubdiv>`{.interpreted-text
role="ref"})
`🔗<class_Viewport_method_set_positional_shadow_atlas_quadrant_subdiv>`{.interpreted-text
role="ref"}

Sets the number of subdivisions to use in the specified quadrant. A
higher number of subdivisions allows you to have more shadows in the
scene at once, but reduces the quality of the shadows. A good practice
is to have quadrants with a varying number of subdivisions and to have
as few subdivisions as possible.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_update_mouse_cursor_state}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**update_mouse_cursor_state**()
`🔗<class_Viewport_method_update_mouse_cursor_state>`{.interpreted-text
role="ref"}

Force instantly updating the display based on the current mouse cursor
position. This includes updating the mouse cursor shape and sending
necessary
`Control.mouse_entered<class_Control_signal_mouse_entered>`{.interpreted-text
role="ref"},
`CollisionObject2D.mouse_entered<class_CollisionObject2D_signal_mouse_entered>`{.interpreted-text
role="ref"},
`CollisionObject3D.mouse_entered<class_CollisionObject3D_signal_mouse_entered>`{.interpreted-text
role="ref"} and
`Window.mouse_entered<class_Window_signal_mouse_entered>`{.interpreted-text
role="ref"} signals and their respective `mouse_exited` counterparts.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_Viewport_method_warp_mouse}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**warp_mouse**(position: `Vector2<class_Vector2>`{.interpreted-text
role="ref"}) `🔗<class_Viewport_method_warp_mouse>`{.interpreted-text
role="ref"}

Moves the mouse pointer to the specified position in this **Viewport**
using the coordinate system of this **Viewport**.

\*\*Note:\*\*
`warp_mouse()<class_Viewport_method_warp_mouse>`{.interpreted-text
role="ref"} is only supported on Windows, macOS and Linux. It has no
effect on Android, iOS and Web.
