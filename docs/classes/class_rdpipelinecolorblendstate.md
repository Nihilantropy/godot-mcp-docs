github_url
:   hide

# RDPipelineColorBlendState {#class_RDPipelineColorBlendState}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Pipeline color blend state (used by
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

:::: {#class_RDPipelineColorBlendState_property_attachments}
::: rst-class
classref-property
:::
::::

`Array<class_Array>`{.interpreted-text
role="ref"}\[`RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>`{.interpreted-text
role="ref"}\] **attachments** = `[]`
`🔗<class_RDPipelineColorBlendState_property_attachments>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_attachments**(value: `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>`{.interpreted-text
  role="ref"}\])
- `Array<class_Array>`{.interpreted-text
  role="ref"}\[`RDPipelineColorBlendStateAttachment<class_RDPipelineColorBlendStateAttachment>`{.interpreted-text
  role="ref"}\] **get_attachments**()

The attachments that are blended together.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendState_property_blend_constant}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **blend_constant** =
`Color(0, 0, 0, 1)`
`🔗<class_RDPipelineColorBlendState_property_blend_constant>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_blend_constant**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_blend_constant**()

The constant color to blend with. See also
`RenderingDevice.draw_list_set_blend_constants()<class_RenderingDevice_method_draw_list_set_blend_constants>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendState_property_enable_logic_op}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_logic_op** =
`false`
`🔗<class_RDPipelineColorBlendState_property_enable_logic_op>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_logic_op**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_logic_op**()

If `true`, performs the logic operation defined in
`logic_op<class_RDPipelineColorBlendState_property_logic_op>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendState_property_logic_op}
::: rst-class
classref-property
:::
::::

`LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
role="ref"} **logic_op** = `0`
`🔗<class_RDPipelineColorBlendState_property_logic_op>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_logic_op**(value:
  `LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
  role="ref"})
- `LogicOperation<enum_RenderingDevice_LogicOperation>`{.interpreted-text
  role="ref"} **get_logic_op**()

The logic operation to perform for blending. Only effective if
`enable_logic_op<class_RDPipelineColorBlendState_property_enable_logic_op>`{.interpreted-text
role="ref"} is `true`.
