github_url
:   hide

# VisualShaderNodeUIntFunc {#class_VisualShaderNodeUIntFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

An unsigned scalar integer function to be used within the visual shader
graph.

::: rst-class
classref-introduction-group
:::

## Description

Accept an unsigned integer scalar (`x`) to the input port and transform
it according to
`function<class_VisualShaderNodeUIntFunc_property_function>`{.interpreted-text
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

:::: {#enum_VisualShaderNodeUIntFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeUIntFunc_constant_FUNC_NEGATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_NEGATE** = `0`

Negates the `x` using `-(x)`.

:::: {#class_VisualShaderNodeUIntFunc_constant_FUNC_BITWISE_NOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_BITWISE_NOT** = `1`

Returns the result of bitwise `NOT` operation on the integer. Translates
to `~a` in the Godot Shader Language.

:::: {#class_VisualShaderNodeUIntFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `2`

Represents the size of the
`Function<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeUIntFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeUIntFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeUIntFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

A function to be applied to the scalar.
