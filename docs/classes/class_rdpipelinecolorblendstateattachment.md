github_url
:   hide

# RDPipelineColorBlendStateAttachment {#class_RDPipelineColorBlendStateAttachment}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Pipeline color blend state attachment (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

Controls how blending between source and destination fragments is
performed when using
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}.

For reference, this is how common user-facing blend modes are
implemented in Godot\'s 2D renderer:

\*\*Mix:\*\*

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA

\*\*Add:\*\*

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE

\*\*Subtract:\*\*

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
    attachment.color_blend_op = RenderingDevice.BLEND_OP_REVERSE_SUBTRACT
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_SRC_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE

\*\*Multiply:\*\*

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_DST_COLOR
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_DST_ALPHA
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ZERO

\*\*Pre-multiplied alpha:\*\*

    var attachment = RDPipelineColorBlendStateAttachment.new()
    attachment.enable_blend = true
    attachment.alpha_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.color_blend_op = RenderingDevice.BLEND_OP_ADD
    attachment.src_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_color_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
    attachment.src_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE
    attachment.dst_alpha_blend_factor = RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA

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

:::: {#class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op}
::: rst-class
classref-property
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **alpha_blend_op** = `0`
`🔗<class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_alpha_blend_op**(value:
  `BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
  role="ref"})
- `BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
  role="ref"} **get_alpha_blend_op**()

The blend mode to use for the alpha channel.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_color_blend_op}
::: rst-class
classref-property
:::
::::

`BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
role="ref"} **color_blend_op** = `0`
`🔗<class_RDPipelineColorBlendStateAttachment_property_color_blend_op>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_blend_op**(value:
  `BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
  role="ref"})
- `BlendOperation<enum_RenderingDevice_BlendOperation>`{.interpreted-text
  role="ref"} **get_color_blend_op**()

The blend mode to use for the red/green/blue color channels.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor}
::: rst-class
classref-property
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **dst_alpha_blend_factor** = `0`
`🔗<class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dst_alpha_blend_factor**(value:
  `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"})
- `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"} **get_dst_alpha_blend_factor**()

Controls how the blend factor for the alpha channel is determined based
on the destination\'s fragments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor}
::: rst-class
classref-property
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **dst_color_blend_factor** = `0`
`🔗<class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_dst_color_blend_factor**(value:
  `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"})
- `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"} **get_dst_color_blend_factor**()

Controls how the blend factor for the color channels is determined based
on the destination\'s fragments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_enable_blend}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **enable_blend** =
`false`
`🔗<class_RDPipelineColorBlendStateAttachment_property_enable_blend>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_enable_blend**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **get_enable_blend**()

If `true`, performs blending between the source and destination
according to the factors defined in
`src_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor>`{.interpreted-text
role="ref"},
`dst_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor>`{.interpreted-text
role="ref"},
`src_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor>`{.interpreted-text
role="ref"} and
`dst_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor>`{.interpreted-text
role="ref"}. The blend modes
`color_blend_op<class_RDPipelineColorBlendStateAttachment_property_color_blend_op>`{.interpreted-text
role="ref"} and
`alpha_blend_op<class_RDPipelineColorBlendStateAttachment_property_alpha_blend_op>`{.interpreted-text
role="ref"} are also taken into account, with
`write_r<class_RDPipelineColorBlendStateAttachment_property_write_r>`{.interpreted-text
role="ref"},
`write_g<class_RDPipelineColorBlendStateAttachment_property_write_g>`{.interpreted-text
role="ref"},
`write_b<class_RDPipelineColorBlendStateAttachment_property_write_b>`{.interpreted-text
role="ref"} and
`write_a<class_RDPipelineColorBlendStateAttachment_property_write_a>`{.interpreted-text
role="ref"} controlling the output.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor}
::: rst-class
classref-property
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **src_alpha_blend_factor** = `0`
`🔗<class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_src_alpha_blend_factor**(value:
  `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"})
- `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"} **get_src_alpha_blend_factor**()

Controls how the blend factor for the alpha channel is determined based
on the source\'s fragments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor}
::: rst-class
classref-property
:::
::::

`BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
role="ref"} **src_color_blend_factor** = `0`
`🔗<class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_src_color_blend_factor**(value:
  `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"})
- `BlendFactor<enum_RenderingDevice_BlendFactor>`{.interpreted-text
  role="ref"} **get_src_color_blend_factor**()

Controls how the blend factor for the color channels is determined based
on the source\'s fragments.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_write_a}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **write_a** = `true`
`🔗<class_RDPipelineColorBlendStateAttachment_property_write_a>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_write_a**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_write_a**()

If `true`, writes the new alpha channel to the final result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_write_b}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **write_b** = `true`
`🔗<class_RDPipelineColorBlendStateAttachment_property_write_b>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_write_b**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_write_b**()

If `true`, writes the new blue color channel to the final result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_write_g}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **write_g** = `true`
`🔗<class_RDPipelineColorBlendStateAttachment_property_write_g>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_write_g**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_write_g**()

If `true`, writes the new green color channel to the final result.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineColorBlendStateAttachment_property_write_r}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **write_r** = `true`
`🔗<class_RDPipelineColorBlendStateAttachment_property_write_r>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_write_r**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"} **get_write_r**()

If `true`, writes the new red color channel to the final result.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Method Descriptions

:::: {#class_RDPipelineColorBlendStateAttachment_method_set_as_mix}
::: rst-class
classref-method
:::
::::

`void (No return value.)`{.interpreted-text role="abbr"}
**set_as_mix**()
`🔗<class_RDPipelineColorBlendStateAttachment_method_set_as_mix>`{.interpreted-text
role="ref"}

Convenience method to perform standard mix blending with straight
(non-premultiplied) alpha. This sets
`enable_blend<class_RDPipelineColorBlendStateAttachment_property_enable_blend>`{.interpreted-text
role="ref"} to `true`,
`src_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_color_blend_factor>`{.interpreted-text
role="ref"} to
`RenderingDevice.BLEND_FACTOR_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA>`{.interpreted-text
role="ref"},
`dst_color_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_color_blend_factor>`{.interpreted-text
role="ref"} to
`RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA>`{.interpreted-text
role="ref"},
`src_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_src_alpha_blend_factor>`{.interpreted-text
role="ref"} to
`RenderingDevice.BLEND_FACTOR_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_SRC_ALPHA>`{.interpreted-text
role="ref"} and
`dst_alpha_blend_factor<class_RDPipelineColorBlendStateAttachment_property_dst_alpha_blend_factor>`{.interpreted-text
role="ref"} to
`RenderingDevice.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA<class_RenderingDevice_constant_BLEND_FACTOR_ONE_MINUS_SRC_ALPHA>`{.interpreted-text
role="ref"}.
