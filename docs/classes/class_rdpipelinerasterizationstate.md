github_url
:   hide

# RDPipelineRasterizationState {#class_RDPipelineRasterizationState}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Pipeline rasterization state (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

This object is used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

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

:::: {#class_RDPipelineRasterizationState_property_cull_mode}
::: rst-class
classref-property
:::
::::

`PolygonCullMode<enum_RenderingDevice_PolygonCullMode>`{.interpreted-text
role="ref"} **cull_mode** = `0`
`🔗<class_RDPipelineRasterizationState_property_cull_mode>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cull_mode**(value:
  `PolygonCullMode<enum_RenderingDevice_PolygonCullMode>`{.interpreted-text
  role="ref"})
- `PolygonCullMode<enum_RenderingDevice_PolygonCullMode>`{.interpreted-text
  role="ref"} **get_cull_mode**()

The cull mode to use when drawing polygons, which determines whether
front faces or backfaces are hidden.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_depth_bias_clamp}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth_bias_clamp**
= `0.0`
`🔗<class_RDPipelineRasterizationState_property_depth_bias_clamp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_bias_clamp**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_depth_bias_clamp**()

A limit for how much each depth value can be offset. If negative, it
serves as a minimum value, but if positive, it serves as a maximum
value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_depth_bias_constant_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**depth_bias_constant_factor** = `0.0`
`🔗<class_RDPipelineRasterizationState_property_depth_bias_constant_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_bias_constant_factor**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_depth_bias_constant_factor**()

A constant offset added to each depth value. Applied after
`depth_bias_slope_factor<class_RDPipelineRasterizationState_property_depth_bias_slope_factor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_depth_bias_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **depth_bias_enabled**
= `false`
`🔗<class_RDPipelineRasterizationState_property_depth_bias_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_bias_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_depth_bias_enabled**()

If `true`, each generated depth value will by offset by some amount. The
specific amount is generated per polygon based on the values of
`depth_bias_slope_factor<class_RDPipelineRasterizationState_property_depth_bias_slope_factor>`{.interpreted-text
role="ref"} and
`depth_bias_constant_factor<class_RDPipelineRasterizationState_property_depth_bias_constant_factor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_depth_bias_slope_factor}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**depth_bias_slope_factor** = `0.0`
`🔗<class_RDPipelineRasterizationState_property_depth_bias_slope_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_bias_slope_factor**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_depth_bias_slope_factor**()

A constant scale applied to the slope of each polygons\' depth. Applied
before
`depth_bias_constant_factor<class_RDPipelineRasterizationState_property_depth_bias_constant_factor>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_discard_primitives}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **discard_primitives**
= `false`
`🔗<class_RDPipelineRasterizationState_property_discard_primitives>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_discard_primitives**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_discard_primitives**()

If `true`, primitives are discarded immediately before the rasterization
stage.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_enable_depth_clamp}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_depth_clamp**
= `false`
`🔗<class_RDPipelineRasterizationState_property_enable_depth_clamp>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_depth_clamp**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_depth_clamp**()

If `true`, clamps depth values according to the minimum and maximum
depth of the associated viewport.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_front_face}
::: rst-class
classref-property
:::
::::

`PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>`{.interpreted-text
role="ref"} **front_face** = `0`
`🔗<class_RDPipelineRasterizationState_property_front_face>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_face**(value:
  `PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>`{.interpreted-text
  role="ref"})
- `PolygonFrontFace<enum_RenderingDevice_PolygonFrontFace>`{.interpreted-text
  role="ref"} **get_front_face**()

The winding order to use to determine which face of a triangle is
considered its front face.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_line_width}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **line_width** =
`1.0`
`🔗<class_RDPipelineRasterizationState_property_line_width>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_line_width**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_line_width**()

The line width to use when drawing lines (in pixels). Thick lines may
not be supported on all hardware.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_patch_control_points}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **patch_control_points**
= `1`
`🔗<class_RDPipelineRasterizationState_property_patch_control_points>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_patch_control_points**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_patch_control_points**()

The number of control points to use when drawing a patch with
tessellation enabled. Higher values result in higher quality at the cost
of performance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineRasterizationState_property_wireframe}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **wireframe** = `false`
`🔗<class_RDPipelineRasterizationState_property_wireframe>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_wireframe**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_wireframe**()

If `true`, performs wireframe rendering for triangles instead of flat or
textured rendering.
