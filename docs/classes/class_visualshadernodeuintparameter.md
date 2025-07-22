github_url
:   hide

# VisualShaderNodeUIntParameter {#class_VisualShaderNodeUIntParameter}

**Inherits:**
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A visual shader node for shader parameter (uniform) of type unsigned
`int<class_int>`{.interpreted-text role="ref"}.

::: rst-class
classref-introduction-group
:::

## Description

A
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} of type unsigned `int<class_int>`{.interpreted-text
role="ref"}. Offers additional customization for range of accepted
values.

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

:::: {#class_VisualShaderNodeUIntParameter_property_default_value}
::: rst-class
classref-property
:::
::::

`int<class_int>`{.interpreted-text role="ref"} **default_value** = `0`
`🔗<class_VisualShaderNodeUIntParameter_property_default_value>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value**(value: `int<class_int>`{.interpreted-text
  role="ref"})
- `int<class_int>`{.interpreted-text role="ref"} **get_default_value**()

Default value of this parameter, which will be used if not set
externally.
`default_value_enabled<class_VisualShaderNodeUIntParameter_property_default_value_enabled>`{.interpreted-text
role="ref"} must be enabled; defaults to `0` otherwise.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeUIntParameter_property_default_value_enabled}
::: rst-class
classref-property
:::
::::

`bool<class_bool>`{.interpreted-text role="ref"}
**default_value_enabled** = `false`
`🔗<class_VisualShaderNodeUIntParameter_property_default_value_enabled>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_default_value_enabled**(value:
  `bool<class_bool>`{.interpreted-text role="ref"})
- `bool<class_bool>`{.interpreted-text role="ref"}
  **is_default_value_enabled**()

If `true`, the node will have a custom default value.
