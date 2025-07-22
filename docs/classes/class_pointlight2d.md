github_url
:   hide

::: {.meta keywords="omni, spot"}
:::

# PointLight2D {#class_PointLight2D}

**Inherits:** `Light2D<class_Light2D>`{.interpreted-text role="ref"}
**\<** `Node2D<class_Node2D>`{.interpreted-text role="ref"} **\<**
`CanvasItem<class_CanvasItem>`{.interpreted-text role="ref"} **\<**
`Node<class_Node>`{.interpreted-text role="ref"} **\<**
`Object<class_Object>`{.interpreted-text role="ref"}

Positional 2D light source.

::: rst-class
classref-introduction-group
:::

## Description

Casts light in a 2D environment. This light\'s shape is defined by a
(usually grayscale) texture.

::: rst-class
classref-introduction-group
:::

## Tutorials

- `2D lights and shadows <../tutorials/2d/2d_lights_and_shadows>`{.interpreted-text
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

:::: {#class_PointLight2D_property_height}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **height** = `0.0`
`🔗<class_PointLight2D_property_height>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_height**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"} **get_height**()

The height of the light. Used with 2D normal mapping. The units are in
pixels, e.g. if the height is 100, then it will illuminate an object 100
pixels away at a 45° angle to the plane.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PointLight2D_property_offset}
::: rst-class
classref-property
:::
::::

`Vector2<class_Vector2>`{.interpreted-text role="ref"} **offset** =
`Vector2(0, 0)`
`🔗<class_PointLight2D_property_offset>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_offset**(value:
  `Vector2<class_Vector2>`{.interpreted-text role="ref"})
- `Vector2<class_Vector2>`{.interpreted-text role="ref"}
  **get_texture_offset**()

The offset of the light\'s
`texture<class_PointLight2D_property_texture>`{.interpreted-text
role="ref"}.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PointLight2D_property_texture}
::: rst-class
classref-property
:::
::::

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} **texture**
`🔗<class_PointLight2D_property_texture>`{.interpreted-text role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture**(value: `Texture2D<class_Texture2D>`{.interpreted-text
  role="ref"})
- `Texture2D<class_Texture2D>`{.interpreted-text role="ref"}
  **get_texture**()

`Texture2D<class_Texture2D>`{.interpreted-text role="ref"} used for the
light\'s appearance.

::: rst-class
classref-item-separator
:::

------------------------------------------------------------------------

:::: {#class_PointLight2D_property_texture_scale}
::: rst-class
classref-property
:::
::::

`float<class_float>`{.interpreted-text role="ref"} **texture_scale** =
`1.0` `🔗<class_PointLight2D_property_texture_scale>`{.interpreted-text
role="ref"}

::: rst-class
classref-property-setget
:::

- `void (No return value.)`{.interpreted-text role="abbr"}
  **set_texture_scale**(value: `float<class_float>`{.interpreted-text
  role="ref"})
- `float<class_float>`{.interpreted-text role="ref"}
  **get_texture_scale**()

The `texture<class_PointLight2D_property_texture>`{.interpreted-text
role="ref"}\'s scale factor.
