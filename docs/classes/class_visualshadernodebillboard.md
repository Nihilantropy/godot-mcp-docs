github_url
:   hide

# VisualShaderNodeBillboard {#class_VisualShaderNodeBillboard}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A node that controls how the object faces the camera to be used within
the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

The output port of this node needs to be connected to
`Model View Matrix` port of
`VisualShaderNodeOutput<class_VisualShaderNodeOutput>`{.interpreted-text
role="ref"}.

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

## Enumerations

:::: {#enum_VisualShaderNodeBillboard_BillboardType}
::: rst-class
classref-enumeration
:::
::::

enum **BillboardType**:
`🔗<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"} **BILLBOARD_TYPE_DISABLED** = `0`

Billboarding is disabled and the node does nothing.

:::: {#class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"} **BILLBOARD_TYPE_ENABLED** = `1`

A standard billboarding algorithm is enabled.

:::: {#class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_FIXED_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"} **BILLBOARD_TYPE_FIXED_Y** = `2`

A billboarding algorithm to rotate around Y-axis is enabled.

:::: {#class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_PARTICLES}
::: rst-class
classref-enumeration-constant
:::
::::

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"} **BILLBOARD_TYPE_PARTICLES** = `3`

A billboarding algorithm designed to use on particles is enabled.

:::: {#class_VisualShaderNodeBillboard_constant_BILLBOARD_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"} **BILLBOARD_TYPE_MAX** = `4`

Represents the size of the
`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeBillboard_property_billboard_type}
::: rst-class
classref-property
:::
::::

`BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
role="ref"} **billboard_type** = `1`
`🔗<class_VisualShaderNodeBillboard_property_billboard_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_billboard_type**(value:
  `BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
  role="ref"})
- `BillboardType<enum_VisualShaderNodeBillboard_BillboardType>`{.interpreted-text
  role="ref"} **get_billboard_type**()

Controls how the object faces the camera.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeBillboard_property_keep_scale}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"} **keep_scale** =
`false`
`🔗<class_VisualShaderNodeBillboard_property_keep_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_keep_scale_enabled**(value: `bool<class_bool>`{.interpreted-text
  role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_keep_scale_enabled**()

If `true`, the shader will keep the scale set for the mesh. Otherwise,
the scale is lost when billboarding.
