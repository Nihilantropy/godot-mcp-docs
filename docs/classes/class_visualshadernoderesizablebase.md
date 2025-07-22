github_url
:   hide

# VisualShaderNodeResizableBase {#class_VisualShaderNodeResizableBase}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeCurveTexture<class_VisualShaderNodeCurveTexture>`{.interpreted-text
role="ref"},
`VisualShaderNodeCurveXYZTexture<class_VisualShaderNodeCurveXYZTexture>`{.interpreted-text
role="ref"},
`VisualShaderNodeFrame<class_VisualShaderNodeFrame>`{.interpreted-text
role="ref"},
`VisualShaderNodeGroupBase<class_VisualShaderNodeGroupBase>`{.interpreted-text
role="ref"}

Base class for resizable nodes in a visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Resizable nodes have a handle that allows the user to adjust their size
as needed.

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

:::: {#class_VisualShaderNodeResizableBase_property_size}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **size** =
`Vector2(0, 0)`
`🔗<class_VisualShaderNodeResizableBase_property_size>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_size**(value: `Vector2<class_Vector2>`{.interpreted-text
  role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"} **get_size**()

The size of the node in the visual shader graph.
