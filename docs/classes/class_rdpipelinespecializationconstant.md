github_url
:   hide

# RDPipelineSpecializationConstant {#class_RDPipelineSpecializationConstant}

**Inherits:** `RefCounted<class_RefCounted>`{.interpreted-text
role="ref"} **\<** `Object<class_Object>`{.interpreted-text role="ref"}

Pipeline specialization constant (used by
`RenderingDevice<class_RenderingDevice>`{.interpreted-text role="ref"}).

::: rst-class
classref-introduction-group
:::

## Description

A *specialization constant* is a way to create additional variants of
shaders without actually increasing the number of shader versions that
are compiled. This allows improving performance by reducing the number
of shader versions and reducing `if` branching, while still allowing
shaders to be flexible for different use cases.

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

:::: {#class_RDPipelineSpecializationConstant_property_constant_id}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **constant_id** = `0`
`🔗<class_RDPipelineSpecializationConstant_property_constant_id>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_constant_id**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_constant_id**()

The identifier of the specialization constant. This is a value starting
from `0` and that increments for every different specialization constant
for a given shader.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_RDPipelineSpecializationConstant_property_value}
::: rst-class
classref-property
:::
::::

`Variant<class_Variant>`{.interpreted-text role="ref"} **value**
`🔗<class_RDPipelineSpecializationConstant_property_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_value**(value: `Variant<class_Variant>`{.interpreted-text
  role="ref"})
- `Variant<class_Variant>`{.interpreted-text role="ref"} **get_value**()

The specialization constant\'s value. Only
`bool<class_bool>`{.interpreted-text role="ref"},
`int<class_int>`{.interpreted-text role="ref"} and
`float<class_float>`{.interpreted-text role="ref"} types are valid for
specialization constants.
