github_url
:   hide

# VisualShaderNodeCompare {#class_VisualShaderNodeCompare}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A comparison function for common types within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Compares `a` and `b` of
`type<class_VisualShaderNodeCompare_property_type>`{.interpreted-text
role="ref"} by
`function<class_VisualShaderNodeCompare_property_function>`{.interpreted-text
role="ref"}. Returns a boolean scalar. Translates to `if` instruction in
shader code.

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

:::: {#enum_VisualShaderNodeCompare_ComparisonType}
::: rst-class
classref-enumeration
:::
::::

enum **ComparisonType**:
`🔗<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_SCALAR}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_SCALAR** = `0`

A floating-point scalar.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_SCALAR_INT}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_SCALAR_INT** = `1`

An integer scalar.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_SCALAR_UINT}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_SCALAR_UINT** = `2`

An unsigned integer scalar.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_2D}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_VECTOR_2D** = `3`

A 2D vector type.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_3D}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_VECTOR_3D** = `4`

A 3D vector type.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_4D}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_VECTOR_4D** = `5`

A 4D vector type.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_BOOLEAN** = `6`

A boolean type.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_TRANSFORM** = `7`

A transform (`mat4`) type.

:::: {#class_VisualShaderNodeCompare_constant_CTYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **CTYPE_MAX** = `8`

Represents the size of the
`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeCompare_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeCompare_constant_FUNC_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **FUNC_EQUAL** = `0`

Comparison for equality (`a == b`).

:::: {#class_VisualShaderNodeCompare_constant_FUNC_NOT_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **FUNC_NOT_EQUAL** = `1`

Comparison for inequality (`a != b`).

:::: {#class_VisualShaderNodeCompare_constant_FUNC_GREATER_THAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **FUNC_GREATER_THAN** = `2`

Comparison for greater than (`a > b`). Cannot be used if
`type<class_VisualShaderNodeCompare_property_type>`{.interpreted-text
role="ref"} set to
`CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>`{.interpreted-text
role="ref"} or
`CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShaderNodeCompare_constant_FUNC_GREATER_THAN_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **FUNC_GREATER_THAN_EQUAL** = `3`

Comparison for greater than or equal (`a >= b`). Cannot be used if
`type<class_VisualShaderNodeCompare_property_type>`{.interpreted-text
role="ref"} set to
`CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>`{.interpreted-text
role="ref"} or
`CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShaderNodeCompare_constant_FUNC_LESS_THAN}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **FUNC_LESS_THAN** = `4`

Comparison for less than (`a < b`). Cannot be used if
`type<class_VisualShaderNodeCompare_property_type>`{.interpreted-text
role="ref"} set to
`CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>`{.interpreted-text
role="ref"} or
`CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShaderNodeCompare_constant_FUNC_LESS_THAN_EQUAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **FUNC_LESS_THAN_EQUAL** = `5`

Comparison for less than or equal (`a <= b`). Cannot be used if
`type<class_VisualShaderNodeCompare_property_type>`{.interpreted-text
role="ref"} set to
`CTYPE_BOOLEAN<class_VisualShaderNodeCompare_constant_CTYPE_BOOLEAN>`{.interpreted-text
role="ref"} or
`CTYPE_TRANSFORM<class_VisualShaderNodeCompare_constant_CTYPE_TRANSFORM>`{.interpreted-text
role="ref"}.

:::: {#class_VisualShaderNodeCompare_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `6`

Represents the size of the
`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeCompare_Condition}
::: rst-class
classref-enumeration
:::
::::

enum **Condition**:
`🔗<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeCompare_constant_COND_ALL}
::: rst-class
classref-enumeration-constant
:::
::::

`Condition<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
role="ref"} **COND_ALL** = `0`

The result will be `true` if all components in the vector satisfy the
comparison condition.

:::: {#class_VisualShaderNodeCompare_constant_COND_ANY}
::: rst-class
classref-enumeration-constant
:::
::::

`Condition<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
role="ref"} **COND_ANY** = `1`

The result will be `true` if any component in the vector satisfies the
comparison condition.

:::: {#class_VisualShaderNodeCompare_constant_COND_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Condition<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
role="ref"} **COND_MAX** = `2`

Represents the size of the
`Condition<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeCompare_property_condition}
::: rst-class
classref-property
:::
::::

`Condition<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
role="ref"} **condition** = `0`
`🔗<class_VisualShaderNodeCompare_property_condition>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_condition**(value:
  `Condition<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
  role="ref"})
- `Condition<enum_VisualShaderNodeCompare_Condition>`{.interpreted-text
  role="ref"} **get_condition**()

Extra condition which is applied if
`type<class_VisualShaderNodeCompare_property_type>`{.interpreted-text
role="ref"} is set to
`CTYPE_VECTOR_3D<class_VisualShaderNodeCompare_constant_CTYPE_VECTOR_3D>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeCompare_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeCompare_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeCompare_Function>`{.interpreted-text
  role="ref"} **get_function**()

A comparison function.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeCompare_property_type}
::: rst-class
classref-property
:::
::::

`ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
role="ref"} **type** = `0`
`🔗<class_VisualShaderNodeCompare_property_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_comparison_type**(value:
  `ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
  role="ref"})
- `ComparisonType<enum_VisualShaderNodeCompare_ComparisonType>`{.interpreted-text
  role="ref"} **get_comparison_type**()

The type to be used in the comparison.
