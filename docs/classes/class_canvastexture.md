github_url
:   hide

# CanvasTexture {#class_CanvasTexture}

**Inherits:** `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**\<** `Texture<class_Texture>`{.interpreted-text role="ref"} **\<**
`Resource<class_Resource>`{.interpreted-text role="ref"} **\<**
`RefCounted<class_RefCounted>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Texture with optional normal and specular maps for use in 2D rendering.

::: rst-class
classref-introduction-group
:::

## Description

**CanvasTexture** is an alternative to
`ImageTexture<class_ImageTexture>`{.interpreted-text role="ref"} for 2D
rendering. It allows using normal maps and specular maps in any node
that inherits from `CanvasItem<class_CanvasItem>`{.interpreted-text
role="ref"}. **CanvasTexture** also allows overriding the texture\'s
filter and repeat mode independently of the node\'s properties (or the
project settings).

\*\*Note:\*\* **CanvasTexture** cannot be used in 3D. It will not
display correctly when applied to any
`VisualInstance3D<class_VisualInstance3D>`{.interpreted-text
role="ref"}, such as `Sprite3D<class_Sprite3D>`{.interpreted-text
role="ref"} or `Decal<class_Decal>`{.interpreted-text role="ref"}. For
physically-based materials in 3D, use
`BaseMaterial3D<class_BaseMaterial3D>`{.interpreted-text role="ref"}
instead.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D Lights and Shadows <../tutorials/2d/2d_lights_and_shadows>`{.interpreted-text
  role="doc"}

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

:::: {#class_CanvasTexture_property_diffuse_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**diffuse_texture**
`🔗<class_CanvasTexture_property_diffuse_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_diffuse_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_diffuse_texture**()

The diffuse (color) texture to use. This is the main texture you want to
set in most cases.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasTexture_property_normal_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**normal_texture**
`🔗<class_CanvasTexture_property_normal_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_normal_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_normal_texture**()

The normal map texture to use. Only has a visible effect if
`Light2D<class_Light2D>`{.interpreted-text role="ref"}s are affecting
this **CanvasTexture**.

\*\*Note:\*\* Godot expects the normal map to use X+, Y+, and Z+
coordinates. See [this
page](http://wiki.polycount.com/wiki/Normal_Map_Technical_Details#Common_Swizzle_Coordinates)
for a comparison of normal map coordinates expected by popular engines.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasTexture_property_specular_color}
::: rst-class
classref-property
:::
::::

`Color<class_Color>`{.interpreted-text role="ref"} **specular_color** =
`Color(1, 1, 1, 1)`
`🔗<class_CanvasTexture_property_specular_color>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_specular_color**(value: `Color<class_Color>`{.interpreted-text
  role="ref"})
- `Color<class_Color>`{.interpreted-text role="ref"}
  **get_specular_color**()

The multiplier for specular reflection colors. The
`Light2D<class_Light2D>`{.interpreted-text role="ref"}\'s color is also
taken into account when determining the reflection color. Only has a
visible effect if `Light2D<class_Light2D>`{.interpreted-text
role="ref"}s are affecting this **CanvasTexture**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasTexture_property_specular_shininess}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"}
**specular_shininess** = `1.0`
`🔗<class_CanvasTexture_property_specular_shininess>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_specular_shininess**(value:
  `float<class_float>`{.interpreted-text role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_specular_shininess**()

The specular exponent for `Light2D<class_Light2D>`{.interpreted-text
role="ref"} specular reflections. Higher values result in a more
glossy/\"wet\" look, with reflections becoming more localized and less
visible overall. The default value of `1.0` disables specular
reflections entirely. Only has a visible effect if
`Light2D<class_Light2D>`{.interpreted-text role="ref"}s are affecting
this **CanvasTexture**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasTexture_property_specular_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
**specular_texture**
`🔗<class_CanvasTexture_property_specular_texture>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_specular_texture**(value:
  `Texture2D<class_Texture2D>`{.interpreted-text role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_specular_texture**()

The specular map to use for `Light2D<class_Light2D>`{.interpreted-text
role="ref"} specular reflections. This should be a grayscale or colored
texture, with brighter areas resulting in a higher
`specular_shininess<class_CanvasTexture_property_specular_shininess>`{.interpreted-text
role="ref"} value. Using a colored
`specular_texture<class_CanvasTexture_property_specular_texture>`{.interpreted-text
role="ref"} allows controlling specular shininess on a per-channel
basis. Only has a visible effect if
`Light2D<class_Light2D>`{.interpreted-text role="ref"}s are affecting
this **CanvasTexture**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasTexture_property_texture_filter}
::: rst-class
classref-property
:::
::::

`TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
role="ref"} **texture_filter** = `0`
`🔗<class_CanvasTexture_property_texture_filter>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_filter**(value:
  `TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
  role="ref"})
- `TextureFilter<enum_CanvasItem_TextureFilter>`{.interpreted-text
  role="ref"} **get_texture_filter**()

The texture filtering mode to use when drawing this **CanvasTexture**.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_CanvasTexture_property_texture_repeat}
::: rst-class
classref-property
:::
::::

`TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
role="ref"} **texture_repeat** = `0`
`🔗<class_CanvasTexture_property_texture_repeat>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_repeat**(value:
  `TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
  role="ref"})
- `TextureRepeat<enum_CanvasItem_TextureRepeat>`{.interpreted-text
  role="ref"} **get_texture_repeat**()

The texture repeat mode to use when drawing this **CanvasTexture**.
