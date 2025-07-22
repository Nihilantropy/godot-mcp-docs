github_url
:   hide

# VisualShaderNodeIntFunc {#class_VisualShaderNodeIntFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A scalar integer function to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Accept an integer scalar (`x`) to the input port and transform it
according to
`function<class_VisualShaderNodeIntFunc_property_function>`{.interpreted-text
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

:::: {#enum_VisualShaderNodeIntFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeIntFunc_constant_FUNC_ABS}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_ABS** = `0`

Returns the absolute value of the parameter. Translates to `abs(x)` in
the Godot Shader Language.

:::: {#class_VisualShaderNodeIntFunc_constant_FUNC_NEGATE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_NEGATE** = `1`

Negates the `x` using `-(x)`.

:::: {#class_VisualShaderNodeIntFunc_constant_FUNC_SIGN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SIGN** = `2`

Extracts the sign of the parameter. Translates to `sign(x)` in the Godot
Shader Language.

:::: {#class_VisualShaderNodeIntFunc_constant_FUNC_BITWISE_NOT}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_BITWISE_NOT** = `3`

Returns the result of bitwise `NOT` operation on the integer. Translates
to `~a` in the Godot Shader Language.

:::: {#class_VisualShaderNodeIntFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `4`

Represents the size of the
`Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeIntFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
role="ref"} **function** = `2`
`🔗<class_VisualShaderNodeIntFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeIntFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

A function to be applied to the scalar.
