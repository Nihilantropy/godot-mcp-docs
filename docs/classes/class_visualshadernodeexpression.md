github_url
:   hide

# VisualShaderNodeExpression {#class_VisualShaderNodeExpression}

**Inherits:**
`VisualShaderNodeGroupBase<class_VisualShaderNodeGroupBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNodeResizableBase<class_VisualShaderNodeResizableBase>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeGlobalExpression<class_VisualShaderNodeGlobalExpression>`{.interpreted-text
role="ref"}

A custom visual shader graph expression written in Godot Shading
Language.

::: rst-class
classref-introduction-group
:::

## Description

Custom Godot Shading Language expression, with a custom number of input
and output ports.

The provided code is directly injected into the graph\'s matching shader
function (`vertex`, `fragment`, or `light`), so it cannot be used to
declare functions, varyings, uniforms, or global constants. See
`VisualShaderNodeGlobalExpression<class_VisualShaderNodeGlobalExpression>`{.interpreted-text
role="ref"} for such global definitions.

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

:::: {#class_VisualShaderNodeExpression_property_expression}
::: rst-class
classref-property
:::
::::

`String<class_String>`{.interpreted-text role="ref"} **expression** =
`""`
`🔗<class_VisualShaderNodeExpression_property_expression>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_expression**(value: `String<class_String>`{.interpreted-text
  role="ref"})
- `String<class_String>`{.interpreted-text role="ref"}
  **get_expression**()

An expression in Godot Shading Language, which will be injected at the
start of the graph\'s matching shader function (`vertex`, `fragment`, or
`light`), and thus cannot be used to declare functions, varyings,
uniforms, or global constants.
