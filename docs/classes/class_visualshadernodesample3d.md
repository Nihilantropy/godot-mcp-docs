github_url
:   hide

# VisualShaderNodeSample3D {#class_VisualShaderNodeSample3D}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeTexture2DArray<class_VisualShaderNodeTexture2DArray>`{.interpreted-text
role="ref"},
`VisualShaderNodeTexture3D<class_VisualShaderNodeTexture3D>`{.interpreted-text
role="ref"}

A base node for nodes which samples 3D textures in the visual shader
graph.

::: rst-class
classref-introduction-group
:::

## Description

A virtual class, use the descendants instead.

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

:::: {#enum_VisualShaderNodeSample3D_Source}
::: rst-class
classref-enumeration
:::
::::

enum **Source**:
`🔗<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeSample3D_constant_SOURCE_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text
role="ref"} **SOURCE_TEXTURE** = `0`

Creates internal uniform and provides a way to assign it within node.

:::: {#class_VisualShaderNodeSample3D_constant_SOURCE_PORT}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text
role="ref"} **SOURCE_PORT** = `1`

Use the uniform texture from sampler port.

:::: {#class_VisualShaderNodeSample3D_constant_SOURCE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text
role="ref"} **SOURCE_MAX** = `2`

Represents the size of the
`Source<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeSample3D_property_source}
::: rst-class
classref-property
:::
::::

`Source<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text
role="ref"} **source** = `0`
`🔗<class_VisualShaderNodeSample3D_property_source>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source**(value:
  `Source<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text
  role="ref"})
- `Source<enum_VisualShaderNodeSample3D_Source>`{.interpreted-text
  role="ref"} **get_source**()

An input source type.
