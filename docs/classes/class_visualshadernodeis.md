github_url
:   hide

# VisualShaderNodeIs {#class_VisualShaderNodeIs}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A boolean comparison operator to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Returns the boolean result of the comparison between `INF` or `NaN` and
a scalar parameter.

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

:::: {#enum_VisualShaderNodeIs_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeIs_Function>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeIs_constant_FUNC_IS_INF}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIs_Function>`{.interpreted-text
role="ref"} **FUNC_IS_INF** = `0`

Comparison with `INF` (Infinity).

:::: {#class_VisualShaderNodeIs_constant_FUNC_IS_NAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIs_Function>`{.interpreted-text
role="ref"} **FUNC_IS_NAN** = `1`

Comparison with `NaN` (Not a Number; indicates invalid numeric results,
such as division by zero).

:::: {#class_VisualShaderNodeIs_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIs_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `2`

Represents the size of the
`Function<enum_VisualShaderNodeIs_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeIs_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeIs_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeIs_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeIs_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeIs_Function>`{.interpreted-text
  role="ref"} **get_function**()

The comparison function.
