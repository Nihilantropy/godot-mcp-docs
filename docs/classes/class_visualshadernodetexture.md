github_url
:   hide

# VisualShaderNodeTexture {#class_VisualShaderNodeTexture}

**Inherits:**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Performs a 2D texture lookup within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Performs a lookup operation on the provided texture, with support for
multiple texture sources to choose from.

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

:::: {#enum_VisualShaderNodeTexture_Source}
::: rst-class
classref-enumeration
:::
::::

enum **Source**:
`🔗<enum_VisualShaderNodeTexture_Source>`{.interpreted-text role="ref"}

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_TEXTURE** = `0`

Use the texture given as an argument for this function.

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_SCREEN** = `1`

Use the current viewport\'s texture as the source.

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_2D_TEXTURE}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_2D_TEXTURE** = `2`

Use the texture from this shader\'s texture built-in (e.g. a texture of
a `Sprite2D<class_Sprite2D>`{.interpreted-text role="ref"}).

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_2D_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_2D_NORMAL** = `3`

Use the texture from this shader\'s normal map built-in.

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_DEPTH** = `4`

Use the depth texture captured during the depth prepass. Only available
when the depth prepass is used (i.e. in spatial shaders and in the
forward_plus or gl_compatibility renderers).

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_PORT}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_PORT** = `5`

Use the texture provided in the input port for this function.

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_3D_NORMAL}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_3D_NORMAL** = `6`

Use the normal buffer captured during the depth prepass. Only available
when the normal-roughness buffer is available (i.e. in spatial shaders
and in the forward_plus renderer).

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_ROUGHNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_ROUGHNESS** = `7`

Use the roughness buffer captured during the depth prepass. Only
available when the normal-roughness buffer is available (i.e. in spatial
shaders and in the forward_plus renderer).

:::: {#class_VisualShaderNodeTexture_constant_SOURCE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **SOURCE_MAX** = `8`

Represents the size of the
`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeTexture_TextureType}
::: rst-class
classref-enumeration
:::
::::

enum **TextureType**:
`🔗<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTexture_constant_TYPE_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
role="ref"} **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

:::: {#class_VisualShaderNodeTexture_constant_TYPE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
role="ref"} **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper sRGB
to linear conversion.

:::: {#class_VisualShaderNodeTexture_constant_TYPE_NORMAL_MAP}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
role="ref"} **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally
converts the texture for proper usage as normal map.

:::: {#class_VisualShaderNodeTexture_constant_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
role="ref"} **TYPE_MAX** = `3`

Represents the size of the
`TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeTexture_property_source}
::: rst-class
classref-property
:::
::::

`Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
role="ref"} **source** = `0`
`🔗<class_VisualShaderNodeTexture_property_source>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_source**(value:
  `Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
  role="ref"})
- `Source<enum_VisualShaderNodeTexture_Source>`{.interpreted-text
  role="ref"} **get_source**()

Determines the source for the lookup.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeTexture_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_VisualShaderNodeTexture_property_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

The source texture, if needed for the selected
`source<class_VisualShaderNodeTexture_property_source>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeTexture_property_texture_type}
::: rst-class
classref-property
:::
::::

`TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
role="ref"} **texture_type** = `0`
`🔗<class_VisualShaderNodeTexture_property_texture_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_type**(value:
  `TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
  role="ref"})
- `TextureType<enum_VisualShaderNodeTexture_TextureType>`{.interpreted-text
  role="ref"} **get_texture_type**()

Specifies the type of the texture if
`source<class_VisualShaderNodeTexture_property_source>`{.interpreted-text
role="ref"} is set to
`SOURCE_TEXTURE<class_VisualShaderNodeTexture_constant_SOURCE_TEXTURE>`{.interpreted-text
role="ref"}.
