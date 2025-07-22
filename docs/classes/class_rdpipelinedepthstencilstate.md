github_url
:   hide

# RDPipelineDepthStencilState {#class_RDPipelineDepthStencilState}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Pipeline depth/stencil state (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

**RDPipelineDepthStencilState** controls the way depth and stencil
comparisons are performed when sampling those values using
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

:::: {#class_RDPipelineDepthStencilState_property_back_op_compare}
::: rst-class
classref-property
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **back_op_compare** = `7`
`🔗<class_RDPipelineDepthStencilState_property_back_op_compare>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_back_op_compare**(value:
  `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"})
- `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"} **get_back_op_compare**()

The method used for comparing the previous back stencil value and
`back_op_reference<class_RDPipelineDepthStencilState_property_back_op_reference>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_back_op_compare_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **back_op_compare_mask**
= `0`
`🔗<class_RDPipelineDepthStencilState_property_back_op_compare_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_back_op_compare_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_back_op_compare_mask**()

Selects which bits from the back stencil value will be compared.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_back_op_depth_fail}
::: rst-class
classref-property
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **back_op_depth_fail** = `1`
`🔗<class_RDPipelineDepthStencilState_property_back_op_depth_fail>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_back_op_depth_fail**(value:
  `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"})
- `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"} **get_back_op_depth_fail**()

The operation to perform on the stencil buffer for back pixels that pass
the stencil test but fail the depth test.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_back_op_fail}
::: rst-class
classref-property
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **back_op_fail** = `1`
`🔗<class_RDPipelineDepthStencilState_property_back_op_fail>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_back_op_fail**(value:
  `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"})
- `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"} **get_back_op_fail**()

The operation to perform on the stencil buffer for back pixels that fail
the stencil test.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_back_op_pass}
::: rst-class
classref-property
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **back_op_pass** = `1`
`🔗<class_RDPipelineDepthStencilState_property_back_op_pass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_back_op_pass**(value:
  `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"})
- `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"} **get_back_op_pass**()

The operation to perform on the stencil buffer for back pixels that pass
the stencil test.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_back_op_reference}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **back_op_reference** =
`0`
`🔗<class_RDPipelineDepthStencilState_property_back_op_reference>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_back_op_reference**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_back_op_reference**()

The value the previous back stencil value will be compared to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_back_op_write_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **back_op_write_mask** =
`0`
`🔗<class_RDPipelineDepthStencilState_property_back_op_write_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_back_op_write_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_back_op_write_mask**()

Selects which bits from the back stencil value will be changed.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_depth_compare_operator}
::: rst-class
classref-property
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **depth_compare_operator** = `7`
`🔗<class_RDPipelineDepthStencilState_property_depth_compare_operator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_compare_operator**(value:
  `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"})
- `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"} **get_depth_compare_operator**()

The method used for comparing the previous and current depth values.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_depth_range_max}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth_range_max** =
`0.0`
`🔗<class_RDPipelineDepthStencilState_property_depth_range_max>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_range_max**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_depth_range_max**()

The maximum depth that returns `true` for
`enable_depth_range<class_RDPipelineDepthStencilState_property_enable_depth_range>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_depth_range_min}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **depth_range_min** =
`0.0`
`🔗<class_RDPipelineDepthStencilState_property_depth_range_min>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_depth_range_min**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_depth_range_min**()

The minimum depth that returns `true` for
`enable_depth_range<class_RDPipelineDepthStencilState_property_enable_depth_range>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_enable_depth_range}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_depth_range**
= `false`
`🔗<class_RDPipelineDepthStencilState_property_enable_depth_range>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_depth_range**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_depth_range**()

If `true`, each depth value will be tested to see if it is between
`depth_range_min<class_RDPipelineDepthStencilState_property_depth_range_min>`{.interpreted-text
role="ref"} and
`depth_range_max<class_RDPipelineDepthStencilState_property_depth_range_max>`{.interpreted-text
role="ref"}. If it is outside of these values, it is discarded.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_enable_depth_test}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_depth_test** =
`false`
`🔗<class_RDPipelineDepthStencilState_property_enable_depth_test>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_depth_test**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_depth_test**()

If `true`, enables depth testing which allows objects to be
automatically occluded by other objects based on their depth. This also
allows objects to be partially occluded by other objects. If `false`,
objects will appear in the order they were drawn (like in Godot\'s 2D
renderer).

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_enable_depth_write}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_depth_write**
= `false`
`🔗<class_RDPipelineDepthStencilState_property_enable_depth_write>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_depth_write**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_depth_write**()

If `true`, writes to the depth buffer whenever the depth test returns
`true`. Only works when enable_depth_test is also `true`.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_enable_stencil}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_stencil** =
`false`
`🔗<class_RDPipelineDepthStencilState_property_enable_stencil>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_stencil**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_stencil**()

If `true`, enables stencil testing. There are separate stencil buffers
for front-facing triangles and back-facing triangles. See properties
that begin with \"front_op\" and properties with \"back_op\" for each.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_front_op_compare}
::: rst-class
classref-property
:::
::::

`CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
role="ref"} **front_op_compare** = `7`
`🔗<class_RDPipelineDepthStencilState_property_front_op_compare>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_op_compare**(value:
  `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"})
- `CompareOperator<enum_RenderingDevice_CompareOperator>`{.interpreted-text
  role="ref"} **get_front_op_compare**()

The method used for comparing the previous front stencil value and
`front_op_reference<class_RDPipelineDepthStencilState_property_front_op_reference>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_front_op_compare_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **front_op_compare_mask**
= `0`
`🔗<class_RDPipelineDepthStencilState_property_front_op_compare_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_op_compare_mask**(value:
  `int<class_int>`{.interpreted-text role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_front_op_compare_mask**()

Selects which bits from the front stencil value will be compared.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_front_op_depth_fail}
::: rst-class
classref-property
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **front_op_depth_fail** = `1`
`🔗<class_RDPipelineDepthStencilState_property_front_op_depth_fail>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_op_depth_fail**(value:
  `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"})
- `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"} **get_front_op_depth_fail**()

The operation to perform on the stencil buffer for front pixels that
pass the stencil test but fail the depth test.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_front_op_fail}
::: rst-class
classref-property
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **front_op_fail** = `1`
`🔗<class_RDPipelineDepthStencilState_property_front_op_fail>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_op_fail**(value:
  `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"})
- `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"} **get_front_op_fail**()

The operation to perform on the stencil buffer for front pixels that
fail the stencil test.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_front_op_pass}
::: rst-class
classref-property
:::
::::

`StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
role="ref"} **front_op_pass** = `1`
`🔗<class_RDPipelineDepthStencilState_property_front_op_pass>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_op_pass**(value:
  `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"})
- `StencilOperation<enum_RenderingDevice_StencilOperation>`{.interpreted-text
  role="ref"} **get_front_op_pass**()

The operation to perform on the stencil buffer for front pixels that
pass the stencil test.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_front_op_reference}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **front_op_reference** =
`0`
`🔗<class_RDPipelineDepthStencilState_property_front_op_reference>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_op_reference**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_front_op_reference**()

The value the previous front stencil value will be compared to.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineDepthStencilState_property_front_op_write_mask}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **front_op_write_mask** =
`0`
`🔗<class_RDPipelineDepthStencilState_property_front_op_write_mask>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_front_op_write_mask**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"}
  **get_front_op_write_mask**()

Selects which bits from the front stencil value will be changed.
