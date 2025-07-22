github_url
:   hide

# VisualShaderNodeUVFunc {#class_VisualShaderNodeUVFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Contains functions to modify texture coordinates (`uv`) to be used
within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

UV functions are similar to `Vector2<class_Vector2>`{.interpreted-text
role="ref"} functions, but the input port of this node uses the
shader\'s UV value by default.

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

:::: {#enum_VisualShaderNodeUVFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeUVFunc_constant_FUNC_PANNING}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text
role="ref"} **FUNC_PANNING** = `0`

Translates `uv` by using `scale` and `offset` values using the following
formula: `uv = uv + offset * scale`. `uv` port is connected to `UV`
built-in by default.

:::: {#class_VisualShaderNodeUVFunc_constant_FUNC_SCALING}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text
role="ref"} **FUNC_SCALING** = `1`

Scales `uv` by using `scale` and `pivot` values using the following
formula: `uv = (uv - pivot) * scale + pivot`. `uv` port is connected to
`UV` built-in by default.

:::: {#class_VisualShaderNodeUVFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `2`

Represents the size of the
`Function<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeUVFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeUVFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeUVFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

A function to be applied to the texture coordinates.
