github_url
:   hide

# VisualShaderNodeColorOp {#class_VisualShaderNodeColorOp}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Color<class_Color>`{.interpreted-text role="ref"} operator to be used
within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Applies
`operator<class_VisualShaderNodeColorOp_property_operator>`{.interpreted-text
role="ref"} to two color inputs.

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

:::: {#enum_VisualShaderNodeColorOp_Operator}
::: rst-class
classref-enumeration
:::
::::

enum **Operator**:
`🔗<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeColorOp_constant_OP_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_SCREEN** = `0`

Produce a screen effect with the following formula:

    result = vec3(1.0) - (vec3(1.0) - a) * (vec3(1.0) - b);

:::: {#class_VisualShaderNodeColorOp_constant_OP_DIFFERENCE}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_DIFFERENCE** = `1`

Produce a difference effect with the following formula:

    result = abs(a - b);

:::: {#class_VisualShaderNodeColorOp_constant_OP_DARKEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_DARKEN** = `2`

Produce a darken effect with the following formula:

    result = min(a, b);

:::: {#class_VisualShaderNodeColorOp_constant_OP_LIGHTEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_LIGHTEN** = `3`

Produce a lighten effect with the following formula:

    result = max(a, b);

:::: {#class_VisualShaderNodeColorOp_constant_OP_OVERLAY}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_OVERLAY** = `4`

Produce an overlay effect with the following formula:

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = 2.0 * base * blend;
        } else {
            result[i] = 1.0 - 2.0 * (1.0 - blend) * (1.0 - base);
        }
    }

:::: {#class_VisualShaderNodeColorOp_constant_OP_DODGE}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_DODGE** = `5`

Produce a dodge effect with the following formula:

    result = a / (vec3(1.0) - b);

:::: {#class_VisualShaderNodeColorOp_constant_OP_BURN}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_BURN** = `6`

Produce a burn effect with the following formula:

    result = vec3(1.0) - (vec3(1.0) - a) / b;

:::: {#class_VisualShaderNodeColorOp_constant_OP_SOFT_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_SOFT_LIGHT** = `7`

Produce a soft light effect with the following formula:

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = base * (blend + 0.5);
        } else {
            result[i] = 1.0 - (1.0 - base) * (1.0 - (blend - 0.5));
        }
    }

:::: {#class_VisualShaderNodeColorOp_constant_OP_HARD_LIGHT}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_HARD_LIGHT** = `8`

Produce a hard light effect with the following formula:

    for (int i = 0; i < 3; i++) {
        float base = a[i];
        float blend = b[i];
        if (base < 0.5) {
            result[i] = base * (2.0 * blend);
        } else {
            result[i] = 1.0 - (1.0 - base) * (1.0 - 2.0 * (blend - 0.5));
        }
    }

:::: {#class_VisualShaderNodeColorOp_constant_OP_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **OP_MAX** = `9`

Represents the size of the
`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeColorOp_property_operator}
::: rst-class
classref-property
:::
::::

`Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
role="ref"} **operator** = `0`
`🔗<class_VisualShaderNodeColorOp_property_operator>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_operator**(value:
  `Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
  role="ref"})
- `Operator<enum_VisualShaderNodeColorOp_Operator>`{.interpreted-text
  role="ref"} **get_operator**()

An operator to be applied to the inputs.
