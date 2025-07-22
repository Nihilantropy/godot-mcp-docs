github_url
:   hide

# VisualShaderNodeDerivativeFunc {#class_VisualShaderNodeDerivativeFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Calculates a derivative within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

This node is only available in `Fragment` and `Light` visual shaders.

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

:::: {#enum_VisualShaderNodeDerivativeFunc_OpType}
::: rst-class
classref-enumeration
:::
::::

enum **OpType**:
`🔗<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_SCALAR** = `0`

A floating-point scalar.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_2D** = `1`

A 2D vector type.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_3D** = `2`

A 3D vector type.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_VECTOR_4D** = `3`

A 4D vector type.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_OP_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"} **OP_TYPE_MAX** = `4`

Represents the size of the
`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeDerivativeFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeDerivativeFunc_constant_FUNC_SUM}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SUM** = `0`

Sum of absolute derivative in `x` and `y`.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_FUNC_X}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
role="ref"} **FUNC_X** = `1`

Derivative in `x` using local differencing.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_FUNC_Y}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
role="ref"} **FUNC_Y** = `2`

Derivative in `y` using local differencing.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `3`

Represents the size of the
`Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeDerivativeFunc_Precision}
::: rst-class
classref-enumeration
:::
::::

enum **Precision**:
`🔗<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeDerivativeFunc_constant_PRECISION_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
role="ref"} **PRECISION_NONE** = `0`

No precision is specified, the GPU driver is allowed to use whatever
level of precision it chooses. This is the default option and is
equivalent to using `dFdx()` or `dFdy()` in text shaders.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_PRECISION_COARSE}
::: rst-class
classref-enumeration-constant
:::
::::

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
role="ref"} **PRECISION_COARSE** = `1`

The derivative will be calculated using the current fragment\'s
neighbors (which may not include the current fragment). This tends to be
faster than using
`PRECISION_FINE<class_VisualShaderNodeDerivativeFunc_constant_PRECISION_FINE>`{.interpreted-text
role="ref"}, but may not be suitable when more precision is needed. This
is equivalent to using `dFdxCoarse()` or `dFdyCoarse()` in text shaders.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_PRECISION_FINE}
::: rst-class
classref-enumeration-constant
:::
::::

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
role="ref"} **PRECISION_FINE** = `2`

The derivative will be calculated using the current fragment and its
immediate neighbors. This tends to be slower than using
`PRECISION_COARSE<class_VisualShaderNodeDerivativeFunc_constant_PRECISION_COARSE>`{.interpreted-text
role="ref"}, but may be necessary when more precision is needed. This is
equivalent to using `dFdxFine()` or `dFdyFine()` in text shaders.

:::: {#class_VisualShaderNodeDerivativeFunc_constant_PRECISION_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
role="ref"} **PRECISION_MAX** = `3`

Represents the size of the
`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeDerivativeFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeDerivativeFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeDerivativeFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

A derivative function type.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeDerivativeFunc_property_op_type}
::: rst-class
classref-property
:::
::::

`OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
role="ref"} **op_type** = `0`
`🔗<class_VisualShaderNodeDerivativeFunc_property_op_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_op_type**(value:
  `OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
  role="ref"})
- `OpType<enum_VisualShaderNodeDerivativeFunc_OpType>`{.interpreted-text
  role="ref"} **get_op_type**()

A type of operands and returned value.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeDerivativeFunc_property_precision}
::: rst-class
classref-property
:::
::::

`Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
role="ref"} **precision** = `0`
`🔗<class_VisualShaderNodeDerivativeFunc_property_precision>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_precision**(value:
  `Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
  role="ref"})
- `Precision<enum_VisualShaderNodeDerivativeFunc_Precision>`{.interpreted-text
  role="ref"} **get_precision**()

Sets the level of precision to use for the derivative function. When
using the Compatibility renderer, this setting has no effect.
