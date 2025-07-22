github_url
:   hide

# VisualShaderNodeTextureParameter {#class_VisualShaderNodeTextureParameter}

**Inherits:**
`VisualShaderNodeParameter<class_VisualShaderNodeParameter>`{.interpreted-text
role="ref"} **\<**
`VisualShaderNode<class_VisualShaderNode>`{.interpreted-text role="ref"}
**\<** `Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

**Inherited By:**
`VisualShaderNodeCubemapParameter<class_VisualShaderNodeCubemapParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeTexture2DArrayParameter<class_VisualShaderNodeTexture2DArrayParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeTexture2DParameter<class_VisualShaderNodeTexture2DParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeTexture3DParameter<class_VisualShaderNodeTexture3DParameter>`{.interpreted-text
role="ref"},
`VisualShaderNodeTextureParameterTriplanar<class_VisualShaderNodeTextureParameterTriplanar>`{.interpreted-text
role="ref"}

Performs a uniform texture lookup within the visual shader graph.

::: rst-class
classref-introduction-group
:::

## Description

Performs a lookup operation on the texture provided as a uniform for the
shader.

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

:::: {#enum_VisualShaderNodeTextureParameter_TextureType}
::: rst-class
classref-enumeration
:::
::::

enum **TextureType**:
`🔗<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTextureParameter_constant_TYPE_DATA}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"} **TYPE_DATA** = `0`

No hints are added to the uniform declaration.

:::: {#class_VisualShaderNodeTextureParameter_constant_TYPE_COLOR}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"} **TYPE_COLOR** = `1`

Adds `source_color` as hint to the uniform declaration for proper sRGB
to linear conversion.

:::: {#class_VisualShaderNodeTextureParameter_constant_TYPE_NORMAL_MAP}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"} **TYPE_NORMAL_MAP** = `2`

Adds `hint_normal` as hint to the uniform declaration, which internally
converts the texture for proper usage as normal map.

:::: {#class_VisualShaderNodeTextureParameter_constant_TYPE_ANISOTROPY}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"} **TYPE_ANISOTROPY** = `3`

Adds `hint_anisotropy` as hint to the uniform declaration to use for a
flowmap.

:::: {#class_VisualShaderNodeTextureParameter_constant_TYPE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"} **TYPE_MAX** = `4`

Represents the size of the
`TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeTextureParameter_ColorDefault}
::: rst-class
classref-enumeration
:::
::::

enum **ColorDefault**:
`🔗<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_WHITE}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
role="ref"} **COLOR_DEFAULT_WHITE** = `0`

Defaults to fully opaque white color.

:::: {#class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_BLACK}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
role="ref"} **COLOR_DEFAULT_BLACK** = `1`

Defaults to fully opaque black color.

:::: {#class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_TRANSPARENT}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
role="ref"} **COLOR_DEFAULT_TRANSPARENT** = `2`

Defaults to fully transparent black color.

:::: {#class_VisualShaderNodeTextureParameter_constant_COLOR_DEFAULT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
role="ref"} **COLOR_DEFAULT_MAX** = `3`

Represents the size of the
`ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeTextureParameter_TextureFilter}
::: rst-class
classref-enumeration
:::
::::

enum **TextureFilter**:
`🔗<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_DEFAULT** = `0`

Sample the texture using the filter determined by the node this shader
is attached to.

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_NEAREST** = `1`

The texture filter reads from the nearest pixel only. This makes the
texture look pixelated from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_LINEAR** = `2`

The texture filter blends between the nearest 4 pixels. This makes the
texture look smooth from up close, and grainy from a distance (due to
mipmaps not being sampled).

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST_MIPMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_NEAREST_MIPMAP** = `3`

The texture filter reads from the nearest pixel and blends between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look pixelated from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR_MIPMAP}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_LINEAR_MIPMAP** = `4`

The texture filter blends between the nearest 4 pixels and between the
nearest 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`). This makes the texture look smooth from up
close, and smooth from a distance.

Use this for non-pixel art textures that may be viewed at a low scale
(e.g. due to `Camera2D<class_Camera2D>`{.interpreted-text role="ref"}
zoom or sprite scaling), as mipmaps are important to smooth out pixels
that are smaller than on-screen pixels.

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST_MIPMAP_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_NEAREST_MIPMAP_ANISOTROPIC** = `5`

The texture filter reads from the nearest pixel and blends between 2
mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`) based on the angle between the surface and the
camera view. This makes the texture look pixelated from up close, and
smooth from a distance. Anisotropic filtering improves texture quality
on surfaces that are almost in line with the camera, but is slightly
slower. The anisotropic filtering level can be changed by adjusting
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This texture filter is rarely useful in 2D projects.
`FILTER_NEAREST_MIPMAP<class_VisualShaderNodeTextureParameter_constant_FILTER_NEAREST_MIPMAP>`{.interpreted-text
role="ref"} is usually more appropriate in this case.

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR_MIPMAP_ANISOTROPIC}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_LINEAR_MIPMAP_ANISOTROPIC** = `6`

The texture filter blends between the nearest 4 pixels and blends
between 2 mipmaps (or uses the nearest mipmap if
`ProjectSettings.rendering/textures/default_filters/use_nearest_mipmap_filter<class_ProjectSettings_property_rendering/textures/default_filters/use_nearest_mipmap_filter>`{.interpreted-text
role="ref"} is `true`) based on the angle between the surface and the
camera view. This makes the texture look smooth from up close, and
smooth from a distance. Anisotropic filtering improves texture quality
on surfaces that are almost in line with the camera, but is slightly
slower. The anisotropic filtering level can be changed by adjusting
`ProjectSettings.rendering/textures/default_filters/anisotropic_filtering_level<class_ProjectSettings_property_rendering/textures/default_filters/anisotropic_filtering_level>`{.interpreted-text
role="ref"}.

\*\*Note:\*\* This texture filter is rarely useful in 2D projects.
`FILTER_LINEAR_MIPMAP<class_VisualShaderNodeTextureParameter_constant_FILTER_LINEAR_MIPMAP>`{.interpreted-text
role="ref"} is usually more appropriate in this case.

:::: {#class_VisualShaderNodeTextureParameter_constant_FILTER_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **FILTER_MAX** = `7`

Represents the size of the
`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeTextureParameter_TextureRepeat}
::: rst-class
classref-enumeration
:::
::::

enum **TextureRepeat**:
`🔗<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTextureParameter_constant_REPEAT_DEFAULT}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
role="ref"} **REPEAT_DEFAULT** = `0`

Sample the texture using the repeat mode determined by the node this
shader is attached to.

:::: {#class_VisualShaderNodeTextureParameter_constant_REPEAT_ENABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
role="ref"} **REPEAT_ENABLED** = `1`

Texture will repeat normally.

:::: {#class_VisualShaderNodeTextureParameter_constant_REPEAT_DISABLED}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
role="ref"} **REPEAT_DISABLED** = `2`

Texture will not repeat.

:::: {#class_VisualShaderNodeTextureParameter_constant_REPEAT_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
role="ref"} **REPEAT_MAX** = `3`

Represents the size of the
`TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#enum_VisualShaderNodeTextureParameter_TextureSource}
::: rst-class
classref-enumeration
:::
::::

enum **TextureSource**:
`🔗<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"}

:::: {#class_VisualShaderNodeTextureParameter_constant_SOURCE_NONE}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"} **SOURCE_NONE** = `0`

The texture source is not specified in the shader.

:::: {#class_VisualShaderNodeTextureParameter_constant_SOURCE_SCREEN}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"} **SOURCE_SCREEN** = `1`

The texture source is the screen texture which captures all opaque
objects drawn this frame.

:::: {#class_VisualShaderNodeTextureParameter_constant_SOURCE_DEPTH}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"} **SOURCE_DEPTH** = `2`

The texture source is the depth texture from the depth prepass.

:::: {#class_VisualShaderNodeTextureParameter_constant_SOURCE_NORMAL_ROUGHNESS}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"} **SOURCE_NORMAL_ROUGHNESS** = `3`

The texture source is the normal-roughness buffer from the depth
prepass.

:::: {#class_VisualShaderNodeTextureParameter_constant_SOURCE_MAX}
::: rst-class
classref-enumeration-constant
:::
::::

`TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"} **SOURCE_MAX** = `4`

Represents the size of the
`TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"} enum.

::: rst-class
classref-section-separator
:::

------------------------------------------------------------------------

::: rst-class
classref-descriptions-group
:::

## Property Descriptions

:::: {#class_VisualShaderNodeTextureParameter_property_color_default}
::: rst-class
classref-property
:::
::::

`ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
role="ref"} **color_default** = `0`
`🔗<class_VisualShaderNodeTextureParameter_property_color_default>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_color_default**(value:
  `ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
  role="ref"})
- `ColorDefault<enum_VisualShaderNodeTextureParameter_ColorDefault>`{.interpreted-text
  role="ref"} **get_color_default**()

Sets the default color if no texture is assigned to the uniform.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeTextureParameter_property_texture_filter}
::: rst-class
classref-property
:::
::::

`TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
role="ref"} **texture_filter** = `0`
`🔗<class_VisualShaderNodeTextureParameter_property_texture_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_filter**(value:
  `TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
  role="ref"})
- `TextureFilter<enum_VisualShaderNodeTextureParameter_TextureFilter>`{.interpreted-text
  role="ref"} **get_texture_filter**()

Sets the texture filtering mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeTextureParameter_property_texture_repeat}
::: rst-class
classref-property
:::
::::

`TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
role="ref"} **texture_repeat** = `0`
`🔗<class_VisualShaderNodeTextureParameter_property_texture_repeat>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_repeat**(value:
  `TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
  role="ref"})
- `TextureRepeat<enum_VisualShaderNodeTextureParameter_TextureRepeat>`{.interpreted-text
  role="ref"} **get_texture_repeat**()

Sets the texture repeating mode.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeTextureParameter_property_texture_source}
::: rst-class
classref-property
:::
::::

`TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
role="ref"} **texture_source** = `0`
`🔗<class_VisualShaderNodeTextureParameter_property_texture_source>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_source**(value:
  `TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
  role="ref"})
- `TextureSource<enum_VisualShaderNodeTextureParameter_TextureSource>`{.interpreted-text
  role="ref"} **get_texture_source**()

Sets the texture source mode. Used for reading from the screen, depth,
or normal_roughness texture.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_VisualShaderNodeTextureParameter_property_texture_type}
::: rst-class
classref-property
:::
::::

`TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
role="ref"} **texture_type** = `0`
`🔗<class_VisualShaderNodeTextureParameter_property_texture_type>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_type**(value:
  `TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
  role="ref"})
- `TextureType<enum_VisualShaderNodeTextureParameter_TextureType>`{.interpreted-text
  role="ref"} **get_texture_type**()

Defines the type of data provided by the source texture.
