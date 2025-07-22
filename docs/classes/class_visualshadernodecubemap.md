github_url
:   hide

# VisualShaderNodeCubemap {#class_VisualShaderNodeCubemap}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

A `Cubemap<class_Cubemap>`{.interpreted-text role="ref"} sampling node
to be used within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Translated to `texture(cubemap, vec3)` in the shader language. Returns a
color vector and alpha channel as scalar.

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

:::: {#enum_VisualShaderNodeCubemap_Source}
::: rst-class
classref-enumeration
:::
::::

enum **Source**:
`🔗<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeCubemap_constant_SOURCE_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text
role="ref"} **SOURCE_TEXTURE** = `0`

Use the `Cubemap<class_Cubemap>`{.interpreted-text role="ref"} set via
`cube_map<class_VisualShaderNodeCubemap_property_cube_map>`{.interpreted-text
role="ref"}. If this is set to
`source<class_VisualShaderNodeCubemap_property_source>`{.interpreted-text
role="ref"}, the `samplerCube` port is ignored.

:::: {#class_VisualShaderNodeCubemap_constant_SOURCE_PORT}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text
role="ref"} **SOURCE_PORT** = `1`

Use the `Cubemap<class_Cubemap>`{.interpreted-text role="ref"} sampler
reference passed via the `samplerCube` port. If this is set to
`source<class_VisualShaderNodeCubemap_property_source>`{.interpreted-text
role="ref"}, the
`cube_map<class_VisualShaderNodeCubemap_property_cube_map>`{.interpreted-text
role="ref"} texture is ignored.

:::: {#class_VisualShaderNodeCubemap_constant_SOURCE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text
role="ref"} **SOURCE_MAX** = `2`

Represents the size of the
`Source<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeCubemap_TextureType}
::: rst-class
classref-enumeration
:::
::::

enum **TextureType**:
`🔗<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeCubemap_constant_TYPE_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
role="ref"} **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

:::: {#class_VisualShaderNodeCubemap_constant_TYPE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
role="ref"} **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper sRGB
to linear conversion.

:::: {#class_VisualShaderNodeCubemap_constant_TYPE_NORMAL_MAP}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
role="ref"} **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally
converts the texture for proper usage as normal map.

:::: {#class_VisualShaderNodeCubemap_constant_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
role="ref"} **TYPE_MAX** = `3`

Represents the size of the
`TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeCubemap_property_cube_map}
::: rst-class
classref-property
:::
::::

`TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
**cube_map**
`🔗<class_VisualShaderNodeCubemap_property_cube_map>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_cube_map**(value:
  `TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"})
- `TextureLayered<class_TextureLayered>`{.interpreted-text role="ref"}
  **get_cube_map**()

The `Cubemap<class_Cubemap>`{.interpreted-text role="ref"} texture to
sample when using
`SOURCE_TEXTURE<class_VisualShaderNodeCubemap_constant_SOURCE_TEXTURE>`{.interpreted-text
role="ref"} as
`source<class_VisualShaderNodeCubemap_property_source>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeCubemap_property_source}
::: rst-class
classref-property
:::
::::

`Source<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text
role="ref"} **source** = `0`
`🔗<class_VisualShaderNodeCubemap_property_source>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source**(value:
  `Source<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text
  role="ref"})
- `Source<enum_VisualShaderNodeCubemap_Source>`{.interpreted-text
  role="ref"} **get_source**()

Defines which source should be used for the sampling.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeCubemap_property_texture_type}
::: rst-class
classref-property
:::
::::

`TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
role="ref"} **texture_type** = `0`
`🔗<class_VisualShaderNodeCubemap_property_texture_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_type**(value:
  `TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
  role="ref"})
- `TextureType<enum_VisualShaderNodeCubemap_TextureType>`{.interpreted-text
  role="ref"} **get_texture_type**()

Defines the type of data provided by the source texture.
