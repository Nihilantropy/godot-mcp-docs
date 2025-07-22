github_url
:   hide

# VisualShaderNodeTransformFunc {#class_VisualShaderNodeTransformFunc}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Computes a `Transform3D<class_Transform3D>`{.interpreted-text
role="ref"} function within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Computes an inverse or transpose function on the provided
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"}.

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

:::: {#enum_VisualShaderNodeTransformFunc_Function}
::: rst-class
classref-enumeration
:::
::::

enum **Function**:
`🔗<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTransformFunc_constant_FUNC_INVERSE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
role="ref"} **FUNC_INVERSE** = `0`

Perform the inverse operation on the
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} matrix.

:::: {#class_VisualShaderNodeTransformFunc_constant_FUNC_TRANSPOSE}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
role="ref"} **FUNC_TRANSPOSE** = `1`

Perform the transpose operation on the
`Transform3D<class_Transform3D>`{.interpreted-text role="ref"} matrix.

:::: {#class_VisualShaderNodeTransformFunc_constant_FUNC_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Function<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
role="ref"} **FUNC_MAX** = `2`

Represents the size of the
`Function<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeTransformFunc_property_function}
::: rst-class
classref-property
:::
::::

`Function<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
role="ref"} **function** = `0`
`🔗<class_VisualShaderNodeTransformFunc_property_function>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_function**(value:
  `Function<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
  role="ref"})
- `Function<enum_VisualShaderNodeTransformFunc_Function>`{.interpreted-text
  role="ref"} **get_function**()

The function to be computed.
